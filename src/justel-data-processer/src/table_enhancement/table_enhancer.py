#!/usr/bin/env python3
"""
table_enhancer.py - LLM-based enhancement of preserved HTML tables

This module takes preserved HTML tables and enhances them using an LLM to:
1. Add proper table structure (thead, tbody)
2. Create bilingual headers with proper formatting
3. Improve cell organization and grouping
4. Add appropriate CSS classes and accessibility attributes

Author: Augment Agent
Date: 2025-07-24
"""

import json
import logging
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import requests
import time

logger = logging.getLogger(__name__)

class TableEnhancer:
    """Enhanced table formatting using LLM."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the table enhancer.

        Args:
            api_key: OpenAI API key for LLM enhancement
        """
        self.api_key = api_key
        self.session = requests.Session()

        if api_key:
            try:
                self.session.headers.update({
                    'Authorization': f'Bearer {api_key}',
                    'Content-Type': 'application/json'
                })
                logger.info("✅ OpenAI API initialized for table enhancement")
            except Exception as e:
                logger.warning(f"⚠️ Failed to initialize OpenAI API: {e}")
                self.api_key = None
        else:
            logger.info("⚠️ No API key provided - table enhancement will be skipped")
    
    def enhance_preserved_tables(self, preserved_tables_dir: str) -> Dict[str, int]:
        """
        Enhance all preserved tables in a directory.

        Args:
            preserved_tables_dir: Directory containing preserved table JSON files

        Returns:
            Dictionary with enhancement statistics
        """
        # COMMENTED OUT: LLM enhancement was too slow and produced poor results
        logger.info("🚫 LLM table enhancement is disabled - preserving raw tables for manual enhancement")
        return {"enhanced": 0, "failed": 0, "skipped": 0}

        # Original LLM enhancement code (commented out):
        # if not self.api_key:
        #     logger.warning("No API key available - skipping table enhancement")
        #     return {"enhanced": 0, "failed": 0, "skipped": 0}
        
        preserved_dir = Path(preserved_tables_dir)
        if not preserved_dir.exists():
            logger.error(f"Preserved tables directory not found: {preserved_tables_dir}")
            return {"enhanced": 0, "failed": 0, "skipped": 0}
        
        stats = {"enhanced": 0, "failed": 0, "skipped": 0}
        
        # Process all table files
        for table_file in preserved_dir.glob("*_tables.json"):
            try:
                document_stats = self._enhance_document_tables(table_file)
                for key in stats:
                    stats[key] += document_stats[key]
            except Exception as e:
                logger.error(f"Error processing {table_file}: {e}")
                stats["failed"] += 1
        
        logger.info(f"Table enhancement complete: {stats}")
        return stats
    
    def _enhance_document_tables(self, table_file: Path) -> Dict[str, int]:
        """
        Enhance all tables in a single document using batch processing.

        Args:
            table_file: Path to the document's table JSON file

        Returns:
            Enhancement statistics for this document
        """
        stats = {"enhanced": 0, "failed": 0, "skipped": 0}

        # Load preserved tables
        with open(table_file, 'r', encoding='utf-8') as f:
            tables = json.load(f)

        logger.info(f"Processing {len(tables)} tables from {table_file.name}")

        # Separate tables that need enhancement vs those that are already well-formatted
        tables_to_enhance = {}
        enhanced_tables = {}

        for placeholder, html_content in tables.items():
            if self._is_already_well_formatted(html_content):
                enhanced_tables[placeholder] = html_content
                stats["skipped"] += 1
                logger.debug(f"Table {placeholder} already well-formatted, skipping")
            else:
                tables_to_enhance[placeholder] = html_content

        # Batch enhance the tables that need enhancement
        if tables_to_enhance:
            # Process in smaller batches to avoid timeouts
            batch_size = 3  # Process 3 tables at a time to avoid timeouts
            table_items = list(tables_to_enhance.items())

            for i in range(0, len(table_items), batch_size):
                batch = dict(table_items[i:i + batch_size])
                logger.info(f"Processing batch {i//batch_size + 1}/{(len(table_items) + batch_size - 1)//batch_size} ({len(batch)} tables)")

                # Check if batch is too large (estimate prompt size)
                total_size = sum(len(html) for html in batch.values())
                if total_size > 15000:  # If batch is too large, process individually
                    logger.info(f"Batch too large ({total_size} chars), processing individually")
                    for placeholder, html_content in batch.items():
                        try:
                            single_batch = {placeholder: html_content}
                            batch_enhanced = self._enhance_tables_batch(single_batch)
                            enhanced_html = batch_enhanced.get(placeholder, html_content)
                            if enhanced_html and enhanced_html != html_content:
                                enhanced_tables[placeholder] = enhanced_html
                                stats["enhanced"] += 1
                                logger.debug(f"Enhanced {placeholder}")
                            else:
                                enhanced_tables[placeholder] = html_content
                                stats["skipped"] += 1
                        except Exception as e:
                            logger.error(f"Individual enhancement failed for {placeholder}: {e}")
                            enhanced_tables[placeholder] = html_content
                            stats["failed"] += 1
                else:
                    try:
                        batch_enhanced = self._enhance_tables_batch(batch)
                        for placeholder, enhanced_html in batch_enhanced.items():
                            if enhanced_html and enhanced_html != batch[placeholder]:
                                enhanced_tables[placeholder] = enhanced_html
                                stats["enhanced"] += 1
                                logger.debug(f"Enhanced {placeholder}")
                            else:
                                enhanced_tables[placeholder] = batch[placeholder]
                                stats["skipped"] += 1
                    except Exception as e:
                        logger.error(f"Batch enhancement failed for batch {i//batch_size + 1}: {e}")
                        # Fallback to original tables for this batch
                        for placeholder, html_content in batch.items():
                            enhanced_tables[placeholder] = html_content
                            stats["failed"] += 1

        # Save enhanced tables back to file
        with open(table_file, 'w', encoding='utf-8') as f:
            json.dump(enhanced_tables, f, ensure_ascii=False, indent=2)

        return stats
    
    def _enhance_single_table(self, html_content: str, placeholder: str) -> Optional[str]:
        """
        Enhance a single HTML table using LLM.
        
        Args:
            html_content: Original HTML table content
            placeholder: Table placeholder ID for logging
            
        Returns:
            Enhanced HTML table or None if enhancement failed
        """
        # Skip if table already looks well-formatted
        if self._is_already_well_formatted(html_content):
            logger.debug(f"Table {placeholder} already well-formatted, skipping")
            return html_content
        
        # Create enhancement prompt
        prompt = self._create_enhancement_prompt(html_content)
        
        try:
            # Call OpenAI API for enhancement
            response = self._call_openai_api(prompt)
            enhanced_html = response.strip()

            # Validate the enhanced HTML
            if self._validate_enhanced_html(enhanced_html, html_content):
                logger.debug(f"Successfully enhanced {placeholder}")
                return enhanced_html
            else:
                logger.warning(f"Enhanced HTML for {placeholder} failed validation")
                return html_content

        except Exception as e:
            logger.error(f"LLM enhancement failed for {placeholder}: {e}")
            return html_content
    
    def _is_already_well_formatted(self, html_content: str) -> bool:
        """
        Check if a table is already well-formatted.
        
        Args:
            html_content: HTML table content
            
        Returns:
            True if table appears to be well-formatted
        """
        # Check for good formatting indicators
        has_thead = '<thead>' in html_content
        has_tbody = '<tbody>' in html_content
        has_scope = 'scope=' in html_content
        has_proper_class = 'class="legal-table"' in html_content
        
        # If it has most good formatting features, skip enhancement
        return has_thead and has_tbody and has_scope and has_proper_class
    
    def _create_enhancement_prompt(self, html_content: str) -> str:
        """
        Create the LLM prompt for table enhancement.
        
        Args:
            html_content: Original HTML table content
            
        Returns:
            Enhancement prompt for the LLM
        """
        prompt = f"""You are an expert at formatting Belgian legal document tables. Please enhance this HTML table to improve its structure and formatting.

Requirements:
1. Create proper table structure with <thead> and <tbody>
2. Add class="legal-table" to the <table> element
3. Add scope="col" to all <th> elements in the header
4. Create bilingual headers combining French/Dutch with <br> between them
5. Organize court/jurisdiction names as "French / Dutch" format
6. Group related rows logically
7. Use &nbsp; for empty cells
8. Preserve all numbers and legal references exactly
9. Remove malformed closing tags and fix structure
10. Output ONLY the enhanced HTML table, no explanations

Example of desired output structure:
<table class="legal-table">
  <thead>
    <tr>
      <th scope="col">Juridiction</th>
      <th scope="col">Présidents de chambre /<br>Kamervoorzitters</th>
      <th scope="col">Traitement /<br>Vergoeding</th>
      <th scope="col">Autres fonctions /<br>Andere functies</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cour de cassation / Hof van cassatie</td>
      <td>Premier président et procureur général</td>
      <td>69.696,16 EUR</td>
      <td>Président et premier avocat général<br>65.281,40 EUR</td>
    </tr>
  </tbody>
</table>

Here is the table to enhance:
{html_content}"""
        
        return prompt
    
    def _validate_enhanced_html(self, enhanced_html: str, original_html: str) -> bool:
        """
        Validate that the enhanced HTML is properly formatted.
        
        Args:
            enhanced_html: Enhanced HTML from LLM
            original_html: Original HTML for comparison
            
        Returns:
            True if enhanced HTML is valid
        """
        # Basic structure checks
        if not enhanced_html or not enhanced_html.strip():
            return False
        
        # Must contain table tags
        if '<table' not in enhanced_html or '</table>' not in enhanced_html:
            return False
        
        # Should have proper structure
        has_thead = '<thead>' in enhanced_html
        has_tbody = '<tbody>' in enhanced_html
        has_legal_table_class = 'class="legal-table"' in enhanced_html
        
        # Should have some content
        has_content = '<td>' in enhanced_html or '<th>' in enhanced_html
        
        return has_thead and has_tbody and has_legal_table_class and has_content

    def _enhance_tables_batch(self, tables_to_enhance: Dict[str, str]) -> Dict[str, str]:
        """
        Enhance multiple tables in a single API call.

        Args:
            tables_to_enhance: Dictionary of {placeholder: html_content}

        Returns:
            Dictionary of {placeholder: enhanced_html}
        """
        if not tables_to_enhance:
            return {}

        # Create batch enhancement prompt
        batch_prompt = self._create_batch_enhancement_prompt(tables_to_enhance)

        try:
            # Call OpenAI API for batch enhancement
            response = self._call_openai_api(batch_prompt)

            # Parse the batch response
            enhanced_tables = self._parse_batch_response(response, tables_to_enhance)

            logger.info(f"Batch enhanced {len(enhanced_tables)} tables")
            return enhanced_tables

        except Exception as e:
            logger.error(f"Batch enhancement failed: {e}")
            # Return original tables as fallback
            return tables_to_enhance

    def _create_batch_enhancement_prompt(self, tables_to_enhance: Dict[str, str]) -> str:
        """
        Create a batch enhancement prompt for multiple tables.

        Args:
            tables_to_enhance: Dictionary of {placeholder: html_content}

        Returns:
            Batch enhancement prompt
        """
        prompt = """You are an expert at formatting Belgian legal document tables. Please enhance these HTML tables to improve their structure and formatting.

Requirements for each table:
1. Create proper table structure with <thead> and <tbody>
2. Add class="legal-table" to the <table> element
3. Add scope="col" to all <th> elements in the header
4. Create bilingual headers combining French/Dutch with <br> between them
5. Organize court/jurisdiction names as "French / Dutch" format
6. Group related rows logically
7. Use &nbsp; for empty cells
8. Preserve all numbers and legal references exactly
9. Remove malformed closing tags and fix structure
10. Output ONLY the enhanced HTML tables, no explanations

For each table, output the enhanced HTML in this format:
=== TABLE_PLACEHOLDER_XXXX ===
<enhanced HTML here>
=== END_TABLE ===

Here are the tables to enhance:

"""

        for placeholder, html_content in tables_to_enhance.items():
            prompt += f"=== {placeholder} ===\n{html_content}\n=== END_INPUT ===\n\n"

        return prompt

    def _parse_batch_response(self, response: str, original_tables: Dict[str, str]) -> Dict[str, str]:
        """
        Parse the batch response from OpenAI.

        Args:
            response: Raw response from OpenAI
            original_tables: Original tables for fallback

        Returns:
            Dictionary of enhanced tables
        """
        enhanced_tables = {}

        # Split response by table markers
        sections = response.split('=== TABLE_PLACEHOLDER_')

        for section in sections[1:]:  # Skip first empty section
            try:
                # Extract placeholder and content
                lines = section.split('\n')
                placeholder_line = lines[0].strip()
                placeholder = f"TABLE_PLACEHOLDER_{placeholder_line.split(' ===')[0]}"

                # Find the enhanced HTML content
                content_start = section.find('===\n') + 4
                content_end = section.find('=== END_TABLE ===')

                if content_end == -1:
                    content_end = len(section)

                enhanced_html = section[content_start:content_end].strip()

                # Validate the enhanced HTML
                if placeholder in original_tables and self._validate_enhanced_html(enhanced_html, original_tables[placeholder]):
                    enhanced_tables[placeholder] = enhanced_html
                else:
                    # Use original if validation fails
                    enhanced_tables[placeholder] = original_tables[placeholder]

            except Exception as e:
                logger.warning(f"Failed to parse section: {e}")
                continue

        # Fill in any missing tables with originals
        for placeholder in original_tables:
            if placeholder not in enhanced_tables:
                enhanced_tables[placeholder] = original_tables[placeholder]

        return enhanced_tables

    def _call_openai_api(self, prompt: str, max_retries: int = 3) -> str:
        """
        Call OpenAI API to enhance the table with retry logic.

        Args:
            prompt: The enhancement prompt
            max_retries: Maximum number of retry attempts

        Returns:
            Enhanced HTML from OpenAI
        """
        url = "https://api.openai.com/v1/chat/completions"

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.1,
            "max_tokens": 8000  # Increased for larger responses
        }

        # Calculate timeout based on prompt size
        prompt_size = len(prompt)
        if prompt_size > 20000:
            timeout = 180  # 3 minutes for very large requests
        elif prompt_size > 10000:
            timeout = 120  # 2 minutes for large requests
        else:
            timeout = 60   # 1 minute for normal requests

        logger.debug(f"Using timeout: {timeout}s for prompt size: {prompt_size} chars")

        for attempt in range(max_retries + 1):
            try:
                if attempt > 0:
                    wait_time = 2 ** attempt  # Exponential backoff: 2, 4, 8 seconds
                    logger.info(f"Retrying API call (attempt {attempt + 1}/{max_retries + 1}) after {wait_time}s...")
                    time.sleep(wait_time)

                response = self.session.post(url, json=payload, timeout=timeout)
                response.raise_for_status()

                data = response.json()
                return data['choices'][0]['message']['content']

            except requests.exceptions.Timeout as e:
                logger.warning(f"API request timed out (attempt {attempt + 1}/{max_retries + 1}): {e}")
                if attempt == max_retries:
                    raise
            except requests.exceptions.RequestException as e:
                logger.error(f"OpenAI API request failed (attempt {attempt + 1}/{max_retries + 1}): {e}")
                if attempt == max_retries:
                    raise
            except KeyError as e:
                logger.error(f"Unexpected OpenAI API response format: {e}")
                raise  # Don't retry on parsing errors


def enhance_tables_for_document(document_id: str, preserved_tables_dir: str, api_key: Optional[str] = None) -> bool:
    """
    Enhance tables for a specific document.
    
    Args:
        document_id: Document ID (filename without extension)
        preserved_tables_dir: Directory containing preserved tables
        api_key: Google Gemini API key
        
    Returns:
        True if enhancement was successful
    """
    enhancer = TableEnhancer(api_key)
    
    table_file = Path(preserved_tables_dir) / f"{document_id}_tables.json"
    if not table_file.exists():
        logger.error(f"Table file not found: {table_file}")
        return False
    
    try:
        stats = enhancer._enhance_document_tables(table_file)
        logger.info(f"Enhanced tables for {document_id}: {stats}")
        return stats["enhanced"] > 0 or stats["skipped"] > 0
    except Exception as e:
        logger.error(f"Failed to enhance tables for {document_id}: {e}")
        return False


if __name__ == "__main__":
    import sys
    import os
    
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    if len(sys.argv) < 2:
        print("Usage: python table_enhancer.py <preserved_tables_dir> [api_key]")
        sys.exit(1)
    
    preserved_tables_dir = sys.argv[1]
    api_key = sys.argv[2] if len(sys.argv) > 2 else os.getenv('OPENAI_API_KEY')

    if not api_key:
        print("Warning: No API key provided. Set OPENAI_API_KEY environment variable or pass as argument.")
        sys.exit(1)
    
    enhancer = TableEnhancer(api_key)
    stats = enhancer.enhance_preserved_tables(preserved_tables_dir)
    
    print(f"Table enhancement complete:")
    print(f"  Enhanced: {stats['enhanced']}")
    print(f"  Failed: {stats['failed']}")
    print(f"  Skipped: {stats['skipped']}")
