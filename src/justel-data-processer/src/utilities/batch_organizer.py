#!/usr/bin/env python3
"""
batch_organizer.py - Organize valid JSON files into batches for easier processing

This script reads all JSON files from the valid_jsons/ directory and organizes them
into batches of exactly 100 files each (with the last batch containing the remainder).
Creates numbered subdirectories and provides a comprehensive summary report.

Author: Augment Agent
Date: 2025-07-14
"""

import os
import shutil
import json
from pathlib import Path
from typing import List, Dict, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/batch_organizer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class JSONBatchOrganizer:
    """
    Organizes valid JSON files into batches for easier processing and review.
    """
    
    def __init__(self, source_dir: str = "valid_jsons", target_dir: str = "valid_jsons_batched", batch_size: int = 100):
        """
        Initialize the batch organizer.
        
        Args:
            source_dir: Directory containing valid JSON files
            target_dir: Directory to create batched subdirectories
            batch_size: Number of files per batch (default: 100)
        """
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.batch_size = batch_size
        self.stats = {
            'total_files': 0,
            'total_batches': 0,
            'files_processed': 0,
            'files_failed': 0,
            'batch_details': []
        }
    
    def validate_directories(self) -> bool:
        """Validate source directory and create target directory."""
        try:
            # Check source directory
            if not self.source_dir.exists():
                logger.error(f"Source directory does not exist: {self.source_dir}")
                return False
            
            if not self.source_dir.is_dir():
                logger.error(f"Source path is not a directory: {self.source_dir}")
                return False
            
            # Create target directory
            self.target_dir.mkdir(parents=True, exist_ok=True)
            logger.info(f"Target directory created/verified: {self.target_dir}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error validating directories: {e}")
            return False
    
    def get_json_files(self) -> List[Path]:
        """Get all JSON files from the source directory."""
        try:
            json_files = []
            for file_path in self.source_dir.iterdir():
                if file_path.is_file() and file_path.suffix.lower() == '.json':
                    json_files.append(file_path)
            
            # Sort files for consistent processing order
            json_files.sort(key=lambda x: x.name)
            
            logger.info(f"Found {len(json_files)} JSON files in {self.source_dir}")
            return json_files
            
        except Exception as e:
            logger.error(f"Error reading JSON files from {self.source_dir}: {e}")
            return []
    
    def create_batches(self, json_files: List[Path]) -> List[List[Path]]:
        """Create batches of files."""
        batches = []
        
        for i in range(0, len(json_files), self.batch_size):
            batch = json_files[i:i + self.batch_size]
            batches.append(batch)
        
        logger.info(f"Created {len(batches)} batches with batch size {self.batch_size}")
        return batches
    
    def copy_batch_files(self, batch_files: List[Path], batch_dir: Path) -> Tuple[int, int]:
        """
        Copy files to batch directory.
        
        Returns:
            Tuple of (successful_copies, failed_copies)
        """
        successful = 0
        failed = 0
        
        for file_path in batch_files:
            try:
                target_path = batch_dir / file_path.name
                shutil.copy2(file_path, target_path)
                successful += 1
                
            except Exception as e:
                logger.error(f"Failed to copy {file_path.name}: {e}")
                failed += 1
        
        return successful, failed
    
    def validate_json_file(self, file_path: Path) -> bool:
        """Validate that a file contains valid JSON."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json.load(f)
            return True
        except Exception as e:
            logger.warning(f"Invalid JSON file {file_path.name}: {e}")
            return False
    
    def organize_batches(self) -> bool:
        """Main method to organize files into batches."""
        try:
            logger.info("Starting batch organization process...")
            
            # Validate directories
            if not self.validate_directories():
                return False
            
            # Get JSON files
            json_files = self.get_json_files()
            if not json_files:
                logger.warning("No JSON files found to process")
                return True
            
            self.stats['total_files'] = len(json_files)
            
            # Create batches
            batches = self.create_batches(json_files)
            self.stats['total_batches'] = len(batches)
            
            # Process each batch
            for batch_num, batch_files in enumerate(batches, 1):
                batch_name = f"batch_{batch_num:03d}"
                batch_dir = self.target_dir / batch_name
                
                # Create batch directory
                batch_dir.mkdir(exist_ok=True)
                
                # Copy files to batch directory
                logger.info(f"Processing {batch_name} with {len(batch_files)} files...")
                successful, failed = self.copy_batch_files(batch_files, batch_dir)
                
                # Update statistics
                self.stats['files_processed'] += successful
                self.stats['files_failed'] += failed
                
                # Store batch details
                batch_info = {
                    'batch_name': batch_name,
                    'file_count': len(batch_files),
                    'successful_copies': successful,
                    'failed_copies': failed,
                    'first_files': [f.name for f in batch_files[:5]]  # First 5 files for verification
                }
                self.stats['batch_details'].append(batch_info)
                
                # Progress indicator
                if batch_num % 5 == 0 or batch_num == len(batches):
                    logger.info(f"Completed {batch_num}/{len(batches)} batches...")
            
            logger.info("Batch organization completed successfully!")
            return True
            
        except Exception as e:
            logger.error(f"Error during batch organization: {e}")
            return False
    
    def generate_summary_report(self) -> str:
        """Generate a comprehensive summary report."""
        report_lines = [
            "=" * 80,
            "BATCH ORGANIZATION SUMMARY REPORT",
            "=" * 80,
            f"Source Directory: {self.source_dir}",
            f"Target Directory: {self.target_dir}",
            f"Batch Size: {self.batch_size} files per batch",
            "",
            "PROCESSING STATISTICS:",
            f"  Total JSON files found: {self.stats['total_files']}",
            f"  Total batches created: {self.stats['total_batches']}",
            f"  Files successfully processed: {self.stats['files_processed']}",
            f"  Files failed to process: {self.stats['files_failed']}",
            "",
            "BATCH DETAILS:",
        ]
        
        for batch_info in self.stats['batch_details']:
            report_lines.extend([
                f"  📁 {batch_info['batch_name']}:",
                f"     Files: {batch_info['file_count']} (✅ {batch_info['successful_copies']}, ❌ {batch_info['failed_copies']})",
                f"     Sample files: {', '.join(batch_info['first_files'])}",
                ""
            ])
        
        # Add final batch information if it's not a full batch
        if self.stats['batch_details']:
            last_batch = self.stats['batch_details'][-1]
            if last_batch['file_count'] < self.batch_size:
                report_lines.extend([
                    "SPECIAL NOTES:",
                    f"  ⚠️  Final batch ({last_batch['batch_name']}) contains {last_batch['file_count']} files (less than {self.batch_size})",
                    ""
                ])
        
        report_lines.extend([
            "DIRECTORY STRUCTURE CREATED:",
            f"  {self.target_dir}/",
        ])
        
        for batch_info in self.stats['batch_details']:
            report_lines.append(f"    ├── {batch_info['batch_name']}/  ({batch_info['file_count']} files)")
        
        report_lines.extend([
            "",
            "✅ Batch organization completed successfully!",
            f"📂 Batched files are available in: {self.target_dir}/",
            "=" * 80
        ])
        
        return "\n".join(report_lines)
    
    def save_report(self, report: str, filename: str = "batch_organization_report.txt") -> None:
        """Save the summary report to a file."""
        try:
            report_path = self.target_dir / filename
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
            logger.info(f"Summary report saved to: {report_path}")
        except Exception as e:
            logger.error(f"Failed to save report: {e}")


def main():
    """Main execution function."""
    try:
        # Create batch organizer
        organizer = JSONBatchOrganizer(
            source_dir="valid_jsons",
            target_dir="valid_jsons_batched",
            batch_size=100
        )
        
        # Organize files into batches
        success = organizer.organize_batches()
        
        if success:
            # Generate and display summary report
            report = organizer.generate_summary_report()
            print(report)
            
            # Save report to file
            organizer.save_report(report)
            
            return True
        else:
            logger.error("Batch organization failed")
            return False
            
    except Exception as e:
        logger.error(f"Unexpected error in main: {e}")
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
