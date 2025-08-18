#!/usr/bin/env python3
"""
HTML to Text Batch Converter for Belgian Legal Documents

This script converts HTML files from input_latest/ directory to clean text files
and saves them to the input/ directory. It performs proper HTML parsing and text
extraction to produce clean, readable content.

Features:
- Batch conversion with progress tracking
- Duplicate checking (skips existing files)
- Proper HTML-to-text conversion using selectolax
- Error handling and logging
- Resume capability
- Preserves existing files in input/ directory

Usage:
    python src/utilities/html_to_text_batch_converter.py [options]
"""

import sys
import logging
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Set
import re

from selectolax.parser import HTMLParser


class HTMLToTextBatchConverter:
    """Converts HTML files to clean text files with proper parsing."""

    def __init__(self,
                 source_dir: str = "input_latest",
                 target_dir: str = "input",
                 dry_run: bool = False,
                 log_level: str = "INFO"):
        """
        Initialize the batch converter.

        Args:
            source_dir: Source directory containing HTML files
            target_dir: Target directory for text files
            dry_run: If True, only simulate conversion without actual file operations
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        """
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.dry_run = dry_run

        # Setup logging
        self.setup_logging(log_level)

        # Statistics
        self.stats = {
            'total_files': 0,
            'converted': 0,
            'skipped': 0,
            'errors': 0,
            'existing_files': 0
        }

    def setup_logging(self, log_level: str):
        """Setup logging configuration."""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"html_to_text_batch_{timestamp}.log"

        logging.basicConfig(
            level=getattr(logging, log_level.upper()),
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler(sys.stdout)
            ]
        )

        self.logger = logging.getLogger(__name__)
        self.logger.info("HTML to Text Batch Converter initialized")
        self.logger.info(f"Source directory: {self.source_dir}")
        self.logger.info(f"Target directory: {self.target_dir}")
        self.logger.info(f"Dry run mode: {self.dry_run}")
        self.logger.info(f"Log file: {log_file}")

    def validate_directories(self) -> bool:
        """Validate source and target directories."""
        if not self.source_dir.exists():
            self.logger.error(f"Source directory does not exist: {self.source_dir}")
            return False

        if not self.source_dir.is_dir():
            self.logger.error(f"Source path is not a directory: {self.source_dir}")
            return False

        # Create target directory if it doesn't exist
        if not self.dry_run:
            self.target_dir.mkdir(parents=True, exist_ok=True)
            self.logger.info(f"Target directory created/verified: {self.target_dir}")
        else:
            self.logger.info(f"DRY RUN: Would create target directory: {self.target_dir}")

        return True

    def get_html_files(self) -> List[Path]:
        """Get list of HTML files from source directory."""
        html_files = list(self.source_dir.glob("*.html"))
        html_files.sort()  # Sort for consistent processing order

        self.logger.info(f"Found {len(html_files)} HTML files in {self.source_dir}")
        return html_files

    def get_existing_txt_files(self) -> Set[str]:
        """Get set of existing TXT file stems in target directory."""
        existing_files = set()
        if self.target_dir.exists():
            for txt_file in self.target_dir.glob("*.txt"):
                existing_files.add(txt_file.stem)

        self.logger.info(f"Found {len(existing_files)} existing TXT files in {self.target_dir}")
        return existing_files

    def html_to_text(self, html_content: str) -> str:
        """
        Convert HTML content to clean text using selectolax.

        Args:
            html_content: Raw HTML content

        Returns:
            Clean text content
        """
        try:
            # Parse HTML
            tree = HTMLParser(html_content)

            # Remove script and style elements
            for tag in tree.css('script, style'):
                tag.decompose()

            # Extract text content
            text = tree.text(separator=' ', strip=True)

            # Clean up whitespace
            text = re.sub(r'\s+', ' ', text)
            text = text.strip()

            return text

        except Exception as e:
            self.logger.error(f"Error converting HTML to text: {e}")
            return ""

    def convert_file(self, html_file: Path, existing_files: Set[str]) -> bool:
        """
        Convert a single HTML file to text file.

        Args:
            html_file: Path to HTML file
            existing_files: Set of existing TXT file stems

        Returns:
            True if successful, False otherwise
        """
        try:
            doc_id = html_file.stem
            target_file = self.target_dir / f"{doc_id}.txt"

            # Check if target already exists
            if doc_id in existing_files:
                self.logger.debug(f"Skipping {html_file.name} - target exists: {target_file.name}")
                self.stats['skipped'] += 1
                return False

            if self.dry_run:
                self.logger.info(f"DRY RUN: Would convert {html_file.name} -> {target_file.name}")
                self.stats['converted'] += 1
                return True

            # Read HTML content
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # Convert HTML to text
            text_content = self.html_to_text(html_content)

            if not text_content or len(text_content.strip()) < 50:
                self.logger.warning(f"Converted text too short for {html_file.name}")
                self.stats['errors'] += 1
                return False

            # Save text file
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(text_content)

            self.logger.debug(f"Converted: {html_file.name} -> {target_file.name}")
            self.stats['converted'] += 1
            return True

        except Exception as e:
            self.logger.error(f"Error converting {html_file.name}: {e}")
            self.stats['errors'] += 1
            return False

    def convert_all(self) -> bool:
        """Convert all HTML files to text files."""
        self.logger.info("Starting HTML to text batch conversion...")

        # Validate directories
        if not self.validate_directories():
            return False

        # Get HTML files
        html_files = self.get_html_files()
        if not html_files:
            self.logger.warning("No HTML files found to convert")
            return True

        # Get existing TXT files
        existing_files = self.get_existing_txt_files()
        self.stats['total_files'] = len(html_files)
        self.stats['existing_files'] = len(existing_files)

        # Convert files
        self.logger.info(f"Converting {len(html_files)} HTML files...")
        self.logger.info(f"Will skip {len(existing_files)} files that already exist as TXT")

        for i, html_file in enumerate(html_files, 1):
            # Progress indicator
            if i % 500 == 0 or i == len(html_files):
                progress = (i / len(html_files)) * 100
                self.logger.info(f"Progress: {i}/{len(html_files)} ({progress:.1f}%)")

            self.convert_file(html_file, existing_files)

        # Print summary
        self.print_summary()
        return True

    def print_summary(self):
        """Print conversion summary."""
        self.logger.info("\n" + "=" * 60)
        self.logger.info("HTML TO TEXT CONVERSION SUMMARY")
        self.logger.info("=" * 60)
        self.logger.info(f"Total HTML files found: {self.stats['total_files']:,}")
        self.logger.info(f"Existing TXT files (skipped): {self.stats['skipped']:,}")
        self.logger.info(f"Successfully converted: {self.stats['converted']:,}")
        self.logger.info(f"Errors: {self.stats['errors']:,}")

        if self.stats['total_files'] > 0:
            success_rate = (self.stats['converted'] / self.stats['total_files']) * 100
            self.logger.info(f"Success rate: {success_rate:.1f}%")

        if self.dry_run:
            self.logger.info("DRY RUN MODE - No files were actually converted")
        else:
            self.logger.info(f"TXT files saved to: {self.target_dir}")


def main():
    """Main function with command-line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Convert HTML files to clean text files for Belgian legal documents"
    )
    parser.add_argument("--source", "-s", default="input_latest",
                       help="Source directory containing HTML files (default: input_latest)")
    parser.add_argument("--target", "-t", default="input",
                       help="Target directory for text files (default: input)")
    parser.add_argument("--dry-run", "-n", action="store_true",
                       help="Simulate conversion without actually creating files")
    parser.add_argument("--log-level", "-l", default="INFO",
                       choices=["DEBUG", "INFO", "WARNING", "ERROR"],
                       help="Set logging level (default: INFO)")

    args = parser.parse_args()

    # Create converter and run
    converter = HTMLToTextBatchConverter(
        source_dir=args.source,
        target_dir=args.target,
        dry_run=args.dry_run,
        log_level=args.log_level
    )

    success = converter.convert_all()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
