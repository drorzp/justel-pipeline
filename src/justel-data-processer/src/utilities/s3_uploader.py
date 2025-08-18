#!/usr/bin/env python3
"""
S3 Uploader for Belgian Legal Documents
Handles batch uploads of JSON files to S3 with progress tracking and error recovery.
"""

import os
import boto3
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import logging
from botocore.exceptions import ClientError, NoCredentialsError
import time
import zipfile
import tempfile
import shutil


class S3LegalDocumentUploader:
    """
    S3 uploader specifically designed for Belgian legal document JSON files.
    Supports batch uploads, progress tracking, and error recovery.
    """
    
    def __init__(self,
                 region: str = "us-east-2",
                 bucket: str = "article-zip",
                 prefix: str = "incoming2/",
                 access_key_id: str = None,
                 secret_access_key: str = None):
        """
        Initialize S3 uploader with Belgian legal document configuration.
        
        Args:
            region: AWS region
            bucket: S3 bucket name
            prefix: S3 key prefix for legal documents
            access_key_id: AWS access key ID (defaults to env var AWS_ACCESS_KEY_ID)
            secret_access_key: AWS secret access key (defaults to env var AWS_SECRET_ACCESS_KEY)
        """
        self.region = region
        self.bucket = bucket
        self.prefix = prefix.rstrip('/') + '/'  # Ensure trailing slash
        
        # Get credentials from environment variables if not provided
        if access_key_id is None:
            access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
        if secret_access_key is None:
            secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        
        if not access_key_id or not secret_access_key:
            raise ValueError("AWS credentials not provided. Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables.")
        
        # Initialize S3 client
        try:
            self.s3_client = boto3.client(
                's3',
                region_name=region,
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key
            )
            
            # Test connection
            self.s3_client.head_bucket(Bucket=bucket)
            
        except NoCredentialsError:
            raise Exception("AWS credentials not found or invalid")
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                raise Exception(f"Bucket '{bucket}' not found")
            else:
                raise Exception(f"S3 connection error: {e}")
        
        # Setup logging
        self.logger = logging.getLogger(__name__)
        
        # Upload statistics
        self.stats = {
            'files_uploaded': 0,
            'files_failed': 0,
            'bytes_uploaded': 0,
            'upload_start_time': None,
            'upload_end_time': None
        }
    
    def generate_s3_key(self, file_path: Path, batch_id: Optional[int] = None) -> str:
        """
        Generate S3 key for a legal document JSON file.
        
        Args:
            file_path: Local file path
            batch_id: Optional batch ID for organization
            
        Returns:
            S3 key string
        """
        filename = file_path.name
        
        if batch_id is not None:
            # Organize by batch: legal-documents/batch_000001/document.json
            return f"{self.prefix}batch_{batch_id:06d}/{filename}"
        else:
            # Direct upload: legal-documents/document.json
            return f"{self.prefix}{filename}"
    
    def upload_single_file(self, file_path: Path, s3_key: str, 
                          metadata: Optional[Dict] = None) -> Tuple[bool, str]:
        """
        Upload a single JSON file to S3.
        
        Args:
            file_path: Local file path
            s3_key: S3 key for the file
            metadata: Optional metadata to attach
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            # Calculate file hash for integrity
            file_hash = self._calculate_file_hash(file_path)

            # Prepare metadata
            upload_metadata = metadata.copy() if metadata else {}
            upload_metadata['file_hash'] = file_hash

            # Prepare extra arguments for upload_file
            extra_args = {
                'ContentType': 'application/json',
                'StorageClass': 'STANDARD',
                'Metadata': {k: str(v) for k, v in upload_metadata.items()}
            }

            # Upload file
            self.s3_client.upload_file(
                str(file_path),
                self.bucket,
                s3_key,
                ExtraArgs=extra_args
            )
            
            # Update statistics
            file_size = file_path.stat().st_size
            self.stats['files_uploaded'] += 1
            self.stats['bytes_uploaded'] += file_size
            
            return True, f"Successfully uploaded {file_path.name}"
            
        except Exception as e:
            self.stats['files_failed'] += 1
            error_msg = f"Failed to upload {file_path.name}: {str(e)}"
            self.logger.error(error_msg)
            return False, error_msg
    
    def create_batch_zip(self, file_paths: List[Path], batch_id: int,
                        temp_dir: Optional[Path] = None) -> Tuple[Path, Dict]:
        """
        Create a zip file containing a batch of JSON files.

        Args:
            file_paths: List of JSON file paths to include in zip
            batch_id: Batch identifier for naming
            temp_dir: Optional temporary directory for zip file

        Returns:
            Tuple of (zip_file_path, zip_metadata)
        """
        if temp_dir is None:
            temp_dir = Path(tempfile.gettempdir())

        zip_filename = f"batch_{batch_id:06d}.zip"
        zip_path = temp_dir / zip_filename

        # Create zip file
        total_original_size = 0
        file_list = []

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
            for file_path in file_paths:
                if not file_path.exists():
                    self.logger.warning(f"File not found, skipping: {file_path}")
                    continue

                # Add file to zip with just the filename (no directory structure)
                arcname = file_path.name
                zipf.write(file_path, arcname)

                # Track metadata
                file_size = file_path.stat().st_size
                total_original_size += file_size
                file_list.append({
                    'filename': file_path.name,
                    'original_size': file_size,
                    'document_type': self._extract_document_type(file_path)
                })

        # Calculate compression statistics
        zip_size = zip_path.stat().st_size
        compression_ratio = (total_original_size - zip_size) / total_original_size if total_original_size > 0 else 0

        zip_metadata = {
            'batch_id': batch_id,
            'zip_filename': zip_filename,
            'file_count': len(file_list),
            'original_total_size': total_original_size,
            'compressed_size': zip_size,
            'compression_ratio': compression_ratio,
            'compression_percentage': compression_ratio * 100,
            'files': file_list,
            'created_at': datetime.utcnow().isoformat()
        }

        self.logger.info(
            f"Created zip {zip_filename}: {len(file_list)} files, "
            f"{total_original_size / (1024*1024):.1f}MB → {zip_size / (1024*1024):.1f}MB "
            f"({compression_ratio*100:.1f}% compression)"
        )

        return zip_path, zip_metadata

    def upload_batch_as_zip(self, file_paths: List[Path], batch_id: int,
                           temp_dir: Optional[Path] = None,
                           cleanup_zip: bool = True) -> Dict:
        """
        Create a zip file from batch files and upload to S3.

        Args:
            file_paths: List of JSON file paths to zip and upload
            batch_id: Batch identifier
            temp_dir: Optional temporary directory for zip creation
            cleanup_zip: Whether to delete zip file after upload

        Returns:
            Dictionary with upload results and zip metadata
        """
        if not file_paths:
            return {'success': True, 'uploaded': 0, 'failed': 0, 'errors': [], 'zip_metadata': None}

        self.logger.info(f"Creating and uploading zip for batch {batch_id}: {len(file_paths)} files")

        try:
            # Create zip file
            zip_path, zip_metadata = self.create_batch_zip(file_paths, batch_id, temp_dir)

            # Generate S3 key for zip file
            s3_key = f"{self.prefix}batches/batch_{batch_id:06d}.zip"

            # Prepare upload metadata
            upload_metadata = {
                'batch_id': str(batch_id),
                'content_type': 'batch_zip',
                'file_count': str(zip_metadata['file_count']),
                'original_size': str(zip_metadata['original_total_size']),
                'compression_ratio': str(zip_metadata['compression_ratio']),
                'upload_timestamp': datetime.utcnow().isoformat()
            }

            # Upload zip file
            success, message = self.upload_single_file(zip_path, s3_key, upload_metadata)

            if success:
                # Verify upload
                if self.verify_upload(s3_key, zip_path):
                    result = {
                        'success': True,
                        'uploaded': len(file_paths),
                        'failed': 0,
                        'errors': [],
                        'zip_metadata': zip_metadata,
                        's3_key': s3_key,
                        'zip_size': zip_metadata['compressed_size']
                    }
                    self.logger.info(f"✅ Batch {batch_id} zip uploaded and verified successfully")
                else:
                    result = {
                        'success': False,
                        'uploaded': 0,
                        'failed': len(file_paths),
                        'errors': ['Upload verification failed'],
                        'zip_metadata': zip_metadata
                    }
                    self.logger.error(f"❌ Batch {batch_id} zip upload verification failed")
            else:
                result = {
                    'success': False,
                    'uploaded': 0,
                    'failed': len(file_paths),
                    'errors': [message],
                    'zip_metadata': zip_metadata
                }
                self.logger.error(f"❌ Batch {batch_id} zip upload failed: {message}")

            # Cleanup zip file if requested
            if cleanup_zip and zip_path.exists():
                zip_path.unlink()
                self.logger.debug(f"Cleaned up temporary zip file: {zip_path}")

            return result

        except Exception as e:
            error_msg = f"Failed to create/upload zip for batch {batch_id}: {str(e)}"
            self.logger.error(error_msg)
            return {
                'success': False,
                'uploaded': 0,
                'failed': len(file_paths),
                'errors': [error_msg],
                'zip_metadata': None
            }

    def upload_batch(self, file_paths: List[Path], batch_id: int,
                    max_workers: int = 10, use_zip: bool = False) -> Dict:
        """
        Upload a batch of JSON files to S3 in parallel.

        Args:
            file_paths: List of file paths to upload
            batch_id: Batch identifier for S3 organization
            max_workers: Maximum number of parallel uploads
            use_zip: If True, compress batch into zip file before upload

        Returns:
            Dictionary with upload results and statistics
        """
        if use_zip:
            # Use zip upload method
            return self.upload_batch_as_zip(file_paths, batch_id)

        # Original individual file upload method
        if not file_paths:
            return {'success': True, 'uploaded': 0, 'failed': 0, 'errors': []}
        
        self.logger.info(f"Starting batch {batch_id} upload: {len(file_paths)} files")
        
        # Prepare upload tasks
        upload_tasks = []
        for file_path in file_paths:
            s3_key = self.generate_s3_key(file_path, batch_id)
            metadata = {
                'batch_id': str(batch_id),
                'document_type': self._extract_document_type(file_path),
                'upload_timestamp': datetime.utcnow().isoformat()
            }
            upload_tasks.append((file_path, s3_key, metadata))
        
        # Execute parallel uploads
        results = {'uploaded': 0, 'failed': 0, 'errors': []}
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all upload tasks
            future_to_task = {
                executor.submit(self.upload_single_file, file_path, s3_key, metadata): 
                (file_path, s3_key, metadata)
                for file_path, s3_key, metadata in upload_tasks
            }
            
            # Process completed uploads
            for future in as_completed(future_to_task):
                file_path, s3_key, metadata = future_to_task[future]
                try:
                    success, message = future.result()
                    if success:
                        results['uploaded'] += 1
                        self.logger.debug(f"✅ {file_path.name} → s3://{self.bucket}/{s3_key}")
                    else:
                        results['failed'] += 1
                        results['errors'].append(message)
                        self.logger.error(f"❌ {file_path.name}: {message}")
                        
                except Exception as e:
                    results['failed'] += 1
                    error_msg = f"Upload task failed for {file_path.name}: {str(e)}"
                    results['errors'].append(error_msg)
                    self.logger.error(error_msg)
        
        # Log batch results
        success_rate = (results['uploaded'] / len(file_paths)) * 100
        self.logger.info(
            f"Batch {batch_id} complete: {results['uploaded']}/{len(file_paths)} "
            f"uploaded ({success_rate:.1f}% success rate)"
        )
        
        results['success'] = results['failed'] == 0
        results['batch_id'] = batch_id
        return results
    
    def upload_zip_metadata(self, zip_metadata_list: List[Dict]) -> bool:
        """
        Upload zip metadata manifest to S3.

        Args:
            zip_metadata_list: List of zip metadata dictionaries

        Returns:
            Success boolean
        """
        metadata_key = f"{self.prefix}metadata/zip_contents.json"

        try:
            zip_manifest = {
                'zip_metadata': zip_metadata_list,
                'total_zips': len(zip_metadata_list),
                'total_files': sum(zm['file_count'] for zm in zip_metadata_list),
                'total_original_size': sum(zm['original_total_size'] for zm in zip_metadata_list),
                'total_compressed_size': sum(zm['compressed_size'] for zm in zip_metadata_list),
                'overall_compression_ratio': 0,  # Will calculate below
                'generated_at': datetime.utcnow().isoformat()
            }

            # Calculate overall compression ratio
            if zip_manifest['total_original_size'] > 0:
                zip_manifest['overall_compression_ratio'] = (
                    zip_manifest['total_original_size'] - zip_manifest['total_compressed_size']
                ) / zip_manifest['total_original_size']

            manifest_json = json.dumps(zip_manifest, indent=2, ensure_ascii=False)

            self.s3_client.put_object(
                Bucket=self.bucket,
                Key=metadata_key,
                Body=manifest_json.encode('utf-8'),
                ContentType='application/json',
                Metadata={
                    'content_type': 'zip_metadata_manifest',
                    'generated_at': datetime.utcnow().isoformat()
                }
            )

            self.logger.info(f"Zip metadata uploaded to s3://{self.bucket}/{metadata_key}")
            return True

        except Exception as e:
            self.logger.error(f"Failed to upload zip metadata: {str(e)}")
            return False

    def upload_manifest(self, manifest_data: Dict, manifest_key: str = None) -> bool:
        """
        Upload processing manifest to S3.
        
        Args:
            manifest_data: Manifest data dictionary
            manifest_key: Optional custom S3 key for manifest
            
        Returns:
            Success boolean
        """
        if manifest_key is None:
            manifest_key = f"{self.prefix}metadata/processing_manifest.json"
        
        try:
            manifest_json = json.dumps(manifest_data, indent=2, ensure_ascii=False)
            
            self.s3_client.put_object(
                Bucket=self.bucket,
                Key=manifest_key,
                Body=manifest_json.encode('utf-8'),
                ContentType='application/json',
                Metadata={
                    'content_type': 'processing_manifest',
                    'generated_at': datetime.utcnow().isoformat()
                }
            )
            
            self.logger.info(f"Manifest uploaded to s3://{self.bucket}/{manifest_key}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to upload manifest: {str(e)}")
            return False
    
    def verify_upload(self, s3_key: str, local_file_path: Path) -> bool:
        """
        Verify that uploaded file matches local file.
        
        Args:
            s3_key: S3 key of uploaded file
            local_file_path: Local file path for comparison
            
        Returns:
            True if files match, False otherwise
        """
        try:
            # Get S3 object metadata
            response = self.s3_client.head_object(Bucket=self.bucket, Key=s3_key)
            s3_size = response['ContentLength']
            
            # Compare file sizes
            local_size = local_file_path.stat().st_size
            if s3_size != local_size:
                return False
            
            # Compare file hashes if available in metadata
            if 'Metadata' in response and 'file_hash' in response['Metadata']:
                s3_hash = response['Metadata']['file_hash']
                local_hash = self._calculate_file_hash(local_file_path)
                return s3_hash == local_hash
            
            # If no hash available, size match is sufficient
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to verify upload for {s3_key}: {str(e)}")
            return False
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA256 hash of file for integrity checking."""
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    
    def _extract_document_type(self, file_path: Path) -> str:
        """
        Extract document type from filename or file content.
        Belgian legal documents: CONSTITUTION, LOI, DECRET, ORDONNANCE, ARRETE
        """
        filename = file_path.name.lower()
        
        # Try to determine from filename patterns
        if 'constitution' in filename:
            return 'CONSTITUTION'
        elif 'loi' in filename:
            return 'LOI'
        elif 'decret' in filename:
            return 'DECRET'
        elif 'ordonnance' in filename:
            return 'ORDONNANCE'
        elif 'arrete' in filename:
            return 'ARRETE'
        
        # If not determinable from filename, try reading JSON content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('document_type', 'UNKNOWN')
        except:
            return 'UNKNOWN'
    
    def get_upload_statistics(self) -> Dict:
        """Get current upload statistics."""
        stats = self.stats.copy()
        
        if stats['upload_start_time'] and stats['upload_end_time']:
            duration = stats['upload_end_time'] - stats['upload_start_time']
            stats['duration_seconds'] = duration
            
            if duration > 0:
                stats['upload_rate_mbps'] = (stats['bytes_uploaded'] / (1024*1024)) / duration
                stats['files_per_second'] = stats['files_uploaded'] / duration
        
        return stats
    
    def start_upload_session(self):
        """Mark the start of an upload session."""
        self.stats['upload_start_time'] = time.time()
    
    def end_upload_session(self):
        """Mark the end of an upload session."""
        self.stats['upload_end_time'] = time.time()


# Example usage and testing
if __name__ == "__main__":
    # Example usage
    uploader = S3LegalDocumentUploader()
    
    # Test connection
    print("S3 uploader initialized successfully!")
    print(f"Target: s3://{uploader.bucket}/{uploader.prefix}")
