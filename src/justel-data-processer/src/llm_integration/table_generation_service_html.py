#!/usr/bin/env python3
"""
table_generation_service_html.py - Service for processing preserved HTML tables

This service processes HTML tables that were preserved during the initial HTML to markdown conversion.
Instead of reconstructing tables from text, it cleans and formats the original HTML tables.
"""

import json
import logging
from typing import List, Dict, Optional, Tuple
from pathlib import Path
from bs4 import BeautifulSoup
import re

logger = logging.getLogger(__name__)


class HTMLTableProcessor:
    """Process and clean preserved HTML tables."""
    
    def __init__(self, openai_client=None):
        """
        Initialize the HTML table processor.
        
        Args:
            openai_client: Optional OpenAI client for table enhancement
        """
        self.openai_client = openai_client
    
    def load_preserved_tables(self, document_id: str, tables_folder: str = "output/16/preserved_tables") -> Dict[str, str]:
        """
        Load preserved HTML tables for a document.
        
        Args:
            document_id: The document ID (filename without extension)
            tables_folder: Path to the folder containing preserved tables
            
        Returns:
            Dictionary mapping table IDs to HTML content
        """
        tables_path = Path(tables_folder) / f"{document_id}_tables.json"
        
        if not tables_path.exists():
            logger.warning(f"No preserved tables found for document: {document_id}")
            return {}
        
        with open(tables_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def clean_html_table(self, html_table: str) -> str:
        """
        Clean and standardize an HTML table.
        
        Args:
            html_table: Raw HTML table string
            
        Returns:
            Cleaned HTML table
        """
        soup = BeautifulSoup(html_table, 'html.parser')
        table = soup.find('table')
        
        if not table:
            return html_table
        
        # Add CSS class for styling
        table['class'] = table.get('class', []) + ['legal-table']
        
        # Process headers - ensure proper structure
        headers = table.find_all('th')
        for header in headers:
            if not header.get('scope'):
                header['scope'] = 'col'
        
        # Clean up empty cells
        for cell in table.find_all(['td', 'th']):
            if not cell.get_text(strip=True):
                cell.string = '\u00A0'  # Non-breaking space
        
        # Detect bilingual headers and format them
        self._format_bilingual_headers(table)
        
        return str(table)
    
    def _format_bilingual_headers(self, table):
        """
        Format bilingual (Dutch/French) headers with proper separators.
        """
        # Common bilingual patterns in Belgian legal documents
        bilingual_patterns = [
            (r'(\w+)\s*/\s*(\w+)', r'\1 / \2'),  # Word / Word
            (r'(\w+)\s*\|\s*(\w+)', r'\1 / \2'),  # Word | Word
        ]
        
        for header in table.find_all('th'):
            text = header.get_text(strip=True)
            for pattern, replacement in bilingual_patterns:
                if re.search(pattern, text):
                    header.string = re.sub(pattern, replacement, text)
                    break
    
    def extract_tables_from_content(self, content: str, preserved_tables: Dict[str, str]) -> List[Tuple[str, str]]:
        """
        Extract table placeholders from content and match with preserved tables.
        
        Args:
            content: Markdown content with table placeholders
            preserved_tables: Dictionary of preserved HTML tables
            
        Returns:
            List of tuples (placeholder, html_table)
        """
        tables = []
        
        # Find all table placeholders
        placeholder_pattern = r'\[TABLE_PLACEHOLDER_(\d{4})\]'
        
        for match in re.finditer(placeholder_pattern, content):
            placeholder = match.group(0)
            table_id = f"TABLE_PLACEHOLDER_{match.group(1)}"
            
            if table_id in preserved_tables:
                html_table = preserved_tables[table_id]
                tables.append((placeholder, html_table))
            else:
                logger.warning(f"Table placeholder {table_id} not found in preserved tables")
        
        return tables

    def _clean_standalone_brackets(self, content: str) -> str:
        """
        Clean up standalone closing square brackets that are the only content in paragraph tags.

        Args:
            content: HTML content that may contain standalone brackets

        Returns:
            Content with standalone brackets removed
        """
        import re

        # Pattern to match <p>]</p> or <p> ] </p> (with optional whitespace)
        # This pattern is very specific to avoid removing legitimate brackets
        standalone_bracket_pattern = r'<p>\s*\]\s*</p>'

        # Remove standalone closing brackets in paragraph tags
        cleaned_content = re.sub(standalone_bracket_pattern, '', content, flags=re.IGNORECASE)

        # Clean up any double spaces that might result from the cleanup
        cleaned_content = re.sub(r'\s{2,}', ' ', cleaned_content)

        return cleaned_content

    def enhance_table_with_llm(self, html_table: str) -> str:
        """
        Use LLM to enhance table formatting if needed.
        
        Args:
            html_table: HTML table to enhance
            
        Returns:
            Enhanced HTML table
        """
        if not self.openai_client:
            return self.clean_html_table(html_table)
        
        # Clean the table first
        cleaned_table = self.clean_html_table(html_table)
        
        # Create a prompt for the LLM
        prompt = f"""You are an expert at formatting bilingual (Dutch/French) legal document tables.

Clean and enhance this HTML table following these rules:
1. Ensure proper HTML table structure with <thead> and <tbody>
2. Add class="legal-table" to the <table> element
3. Add scope="col" to all <th> elements
4. Format bilingual headers as "French / Dutch" with proper spacing
5. Preserve all data exactly as provided
6. Ensure the table is well-structured and accessible

Input table:
{cleaned_table}

Output ONLY the enhanced HTML table, no explanations."""
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert HTML table formatter for legal documents."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1
            )
            
            enhanced_html = response.choices[0].message.content.strip()
            
            # Validate the response contains a table
            if '<table' in enhanced_html and '</table>' in enhanced_html:
                return enhanced_html
            else:
                logger.warning("LLM response did not contain a valid table")
                return cleaned_table
                
        except Exception as e:
            logger.error(f"Error enhancing table with LLM: {e}")
            return cleaned_table
    
    def process_document_tables(self, document_id: str, content: str, 
                              tables_folder: str = "output/16/preserved_tables",
                              use_llm: bool = True) -> str:
        """
        Process all tables in a document by replacing placeholders with cleaned HTML.
        
        Args:
            document_id: The document ID
            content: Document content with table placeholders
            tables_folder: Path to preserved tables
            use_llm: Whether to use LLM for enhancement
            
        Returns:
            Content with placeholders replaced by HTML tables
        """
        # Load preserved tables
        preserved_tables = self.load_preserved_tables(document_id, tables_folder)
        
        if not preserved_tables:
            return content
        
        # Extract and process tables
        tables = self.extract_tables_from_content(content, preserved_tables)
        
        # Replace placeholders with processed tables
        processed_content = content
        for placeholder, html_table in tables:
            if use_llm and self.openai_client:
                processed_table = self.enhance_table_with_llm(html_table)
            else:
                processed_table = self.clean_html_table(html_table)
            
            processed_content = processed_content.replace(placeholder, processed_table)
        
        # Clean up any standalone closing brackets in paragraph tags
        processed_content = self._clean_standalone_brackets(processed_content)

        return processed_content


def integrate_preserved_tables(json_file_path: str, tables_folder: str = "output/16/preserved_tables",
                             openai_client=None, use_llm: bool = True) -> None:
    """
    Integrate preserved HTML tables into a JSON document structure.
    
    Args:
        json_file_path: Path to the JSON file to update
        tables_folder: Path to the folder containing preserved tables
        openai_client: Optional OpenAI client for enhancement
        use_llm: Whether to use LLM for table enhancement
    """
    # Extract document ID from filename
    document_id = Path(json_file_path).stem
    
    # Initialize processor
    processor = HTMLTableProcessor(openai_client)
    
    # Load the JSON document
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Process articles in the document
    def process_article(article):
        if article.get('type') == 'article':
            content = article.get('article_content', {}).get('content', {})
            main_text_raw = content.get('main_text_raw', '')
            main_text = content.get('main_text', '')

            # Process tables in main_text_raw (original text)
            if '[TABLE_PLACEHOLDER_' in main_text_raw:
                processed_text = processor.process_document_tables(
                    document_id, main_text_raw, tables_folder, use_llm
                )
                content['main_text_raw'] = processed_text
                content['has_preserved_tables'] = True

            # Process tables in main_text (structured HTML content)
            if '[TABLE_PLACEHOLDER_' in main_text:
                processed_html = processor.process_document_tables(
                    document_id, main_text, tables_folder, use_llm
                )
                content['main_text'] = processed_html
                content['has_preserved_tables'] = True

        # Process children recursively
        for child in article.get('children', []):
            process_article(child)
    
    # Process all root nodes
    for root_node in data.get('document_hierarchy', []):
        process_article(root_node)
    
    # Save the updated JSON
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    logger.info(f"Integrated preserved tables into {json_file_path}")


if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
        integrate_preserved_tables(json_file)
    else:
        print("Usage: python table_generation_service_html.py <json_file_path>")