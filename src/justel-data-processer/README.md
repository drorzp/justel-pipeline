# Belgian Legal Documents Processing Pipeline

A comprehensive Python pipeline for scraping, processing, and uploading Belgian legal documents from the Justel website to AWS S3.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- AWS account with S3 access
- OpenAI API key (for title cleaning functionality)

## Installation

### 1. Install Python Dependencies

Navigate to the `justel-data-processer` directory and install all required packages:

```bash
cd src/justel-data-processer
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the `justel-data-processer` directory with your credentials:

```bash
cp .env.example .env
```

Edit the `.env` file and add your credentials:

```
# AWS Credentials for S3 uploads
AWS_ACCESS_KEY_ID=your_actual_aws_access_key
AWS_SECRET_ACCESS_KEY=your_actual_aws_secret_key

# OpenAI API Key for title cleaning
OPENAI_API_KEY=your_actual_openai_api_key
```

**Important:** Never commit the `.env` file to version control. It's already in `.gitignore`.

## Directory Structure

```
justel-data-processer/
├── data/
│   └── csv_data/
│       └── full-list.csv        # Master list of all URLs to process
├── input/                        # Scraped HTML/text files (created automatically)
├── output/                       # Processed JSON files (created automatically)
├── logs/                         # Processing logs (created automatically)
├── populate_full_list.py         # Step 1: URL discovery
├── run_comprehensive_html_scraping.py  # Step 2: HTML scraping
├── comprehensive_pipeline.py     # Step 3: Document processing
└── aws-s3/                       # S3 upload utilities
```

## Running the Pipeline

The pipeline consists of three main scripts that should be run in sequence:

### Option 1: Run from Node.js (Recommended)

If running as part of the larger Node.js pipeline:

```bash
# From the project root
npm run start
```

This will automatically run all three Python scripts in sequence.

### Option 2: Run Python Scripts Individually

#### Step 1: Update URL List

Discovers new URLs from the Justel website and updates the master CSV:

```bash
python populate_full_list.py
```

This script:
- Reads the last URL from `data/csv_data/full-list.csv`
- Scrapes new URLs from the Justel website since that date
- Appends new URLs to the CSV file

#### Step 2: Scrape HTML Content

Downloads HTML content for all URLs in the CSV:

```bash
# Production mode (processes all URLs)
python run_comprehensive_html_scraping.py --concurrent 35 --delay 0.02 --resume

# Test mode (processes only 10 URLs for testing)
python run_comprehensive_html_scraping.py --test --test-limit 10
```

Parameters:
- `--concurrent`: Number of concurrent requests (default: 35)
- `--delay`: Delay between batches in seconds (default: 0.02)
- `--resume`: Resume from checkpoint if interrupted
- `--test`: Run in test mode
- `--test-limit`: Number of URLs to process in test mode

This script:
- Reads URLs from the CSV
- Downloads HTML content for each URL
- Saves as text files in the `input/` directory
- Supports resuming if interrupted

#### Step 3: Process Documents and Upload to S3

Processes scraped HTML through the text processing pipeline and uploads to S3:

```bash
# Production mode (processes all files)
python comprehensive_pipeline.py --process-all --batch-size 1000

# Test mode (processes only 3 files for testing)
python comprehensive_pipeline.py --max-files 3 --batch-size 3
```

Parameters:
- `--process-all`: Process all files in input directory
- `--batch-size`: Number of files per batch (default: 1000)
- `--max-files`: Maximum number of files to process (for testing)
- `--dry-run`: Simulate execution without making changes

This script:
- Processes text files through multiple transformation steps
- Converts to Markdown
- Extracts structured JSON
- Validates JSON structure
- Creates ZIP archives
- Uploads to S3 buckets:
  - Valid documents → `s3://article-zip/incoming3/`
  - Invalid documents → `s3://article-zip/incoming_no_articles3/`

## Testing the Installation

### 1. Test Environment Setup

```bash
# Check Python version
python --version  # Should be 3.8+

# Test package installation
python -c "import pandas, boto3, openai, requests, beautifulsoup4; print('All packages installed')"

# Test environment variables
python -c "
from dotenv import load_dotenv
import os
load_dotenv()
print('AWS_ACCESS_KEY_ID:', 'Set' if os.environ.get('AWS_ACCESS_KEY_ID') else 'Not set')
print('AWS_SECRET_ACCESS_KEY:', 'Set' if os.environ.get('AWS_SECRET_ACCESS_KEY') else 'Not set')
print('OPENAI_API_KEY:', 'Set' if os.environ.get('OPENAI_API_KEY') else 'Not set')
"
```

### 2. Test Pipeline Components

```bash
# Test URL discovery (dry run, no new URLs expected if up to date)
python populate_full_list.py

# Test HTML scraping with 5 URLs
python run_comprehensive_html_scraping.py --test --test-limit 5

# Test document processing with 3 files
python comprehensive_pipeline.py --max-files 3 --batch-size 3
```

## Monitoring and Logs

- Logs are automatically created in the `logs/` directory
- Each script creates timestamped log files
- Invalid JSON files are logged separately for review

## S3 Bucket Structure

Processed documents are uploaded to S3 with the following structure:

```
s3://article-zip/
├── incoming3/                    # Valid documents (with content)
│   └── 20250818_125123_belgian_legal_batch_000_valid_*.zip
└── incoming_no_articles3/        # Invalid documents (empty/malformed)
    └── 20250818_125135_belgian_legal_batch_000_invalid_*.zip
```

## Troubleshooting

### Common Issues

1. **ImportError: No module named 'xxx'**
   - Solution: Run `pip install -r requirements.txt`

2. **AWS credentials not provided**
   - Solution: Ensure `.env` file exists and contains valid AWS credentials
   - Test with: `python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.environ.get('AWS_ACCESS_KEY_ID'))"`

3. **OpenAI API key not found**
   - Solution: Add OPENAI_API_KEY to `.env` file
   - Note: Title cleaning will be skipped if API key is missing

4. **No .txt files found in input directory**
   - Solution: Run `populate_full_list.py` and `run_comprehensive_html_scraping.py` first

5. **S3 upload fails**
   - Check AWS credentials are correct
   - Verify S3 bucket exists and you have write permissions
   - Check network connectivity

### Performance Tuning

- Adjust `--concurrent` parameter in scraping based on server capacity
- Increase `--batch-size` for better performance with large datasets
- Use `--resume` flag to continue from interruptions

## Production Deployment

For production deployment on a server:

1. Clone the repository
2. Install Python 3.8+ if not present
3. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies: `pip install -r requirements.txt`
5. Configure `.env` with production credentials
6. Set up a cron job or scheduler to run the pipeline periodically
7. Monitor logs in the `logs/` directory

## Cron Job Example

To run the pipeline daily at 2 AM:

```bash
# Edit crontab
crontab -e

# Add this line (adjust paths as needed)
0 2 * * * cd /path/to/justel-data-processer && /usr/bin/python3 populate_full_list.py && /usr/bin/python3 run_comprehensive_html_scraping.py --resume && /usr/bin/python3 comprehensive_pipeline.py --process-all
```

## Support

For issues or questions about the pipeline, check:
- Log files in the `logs/` directory
- Error messages in console output
- AWS S3 console for uploaded files
- This README for common solutions

## Security Notes

- Never commit `.env` file or credentials to version control
- Regularly rotate AWS access keys
- Use IAM roles with minimal required permissions
- Keep OpenAI API key secure and monitor usage