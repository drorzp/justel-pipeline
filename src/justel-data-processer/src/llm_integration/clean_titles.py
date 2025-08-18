#!/usr/bin/env python3
"""
clean_titles.py - Standalone script for cleaning Belgian legal document titles

This script can be run standalone to clean titles in existing JSON files or integrated
into the main processing pipeline. It provides comprehensive title cleaning using
Google Gemini 2.5 Flash-Lite Preview 06-17.

Usage:
    python clean_titles.py --directory output/24 --api-key YOUR_API_KEY
    python clean_titles.py --file output/24/1967101053.json --api-key YOUR_API_KEY
    python clean_titles.py --test-connection --api-key YOUR_API_KEY

Author: Augment Agent
Date: 2025-07-21
"""

import argparse
import logging
import sys
import os
from pathlib import Path
from typing import Optional

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.llm_integration.title_cleaning_service import TitleCleaningService, TitleCleaningConfig
from src.llm_integration.openai_client import OpenAIClient, OpenAIConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('title_cleaning.log')
    ]
)
logger = logging.getLogger(__name__)

# Get API key from environment variable
DEFAULT_API_KEY = os.environ.get('OPENAI_API_KEY', '')


def test_api_connection(api_key: str) -> bool:
    """
    Test the connection to the OpenAI API.

    Args:
        api_key: The API key to test

    Returns:
        True if connection is successful, False otherwise
    """
    try:
        logger.info("Testing OpenAI API connection...")

        config = OpenAIConfig(api_key=api_key)
        client = OpenAIClient(config)
        
        if client.test_connection():
            logger.info("✅ API connection test successful!")
            return True
        else:
            logger.error("❌ API connection test failed!")
            return False
            
    except Exception as e:
        logger.error(f"❌ API connection test failed with error: {str(e)}")
        return False


def clean_single_file(file_path: Path, api_key: str) -> bool:
    """
    Clean titles in a single JSON file.
    
    Args:
        file_path: Path to the JSON file
        api_key: API key for Gemini
        
    Returns:
        True if successful, False otherwise
    """
    try:
        logger.info(f"Cleaning titles in file: {file_path}")
        
        config = TitleCleaningConfig(
            api_key=api_key,
            enable_cleaning=True,
            log_cleaning_results=True
        )
        
        service = TitleCleaningService(config)
        
        if service.process_json_file(file_path):
            logger.info(f"✅ Successfully processed file: {file_path}")
            return True
        else:
            logger.error(f"❌ Failed to process file: {file_path}")
            return False
            
    except Exception as e:
        logger.error(f"❌ Error processing file {file_path}: {str(e)}")
        return False


def clean_directory(directory_path: Path, api_key: str, batch_size: int = 20) -> bool:
    """
    Clean titles in all JSON files in a directory.
    
    Args:
        directory_path: Path to the directory containing JSON files
        api_key: API key for Gemini
        batch_size: Number of files to process in each batch
        
    Returns:
        True if successful, False otherwise
    """
    try:
        logger.info(f"Cleaning titles in directory: {directory_path}")
        
        config = TitleCleaningConfig(
            api_key=api_key,
            batch_size=batch_size,
            enable_cleaning=True,
            log_cleaning_results=True,
            delay_between_batches=0.5
        )
        
        service = TitleCleaningService(config)
        
        results = service.process_directory(directory_path)
        
        logger.info("📊 Processing Results:")
        logger.info(f"   Total files: {results['total_files']}")
        logger.info(f"   Successful: {results['successful_files']}")
        logger.info(f"   Failed: {results['failed_files']}")
        logger.info(f"   Titles cleaned: {results['total_titles_cleaned']}")
        logger.info(f"   API calls made: {results['total_api_calls_made']}")
        logger.info(f"   Processing time: {results['total_processing_time_seconds']:.2f}s")
        
        if results['failed_files'] == 0:
            logger.info("✅ All files processed successfully!")
            return True
        else:
            logger.warning(f"⚠️  {results['failed_files']} files failed to process")
            return results['successful_files'] > 0
            
    except Exception as e:
        logger.error(f"❌ Error processing directory {directory_path}: {str(e)}")
        return False


def main():
    """Main entry point for the title cleaning script."""
    parser = argparse.ArgumentParser(
        description="Clean Belgian legal document titles using LLM",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Test API connection
  python clean_titles.py --test-connection --api-key YOUR_API_KEY
  
  # Clean titles in a single file
  python clean_titles.py --file output/24/1967101053.json --api-key YOUR_API_KEY
  
  # Clean titles in all JSON files in a directory
  python clean_titles.py --directory output/24 --api-key YOUR_API_KEY
  
  # Use environment variable for API key
  export GEMINI_API_KEY=YOUR_API_KEY
  python clean_titles.py --directory output/24
        """
    )
    
    # API key options
    parser.add_argument(
        '--api-key',
        type=str,
        help='Gemini API key (can also be set via GEMINI_API_KEY environment variable)'
    )
    
    # Processing options
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--test-connection',
        action='store_true',
        help='Test the API connection and exit'
    )
    group.add_argument(
        '--file',
        type=Path,
        help='Path to a single JSON file to process'
    )
    group.add_argument(
        '--directory',
        type=Path,
        help='Path to directory containing JSON files to process'
    )
    
    # Additional options
    parser.add_argument(
        '--batch-size',
        type=int,
        default=20,
        help='Number of files to process in each batch (default: 20)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Get API key
    api_key = args.api_key or os.environ.get('GEMINI_API_KEY') or DEFAULT_API_KEY
    
    if not api_key:
        logger.error("❌ No API key provided. Use --api-key or set GEMINI_API_KEY environment variable.")
        sys.exit(1)
    
    # Execute the requested operation
    try:
        if args.test_connection:
            success = test_api_connection(api_key)
        elif args.file:
            if not args.file.exists():
                logger.error(f"❌ File does not exist: {args.file}")
                sys.exit(1)
            success = clean_single_file(args.file, api_key)
        elif args.directory:
            if not args.directory.exists():
                logger.error(f"❌ Directory does not exist: {args.directory}")
                sys.exit(1)
            success = clean_directory(args.directory, api_key, args.batch_size)
        else:
            logger.error("❌ No operation specified")
            sys.exit(1)
        
        if success:
            logger.info("🎉 Operation completed successfully!")
            sys.exit(0)
        else:
            logger.error("❌ Operation failed!")
            sys.exit(1)
            
    except KeyboardInterrupt:
        logger.info("⏹️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
