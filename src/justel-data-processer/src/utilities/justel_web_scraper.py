#!/usr/bin/env python3
"""
JUSTEL Legal Documents Web Scraper - High Performance Version

This script processes legal documents from a CSV file and downloads HTML content
from JUSTEL URLs using the fastest Python libraries for maximum speed.

Requirements:
- pandas
- httpx (fastest HTTP client)
- selectolax (fastest HTML parser)
- asyncio (for concurrent requests)

Usage:
    python justel_web_scraper.py [options]
"""

import os
import sys
import csv
import json
import re
import time
import logging
import argparse
import asyncio
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple, List, Dict, Set
from urllib.parse import urlparse, urljoin, parse_qs, urlencode

import pandas as pd
import httpx
from selectolax.parser import HTMLParser


class JustelScraper:
    """High-performance web scraper for JUSTEL legal documents using httpx and selectolax."""

    def __init__(self,
                 input_excel: str = "data/csv_data/full-list.csv",
                 output_dir: str = "input",
                 delay: float = 0.02,  # Reduced for maximum performance
                 concurrent_requests: int = 35,  # Optimized for Belgian eJustice servers
                 test_mode: bool = False,
                 test_limit: int = 20):
        """
        Initialize the scraper for comprehensive Belgian legal document processing.

        Args:
            input_excel: Path to Excel file with URLs (default: data/csv_data/full-list.csv)
            output_dir: Directory to save TXT files (default: input)
            delay: Delay between requests in seconds (optimized for full dataset)
            concurrent_requests: Number of concurrent requests (increased for scale)
            test_mode: Process only limited number of URLs for testing
            test_limit: Number of URLs to process in test mode
        """
        self.input_excel = input_excel
        self.output_dir = Path(output_dir)
        self.delay = delay
        self.concurrent_requests = concurrent_requests
        self.test_mode = test_mode
        self.test_limit = test_limit

        # Create output directory
        self.output_dir.mkdir(exist_ok=True, parents=True)

        # Setup checkpoint file for resume capability
        self.checkpoint_file = self.output_dir / "scraping_checkpoint.json"

        # Setup logging
        self.setup_logging()

        # HTTP client configuration optimized for maximum performance
        self.client_config = {
            'timeout': httpx.Timeout(25.0),  # Slightly reduced for faster failures
            'limits': httpx.Limits(
                max_connections=100,  # Increased for higher concurrency
                max_keepalive_connections=50,  # More persistent connections
                keepalive_expiry=30.0  # Keep connections alive longer
            ),
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }
        }

        # Statistics
        self.stats = {
            'total': 0,
            'successful': 0,
            'failed': 0,
            'skipped': 0,
            'duplicates_removed': 0,
            'original_rows': 0
        }
    
    def setup_logging(self):
        """Setup logging configuration."""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"justel_scraper_{timestamp}.log"

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def extract_legislation_id(self, url: str) -> Optional[str]:
        """
        Extract 10-digit legislation ID from JUSTEL URL.

        Args:
            url: JUSTEL URL

        Returns:
            10-digit ID or None if not found
        """
        if not url or pd.isna(url):
            return None

        # Pattern to match 10-digit numbers in the URL path
        patterns = [
            r'/(\d{10})/',      # ID in middle of path
            r'/(\d{10})$',      # ID at end of path
            r'=(\d{10})$',      # ID as parameter value
            r'numac=(\d{10})',  # ID in numac parameter
            r'/(\d{10})/justel' # ID before /justel
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)

        return None

    def extract_numac_search(self, url: str) -> Optional[str]:
        """
        Extract numac_search parameter from JUSTEL URL.
        
        Args:
            url: JUSTEL URL
            
        Returns:
            numac_search value or None if not found
        """
        if not url or pd.isna(url):
            return None
            
        try:
            # Parse URL and extract query parameters
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            
            # Get numac_search parameter
            numac_search = query_params.get('numac_search', [None])[0]
            
            if numac_search and len(numac_search) >= 8:  # Validate minimum length
                return numac_search
                
            return None
            
        except Exception as e:
            self.logger.warning(f"Error parsing URL {url}: {e}")
            return None

    def ensure_french_url(self, url: str) -> str:
        """
        Ensure the URL is configured for French content.
        
        Args:
            url: Original JUSTEL URL
            
        Returns:
            URL modified to ensure French content
        """
        if not url:
            return url
            
        try:
            # Parse URL and extract query parameters
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            
            # Ensure French language parameters
            query_params['language'] = ['fr']
            query_params['lg_txt'] = ['f']  # French text flag
            
            # Rebuild query string
            new_query = urlencode(query_params, doseq=True)
            
            # Rebuild URL
            french_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{new_query}"
            
            return french_url
            
        except Exception as e:
            self.logger.warning(f"Error modifying URL for French content {url}: {e}")
            return url

    def extract_french_url(self, html_content: str, base_url: str) -> Optional[str]:
        """
        Extract the French version URL from the HTML content.
        
        Args:
            html_content: HTML content of the page
            base_url: Base URL for relative URL resolution
            
        Returns:
            French URL or None if not found
        """
        try:
            # Parse HTML to find the French language button
            tree = HTMLParser(html_content)
            
            # Look for the French language button with active class or href containing language=fr
            french_selectors = [
                'a.nav__language-button.active[href*="language=fr"]',
                'a.nav__language-button[href*="language=fr"]',
                'a[href*="language=fr"][href*="lg_txt=f"]'
            ]
            
            for selector in french_selectors:
                french_links = tree.css(selector)
                if french_links:
                    href = french_links[0].attributes.get('href')
                    if href:
                        # Convert relative URL to absolute
                        if href.startswith('http'):
                            return href
                        else:
                            # Parse base URL to get the base domain
                            return urljoin(base_url, href)
                            
            return None
            
        except Exception as e:
            self.logger.warning(f"Error extracting French URL: {e}")
            return None

    def file_exists(self, legislation_id: str) -> bool:
        """Check if TXT file already exists for given legislation ID."""
        file_path = self.output_dir / f"{legislation_id}.txt"
        return file_path.exists()

    async def fetch_url_content(self, session: httpx.AsyncClient, url: str, legislation_id: str) -> bool:
        """
        Fetch content from URL with French validation and save as TXT file.

        Args:
            session: HTTP client session
            url: URL to fetch
            legislation_id: Document ID for filename

        Returns:
            True if successful, False otherwise
        """
        try:
            self.logger.info(f"📥 Fetching: {url}")

            # Ensure URL is configured for French content
            french_url = self.ensure_french_url(url)
            if french_url != url:
                self.logger.info(f"🇫🇷 Using French URL: {french_url}")

            # Make initial HTTP request
            response = await session.get(french_url, follow_redirects=True)
            response.raise_for_status()

            # Get HTML content
            html_content = response.text

            # Basic validation - check if content contains expected document ID
            if not self.validate_content(html_content, legislation_id):
                self.logger.warning(f"⚠️ Content validation failed for {legislation_id}")
                return False

            # Try to extract French URL from the HTML if not already French
            extracted_french_url = self.extract_french_url(html_content, french_url)
            
            if extracted_french_url and extracted_french_url != french_url:
                self.logger.info(f"🇫🇷 Found French version, fetching: {extracted_french_url}")
                
                # Fetch the French version
                french_response = await session.get(extracted_french_url, follow_redirects=True)
                french_response.raise_for_status()
                html_content = french_response.text
                
                # Validate French content
                if not self.validate_content(html_content, legislation_id):
                    self.logger.warning(f"⚠️ French content validation failed for {legislation_id}")
                    return False
            else:
                self.logger.info(f"ℹ️ Using original URL (French URL not found or same as original)")

            # Basic validation - check if content is not empty or too short
            if not html_content or len(html_content.strip()) < 500:
                self.logger.warning(f"⚠️ HTML content too short for {legislation_id}")
                return False

            # Save as TXT file (HTML content with .txt extension)
            file_path = self.output_dir / f"{legislation_id}.txt"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)

            self.logger.info(f"✅ Successfully saved {legislation_id}.txt")
            return True

        except Exception as e:
            self.logger.error(f"❌ Error fetching {url}: {e}")
            return False

    def validate_content(self, html_content: str, expected_doc_id: str) -> bool:
        """Validate that the scraped content contains the expected document ID."""
        # Check if content contains the expected document ID
        if expected_doc_id in html_content:
            # Also check it doesn't contain the corrupted document ID
            if '1994015214' not in html_content:
                return True
            else:
                self.logger.warning(f"⚠️ Content contains corrupted document 1994015214")
                return False
        else:
            self.logger.warning(f"⚠️ Content does not contain expected document ID {expected_doc_id}")
            return False


    
    async def process_url_batch(self, session: httpx.AsyncClient, url_batch: List[Tuple[str, str]]) -> None:
        """
        Process a batch of URLs concurrently.

        Args:
            session: httpx async client session
            url_batch: List of (url, legislation_id) tuples
        """
        tasks = []
        for url, legislation_id in url_batch:
            task = self.fetch_url_content(session, url, legislation_id)
            tasks.append(task)

        # Execute all tasks concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Update statistics
        for result in results:
            if isinstance(result, Exception):
                self.stats['failed'] += 1
            elif result:
                self.stats['successful'] += 1
            else:
                self.stats['failed'] += 1
    
    async def process_excel(self) -> None:
        """Process the Excel file and download HTML content using async requests."""
        try:
            # Read Excel file
            self.logger.info(f"Reading Excel file: {self.input_excel}")
            # Read CSV or Excel based on file extension
            if self.input_excel.endswith('.csv'):
                df = pd.read_csv(self.input_excel)
            else:
                df = pd.read_excel(self.input_excel)

            self.logger.info(f"Loaded Excel with {len(df)} rows")
            self.logger.info(f"Columns: {list(df.columns)}")

            # Extract numac_search from URLs
            self.logger.info("Extracting numac_search parameters from URLs...")
            url_numac_pairs = []
            
            for _, row in df.iterrows():
                url = row['URL']
                numac_search = self.extract_numac_search(url)
                
                if numac_search:
                    url_numac_pairs.append((url, numac_search))
                else:
                    self.logger.warning(f"Could not extract numac_search from URL: {url}")

            self.logger.info(f"Extracted {len(url_numac_pairs)} valid numac_search parameters")

            # Apply test mode limit if enabled
            if self.test_mode:
                url_numac_pairs = url_numac_pairs[:self.test_limit]
                self.logger.info(f"Test mode: processing first {len(url_numac_pairs)} URLs")

            # No deduplication needed as per requirements (assume CSV is already deduplicated)
            self.stats['duplicates_removed'] = 0
            self.stats['original_rows'] = len(url_numac_pairs)

            # Load checkpoint and existing files for resume capability
            processed_ids = self.load_checkpoint()
            existing_files = self.get_existing_files()
            all_existing = processed_ids.union(existing_files)

            self.logger.info(f"Resume capability: {len(processed_ids)} from checkpoint, {len(existing_files)} existing files")

            # Now check which files already exist and build final URL list
            url_list = []
            for url, numac_search in url_numac_pairs:
                # Check if file already exists or was processed
                if numac_search in all_existing or self.file_exists(numac_search):
                    if numac_search in processed_ids:
                        self.logger.debug(f"⚠ Document {numac_search} already processed (from checkpoint), skipping")
                    else:
                        self.logger.debug(f"⚠ File {numac_search}.txt already exists, skipping")
                    self.stats['skipped'] += 1
                    continue

                url_list.append((url, numac_search))

            self.stats['total'] = len(url_list)
            self.logger.info(f"Processing {len(url_list)} URLs (after filtering)")

            # Process URLs in batches using async requests
            processed_document_ids = processed_ids.copy()  # Start with already processed IDs

            async with httpx.AsyncClient(**self.client_config) as session:
                # Split URLs into batches for concurrent processing
                batch_size = self.concurrent_requests
                for i in range(0, len(url_list), batch_size):
                    batch = url_list[i:i + batch_size]
                    batch_num = (i // batch_size) + 1
                    total_batches = (len(url_list) + batch_size - 1) // batch_size

                    self.logger.info(f"\n--- Processing batch {batch_num}/{total_batches} ({len(batch)} URLs) ---")

                    # Process batch concurrently
                    await self.process_url_batch(session, batch)

                    # Add processed document IDs to checkpoint
                    for url, document_id in batch:
                        processed_document_ids.add(document_id)

                    # Save checkpoint every 10 batches or at the end
                    if batch_num % 10 == 0 or i + batch_size >= len(url_list):
                        total_expected = len(url_numac_pairs)
                        self.save_checkpoint(processed_document_ids, total_expected)

                    # Add delay between batches
                    if i + batch_size < len(url_list):
                        await asyncio.sleep(self.delay)

                    # Log progress with checkpoint info
                    processed = min(i + batch_size, len(url_list))
                    total_processed_overall = len(processed_document_ids)
                    self.logger.info(f"Progress: {processed}/{len(url_list)} URLs processed "
                                   f"({total_processed_overall}/{len(url_numac_pairs)} total documents)")

            self.print_summary()

        except Exception as e:
            self.logger.error(f"Error processing CSV: {e}")
            raise
    
    def print_summary(self):
        """Print scraping summary."""
        self.logger.info("\n" + "="*50)
        self.logger.info("SCRAPING COMPLETE")
        self.logger.info("="*50)

        # Performance improvement metrics
        if self.stats['original_rows'] > 0:
            self.logger.info(f"Original CSV rows: {self.stats['original_rows']}")
            self.logger.info(f"Duplicates removed: {self.stats['duplicates_removed']}")
            efficiency_gain = (self.stats['duplicates_removed'] / self.stats['original_rows']) * 100
            self.logger.info(f"Efficiency gain: {efficiency_gain:.1f}% (avoided processing duplicates)")

        self.logger.info(f"Total URLs processed: {self.stats['total']}")
        self.logger.info(f"Successful: {self.stats['successful']}")
        self.logger.info(f"Failed: {self.stats['failed']}")
        self.logger.info(f"Skipped (already exist): {self.stats['skipped']}")

        # Processing statistics
        if self.stats['successful'] > 0:
            self.logger.info(f"Direct URL processing: Simplified approach using comprehensive URL dataset")

        if self.stats['total'] > 0:
            success_rate = (self.stats['successful'] / self.stats['total']) * 100
            self.logger.info(f"Overall success rate: {success_rate:.1f}%")

        self.logger.info(f"Files saved in: {self.output_dir}")

        # Performance metrics
        total_processed = self.stats['successful'] + self.stats['failed']
        if total_processed > 0:
            self.logger.info(f"Processing: High-performance async HTTP requests with direct URL fetching")

    def load_checkpoint(self) -> set:
        """Load checkpoint data to resume processing."""
        if self.checkpoint_file.exists():
            try:
                with open(self.checkpoint_file, 'r') as f:
                    checkpoint_data = json.load(f)
                    processed_ids = set(checkpoint_data.get('processed_document_ids', []))
                    self.logger.info(f"Loaded checkpoint: {len(processed_ids)} documents already processed")
                    return processed_ids
            except Exception as e:
                self.logger.warning(f"Could not load checkpoint: {e}")
        return set()

    def save_checkpoint(self, processed_ids: set, total_urls: int):
        """Save checkpoint data for resume capability."""
        try:
            checkpoint_data = {
                'processed_document_ids': list(processed_ids),
                'total_processed': len(processed_ids),
                'total_urls': total_urls,
                'last_updated': datetime.now().isoformat(),
                'output_directory': str(self.output_dir),
                'input_csv': str(self.input_csv)
            }

            with open(self.checkpoint_file, 'w') as f:
                json.dump(checkpoint_data, f, indent=2)

            self.logger.debug(f"Checkpoint saved: {len(processed_ids)}/{total_urls} processed")
        except Exception as e:
            self.logger.warning(f"Could not save checkpoint: {e}")

    def get_existing_files(self) -> set:
        """Get set of document IDs that already have HTML files."""
        existing_ids = set()
        if self.output_dir.exists():
            for html_file in self.output_dir.glob("*.html"):
                # Extract document ID from filename (remove .html extension)
                doc_id = html_file.stem
                existing_ids.add(doc_id)
        return existing_ids


def run_scraper(scraper: JustelScraper):
    """Run the scraper with proper async handling."""
    try:
        asyncio.run(scraper.process_excel())
    except KeyboardInterrupt:
        scraper.logger.info("\nScraping interrupted by user")
    except Exception as e:
        scraper.logger.error(f"Scraping failed: {e}")
        sys.exit(1)


def main():
    """Main function with command-line argument parsing for comprehensive Belgian legal document processing."""
    parser = argparse.ArgumentParser(description="JUSTEL Legal Documents Web Scraper - Comprehensive Dataset (207,911 URLs)")
    parser.add_argument("--input", "-i", default="data/csv_data/ejustice_urls.csv",
                       help="Input CSV file path (default: data/csv_data/ejustice_urls.csv)")
    parser.add_argument("--output", "-o", default="data/html_raw_all",
                       help="Output directory for HTML files (default: data/html_raw_all)")
    parser.add_argument("--delay", "-d", type=float, default=0.02,
                       help="Delay between request batches in seconds (default: 0.02)")
    parser.add_argument("--concurrent", "-c", type=int, default=35,
                       help="Number of concurrent requests (default: 35)")
    parser.add_argument("--test", "-t", action="store_true",
                       help="Run in test mode (process limited URLs)")
    parser.add_argument("--test-limit", type=int, default=100,
                       help="Number of URLs to process in test mode (default: 100)")

    args = parser.parse_args()

    scraper = JustelScraper(
        input_csv=args.input,
        output_dir=args.output,
        delay=args.delay,
        concurrent_requests=args.concurrent,
        test_mode=args.test,
        test_limit=args.test_limit
    )

    run_scraper(scraper)


if __name__ == "__main__":
    main()
