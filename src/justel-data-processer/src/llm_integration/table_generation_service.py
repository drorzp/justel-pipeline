#!/usr/bin/env python3
"""
table_generation_service.py - Service for generating HTML tables from pipe-separated text using LLM

This service uses OpenAI GPT-4o-mini to convert pipe-separated table text
into properly formatted HTML tables for Belgian legal documents.

Author: Augment Agent
Date: 2025-07-24
"""

import logging
import time
from typing import Optional, Dict, Any
from dataclasses import dataclass

from .openai_client import OpenAIClient, OpenAIConfig, OpenAIAPIError
from .table_generation_prompt import (
    get_table_generation_prompt,
    validate_table_html,
    validate_table_html_simple,
    extract_table_from_text,
    clean_table_text,
    analyze_table_structure,
    post_process_html,
    TABLE_GENERATION_CONFIG
)

logger = logging.getLogger(__name__)


@dataclass
class TableGenerationConfig:
    """Configuration for the table generation service."""
    api_key: str
    enable_generation: bool = True
    fallback_on_error: bool = True
    max_retries: int = 2
    timeout: int = 30
    log_generation_results: bool = True
    model: str = "gpt-4o-mini"
    temperature: float = 0.1
    max_tokens: int = 4000


class TableGenerationService:
    """
    Service for generating HTML tables from pipe-separated text using LLM.
    
    This service:
    - Detects table content in text
    - Converts pipe-separated tables to HTML using OpenAI GPT-4o-mini
    - Handles bilingual Belgian legal document tables
    - Provides error recovery and fallback mechanisms
    - Logs generation operations for monitoring
    """
    
    def __init__(self, config: TableGenerationConfig):
        """
        Initialize the table generation service.
        
        Args:
            config: TableGenerationConfig object with service settings
        """
        self.config = config
        self.stats = {
            'tables_generated': 0,
            'api_calls_made': 0,
            'total_processing_time': 0,
            'errors_encountered': 0
        }
        
        # Initialize OpenAI client if generation is enabled
        if self.config.enable_generation:
            openai_config = OpenAIConfig(
                api_key=self.config.api_key,
                model=self.config.model,
                max_retries=self.config.max_retries,
                timeout=self.config.timeout,
                retry_delay=1.0,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )
            self.openai_client = OpenAIClient(openai_config)

            # Test connection
            if not self.openai_client.test_connection():
                logger.warning("OpenAI API connection test failed. Table generation will be disabled.")
                self.config.enable_generation = False
        else:
            self.openai_client = None
            logger.info("Table generation is disabled")
    
    def detect_and_generate_table(self, text: str) -> Optional[str]:
        """
        Detect table content in text and generate HTML table if found.
        
        Args:
            text: Text that may contain pipe-separated table content
            
        Returns:
            HTML table string if table detected and generated successfully, None otherwise
        """
        if not self.config.enable_generation:
            return None
        
        # Extract table content from text
        table_text = extract_table_from_text(text)
        if not table_text:
            return None
        
        # Validate table meets minimum requirements
        if not self._validate_table_requirements(table_text):
            return None
        
        # Generate HTML table
        return self.generate_table_html(table_text)
    
    def generate_table_html(self, table_text: str) -> Optional[str]:
        """
        Generate HTML table from pipe-separated table text.
        
        Args:
            table_text: Pipe-separated table text
            
        Returns:
            HTML table string if generation successful, None otherwise
        """
        if not self.config.enable_generation or not self.openai_client:
            return None

        try:
            start_time = time.time()

            # Debug: Log the table text being sent to OpenAI
            logger.info(f"🔍 Sending table text to OpenAI (length: {len(table_text)} chars)")
            logger.info(f"📝 Table text preview: {table_text[:200]}...")
            logger.info(f"🔍 Full table text: {table_text}")

            # Clean and prepare table text
            cleaned_table_text = clean_table_text(table_text)

            # Generate prompt with the simplified format
            prompt = get_table_generation_prompt(cleaned_table_text)

            # Make API request
            html_output = self.openai_client._make_api_request(prompt)
            self.stats['api_calls_made'] += 1

            # Debug: Log the raw response from OpenAI
            logger.info(f"📤 Raw OpenAI response preview: {html_output[:300]}...")

            # Clean up the output (remove markdown code blocks and extra whitespace)
            html_output = self._clean_llm_output(html_output)

            # Enhanced validation with detailed error reporting
            is_valid, validation_errors = validate_table_html(html_output)
            if not is_valid:
                logger.warning(f"Generated HTML table failed validation: {', '.join(validation_errors)}")
                self.stats['errors_encountered'] += 1
                return None

            # Post-process the HTML for better formatting
            if TABLE_GENERATION_CONFIG.get('post_process_output', True):
                html_output = post_process_html(html_output)
            
            processing_time = time.time() - start_time
            self.stats['total_processing_time'] += processing_time
            self.stats['tables_generated'] += 1
            
            if self.config.log_generation_results:
                rows_count = table_text.count('\n') + 1
                logger.info(f"Generated HTML table with {rows_count} rows in {processing_time:.2f}s")
            
            return html_output
            
        except OpenAIAPIError as e:
            logger.error(f"OpenAI API error during table generation: {str(e)}")
            self.stats['errors_encountered'] += 1
            return None
        except Exception as e:
            logger.error(f"Unexpected error during table generation: {str(e)}")
            self.stats['errors_encountered'] += 1
            return None
    
    def _validate_table_requirements(self, table_text: str) -> bool:
        """
        Validate that table text meets minimum requirements for processing.
        
        Args:
            table_text: Table text to validate
            
        Returns:
            True if table meets requirements, False otherwise
        """
        if not table_text or not table_text.strip():
            return False
        
        lines = [line.strip() for line in table_text.split('\n') if line.strip()]
        
        # Check minimum number of rows
        if len(lines) < TABLE_GENERATION_CONFIG['min_table_rows']:
            return False
        
        # Check that each line has minimum number of columns
        for line in lines:
            if line.count('|') + 1 < TABLE_GENERATION_CONFIG['min_columns']:
                return False
        
        # Check maximum table size
        if len(lines) > TABLE_GENERATION_CONFIG['max_table_size']:
            logger.warning(f"Table too large ({len(lines)} rows), skipping generation")
            return False
        
        return True
    
    def is_bilingual_table(self, table_text: str) -> bool:
        """
        Determine if table appears to be bilingual (Dutch/French).
        
        Args:
            table_text: Table text to analyze
            
        Returns:
            True if table appears to be bilingual
        """
        indicators = TABLE_GENERATION_CONFIG['bilingual_indicators']
        
        # Check first few lines for bilingual indicators
        lines = table_text.split('\n')[:3]  # Check first 3 lines
        for line in lines:
            for indicator in indicators:
                if indicator in line:
                    return True
        
        return False
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get service statistics.
        
        Returns:
            Dictionary with service statistics
        """
        return {
            **self.stats,
            'service_enabled': self.config.enable_generation,
            'average_processing_time': (
                self.stats['total_processing_time'] / max(1, self.stats['api_calls_made'])
            ),
            'success_rate': (
                self.stats['tables_generated'] / max(1, self.stats['api_calls_made'])
            ) if self.stats['api_calls_made'] > 0 else 0
        }
    
    def reset_stats(self):
        """Reset service statistics."""
        self.stats = {
            'tables_generated': 0,
            'api_calls_made': 0,
            'total_processing_time': 0,
            'errors_encountered': 0
        }
    
    def test_connection(self) -> bool:
        """
        Test the connection to the OpenAI API.

        Returns:
            True if connection is successful, False otherwise
        """
        if not self.config.enable_generation or not self.openai_client:
            return False

        return self.openai_client.test_connection()

    def _clean_llm_output(self, raw_output: str) -> str:
        """
        Clean the raw LLM output by removing markdown code blocks and extra formatting.

        Args:
            raw_output: Raw output from the LLM

        Returns:
            Cleaned HTML output
        """
        if not raw_output:
            return ""

        # Remove markdown code blocks
        output = raw_output.strip()

        # Remove ```html at the beginning
        if output.startswith('```html'):
            output = output[7:].strip()
        elif output.startswith('```'):
            output = output[3:].strip()

        # Remove ``` at the end
        if output.endswith('```'):
            output = output[:-3].strip()

        # Remove any extra whitespace and newlines
        output = output.strip()

        return output


# Convenience function for quick table generation
def generate_table_html_quick(table_text: str, api_key: str) -> Optional[str]:
    """
    Quick function to generate HTML table from text using default configuration.

    Args:
        table_text: Pipe-separated table text
        api_key: OpenAI API key

    Returns:
        HTML table string if successful, None otherwise
    """
    config = TableGenerationConfig(
        api_key=api_key,
        enable_generation=True,
        log_generation_results=False
    )
    
    service = TableGenerationService(config)
    return service.generate_table_html(table_text)
