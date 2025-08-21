#!/usr/bin/env python3
"""
Belgian eJustice URL Discovery Scraper

This script systematically discovers all Justel URLs from the Belgian eJustice portal
by querying every possible combination of document types, years, months, and days.

The scraper targets the ELI (European Legislation Identifier) system at:
http://www.ejustice.just.fgov.be/eli/

URL Structure:
http://www.ejustice.just.fgov.be/eli/DT/AAAA/MM/JJ/Identificateur_Unique/version

Where:
- DT: Document type (CONSTITUTION, LOI, DECRET, ORDONNANCE, ARRETE)
- AAAA: Year (1800-current)
- MM: Month (01-12)
- JJ: Day (01-31)
- Identificateur_Unique: 10-digit unique identifier
- version: 'justel' for consolidated version

Expected output: 200,000-300,000 URLs to process
Target: Extract <a href="...justel">Justel</a> links from search result pages

Requirements:
- pandas
- httpx (fastest HTTP client)
- selectolax (fastest HTML parser)
- asyncio (for concurrent requests)

Usage:
    python ejustice_url_discovery_scraper.py [options]
"""

import os
import sys
import csv
import re
import time
import logging
import argparse
import asyncio
from datetime import datetime, date
from pathlib import Path
from typing import Optional, Tuple, List, Dict, Set, Generator
from urllib.parse import urlparse, urljoin
import calendar
import json

import pandas as pd
import httpx
from selectolax.parser import HTMLParser


class EJusticeURLDiscoveryScraper:
    """
    Comprehensive scraper for discovering Justel URLs from Belgian eJustice portal.
    
    Systematically queries all possible combinations of document types, years, months,
    and days to extract Justel URLs from search result pages.
    """

    # Document types available in the Belgian eJustice system
    DOCUMENT_TYPES = [
        'CONSTITUTION',
        'LOI',           # Federal legislation
        'DECRET',        # Regional and community legislation (since 1972)
        'ORDONNANCE',    # Brussels regional legislation (since 1990)
        'ARRETE'         # Secondary legislation (royal decrees, government decrees, ministerial decrees)
    ]

    def __init__(self,
                 output_csv: str = "data/csv_data/ejustice_urls.csv",
                 checkpoint_file: str = "data/csv_data/ejustice_checkpoint.json",
                 start_year: int = 1789,
                 end_year: Optional[int] = None,
                 delay: float = 0.05,
                 concurrent_requests: int = 20,
                 test_mode: bool = False,
                 test_limit: int = 100,
                 resume: bool = True):
        """
        Initialize the eJustice URL discovery scraper.

        Args:
            output_csv: Path to output CSV file for discovered URLs
            checkpoint_file: Path to checkpoint file for resume capability
            start_year: Starting year for URL discovery (default: 1800)
            end_year: Ending year for URL discovery (default: current year)
            delay: Delay between request batches in seconds
            concurrent_requests: Number of concurrent requests
            test_mode: Process only limited combinations for testing
            test_limit: Number of URL combinations to process in test mode
            resume: Whether to resume from checkpoint if available
        """
        self.output_csv = Path(output_csv)
        self.checkpoint_file = Path(checkpoint_file)
        self.start_year = start_year
        self.end_year = end_year or datetime.now().year
        self.delay = delay
        self.concurrent_requests = concurrent_requests
        self.test_mode = test_mode
        self.test_limit = test_limit
        self.resume = resume

        # Create output directories
        self.output_csv.parent.mkdir(parents=True, exist_ok=True)
        self.checkpoint_file.parent.mkdir(parents=True, exist_ok=True)

        # Setup logging
        self.setup_logging()

        # HTTP client configuration - optimized for high throughput
        self.client_config = {
            'timeout': httpx.Timeout(15.0),  # Reduced timeout for faster failures
            'limits': httpx.Limits(
                max_connections=50,  # Increased connection pool
                max_keepalive_connections=25,  # More keepalive connections
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

        # Statistics tracking
        self.stats = {
            'total_combinations': 0,
            'processed_combinations': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'help_pages_skipped': 0,
            'database_error_pages_skipped': 0,
            'justel_urls_found': 0,
            'pages_with_no_results': 0,
            'pages_with_single_result': 0,
            'pages_with_multiple_results': 0,
            'duplicate_urls_filtered': 0,
            'start_time': None,
            'last_checkpoint_time': None
        }

        # Discovered URLs storage (for deduplication)
        self.discovered_urls: Set[str] = set()
        self.url_metadata: List[Dict[str, str]] = []

        # Checkpoint data
        self.checkpoint_data = {
            'last_processed': None,
            'discovered_urls': [],
            'stats': {}
        }

        # Load checkpoint if resuming
        if self.resume:
            self.load_checkpoint()

    def setup_logging(self):
        """Setup logging configuration."""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"ejustice_discovery_{timestamp}.log"

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info("eJustice URL Discovery Scraper initialized")

    def load_checkpoint(self):
        """Load checkpoint data for resuming interrupted sessions."""
        if self.checkpoint_file.exists():
            try:
                with open(self.checkpoint_file, 'r', encoding='utf-8') as f:
                    self.checkpoint_data = json.load(f)

                # Restore discovered URLs
                self.discovered_urls = set(self.checkpoint_data.get('discovered_urls', []))

                # Restore statistics and convert datetime strings back to datetime objects
                saved_stats = self.checkpoint_data.get('stats', {})
                if 'start_time' in saved_stats and saved_stats['start_time']:
                    try:
                        saved_stats['start_time'] = datetime.fromisoformat(saved_stats['start_time'])
                    except (ValueError, TypeError):
                        saved_stats['start_time'] = None
                if 'last_checkpoint_time' in saved_stats and saved_stats['last_checkpoint_time']:
                    try:
                        saved_stats['last_checkpoint_time'] = datetime.fromisoformat(saved_stats['last_checkpoint_time'])
                    except (ValueError, TypeError):
                        saved_stats['last_checkpoint_time'] = None

                self.stats.update(saved_stats)

                self.logger.info(f"Loaded checkpoint: {len(self.discovered_urls)} URLs already discovered")
                self.logger.info(f"Last processed: {self.checkpoint_data.get('last_processed', 'None')}")

            except Exception as e:
                self.logger.warning(f"Failed to load checkpoint: {e}")
                self.checkpoint_data = {'last_processed': None, 'discovered_urls': [], 'stats': {}}

    def save_checkpoint(self):
        """Save current progress to checkpoint file."""
        try:
            # Convert datetime objects to ISO strings for JSON serialization
            stats_copy = self.stats.copy()
            if 'start_time' in stats_copy and stats_copy['start_time']:
                stats_copy['start_time'] = stats_copy['start_time'].isoformat()
            if 'last_checkpoint_time' in stats_copy and stats_copy['last_checkpoint_time']:
                stats_copy['last_checkpoint_time'] = stats_copy['last_checkpoint_time'].isoformat()

            self.checkpoint_data['discovered_urls'] = list(self.discovered_urls)
            self.checkpoint_data['stats'] = stats_copy
            self.checkpoint_data['last_checkpoint_time'] = datetime.now().isoformat()

            with open(self.checkpoint_file, 'w', encoding='utf-8') as f:
                json.dump(self.checkpoint_data, f, indent=2, ensure_ascii=False)

            self.stats['last_checkpoint_time'] = datetime.now()
            self.logger.debug("Checkpoint saved successfully")

        except Exception as e:
            self.logger.error(f"Failed to save checkpoint: {e}")

    def generate_url_combinations(self) -> Generator[Tuple[str, str, int, int, int], None, None]:
        """
        Generate all possible URL combinations for document types, years, months, and days.
        Stops at today's date to avoid processing future dates.

        Yields:
            Tuple of (document_type, url, year, month, day)
        """
        total_combinations = 0
        processed_combinations = 0
        today = date.today()

        # Calculate total combinations for progress tracking
        for doc_type in self.DOCUMENT_TYPES:
            for year in range(self.start_year, self.end_year + 1):
                # Determine month range for this year
                max_month = 12 if year < today.year else today.month

                for month in range(1, max_month + 1):
                    # Determine day range for this month/year
                    days_in_month = calendar.monthrange(year, month)[1]
                    if year == today.year and month == today.month:
                        # For current month, only go up to today
                        max_day = today.day
                    else:
                        max_day = days_in_month

                    total_combinations += max_day

        self.stats['total_combinations'] = total_combinations
        self.logger.info(f"Total URL combinations to process: {total_combinations:,} (up to {today})")

        if self.test_mode:
            self.logger.info(f"Test mode: limiting to {self.test_limit} combinations")

        # Generate combinations
        for doc_type in self.DOCUMENT_TYPES:
            for year in range(self.start_year, self.end_year + 1):
                # Determine month range for this year
                max_month = 12 if year < today.year else today.month

                for month in range(1, max_month + 1):
                    # Determine day range for this month/year
                    days_in_month = calendar.monthrange(year, month)[1]
                    if year == today.year and month == today.month:
                        # For current month, only go up to today
                        max_day = today.day
                    else:
                        max_day = days_in_month

                    for day in range(1, max_day + 1):
                        # Check if we should skip this combination (resume functionality)
                        combination_key = f"{doc_type}_{year:04d}_{month:02d}_{day:02d}"

                        if (self.checkpoint_data.get('last_processed') and
                            self._should_skip_combination(doc_type, year, month, day)):
                            processed_combinations += 1
                            continue

                        # Generate the eJustice URL
                        url = f"http://www.ejustice.just.fgov.be/eli/{doc_type.lower()}/{year}/{month:02d}/{day:02d}"

                        yield doc_type, url, year, month, day

                        processed_combinations += 1

                        # Update checkpoint key
                        self.checkpoint_data['last_processed'] = combination_key

                        # Test mode limit
                        if self.test_mode and processed_combinations >= self.test_limit:
                            self.logger.info(f"Test mode limit reached: {self.test_limit} combinations")
                            return

    def _should_skip_combination(self, doc_type: str, year: int, month: int, day: int) -> bool:
        """
        Determine if a combination should be skipped based on checkpoint data.
        Uses proper sequential ordering instead of string comparison.

        Args:
            doc_type: Document type
            year: Year
            month: Month
            day: Day

        Returns:
            True if combination should be skipped, False otherwise
        """
        if not self.checkpoint_data.get('last_processed'):
            return False

        # Parse last processed combination
        last_processed = self.checkpoint_data['last_processed']
        try:
            parts = last_processed.split('_')
            last_doc_type = parts[0]
            last_year = int(parts[1])
            last_month = int(parts[2])
            last_day = int(parts[3])
        except (IndexError, ValueError):
            # If we can't parse, don't skip
            return False

        # Get document type indices for proper ordering
        try:
            current_doc_index = self.DOCUMENT_TYPES.index(doc_type)
            last_doc_index = self.DOCUMENT_TYPES.index(last_doc_type)
        except ValueError:
            # If document type not found, don't skip
            return False

        # Compare using proper sequential ordering
        if current_doc_index < last_doc_index:
            return True
        elif current_doc_index > last_doc_index:
            return False
        else:
            # Same document type, compare dates
            current_date = (year, month, day)
            last_date = (last_year, last_month, last_day)
            return current_date <= last_date

    def is_valid_date(self, year: int, month: int, day: int) -> bool:
        """
        Validate if the given year, month, day combination is a valid date.

        Args:
            year: Year value
            month: Month value (1-12)
            day: Day value (1-31)

        Returns:
            True if valid date, False otherwise
        """
        try:
            date(year, month, day)
            return True
        except ValueError:
            return False

    def is_help_page(self, html_content: str) -> Tuple[bool, str]:
        """
        Check if the HTML content is the eJustice help/instructions page or database error page.

        The help page appears when no documents are found for a specific date combination.
        Database error pages appear when invalid dates are submitted (like 1999-99-99).
        Both contain content that we should not harvest as real discoveries.

        Args:
            html_content: HTML content to check

        Returns:
            Tuple of (is_error_page, page_type) where page_type is 'help', 'database_error', or 'content'
        """
        if not html_content:
            return False, 'content'

        content_lower = html_content.lower()

        # Key phrases that identify the help page
        help_indicators = [
            "Désolé, la requête que vous avez formulée",
            "Veuillez adapter les éléments introduits",
            "Aide ELI",
            "Exemples d'adressage correct"
        ]

        # Key phrases that identify database error pages
        database_error_indicators = [
            "error select",
            "select nm,cn,pd,actif,tit,so,dd from",
            "loi_all where",
            "where dd =",
            "and actif = 'y'"
        ]

        # Count indicators for each type
        found_help_indicators = sum(1 for indicator in help_indicators
                                   if indicator.lower() in content_lower)

        found_db_error_indicators = sum(1 for indicator in database_error_indicators
                                       if indicator.lower() in content_lower)

        # Check for specific SQL error pattern (very strong indicator)
        has_sql_error_pattern = "error select nm,cn,pd,actif,tit,so,dd from loi_all where" in content_lower

        # Determine page type with conservative thresholds
        if has_sql_error_pattern or found_db_error_indicators >= 3:
            self.logger.debug("Detected database error page - skipping URL extraction")
            return True, 'database_error'
        elif found_help_indicators >= 2:
            self.logger.debug("Detected help/instructions page - skipping URL extraction")
            return True, 'help'
        else:
            return False, 'content'

    async def fetch_page_content(self, url: str, session: httpx.AsyncClient) -> Tuple[Optional[str], str]:
        """
        Fetch the content of a single eJustice page.

        Args:
            url: The eJustice URL to fetch
            session: HTTP client session

        Returns:
            Tuple of (HTML content if successful, status)
            status can be: 'success', 'help_page', 'database_error', '404', 'error'
        """
        try:
            self.logger.debug(f"Fetching: {url}")

            response = await session.get(url, follow_redirects=True)
            response.raise_for_status()

            html_content = response.text

            # Check if this is a help page or database error page
            is_error_page, page_type = self.is_help_page(html_content)
            if is_error_page:
                if page_type == 'database_error':
                    self.logger.debug(f"Database error page detected for {url} - skipping")
                    return None, 'database_error'
                else:  # help page
                    self.logger.debug(f"Help page detected for {url} - skipping")
                    return None, 'help_page'

            return html_content, 'success'

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                self.logger.debug(f"404 Not Found: {url}")
                return None, '404'
            else:
                self.logger.warning(f"HTTP error {e.response.status_code} for {url}: {e}")
                return None, 'error'
        except Exception as e:
            self.logger.error(f"Error fetching {url}: {e}")
            return None, 'error'

    def extract_justel_urls(self, html_content: str, base_url: str) -> List[Dict[str, str]]:
        """
        Extract Justel URLs from the HTML content of an eJustice page.

        Args:
            html_content: HTML content of the page
            base_url: Base URL for resolving relative links

        Returns:
            List of dictionaries containing URL metadata
        """
        justel_urls = []

        try:
            parser = HTMLParser(html_content)

            # Find all <a> tags with href containing 'justel'
            links = parser.css('a[href*="justel"]')

            for link in links:
                href = link.attributes.get('href', '')
                text = link.text(strip=True)

                # Resolve relative URLs
                if href.startswith('/'):
                    full_url = urljoin('http://www.ejustice.just.fgov.be', href)
                elif href.startswith('http'):
                    full_url = href
                else:
                    full_url = urljoin(base_url, href)

                # Extract metadata from the URL
                metadata = self.extract_url_metadata(full_url, base_url)
                if metadata:
                    # If link text is a URL (common on eJustice), use "Justel" instead
                    if text.startswith('http://') or text.startswith('https://'):
                        metadata['link_text'] = 'Justel'
                    else:
                        metadata['link_text'] = text or 'Justel'
                    metadata['source_url'] = base_url
                    justel_urls.append(metadata)

            # Also look for direct justel URLs in the page content
            # Pattern: http://www.ejustice.just.fgov.be/eli/[type]/[year]/[month]/[day]/[id]/justel
            # Updated to handle various document ID formats (numeric, alphanumeric, etc.)
            justel_pattern = r'http://www\.ejustice\.just\.fgov\.be/eli/([^/]+)/(\d{4})/(\d{1,2})/(\d{1,2})/([^/]+)/justel'
            matches = re.finditer(justel_pattern, html_content)

            for match in matches:
                full_url = match.group(0)
                doc_type, year, month, day, doc_id = match.groups()

                metadata = {
                    'url_justel': full_url,
                    'document_type': doc_type.upper(),
                    'year': year,
                    'month': month.zfill(2),
                    'day': day.zfill(2),
                    'document_id': doc_id,
                    'link_text': 'Justel',
                    'source_url': base_url
                }
                justel_urls.append(metadata)

        except Exception as e:
            self.logger.error(f"Error parsing HTML content: {e}")

        return justel_urls

    def extract_url_metadata(self, justel_url: str, source_url: str = None) -> Optional[Dict[str, str]]:
        """
        Extract metadata from a Justel URL.

        Args:
            justel_url: The Justel URL to parse
            source_url: The source URL where this was found

        Returns:
            Dictionary with extracted metadata or None if parsing failed
        """
        try:
            # Pattern: http://www.ejustice.just.fgov.be/eli/[type]/[year]/[month]/[day]/[id]/justel
            # Updated to handle various document ID formats (numeric, alphanumeric, etc.)
            pattern = r'http://www\.ejustice\.just\.fgov\.be/eli/([^/]+)/(\d{4})/(\d{1,2})/(\d{1,2})/([^/]+)/justel'
            match = re.match(pattern, justel_url)

            if match:
                doc_type, year, month, day, doc_id = match.groups()

                return {
                    'url_justel': justel_url,
                    'document_type': doc_type.upper(),
                    'year': year,
                    'month': month.zfill(2),
                    'day': day.zfill(2),
                    'document_id': doc_id,
                    'link_text': '',  # Will be filled in by calling method
                    'source_url': ''  # Will be filled in by calling method
                }
            else:
                self.logger.warning(f"Could not parse Justel URL: {justel_url}")
                return None

        except Exception as e:
            self.logger.error(f"Error extracting metadata from {justel_url}: {e}")
            return None

    async def process_url_batch(self, url_batch: List[Tuple[str, str, int, int, int]],
                               session: httpx.AsyncClient) -> List[Dict[str, str]]:
        """
        Process a batch of URLs concurrently.

        Args:
            url_batch: List of (doc_type, url, year, month, day) tuples
            session: HTTP client session

        Returns:
            List of discovered Justel URLs with metadata
        """
        batch_results = []

        # Create tasks for concurrent processing
        tasks = []
        for doc_type, url, year, month, day in url_batch:
            task = asyncio.create_task(self.fetch_page_content(url, session))
            tasks.append((task, doc_type, url, year, month, day))

        # Wait for all tasks to complete
        for task, doc_type, url, year, month, day in tasks:
            try:
                html_content, status = await task
                self.stats['processed_combinations'] += 1

                if status == 'success' and html_content:
                    self.stats['successful_requests'] += 1

                    # Extract Justel URLs from the page
                    justel_urls = self.extract_justel_urls(html_content, url)

                    if justel_urls:
                        if len(justel_urls) == 1:
                            self.stats['pages_with_single_result'] += 1
                        else:
                            self.stats['pages_with_multiple_results'] += 1

                        # Add to batch results
                        for justel_data in justel_urls:
                            # Check for duplicates
                            justel_url = justel_data['url_justel']
                            if justel_url not in self.discovered_urls:
                                self.discovered_urls.add(justel_url)
                                batch_results.append(justel_data)
                                self.stats['justel_urls_found'] += 1
                            else:
                                self.stats['duplicate_urls_filtered'] += 1
                    else:
                        self.stats['pages_with_no_results'] += 1

                elif status == 'help_page':
                    self.stats['help_pages_skipped'] += 1

                elif status == 'database_error':
                    self.stats['database_error_pages_skipped'] += 1

                else:
                    # 404, error, or other failure
                    self.stats['failed_requests'] += 1

            except Exception as e:
                self.logger.error(f"Error processing {url}: {e}")
                self.stats['failed_requests'] += 1

        return batch_results

    def save_urls_to_csv(self, urls_data: List[Dict[str, str]], append: bool = True):
        """
        Save discovered URLs to CSV file.

        Args:
            urls_data: List of URL metadata dictionaries
            append: Whether to append to existing file or overwrite
        """
        if not urls_data:
            return

        try:
            # Define CSV columns
            fieldnames = [
                'url_justel',
                'document_type',
                'year',
                'month',
                'day',
                'document_id',
                'link_text',
                'source_url',
                'discovery_timestamp'
            ]

            # Add timestamp to each record
            timestamp = datetime.now().isoformat()
            for url_data in urls_data:
                url_data['discovery_timestamp'] = timestamp

            # Write to CSV
            mode = 'a' if append and self.output_csv.exists() else 'w'
            with open(self.output_csv, mode, newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write header only if creating new file
                if mode == 'w':
                    writer.writeheader()

                writer.writerows(urls_data)

            self.logger.info(f"Saved {len(urls_data)} URLs to {self.output_csv}")

        except Exception as e:
            self.logger.error(f"Error saving URLs to CSV: {e}")

    def print_progress_stats(self):
        """Print current progress statistics."""
        if self.stats['start_time']:
            elapsed = datetime.now() - self.stats['start_time']
            elapsed_str = str(elapsed).split('.')[0]  # Remove microseconds
        else:
            elapsed_str = "00:00:00"

        progress_pct = (self.stats['processed_combinations'] / max(self.stats['total_combinations'], 1)) * 100

        self.logger.info(f"""
=== Progress Report ===
Elapsed Time: {elapsed_str}
Progress: {self.stats['processed_combinations']:,} / {self.stats['total_combinations']:,} ({progress_pct:.1f}%)
Successful Requests: {self.stats['successful_requests']:,}
Failed Requests: {self.stats['failed_requests']:,}
Help Pages Skipped: {self.stats['help_pages_skipped']:,}
Database Error Pages Skipped: {self.stats['database_error_pages_skipped']:,}
Justel URLs Found: {self.stats['justel_urls_found']:,}
Pages with Results: {self.stats['pages_with_single_result'] + self.stats['pages_with_multiple_results']:,}
Pages with No Results: {self.stats['pages_with_no_results']:,}
Duplicates Filtered: {self.stats['duplicate_urls_filtered']:,}
=======================""")

    async def run_discovery(self):
        """
        Main method to run the URL discovery process.
        """
        self.logger.info("Starting eJustice URL discovery process...")
        self.stats['start_time'] = datetime.now()

        # Initialize CSV file with headers if not resuming
        if not self.resume or not self.output_csv.exists():
            self.save_urls_to_csv([], append=False)

        # Use larger batches for better throughput - process 2x concurrent requests per batch
        batch_size = self.concurrent_requests * 2
        url_batch = []
        batch_results = []

        # Configure HTTP client
        async with httpx.AsyncClient(**self.client_config) as session:

            # Process URL combinations in batches
            for combination in self.generate_url_combinations():
                url_batch.append(combination)

                # Process batch when it reaches the desired size
                if len(url_batch) >= batch_size:
                    batch_urls = await self.process_url_batch(url_batch, session)
                    batch_results.extend(batch_urls)

                    # Save results periodically (every 20 batches for better performance)
                    if len(batch_results) >= batch_size * 20:
                        self.save_urls_to_csv(batch_results)
                        batch_results = []

                    # Save checkpoint less frequently to reduce I/O overhead
                    if self.stats['processed_combinations'] % (batch_size * 50) == 0:
                        self.save_checkpoint()
                        self.print_progress_stats()

                    # Clear batch and add delay
                    url_batch = []
                    if self.delay > 0:
                        await asyncio.sleep(self.delay)

            # Process remaining URLs in the last batch
            if url_batch:
                batch_urls = await self.process_url_batch(url_batch, session)
                batch_results.extend(batch_urls)

            # Save any remaining results
            if batch_results:
                self.save_urls_to_csv(batch_results)

        # Final checkpoint and statistics
        self.save_checkpoint()
        self.print_final_stats()

    def print_final_stats(self):
        """Print final statistics summary."""
        if self.stats['start_time']:
            total_time = datetime.now() - self.stats['start_time']
            total_time_str = str(total_time).split('.')[0]
        else:
            total_time_str = "00:00:00"

        self.logger.info(f"""
=== FINAL RESULTS ===
Total Runtime: {total_time_str}
Total Combinations Processed: {self.stats['processed_combinations']:,}
Successful Requests: {self.stats['successful_requests']:,}
Failed Requests: {self.stats['failed_requests']:,}
Help Pages Skipped: {self.stats['help_pages_skipped']:,}
Database Error Pages Skipped: {self.stats['database_error_pages_skipped']:,}
Total Justel URLs Discovered: {self.stats['justel_urls_found']:,}
Unique URLs (after deduplication): {len(self.discovered_urls):,}
Pages with Single Result: {self.stats['pages_with_single_result']:,}
Pages with Multiple Results: {self.stats['pages_with_multiple_results']:,}
Pages with No Results: {self.stats['pages_with_no_results']:,}
Duplicates Filtered: {self.stats['duplicate_urls_filtered']:,}
Output File: {self.output_csv}
Checkpoint File: {self.checkpoint_file}
====================""")


def main():
    """Main function with command-line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Belgian eJustice URL Discovery Scraper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run full discovery (will take days/weeks)
  python ejustice_url_discovery_scraper.py

  # Test mode with limited combinations
  python ejustice_url_discovery_scraper.py --test --test-limit 50

  # Resume from checkpoint
  python ejustice_url_discovery_scraper.py --resume

  # Custom year range
  python ejustice_url_discovery_scraper.py --start-year 2000 --end-year 2023

  # Faster processing (more concurrent requests)
  python ejustice_url_discovery_scraper.py --concurrent 15 --delay 0.1
        """
    )

    parser.add_argument("--output", "-o",
                       default="data/csv_data/ejustice_urls.csv",
                       help="Output CSV file path (default: data/csv_data/ejustice_urls.csv)")

    parser.add_argument("--checkpoint", "-c",
                       default="data/csv_data/ejustice_checkpoint.json",
                       help="Checkpoint file path (default: data/csv_data/ejustice_checkpoint.json)")

    parser.add_argument("--start-year", "-s", type=int, default=1789,
                       help="Starting year for discovery (default: 1789)")

    parser.add_argument("--end-year", "-e", type=int,
                       help="Ending year for discovery (default: current year)")

    parser.add_argument("--delay", "-d", type=float, default=0.05,
                       help="Delay between request batches in seconds (default: 0.05)")

    parser.add_argument("--concurrent", type=int, default=20,
                       help="Number of concurrent requests (default: 20)")

    parser.add_argument("--test", "-t", action="store_true",
                       help="Run in test mode (process limited combinations)")

    parser.add_argument("--test-limit", type=int, default=100,
                       help="Number of combinations to process in test mode (default: 100)")

    parser.add_argument("--resume", "-r", action="store_true", default=True,
                       help="Resume from checkpoint if available (default: True)")

    parser.add_argument("--no-resume", action="store_true",
                       help="Start fresh, ignore any existing checkpoint")

    args = parser.parse_args()

    # Handle resume logic
    resume = args.resume and not args.no_resume

    # Create scraper instance
    scraper = EJusticeURLDiscoveryScraper(
        output_csv=args.output,
        checkpoint_file=args.checkpoint,
        start_year=args.start_year,
        end_year=args.end_year,
        delay=args.delay,
        concurrent_requests=args.concurrent,
        test_mode=args.test,
        test_limit=args.test_limit,
        resume=resume
    )

    # Print configuration
    print(f"""
=== eJustice URL Discovery Scraper ===
Output CSV: {args.output}
Checkpoint: {args.checkpoint}
Year Range: {args.start_year} - {args.end_year or 'current'}
Delay: {args.delay}s
Concurrent Requests: {args.concurrent}
Test Mode: {args.test}
Resume: {resume}
======================================
""")

    # Confirm before starting (unless in test mode)
    if not args.test:
        estimated_combinations = len(EJusticeURLDiscoveryScraper.DOCUMENT_TYPES) * \
                               (args.end_year or datetime.now().year - args.start_year + 1) * \
                               365  # Rough estimate

        print(f"⚠️  WARNING: This will process approximately {estimated_combinations:,} URL combinations.")
        print("This could take several days or weeks to complete.")
        print("Make sure you have sufficient disk space and network bandwidth.")

        # response = input("\nDo you want to continue? (y/N): ")
        # if response.lower() not in ['y', 'yes']:
        #     print("Operation cancelled.")
        #     return

    # Run the discovery process
    try:
        asyncio.run(scraper.run_discovery())
        print("\n✅ URL discovery completed successfully!")

    except KeyboardInterrupt:
        print("\n⚠️ Process interrupted by user. Progress has been saved to checkpoint.")
        scraper.save_checkpoint()

    except Exception as e:
        print(f"\n❌ Error during discovery: {e}")
        scraper.logger.error(f"Fatal error: {e}")
        scraper.save_checkpoint()
        sys.exit(1)


if __name__ == "__main__":
    main()
