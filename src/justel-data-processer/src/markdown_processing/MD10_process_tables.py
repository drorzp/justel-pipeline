#!/usr/bin/env python3
"""
MD10_process_tables.py - Table Processing for Belgian Legal Documents

This script processes JSON files to replace [TABLE_PLACEHOLDER_X] with actual HTML tables
from preserved table files. It handles both main_text_raw and main_text fields.

This script should be run after MD9_clean_titles.py in the pipeline.

Author: Augment Agent
Date: 2025-07-25
"""

import os
import sys
import json
import logging
import glob
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.llm_integration.table_generation_service_html import HTMLTableProcessor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
TABLES_FOLDER = "output/16/preserved_tables"
USE_LLM_ENHANCEMENT = False  # Disabled by default to avoid API costs
OUTPUT_DIR = "output"

def process_single_file(json_file_path: str, tables_folder: str = TABLES_FOLDER, 
                       use_llm: bool = USE_LLM_ENHANCEMENT) -> bool:
    """
    Process a single JSON file to replace table placeholders.
    
    Args:
        json_file_path: Path to the JSON file to process
        tables_folder: Path to preserved tables folder
        use_llm: Whether to use LLM enhancement (disabled by default)
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Extract document ID from filename
        document_id = Path(json_file_path).stem
        
        # Initialize processor (no OpenAI client needed when use_llm=False)
        processor = HTMLTableProcessor(openai_client=None)
        
        # Load the JSON document
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        tables_processed = 0
        
        # Process articles in the document (recursive function)
        def process_article(node):
            nonlocal tables_processed

            if node.get('type') == 'article':
                article_content = node.get('article_content')
                if not article_content:
                    return  # Skip articles without content

                content = article_content.get('content', {})
                main_text_raw = content.get('main_text_raw', '')
                main_text = content.get('main_text', '')
                article_number = content.get('article_number', 'unknown')

                # Process tables in main_text_raw (original text)
                if '[TABLE_PLACEHOLDER_' in main_text_raw:
                    try:
                        processed_text = processor.process_document_tables(
                            document_id, main_text_raw, tables_folder, use_llm
                        )
                        if processed_text != main_text_raw:
                            content['main_text_raw'] = processed_text
                            content['has_preserved_tables'] = True
                            tables_processed += 1
                            logger.info(f"✅ Processed tables in main_text_raw for article {article_number}")
                    except Exception as e:
                        logger.warning(f"Failed to process tables in main_text_raw for article {article_number}: {str(e)}")

                # Process tables in main_text (structured HTML content)
                if '[TABLE_PLACEHOLDER_' in main_text:
                    try:
                        processed_html = processor.process_document_tables(
                            document_id, main_text, tables_folder, use_llm
                        )
                        if processed_html != main_text:
                            content['main_text'] = processed_html
                            content['has_preserved_tables'] = True
                            tables_processed += 1
                            logger.info(f"✅ Processed tables in main_text for article {article_number}")
                    except Exception as e:
                        logger.warning(f"Failed to process tables in main_text for article {article_number}: {str(e)}")

            # Process children recursively (for nested hierarchical structures)
            for child in node.get('children', []):
                process_article(child)
        
        # Process all root nodes
        for root_node in data.get('document_hierarchy', []):
            process_article(root_node)
        
        # Save the updated JSON if any tables were processed
        if tables_processed > 0:
            with open(json_file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            logger.info(f"✅ Processed {tables_processed} table sections in {Path(json_file_path).name}")
        else:
            logger.info(f"ℹ️  No table placeholders found in {Path(json_file_path).name}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Error processing {json_file_path}: {str(e)}")
        return False

def process_directory(output_dir: str = OUTPUT_DIR, tables_folder: str = TABLES_FOLDER,
                     use_llm: bool = USE_LLM_ENHANCEMENT) -> None:
    """
    Process all JSON files in the output directory.
    
    Args:
        output_dir: Directory containing JSON files
        tables_folder: Path to preserved tables folder
        use_llm: Whether to use LLM enhancement
    """
    logger.info("🔄 Starting table processing for all JSON files...")
    logger.info(f"📁 Output directory: {output_dir}")
    logger.info(f"📋 Tables folder: {tables_folder}")
    logger.info(f"🤖 LLM enhancement: {'Enabled' if use_llm else 'Disabled'}")
    
    # Find all JSON files
    json_pattern = os.path.join(output_dir, "**", "*.json")
    json_files = glob.glob(json_pattern, recursive=True)
    
    if not json_files:
        logger.warning(f"⚠️  No JSON files found in {output_dir}")
        return
    
    logger.info(f"📄 Found {len(json_files)} JSON files to process")
    
    # Check if tables folder exists
    if not os.path.exists(tables_folder):
        logger.warning(f"⚠️  Tables folder not found: {tables_folder}")
        logger.info("ℹ️  Table placeholders will be left as-is")
    
    # Process each file
    successful = 0
    failed = 0
    
    for i, json_file in enumerate(json_files, 1):
        logger.info(f"📄 Processing file {i}/{len(json_files)}: {Path(json_file).name}")
        
        if process_single_file(json_file, tables_folder, use_llm):
            successful += 1
        else:
            failed += 1
    
    # Summary
    logger.info("=" * 60)
    logger.info("📊 TABLE PROCESSING SUMMARY")
    logger.info("=" * 60)
    logger.info(f"✅ Successfully processed: {successful} files")
    logger.info(f"❌ Failed to process: {failed} files")
    logger.info(f"📄 Total files: {len(json_files)}")
    
    if failed > 0:
        logger.warning(f"⚠️  {failed} files had processing errors")
    else:
        logger.info("🎉 All files processed successfully!")

def main():
    """Main entry point."""
    logger.info("🚀 Starting MD10 Table Processing")
    logger.info("=" * 60)
    
    try:
        # Process all files in the output directory
        process_directory()
        
        logger.info("✅ MD10 Table Processing completed successfully")
        
    except Exception as e:
        logger.error(f"❌ MD10 Table Processing failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
