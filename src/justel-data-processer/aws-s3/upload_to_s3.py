#!/usr/bin/env python3
"""
Upload Belgian Legal Documents to S3
Main script for uploading processed JSON files to S3 with batch management.
"""

import sys
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import List, Dict
import argparse

# Add src directory to path (go up one level from aws-s3 folder)
try:
    # Try using __file__ first
    script_dir = Path(__file__).parent
except NameError:
    # Fallback for execution contexts where __file__ is not defined
    script_dir = Path.cwd() / "aws-s3"

sys.path.insert(0, str(script_dir.parent / "src"))

from utilities.s3_uploader import S3LegalDocumentUploader


def setup_logging(log_level: str = "INFO") -> logging.Logger:
    """Setup logging configuration."""
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('s3_upload.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)


def find_json_files(directory: Path) -> List[Path]:
    """Find all JSON files in a directory."""
    if not directory.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    json_files = list(directory.glob("*.json"))
    return sorted(json_files)


def organize_files_into_batches(files: List[Path], batch_size: int) -> List[List[Path]]:
    """Organize files into batches for upload."""
    batches = []
    for i in range(0, len(files), batch_size):
        batch = files[i:i + batch_size]
        batches.append(batch)
    return batches


def create_processing_manifest(total_files: int, total_batches: int, 
                             document_type_counts: Dict[str, int]) -> Dict:
    """Create processing manifest for S3."""
    return {
        "processing_metadata": {
            "total_documents": total_files,
            "total_batches": total_batches,
            "processing_start": datetime.utcnow().isoformat(),
            "s3_bucket": "article-zip",
            "s3_prefix": "incoming2/",
            "batch_size": total_files // total_batches if total_batches > 0 else 0
        },
        "document_types": document_type_counts,
        "batch_status": [],
        "upload_statistics": {
            "files_uploaded": 0,
            "files_failed": 0,
            "bytes_uploaded": 0
        }
    }


def count_document_types(files: List[Path]) -> Dict[str, int]:
    """Count document types from JSON files."""
    type_counts = {}
    
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                doc_type = data.get('document_type', 'UNKNOWN')
                type_counts[doc_type] = type_counts.get(doc_type, 0) + 1
        except Exception as e:
            logging.warning(f"Could not read document type from {file_path}: {e}")
            type_counts['UNKNOWN'] = type_counts.get('UNKNOWN', 0) + 1
    
    return type_counts


def upload_batch_with_retry(uploader: S3LegalDocumentUploader,
                           batch_files: List[Path], batch_id: int,
                           max_retries: int = 3, use_zip: bool = False) -> Dict:
    """Upload batch with retry logic."""
    logger = logging.getLogger(__name__)
    
    for attempt in range(max_retries):
        try:
            upload_method = "zip" if use_zip else "individual files"
            logger.info(f"Uploading batch {batch_id} as {upload_method}, attempt {attempt + 1}/{max_retries}")
            result = uploader.upload_batch(batch_files, batch_id, use_zip=use_zip)

            if result['success']:
                logger.info(f"✅ Batch {batch_id} uploaded successfully")
                return result
            else:
                logger.warning(f"⚠️ Batch {batch_id} had {result['failed']} failures")
                if attempt < max_retries - 1:
                    logger.info(f"Retrying batch {batch_id}...")
                    continue
                else:
                    return result
                    
        except Exception as e:
            logger.error(f"❌ Batch {batch_id} attempt {attempt + 1} failed: {e}")
            if attempt == max_retries - 1:
                return {
                    'success': False,
                    'uploaded': 0,
                    'failed': len(batch_files),
                    'errors': [f"All retry attempts failed: {str(e)}"],
                    'batch_id': batch_id
                }
    
    return {'success': False, 'uploaded': 0, 'failed': len(batch_files), 'batch_id': batch_id}


def main():
    """Main upload function."""
    parser = argparse.ArgumentParser(description='Upload Belgian Legal Documents to S3')
    parser.add_argument('input_dir', help='Directory containing JSON files to upload')
    parser.add_argument('--batch-size', type=int, default=1000, 
                       help='Number of files per batch (default: 1000)')
    parser.add_argument('--max-workers', type=int, default=10,
                       help='Maximum parallel uploads per batch (default: 10)')
    parser.add_argument('--log-level', default='INFO',
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       help='Logging level (default: INFO)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be uploaded without actually uploading')
    parser.add_argument('--use-zip', action='store_true',
                       help='Compress batches into zip files before upload (recommended)')
    parser.add_argument('--zip-temp-dir', type=str,
                       help='Temporary directory for zip file creation (default: system temp)')
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logging(args.log_level)
    
    try:
        # Find JSON files
        input_dir = Path(args.input_dir)
        logger.info(f"Scanning for JSON files in: {input_dir}")
        
        json_files = find_json_files(input_dir)
        if not json_files:
            logger.error(f"No JSON files found in {input_dir}")
            return 1
        
        logger.info(f"Found {len(json_files)} JSON files")
        
        # Organize into batches
        batches = organize_files_into_batches(json_files, args.batch_size)
        logger.info(f"Organized into {len(batches)} batches of {args.batch_size} files each")
        
        # Count document types
        logger.info("Analyzing document types...")
        doc_type_counts = count_document_types(json_files)
        for doc_type, count in doc_type_counts.items():
            logger.info(f"  {doc_type}: {count:,} documents")
        
        if args.dry_run:
            upload_method = "zip files" if args.use_zip else "individual files"
            logger.info("DRY RUN - Would upload:")
            logger.info(f"  Total files: {len(json_files):,}")
            logger.info(f"  Total batches: {len(batches)}")
            logger.info(f"  Batch size: {args.batch_size}")
            logger.info(f"  Upload method: {upload_method}")
            logger.info(f"  Target: s3://article-zip/incoming2/")

            if args.use_zip:
                # Estimate compression savings
                total_size_mb = sum(f.stat().st_size for f in json_files) / (1024*1024)
                estimated_compressed_mb = total_size_mb * 0.2  # Assume 80% compression
                logger.info(f"  Estimated original size: {total_size_mb:.1f} MB")
                logger.info(f"  Estimated compressed size: {estimated_compressed_mb:.1f} MB")
                logger.info(f"  Estimated savings: {total_size_mb - estimated_compressed_mb:.1f} MB")

            return 0
        
        # Initialize S3 uploader
        logger.info("Initializing S3 uploader...")
        uploader = S3LegalDocumentUploader()
        uploader.start_upload_session()
        
        # Create and upload manifest
        manifest = create_processing_manifest(len(json_files), len(batches), doc_type_counts)
        logger.info("Uploading processing manifest...")
        uploader.upload_manifest(manifest)
        
        # Upload batches
        upload_method = "zip files" if args.use_zip else "individual files"
        logger.info(f"Starting upload of {len(batches)} batches as {upload_method}...")
        total_uploaded = 0
        total_failed = 0
        zip_metadata_list = []

        for i, batch_files in enumerate(batches, 1):
            logger.info(f"\n📦 Processing batch {i}/{len(batches)} ({len(batch_files)} files)")

            result = upload_batch_with_retry(uploader, batch_files, i, max_retries=3, use_zip=args.use_zip)

            total_uploaded += result['uploaded']
            total_failed += result['failed']

            # Collect zip metadata if using zip uploads
            if args.use_zip and 'zip_metadata' in result and result['zip_metadata']:
                zip_metadata_list.append(result['zip_metadata'])
            
            # Update manifest with batch status
            batch_status = {
                "batch_id": i,
                "document_range": f"{(i-1)*args.batch_size + 1}-{(i-1)*args.batch_size + len(batch_files)}",
                "s3_path": f"incoming2/batch_{i:06d}/",
                "document_count": result['uploaded'],
                "upload_complete": result['success'],
                "upload_timestamp": datetime.utcnow().isoformat(),
                "failed_count": result['failed']
            }
            manifest['batch_status'].append(batch_status)
            
            # Progress update
            progress = (i / len(batches)) * 100
            logger.info(f"Progress: {progress:.1f}% ({total_uploaded:,} uploaded, {total_failed:,} failed)")
        
        # Finalize upload session
        uploader.end_upload_session()
        
        # Upload zip metadata if using zip uploads
        if args.use_zip and zip_metadata_list:
            logger.info("Uploading zip metadata manifest...")
            uploader.upload_zip_metadata(zip_metadata_list)

            # Add compression statistics to main manifest
            total_original_size = sum(zm['original_total_size'] for zm in zip_metadata_list)
            total_compressed_size = sum(zm['compressed_size'] for zm in zip_metadata_list)
            overall_compression = (total_original_size - total_compressed_size) / total_original_size if total_original_size > 0 else 0

            manifest['compression_statistics'] = {
                'total_original_size_mb': total_original_size / (1024*1024),
                'total_compressed_size_mb': total_compressed_size / (1024*1024),
                'overall_compression_ratio': overall_compression,
                'compression_percentage': overall_compression * 100,
                'space_saved_mb': (total_original_size - total_compressed_size) / (1024*1024)
            }

        # Update final manifest
        manifest['processing_metadata']['processing_complete'] = datetime.utcnow().isoformat()
        manifest['processing_metadata']['upload_method'] = 'zip' if args.use_zip else 'individual'
        manifest['upload_statistics'] = uploader.get_upload_statistics()

        logger.info("Uploading final manifest...")
        uploader.upload_manifest(manifest)
        
        # Final statistics
        stats = uploader.get_upload_statistics()
        logger.info(f"\n🎉 Upload Complete!")
        logger.info(f"  Files uploaded: {stats['files_uploaded']:,}")
        logger.info(f"  Files failed: {stats['files_failed']:,}")
        logger.info(f"  Data uploaded: {stats['bytes_uploaded'] / (1024*1024):.1f} MB")

        # Show compression statistics if using zip
        if args.use_zip and 'compression_statistics' in manifest:
            comp_stats = manifest['compression_statistics']
            logger.info(f"\n📦 Compression Statistics:")
            logger.info(f"  Original size: {comp_stats['total_original_size_mb']:.1f} MB")
            logger.info(f"  Compressed size: {comp_stats['total_compressed_size_mb']:.1f} MB")
            logger.info(f"  Compression ratio: {comp_stats['compression_percentage']:.1f}%")
            logger.info(f"  Space saved: {comp_stats['space_saved_mb']:.1f} MB")

        if 'duration_seconds' in stats:
            logger.info(f"\n⏱️ Performance:")
            logger.info(f"  Duration: {stats['duration_seconds']:.1f} seconds")
            logger.info(f"  Upload rate: {stats.get('upload_rate_mbps', 0):.1f} MB/s")
        
        return 0 if stats['files_failed'] == 0 else 1
        
    except Exception as e:
        logger.error(f"Upload failed: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return 1


if __name__ == "__main__":
    sys.exit(main())
