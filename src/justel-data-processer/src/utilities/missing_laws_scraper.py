#!/usr/bin/env python3
"""
Missing Belgian Laws Scraper

This script identifies and scrapes missing Belgian laws from justel.be by:
1. Reading the complete list of law URLs from data/csv_data/full-list.xlsx
2. Extracting numac_search parameters to identify each law
3. Checking if each law already exists as {numac_search}.txt in the input directory
4. Scraping missing laws using the existing justel web scraper logic
5. Saving newly scraped content as HTML files in input_latest/ directory

Requirements:
- pandas
- httpx
- selectolax
- openpyxl

Usage:
    python missing_laws_scraper.py [options]
"""

import sys
import logging
import argparse
import asyncio
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Set
from urllib.parse import urlparse, parse_qs

import pandas as pd
import httpx
from selectolax.parser import HTMLParser


class MissingLawsScraper:
    """Scraper for identifying and downloading missing Belgian laws."""

    def __init__(self,
                 input_excel: str = "data/csv_data/full-list.xlsx",
                 existing_dir: str = "input",
                 output_dir: str = "input_latest",
                 delay: float = 0.05,
                 concurrent_requests: int = 20,
                 test_mode: bool = False,
                 test_limit: int = 50):
        """
        Initialize the missing laws scraper.

        Args:
            input_excel: Path to Excel file with all law URLs
            existing_dir: Directory with existing TXT files
            output_dir: Directory to save newly scraped TXT files
            delay: Delay between request batches in seconds
            concurrent_requests: Number of concurrent requests
            test_mode: Process only limited number of URLs for testing
            test_limit: Number of URLs to process in test mode
        """
        self.input_excel = input_excel
        self.existing_dir = Path(existing_dir)
        self.output_dir = Path(output_dir)
        self.delay = delay
        self.concurrent_requests = concurrent_requests
        self.test_mode = test_mode
        self.test_limit = test_limit

        # Create output directory
        self.output_dir.mkdir(exist_ok=True, parents=True)

        # Setup logging
        self.setup_logging()

        # HTTP client configuration
        self.client_config = {
            'timeout': httpx.Timeout(30.0),
            'limits': httpx.Limits(
                max_connections=50,
                max_keepalive_connections=25,
                keepalive_expiry=30.0
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
            'total_urls': 0,
            'existing_files': 0,
            'missing_laws': 0,
            'successful': 0,
            'failed': 0,
            'invalid_urls': 0
        }

    def setup_logging(self):
        """Setup logging configuration."""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"missing_laws_scraper_{timestamp}.log"

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)

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
            from urllib.parse import urlencode
            new_query = urlencode(query_params, doseq=True)

            # Rebuild URL
            french_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{new_query}"

            return french_url

        except Exception as e:
            self.logger.warning(f"Error modifying URL for French content {url}: {e}")
            return url

    def file_exists(self, numac_search: str) -> bool:
        """Check if TXT file already exists for given numac_search."""
        file_path = self.existing_dir / f"{numac_search}.txt"
        return file_path.exists()

    def get_existing_files(self) -> Set[str]:
        """Get set of numac_search IDs that already have TXT files."""
        existing_ids = set()
        if self.existing_dir.exists():
            for txt_file in self.existing_dir.glob("*.txt"):
                # Extract numac_search from filename (remove .txt extension)
                numac_id = txt_file.stem
                existing_ids.add(numac_id)
        return existing_ids

    def get_already_scraped_files(self) -> Set[str]:
        """Get set of numac_search IDs that already have HTML files in output directory."""
        scraped_ids = set()
        if self.output_dir.exists():
            for html_file in self.output_dir.glob("*.html"):
                # Extract numac_search from filename (remove .html extension)
                numac_id = html_file.stem
                scraped_ids.add(numac_id)
        return scraped_ids

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
                            from urllib.parse import urljoin
                            return urljoin(base_url, href)

            return None

        except Exception as e:
            self.logger.warning(f"Error extracting French URL: {e}")
            return None

    async def fetch_and_save_html(self, session: httpx.AsyncClient, url: str, numac_search: str) -> bool:
        """
        Fetch HTML content from URL, extract French version URL, and save as HTML file.

        Args:
            session: HTTP client session
            url: URL to fetch
            numac_search: Document ID for filename

        Returns:
            True if successful, False otherwise
        """
        try:
            self.logger.info(f"📥 Fetching: {url}")

            # Make initial HTTP request
            response = await session.get(url, follow_redirects=True)
            response.raise_for_status()

            # Get HTML content
            html_content = response.text

            # Basic validation - check if content contains expected document ID
            if numac_search not in html_content:
                self.logger.warning(f"⚠️ Content does not contain expected numac_search {numac_search}")
                return False

            # Extract French URL from the HTML
            french_url = self.extract_french_url(html_content, url)

            if french_url and french_url != url:
                self.logger.info(f"🇫🇷 Found French URL, fetching: {french_url}")

                # Fetch the French version
                french_response = await session.get(french_url, follow_redirects=True)
                french_response.raise_for_status()
                html_content = french_response.text

                # Validate French content
                if numac_search not in html_content:
                    self.logger.warning(f"⚠️ French content does not contain expected numac_search {numac_search}")
                    return False
            else:
                self.logger.info(f"ℹ️ Using original URL (French URL not found or same as original)")

            # Basic validation - check if content is not empty or too short
            if not html_content or len(html_content.strip()) < 500:
                self.logger.warning(f"⚠️ HTML content too short for {numac_search}")
                return False

            # Save as HTML file
            html_file_path = self.output_dir / f"{numac_search}.html"
            with open(html_file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)

            self.logger.info(f"✅ Successfully saved {numac_search}.html")
            return True

        except Exception as e:
            self.logger.error(f"❌ Error fetching {url}: {e}")
            return False



    async def process_url_batch(self, session: httpx.AsyncClient, url_batch: List[tuple]) -> None:
        """
        Process a batch of URLs concurrently.

        Args:
            session: httpx async client session
            url_batch: List of (url, numac_search) tuples
        """
        tasks = []
        for url, numac_search in url_batch:
            task = self.fetch_and_save_html(session, url, numac_search)
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

    async def process_missing_laws(self) -> None:
        """Main processing function to identify and scrape missing laws."""
        try:
            # Read Excel file
            self.logger.info(f"Reading Excel file: {self.input_excel}")
            df = pd.read_excel(self.input_excel)
            
            self.logger.info(f"Loaded Excel with {len(df)} rows")
            self.logger.info(f"Columns: {list(df.columns)}")
            
            self.stats['total_urls'] = len(df)

            # Extract numac_search from URLs
            self.logger.info("Extracting numac_search parameters from URLs...")
            url_numac_pairs = []
            
            for _, row in df.iterrows():
                url = row['URL']
                numac_search = self.extract_numac_search(url)
                
                if numac_search:
                    url_numac_pairs.append((url, numac_search))
                else:
                    self.stats['invalid_urls'] += 1

            self.logger.info(f"Extracted {len(url_numac_pairs)} valid numac_search parameters")

            # Get existing files
            self.logger.info("Checking for existing files...")
            existing_files = self.get_existing_files()
            self.stats['existing_files'] = len(existing_files)

            # Get already scraped files (for resume capability)
            already_scraped = self.get_already_scraped_files()
            self.logger.info(f"Found {len(existing_files)} existing TXT files")
            self.logger.info(f"Found {len(already_scraped)} already scraped HTML files (resume capability)")

            # Filter out existing files AND already scraped files
            missing_laws = []
            for url, numac_search in url_numac_pairs:
                if numac_search not in existing_files and numac_search not in already_scraped:
                    missing_laws.append((url, numac_search))

            self.stats['missing_laws'] = len(missing_laws)
            self.logger.info(f"Found {len(missing_laws)} missing laws to scrape")

            # Apply test mode limit if enabled
            if self.test_mode:
                missing_laws = missing_laws[:self.test_limit]
                self.logger.info(f"Test mode: processing first {len(missing_laws)} missing laws")

            if not missing_laws:
                self.logger.info("No missing laws found. All laws are already scraped!")
                return

            # Process missing laws in batches
            async with httpx.AsyncClient(**self.client_config) as session:
                batch_size = self.concurrent_requests
                for i in range(0, len(missing_laws), batch_size):
                    batch = missing_laws[i:i + batch_size]
                    batch_num = (i // batch_size) + 1
                    total_batches = (len(missing_laws) + batch_size - 1) // batch_size

                    self.logger.info(f"\n--- Processing batch {batch_num}/{total_batches} ({len(batch)} URLs) ---")

                    # Process batch concurrently
                    await self.process_url_batch(session, batch)

                    # Add delay between batches
                    if i + batch_size < len(missing_laws):
                        await asyncio.sleep(self.delay)

                    # Log progress
                    processed = min(i + batch_size, len(missing_laws))
                    self.logger.info(f"Progress: {processed}/{len(missing_laws)} missing laws processed")

            self.print_summary()

        except Exception as e:
            self.logger.error(f"Error processing missing laws: {e}")
            raise

    def print_summary(self):
        """Print scraping summary."""
        self.logger.info("\n" + "="*60)
        self.logger.info("MISSING LAWS SCRAPING COMPLETE")
        self.logger.info("="*60)
        
        self.logger.info(f"Total URLs in Excel file: {self.stats['total_urls']:,}")
        self.logger.info(f"Invalid URLs (no numac_search): {self.stats['invalid_urls']:,}")
        self.logger.info(f"Existing TXT files: {self.stats['existing_files']:,}")

        # Show resume information
        already_scraped = self.get_already_scraped_files()
        if already_scraped:
            self.logger.info(f"Already scraped HTML files (resumed): {len(already_scraped):,}")

        self.logger.info(f"Missing laws identified: {self.stats['missing_laws']:,}")
        self.logger.info(f"Successfully scraped: {self.stats['successful']:,}")
        self.logger.info(f"Failed to scrape: {self.stats['failed']:,}")
        
        if self.stats['successful'] + self.stats['failed'] > 0:
            success_rate = (self.stats['successful'] / (self.stats['successful'] + self.stats['failed'])) * 100
            self.logger.info(f"Success rate: {success_rate:.1f}%")
        
        self.logger.info(f"New HTML files saved in: {self.output_dir}")


def run_scraper(scraper: MissingLawsScraper):
    """Run the scraper with proper async handling."""
    try:
        asyncio.run(scraper.process_missing_laws())
    except KeyboardInterrupt:
        scraper.logger.info("\nScraping interrupted by user")
    except Exception as e:
        scraper.logger.error(f"Scraping failed: {e}")
        sys.exit(1)


def main():
    """Main function with command-line argument parsing."""
    parser = argparse.ArgumentParser(description="Missing Belgian Laws Scraper")
    parser.add_argument("--input", "-i", default="data/csv_data/full-list.xlsx",
                       help="Input Excel file path (default: data/csv_data/full-list.xlsx)")
    parser.add_argument("--existing", "-e", default="input",
                       help="Directory with existing TXT files (default: input)")
    parser.add_argument("--output", "-o", default="input_latest",
                       help="Output directory for new TXT files (default: input_latest)")
    parser.add_argument("--delay", "-d", type=float, default=0.05,
                       help="Delay between request batches in seconds (default: 0.05)")
    parser.add_argument("--concurrent", "-c", type=int, default=20,
                       help="Number of concurrent requests (default: 20)")
    parser.add_argument("--test", "-t", action="store_true",
                       help="Run in test mode (process limited URLs)")
    parser.add_argument("--test-limit", type=int, default=50,
                       help="Number of URLs to process in test mode (default: 50)")

    args = parser.parse_args()

    scraper = MissingLawsScraper(
        input_excel=args.input,
        existing_dir=args.existing,
        output_dir=args.output,
        delay=args.delay,
        concurrent_requests=args.concurrent,
        test_mode=args.test,
        test_limit=args.test_limit
    )

    run_scraper(scraper)


if __name__ == "__main__":
    main()
