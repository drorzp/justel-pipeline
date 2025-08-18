#!/usr/bin/env python3
"""
MD9_clean_titles.py - LLM-powered title cleaning for Belgian legal documents

This script integrates into the main processing pipeline to clean document titles
using OpenAI's GPT-4o-mini model. It processes JSON files in the
output directory and cleans their titles while preserving original data.

This script should be run after MD8_extract_to_json.py in the pipeline.

Author: Augment Agent
Date: 2025-07-25
"""

import logging
import sys
import os
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.llm_integration import TitleCleaningService, TitleCleaningConfig

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
API_KEY = os.environ.get('OPENAI_API_KEY', '')
INPUT_DIR = Path("output")
BATCH_SIZE = 15  # Conservative batch size to avoid rate limits
ENABLE_CLEANING = True  # Set to False to disable LLM cleaning (will still add raw_title field)


def find_json_files(directory: Path) -> list:
    """
    Find all JSON files in the directory and subdirectories.
    
    Args:
        directory: Directory to search for JSON files
        
    Returns:
        List of Path objects for JSON files
    """
    json_files = []
    
    if not directory.exists():
        logger.error(f"Directory does not exist: {directory}")
        return json_files
    
    # Search for JSON files in all subdirectories
    for json_file in directory.rglob("*.json"):
        json_files.append(json_file)
    
    return sorted(json_files)


def main():
    """Main processing function."""
    logger.info("🚀 Starting LLM-powered title cleaning for Belgian legal documents")
    
    # Check if input directory exists
    if not INPUT_DIR.exists():
        logger.error(f"❌ Input directory does not exist: {INPUT_DIR}")
        sys.exit(1)
    
    # Find all JSON files
    json_files = find_json_files(INPUT_DIR)
    
    if not json_files:
        logger.warning(f"⚠️  No JSON files found in {INPUT_DIR}")
        sys.exit(0)
    
    logger.info(f"📁 Found {len(json_files)} JSON files to process")
    
    # Initialize the title cleaning service
    try:
        config = TitleCleaningConfig(
            api_key=API_KEY,
            batch_size=BATCH_SIZE,
            enable_cleaning=ENABLE_CLEANING,
            fallback_on_error=True,
            delay_between_batches=0.5,
            log_cleaning_results=True
        )
        
        service = TitleCleaningService(config)
        
        # Test API connection if cleaning is enabled
        if ENABLE_CLEANING:
            logger.info("🔗 Testing API connection...")
            if hasattr(service, 'openai_client') and service.openai_client:
                if not service.openai_client.test_connection():
                    logger.warning("⚠️  API connection test failed. Proceeding with raw_title field addition only.")
                    config.enable_cleaning = False
                else:
                    logger.info("✅ API connection successful")
            else:
                logger.warning("⚠️  OpenAI client not initialized. Proceeding with raw_title field addition only.")
                config.enable_cleaning = False
        
    except Exception as e:
        logger.error(f"❌ Failed to initialize title cleaning service: {str(e)}")
        sys.exit(1)
    
    # Process files by directory to maintain organization
    directories_processed = set()
    total_successful = 0
    total_failed = 0
    
    for json_file in json_files:
        file_dir = json_file.parent
        
        if file_dir not in directories_processed:
            logger.info(f"📂 Processing directory: {file_dir}")
            directories_processed.add(file_dir)
        
        try:
            if service.process_json_file(json_file):
                total_successful += 1
                logger.debug(f"✅ Processed: {json_file.name}")
            else:
                total_failed += 1
                logger.warning(f"⚠️  Failed to process: {json_file.name}")
                
        except Exception as e:
            total_failed += 1
            logger.error(f"❌ Error processing {json_file.name}: {str(e)}")
    
    # Get final statistics
    stats = service.get_statistics()
    
    # Log final results
    logger.info("📊 Title Cleaning Results:")
    logger.info(f"   Total files found: {len(json_files)}")
    logger.info(f"   Successfully processed: {total_successful}")
    logger.info(f"   Failed to process: {total_failed}")
    logger.info(f"   Titles cleaned by LLM: {stats['titles_cleaned']}")
    logger.info(f"   API calls made: {stats['api_calls_made']}")
    logger.info(f"   Total processing time: {stats['total_processing_time']:.2f}s")
    
    if total_failed == 0:
        logger.info("🎉 All files processed successfully!")
        sys.exit(0)
    elif total_successful > 0:
        logger.warning(f"⚠️  Completed with {total_failed} failures out of {len(json_files)} files")
        sys.exit(0)  # Still consider success if some files were processed
    else:
        logger.error("❌ All files failed to process!")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("⏹️  Processing interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")
        sys.exit(1)
