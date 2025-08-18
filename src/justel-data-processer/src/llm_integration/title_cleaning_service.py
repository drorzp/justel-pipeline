#!/usr/bin/env python3
"""
title_cleaning_service.py - Service for LLM-powered title cleaning integration

This module provides a service that integrates LLM-powered title cleaning into the
Belgian legal document processing pipeline. It handles batch processing, error recovery,
and maintains backwards compatibility with the existing JSON structure.

Author: Augment Agent
Date: 2025-07-21
"""

import logging
import json
import os
import time
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path
from dataclasses import dataclass

from .openai_client import OpenAIClient, OpenAIConfig, GeminiAPIError

logger = logging.getLogger(__name__)

@dataclass
class TitleCleaningConfig:
    """Configuration for the title cleaning service."""
    api_key: str
    batch_size: int = 20
    enable_cleaning: bool = True
    fallback_on_error: bool = True
    max_retries_per_batch: int = 2
    delay_between_batches: float = 0.5
    backup_original_titles: bool = True
    log_cleaning_results: bool = True


class TitleCleaningService:
    """
    Service for cleaning document titles using LLM integration.
    
    This service:
    - Processes JSON files to clean document titles
    - Maintains backwards compatibility by preserving original titles
    - Handles batch processing for efficiency
    - Provides error recovery and fallback mechanisms
    - Logs cleaning operations for monitoring
    """
    
    def __init__(self, config: TitleCleaningConfig):
        """
        Initialize the title cleaning service.
        
        Args:
            config: TitleCleaningConfig object with service settings
        """
        self.config = config
        self.stats = {
            "files_processed": 0,
            "titles_cleaned": 0,
            "titles_failed": 0,
            "api_calls_made": 0,
            "total_processing_time": 0.0
        }
        
        # Initialize OpenAI client if cleaning is enabled
        if self.config.enable_cleaning:
            openai_config = OpenAIConfig(
                api_key=self.config.api_key,
                max_retries=3,
                retry_delay=1.0
            )
            self.openai_client = OpenAIClient(openai_config)

            # Test connection
            if not self.openai_client.test_connection():
                logger.warning("OpenAI API connection test failed. Title cleaning will be disabled.")
                self.config.enable_cleaning = False
        else:
            self.openai_client = None
            logger.info("Title cleaning is disabled")
    
    def process_json_file(self, file_path: Path) -> bool:
        """
        Process a single JSON file to clean its document title.
        
        Args:
            file_path: Path to the JSON file to process
            
        Returns:
            True if processing was successful, False otherwise
        """
        try:
            logger.debug(f"Processing file: {file_path}")
            
            # Load the JSON file
            with open(file_path, 'r', encoding='utf-8') as f:
                document = json.load(f)
            
            # Check if document has the expected structure
            if 'document_metadata' not in document:
                logger.warning(f"File {file_path} missing document_metadata, skipping")
                return False
            
            metadata = document['document_metadata']
            
            # Check if title exists
            if 'title' not in metadata or not metadata['title']:
                logger.warning(f"File {file_path} missing title, skipping")
                return False
            
            original_title = metadata['title']
            
            # Skip if title is already cleaned (has raw_title field)
            if 'raw_title' in metadata:
                logger.debug(f"File {file_path} already has cleaned title, skipping")
                return True
            
            # Clean the title if service is enabled
            if self.config.enable_cleaning:
                cleaned_title = self._clean_single_title(original_title)
                
                if cleaned_title and cleaned_title != original_title:
                    # Update the document structure
                    metadata['raw_title'] = original_title
                    metadata['title'] = cleaned_title
                    
                    # Add cleaning metadata
                    if 'title_cleaning' not in metadata:
                        metadata['title_cleaning'] = {}
                    
                    metadata['title_cleaning'].update({
                        'cleaned_at': time.time(),
                        'cleaning_method': 'openai_llm',
                        'original_length': len(original_title),
                        'cleaned_length': len(cleaned_title)
                    })
                    
                    # Save the updated file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(document, f, ensure_ascii=False, indent=2)
                    
                    self.stats['titles_cleaned'] += 1
                    
                    if self.config.log_cleaning_results:
                        logger.info(f"Cleaned title for {file_path.name}: '{original_title[:50]}...' -> '{cleaned_title[:50]}...'")
                else:
                    # Cleaning failed - do not mark as processed
                    logger.warning(f"Title cleaning failed for {file_path.name}, file will not be marked as processed")
                    self.stats['titles_failed'] += 1
                    return False
            else:
                # Cleaning disabled, just add raw_title field for consistency
                metadata['raw_title'] = original_title
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(document, f, ensure_ascii=False, indent=2)
            
            self.stats['files_processed'] += 1
            return True
            
        except Exception as e:
            logger.error(f"Error processing file {file_path}: {str(e)}")
            self.stats['titles_failed'] += 1
            return False
    
    def _clean_single_title(self, title: str) -> Optional[str]:
        """
        Clean a single title using the LLM service.
        
        Args:
            title: The raw title to clean
            
        Returns:
            Cleaned title or None if cleaning failed
        """
        try:
            cleaned_titles, metadata = self.openai_client.clean_titles([title])
            self.stats['api_calls_made'] += 1
            self.stats['total_processing_time'] += metadata.get('processing_time_seconds', 0)

            if metadata['status'] == 'success' and len(cleaned_titles) == 1:
                return cleaned_titles[0]
            else:
                logger.warning(f"Failed to clean title: {metadata.get('error_message', 'Unknown error')}")
                return None

        except Exception as e:
            logger.error(f"Error cleaning title '{title[:50]}...': {str(e)}")
            return None
    
    def process_batch_files(self, file_paths: List[Path]) -> Dict[str, Any]:
        """
        Process a batch of JSON files for title cleaning.
        
        Args:
            file_paths: List of paths to JSON files to process
            
        Returns:
            Dictionary with batch processing results
        """
        start_time = time.time()
        successful_files = 0
        failed_files = 0
        
        logger.info(f"Processing batch of {len(file_paths)} files for title cleaning")
        
        for i, file_path in enumerate(file_paths):
            try:
                if self.process_json_file(file_path):
                    successful_files += 1
                else:
                    failed_files += 1
                
                # Add delay between files to avoid rate limiting
                if i < len(file_paths) - 1:  # Don't delay after the last file
                    time.sleep(self.config.delay_between_batches)
                    
            except Exception as e:
                logger.error(f"Unexpected error processing {file_path}: {str(e)}")
                failed_files += 1
        
        processing_time = time.time() - start_time
        
        results = {
            "total_files": len(file_paths),
            "successful_files": successful_files,
            "failed_files": failed_files,
            "processing_time_seconds": round(processing_time, 2),
            "titles_cleaned": self.stats['titles_cleaned'],
            "api_calls_made": self.stats['api_calls_made']
        }
        
        logger.info(f"Batch processing completed: {successful_files}/{len(file_paths)} files successful")
        
        return results
    
    def process_directory(self, directory_path: Path, file_pattern: str = "*.json") -> Dict[str, Any]:
        """
        Process all JSON files in a directory for title cleaning.
        
        Args:
            directory_path: Path to the directory containing JSON files
            file_pattern: Glob pattern for matching files (default: "*.json")
            
        Returns:
            Dictionary with processing results
        """
        if not directory_path.exists():
            raise ValueError(f"Directory does not exist: {directory_path}")
        
        # Find all matching files
        json_files = list(directory_path.glob(file_pattern))
        
        if not json_files:
            logger.warning(f"No files found matching pattern '{file_pattern}' in {directory_path}")
            return {"total_files": 0, "successful_files": 0, "failed_files": 0}
        
        logger.info(f"Found {len(json_files)} files to process in {directory_path}")
        
        # Process files in batches
        all_results = []
        
        for i in range(0, len(json_files), self.config.batch_size):
            batch_files = json_files[i:i + self.config.batch_size]
            batch_results = self.process_batch_files(batch_files)
            all_results.append(batch_results)
            
            # Log progress
            logger.info(f"Completed batch {i // self.config.batch_size + 1}/{(len(json_files) + self.config.batch_size - 1) // self.config.batch_size}")
        
        # Aggregate results
        total_results = {
            "total_files": sum(r["total_files"] for r in all_results),
            "successful_files": sum(r["successful_files"] for r in all_results),
            "failed_files": sum(r["failed_files"] for r in all_results),
            "total_processing_time_seconds": sum(r["processing_time_seconds"] for r in all_results),
            "total_titles_cleaned": self.stats['titles_cleaned'],
            "total_api_calls_made": self.stats['api_calls_made']
        }
        
        return total_results
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get current processing statistics.
        
        Returns:
            Dictionary with current statistics
        """
        return self.stats.copy()
    
    def reset_statistics(self):
        """Reset processing statistics."""
        self.stats = {
            "files_processed": 0,
            "titles_cleaned": 0,
            "titles_failed": 0,
            "api_calls_made": 0,
            "total_processing_time": 0.0
        }
