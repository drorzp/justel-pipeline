#!/usr/bin/env python3
"""
Comprehensive Belgian Legal Document Processing Pipeline

 python comprehensive_pipeline.py --process-all --batch-size=1000

This script orchestrates the complete processing pipeline:
1. Environment preparation (cleanup output directory)
2. Document processing (first 1000 files through 000_Master.py)
3. Quality filtering and S3 upload (JSON files with document_hierarchy)

Features:
- Comprehensive logging and error handling
- Dry-run capability for testing
- Progress tracking for all phases
- Safety checks and confirmations
- Automatic cleanup and rollback mechanisms
"""

import os
import sys
import json
import shutil
import zipfile
import logging
import argparse
import subprocess
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import glob
import tempfile


class ComprehensivePipeline:
    """Main pipeline orchestrator class."""
    
    def __init__(self, dry_run: bool = False, max_files: int = 10000000, log_level: str = "INFO",
                 batch_size: int = 1000, start_batch: int = 1, process_all: bool = False):
        """Initialize the pipeline."""
        self.dry_run = dry_run
        self.max_files = max_files
        self.batch_size = batch_size
        self.start_batch = start_batch
        self.process_all = process_all
        self.script_dir = Path(__file__).parent.absolute()

        # Directory paths
        self.input_dir = self.script_dir / "input"
        self.output_dir = self.script_dir / "output"
        self.logs_dir = self.script_dir / "logs"
        self.master_script = self.script_dir / "000_Master.py"

        # Calculate total batches
        if self.process_all:
            # Get actual file count from input directory
            all_files = list(self.input_dir.glob("*.txt"))
            self.total_files = len(all_files)
            self.total_batches = (self.total_files + self.batch_size - 1) // self.batch_size
        else:
            self.total_files = self.max_files
            self.total_batches = (self.max_files + self.batch_size - 1) // self.batch_size

        # Statistics
        self.stats = {
            'total_files': self.total_files,
            'total_batches': self.total_batches,
            'current_batch': 0,
            'files_processed': 0,
            'json_files_created': 0,
            'valid_json_files': 0,
            'invalid_json_files': 0,
            'valid_zips_uploaded': 0,
            'invalid_zips_uploaded': 0,
            'upload_success': False,
            'cleanup_performed': False
        }

        # Setup logging
        self.setup_logging(log_level)
        
    def setup_logging(self, log_level: str):
        """Setup comprehensive logging."""
        self.logs_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = self.logs_dir / f"comprehensive_pipeline_{timestamp}.log"
        
        logging.basicConfig(
            level=getattr(logging, log_level.upper()),
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("=" * 80)
        self.logger.info("COMPREHENSIVE BELGIAN LEGAL DOCUMENT PROCESSING PIPELINE")
        self.logger.info("=" * 80)
        self.logger.info(f"Pipeline initialized - Dry run: {self.dry_run}")
        self.logger.info(f"Max files to process: {self.max_files}")
        self.logger.info(f"Log file: {log_file}")
        
    def check_prerequisites(self) -> bool:
        """Check if all prerequisites are met."""
        self.logger.info("🔍 Checking prerequisites...")
        
        # Check if master script exists
        if not self.master_script.exists():
            self.logger.error(f"Master script not found: {self.master_script}")
            return False
            
        # Check if input directory exists and has files
        if not self.input_dir.exists():
            self.logger.error(f"Input directory not found: {self.input_dir}")
            return False
            
        # Count available input files
        input_files = list(self.input_dir.glob("*.txt"))
        if len(input_files) == 0:
            self.logger.error("No .txt files found in input directory")
            return False
            
        self.logger.info(f"✅ Found {len(input_files):,} .txt files in input directory")
        
        # Check disk space (require at least 5GB free)
        try:
            statvfs = os.statvfs(self.script_dir)
            free_space_gb = (statvfs.f_frsize * statvfs.f_bavail) / (1024**3)
            if free_space_gb < 5:
                self.logger.warning(f"Low disk space: {free_space_gb:.1f}GB free")
            else:
                self.logger.info(f"✅ Sufficient disk space: {free_space_gb:.1f}GB free")
        except Exception as e:
            self.logger.warning(f"Could not check disk space: {e}")
            
        return True
        
    def phase1_environment_preparation(self) -> bool:
        """Phase 1: Clean output directory and prepare environment."""
        self.logger.info("\n" + "="*60)
        self.logger.info("PHASE 1: ENVIRONMENT PREPARATION")
        self.logger.info("="*60)
        
        try:
            # Check if output directory exists and has content
            if self.output_dir.exists():
                existing_files = list(self.output_dir.rglob("*"))
                existing_files = [f for f in existing_files if f.is_file()]
                
                if existing_files:
                    self.logger.info(f"Found {len(existing_files):,} existing files in output directory")

                    if not self.dry_run:
                        # Automatically clean up for unattended processing
                        self.logger.info(f"🧹 Automatically cleaning {len(existing_files):,} files for unattended processing")
                    
                    # Perform cleanup
                    self.logger.info("🧹 Cleaning output directory...")

                    if self.dry_run:
                        self.logger.info(f"DRY RUN: Would delete {len(existing_files):,} files")
                    else:
                        # Delete existing output directory
                        shutil.rmtree(self.output_dir)

                        # Create fresh output directory
                        self.output_dir.mkdir(exist_ok=True)

                        self.logger.info(f"✅ Cleaned output directory")
                        self.stats['cleanup_performed'] = True
                else:
                    self.logger.info("✅ Output directory is already clean")
            else:
                self.logger.info("Creating output directory...")
                if not self.dry_run:
                    self.output_dir.mkdir(exist_ok=True)
                self.logger.info("✅ Output directory created")
                
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Error in environment preparation: {e}")
            return False
            
    def get_first_n_files(self, n: int) -> List[Path]:
        """Get first N files from input directory in alphabetical order."""
        all_files = list(self.input_dir.glob("*.txt"))
        all_files.sort(key=lambda x: x.name)
        return all_files[:n]

    def get_batch_files(self, batch_number: int) -> List[Path]:
        """Get files for a specific batch from the input directory."""
        all_files = list(self.input_dir.glob("*.txt"))
        all_files.sort(key=lambda x: x.name)

        start_idx = (batch_number - 1) * self.batch_size
        end_idx = start_idx + self.batch_size

        batch_files = all_files[start_idx:end_idx]

        self.logger.info(f"Batch {batch_number}: Selected {len(batch_files)} files")
        if batch_files:
            self.logger.info(f"  First file: {batch_files[0].name}")
            self.logger.info(f"  Last file: {batch_files[-1].name}")

        return batch_files

    def copy_batch_to_processing(self, batch_files: List[Path]) -> bool:
        """Copy batch files to the processing directory."""
        processing_dir = self.script_dir / "data" / "text_input"
        processing_dir.mkdir(parents=True, exist_ok=True)

        # Clear existing files
        for existing_file in processing_dir.glob("*.txt"):
            existing_file.unlink()

        self.logger.info(f"Copying {len(batch_files)} files to processing directory...")

        if self.dry_run:
            self.logger.info(f"DRY RUN: Would copy {len(batch_files)} files")
            return True

        try:
            for i, file_path in enumerate(batch_files, 1):
                if i % 500 == 0:
                    self.logger.info(f"  Copied {i}/{len(batch_files)} files")

                dest_path = processing_dir / file_path.name
                shutil.copy2(file_path, dest_path)

            self.logger.info(f"✅ Copied {len(batch_files)} files to processing directory")
            return True

        except Exception as e:
            self.logger.error(f"❌ Error copying batch files: {e}")
            return False

    def phase2_document_processing(self) -> bool:
        """Phase 2: Process first N documents through master pipeline."""
        self.logger.info("\n" + "="*60)
        self.logger.info("PHASE 2: DOCUMENT PROCESSING")
        self.logger.info("="*60)
        
        try:
            # Get files from the processing directory (already copied by batch processing)
            temp_input_dir = self.script_dir / "data" / "text_input"

            if not temp_input_dir.exists():
                self.logger.error(f"Processing directory not found: {temp_input_dir}")
                return False

            files_to_process = list(temp_input_dir.glob("*.txt"))

            if not files_to_process:
                self.logger.error("No files found in processing directory")
                return False

            files_to_process.sort(key=lambda x: x.name)

            self.logger.info(f"Processing {len(files_to_process)} files from current batch")
            self.logger.info(f"First file: {files_to_process[0].name}")
            self.logger.info(f"Last file: {files_to_process[-1].name}")

            if self.dry_run:
                self.logger.info("DRY RUN: Would process files through master pipeline")
                self.stats['files_processed'] = len(files_to_process)
                return True
            
            # Execute master script
            self.logger.info("🚀 Executing master processing pipeline...")
            
            try:
                # Change to script directory for execution
                original_cwd = os.getcwd()
                os.chdir(self.script_dir)
                
                # Run master script with consistent Python interpreter
                python_executable = sys.executable
                result = subprocess.run(
                    [python_executable, str(self.master_script)],
                    capture_output=True,
                    text=True,
                    timeout=3600  # 1 hour timeout
                )
                
                # Restore working directory
                os.chdir(original_cwd)
                
                if result.returncode == 0:
                    self.logger.info("✅ Master pipeline completed successfully")
                    self.stats['files_processed'] = len(files_to_process)
                    
                    # Log output for debugging
                    if result.stdout:
                        self.logger.debug(f"Master script output: {result.stdout}")
                        
                    return True
                else:
                    self.logger.error(f"❌ Master pipeline failed with return code {result.returncode}")
                    if result.stderr:
                        self.logger.error(f"Error output: {result.stderr}")
                    if result.stdout:
                        self.logger.error(f"Standard output: {result.stdout}")
                    return False
                    
            except subprocess.TimeoutExpired:
                self.logger.error("❌ Master pipeline timed out after 1 hour")
                return False
            except Exception as e:
                self.logger.error(f"❌ Error executing master pipeline: {e}")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Error in document processing phase: {e}")
            return False
            
    def scan_json_files(self) -> Tuple[List[Path], List[Path]]:
        """Scan output directory for JSON files and categorize them."""
        self.logger.info("🔍 Scanning for generated JSON files...")

        # Get all JSON files but exclude preserved_tables directory
        all_json_files = []
        for json_file in self.output_dir.rglob("*.json"):
            # Skip files in preserved_tables directories
            if "preserved_tables" not in str(json_file):
                all_json_files.append(json_file)

        valid_files = []
        invalid_files = []

        self.logger.info(f"Found {len(all_json_files):,} JSON files (excluding preserved tables)")
        
        for i, json_file in enumerate(all_json_files, 1):
            if i % 100 == 0:
                self.logger.info(f"  Scanned {i}/{len(all_json_files)} files")
                
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                # Check if document_hierarchy field exists and is non-empty
                document_hierarchy = data.get('document_hierarchy', [])
                if isinstance(document_hierarchy, list) and len(document_hierarchy) > 0:
                    valid_files.append(json_file)
                else:
                    invalid_files.append(json_file)
                    
            except Exception as e:
                self.logger.warning(f"Error reading {json_file.name}: {e}")
                invalid_files.append(json_file)
                
        self.logger.info(f"✅ Scan complete:")
        self.logger.info(f"  Valid files (with non-empty document_hierarchy): {len(valid_files):,}")
        self.logger.info(f"  Invalid files (empty or missing document_hierarchy): {len(invalid_files):,}")
        
        self.stats['json_files_created'] = len(all_json_files)
        self.stats['valid_json_files'] = len(valid_files)
        self.stats['invalid_json_files'] = len(invalid_files)
        
        return valid_files, invalid_files

    def create_zip_archive(self, valid_files: List[Path]) -> Optional[Path]:
        """Create ZIP archive with valid JSON files."""
        if not valid_files:
            self.logger.warning("No valid files to archive")
            return None

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_filename = f"belgian_legal_docs_{timestamp}_{len(valid_files)}_files.zip"
        zip_path = self.script_dir / zip_filename

        self.logger.info(f"📦 Creating ZIP archive: {zip_filename}")

        if self.dry_run:
            self.logger.info(f"DRY RUN: Would create ZIP with {len(valid_files):,} files")
            return zip_path

        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
                for i, json_file in enumerate(valid_files, 1):
                    if i % 100 == 0:
                        self.logger.info(f"  Added {i}/{len(valid_files)} files to ZIP")

                    # Use relative path in ZIP
                    arcname = json_file.relative_to(self.output_dir)
                    zipf.write(json_file, arcname)

            # Get ZIP file size
            zip_size_mb = zip_path.stat().st_size / (1024 * 1024)
            self.logger.info(f"✅ ZIP archive created: {zip_size_mb:.1f} MB")

            return zip_path

        except Exception as e:
            self.logger.error(f"❌ Error creating ZIP archive: {e}")
            return None

    def upload_to_s3(self, zip_path: Path) -> bool:
        """Upload ZIP file to S3."""
        self.logger.info("☁️  Uploading to S3...")

        if self.dry_run:
            self.logger.info("DRY RUN: Would upload ZIP file to S3")
            return True

        try:
            # Check if ZIP upload script exists
            upload_script = self.script_dir / "aws-s3" / "upload_zip_to_s3.py"
            if not upload_script.exists():
                self.logger.error(f"ZIP upload script not found: {upload_script}")
                return False

            # Execute ZIP upload script
            result = subprocess.run(
                [sys.executable, str(upload_script), str(zip_path)],
                capture_output=True,
                text=True,
                timeout=1800  # 30 minute timeout
            )

            if result.returncode == 0:
                self.logger.info("✅ Successfully uploaded to S3")
                if result.stdout:
                    self.logger.info(f"Upload output: {result.stdout}")
                return True
            else:
                self.logger.error(f"❌ S3 upload failed with return code {result.returncode}")
                if result.stderr:
                    self.logger.error(f"Error output: {result.stderr}")
                return False

        except subprocess.TimeoutExpired:
            self.logger.error("❌ S3 upload timed out after 30 minutes")
            return False
        except Exception as e:
            self.logger.error(f"❌ Error during S3 upload: {e}")
            return False

    def cleanup_temporary_files(self, zip_path: Optional[Path] = None):
        """Clean up temporary files after processing."""
        self.logger.info("🧹 Cleaning up temporary files...")

        try:
            # Clean up temporary input directory
            temp_input_dir = self.script_dir / "data" / "text_input"
            if temp_input_dir.exists():
                if self.dry_run:
                    temp_files = list(temp_input_dir.glob("*.txt"))
                    self.logger.info(f"DRY RUN: Would clean up {len(temp_files)} temporary input files")
                else:
                    for temp_file in temp_input_dir.glob("*.txt"):
                        temp_file.unlink()
                    self.logger.info("✅ Cleaned up temporary input files")

            # Optionally remove ZIP file after successful upload
            if zip_path and zip_path.exists() and self.stats.get('upload_success', False):
                if not self.dry_run:
                    response = input(f"\nRemove local ZIP file {zip_path.name} after successful upload? (y/N): ")
                    if response.lower() == 'y':
                        zip_path.unlink()
                        self.logger.info(f"✅ Removed local ZIP file: {zip_path.name}")

        except Exception as e:
            self.logger.error(f"❌ Error during cleanup: {e}")

    def phase3_quality_filtering_and_upload(self) -> bool:
        """Phase 3: Filter JSON files, create batches, and upload to S3."""
        self.logger.info("\n" + "="*60)
        self.logger.info("PHASE 3: QUALITY FILTERING AND BATCH S3 UPLOAD")
        self.logger.info("="*60)

        try:
            # Scan for JSON files
            valid_files, invalid_files = self.scan_json_files()

            if not valid_files:
                self.logger.warning("No valid JSON files found - nothing to upload")
                return False

            # Log invalid files for audit
            if invalid_files:
                self.logger.info(f"📝 Logging {len(invalid_files)} invalid files...")
                invalid_log = self.logs_dir / f"invalid_json_files_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

                if not self.dry_run:
                    with open(invalid_log, 'w') as f:
                        f.write("Invalid JSON files (empty or missing document_hierarchy field):\n")
                        f.write("=" * 60 + "\n")
                        for invalid_file in invalid_files:
                            f.write(f"{invalid_file.relative_to(self.output_dir)}\n")
                    self.logger.info(f"✅ Invalid files logged to: {invalid_log}")

            # Create category-based ZIP files and upload
            batch_success = self.create_batches_and_upload(valid_files, invalid_files, self.stats['current_batch'])
            self.stats['upload_success'] = batch_success

            return batch_success

        except Exception as e:
            self.logger.error(f"❌ Error in quality filtering and upload phase: {e}")
            return False

    def create_batches(self, files: List[Path], batch_size: int = 100) -> List[List[Path]]:
        """Organize files into batches of specified size."""
        batches = []
        for i in range(0, len(files), batch_size):
            batch = files[i:i + batch_size]
            batches.append(batch)
        return batches

    def create_batch_zip(self, files: List[Path], batch_number: int) -> Optional[Path]:
        """Create a ZIP file for a batch of JSON files."""
        if not files:
            return None

        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            zip_filename = f"belgian_legal_batch_{batch_number:03d}_{timestamp}_{len(files)}_files.zip"
            zip_path = self.script_dir / zip_filename

            self.logger.info(f"📦 Creating batch {batch_number} ZIP: {zip_filename}")

            if self.dry_run:
                self.logger.info(f"DRY RUN: Would create ZIP with {len(files)} files")
                return zip_path

            total_size = 0
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
                for file_path in files:
                    if file_path.exists():
                        # Add file to zip with just the filename (no directory structure)
                        arcname = file_path.name
                        zipf.write(file_path, arcname)
                        total_size += file_path.stat().st_size

            zip_size = zip_path.stat().st_size
            compression_ratio = (total_size - zip_size) / total_size if total_size > 0 else 0

            self.logger.info(
                f"✅ Created batch {batch_number}: {len(files)} files, "
                f"{total_size / (1024*1024):.1f}MB → {zip_size / (1024*1024):.1f}MB "
                f"({compression_ratio*100:.1f}% compression)"
            )

            return zip_path

        except Exception as e:
            self.logger.error(f"❌ Error creating batch {batch_number} ZIP: {e}")
            return None

    def upload_batch_to_s3(self, zip_path: Path, batch_number: int) -> bool:
        """Upload a batch ZIP file to S3."""
        self.logger.info(f"☁️  Uploading batch {batch_number} to S3...")

        if self.dry_run:
            self.logger.info(f"DRY RUN: Would upload batch {batch_number} ZIP file to S3")
            return True

        try:
            # Check if upload script exists
            upload_script = self.script_dir / "aws-s3" / "upload_zip_to_s3.py"
            if not upload_script.exists():
                self.logger.error(f"ZIP upload script not found: {upload_script}")
                return False

            # Execute ZIP upload script
            result = subprocess.run(
                [sys.executable, str(upload_script), str(zip_path)],
                capture_output=True,
                text=True,
                timeout=1800  # 30 minute timeout
            )

            if result.returncode == 0:
                self.logger.info(f"✅ Batch {batch_number} uploaded successfully to S3")
                if result.stdout:
                    # Log only the S3 location line for brevity
                    for line in result.stdout.split('\n'):
                        if 'S3 location:' in line:
                            self.logger.info(f"  {line.strip()}")
                return True
            else:
                self.logger.error(f"❌ Batch {batch_number} S3 upload failed with return code {result.returncode}")
                if result.stderr:
                    self.logger.error(f"Error output: {result.stderr}")
                return False

        except subprocess.TimeoutExpired:
            self.logger.error(f"❌ Batch {batch_number} S3 upload timed out after 30 minutes")
            return False
        except Exception as e:
            self.logger.error(f"❌ Error during batch {batch_number} S3 upload: {e}")
            return False

    def create_category_zip(self, files: List[Path], category: str, batch_number: int) -> Optional[Path]:
        """Create a ZIP file for a specific category (valid/invalid) of JSON files."""
        if not files:
            self.logger.info(f"No {category} files to archive for batch {batch_number}")
            return None

        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            zip_filename = f"belgian_legal_batch_{batch_number:03d}_{category}_{timestamp}_{len(files)}_files.zip"
            zip_path = self.script_dir / zip_filename

            self.logger.info(f"📦 Creating {category} ZIP for batch {batch_number}: {zip_filename}")

            if self.dry_run:
                self.logger.info(f"DRY RUN: Would create {category} ZIP with {len(files)} files")
                return zip_path

            total_size = 0
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
                for file_path in files:
                    if file_path.exists():
                        # Add file to zip with just the filename (no directory structure)
                        arcname = file_path.name
                        zipf.write(file_path, arcname)
                        total_size += file_path.stat().st_size

            zip_size = zip_path.stat().st_size
            compression_ratio = (total_size - zip_size) / total_size if total_size > 0 else 0

            self.logger.info(
                f"✅ Created {category} ZIP for batch {batch_number}: {len(files)} files, "
                f"{total_size / (1024*1024):.1f}MB → {zip_size / (1024*1024):.1f}MB "
                f"({compression_ratio*100:.1f}% compression)"
            )

            return zip_path

        except Exception as e:
            self.logger.error(f"❌ Error creating {category} ZIP for batch {batch_number}: {e}")
            return None

    def upload_category_zip_to_s3(self, zip_path: Path, category: str, batch_number: int) -> bool:
        """Upload a category ZIP file to S3 with appropriate prefix."""
        if category == "valid":
            s3_prefix = "incoming3"
        elif category == "invalid":
            s3_prefix = "incoming_no_articles3"
        else:
            self.logger.error(f"Unknown category: {category}")
            return False

        self.logger.info(f"☁️  Uploading {category} batch {batch_number} to S3 prefix: {s3_prefix}/")

        if self.dry_run:
            self.logger.info(f"DRY RUN: Would upload {category} ZIP to S3 prefix {s3_prefix}/")
            return True

        try:
            # Use the new upload script with custom prefix support
            upload_script = self.script_dir / "aws-s3" / "upload_zip_to_s3_with_prefix.py"
            if not upload_script.exists():
                self.logger.error(f"ZIP upload script not found: {upload_script}")
                return False

            # Execute upload script with custom prefix
            # Use the same Python interpreter that's currently running
            python_executable = sys.executable
            result = subprocess.run(
                [python_executable, str(upload_script), str(zip_path), "--prefix", s3_prefix],
                capture_output=True,
                text=True,
                timeout=1800  # 30 minute timeout
            )

            if result.returncode == 0:
                self.logger.info(f"✅ {category.title()} batch {batch_number} uploaded successfully to S3")
                if result.stdout:
                    # Log only the S3 location line for brevity
                    for line in result.stdout.split('\n'):
                        if 'S3 location:' in line:
                            self.logger.info(f"  {line.strip()}")
                return True
            else:
                self.logger.error(f"❌ {category.title()} batch {batch_number} S3 upload failed with return code {result.returncode}")
                if result.stderr:
                    self.logger.error(f"Error output: {result.stderr}")
                if result.stdout:
                    self.logger.error(f"Stdout output: {result.stdout}")
                self.logger.error(f"Command executed: {[python_executable, str(upload_script), str(zip_path), '--prefix', s3_prefix]}")
                return False

        except subprocess.TimeoutExpired:
            self.logger.error(f"❌ {category.title()} batch {batch_number} S3 upload timed out after 30 minutes")
            return False
        except Exception as e:
            self.logger.error(f"❌ Error during {category} batch {batch_number} S3 upload: {e}")
            return False

    def create_batches_and_upload(self, valid_files: List[Path], invalid_files: List[Path], batch_number: int) -> bool:
        """Create category-based ZIP files and upload to S3 with appropriate prefixes."""

        self.logger.info(f"📊 Batch {batch_number} file distribution:")
        self.logger.info(f"  Valid files (non-empty document_hierarchy): {len(valid_files)}")
        self.logger.info(f"  Invalid files (empty document_hierarchy): {len(invalid_files)}")

        successful_uploads = 0
        failed_uploads = 0

        # Create and upload valid files ZIP
        if valid_files:
            self.logger.info(f"\n🔄 Processing valid files for batch {batch_number}")
            valid_zip_path = self.create_category_zip(valid_files, "valid", batch_number)
            if valid_zip_path:
                upload_success = self.upload_category_zip_to_s3(valid_zip_path, "valid", batch_number)
                if upload_success:
                    successful_uploads += 1
                    self.stats['valid_zips_uploaded'] += 1

                    # Clean up ZIP file after successful upload
                    if not self.dry_run and valid_zip_path.exists():
                        valid_zip_path.unlink()
                        self.logger.info(f"🧹 Cleaned up valid ZIP file for batch {batch_number}")
                else:
                    failed_uploads += 1
            else:
                failed_uploads += 1

        # Create and upload invalid files ZIP
        if invalid_files:
            self.logger.info(f"\n🔄 Processing invalid files for batch {batch_number}")
            invalid_zip_path = self.create_category_zip(invalid_files, "invalid", batch_number)
            if invalid_zip_path:
                upload_success = self.upload_category_zip_to_s3(invalid_zip_path, "invalid", batch_number)
                if upload_success:
                    successful_uploads += 1
                    self.stats['invalid_zips_uploaded'] += 1

                    # Clean up ZIP file after successful upload
                    if not self.dry_run and invalid_zip_path.exists():
                        invalid_zip_path.unlink()
                        self.logger.info(f"🧹 Cleaned up invalid ZIP file for batch {batch_number}")
                else:
                    failed_uploads += 1
            else:
                failed_uploads += 1

        # Batch summary
        self.logger.info(f"\n📊 BATCH {batch_number} UPLOAD SUMMARY:")
        self.logger.info(f"  Successful uploads: {successful_uploads}")
        self.logger.info(f"  Failed uploads: {failed_uploads}")

        return failed_uploads == 0

    def cleanup_batch_files(self) -> bool:
        """Clean up all intermediate files after batch processing."""
        self.logger.info("🧹 Cleaning up batch files...")

        if self.dry_run:
            self.logger.info("DRY RUN: Would clean up batch files")
            return True

        try:
            # Clear output directory
            if self.output_dir.exists():
                shutil.rmtree(self.output_dir)
                self.logger.info("✅ Cleared output directory")

            # Clear processing input directory
            processing_dir = self.script_dir / "data" / "text_input"
            if processing_dir.exists():
                shutil.rmtree(processing_dir)
                self.logger.info("✅ Cleared processing input directory")

            # Remove any leftover ZIP files
            for zip_file in self.script_dir.glob("belgian_legal_batch_*.zip"):
                zip_file.unlink()
                self.logger.info(f"✅ Removed leftover ZIP file: {zip_file.name}")

            return True

        except Exception as e:
            self.logger.error(f"❌ Error during cleanup: {e}")
            return False

    def process_large_batches(self) -> bool:
        """Process all files in large batches."""
        self.logger.info("\n" + "="*80)
        self.logger.info("LARGE-BATCH PROCESSING MODE")
        self.logger.info("="*80)
        self.logger.info(f"Total files to process: {self.total_files:,}")
        self.logger.info(f"Batch size: {self.batch_size:,}")
        self.logger.info(f"Total batches: {self.total_batches}")
        self.logger.info(f"Starting from batch: {self.start_batch}")

        overall_success = True

        for batch_num in range(self.start_batch, self.total_batches + 1):
            self.stats['current_batch'] = batch_num

            self.logger.info(f"\n" + "="*60)
            self.logger.info(f"PROCESSING BATCH {batch_num}/{self.total_batches}")
            self.logger.info("="*60)

            # Get files for this batch
            batch_files = self.get_batch_files(batch_num)
            if not batch_files:
                self.logger.warning(f"No files found for batch {batch_num}")
                continue

            # Copy batch files to processing directory
            if not self.copy_batch_to_processing(batch_files):
                self.logger.error(f"❌ Failed to copy files for batch {batch_num}")
                overall_success = False
                continue

            # Run the complete pipeline on this batch
            batch_success = (
                self.phase1_environment_preparation() and
                self.phase2_document_processing() and
                self.phase3_quality_filtering_and_upload()
            )

            if batch_success:
                self.logger.info(f"✅ Batch {batch_num} completed successfully")
            else:
                self.logger.error(f"❌ Batch {batch_num} failed")
                overall_success = False

            # Clean up intermediate files before next batch
            if not self.cleanup_batch_files():
                self.logger.warning(f"⚠️  Failed to clean up files after batch {batch_num}")

            # Update overall statistics
            self.stats['files_processed'] += len(batch_files)

        return overall_success

    def print_final_summary(self):
        """Print comprehensive final summary."""
        self.logger.info("\n" + "="*80)
        self.logger.info("PIPELINE EXECUTION SUMMARY")
        self.logger.info("="*80)

        self.logger.info(f"Mode: {'DRY RUN' if self.dry_run else 'LIVE EXECUTION'}")
        self.logger.info(f"Max files configured: {self.max_files:,}")
        self.logger.info(f"Files processed: {self.stats['files_processed']:,}")
        self.logger.info(f"JSON files created: {self.stats['json_files_created']:,}")
        self.logger.info(f"Valid JSON files: {self.stats['valid_json_files']:,}")
        self.logger.info(f"Invalid JSON files: {self.stats['invalid_json_files']:,}")

        # Batch statistics
        if 'batches_created' in self.stats:
            self.logger.info(f"Batches created: {self.stats['batches_created']:,}")
            self.logger.info(f"Successful batch uploads: {self.stats.get('successful_batch_uploads', 0):,}")
            self.logger.info(f"Failed batch uploads: {self.stats.get('failed_batch_uploads', 0):,}")
            self.logger.info(f"Total files uploaded: {self.stats.get('total_files_uploaded', 0):,}")

        self.logger.info(f"Environment cleanup: {'Yes' if self.stats['cleanup_performed'] else 'No'}")
        self.logger.info(f"S3 upload: {'Success' if self.stats['upload_success'] else 'Failed/Skipped'}")

        if self.stats['valid_json_files'] > 0:
            success_rate = (self.stats['valid_json_files'] / self.stats['json_files_created']) * 100
            self.logger.info(f"Quality success rate: {success_rate:.1f}%")

        self.logger.info("="*80)

    def run_pipeline(self) -> bool:
        """Execute the complete pipeline."""
        try:
            self.logger.info("🚀 Starting comprehensive processing pipeline...")

            # Check prerequisites
            if not self.check_prerequisites():
                self.logger.error("❌ Prerequisites check failed")
                return False

            # Choose processing mode based on configuration
            if self.process_all or self.total_batches > 1:
                # Large-batch processing mode
                success = self.process_large_batches()
            else:
                # Single-batch processing mode (original behavior)
                success = (
                    self.phase1_environment_preparation() and
                    self.phase2_document_processing() and
                    self.phase3_quality_filtering_and_upload()
                )

            if success:
                self.logger.info("🎉 Pipeline completed successfully!")
            else:
                self.logger.error("❌ Pipeline failed")

            return success

        except KeyboardInterrupt:
            self.logger.warning("⚠️ Pipeline interrupted by user")
            return False
        except Exception as e:
            self.logger.error(f"❌ Unexpected error in pipeline: {e}")
            return False
        finally:
            self.print_final_summary()


def main():
    """Main function with command-line interface."""
    parser = argparse.ArgumentParser(
        description="Comprehensive Belgian Legal Document Processing Pipeline"
    )
    parser.add_argument("--dry-run", "-n", action="store_true",
                       help="Simulate pipeline execution without making changes")
    parser.add_argument("--max-files", "-m", type=int, default=1000,
                       help="Maximum number of files to process (default: 1000)")
    parser.add_argument("--batch-size", "-b", type=int, default=1000,
                       help="Number of files per batch for large-batch processing (default: 1000)")
    parser.add_argument("--start-batch", "-s", type=int, default=1,
                       help="Starting batch number for resuming processing (default: 1)")
    parser.add_argument("--process-all", "-a", action="store_true",
                       help="Process all files in input directory using large-batch mode")
    parser.add_argument("--log-level", "-l", default="INFO",
                       choices=["DEBUG", "INFO", "WARNING", "ERROR"],
                       help="Set logging level (default: INFO)")

    args = parser.parse_args()

    # Create and run pipeline
    pipeline = ComprehensivePipeline(
        dry_run=args.dry_run,
        max_files=args.max_files,
        log_level=args.log_level,
        batch_size=args.batch_size,
        start_batch=args.start_batch,
        process_all=args.process_all
    )

    success = pipeline.run_pipeline()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
