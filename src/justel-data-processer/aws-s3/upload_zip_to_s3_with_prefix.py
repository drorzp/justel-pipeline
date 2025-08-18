#!/usr/bin/env python3
"""
Upload ZIP file containing Belgian legal documents to S3 with custom prefix.

This script is specifically designed to upload pre-created ZIP files
to S3 with a configurable prefix for different document categories.
"""

import sys
import logging
import argparse
from pathlib import Path
from datetime import datetime
import zipfile
import json
from typing import Dict, Any

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
    # Try adding the current directory to the path as fallback
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_dir)
    try:
        from src.utilities.s3_uploader import S3LegalDocumentUploader
    except ImportError:
        print("Error: Could not import S3LegalDocumentUploader")
        print("Make sure src/utilities/s3_uploader.py exists and is accessible")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Script directory: {current_dir}")
        print(f"Python path: {sys.path}")
        sys.exit(1)


def setup_logging(level: str = 'INFO') -> logging.Logger:
    """Setup logging configuration."""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('s3_upload.log', mode='w')
        ]
    )
    return logging.getLogger(__name__)


def analyze_zip_contents(zip_path: Path) -> Dict[str, Any]:
    """Analyze the contents of a ZIP file to extract metadata."""
    logger = logging.getLogger(__name__)
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            file_list = zipf.namelist()
            json_files = [f for f in file_list if f.endswith('.json')]
            
            # Sample a few files to get document types
            document_types = {}
            sample_size = min(10, len(json_files))
            
            for json_file in json_files[:sample_size]:
                try:
                    with zipf.open(json_file) as f:
                        data = json.load(f)
                        doc_type = data.get('document_metadata', {}).get('document_type', 'unknown')
                        document_types[doc_type] = document_types.get(doc_type, 0) + 1
                except Exception as e:
                    logger.warning(f"Could not analyze {json_file}: {e}")
            
            # Calculate total size
            total_size = sum(zipf.getinfo(f).file_size for f in json_files)
            
            metadata = {
                'total_files': len(json_files),
                'total_size_bytes': total_size,
                'total_size_mb': total_size / (1024 * 1024),
                'zip_size_bytes': zip_path.stat().st_size,
                'zip_size_mb': zip_path.stat().st_size / (1024 * 1024),
                'compression_ratio': 1 - (zip_path.stat().st_size / total_size) if total_size > 0 else 0,
                'sample_document_types': document_types,
                'file_list_sample': json_files[:5]  # First 5 files as sample
            }
            
            return metadata
            
    except Exception as e:
        logger.error(f"Error analyzing ZIP file: {e}")
        return {}


def upload_zip_file(zip_path: Path, s3_prefix: str = "incoming3", dry_run: bool = False) -> bool:
    """Upload a ZIP file to S3 with specified prefix."""
    logger = logging.getLogger(__name__)
    
    if not zip_path.exists():
        logger.error(f"ZIP file not found: {zip_path}")
        return False
    
    if not zip_path.suffix.lower() == '.zip':
        logger.error(f"File is not a ZIP file: {zip_path}")
        return False
    
    logger.info(f"Preparing to upload ZIP file: {zip_path}")
    logger.info(f"ZIP file size: {zip_path.stat().st_size / (1024*1024):.1f} MB")
    logger.info(f"S3 prefix: {s3_prefix}/")
    
    # Analyze ZIP contents
    logger.info("Analyzing ZIP file contents...")
    metadata = analyze_zip_contents(zip_path)
    
    if metadata:
        logger.info(f"ZIP contains {metadata['total_files']} JSON files")
        logger.info(f"Total uncompressed size: {metadata['total_size_mb']:.1f} MB")
        logger.info(f"Compression ratio: {metadata['compression_ratio']*100:.1f}%")
        if metadata['sample_document_types']:
            logger.info("Sample document types found:")
            for doc_type, count in metadata['sample_document_types'].items():
                logger.info(f"  {doc_type}: {count} files (in sample)")
    
    if dry_run:
        logger.info("DRY RUN - Would upload ZIP file to S3")
        logger.info(f"Target: s3://article-zip/{s3_prefix}/")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logger.info(f"S3 key: {s3_prefix}/{timestamp}_{zip_path.name}")
        return True
    
    try:
        # Initialize S3 uploader
        logger.info("Initializing S3 uploader...")
        uploader = S3LegalDocumentUploader()
        
        # Generate S3 key for the ZIP file with custom prefix
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        s3_key = f"{s3_prefix}/{timestamp}_{zip_path.name}"
        
        # Prepare upload metadata
        upload_metadata = {
            'content_type': 'legal_documents_zip',
            'file_count': str(metadata.get('total_files', 0)),
            'original_size': str(metadata.get('total_size_bytes', 0)),
            'compression_ratio': str(metadata.get('compression_ratio', 0)),
            'upload_timestamp': datetime.utcnow().isoformat(),
            'source_pipeline': 'comprehensive_belgian_legal_pipeline',
            's3_prefix': s3_prefix
        }
        
        # Upload the ZIP file
        logger.info(f"Uploading to S3 key: {s3_key}")
        success, message = uploader.upload_single_file(zip_path, s3_key, upload_metadata)
        
        if success:
            logger.info("✅ ZIP file uploaded successfully to S3")
            logger.info(f"S3 location: s3://article-zip/{s3_key}")
            return True
        else:
            logger.error(f"❌ Failed to upload ZIP file: {message}")
            return False
            
    except Exception as e:
        logger.error(f"❌ Error during S3 upload: {e}")
        return False


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Upload ZIP file containing Belgian legal documents to S3 with custom prefix')
    parser.add_argument('zip_file', help='Path to ZIP file to upload')
    parser.add_argument('--prefix', default='incoming3',
                       help='S3 prefix for upload (default: incoming3)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be uploaded without actually uploading')
    parser.add_argument('--log-level', default='INFO',
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       help='Logging level (default: INFO)')
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logging(args.log_level)
    
    logger.info("="*80)
    logger.info("BELGIAN LEGAL DOCUMENTS - ZIP FILE S3 UPLOADER WITH CUSTOM PREFIX")
    logger.info("="*80)
    logger.info(f"ZIP file: {args.zip_file}")
    logger.info(f"S3 prefix: {args.prefix}")
    logger.info(f"Dry run: {args.dry_run}")
    logger.info(f"Log level: {args.log_level}")
    
    try:
        zip_path = Path(args.zip_file)
        success = upload_zip_file(zip_path, args.prefix, dry_run=args.dry_run)
        
        if success:
            logger.info("🎉 Upload completed successfully!")
            return 0
        else:
            logger.error("❌ Upload failed")
            return 1
            
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
