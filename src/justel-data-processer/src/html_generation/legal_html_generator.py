#!/usr/bin/env python3
"""
Belgian Legal Document HTML Generator

This module generates clean, semantic HTML for Belgian legal articles,
replacing the complex JSON structure approach with direct HTML generation.

Author: Augment Agent
Date: 2025-01-23
"""

import re
import os
import logging
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from html import escape as html_escape

def escape(text: str) -> str:
    """Custom HTML escape function that doesn't escape apostrophes.

    Apostrophes don't need to be escaped in HTML content (only in attributes),
    so we avoid converting ' to &#x27; to prevent double-escaping issues.
    """
    if not text:
        return text
    # Use the standard HTML escape but then convert apostrophe entities back
    escaped = html_escape(text)
    # Convert &#x27; back to ' since apostrophes don't need escaping in HTML content
    escaped = escaped.replace('&#x27;', "'")
    return escaped

# Set up logger
logger = logging.getLogger(__name__)

# Import citation parser
try:
    # Try relative import first (when used as module)
    from ..markdown_processing.citation_parser import CitationParser
    CITATION_PARSER_AVAILABLE = True
except ImportError:
    try:
        # Try absolute import (when used directly)
        import sys
        import os
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
        from markdown_processing.citation_parser import CitationParser
        CITATION_PARSER_AVAILABLE = True
    except ImportError:
        CITATION_PARSER_AVAILABLE = False
        logger.warning("Citation parser not available - citations will use basic formatting")

# Import LLM table generation service
try:
    # Try relative import first (when used as module)
    from ..llm_integration import TableGenerationService, TableGenerationConfig, extract_table_from_text
    LLM_AVAILABLE = True
except ImportError:
    try:
        # Try absolute import (when used directly)
        import sys
        import os
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
        from llm_integration import TableGenerationService, TableGenerationConfig, extract_table_from_text
        LLM_AVAILABLE = True
    except ImportError:
        LLM_AVAILABLE = False


class LegalHtmlGenerator:
    """
    Generates semantic HTML for Belgian legal documents.
    
    Converts article content into properly structured HTML with:
    - Semantic markup (article, section, ol, etc.)
    - CSS classes for styling
    - Accessibility features
    - Interactive elements
    """
    
    def __init__(self, api_key: str = None, preserved_tables_dir: str = None):
        """
        Initialize the HTML generator with regex patterns and optional LLM table generation.

        Args:
            api_key: Optional Gemini API key for LLM-based table generation.
                    If not provided, will try to get from environment variable GEMINI_API_KEY.
            preserved_tables_dir: Optional directory containing preserved HTML tables JSON files.
        """
        self.preserved_tables_dir = preserved_tables_dir
        self.preserved_tables_cache = {}
        # Paragraph markers: § 1er., § 2., § 1/1., § 2bis., etc.
        self.paragraph_pattern = re.compile(
            r'§\s*(\d+(?:er|e)?(?:/\d+)?(?:bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?\.)',
            re.IGNORECASE
        )

        # Legal citations: <L date, art. X, Y; En vigueur : date>
        self.citation_pattern = re.compile(r'<([^>]+)>', re.IGNORECASE)

        # Footnote references: [1 content]1, [2 ...]2, etc.
        self.footnote_pattern = re.compile(r'\[(\d+)\s*([^\]]*?)\]\1', re.IGNORECASE)

        # Insertion notes: <Inséré par ...>
        self.insertion_pattern = re.compile(r'<(Inséré par[^>]+)>', re.IGNORECASE)

        # Table detection patterns (fallback for when LLM is not available)
        self.table_pattern = re.compile(r'([^|]*\|[^|]*\|[^|]*)', re.MULTILINE)
        self.table_row_pattern = re.compile(r'([^|]+)')

        # Bilingual table header patterns (Dutch/French)
        self.bilingual_header_pattern = re.compile(r'(Hoven|Cours|Rechtbanken|Tribunaux)', re.IGNORECASE)

        # Initialize LLM table generation service
        self.table_service = None
        if LLM_AVAILABLE:
            # Get API key from parameter or environment
            if not api_key:
                api_key = os.getenv('OPENAI_API_KEY')

            if api_key:
                try:
                    config = TableGenerationConfig(
                        api_key=api_key,
                        enable_generation=True,
                        log_generation_results=False  # Keep logs quiet for HTML generation
                    )
                    self.table_service = TableGenerationService(config)

                    # Test connection
                    if not self.table_service.test_connection():
                        self.table_service = None
                except Exception:
                    self.table_service = None

        # Initialize enhanced citation parser
        self.citation_parser = None
        if CITATION_PARSER_AVAILABLE:
            try:
                self.citation_parser = CitationParser()
                logger.debug("Enhanced citation parser initialized successfully")
            except Exception as e:
                logger.warning(f"Failed to initialize citation parser: {e}")
                self.citation_parser = None
    
    def generate_article_html(self, article_data: Dict[str, Any], document_id: str = None, dossier_number: str = None) -> str:
        """
        Generate article HTML content for a Belgian legal article.

        Args:
            article_data: Article data from JSON with content and metadata
            document_id: Optional document ID for loading preserved tables
            dossier_number: Optional document dossier number for footnote data attributes

        Returns:
            Article HTML content (just the <article> element and its contents) with CSS classes preserved
        """
        # Store document_id for use in nested methods
        if document_id:
            self.current_document_id = document_id

        article_content = article_data.get('article_content', {})
        article_number = article_content.get('article_number', 'Unknown')
        main_text_raw = article_content.get('content', {}).get('main_text_raw', '')
        numbered_provisions = article_content.get('content', {}).get('numbered_provisions', [])

        # Extract footnote data for processing
        footnotes = article_data.get('footnotes', [])
        footnote_references = article_data.get('footnote_references', [])

        # Generate article content with footnote integration
        article_html = self._generate_article_container(
            article_number, main_text_raw, numbered_provisions, footnotes, footnote_references, dossier_number
        )

        # Return just the article content (no full HTML document wrapper)
        # Note: We do NOT clean the main_text field in the JSON - we preserve all original data
        # Table content removal only happens during HTML generation for clean display

        return article_html


    def _generate_article_container(self, article_number: str, main_text_raw: str, numbered_provisions: List[Dict],
                                   footnotes: List[Dict] = None, footnote_references: List[Dict] = None, dossier_number: str = None) -> str:
        """Generate the main article container with all content."""

        article_id = f"art-{article_number.replace('.', '-')}"

        html = f'<article class="legal-article" id="{article_id}">\n'

        # Generate article header
        html += self._generate_article_header(article_number, main_text_raw)

        # Generate article content (paragraphs) with footnote integration
        html += '  <div class="article-content">\n'
        html += self._generate_paragraphs(main_text_raw, numbered_provisions, footnotes, footnote_references, dossier_number)
        html += '  </div>\n'

        html += '</article>'

        return html
    
    def _generate_article_header(self, article_number: str, main_text_raw: str) -> str:
        """Generate the article header with number and metadata."""
        html = '  <header class="article-header">\n'
        html += f'    <h2 class="article-number">Article {article_number}</h2>\n'

        # Extract metadata from the beginning of main_text_raw
        metadata_html = self._extract_and_format_metadata(main_text_raw)
        if metadata_html:
            html += '    <div class="article-metadata">\n'
            html += metadata_html
            html += '    </div>\n'

        html += '  </header>\n'

        return html
    
    def _extract_and_format_metadata(self, main_text_raw: str) -> str:
        """Extract and format article metadata (former article, citations)."""
        html = ''

        # Look for former article reference: (ancien art. X)
        former_match = re.search(r'\(ancien art\. ([^)]+)\)', main_text_raw)
        if former_match:
            html += f'      <span class="former-article">(ancien art. {escape(former_match.group(1))})</span>\n'

        # Extract initial legal citations (before first §) - but only if enhanced citation parser is not available
        # When enhanced citation parser is available, it handles ALL citations in the main content processing,
        # so we skip the old citation processing here to avoid duplication
        if not self.citation_parser:
            first_para_match = self.paragraph_pattern.search(main_text_raw)
            if first_para_match:
                metadata_section = main_text_raw[:first_para_match.start()]
            else:
                metadata_section = main_text_raw[:200]  # First 200 chars if no paragraphs

            citations = self.citation_pattern.findall(metadata_section)
            if citations:
                html += '      <div class="legal-citations">\n'
                for citation in citations:
                    html += f'        <span class="citation">&lt;{escape(citation)}&gt;</span>\n'
                html += '      </div>\n'

        return html

    def _generate_paragraphs_with_processed_footnotes(self, processed_main_text: str, original_main_text: str, numbered_provisions: List[Dict]) -> str:
        """Generate HTML for all paragraphs using text that already has footnote markers processed."""
        html = ''

        # Find all paragraph markers in the ORIGINAL text (for pattern matching)
        all_matches = list(self.paragraph_pattern.finditer(original_main_text))
        paragraph_matches = []

        for match in all_matches:
            # Check the context before this match to see if it's a reference
            start_pos = match.start()
            context_before = original_main_text[max(0, start_pos - 20):start_pos]

            # More specific reference detection:
            # Only skip if it's clearly a reference within an article citation
            is_reference = (
                # After comma AND within article reference
                (context_before.endswith(', ') and ('article' in context_before.lower() or 'art.' in context_before.lower())) or
                # After comma with no space AND within article reference
                (context_before.endswith(',') and ('article' in context_before.lower() or 'art.' in context_before.lower()))
            )

            if not is_reference:
                paragraph_matches.append(match)

        if not paragraph_matches:
            # No paragraphs found, treat as single content block
            # Use the already-parsed numbered provisions from JSON instead of re-parsing
            # This ensures we benefit from the fixed regex pattern in the article extractor
            provisions_in_text = numbered_provisions if numbered_provisions else []
            hyphenated_items = self._find_hyphenated_items_in_paragraph(original_main_text)

            if provisions_in_text or hyphenated_items:
                # Generate content with provisions and/or hyphenated items (footnotes already processed)
                html += '    <div class="article-text">\n'
                html += self._generate_paragraph_with_provisions_and_items_preprocessed(processed_main_text, provisions_in_text, hyphenated_items)
                html += '    </div>\n'
            else:
                # No provisions or items, just plain text (footnotes already processed)
                content = self._clean_and_format_text_with_markers(processed_main_text)
                html += '    <div class="article-text">\n'
                html += f'      <p>{content}</p>\n'
                html += '    </div>\n'
            return html

        # Process each paragraph
        for i, match in enumerate(paragraph_matches):
            paragraph_marker = match.group(1)  # e.g., "1er.", "2.", "2bis."

            # Find paragraph content from ORIGINAL text (for position calculation)
            start_pos = match.start()
            end_pos = paragraph_matches[i + 1].start() if i + 1 < len(paragraph_matches) else len(original_main_text)

            # Extract the corresponding section from PROCESSED text
            processed_paragraph_text = processed_main_text[start_pos:end_pos].strip()
            original_paragraph_text = original_main_text[start_pos:end_pos].strip()

            # Remove the paragraph marker from the beginning
            marker_end = match.end() - match.start()
            processed_paragraph_content = processed_paragraph_text[marker_end:].strip()
            original_paragraph_content = original_paragraph_text[marker_end:].strip()

            # Get provisions that belong to this specific paragraph
            paragraph_provisions = self._get_provisions_for_paragraph(original_main_text, start_pos, end_pos, numbered_provisions)

            # Generate paragraph HTML (footnotes already processed)
            html += self._generate_single_paragraph_with_processed_footnotes(paragraph_marker, processed_paragraph_content, original_paragraph_content, paragraph_provisions)

        return html

    def _get_provisions_for_paragraph(self, main_text_raw: str, paragraph_start: int, paragraph_end: int,
                                     numbered_provisions: List[Dict]) -> List[Dict]:
        """
        Get numbered provisions that belong to a specific paragraph.

        Args:
            main_text_raw: The full article text
            paragraph_start: Start position of the paragraph in the text
            paragraph_end: End position of the paragraph in the text
            numbered_provisions: All numbered provisions for the article

        Returns:
            List of provisions that fall within this paragraph's boundaries
        """
        if not numbered_provisions:
            return []

        paragraph_provisions = []

        for provision in numbered_provisions:
            # Find the position of this provision number in the text
            provision_number = provision['number']
            provision_text = provision['text']

            # Look for the provision number within the paragraph boundaries
            paragraph_text = main_text_raw[paragraph_start:paragraph_end]

            # Check if this provision number appears in this paragraph
            # We need to be careful to match the exact provision pattern
            import re
            provision_pattern = re.compile(rf'\b{re.escape(provision_number)}\s+', re.IGNORECASE)

            # Search for the provision in the paragraph text
            if provision_pattern.search(paragraph_text):
                # Additional check: make sure the provision text also appears in this paragraph
                # This helps avoid false positives where just the number appears
                if provision_text[:20] in paragraph_text:  # Check first 20 chars of provision text
                    paragraph_provisions.append(provision)

        return paragraph_provisions

    def _generate_paragraphs(self, main_text_raw: str, numbered_provisions: List[Dict],
                            footnotes: List[Dict] = None, footnote_references: List[Dict] = None, dossier_number: str = None) -> str:
        """Generate HTML for all paragraphs in the article."""

        html = ''

        # Default to empty lists if not provided
        if footnotes is None:
            footnotes = []
        if footnote_references is None:
            footnote_references = []

        # Find all paragraph markers, but filter out references
        all_matches = list(self.paragraph_pattern.finditer(main_text_raw))
        paragraph_matches = []

        for match in all_matches:
            # Check the context before this match to see if it's a reference
            start_pos = match.start()
            context_before = main_text_raw[max(0, start_pos - 20):start_pos]

            # More specific reference detection:
            # Only skip if it's clearly a reference within an article citation
            is_reference = (
                # After comma AND within article reference
                (context_before.endswith(', ') and ('article' in context_before.lower() or 'art.' in context_before.lower())) or
                # After comma with no space AND within article reference
                (context_before.endswith(',') and ('article' in context_before.lower() or 'art.' in context_before.lower()))
            )

            if not is_reference:
                paragraph_matches.append(match)

        # Process main text content - check for tables and handle them inline
        if not paragraph_matches:
            # No paragraphs found, treat as single content block
            # Check if this content contains tables
            tables_in_content = self._extract_and_clean_tables_from_text(main_text_raw)

            if tables_in_content:
                # Content has tables - process with table handling
                html += self._generate_content_with_inline_tables(main_text_raw, tables_in_content, numbered_provisions, footnotes, footnote_references, dossier_number)
            else:
                # No tables - process normally
                # Use the already-parsed numbered provisions from JSON instead of re-parsing
                provisions_in_text = numbered_provisions if numbered_provisions else []
                hyphenated_items = self._find_hyphenated_items_in_paragraph(main_text_raw)

                html += '    <div class="article-text">\n'

                if provisions_in_text or hyphenated_items:
                    # Generate content with provisions and/or hyphenated items
                    html += self._generate_paragraph_with_provisions_and_items(main_text_raw, provisions_in_text, hyphenated_items, footnotes, footnote_references, dossier_number)
                else:
                    # Check for preserved table placeholders first
                    if '[TABLE_PLACEHOLDER_' in main_text_raw:
                        document_id = getattr(self, 'current_document_id', None)
                        logger.info(f"Found TABLE_PLACEHOLDER in plain text path, document_id: {document_id}")
                        # Use the preserved table method directly
                        table_html = self._generate_paragraph_with_preserved_tables(main_text_raw, footnotes, footnote_references, document_id, dossier_number)
                        html += table_html
                    else:
                        # Just plain text with footnotes
                        content = self._process_footnotes_in_text(main_text_raw, footnotes, footnote_references, dossier_number)
                        html += f'      <p>{content}</p>\n'

                html += '    </div>\n'

            return html

        # Process each paragraph (now with cleaned text)
        for i, match in enumerate(paragraph_matches):
            paragraph_marker = match.group(1)  # e.g., "1er.", "2.", "2bis."

            # Find paragraph content from cleaned text
            start_pos = match.start()
            end_pos = paragraph_matches[i + 1].start() if i + 1 < len(paragraph_matches) else len(main_text_raw)

            paragraph_text = main_text_raw[start_pos:end_pos].strip()

            # Remove the paragraph marker from the beginning
            marker_end = match.end() - match.start()
            paragraph_content = paragraph_text[marker_end:].strip()

            # Get provisions that belong to this specific paragraph
            paragraph_provisions = self._get_provisions_for_paragraph(main_text_raw, start_pos, end_pos, numbered_provisions)

            # Generate paragraph HTML
            html += self._generate_single_paragraph(paragraph_marker, paragraph_content, paragraph_provisions, footnotes, footnote_references, dossier_number)
        
        return html

    def _generate_single_paragraph_with_processed_footnotes(self, marker: str, processed_content: str, original_content: str, numbered_provisions: List[Dict]) -> str:
        """Generate HTML for a single paragraph where footnotes have already been processed."""
        # Create paragraph ID
        para_id = f"para-{marker.replace('.', '').replace('/', '-')}"

        html = f'    <section class="paragraph" id="{para_id}">\n'
        html += f'      <h3 class="paragraph-marker">§ {marker}</h3>\n'
        html += '      <div class="paragraph-content">\n'

        # Check if this paragraph contains tables, numbered provisions, or hyphenated items
        tables = self._detect_tables_in_text(original_content)
        # The numbered_provisions passed here should already be filtered for this paragraph
        paragraph_provisions = numbered_provisions if numbered_provisions else []
        hyphenated_items = self._find_hyphenated_items_in_paragraph(original_content)

        if tables:
            html += self._generate_paragraph_with_tables_preprocessed(processed_content, tables)
        elif paragraph_provisions or hyphenated_items:
            html += self._generate_paragraph_with_provisions_and_items_preprocessed(processed_content, paragraph_provisions, hyphenated_items)
        else:
            html += self._generate_simple_paragraph_preprocessed(processed_content)

        html += '      </div>\n'
        html += '    </section>\n'

        return html

    def _generate_paragraph_with_provisions_and_items_preprocessed(self, processed_content: str, provisions: List[Dict], hyphenated_items: List[Dict]) -> str:
        """Generate HTML for a paragraph with provisions/items where footnotes have already been processed."""
        # For now, use a simplified approach that preserves footnote markers
        html = ''

        # If we have provisions, try to split the content around them
        if provisions:
            # Find intro text (text before first provision)
            if provisions:
                first_provision_text = provisions[0]['text']
                # Look for this provision text in the processed content
                provision_start = processed_content.find(first_provision_text)
                if provision_start > 0:
                    intro_text = processed_content[:provision_start].strip()
                    # Clean up intro text (remove trailing provision markers)
                    intro_text = re.sub(r'\s*\d+°\s*$', '', intro_text)
                    if intro_text:
                        intro_text = self._clean_and_format_text_with_markers(intro_text + ':')
                        html += f'        <p class="intro-text">{intro_text}</p>\n'

            # Generate provisions list
            html += '        <ol class="numbered-provisions">\n'
            for provision in provisions:
                number = provision['number']
                text = provision['text']

                # Find the provision text in the processed content (which may have footnote markers)
                text_start = processed_content.find(text)
                if text_start != -1:
                    # Extract the text with any footnote markers
                    text_end = text_start + len(text)
                    actual_text = processed_content[text_start:text_end]
                    formatted_text = self._clean_and_format_text_with_markers(actual_text)
                else:
                    # Fallback to original text
                    formatted_text = self._clean_and_format_text_with_markers(text)

                html += f'          <li class="provision" data-number="{escape(number)}">\n'
                html += f'            <span class="provision-text">{formatted_text}</span>\n'
                html += '          </li>\n'
            html += '        </ol>\n'

            # Find closing text (text after last provision)
            if provisions:
                last_provision_text = provisions[-1]['text']
                provision_end = processed_content.rfind(last_provision_text)
                if provision_end != -1:
                    provision_end += len(last_provision_text)
                    closing_text = processed_content[provision_end:].strip()
                    if closing_text:
                        closing_text = self._clean_and_format_text_with_markers(closing_text)
                        html += f'        <p class="closing-text">{closing_text}</p>\n'

        # Handle hyphenated items if present
        if hyphenated_items:
            html += '        <ul class="hyphenated-items">\n'
            for item in hyphenated_items:
                item_text = item['text']
                # Find the item text in the processed content
                text_start = processed_content.find(item_text)
                if text_start != -1:
                    text_end = text_start + len(item_text)
                    actual_text = processed_content[text_start:text_end]
                    formatted_text = self._clean_and_format_text_with_markers(actual_text)
                else:
                    formatted_text = self._clean_and_format_text_with_markers(item_text)

                html += '          <li class="hyphenated-item">\n'
                html += f'            <span class="item-text">{formatted_text}</span>\n'
                html += '          </li>\n'
            html += '        </ul>\n'

        return html

    def _generate_single_paragraph_preprocessed(self, marker: str, content: str, numbered_provisions: List[Dict]) -> str:
        """Generate HTML for a single paragraph where footnotes have already been processed."""
        # Create paragraph ID
        para_id = f"para-{marker.replace('.', '').replace('/', '-')}"

        html = f'    <section class="paragraph" id="{para_id}">\n'
        html += f'      <h3 class="paragraph-marker">§ {marker}</h3>\n'
        html += '      <div class="paragraph-content">\n'

        # Check if this paragraph contains numbered provisions or hyphenated items (use original patterns)
        # We need to extract the original text for pattern matching
        original_content = self._extract_original_text_from_processed(content)
        # Use the already-parsed numbered provisions from JSON instead of re-parsing
        paragraph_provisions = numbered_provisions if numbered_provisions else []
        hyphenated_items = self._find_hyphenated_items_in_paragraph(original_content)

        if paragraph_provisions or hyphenated_items:
            html += self._generate_paragraph_with_provisions_and_items_preprocessed(content, paragraph_provisions, hyphenated_items)
        else:
            html += self._generate_simple_paragraph_preprocessed(content)

        html += '      </div>\n'
        html += '    </section>\n'

        return html

    def _extract_original_text_from_processed(self, processed_text: str) -> str:
        """Extract original text from processed text by removing footnote markers."""
        import re
        # Remove footnote markers but keep the text content
        footnote_pattern = re.compile(r'<span class="footnote-ref"[^>]*>(.*?)</span>', re.DOTALL)
        original_text = footnote_pattern.sub(r'\1', processed_text)
        return original_text

    def _generate_simple_paragraph_preprocessed(self, content: str) -> str:
        """Generate HTML for a simple paragraph where footnotes have already been processed."""
        # Check for preserved table placeholders first
        if '[TABLE_PLACEHOLDER_' in content:
            document_id = getattr(self, 'current_document_id', None)
            logger.info(f"🔍 Found TABLE_PLACEHOLDER in _generate_simple_paragraph_preprocessed, document_id: {document_id}")
            return self._generate_paragraph_with_preserved_tables(content, [], [], document_id)

        # Content already has footnote markers, just clean and format
        formatted_content = self._clean_and_format_text_with_markers(content)
        return f'        <p>{formatted_content}</p>\n'

    def _generate_paragraph_with_provisions_and_items_preprocessed(self, content: str, provisions: List[Dict], hyphenated_items: List[Dict]) -> str:
        """Generate HTML for a paragraph with provisions/items where footnotes have already been processed."""
        # Check for preserved table placeholders first
        if '[TABLE_PLACEHOLDER_' in content:
            document_id = getattr(self, 'current_document_id', None)
            logger.info(f"🔍 Found TABLE_PLACEHOLDER in _generate_paragraph_with_provisions_and_items_preprocessed, document_id: {document_id}")
            return self._generate_paragraph_with_preserved_tables(content, [], [], document_id)

        # If we only have provisions, use the existing logic
        if provisions and not hyphenated_items:
            return self._generate_paragraph_with_provisions_preprocessed(content, provisions)

        # If we only have hyphenated items, use bullet point logic
        if hyphenated_items and not provisions:
            return self._generate_paragraph_with_hyphenated_items_preprocessed(content, hyphenated_items)

        # If we have both, we need to handle them together
        if provisions and hyphenated_items:
            return self._generate_paragraph_with_mixed_items_preprocessed(content, provisions, hyphenated_items)

        # Fallback to simple paragraph
        return self._generate_simple_paragraph_preprocessed(content)

    def _generate_single_paragraph(self, marker: str, content: str, numbered_provisions: List[Dict],
                                  footnotes: List[Dict] = None, footnote_references: List[Dict] = None, dossier_number: str = None) -> str:
        """Generate HTML for a single paragraph."""

        # Create paragraph ID
        para_id = f"para-{marker.replace('.', '').replace('/', '-')}"

        html = f'    <section class="paragraph" id="{para_id}">\n'
        html += f'      <h3 class="paragraph-marker">§ {marker}</h3>\n'
        html += '      <div class="paragraph-content">\n'

        # Default to empty lists if not provided
        if footnotes is None:
            footnotes = []
        if footnote_references is None:
            footnote_references = []

        # Check if this paragraph contains tables, numbered provisions, or hyphenated items
        tables_in_paragraph = self._extract_and_clean_tables_from_text(content)

        if tables_in_paragraph:
            # This paragraph contains tables - generate tables first, then clean content
            table_html = ''
            for table in tables_in_paragraph:
                table_html += self._generate_standalone_table_section(table)

            # Now clean the content for normal paragraph processing
            cleaned_content = self._remove_table_content_from_text(content, tables_in_paragraph)
            # Use the already-parsed numbered provisions from JSON instead of re-parsing
            paragraph_provisions = numbered_provisions if numbered_provisions else []
            hyphenated_items = self._find_hyphenated_items_in_paragraph(cleaned_content)

            # Process the cleaned content first
            if paragraph_provisions or hyphenated_items:
                html += self._generate_paragraph_with_provisions_and_items(cleaned_content, paragraph_provisions, hyphenated_items, footnotes, footnote_references, dossier_number)
            else:
                processed_content = self._process_footnotes_in_text(cleaned_content, footnotes, footnote_references, dossier_number)
                html += f'        <p>{processed_content}</p>\n'

            # Close the paragraph content div
            html += '      </div>\n'
            html += '    </section>\n'

            # Add tables after the paragraph
            html += table_html

            return html
        else:
            # No tables - process normally
            # Use the already-parsed numbered provisions from JSON instead of re-parsing
            paragraph_provisions = numbered_provisions if numbered_provisions else []
            hyphenated_items = self._find_hyphenated_items_in_paragraph(content)

        if paragraph_provisions or hyphenated_items:
            html += self._generate_paragraph_with_provisions_and_items(content, paragraph_provisions, hyphenated_items, footnotes, footnote_references, dossier_number)
        else:
            html += self._generate_simple_paragraph(content, footnotes, footnote_references, dossier_number)
        
        html += '      </div>\n'
        html += '    </section>\n'
        
        return html

    def _generate_content_with_inline_tables(self, text: str, tables: List[str], numbered_provisions: List[Dict], footnotes: List[Dict], footnote_references: List[Dict], dossier_number: str = None) -> str:
        """
        Generate content with tables placed inline at their natural position.
        """
        html = ''

        # Remove table content from text for clean processing
        cleaned_text = self._remove_table_content_from_text(text, tables)

        # Process the cleaned text normally
        # Use the already-parsed numbered provisions from JSON instead of re-parsing
        provisions_in_text = numbered_provisions if numbered_provisions else []
        hyphenated_items = self._find_hyphenated_items_in_paragraph(cleaned_text)

        html += '    <div class="article-text">\n'

        if provisions_in_text or hyphenated_items:
            # Generate content with provisions and/or hyphenated items
            html += self._generate_paragraph_with_provisions_and_items(cleaned_text, provisions_in_text, hyphenated_items, footnotes, footnote_references, dossier_number)
        else:
            # Just plain text with footnotes
            content = self._process_footnotes_in_text(cleaned_text, footnotes, footnote_references, dossier_number)
            html += f'      <p>{content}</p>\n'

        html += '    </div>\n'

        # Add tables after the text content
        for table in tables:
            html += self._generate_standalone_table_section(table)

        return html

    def _extract_and_clean_tables_from_text(self, text: str) -> List[str]:
        """
        Extract all tables from text and return them as clean table strings.
        This is the simplified approach - extract tables first, process separately.
        """
        if LLM_AVAILABLE:
            # Use enhanced table detection from LLM integration
            table_texts = extract_table_from_text(text)

            # Table detection completed

            return table_texts

        # Fallback to basic detection
        tables = self._detect_tables_in_text(text)
        table_texts = []
        for table in tables:
            # Convert table dict back to text format
            if 'rows' in table:
                table_lines = []
                for row in table['rows']:
                    if 'cells' in row:
                        table_lines.append(' | '.join(row['cells']))
                if table_lines:
                    table_texts.append('\n'.join(table_lines))

        return table_texts

    def _remove_table_content_from_text(self, text: str, tables: List[str]) -> str:
        """
        Remove all table content from the text, leaving clean text for normal processing.
        """
        if not tables:
            return text

        cleaned_text = text

        # More aggressive approach: remove everything from "tableau ci-dessous" to the next paragraph
        tableau_text = "tableau ci-dessous."

        if tableau_text in cleaned_text:
            # Find the start of the table reference
            tableau_pos = cleaned_text.find(tableau_text)

            # Keep text up to and including "tableau ci-dessous."
            before_table = cleaned_text[:tableau_pos + len(tableau_text)]

            # Find the end by looking for the next paragraph marker
            end_markers = ['§ 2', '§ 3', '§ 4', '§ 5']
            end_pos = len(cleaned_text)

            for end_marker in end_markers:
                marker_pos = cleaned_text.find(end_marker, tableau_pos)
                if marker_pos != -1:
                    end_pos = marker_pos
                    break

            # Get text after the table
            after_table = cleaned_text[end_pos:]

            # Combine before and after, removing the table
            cleaned_text = before_table + " " + after_table
        else:
            # Fallback: look for table indicators
            table_indicators = ['Hoven', 'Cours', 'Rechtbanken', 'Tribunaux']

            for indicator in table_indicators:
                if indicator in cleaned_text:
                    # Find the start of the table
                    start_pos = cleaned_text.find(indicator)
                    if start_pos != -1:
                        # Find the end by looking for the next paragraph marker
                        end_markers = ['§ 2', '§ 3', '§ 4', '§ 5']
                        end_pos = len(cleaned_text)

                        for end_marker in end_markers:
                            marker_pos = cleaned_text.find(end_marker, start_pos)
                            if marker_pos != -1:
                                end_pos = marker_pos
                                break

                        # Remove the table section
                        before_table = cleaned_text[:start_pos]
                        after_table = cleaned_text[end_pos:]

                        cleaned_text = before_table + " " + after_table
                        break

        # Clean up extra whitespace and normalize
        cleaned_text = ' '.join(cleaned_text.split())

        return cleaned_text

    def _generate_standalone_table_section(self, table_text: str) -> str:
        """
        Generate a standalone table section with proper section separators.
        """
        # Check if table has section separators
        if 'SECTION_SEPARATOR' in table_text:
            return self._generate_table_with_sections(table_text)

        # Try LLM-based table generation first
        if self.table_service and LLM_AVAILABLE:
            table_html = self.table_service.generate_table_html(table_text)
            if table_html:
                # Just wrap the LLM output in a container - that's it!
                html = '    <section class="table-section">\n'
                html += '      <div class="table-container">\n'
                html += f'        {table_html}\n'
                html += '      </div>\n'
                html += '    </section>\n'
                return html

        # If LLM fails, return empty (no fallback complexity)
        return ''

    def _generate_table_with_sections(self, table_text: str) -> str:
        """
        Generate table with proper section separators and visual breaks.
        """
        lines = table_text.split('\n')
        sections = []
        current_section = []

        for line in lines:
            if line == 'SECTION_SEPARATOR':
                # End current section and start new one
                if current_section:
                    sections.append('\n'.join(current_section))
                    current_section = []
            else:
                current_section.append(line)

        # Don't forget the last section
        if current_section:
            sections.append('\n'.join(current_section))

        # Generate HTML for each section
        html = '    <section class="table-section">\n'

        for i, section in enumerate(sections):
            if i > 0:
                # Add visual separator between sections
                html += '      <div class="table-section-separator"></div>\n'

            html += '      <div class="table-container">\n'

            # Generate table HTML for this section
            if self.table_service and LLM_AVAILABLE:
                table_html = self.table_service.generate_table_html(section)
                if table_html:
                    html += f'        {table_html}\n'
                else:
                    # Fallback to simple table
                    html += self._generate_simple_table_html(section)
            else:
                html += self._generate_simple_table_html(section)

            html += '      </div>\n'

        html += '    </section>\n'
        return html

    def _generate_simple_table_html(self, table_text: str) -> str:
        """
        Generate simple HTML table as fallback.
        """
        lines = [line.strip() for line in table_text.split('\n') if line.strip()]
        if not lines:
            return ''

        html = '<table class="legal-table">\n'

        # First line as header
        if lines:
            header_cells = [cell.strip() for cell in lines[0].split('|')]
            html += '  <thead>\n    <tr>\n'
            for cell in header_cells:
                if cell:
                    html += f'      <th scope="col">{escape(cell)}</th>\n'
            html += '    </tr>\n  </thead>\n'

        # Remaining lines as body
        if len(lines) > 1:
            html += '  <tbody>\n'
            for line in lines[1:]:
                cells = [cell.strip() for cell in line.split('|')]
                html += '    <tr>\n'
                for cell in cells:
                    if cell:
                        html += f'      <td>{escape(cell)}</td>\n'
                html += '    </tr>\n'
            html += '  </tbody>\n'

        html += '</table>\n'
        return html

    def _detect_tables_in_text(self, text: str) -> List[Dict]:
        """Detect and extract table structures from text using enhanced detection."""
        tables = []

        # Use the enhanced table detection from LLM integration
        if LLM_AVAILABLE:
            table_texts = extract_table_from_text(text)
            for table_text in table_texts:
                # Convert to the format expected by the HTML generator
                lines = table_text.split('\n')
                table_data = self._parse_table_structure(lines)
                if table_data:
                    tables.append(table_data)

            if tables:
                return tables

        # Fallback to original detection method
        lines = text.split('\n')
        table_lines = []
        in_table = False

        for line in lines:
            line = line.strip()
            if not line:
                if in_table and table_lines:
                    # End of table
                    table_data = self._parse_table_structure(table_lines)
                    if table_data:
                        tables.append(table_data)
                    table_lines = []
                    in_table = False
                continue

            # Check if line contains table separators (|) - need at least 3 pipes for a valid table
            if '|' in line and line.count('|') >= 3:
                table_lines.append(line)
                in_table = True
            else:
                if in_table and table_lines:
                    # End of table
                    table_data = self._parse_table_structure(table_lines)
                    if table_data:
                        tables.append(table_data)
                    table_lines = []
                    in_table = False

        # Handle table at end of text
        if in_table and table_lines:
            table_data = self._parse_table_structure(table_lines)
            if table_data:
                tables.append(table_data)

        return tables

    def _parse_table_structure(self, table_lines: List[str]) -> Dict:
        """Parse table structure from pipe-separated lines."""
        if not table_lines:
            return None

        # Clean and split each line
        rows = []
        for line in table_lines:
            # Split by pipe and clean each cell
            cells = [cell.strip() for cell in line.split('|')]
            # Remove empty cells at start/end only
            while cells and not cells[0]:
                cells.pop(0)
            while cells and not cells[-1]:
                cells.pop()

            if cells:  # Only add non-empty rows
                rows.append(cells)

        if not rows:
            return None

        # Detect if this is a bilingual table (Dutch/French)
        is_bilingual = self._is_bilingual_table(rows)

        return {
            'type': 'table',
            'rows': rows,
            'is_bilingual': is_bilingual,
            'column_count': max(len(row) for row in rows) if rows else 0
        }

    def _is_bilingual_table(self, rows: List[List[str]]) -> bool:
        """Determine if table is bilingual (Dutch/French)."""
        if not rows:
            return False

        # Check first few rows for bilingual indicators
        for row in rows[:3]:  # Check first 3 rows
            for cell in row:
                if self.bilingual_header_pattern.search(cell):
                    return True

        return False

    def _generate_table_html(self, table_data: Dict, footnotes: List[Dict] = None, footnote_references: List[Dict] = None) -> str:
        """Generate HTML for a table structure."""
        if not table_data or not table_data.get('rows'):
            return ''

        rows = table_data['rows']
        is_bilingual = table_data.get('is_bilingual', False)

        html = ''

        if is_bilingual:
            html += self._generate_bilingual_table_html(rows, footnotes, footnote_references)
        else:
            html += self._generate_standard_table_html(rows, footnotes, footnote_references)

        return html

    def _generate_bilingual_table_html(self, rows: List[List[str]], footnotes: List[Dict] = None, footnote_references: List[Dict] = None) -> str:
        """Generate HTML for bilingual (Dutch/French) tables."""
        if not rows:
            return ''

        html = '<div class="table-container">\n'
        html += '  <table class="legal-table bilingual-table">\n'

        # Process header rows
        header_rows = []
        data_rows = []

        # Identify header vs data rows
        for i, row in enumerate(rows):
            # First few rows are likely headers if they contain text like "Hoven", "Cours", etc.
            is_header = (i < 2 and any(self.bilingual_header_pattern.search(cell) for cell in row))
            if is_header:  # Only rows with bilingual indicators are headers
                header_rows.append(row)
            else:
                data_rows.append(row)

        # Generate table header
        if header_rows:
            html += '    <thead>\n'
            for i, row in enumerate(header_rows):
                html += '      <tr class="'
                if i == 0:
                    html += 'main-header'
                else:
                    html += 'sub-header'
                html += '">\n'

                for cell in row:
                    processed_cell = self._process_table_cell_content(cell, footnotes, footnote_references)
                    html += f'        <th>{processed_cell}</th>\n'

                html += '      </tr>\n'
            html += '    </thead>\n'

        # Generate table body
        if data_rows:
            html += '    <tbody>\n'
            for row in data_rows:
                html += '      <tr>\n'
                for cell in row:
                    processed_cell = self._process_table_cell_content(cell, footnotes, footnote_references)
                    html += f'        <td>{processed_cell}</td>\n'
                html += '      </tr>\n'
            html += '    </tbody>\n'

        html += '  </table>\n'
        html += '</div>\n'

        return html

    def _generate_standard_table_html(self, rows: List[List[str]], footnotes: List[Dict] = None, footnote_references: List[Dict] = None) -> str:
        """Generate HTML for standard tables."""
        if not rows:
            return ''

        html = '<div class="table-container">\n'
        html += '  <table class="legal-table">\n'

        # First row as header
        if rows:
            html += '    <thead>\n'
            html += '      <tr>\n'
            for cell in rows[0]:
                processed_cell = self._process_table_cell_content(cell, footnotes, footnote_references)
                html += f'        <th>{processed_cell}</th>\n'
            html += '      </tr>\n'
            html += '    </thead>\n'

        # Remaining rows as data
        if len(rows) > 1:
            html += '    <tbody>\n'
            for row in rows[1:]:
                html += '      <tr>\n'
                for cell in row:
                    processed_cell = self._process_table_cell_content(cell, footnotes, footnote_references)
                    html += f'        <td>{processed_cell}</td>\n'
                html += '      </tr>\n'
            html += '    </tbody>\n'

        html += '  </table>\n'
        html += '</div>\n'

        return html

    def _process_table_cell_content(self, cell: str, footnotes: List[Dict] = None, footnote_references: List[Dict] = None, dossier_number: str = None) -> str:
        """Process table cell content, including footnotes."""
        if not cell:
            return ''

        # Clean the cell content
        cell = cell.strip()

        # Process footnotes if available
        if footnotes and footnote_references:
            cell = self._process_footnotes_in_text(cell, footnotes, footnote_references, dossier_number)

        # If no footnotes were processed, clean and format the text
        if not (footnotes and footnote_references):
            cell = self._clean_and_format_text_with_markers(cell)

        return cell

    def _generate_paragraph_with_tables_preprocessed(self, content: str, tables: List[Dict]) -> str:
        """Generate HTML for a paragraph containing tables where footnotes have already been processed."""
        html = ''

        # Split content around tables
        remaining_content = content

        # Remove table content from text and replace with table HTML
        for table in tables:
            # Generate the table HTML
            table_html = self._generate_table_html(table)
            html += table_html

            # Remove table rows from remaining content
            if table.get('rows'):
                for row in table['rows']:
                    # Create pattern to match this table row
                    row_pattern = '|'.join([re.escape(cell.strip()) for cell in row])
                    remaining_content = re.sub(row_pattern, '', remaining_content)

        # Clean up remaining content
        if remaining_content and remaining_content.strip():
            # Remove any remaining pipe separators and clean up
            text_content = remaining_content
            # Remove lines that are mostly pipe characters
            lines = text_content.split('\n')
            clean_lines = []
            for line in lines:
                line = line.strip()
                # Skip lines that are mostly pipes or empty
                if line and line.count('|') < len(line) * 0.3:  # Less than 30% pipes
                    clean_lines.append(line)

            text_content = '\n'.join(clean_lines).strip()

            if text_content:
                html += f'        <p>{text_content}</p>\n'

        return html

    def _generate_paragraph_with_tables(self, content: str, tables: List[Dict], footnotes: List[Dict] = None, footnote_references: List[Dict] = None, dossier_number: str = None) -> str:
        """Generate HTML for a paragraph containing tables."""
        # Check for preserved table placeholders first
        if '[TABLE_PLACEHOLDER_' in content:
            document_id = getattr(self, 'current_document_id', None)
            logger.info(f"🔍 Found TABLE_PLACEHOLDER in _generate_paragraph_with_tables, document_id: {document_id}")
            return self._generate_paragraph_with_preserved_tables(content, footnotes, footnote_references, document_id, dossier_number)

        html = ''

        # Split content around tables
        remaining_content = content

        # Remove table content from text and replace with table HTML
        for table in tables:
            # Generate the table HTML with footnote processing
            table_html = self._generate_table_html(table, footnotes, footnote_references)
            html += table_html

            # Remove table rows from remaining content
            if table.get('rows'):
                for row in table['rows']:
                    # Create pattern to match this table row
                    row_pattern = '|'.join([re.escape(cell.strip()) for cell in row])
                    remaining_content = re.sub(row_pattern, '', remaining_content)

        # Clean up remaining content
        if remaining_content and remaining_content.strip():
            # Remove any remaining pipe separators and clean up
            text_content = remaining_content
            # Remove lines that are mostly pipe characters
            lines = text_content.split('\n')
            clean_lines = []
            for line in lines:
                line = line.strip()
                # Skip lines that are mostly pipes or empty
                if line and line.count('|') < len(line) * 0.3:  # Less than 30% pipes
                    clean_lines.append(line)

            text_content = '\n'.join(clean_lines).strip()

            if text_content:
                # Process footnotes in the remaining text
                if footnotes and footnote_references:
                    text_content = self._process_footnotes_in_text(text_content, footnotes, footnote_references, dossier_number)
                else:
                    text_content = self._clean_and_format_text(text_content)
                html += f'        <p>{text_content}</p>\n'

        return html

    def load_preserved_tables(self, document_id: str) -> Dict[str, str]:
        """
        Load preserved HTML tables for a document.
        
        Args:
            document_id: The document ID (filename without extension)
            
        Returns:
            Dictionary mapping table placeholders to HTML content
        """
        if not self.preserved_tables_dir:
            return {}
            
        # Check cache first
        if document_id in self.preserved_tables_cache:
            return self.preserved_tables_cache[document_id]
        
        # Load from file
        tables_file = Path(self.preserved_tables_dir) / f"{document_id}_tables.json"
        if not tables_file.exists():
            logger.info(f"No preserved tables found for document: {document_id}")
            return {}
        
        try:
            with open(tables_file, 'r', encoding='utf-8') as f:
                tables = json.load(f)
                self.preserved_tables_cache[document_id] = tables
                logger.info(f"Loaded {len(tables)} preserved tables for document: {document_id}")
                return tables
        except Exception as e:
            logger.error(f"Error loading preserved tables for {document_id}: {e}")
            return {}
    
    def _clean_preserved_table(self, html_table: str) -> str:
        """
        Clean and enhance a preserved HTML table.
        
        Args:
            html_table: Raw HTML table string
            
        Returns:
            Cleaned HTML table
        """
        # Basic cleaning - ensure proper CSS class
        if 'class=' not in html_table:
            html_table = html_table.replace('<table', '<table class="legal-table"')
        
        # Remove any border attributes (will be handled by CSS)
        html_table = re.sub(r'\s*border="[^"]*"', '', html_table)
        
        # Fix thead tags that might be corrupted
        html_table = re.sub(r'<th[^>]*ead>', '<thead>', html_table)
        
        # Ensure scope on headers only if not already present
        def add_scope(match):
            th_tag = match.group(0)
            if 'scope=' not in th_tag:
                return th_tag[:-1] + ' scope="col">'
            return th_tag
        
        html_table = re.sub(r'<th[^>]*>', add_scope, html_table)
        
        return html_table
    
    def _generate_paragraph_with_preserved_tables(self, content: str, footnotes: List[Dict] = None,
                                                footnote_references: List[Dict] = None,
                                                document_id: str = None, dossier_number: str = None) -> str:
        """Generate HTML for a paragraph containing preserved HTML table placeholders."""
        html = ''
        
        # Load preserved tables if document_id is provided
        preserved_tables = {}
        if document_id:
            preserved_tables = self.load_preserved_tables(document_id)
            logger.info(f"🔍 Loaded {len(preserved_tables)} preserved tables for document_id: {document_id}")
        else:
            logger.warning(f"🔍 No document_id provided to _generate_paragraph_with_preserved_tables")
        
        # Split content by table placeholders
        parts = re.split(r'(\[TABLE_PLACEHOLDER_\d{4}\])', content)
        
        for i, part in enumerate(parts):
            part = part.strip()
            if not part:
                continue
                
            # Check if this is a table placeholder
            if part.startswith('[TABLE_PLACEHOLDER_') and part.endswith(']'):
                # Extract the placeholder ID
                placeholder = part.strip('[]')
                
                if placeholder in preserved_tables:
                    # Get the preserved table HTML
                    table_html = preserved_tables[placeholder]
                    
                    # Clean the table
                    table_html = self._clean_preserved_table(table_html)
                    
                    # Add separator between tables
                    if i > 0 and html.strip().endswith('</div>'):
                        html += '<div class="table-section-separator"></div>\n'
                    
                    # Wrap in table container
                    html += '<div class="table-container">\n'
                    html += f'  {table_html}\n'
                    html += '</div>\n'
                    
                    logger.info(f"Replaced placeholder {placeholder} with preserved table")
                else:
                    # Placeholder not found in preserved tables
                    logger.warning(f"Preserved table not found for placeholder: {placeholder}")
                    html += f'<div class="missing-table-placeholder">{part}</div>\n'
            else:
                # This is regular text content
                if footnotes and footnote_references:
                    processed_text = self._process_footnotes_in_text(part, footnotes, footnote_references, dossier_number)
                else:
                    processed_text = self._clean_and_format_text(part)
                
                if processed_text.strip():
                    html += f'        <p>{processed_text}</p>\n'
        
        return html

    def _generate_paragraph_with_tables_llm(self, content: str, tables: List[Dict], footnotes: List[Dict] = None, footnote_references: List[Dict] = None, dossier_number: str = None) -> str:
        """Generate HTML for a paragraph containing tables using LLM service."""
        html = ''

        # Debug: Log content being processed
        logger.info(f"🔍 _generate_paragraph_with_tables_llm called with content length: {len(content)}")
        if "Hoven" in content or "Cours" in content:
            logger.info(f"📊 Content contains table indicators (Hoven/Cours)")
            logger.info(f"📝 Content preview: {content[:300]}...")

        # Check for preserved HTML table placeholders first
        if '[TABLE_PLACEHOLDER_' in content:
            logger.info("📊 Found preserved table placeholders")
            # Extract document_id from the current context if available
            document_id = getattr(self, 'current_document_id', None)
            logger.debug(f"Found TABLE_PLACEHOLDER in _generate_paragraph_with_tables_llm, document_id: {document_id}")
            return self._generate_paragraph_with_preserved_tables(content, footnotes, footnote_references, document_id, dossier_number)

        # Try LLM-based table generation first
        if self.table_service and LLM_AVAILABLE:
            # Extract table text from content
            table_texts = extract_table_from_text(content)  # Returns list of strings
            logger.info(f"🔍 Table extraction found {len(table_texts)} tables in content (length: {len(content)})")
            if table_texts:
                logger.info(f"📊 Processing {len(table_texts)} tables with OpenAI")
                # Process ALL tables found, not just the first one
                remaining_content = content
                for i, table_text in enumerate(table_texts):
                    logger.info(f"🔧 Processing table {i+1}/{len(table_texts)} (length: {len(table_text)})")
                    # Generate HTML table using LLM
                    table_html = self.table_service.generate_table_html(table_text)
                    if table_html:
                        logger.info(f"✅ Successfully generated HTML for table {i+1}")
                        # Add separator between tables if there are multiple
                        if i > 0:
                            html += '<div class="table-section-separator"></div>\n'

                        # Wrap in table container
                        html += '<div class="table-container">\n'
                        html += f'  {table_html}\n'
                        html += '</div>\n'

                        # Remove table content from remaining text
                        for line in table_text.split('\n'):
                            remaining_content = remaining_content.replace(line, '')
                    else:
                        logger.warning(f"❌ Failed to generate HTML for table {i+1}")
            else:
                logger.info("ℹ️ No tables found in content")

            # Clean up remaining content
            remaining_content = remaining_content.strip()
            if remaining_content:
                # Process footnotes in the remaining text
                if footnotes and footnote_references:
                    remaining_content = self._process_footnotes_in_text(remaining_content, footnotes, footnote_references, dossier_number)
                else:
                    remaining_content = self._clean_and_format_text(remaining_content)
                html += f'        <p>{remaining_content}</p>\n'

            return html

        # Fallback to regex-based table generation
        return self._generate_paragraph_with_tables(content, tables, footnotes, footnote_references, dossier_number)

    def _find_provisions_in_paragraph(self, content: str, numbered_provisions: List[Dict]) -> List[Dict]:
        """Find which numbered provisions appear in this specific paragraph by parsing directly from text."""
        provisions_in_paragraph = []

        # Simple heuristic: Only treat as provisions if there's a colon or semicolon in the content
        # This catches most real provision cases while avoiding references
        # Provisions can come after colons (:) or semicolons (;)
        if ':' not in content and ';' not in content:
            return provisions_in_paragraph

        try:
            # Split on provision markers, but avoid citations
            # Use context-aware splitting to distinguish between provision markers and references
            parts = self._smart_split_provisions(content)

            # Safety check - need at least a number and content
            if len(parts) < 2:
                return provisions_in_paragraph

            # Process the parts: [prefix, number1, content1, number2, content2, ...]
            # OR [number1, content1, number2, content2, ...] if provisions start at beginning

            # Determine if we have a prefix or if provisions start immediately
            has_prefix = len(parts) > 0 and not re.match(r'\d+°', parts[0].strip())
            i = 1 if has_prefix else 0  # Skip the prefix part if it exists
            max_iterations = 20  # Safety limit
            iteration_count = 0

            while i < len(parts) - 1 and iteration_count < max_iterations:
                iteration_count += 1

                number = parts[i].strip()
                text = parts[i + 1].strip()

                # Simple check: skip if the prefix ends with common reference words or citation patterns
                prefix = parts[i - 1] if (has_prefix and i > 1) or (not has_prefix and i > 0) else ""

                # Enhanced citation detection: skip if this looks like a citation or reference
                is_citation = (
                    # Common citation patterns in text
                    'En vigueur' in text or
                    # Date patterns in text (YYYY-MM-DD)
                    re.search(r'\d{4}-\d{2}-\d{2}', text) or
                    # Reference patterns in prefix - be more specific
                    (prefix.endswith(', ') and ('art.' in prefix.lower() or 'article' in prefix.lower())) or
                    prefix.endswith(' et ') or
                    # Specific citation context: comma followed by art.
                    (', art.' in prefix.lower() and len(prefix) < 50) or
                    # Paragraph references: "au § X, Y°" pattern
                    re.search(r'au\s+§\s+\d+,\s*$', prefix) or
                    # Other reference patterns
                    prefix.endswith(' au ') or
                    prefix.endswith(' du ')
                )

                if is_citation:
                    i += 2
                    continue  # Skip this, it's likely a citation

                # Clean up text - remove leading separators
                text = text.lstrip(':; \t\n\r')  # Remove leading separators

                # Stop provision text at period followed by capital letter (new sentence)
                # This prevents including text that belongs to the next section
                period_match = re.search(r'\.\s+[A-Z]', text)
                if period_match:
                    # Cut off at the period, don't include the new sentence
                    text = text[:period_match.start() + 1]  # Include the period

                # Remove trailing separators
                text = text.rstrip('; \t\n\r')   # Remove trailing semicolons

                # Only include if this looks like a real provision (substantial content)
                if number and text and len(text) > 5:  # At least 5 characters for real provisions
                    provisions_in_paragraph.append({
                        'number': number,
                        'text': text
                    })

                i += 2

            if iteration_count >= max_iterations:
                print(f"Warning: Hit iteration limit in _find_provisions_in_paragraph")

        except Exception as e:
            print(f"Error in _find_provisions_in_paragraph: {e}")
            # Return empty list on error to avoid breaking the pipeline
            return []

        return provisions_in_paragraph

    def _find_hyphenated_items_in_paragraph(self, content: str) -> List[Dict]:
        """Find hyphenated list items in paragraph content."""
        hyphenated_items = []

        # Look for hyphenated items pattern: "- item text" or "\\- item text"
        # Only process if there's a colon (indicating a list introduction)
        if ':' not in content:
            return hyphenated_items

        try:
            # Split on hyphen markers (handle both - and \\- patterns)
            parts = re.split(r'(?:\\)?-\s+', content)

            # Safety check
            if len(parts) < 2:
                return hyphenated_items

            # Process the parts: [prefix, item1, item2, ...]
            for i in range(1, len(parts)):  # Skip the prefix part
                text = parts[i].strip()

                # Stop item text at period followed by capital letter (new sentence)
                period_match = re.search(r'\.\s+[A-Z]', text)
                if period_match:
                    text = text[:period_match.start() + 1]  # Include the period

                # Clean up text - remove trailing separators
                text = text.rstrip('; \t\n\r')

                # Only include if this looks like a real item (substantial content)
                if text and len(text) > 5:  # At least 5 characters for real items
                    hyphenated_items.append({
                        'type': 'hyphenated',
                        'text': text
                    })

        except Exception as e:
            print(f"Error in _find_hyphenated_items_in_paragraph: {e}")
            return []

        return hyphenated_items

    def _smart_split_provisions(self, content: str) -> List[str]:
        """
        Smart splitting that distinguishes between provision markers and references.

        This method analyzes context to avoid splitting on references like "article 2, 1°"
        while correctly identifying real provision markers like "1°", "2°".
        """
        # First, find all potential provision markers
        provision_pattern = re.compile(r'(\d+°)')
        matches = list(provision_pattern.finditer(content))

        if not matches:
            return [content]

        # Analyze each match to determine if it's a real provision or a reference
        valid_splits = []

        for match in matches:
            number = match.group(1)
            start_pos = match.start()
            end_pos = match.end()

            # Get context before and after the match
            before_context = content[max(0, start_pos - 50):start_pos]
            after_context = content[end_pos:min(len(content), end_pos + 20)]

            # Check if this looks like a real provision marker
            is_real_provision = self._is_real_provision_marker(number, before_context, after_context, start_pos == 0)

            if is_real_provision:
                valid_splits.append(start_pos)

        # Split the content at valid provision positions
        if not valid_splits:
            return [content]

        parts = []
        last_pos = 0

        for split_pos in valid_splits:
            # Add text before this provision
            if split_pos > last_pos:
                parts.append(content[last_pos:split_pos])

            # Find the end of the provision number
            match = provision_pattern.match(content, split_pos)
            if match:
                parts.append(match.group(1))  # The provision number
                last_pos = match.end()

        # Add remaining text
        if last_pos < len(content):
            parts.append(content[last_pos:])

        return parts

    def _is_real_provision_marker(self, number: str, before_context: str, after_context: str, is_at_start: bool) -> bool:
        """
        Determine if a numbered marker is a real provision or just a reference.

        Args:
            number: The provision number (e.g., "1°", "2°")
            before_context: Text before the marker (up to 50 chars)
            after_context: Text after the marker (up to 20 chars)
            is_at_start: Whether this marker is at the very start of content
        """
        # Real provisions typically appear:
        # 1. At the start of content
        # 2. After colons (introductory text)
        # 3. After semicolons (previous provisions)
        # 4. After periods ending sentences

        # References typically appear:
        # 1. After commas in citations: "article 2, 1°"
        # 2. In the middle of sentences without proper separators

        # Check for reference patterns (these are NOT real provisions)
        reference_patterns = [
            r'article\s+\d+,\s*$',  # "article 2, " (before the number)
            r'art\.\s+\d+,\s*$',    # "art. 2, " (before the number)
            r'§\s+\d+,\s*$',        # "§ 2, " (before the number)
            r',\s*$',               # Just a comma before (generic reference)
        ]

        for pattern in reference_patterns:
            if re.search(pattern, before_context, re.IGNORECASE):
                return False

        # Check for provision patterns (these ARE real provisions)
        provision_patterns = [
            r':\s*$',               # Colon before (introductory text)
            r';\s*$',               # Semicolon before (previous provision)
            r'\.\s*$',              # Period before (end of sentence)
            r'^\s*$',               # Start of content or after whitespace
        ]

        if is_at_start:
            return True

        for pattern in provision_patterns:
            if re.search(pattern, before_context):
                return True

        # Additional check: if the after_context starts with typical provision content
        # (quotes, definitions, etc.), it's likely a real provision
        if re.match(r'^\s*["\']', after_context):
            return True

        # Default to False for ambiguous cases (safer to not split)
        return False

    def _generate_paragraph_with_provisions_and_items(self, content: str, provisions: List[Dict], hyphenated_items: List[Dict],
                                                     footnotes: List[Dict] = None, footnote_references: List[Dict] = None, dossier_number: str = None) -> str:
        """Generate HTML for a paragraph that contains numbered provisions and/or hyphenated items."""
        # Default to empty lists if not provided
        if footnotes is None:
            footnotes = []
        if footnote_references is None:
            footnote_references = []

        # If we only have provisions, use the existing logic
        if provisions and not hyphenated_items:
            return self._generate_paragraph_with_provisions(content, provisions, footnotes, footnote_references, dossier_number)

        # If we only have hyphenated items, use bullet point logic
        if hyphenated_items and not provisions:
            return self._generate_paragraph_with_hyphenated_items(content, hyphenated_items, footnotes, footnote_references, dossier_number)

        # If we have both, we need to handle them together
        if provisions and hyphenated_items:
            return self._generate_paragraph_with_mixed_items(content, provisions, hyphenated_items, footnotes, footnote_references, dossier_number)

        # Fallback to simple paragraph
        return self._generate_simple_paragraph(content, footnotes, footnote_references, dossier_number)

    def _generate_paragraph_with_provisions(self, content: str, provisions: List[Dict],
                                           footnotes: List[Dict] = None, footnote_references: List[Dict] = None, dossier_number: str = None) -> str:
        """Generate HTML for a paragraph that contains numbered provisions."""
        # Check for preserved table placeholders first
        if '[TABLE_PLACEHOLDER_' in content:
            document_id = getattr(self, 'current_document_id', None)
            logger.info(f"🔍 Found TABLE_PLACEHOLDER in _generate_paragraph_with_provisions, document_id: {document_id}")
            return self._generate_paragraph_with_preserved_tables(content, footnotes, footnote_references, document_id, dossier_number)

        html = ''

        # Default to empty lists if not provided
        if footnotes is None:
            footnotes = []
        if footnote_references is None:
            footnote_references = []

        # Group provisions by their sequences (when numbering restarts)
        provision_groups = []
        current_group = []
        last_number = 0

        for provision in provisions:
            # Extract numeric part from provision number (e.g., "3°" -> 3)
            import re
            number_match = re.search(r'(\d+)', provision['number'])
            if number_match:
                current_number = int(number_match.group(1))

                # If number decreased, start a new group
                if current_number <= last_number and current_group:
                    provision_groups.append(current_group)
                    current_group = []

                current_group.append(provision)
                last_number = current_number

        # Add the last group
        if current_group:
            provision_groups.append(current_group)

        # Process each group separately
        content_position = 0

        for group in provision_groups:
            # Find where this group starts in the content
            first_provision = group[0]
            group_start = content.find(first_provision['number'], content_position)

            if group_start == -1:
                continue

            # Add any text before this group
            text_before = content[content_position:group_start].strip()
            if text_before:
                # Clean up the text (remove trailing separators but keep meaningful content)
                text_before = re.sub(r'[:\s]*$', '', text_before)
                if text_before and len(text_before) > 1:
                    text_before = self._process_footnotes_in_text(text_before + ':', footnotes, footnote_references, dossier_number)  # Add colon back
                    html += f'        <p class="intro-text">{text_before}</p>\n'

            # Generate the provisions list for this group
            html += '        <ol class="numbered-provisions">\n'

            for provision in group:
                number = provision['number']
                text = provision['text']

                # Clean and format the provision text with footnotes
                formatted_text = self._process_footnotes_in_text(text, footnotes, footnote_references, dossier_number)

                html += f'          <li class="provision" data-number="{escape(number)}">\n'
                html += f'            <span class="provision-text">{formatted_text}</span>\n'

                # Add any citations that appear in this provision
                citations = self.citation_pattern.findall(text)
                if citations:
                    html += '            <div class="legal-citations">\n'
                    for citation in citations:
                        html += f'              <span class="citation">&lt;{escape(citation)}&gt;</span>\n'
                    html += '            </div>\n'

                html += '          </li>\n'

            html += '        </ol>\n'

            # Update position to after this group
            last_provision = group[-1]
            last_provision_end = content.find(last_provision['text'], group_start) + len(last_provision['text'])
            content_position = last_provision_end

        # Add any remaining text after all provisions
        remaining_text = content[content_position:].strip()
        if remaining_text and len(remaining_text) > 10:
            # Clean up remaining text but preserve citation spans and footnote markers
            # Don't strip HTML tags - use the markers-aware method instead
            remaining_text = self._clean_and_format_text_with_markers(remaining_text)
            if remaining_text:
                html += f'        <p class="closing-text">{remaining_text}</p>\n'

        return html

    def _generate_paragraph_with_hyphenated_items(self, content: str, hyphenated_items: List[Dict],
                                                 footnotes: List[Dict] = None, footnote_references: List[Dict] = None, dossier_number: str = None) -> str:
        """Generate HTML for a paragraph that contains hyphenated list items."""
        # Check for preserved table placeholders first
        if '[TABLE_PLACEHOLDER_' in content:
            document_id = getattr(self, 'current_document_id', None)
            logger.info(f"🔍 Found TABLE_PLACEHOLDER in _generate_paragraph_with_hyphenated_items, document_id: {document_id}")
            return self._generate_paragraph_with_preserved_tables(content, footnotes, footnote_references, document_id, dossier_number)

        html = ''

        # Default to empty lists if not provided
        if footnotes is None:
            footnotes = []
        if footnote_references is None:
            footnote_references = []

        # Find the intro text (everything before the first hyphen)
        first_hyphen_pos = -1
        if hyphenated_items:
            # Look for the first hyphen in the content
            first_hyphen_pos = content.find('- ')
            if first_hyphen_pos == -1:
                first_hyphen_pos = content.find('\\- ')

            if first_hyphen_pos > 0:
                intro_text = content[:first_hyphen_pos].strip()
                # Clean up the intro text (remove trailing separators but keep meaningful content)
                intro_text = re.sub(r'[:\s]*$', '', intro_text)
                if intro_text and len(intro_text) > 1:
                    intro_text = self._process_footnotes_in_text(intro_text + ':', footnotes, footnote_references, dossier_number)  # Add colon back
                    html += f'        <p class="intro-text">{intro_text}</p>\n'

        # Generate the hyphenated items list
        if hyphenated_items:
            html += '        <ul class="hyphenated-items">\n'

            for item in hyphenated_items:
                text = item['text']

                # Clean and format the item text with footnotes
                formatted_text = self._process_footnotes_in_text(text, footnotes, footnote_references, dossier_number)

                html += f'          <li class="hyphenated-item">\n'
                html += f'            <span class="item-text">{formatted_text}</span>\n'
                html += f'          </li>\n'

            html += '        </ul>\n'

        # Find and add closing text after the hyphenated items
        if hyphenated_items and first_hyphen_pos > -1:
            # Find where the last hyphenated item ends in the original content
            last_item = hyphenated_items[-1]
            last_item_text = last_item['text']

            # Find the position of the last item in the content
            # We need to be careful because the item text might be cleaned up
            last_item_pos = content.rfind(last_item_text.rstrip('.;, \t\n\r'))

            if last_item_pos != -1:
                # Calculate where the last item ends
                item_end_pos = last_item_pos + len(last_item_text.rstrip('.;, \t\n\r'))

                # Look for the actual end including punctuation
                remaining_content = content[item_end_pos:]

                # Skip past any punctuation and separators that are part of the list
                skip_match = re.match(r'^[.;,\s]*', remaining_content)
                if skip_match:
                    actual_end_pos = item_end_pos + skip_match.end()
                    closing_text = content[actual_end_pos:].strip()

                    if closing_text and len(closing_text) > 10:
                        # Clean and format the closing text
                        closing_text = self._clean_and_format_text(closing_text)
                        html += f'        <div class="closing-text">\n'
                        html += f'          <p>{closing_text}</p>\n'
                        html += f'        </div>\n'

        return html

    def _generate_paragraph_with_mixed_items(self, content: str, provisions: List[Dict], hyphenated_items: List[Dict], footnotes: List[Dict] = None, footnote_references: List[Dict] = None, dossier_number: str = None) -> str:
        """Generate HTML for a paragraph that contains both numbered provisions and hyphenated items."""
        # Check for preserved table placeholders first
        if '[TABLE_PLACEHOLDER_' in content:
            document_id = getattr(self, 'current_document_id', None)
            logger.info(f"🔍 Found TABLE_PLACEHOLDER in _generate_paragraph_with_mixed_items, document_id: {document_id}")
            return self._generate_paragraph_with_preserved_tables(content, footnotes, footnote_references, document_id, dossier_number)

        # For now, handle them separately - provisions first, then hyphenated items
        # This can be enhanced later if we find cases where they're truly intermixed
        html = ''

        # Generate provisions first
        if provisions:
            html += self._generate_paragraph_with_provisions(content, provisions, footnotes, footnote_references)

        # Then generate hyphenated items
        if hyphenated_items:
            html += self._generate_paragraph_with_hyphenated_items(content, hyphenated_items, footnotes, footnote_references)

        return html

    def _generate_simple_paragraph(self, content: str, footnotes: List[Dict] = None, footnote_references: List[Dict] = None, dossier_number: str = None) -> str:
        """Generate HTML for a simple paragraph without numbered provisions."""
        # Default to empty lists if not provided
        if footnotes is None:
            footnotes = []
        if footnote_references is None:
            footnote_references = []

        # Check for preserved table placeholders first
        if '[TABLE_PLACEHOLDER_' in content:
            document_id = getattr(self, 'current_document_id', None)
            logger.debug(f"Found TABLE_PLACEHOLDER in _generate_simple_paragraph, document_id: {document_id}")
            return self._generate_paragraph_with_preserved_tables(content, footnotes, footnote_references, document_id, dossier_number)

        # Process footnotes and format the content
        formatted_content = self._process_footnotes_in_text(content, footnotes, footnote_references, dossier_number)

        # Check for insertion notes (after footnote processing)
        insertion_notes = self.insertion_pattern.findall(content)
        if insertion_notes:
            for note in insertion_notes:
                note_html = f'<span class="insertion-note">&lt;{escape(note)}&gt;</span>'
                # Need to be careful with replacement since we now have HTML markers
                formatted_content = formatted_content.replace(f'&lt;{escape(note)}&gt;', note_html)

        return f'        <p>{formatted_content}</p>\n'
    
    def _clean_and_format_text(self, text: str) -> str:
        """Clean and format text content with proper HTML markup and enhanced citation processing."""
        if not text:
            return ''

        # Remove literal \n and \\ characters that come from JSON escaping
        text = text.replace('\\n', ' ')  # Replace literal \n with space
        text = text.replace('\\\\', '')  # Remove literal backslashes
        text = text.replace('\n', ' ')   # Replace actual newlines with space

        # Check if text already contains citation spans (to avoid double processing)
        has_citation_spans = '<span class="legal-citation' in text

        # Process enhanced legal citations BEFORE HTML escaping
        # Only if the text doesn't already contain citation spans from previous processing
        if self.citation_parser and not has_citation_spans:
            try:
                text, citations = self.citation_parser.process_text_with_citations(text)
                if citations:
                    logger.debug(f"Processed {len(citations)} enhanced citations in text")
            except Exception as e:
                logger.warning(f"Error processing enhanced citations: {e}")
                # Fall back to basic citation processing
        elif has_citation_spans:
            logger.debug("Text already contains citation spans, skipping citation processing to avoid double processing")

        # Escape HTML (after citation processing which creates HTML)
        # Split text to preserve citation HTML while escaping the rest
        citation_pattern = re.compile(r'(<span class="legal-citation[^>]*>.*?</span>)', re.DOTALL | re.IGNORECASE)
        parts = citation_pattern.split(text)

        escaped_parts = []
        for i, part in enumerate(parts):
            if i % 2 == 0:  # Regular text (even indices)
                if has_citation_spans:
                    # Text already contains citation spans, so it has been processed by citation parser
                    # The citation parser has already escaped content, so don't escape again
                    processed_part = part
                    # Format footnote references (but don't escape first)
                    processed_part = self.footnote_pattern.sub(r'<span class="footnote-ref">[\1 \2]\1</span>', processed_part)
                    escaped_parts.append(processed_part)
                else:
                    # Text has not been processed by citation parser, apply normal escaping
                    escaped_part = escape(part)
                    # Format footnote references
                    escaped_part = self.footnote_pattern.sub(r'<span class="footnote-ref">[\1 \2]\1</span>', escaped_part)
                    # Format basic legal citations (fallback for citations not caught by enhanced parser)
                    # Updated to handle all law types (L, DRW, AR, etc.), not just L
                    escaped_part = re.sub(r'&lt;([A-Z]+\s+[^&]+)&gt;', r'<span class="citation">&lt;\1&gt;</span>', escaped_part)
                    escaped_parts.append(escaped_part)
            else:  # Citation HTML (odd indices) - keep as is
                escaped_parts.append(part)

        text = ''.join(escaped_parts)

        # Clean up extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()

        return text

    def _process_footnotes_in_text(self, text: str, footnotes: List[Dict], footnote_references: List[Dict], dossier_number: str = None) -> str:
        """
        Process footnote references in text and add HTML markers for frontend processing.

        This method handles footnotes that may span across multiple structural elements by:
        1. Finding footnote references that intersect with the given text
        2. Adding HTML markers only for the portions that appear in this text
        3. Preserving the structure for React frontend processing

        Args:
            text: The text content to process
            footnotes: List of footnote objects with id, footnote_content, direct_url, etc.
            footnote_references: List of footnote reference objects with reference_number, referenced_text, etc.
            dossier_number: Optional document dossier number for data attributes

        Returns:
            Text with footnote markers replaced by HTML spans with data attributes
        """
        if not footnote_references or not footnotes:
            return self._clean_and_format_text(text)

        # Create a map of footnote numbers to footnote objects for quick lookup
        footnote_map = {}
        for footnote in footnotes:
            footnote_map[footnote.get('footnote_number', '')] = footnote

        # Process text to add footnote markers
        # We need to be careful about overlapping footnotes and process them in a way that doesn't interfere

        # First, find all footnote references that have text in our content
        applicable_refs = []
        for ref in footnote_references:
            ref_number = ref.get('reference_number', '')
            referenced_text = ref.get('referenced_text', '')

            if not ref_number or not referenced_text:
                continue

            # Find the corresponding footnote
            footnote = footnote_map.get(ref_number)
            if not footnote:
                continue

            # Check if this footnote reference text appears in our text
            text_pos = self._find_robust_text_match(referenced_text, text)
            if text_pos != -1:
                # Found exact or robust match
                applicable_refs.append({
                    'ref': ref,
                    'footnote': footnote,
                    'text_pos': text_pos,
                    'text_end': text_pos + len(referenced_text),
                    'referenced_text': referenced_text,
                    'ref_number': ref_number
                })
            else:
                # Check for partial matches for footnotes that span multiple elements
                intersection = self._find_text_intersection(referenced_text, text)
                if intersection and len(intersection.strip()) > 10:
                    text_pos = text.find(intersection)
                    if text_pos != -1:
                        applicable_refs.append({
                            'ref': ref,
                            'footnote': footnote,
                            'text_pos': text_pos,
                            'text_end': text_pos + len(intersection),
                            'referenced_text': referenced_text,  # Keep original for data attribute
                            'actual_text': intersection,  # What we actually found
                            'ref_number': ref_number
                        })

        # Sort by position in text (earliest first) to avoid interference
        applicable_refs.sort(key=lambda x: x['text_pos'])

        # Check for overlapping footnotes and resolve conflicts
        applicable_refs = self._resolve_overlapping_footnotes(applicable_refs)

        # Process footnotes from end to beginning to avoid position shifts
        applicable_refs.reverse()

        processed_text = text
        for ref_info in applicable_refs:
            ref_number = ref_info['ref_number']
            referenced_text = ref_info['referenced_text']
            actual_text = ref_info.get('actual_text', referenced_text)
            text_pos = ref_info['text_pos']
            text_end = ref_info['text_end']

            # Double-check that the text at this position matches what we expect
            current_text = processed_text[text_pos:text_end]
            if current_text != actual_text:
                # Text has changed (likely due to previous footnote processing)
                # Try to find the text again
                new_pos = processed_text.find(actual_text, text_pos - 50)
                if new_pos != -1:
                    text_pos = new_pos
                    text_end = new_pos + len(actual_text)
                else:
                    # Skip this footnote if we can't find the text
                    continue

            # Create footnote marker HTML with data attributes for React processing
            footnote = ref_info['footnote']
            direct_article_url = footnote.get('direct_article_url', '')
            
            # Extract dossier number from the footnote's law reference
            footnote_dossier_number = ''
            law_reference = footnote.get('law_reference', {})
            if law_reference:
                footnote_dossier_number = law_reference.get('date_reference', '')

            marker_html = (
                f'<span class="footnote-ref" '
                f'data-footnote-id="{escape(ref_number)}" '
                f'data-referenced-text="{escape(referenced_text)}" '
                f'data-direct-article-url="{escape(direct_article_url)}" '
                f'data-article-dossier-number="{escape(footnote_dossier_number)}">'
                f'{escape(actual_text)}'
                f'</span>'
            )

            # Replace the text at the specific position to avoid conflicts
            processed_text = processed_text[:text_pos] + marker_html + processed_text[text_end:]

        # Clean and format the remaining text (but preserve our HTML markers)
        return self._clean_and_format_text_with_markers(processed_text)

    def _resolve_overlapping_footnotes(self, footnote_refs: List[Dict]) -> List[Dict]:
        """
        Resolve overlapping footnote references by removing conflicts.

        When footnotes overlap, we prioritize:
        1. Longer footnotes over shorter ones
        2. Earlier footnotes over later ones (if same length)
        """
        if len(footnote_refs) <= 1:
            return footnote_refs

        # Sort by position first
        sorted_refs = sorted(footnote_refs, key=lambda x: x['text_pos'])

        resolved_refs = []
        for current_ref in sorted_refs:
            current_start = current_ref['text_pos']
            current_end = current_ref['text_end']

            # Check if this ref overlaps with any already resolved refs
            overlaps = False
            for resolved_ref in resolved_refs:
                resolved_start = resolved_ref['text_pos']
                resolved_end = resolved_ref['text_end']

                # Check for overlap
                if (current_start < resolved_end and current_end > resolved_start):
                    # There's an overlap
                    current_length = current_end - current_start
                    resolved_length = resolved_end - resolved_start

                    # Keep the longer footnote, or the earlier one if same length
                    if current_length > resolved_length:
                        # Remove the resolved ref and add current
                        resolved_refs.remove(resolved_ref)
                        resolved_refs.append(current_ref)
                    # If current is shorter or same length, skip it
                    overlaps = True
                    break

            if not overlaps:
                resolved_refs.append(current_ref)

        return resolved_refs

    def _find_robust_text_match(self, search_text: str, target_text: str) -> int:
        """
        Find text with robust matching that handles encoding differences and whitespace variations.

        Returns the position of the match, or -1 if not found.
        """
        # Try exact match first
        pos = target_text.find(search_text)
        if pos != -1:
            return pos

        # Normalize both texts for comparison
        def normalize_text(text):
            import unicodedata
            # Normalize unicode characters
            text = unicodedata.normalize('NFKC', text)
            # Replace different types of apostrophes and quotes
            text = text.replace(''', "'").replace(''', "'")
            text = text.replace('"', '"').replace('"', '"')
            text = text.replace('–', '-').replace('—', '-')
            # Normalize whitespace
            text = ' '.join(text.split())
            return text

        normalized_search = normalize_text(search_text)
        normalized_target = normalize_text(target_text)

        # Try normalized match
        pos = normalized_target.find(normalized_search)
        if pos != -1:
            # Find the corresponding position in the original text
            # This is approximate but should work for most cases
            return target_text.find(search_text[:20]) if len(search_text) > 20 else -1

        # Try partial match with first significant words
        search_words = normalized_search.split()
        if len(search_words) >= 3:
            partial_search = ' '.join(search_words[:3])
            pos = normalized_target.find(partial_search)
            if pos != -1:
                # Find the corresponding position in the original text
                original_partial = ' '.join(search_text.split()[:3])
                return target_text.find(original_partial)

        return -1

    def _find_text_intersection(self, footnote_text: str, current_text: str) -> str:
        """
        Find the longest meaningful intersection between footnote text and current text.
        This handles cases where footnotes span multiple structural elements.
        """
        # Clean both texts for comparison
        clean_footnote = footnote_text.strip()
        clean_current = current_text.strip()

        # Try to find the longest substring that appears in both
        max_intersection = ""

        # Start with sentences or meaningful chunks
        import re

        # Split footnote text into sentences/chunks
        footnote_chunks = re.split(r'[.!?]\s+', clean_footnote)

        for chunk in footnote_chunks:
            chunk = chunk.strip()
            if len(chunk) > 10 and chunk in clean_current:
                if len(chunk) > len(max_intersection):
                    max_intersection = chunk

        # If no sentence-level match, try phrase-level (comma-separated)
        if not max_intersection:
            footnote_phrases = re.split(r',\s+', clean_footnote)
            for phrase in footnote_phrases:
                phrase = phrase.strip()
                if len(phrase) > 10 and phrase in clean_current:
                    if len(phrase) > len(max_intersection):
                        max_intersection = phrase

        return max_intersection

    def _clean_and_format_text_with_markers(self, text: str) -> str:
        """
        Clean and format text content while preserving footnote markers and processing enhanced citations.

        This is similar to _clean_and_format_text but preserves HTML footnote markers.
        """
        if not text:
            return ''

        # Remove literal \n and \\ characters that come from JSON escaping
        text = text.replace('\\n', ' ')  # Replace literal \n with space
        text = text.replace('\\\\', '')  # Remove literal backslashes
        text = text.replace('\n', ' ')   # Replace actual newlines with space

        # Check if text already contains citation spans (to avoid double processing)
        has_citation_spans = '<span class="legal-citation' in text

        # Process enhanced legal citations BEFORE HTML escaping (but after footnote processing)
        # Only if the text doesn't already contain citation spans from previous processing
        if self.citation_parser and not has_citation_spans:
            try:
                text, citations = self.citation_parser.process_text_with_citations(text)
                if citations:
                    logger.debug(f"Processed {len(citations)} enhanced citations in text with markers")
            except Exception as e:
                logger.warning(f"Error processing enhanced citations in text with markers: {e}")
        elif has_citation_spans:
            logger.debug("Text already contains citation spans, skipping citation processing to avoid double processing")

        # Split text into parts: footnote markers, citation markers, and regular text
        import re
        # Pattern that handles both footnote and citation markers
        marker_pattern = re.compile(
            r'(<span class="(?:footnote-ref|legal-citation[^"]*)"[^>]*>.*?</span>)',
            re.DOTALL | re.IGNORECASE
        )
        parts = marker_pattern.split(text)

        processed_parts = []
        for i, part in enumerate(parts):
            if i % 2 == 0:  # Regular text (even indices)
                if has_citation_spans:
                    # Text already contains citation spans, so it has been processed by citation parser
                    # The citation parser has already escaped content, so don't escape again
                    cleaned_part = re.sub(r'\s+', ' ', part).strip()
                    processed_parts.append(cleaned_part)
                else:
                    # Text has not been processed by citation parser, apply normal escaping
                    escaped_part = escape(part)
                    # Format basic legal citations (fallback for citations not caught by enhanced parser)
                    # Updated to handle all law types (L, DRW, AR, etc.), not just L
                    escaped_part = re.sub(r'&lt;([A-Z]+\s+[^&]+)&gt;', r'<span class="citation">&lt;\1&gt;</span>', escaped_part)
                    # Clean up extra whitespace
                    escaped_part = re.sub(r'\s+', ' ', escaped_part).strip()
                    processed_parts.append(escaped_part)
            else:  # Footnote or citation marker (odd indices) - keep as is
                processed_parts.append(part)

        return ''.join(processed_parts)

    def _generate_complete_html_document(self, article_html: str, article_number: str) -> str:
        """Generate a complete HTML document with embedded CSS."""

        css_styles = """
        body {
            font-family: 'Georgia', 'Times New Roman', serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fafafa;
            color: #333;
        }

        .legal-article {
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            border: 1px solid #e0e0e0;
        }

        .article-header {
            border-bottom: 3px solid #2c3e50;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }

        .article-number {
            color: #2c3e50;
            margin: 0 0 15px 0;
            font-size: 2.2em;
            font-weight: bold;
        }

        .former-article {
            color: #7f8c8d;
            font-style: italic;
            font-size: 1em;
            display: block;
            margin-bottom: 10px;
        }

        .legal-citations {
            margin-top: 15px;
        }

        .citation {
            display: inline-block;
            background: #ecf0f1;
            padding: 4px 8px;
            margin: 3px;
            border-radius: 4px;
            font-size: 0.85em;
            color: #34495e;
            border: 1px solid #bdc3c7;
        }

        /* Enhanced legal citation styles */
        .legal-citation {
            display: inline-block;
            background: #e8f4fd;
            padding: 3px 8px;
            margin: 2px;
            border-radius: 4px;
            font-size: 0.85em;
            color: #1565c0;
            border: 1px solid #bbdefb;
            cursor: pointer;
            transition: background-color 0.2s ease, border-color 0.2s ease;
            text-decoration: none;
        }

        .legal-citation:hover {
            background: #d1e7dd;
            border-color: #a3cfbb;
            color: #0f5132;
        }

        .legal-citation-insertion {
            background: #d1ecf1;
            color: #0c5460;
            border-color: #bee5eb;
        }

        .legal-citation-insertion:hover {
            background: #b8daff;
            border-color: #86b7fe;
            color: #084298;
        }

        .legal-citation-modification {
            background: #fff3cd;
            color: #856404;
            border-color: #ffeaa7;
        }

        .legal-citation-modification:hover {
            background: #ffe69c;
            border-color: #ffdf7e;
            color: #664d03;
        }

        .legal-citation-abrogation {
            background: #f8d7da;
            color: #721c24;
            border-color: #f1aeb5;
        }

        .legal-citation-abrogation:hover {
            background: #f5c2c7;
            border-color: #ea868f;
            color: #58151c;
        }

        .legal-citation-replacement {
            background: #e2e3e5;
            color: #383d41;
            border-color: #d6d8db;
        }

        .legal-citation-replacement:hover {
            background: #d1ecf1;
            border-color: #bee5eb;
            color: #0c5460;
        }

        .paragraph {
            margin-bottom: 30px;
            border-left: 4px solid #3498db;
            padding-left: 20px;
            background: #f8f9fa;
            padding: 20px;
            border-radius: 0 8px 8px 0;
        }

        .paragraph-marker {
            color: #2980b9;
            margin: 0 0 15px 0;
            font-size: 1.4em;
            font-weight: bold;
        }

        .paragraph-content p {
            margin-bottom: 15px;
            text-align: justify;
        }

        .intro-text {
            font-weight: 500;
            margin-bottom: 20px;
            color: #2c3e50;
        }

        .numbered-provisions {
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            border: 2px solid #e8f4f8;
            list-style: none;
            counter-reset: provision-counter;
        }

        .hyphenated-items {
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            border: 2px solid #f0e8f4;
            list-style: none;
        }

        .provision {
            margin-bottom: 20px;
            padding: 15px;
            background: #fff;
            border-radius: 6px;
            border-left: 4px solid #e74c3c;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            position: relative;
        }

        .provision:last-child {
            margin-bottom: 0;
        }

        .provision-marker {
            font-weight: bold;
            color: #c0392b;
            margin-right: 10px;
            font-size: 1.1em;
        }

        .provision-text {
            line-height: 1.6;
            text-align: justify;
        }

        .hyphenated-item {
            margin-bottom: 15px;
            padding: 12px;
            background: #fff;
            border-radius: 6px;
            border-left: 4px solid #8e44ad;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            position: relative;
        }

        .hyphenated-item:last-child {
            margin-bottom: 0;
        }

        .hyphenated-item:before {
            content: "•";
            color: #8e44ad;
            font-weight: bold;
            font-size: 1.2em;
            margin-right: 10px;
        }

        .item-text {
            line-height: 1.6;
            text-align: justify;
        }

        .closing-text {
            margin-top: 20px;
            font-style: italic;
            color: #555;
            background: #f1f2f6;
            padding: 15px;
            border-radius: 6px;
            border-left: 4px solid #95a5a6;
        }

        .footnote-ref {
            background: #fff3cd;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 0.9em;
            color: #856404;
            border: 1px solid #ffeaa7;
        }

        .insertion-note {
            background: #d1ecf1;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.9em;
            color: #0c5460;
            border: 1px solid #bee5eb;
        }

        .article-text p {
            margin-bottom: 15px;
            text-align: justify;
        }

        /* Table styles */
        .table-container {
            margin: 20px 0;
            overflow-x: auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .table-section-separator {
            height: 20px;
            margin: 15px 0;
            border-bottom: 2px solid #e0e0e0;
            position: relative;
        }

        .table-section-separator::after {
            content: "";
            position: absolute;
            bottom: -1px;
            left: 50%;
            transform: translateX(-50%);
            width: 50px;
            height: 2px;
            background: #3498db;
        }

        .legal-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9em;
            background: white;
        }

        .legal-table th,
        .legal-table td {
            padding: 12px 8px;
            text-align: left;
            border: 1px solid #ddd;
            vertical-align: top;
        }

        .legal-table th {
            background: #f8f9fa;
            font-weight: bold;
            color: #2c3e50;
        }

        .legal-table .main-header th {
            background: #34495e;
            color: white;
            font-size: 1.1em;
            text-align: center;
        }

        .legal-table .sub-header th {
            background: #ecf0f1;
            color: #2c3e50;
            font-size: 0.9em;
            font-weight: 600;
        }

        .bilingual-table th,
        .bilingual-table td {
            text-align: center;
        }

        .bilingual-table .main-header th:first-child,
        .bilingual-table .main-header th:nth-child(7) {
            font-size: 1.2em;
            font-weight: bold;
        }

        .legal-table tbody tr:nth-child(even) {
            background: #f9f9f9;
        }

        .legal-table tbody tr:hover {
            background: #f1f3f4;
        }

        .legal-table td:first-child {
            font-weight: 500;
            background: #fafbfc;
        }

        /* Print styles */
        @media print {
            body {
                background-color: white;
                padding: 0;
            }

            .legal-article {
                box-shadow: none;
                border: none;
                padding: 20px;
            }

            .paragraph {
                background: white;
                border-left: 2px solid #333;
            }
        }

        /* Mobile responsive */
        @media (max-width: 768px) {
            body {
                padding: 10px;
            }

            .legal-article {
                padding: 20px;
            }

            .article-number {
                font-size: 1.8em;
            }

            .paragraph {
                padding: 15px;
            }

            .table-container {
                margin: 15px -10px;
            }

            .legal-table {
                font-size: 0.8em;
            }

            .legal-table th,
            .legal-table td {
                padding: 8px 4px;
            }
        }
        """

        complete_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Article {escape(article_number)} - Code Judiciaire Belge</title>
    <style>
{css_styles}
    </style>
</head>
<body>
{article_html}
</body>
</html>"""

        return complete_html


    def _generate_paragraph_with_provisions_preprocessed(self, content: str, provisions: List[Dict]) -> str:
        """Generate HTML for a paragraph with provisions where footnotes have already been processed."""
        # For now, use a simplified approach - just use the existing method but with preprocessed text
        return self._generate_paragraph_with_provisions(content, provisions, [], [])

    def _generate_paragraph_with_hyphenated_items_preprocessed(self, content: str, hyphenated_items: List[Dict]) -> str:
        """Generate HTML for a paragraph with hyphenated items where footnotes have already been processed."""
        # For now, use a simplified approach - just use the existing method but with preprocessed text
        return self._generate_paragraph_with_hyphenated_items(content, hyphenated_items, [], [])

    def _generate_paragraph_with_mixed_items_preprocessed(self, content: str, provisions: List[Dict], hyphenated_items: List[Dict]) -> str:
        """Generate HTML for a paragraph with mixed items where footnotes have already been processed."""
        # For now, use a simplified approach - just use the existing method but with preprocessed text
        return self._generate_paragraph_with_mixed_items(content, provisions, hyphenated_items)


def generate_html_for_article(article_data: Dict[str, Any], dossier_number: str = None) -> str:
    """
    Convenience function to generate HTML for a single article.

    Args:
        article_data: Article data from JSON
        dossier_number: Optional document dossier number for footnote data attributes

    Returns:
        Complete HTML string for the article
    """
    generator = LegalHtmlGenerator()
    return generator.generate_article_html(article_data, dossier_number=dossier_number)
