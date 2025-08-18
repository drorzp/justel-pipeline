# AWS S3 Upload Scripts

This directory contains all AWS S3-related scripts for uploading processed Belgian legal documents.

## Scripts Overview

### Core Upload Scripts

- **`upload_to_s3.py`** - Basic S3 upload functionality for individual JSON files
- **`upload_zip_to_s3.py`** - Upload ZIP archives to S3 with metadata
- **`upload_zip_to_s3_with_prefix.py`** - Upload ZIP files with custom S3 prefixes
- **`batch_upload_to_s3.py`** - Batch upload management for large document collections

### Log Files

- **`batch_s3_upload.log`** - Log file for batch upload operations

## Usage

### Basic ZIP Upload
```bash
python aws-s3/upload_zip_to_s3.py /path/to/archive.zip
```

### Upload with Custom Prefix
```bash
python aws-s3/upload_zip_to_s3_with_prefix.py /path/to/archive.zip --prefix incoming2
```

### Batch Upload
```bash
python aws-s3/batch_upload_to_s3.py --input-dir /path/to/json/files --batch-size 100
```

## Dependencies

All scripts depend on:
- `src/utilities/s3_uploader.py` - Core S3 upload functionality
- AWS credentials configured (via AWS CLI, environment variables, or IAM roles)
- `boto3` Python package

## Configuration

Scripts automatically detect AWS credentials from:
1. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
2. AWS credentials file (`~/.aws/credentials`)
3. IAM roles (when running on EC2)

## Integration

These scripts are used by:
- `comprehensive_pipeline.py` - Main processing pipeline
- Manual upload operations for processed documents

## Notes

- All scripts include error handling and retry logic
- Upload progress is logged for monitoring
- ZIP files include metadata for tracking and validation
- Custom S3 prefixes allow for organized storage (e.g., `incoming2/`, `incoming_no_articles2/`)
