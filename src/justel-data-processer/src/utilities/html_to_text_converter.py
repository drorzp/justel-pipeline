#!/usr/bin/env python3
"""
HTML to Text Converter for Belgian Legal Document Processing Pipeline

This script converts HTML files from the input_html/ directory to text files
in the input/ directory, changing file extensions from .html to .txt while
preserving document IDs and handling conflicts gracefully.

Usage:
    python src/utilities/html_to_text_converter.py [options]

Features:
- Batch conversion with progress indicators
- Conflict detection and handling
- Detailed logging
- Dry-run mode for testing
- Resume capability for interrupted conversions
"""

import os
import sys
import shutil
import logging
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Optional


class HTMLToTextConverter:
    """Converts HTML files to text files with proper logging and error handling."""
    
    def __init__(self, 
                 source_dir: str = "input_html",
                 target_dir: str = "input", 
                 dry_run: bool = False,
                 overwrite: bool = False,
                 log_level: str = "INFO"):
        """
        Initialize the converter.
        
        Args:
            source_dir: Source directory containing HTML files
            target_dir: Target directory for text files
            dry_run: If True, only simulate the conversion without actual file operations
            overwrite: If True, overwrite existing files in target directory
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        """
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.dry_run = dry_run
        self.overwrite = overwrite
        
        # Setup logging
        self.setup_logging(log_level)
        
        # Statistics
        self.stats = {
            'total_files': 0,
            'converted': 0,
            'skipped': 0,
            'errors': 0,
            'conflicts': 0
        }
        
    def setup_logging(self, log_level: str):
        """Setup logging configuration."""
        # Create logs directory if it doesn't exist
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        # Create log filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"html_to_text_converter_{timestamp}.log"
        
        # Configure logging
        logging.basicConfig(
            level=getattr(logging, log_level.upper()),
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"HTML to Text Converter initialized")
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
        
    def get_document_id(self, html_file: Path) -> str:
        """Extract document ID from HTML filename."""
        return html_file.stem  # Remove .html extension
        
    def check_conflicts(self, html_files: List[Path]) -> List[Tuple[Path, Path]]:
        """Check for potential conflicts in target directory."""
        conflicts = []
        
        for html_file in html_files:
            doc_id = self.get_document_id(html_file)
            target_file = self.target_dir / f"{doc_id}.txt"
            
            if target_file.exists() and not self.overwrite:
                conflicts.append((html_file, target_file))
                
        if conflicts:
            self.logger.warning(f"Found {len(conflicts)} potential conflicts")
            for html_file, target_file in conflicts[:5]:  # Show first 5
                self.logger.warning(f"  Conflict: {html_file.name} -> {target_file.name} (exists)")
            if len(conflicts) > 5:
                self.logger.warning(f"  ... and {len(conflicts) - 5} more conflicts")
                
        return conflicts
        
    def convert_file(self, html_file: Path) -> bool:
        """Convert a single HTML file to text file (simple copy with extension change)."""
        try:
            doc_id = self.get_document_id(html_file)
            target_file = self.target_dir / f"{doc_id}.txt"

            # Check if target exists and we're not overwriting
            if target_file.exists() and not self.overwrite:
                self.logger.debug(f"Skipping {html_file.name} - target exists")
                self.stats['skipped'] += 1
                self.stats['conflicts'] += 1
                return False

            if self.dry_run:
                self.logger.info(f"DRY RUN: Would convert {html_file.name} -> {target_file.name}")
                self.stats['converted'] += 1
                return True

            # Simple copy with extension change
            shutil.copy2(html_file, target_file)

            self.logger.debug(f"Converted: {html_file.name} -> {target_file.name}")
            self.stats['converted'] += 1
            return True

        except Exception as e:
            self.logger.error(f"Error converting {html_file.name}: {e}")
            self.stats['errors'] += 1
            return False
            
    def convert_all(self) -> bool:
        """Convert all HTML files to text files."""
        self.logger.info("Starting HTML to text conversion...")
        
        # Validate directories
        if not self.validate_directories():
            return False
            
        # Get HTML files
        html_files = self.get_html_files()
        if not html_files:
            self.logger.warning("No HTML files found to convert")
            return True
            
        self.stats['total_files'] = len(html_files)
        
        # Check for conflicts
        conflicts = self.check_conflicts(html_files)
        if conflicts and not self.overwrite:
            self.logger.warning(f"Found {len(conflicts)} conflicts. Use --overwrite to force conversion.")
            
        # Convert files
        self.logger.info(f"Converting {len(html_files)} files...")
        
        for i, html_file in enumerate(html_files, 1):
            # Progress indicator
            if i % 100 == 0 or i == len(html_files):
                progress = (i / len(html_files)) * 100
                self.logger.info(f"Progress: {i}/{len(html_files)} ({progress:.1f}%)")
                
            self.convert_file(html_file)
            
        # Print summary
        self.print_summary()
        return True
        
    def print_summary(self):
        """Print conversion summary."""
        self.logger.info("=" * 60)
        self.logger.info("CONVERSION SUMMARY")
        self.logger.info("=" * 60)
        self.logger.info(f"Total files found: {self.stats['total_files']}")
        self.logger.info(f"Successfully converted: {self.stats['converted']}")
        self.logger.info(f"Skipped (conflicts): {self.stats['skipped']}")
        self.logger.info(f"Errors: {self.stats['errors']}")
        
        if self.stats['total_files'] > 0:
            success_rate = (self.stats['converted'] / self.stats['total_files']) * 100
            self.logger.info(f"Success rate: {success_rate:.1f}%")
            
        if self.dry_run:
            self.logger.info("DRY RUN MODE - No files were actually converted")
        else:
            self.logger.info(f"Files saved to: {self.target_dir}")


def main():
    """Main function with command-line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Convert HTML files to text files for Belgian legal document processing"
    )
    parser.add_argument("--source", "-s", default="input_html",
                       help="Source directory containing HTML files (default: input_html)")
    parser.add_argument("--target", "-t", default="input", 
                       help="Target directory for text files (default: input)")
    parser.add_argument("--dry-run", "-n", action="store_true",
                       help="Simulate conversion without actually copying files")
    parser.add_argument("--overwrite", "-f", action="store_true",
                       help="Overwrite existing files in target directory")
    parser.add_argument("--log-level", "-l", default="INFO",
                       choices=["DEBUG", "INFO", "WARNING", "ERROR"],
                       help="Set logging level (default: INFO)")
    
    args = parser.parse_args()
    
    # Create converter and run
    converter = HTMLToTextConverter(
        source_dir=args.source,
        target_dir=args.target,
        dry_run=args.dry_run,
        overwrite=args.overwrite,
        log_level=args.log_level
    )
    
    success = converter.convert_all()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
