#!/usr/bin/env python3
"""
Simple Directory Restructuring Script for Belgian Legal Document Processing

This script reorganizes the data directories following a simple, maintainable structure:
- input_html/ → data/html_raw/
- input/ → data/text_input/  
- excel/ → data/csv_data/

Usage:
    python src/utilities/restructure_directories.py [--dry-run] [--backup]
"""

import os
import sys
import shutil
import logging
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple


class DirectoryRestructurer:
    """Simple directory restructuring with backup and rollback capabilities."""
    
    def __init__(self, dry_run: bool = False, create_backup: bool = True):
        """
        Initialize the restructurer.

        Args:
            dry_run: If True, only simulate the restructuring
            create_backup: If True, create backup before restructuring
        """
        self.dry_run = dry_run
        self.should_create_backup = create_backup
        
        # Define the simple mapping
        self.directory_mapping = {
            "input_html": "data/html_raw",
            "input": "data/text_input", 
            "excel": "data/csv_data"
        }
        
        # Setup logging
        self.setup_logging()
        
        # Statistics
        self.stats = {
            'directories_moved': 0,
            'files_moved': 0,
            'errors': 0
        }
        
    def setup_logging(self):
        """Setup simple logging."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[logging.StreamHandler(sys.stdout)]
        )
        self.logger = logging.getLogger(__name__)
        
    def check_prerequisites(self) -> bool:
        """Check if restructuring can proceed."""
        self.logger.info("Checking prerequisites...")
        
        # Check if source directories exist
        missing_dirs = []
        for old_dir in self.directory_mapping.keys():
            if not Path(old_dir).exists():
                missing_dirs.append(old_dir)
                
        if missing_dirs:
            self.logger.warning(f"Missing source directories: {missing_dirs}")
            self.logger.info("This is normal if directories were already moved or don't exist yet")
            
        # Check if target directories already exist
        existing_targets = []
        for new_dir in self.directory_mapping.values():
            if Path(new_dir).exists():
                existing_targets.append(new_dir)
                
        if existing_targets:
            self.logger.warning(f"Target directories already exist: {existing_targets}")
            response = input("Continue anyway? (y/N): ")
            if response.lower() != 'y':
                return False
                
        return True
        
    def create_backup(self) -> str:
        """Create backup of current structure."""
        if not self.should_create_backup:
            return ""
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = f"backup_before_restructure_{timestamp}"
        
        self.logger.info(f"Creating backup: {backup_dir}")
        
        if self.dry_run:
            self.logger.info(f"DRY RUN: Would create backup directory {backup_dir}")
            return backup_dir
            
        # Create backup directory
        Path(backup_dir).mkdir(exist_ok=True)
        
        # Copy directories that will be moved
        for old_dir in self.directory_mapping.keys():
            if Path(old_dir).exists():
                backup_path = Path(backup_dir) / old_dir
                shutil.copytree(old_dir, backup_path)
                self.logger.info(f"Backed up: {old_dir} → {backup_path}")
                
        return backup_dir
        
    def create_new_structure(self):
        """Create the new directory structure."""
        self.logger.info("Creating new directory structure...")
        
        # Create data parent directory
        if self.dry_run:
            self.logger.info("DRY RUN: Would create data/ directory")
        else:
            Path("data").mkdir(exist_ok=True)
            self.logger.info("Created: data/")
            
        # Create target directories
        for new_dir in self.directory_mapping.values():
            if self.dry_run:
                self.logger.info(f"DRY RUN: Would create {new_dir}/")
            else:
                Path(new_dir).mkdir(parents=True, exist_ok=True)
                self.logger.info(f"Created: {new_dir}/")
                
    def move_directory_contents(self, source: str, target: str) -> bool:
        """Move contents from source to target directory."""
        source_path = Path(source)
        target_path = Path(target)
        
        if not source_path.exists():
            self.logger.warning(f"Source directory doesn't exist: {source}")
            return True  # Not an error, just skip
            
        if self.dry_run:
            file_count = len(list(source_path.iterdir()))
            self.logger.info(f"DRY RUN: Would move {file_count} items from {source} to {target}")
            self.stats['files_moved'] += file_count
            return True
            
        try:
            # Move all contents
            file_count = 0
            for item in source_path.iterdir():
                target_item = target_path / item.name
                shutil.move(str(item), str(target_item))
                file_count += 1
                
            self.logger.info(f"Moved {file_count} items: {source} → {target}")
            self.stats['files_moved'] += file_count
            
            # Remove empty source directory
            source_path.rmdir()
            self.logger.info(f"Removed empty directory: {source}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error moving {source} to {target}: {e}")
            self.stats['errors'] += 1
            return False
            
    def restructure(self) -> bool:
        """Perform the directory restructuring."""
        self.logger.info("Starting directory restructuring...")
        self.logger.info(f"Dry run mode: {self.dry_run}")
        
        # Check prerequisites
        if not self.check_prerequisites():
            return False
            
        # Create backup
        backup_dir = self.create_backup()
        if backup_dir:
            self.logger.info(f"Backup created: {backup_dir}")
            
        # Create new structure
        self.create_new_structure()
        
        # Move directories
        self.logger.info("Moving directories...")
        success = True
        
        for old_dir, new_dir in self.directory_mapping.items():
            self.logger.info(f"Processing: {old_dir} → {new_dir}")
            if self.move_directory_contents(old_dir, new_dir):
                self.stats['directories_moved'] += 1
            else:
                success = False
                
        # Print summary
        self.print_summary()
        
        if success and not self.dry_run:
            self.logger.info("✅ Directory restructuring completed successfully!")
            self.logger.info("Next steps:")
            self.logger.info("1. Update script paths using: python src/utilities/update_script_paths.py")
            self.logger.info("2. Update .gitignore file")
            self.logger.info("3. Test the processing pipeline")
        elif success and self.dry_run:
            self.logger.info("✅ Dry run completed successfully!")
            self.logger.info("Run without --dry-run to perform actual restructuring")
        else:
            self.logger.error("❌ Directory restructuring failed!")
            if backup_dir:
                self.logger.info(f"Restore from backup if needed: {backup_dir}")
                
        return success
        
    def print_summary(self):
        """Print restructuring summary."""
        self.logger.info("=" * 50)
        self.logger.info("RESTRUCTURING SUMMARY")
        self.logger.info("=" * 50)
        self.logger.info(f"Directories moved: {self.stats['directories_moved']}")
        self.logger.info(f"Files moved: {self.stats['files_moved']}")
        self.logger.info(f"Errors: {self.stats['errors']}")


def main():
    """Main function with command-line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Simple directory restructuring for Belgian legal document processing"
    )
    parser.add_argument("--dry-run", "-n", action="store_true",
                       help="Simulate restructuring without actually moving files")
    parser.add_argument("--no-backup", action="store_true",
                       help="Skip creating backup (not recommended)")
    
    args = parser.parse_args()
    
    # Create restructurer and run
    restructurer = DirectoryRestructurer(
        dry_run=args.dry_run,
        create_backup=not args.no_backup
    )
    
    success = restructurer.restructure()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
