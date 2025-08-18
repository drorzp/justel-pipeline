#!/usr/bin/env python3
"""
Batch Upload Script for Belgian Legal Documents

This script takes valid JSON files, organizes them into batches of specified size,
creates ZIP files for each batch, and uploads them to S3.
"""

import sys
import logging
import argparse
import json
import zipfile
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Tuple

# Add src directory to path (go up one level from aws-s3 folder)
try:
    # Try using __file__ first
    script_dir = Path(__file__).parent
except NameError:
    # Fallback for execution contexts where __file__ is not defined
    script_dir = Path.cwd() / "aws-s3"

sys.path.insert(0, str(script_dir.parent / "src"))

# Import the S3 uploader
try:
    from utilities.s3_uploader import S3LegalDocumentUploader
except ImportError:
    print("Error: Could not import S3LegalDocumentUploader")
    print("Make sure src/utilities/s3_uploader.py exists and is accessible")
    sys.exit(1)


def setup_logging(level: str = 'INFO') -> logging.Logger:
    """Setup logging configuration."""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('batch_s3_upload.log', mode='w')
        ]
    )
    return logging.getLogger(__name__)


def validate_json_file(json_path: Path) -> bool:
    """Check if JSON file has non-empty document_hierarchy."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        document_hierarchy = data.get('document_hierarchy', [])
        return isinstance(document_hierarchy, list) and len(document_hierarchy) > 0
        
    except Exception:
        return False


def find_valid_json_files(directory: Path) -> List[Path]:
    """Find all valid JSON files with non-empty document_hierarchy."""
    logger = logging.getLogger(__name__)
    
    if not directory.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    logger.info(f"Scanning for JSON files in: {directory}")
    all_json_files = list(directory.glob("*.json"))
    logger.info(f"Found {len(all_json_files)} total JSON files")
    
    valid_files = []
    invalid_count = 0
    
    for json_file in all_json_files:
        if validate_json_file(json_file):
            valid_files.append(json_file)
        else:
            invalid_count += 1
    
    logger.info(f"Valid files (non-empty document_hierarchy): {len(valid_files)}")
    logger.info(f"Invalid files (empty/missing document_hierarchy): {invalid_count}")
    
    return sorted(valid_files)


def create_batches(files: List[Path], batch_size: int) -> List[List[Path]]:
    """Organize files into batches of specified size."""
    batches = []
    for i in range(0, len(files), batch_size):
        batch = files[i:i + batch_size]
        batches.append(batch)
    return batches


def create_batch_zip(files: List[Path], batch_number: int, output_dir: Path) -> Tuple[Path, Dict[str, Any]]:
    """Create a ZIP file for a batch of JSON files."""
    logger = logging.getLogger(__name__)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"belgian_legal_batch_{batch_number:03d}_{timestamp}_{len(files)}_files.zip"
    zip_path = output_dir / zip_filename
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    total_original_size = 0
    file_metadata = []
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
        for file_path in files:
            if not file_path.exists():
                logger.warning(f"File not found, skipping: {file_path}")
                continue
            
            # Add file to zip with just the filename
            arcname = file_path.name
            zipf.write(file_path, arcname)
            
            # Track metadata
            file_size = file_path.stat().st_size
            total_original_size += file_size
            
            # Extract document type from JSON
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                doc_type = data.get('document_metadata', {}).get('document_type', 'unknown')
            except:
                doc_type = 'unknown'
            
            file_metadata.append({
                'filename': file_path.name,
                'original_size': file_size,
                'document_type': doc_type
            })
    
    # Calculate compression statistics
    zip_size = zip_path.stat().st_size
    compression_ratio = (total_original_size - zip_size) / total_original_size if total_original_size > 0 else 0
    
    batch_metadata = {
        'batch_number': batch_number,
        'zip_filename': zip_filename,
        'file_count': len(file_metadata),
        'original_total_size': total_original_size,
        'compressed_size': zip_size,
        'compression_ratio': compression_ratio,
        'compression_percentage': compression_ratio * 100,
        'files': file_metadata,
        'created_at': datetime.utcnow().isoformat()
    }
    
    logger.info(
        f"Created batch {batch_number}: {len(file_metadata)} files, "
        f"{total_original_size / (1024*1024):.1f}MB → {zip_size / (1024*1024):.1f}MB "
        f"({compression_ratio*100:.1f}% compression)"
    )
    
    return zip_path, batch_metadata


def upload_batch_to_s3(zip_path: Path, batch_metadata: Dict[str, Any], dry_run: bool = False) -> bool:
    """Upload a batch ZIP file to S3."""
    logger = logging.getLogger(__name__)
    
    if dry_run:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        s3_key = f"incoming2/{timestamp}_{zip_path.name}"
        logger.info(f"DRY RUN - Would upload: {zip_path.name}")
        logger.info(f"DRY RUN - S3 key: {s3_key}")
        return True
    
    try:
        # Initialize S3 uploader
        uploader = S3LegalDocumentUploader()
        
        # Generate S3 key
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        s3_key = f"incoming2/{timestamp}_{zip_path.name}"
        
        # Prepare upload metadata
        upload_metadata = {
            'content_type': 'legal_documents_batch',
            'batch_number': str(batch_metadata['batch_number']),
            'file_count': str(batch_metadata['file_count']),
            'original_size': str(batch_metadata['original_total_size']),
            'compression_ratio': str(batch_metadata['compression_ratio']),
            'upload_timestamp': datetime.utcnow().isoformat(),
            'source_pipeline': 'comprehensive_belgian_legal_batch_pipeline'
        }
        
        # Upload the ZIP file
        logger.info(f"Uploading batch {batch_metadata['batch_number']} to S3...")
        success, message = uploader.upload_single_file(zip_path, s3_key, upload_metadata)
        
        if success:
            logger.info(f"✅ Batch {batch_metadata['batch_number']} uploaded successfully")
            logger.info(f"S3 location: s3://article-zip/{s3_key}")
            return True
        else:
            logger.error(f"❌ Failed to upload batch {batch_metadata['batch_number']}: {message}")
            return False
            
    except Exception as e:
        logger.error(f"❌ Error uploading batch {batch_metadata['batch_number']}: {e}")
        return False


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Batch upload Belgian legal documents to S3')
    parser.add_argument('input_dir', help='Directory containing JSON files')
    parser.add_argument('--batch-size', type=int, default=100,
                       help='Number of files per batch (default: 100)')
    parser.add_argument('--output-dir', default='batch_zips',
                       help='Directory to store batch ZIP files (default: batch_zips)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be uploaded without actually uploading')
    parser.add_argument('--log-level', default='INFO',
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       help='Logging level (default: INFO)')
    parser.add_argument('--keep-zips', action='store_true',
                       help='Keep ZIP files after upload (default: delete after upload)')
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logging(args.log_level)
    
    logger.info("="*80)
    logger.info("BELGIAN LEGAL DOCUMENTS - BATCH S3 UPLOADER")
    logger.info("="*80)
    logger.info(f"Input directory: {args.input_dir}")
    logger.info(f"Batch size: {args.batch_size}")
    logger.info(f"Output directory: {args.output_dir}")
    logger.info(f"Dry run: {args.dry_run}")
    logger.info(f"Keep ZIPs: {args.keep_zips}")
    
    try:
        # Find valid JSON files
        input_dir = Path(args.input_dir)
        valid_files = find_valid_json_files(input_dir)
        
        if not valid_files:
            logger.error("No valid JSON files found")
            return 1
        
        # Create batches
        batches = create_batches(valid_files, args.batch_size)
        logger.info(f"Created {len(batches)} batches of up to {args.batch_size} files each")
        
        # Process each batch
        output_dir = Path(args.output_dir)
        successful_uploads = 0
        failed_uploads = 0
        
        for i, batch_files in enumerate(batches, 1):
            logger.info(f"\n📦 Processing batch {i}/{len(batches)} ({len(batch_files)} files)")
            
            # Create ZIP file
            zip_path, batch_metadata = create_batch_zip(batch_files, i, output_dir)
            
            # Upload to S3
            upload_success = upload_batch_to_s3(zip_path, batch_metadata, args.dry_run)
            
            if upload_success:
                successful_uploads += 1
                # Clean up ZIP file unless keeping them
                if not args.keep_zips and not args.dry_run:
                    zip_path.unlink()
                    logger.info(f"Cleaned up ZIP file: {zip_path.name}")
            else:
                failed_uploads += 1
        
        # Final summary
        logger.info(f"\n🎉 Batch upload completed!")
        logger.info(f"Total valid files processed: {len(valid_files)}")
        logger.info(f"Total batches created: {len(batches)}")
        logger.info(f"Successful uploads: {successful_uploads}")
        logger.info(f"Failed uploads: {failed_uploads}")
        
        if failed_uploads > 0:
            logger.warning(f"⚠️  {failed_uploads} batches failed to upload")
            return 1
        else:
            logger.info("✅ All batches uploaded successfully!")
            return 0
            
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
