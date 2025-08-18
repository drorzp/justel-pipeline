#!/usr/bin/env python3
"""
article_extractor.py - Article extraction for Belgian Legal Documents

This module handles extraction of individual articles from Belgian legal documents,
including content parsing, numbered provisions, and content cleaning.

Author: Augment Agent
Date: 2025-07-13
"""

import re
import logging
from typing import Dict, List, Any, Optional, Tuple

# Handle both relative and absolute imports
try:
    from .extraction_utils import ExtractionUtils
    from .footnote_processor import FootnoteProcessor
    from ..html_generation.legal_html_generator import LegalHtmlGenerator
    from .citation_parser import CitationParser
    ENHANCED_CITATION_PARSER_AVAILABLE = True
except ImportError:
    from extraction_utils import ExtractionUtils
    from footnote_processor import FootnoteProcessor
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'html_generation'))
    from legal_html_generator import LegalHtmlGenerator
    try:
        from citation_parser import CitationParser
        ENHANCED_CITATION_PARSER_AVAILABLE = True
    except ImportError:
        ENHANCED_CITATION_PARSER_AVAILABLE = False
        logger.warning("Enhanced citation parser not available - using basic citation processing")

logger = logging.getLogger(__name__)


class ArticleExtractor:
    """
    Extracts individual articles from Belgian legal documents.
    """
    
    def __init__(self, utils: ExtractionUtils, footnote_processor: FootnoteProcessor, api_key: str = None, preserved_tables_dir: str = None):
        """
        Initialize with utility functions and footnote processor.

        Args:
            utils: ExtractionUtils instance
            footnote_processor: FootnoteProcessor instance
            api_key: Optional Gemini API key for LLM-based table generation
            preserved_tables_dir: Optional directory containing preserved HTML tables
        """
        self.utils = utils
        self.footnote_processor = footnote_processor
        self.html_generator = LegalHtmlGenerator(api_key=api_key, preserved_tables_dir=preserved_tables_dir)
        self.preserved_tables_dir = preserved_tables_dir

        # Initialize enhanced citation parser
        self.enhanced_citation_parser = None
        if ENHANCED_CITATION_PARSER_AVAILABLE:
            try:
                self.enhanced_citation_parser = CitationParser()
                logger.debug("Enhanced citation parser initialized in ArticleExtractor")
            except Exception as e:
                logger.warning(f"Failed to initialize enhanced citation parser: {e}")
                self.enhanced_citation_parser = None

        # Pre-compile regex patterns for performance (used across 100k+ files)
        import re
        self.legal_citation_pattern = re.compile(r'^<([^>]+)>\s*', re.IGNORECASE | re.DOTALL)
        self.url_pattern = re.compile(r'\(([^)]+)\)')

        # Regional variation pattern for Belgian legal documents
        # Matches patterns like: (REGION WALLONNE), (Région wallonne), (REGION FLAMANDE), (Région flamande), etc.
        # Handles both French "Région" and English "REGION" with various capitalizations
        # Updated to include BRUXELLES-CAPITALE both with and without "DE"
        # Updated to support both WALLONNE (double N) and WALLONE (single N) variations
        self.regional_pattern = re.compile(r'\((?:REGION|R[éeÉE]gion)\s+(WALLON(?:N)?E?|FLAMANDE?|BRUXELLES-CAPITALE|DE\s+BRUXELLES-CAPITALE|BRUXELLOISE)\)', re.IGNORECASE)

    def _extract_regional_suffix(self, article_content: str) -> str:
        """
        Extract regional suffix from article content to create unique article numbers.

        Args:
            article_content: The article content that may contain regional markers

        Returns:
            Regional suffix to append to article number (e.g., "-WALLONNE", "-FLAMANDE", "")
        """
        regional_match = self.regional_pattern.search(article_content)

        if regional_match:
            region = regional_match.group(1).strip()
            # Normalize region names for consistent suffixes
            # Handle both French and English variations with different capitalizations
            region_mapping = {
                'WALLONNE': 'WALLONNE',
                'WALLONE': 'WALLONNE',  # Handle potential single 'N' variation
                'WALLON': 'WALLONNE',   # Handle missing 'E' and single 'N' variation
                'FLAMANDE': 'FLAMANDE',
                'FLAMAND': 'FLAMANDE',  # Handle potential missing 'E' variation
                'BRUXELLES-CAPITALE': 'BRUXELLES',  # Handle standalone BRUXELLES-CAPITALE
                'DE BRUXELLES-CAPITALE': 'BRUXELLES',
                'BRUXELLOISE': 'BRUXELLES'
            }
            # Clean up any extra spaces in the region name
            region_clean = ' '.join(region.upper().split())
            normalized_region = region_mapping.get(region_clean, region_clean)
            return normalized_region  # Return just the region name, spaces will be handled in caller

        return ""

    def _remove_redundant_regional_text(self, content: str, regional_suffix: str) -> str:
        """
        Remove redundant regional text from article content when the region is already
        indicated in the article number.

        Args:
            content: The article content that may contain regional markers
            regional_suffix: The regional suffix extracted for the article number

        Returns:
            Content with redundant regional text removed
        """
        if not regional_suffix:
            return content

        # Create pattern to match the regional text at the beginning of content
        # Handle various formats: (REGION FLAMANDE), (Région flamande), etc.
        region_patterns = [
            f"(REGION {regional_suffix})",
            f"(Région {regional_suffix.lower()})",
            f"(REGION {regional_suffix.lower()})",
            f"(Région {regional_suffix})"
        ]

        # Try to remove the regional text if it appears at the very beginning
        for pattern in region_patterns:
            if content.strip().startswith(pattern):
                # Remove the pattern and any following whitespace
                content = content.strip()[len(pattern):].strip()
                break

        return content

    def parse_numbered_provisions(self, text: str) -> List[Dict[str, Any]]:
        """Parse numbered provisions from article text and clean footnote markers."""
        provisions = []

        # Find numbered provisions (1°, 2°, etc.)
        matches = self.utils.numbered_provision_pattern.finditer(text)

        for match in matches:
            number = match.group(1)
            provision_text = match.group(2).strip()

            # Clean footnote markers from provision text
            cleaned_provision_text = self._clean_footnote_references_intelligently(provision_text, [])

            # Additional cleanup for numbered provisions
            import re
            # Remove HTML tags and escaped citations
            cleaned_provision_text = re.sub(r'<[^>]+>', '', cleaned_provision_text)
            cleaned_provision_text = re.sub(r'&lt;[^&]+&gt;', '', cleaned_provision_text)
            # Remove trailing orphaned brackets
            cleaned_provision_text = re.sub(r'\]$', '', cleaned_provision_text.strip())
            # Clean up extra whitespace
            cleaned_provision_text = re.sub(r'\s+', ' ', cleaned_provision_text).strip()

            # Filter out provisions that are clearly citations (contain citation patterns)
            # Only skip if the provision text itself contains these patterns, not just any text after it
            if re.search(r'En\s+vigueur|art\.|[0-9]{4}-[0-9]{2}-[0-9]{2}', cleaned_provision_text):
                continue  # Skip this match as it's likely a citation, not a real provision

            provision = {
                "number": number,
                "text": cleaned_provision_text,
                "sub_items": []  # Could be enhanced to parse sub-items
            }
            provisions.append(provision)

        return provisions

    def extract_articles_with_hierarchy(self, content: str, hierarchy: Dict[str, List[Dict[str, Any]]], document_id: str = None) -> List[Dict[str, Any]]:
        """Extract all articles from the document content with hierarchy information."""
        articles = []

        # Split content by articles
        article_matches = list(self.utils.article_pattern.finditer(content))

        for i, match in enumerate(article_matches):
            # Extract article number from the appropriate capture group
            # Updated for 16-group pattern with case-insensitive support:
            # UPPERCASE patterns (Groups 1-8, preserved for backwards compatibility):
            # Group 1: [Art.] [NUMBER]. format (with brackets)
            # Group 2: [Art.] NUMBER. format (without brackets) - FIXED: captures Article 57
            # Group 3: [Art.] N. format (placeholder)
            # Group 4: [Art.] NUMBER\. format (literal backslash-period) - NEW: captures Article 3
            # Group 5: Art. [NUMBER] format (without brackets around Art) - NEW
            # Group 6: Article [NUMBER]. format
            # Group 7: Article NUMBER\. format (without brackets)
            # Group 8: [}Art.] [NUMBER] format (malformed brackets from TITLE conversion)
            # LOWERCASE patterns (Groups 9-16, case-insensitive equivalents):
            # Group 9: [art.] [NUMBER]. format
            # Group 10: [art.] NUMBER. format
            # Group 11: [art.] N. format
            # Group 12: [art.] NUMBER\. format
            # Group 13: art. [NUMBER] format
            # Group 14: article [NUMBER]. format
            # Group 15: article NUMBER\. format
            # Group 16: [}art.] [NUMBER] format (malformed brackets with lowercase)
            article_number = (match.group(1) or match.group(2) or match.group(3) or match.group(4) or
                            match.group(5) or match.group(6) or match.group(7) or match.group(8) or
                            match.group(9) or match.group(10) or match.group(11) or match.group(12) or
                            match.group(13) or match.group(14) or match.group(15) or match.group(16))
            start_pos = match.end()

            # Debug: log first few article numbers
            if i < 5:
                logger.info(f"DEBUG: Processing article {i+1}: '{article_number}'")

            # Find the end position (start of next article, next **TITLE** marker, **ANNEXE** marker, document section marker, or end of content)
            next_article_pos = article_matches[i + 1].start() if i + 1 < len(article_matches) else len(content)

            # Look for boundary markers between current article and next article
            search_content = content[start_pos:next_article_pos]

            # Check for **TITLE** markers
            title_matches = list(self.utils.title_pattern.finditer(search_content))

            # Check for **ANNEXE** markers
            annexe_pattern = re.compile(r'\*\*ANNEXE\*\*\[([^\]]+)\]')
            annexe_matches = list(annexe_pattern.finditer(search_content))

            # Check for document section markers like [12A] ## Travaux parlementaires [12B]
            section_pattern = re.compile(r'\[\d+[A-Z]\]\s*##\s*[^[]+\[\d+[A-Z]\]')
            section_matches = list(section_pattern.finditer(search_content))

            # Debug logging for Article 1er
            if article_number == "1er":
                logger.info(f"DEBUG Article 1er: start_pos={start_pos}, next_article_pos={next_article_pos}")
                logger.info(f"DEBUG Article 1er: search_content length={len(search_content)}")
                logger.info(f"DEBUG Article 1er: title_matches found={len(title_matches)}")
                logger.info(f"DEBUG Article 1er: annexe_matches found={len(annexe_matches)}")
                logger.info(f"DEBUG Article 1er: section_matches found={len(section_matches)}")
                if title_matches:
                    logger.info(f"DEBUG Article 1er: first title match at position={title_matches[0].start()}")
                    logger.info(f"DEBUG Article 1er: title content={title_matches[0].group()}")
                # Show first few characters of search content
                preview = search_content[:300].replace('\n', '\\n')
                logger.info(f"DEBUG Article 1er: search_content preview={preview}")

            # Find the earliest boundary marker
            boundary_positions = []
            if title_matches:
                boundary_positions.append(title_matches[0].start())
            if annexe_matches:
                boundary_positions.append(annexe_matches[0].start())
            if section_matches:
                boundary_positions.append(section_matches[0].start())

            if boundary_positions:
                # Stop at the earliest boundary marker
                end_pos = start_pos + min(boundary_positions)
            else:
                # No boundary markers found, use next article position
                end_pos = next_article_pos

            # Extract article content
            article_content = content[start_pos:end_pos].strip()

            # Split main content from footnotes
            main_content, footnotes = self.footnote_processor.split_article_content_and_footnotes(article_content, article_number)

            # Extract footnote references from main content
            footnote_references = self.footnote_processor.extract_footnote_references_from_text(main_content, article_number)

            # Parse numbered provisions
            numbered_provisions = self.parse_numbered_provisions(main_content)

            # Create main text (content without footnote references for clean display)
            main_text = self._clean_footnote_references_intelligently(main_content, footnote_references)

            # Extract legal citation markers from the beginning of article text (existing functionality)
            main_text, legal_citation = self._extract_legal_citation_markers(main_text)

            # Unescape markdown escape sequences to prevent double-escaping in JSON
            main_text = self.utils.unescape_markdown_sequences(main_text)

            # Store the original text as main_text_raw BEFORE citation processing
            main_text_raw = main_text.strip()

            # Enhanced citation processing - extract all citations throughout the article content
            # This creates HTML spans for display but doesn't modify the raw text
            enhanced_citations = []
            main_text_with_citation_spans = main_text  # Copy for HTML processing
            if self.enhanced_citation_parser:
                try:
                    # Process text to replace citations with HTML spans and get citation metadata
                    main_text_with_citation_spans, enhanced_citations = self.enhanced_citation_parser.process_text_with_citations(main_text)
                    if enhanced_citations:
                        logger.debug(f"Found {len(enhanced_citations)} enhanced citations in article {article_number}")
                except Exception as e:
                    logger.warning(f"Error in enhanced citation processing for article {article_number}: {e}")

            # Extract regional information and create unique article number
            regional_suffix = self._extract_regional_suffix(main_content)
            if regional_suffix:
                # Create unique article number with regional information
                # Clean up any extra spaces and ensure single space between number and region
                unique_article_number = f"{article_number} {regional_suffix.strip()}"
                unique_anchor_id = f"art_{article_number}_{regional_suffix.strip().replace(' ', '_')}"

                # Remove redundant regional text from main content if it's already in the article number
                main_content = self._remove_redundant_regional_text(main_content, regional_suffix)
            else:
                # No regional variation, use original number
                unique_article_number = article_number
                unique_anchor_id = f"art_{article_number}"

            # Detect abrogation status for entire article
            abrogation_status = self._detect_article_abrogation_status(main_text)

            # Find parent structure for this article (using hierarchy parser)
            try:
                from .hierarchy_parser import HierarchyParser
            except ImportError:
                from hierarchy_parser import HierarchyParser
            hierarchy_parser = HierarchyParser(self.utils)
            parent_structure = hierarchy_parser.find_article_parent_structure(article_number, hierarchy)

            # Build article content structure with optional legal citation
            article_content = {
                "main_text_raw": main_text_raw,  # Use original text with angle brackets
                "numbered_provisions": numbered_provisions
            }

            # Add abrogation status if detected
            if abrogation_status:
                article_content["abrogation_status"] = abrogation_status

            # Add legal citation if present
            if legal_citation:
                article_content["legal_citation"] = legal_citation

            # Add enhanced citations if found
            if enhanced_citations:
                article_content["enhanced_citations"] = enhanced_citations

            # Add regional information if present
            if regional_suffix:
                article_content["region"] = regional_suffix.lstrip('-')

            article = {
                "article_number": unique_article_number,  # Use unique number with regional info
                "anchor_id": unique_anchor_id,
                "content": article_content,
                "footnote_references": footnote_references,
                "footnotes": footnotes,
                "parent_structure": parent_structure
            }

            articles.append(article)

        return articles

    def _detect_article_abrogation_status(self, main_text: str) -> str:
        """
        Detect if an entire article has been abrogated based on specific patterns.

        This method looks for abrogation indicators that appear immediately after
        the article label/number (before any article content begins).

        Detection Rules:
        1. The abrogation indicator must appear immediately after the article label/number
        2. Look for the word "abrogé" or "Abrogé" in these specific patterns:
           - Inside legal citation angle brackets: <Abrogé par ...>
           - In square brackets before citation: [abrogé] <citation>
           - In parentheses before citation: (Abrogé) <citation>
           - In square brackets without citation: [Abrogé]

        Args:
            main_text (str): The main text content of the article

        Returns:
            str: "abrogé" if entire article is abrogated, empty string otherwise
        """
        if not main_text:
            return ""

        # Clean the text and get the first part (first 200 characters should be enough)
        # This ensures we only look at the beginning of the article content
        text_start = main_text.strip()[:200]

        # Pattern 1: [abrogé] or [Abrogé] in square brackets (with or without citation)
        # Examples: "[abrogé] <citation>", "[Abrogé]"
        square_bracket_pattern = r'\[(?:abrogé|Abrogé)\]'
        if re.search(square_bracket_pattern, text_start):
            return "abrogé"

        # Pattern 2: (abrogé) or (Abrogé) in parentheses (usually before citation)
        # Examples: "(Abrogé) <citation>"
        parentheses_pattern = r'\((?:abrogé|Abrogé)\)'
        if re.search(parentheses_pattern, text_start):
            return "abrogé"

        # Pattern 3: <Abrogé par ...> inside legal citation angle brackets
        # Examples: "<Abrogé par DCFL 2019-04-26/28, art. 45, 239; En vigueur : 01-01-2022>"
        angle_bracket_pattern = r'<(?:abrogé|Abrogé)\s+par\s+[^>]+>'
        if re.search(angle_bracket_pattern, text_start):
            return "abrogé"

        # Pattern 4: Check for standalone "abrogé" at the very beginning (after region info)
        # This handles cases like "(REGION FLAMANDE) abrogé" where it's the only content
        # Remove region info first, then check if remaining content is just "abrogé"
        region_pattern = r'^\([^)]+\)\s*'
        text_without_region = re.sub(region_pattern, '', text_start).strip()

        if text_without_region.lower() == "abrogé":
            return "abrogé"

        return ""

    def extract_articles(self, content: str, document_id: str = None) -> List[Dict[str, Any]]:
        """Extract all articles from the document content."""
        articles = []
        
        # Split content by articles
        article_matches = list(self.utils.article_pattern.finditer(content))
        
        for i, match in enumerate(article_matches):
            # Extract article number from the appropriate capture group
            # Updated for 16-group pattern with case-insensitive support:
            # UPPERCASE patterns (Groups 1-8, preserved for backwards compatibility):
            # Group 1: [Art.] [NUMBER]. format (with brackets)
            # Group 2: [Art.] NUMBER. format (without brackets) - FIXED: captures Article 57
            # Group 3: [Art.] N. format (placeholder)
            # Group 4: [Art.] NUMBER\. format (literal backslash-period) - NEW: captures Article 3
            # Group 5: Art. [NUMBER] format (without brackets around Art) - NEW
            # Group 6: Article [NUMBER]. format
            # Group 7: Article NUMBER\. format (without brackets)
            # Group 8: [}Art.] [NUMBER] format (malformed brackets from TITLE conversion)
            # LOWERCASE patterns (Groups 9-16, case-insensitive equivalents):
            # Group 9: [art.] [NUMBER]. format
            # Group 10: [art.] NUMBER. format
            # Group 11: [art.] N. format
            # Group 12: [art.] NUMBER\. format
            # Group 13: art. [NUMBER] format
            # Group 14: article [NUMBER]. format
            # Group 15: article NUMBER\. format
            # Group 16: [}art.] [NUMBER] format (malformed brackets with lowercase)
            article_number = (match.group(1) or match.group(2) or match.group(3) or match.group(4) or
                            match.group(5) or match.group(6) or match.group(7) or match.group(8) or
                            match.group(9) or match.group(10) or match.group(11) or match.group(12) or
                            match.group(13) or match.group(14) or match.group(15) or match.group(16))
            start_pos = match.end()
            
            # Find the end position (start of next article, next **TITLE** marker, **ANNEXE** marker, document section marker, or end of content)
            # FIXED: Use start of next article as boundary, not include it in current article content
            next_article_pos = article_matches[i + 1].start() if i + 1 < len(article_matches) else len(content)

            # Look for boundary markers between current article and next article
            search_content = content[start_pos:next_article_pos]

            # Check for **TITLE** markers
            title_matches = list(self.utils.title_pattern.finditer(search_content))

            # Check for **ANNEXE** markers
            annexe_pattern = re.compile(r'\*\*ANNEXE\*\*\[([^\]]+)\]')
            annexe_matches = list(annexe_pattern.finditer(search_content))

            # Check for document section markers like [12A] ## Travaux parlementaires [12B]
            section_pattern = re.compile(r'\[\d+[A-Z]\]\s*##\s*[^[]+\[\d+[A-Z]\]')
            section_matches = list(section_pattern.finditer(search_content))

            # Find the earliest boundary marker
            boundary_positions = []
            if title_matches:
                boundary_positions.append(title_matches[0].start())
            if annexe_matches:
                boundary_positions.append(annexe_matches[0].start())
            if section_matches:
                boundary_positions.append(section_matches[0].start())

            if boundary_positions:
                # Stop at the earliest boundary marker
                end_pos = start_pos + min(boundary_positions)
            else:
                # No boundary markers found, use next article position
                end_pos = next_article_pos

            article_text = content[start_pos:end_pos].strip()
            
            # Split content and footnotes
            main_content, footnotes = self.footnote_processor.split_article_content_and_footnotes(article_text, article_number)
            
            # Extract footnote references from main content
            footnote_references = self.footnote_processor.extract_footnote_references_from_text(main_content, article_number)
            
            # Parse numbered provisions
            numbered_provisions = self.parse_numbered_provisions(main_content)
            
            # Create main text (content without footnote references for clean display)
            main_text = self._clean_footnote_references_intelligently(main_content, footnote_references)

            # Extract legal citation markers from the beginning of article text (existing functionality)
            main_text, legal_citation = self._extract_legal_citation_markers(main_text)

            # Unescape markdown escape sequences to prevent double-escaping in JSON
            main_text = self.utils.unescape_markdown_sequences(main_text)

            # Store the original text as main_text_raw BEFORE citation processing
            main_text_raw = main_text.strip()

            # Enhanced citation processing - extract all citations throughout the article content
            # This creates HTML spans for display but doesn't modify the raw text
            enhanced_citations = []
            main_text_with_citation_spans = main_text  # Copy for HTML processing
            if self.enhanced_citation_parser:
                try:
                    # Process text to replace citations with HTML spans and get citation metadata
                    main_text_with_citation_spans, enhanced_citations = self.enhanced_citation_parser.process_text_with_citations(main_text)
                    if enhanced_citations:
                        logger.debug(f"Found {len(enhanced_citations)} enhanced citations in article {article_number}")
                except Exception as e:
                    logger.warning(f"Error in enhanced citation processing for article {article_number}: {e}")

            # Extract regional information and create unique article number
            # Check both the article header (match text) and content for regional markers
            article_header = match.group(0)  # The matched article header text
            regional_suffix = self._extract_regional_suffix(main_content)
            if not regional_suffix:
                # If not found in content, check the article header (for TITLE articles)
                regional_suffix = self._extract_regional_suffix(article_header)
            if regional_suffix:
                # Create unique article number with regional information
                # Clean up any extra spaces and ensure single space between number and region
                unique_article_number = f"{article_number} {regional_suffix.strip()}"
                unique_anchor_id = f"art_{article_number}_{regional_suffix.strip().replace(' ', '_')}"

                # Remove redundant regional text from main content if it's already in the article number
                main_content = self._remove_redundant_regional_text(main_content, regional_suffix)
            else:
                # No regional variation, use original number
                unique_article_number = article_number
                unique_anchor_id = f"art_{article_number}"

            # Detect abrogation status for entire article
            abrogation_status = self._detect_article_abrogation_status(main_text)

            # Build article content structure with optional legal citation
            article_content = {
                "main_text_raw": main_text_raw,  # Use original text with angle brackets
                "numbered_provisions": numbered_provisions
            }

            # Add abrogation status if detected
            if abrogation_status:
                article_content["abrogation_status"] = abrogation_status

            # Add HTML generation for structured content
            try:
                # Create article data structure for HTML generator
                article_data = {
                    'article_content': {
                        'article_number': unique_article_number,
                        'content': {
                            'main_text_raw': main_text_with_citation_spans.strip(),  # Use processed text with citation spans for HTML
                            'numbered_provisions': numbered_provisions
                        }
                    },
                    'footnotes': footnotes,
                    'footnote_references': footnote_references
                }

                # Generate HTML with document_id for preserved tables
                structured_html = self.html_generator.generate_article_html(article_data, document_id)

                # Clean HTML for JSON storage (remove newlines and extra whitespace)
                cleaned_html = self._clean_html_for_json(structured_html)

                # Add HTML and metadata to article content (renamed fields)
                article_content['main_text'] = cleaned_html
                article_content['structured_content_metadata'] = {
                    'paragraph_count': structured_html.count('<section class="paragraph"'),
                    'provision_count': len(numbered_provisions),
                    'has_tables': 'table' in main_text.lower(),
                    'generation_timestamp': __import__('datetime').datetime.now().isoformat()
                }

            except Exception as e:
                logger.warning(f"HTML generation failed for article {unique_article_number}: {e}")
                # Continue without structured content - backwards compatibility maintained

            # Add legal citation if present
            if legal_citation:
                article_content["legal_citation"] = legal_citation

            # Add enhanced citations if found
            if enhanced_citations:
                article_content["enhanced_citations"] = enhanced_citations

            # Add regional information if present
            if regional_suffix:
                article_content["region"] = regional_suffix.lstrip('-')

            article = {
                "article_number": unique_article_number,  # Use unique number with regional info
                "anchor_id": unique_anchor_id,
                "content": article_content,
                "footnote_references": footnote_references,
                "footnotes": footnotes,
                "parent_structure": {
                    "chapter": "",
                    "section": "",
                    "paragraph": ""
                },
                # Add top-level fields for backward compatibility with MD8
                "structured_content_html": article_content.get('main_text', ''),
                "structured_content_metadata": article_content.get('structured_content_metadata', {})
            }
            
            articles.append(article)

        return articles

    def _clean_html_for_json(self, html: str) -> str:
        """Clean HTML for JSON storage by removing newlines and normalizing whitespace."""
        if not html:
            return ""

        # Remove all newline characters (both \n and \r\n)
        cleaned = html.replace('\n', ' ').replace('\r', '')

        # Normalize multiple spaces to single spaces
        import re
        cleaned = re.sub(r'\s+', ' ', cleaned)

        # Remove spaces around HTML tags to make it more compact
        cleaned = re.sub(r'>\s+<', '><', cleaned)

        # Trim leading/trailing whitespace
        cleaned = cleaned.strip()

        return cleaned

    def populate_tree_with_articles(self, tree_nodes: List[Dict[str, Any]], articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Populate the tree structure with actual article content.

        Args:
            tree_nodes: The hierarchical tree structure from parse_table_of_contents_to_tree
            articles: List of extracted articles with full content

        Returns:
            Updated tree structure with article content embedded
        """
        # Create a mapping of base article numbers to lists of article objects
        # This handles cases where multiple articles have the same base number (e.g., regional variations)
        # We extract the base number from unique numbers like "1 WALLONNE" -> "1"
        article_map = {}
        for article in articles:
            full_article_number = article.get("article_number", "")
            # Extract base article number (everything before the first space)
            base_article_number = full_article_number.split()[0] if full_article_number else ""

            if base_article_number not in article_map:
                article_map[base_article_number] = []
            article_map[base_article_number].append(article)

        # Keep track of which articles have been used to avoid reusing them
        used_articles = set()

        # Recursively populate tree nodes
        def populate_node(node):
            if node["type"] == "article":
                # Extract article numbers from the range
                article_range = node["metadata"].get("article_range", "")
                article_numbers = self.utils.parse_article_range(article_range)

                # Check if we got the special marker indicating malformed TOC
                if article_numbers == ["__EXTRACT_ALL_ARTICLES__"]:
                    # Table of contents is malformed, but we should still try to extract
                    # all articles found in the document. Use all available articles.
                    logger.warning(f"Malformed table of contents entry, falling back to extracting all available articles")
                    article_numbers = list(article_map.keys())

                if len(article_numbers) == 1:
                    # Single article - embed the full article object
                    article_num = article_numbers[0]

                    # Try to find exact match first (for articles with regional suffixes)
                    if article_num in article_map:
                        article_list = article_map[article_num]
                    else:
                        # Look for articles that match this range (including suffixed versions)
                        matching_key = None
                        for key in article_map.keys():
                            # Use the new article_matches_range method to handle suffixed articles
                            if self.utils.article_matches_range(key, article_numbers):
                                # For regional articles, prefer the one that matches the regional pattern
                                if '(REGION' in article_num:
                                    # Extract region from tree structure format
                                    if 'WALLONNE' in article_num and 'WALLONNE' in key:
                                        matching_key = key
                                        break
                                    elif 'BRUXELLES' in article_num and 'BRUXELLES' in key:
                                        matching_key = key
                                        break
                                    elif 'FLAMANDE' in article_num and 'FLAMANDE' in key:
                                        matching_key = key
                                        break
                                else:
                                    # For non-regional articles, take the first match
                                    matching_key = key
                                    break

                        if matching_key and matching_key in article_map:
                            article_list = article_map[matching_key]
                        else:
                            # Final fallback - try base article number extraction
                            base_article_num = article_num.split()[0] if article_num else ""
                            base_article_num = base_article_num.rstrip('.').split('(')[0].strip()
                            if base_article_num in article_map:
                                article_list = article_map[base_article_num]
                            else:
                                article_list = None

                    if article_list:
                        # Find the first unused article with this number
                        article_obj = None
                        for i, candidate in enumerate(article_list):
                            article_id = id(candidate)  # Use object ID as unique identifier
                            if article_id not in used_articles:
                                article_obj = candidate
                                used_articles.add(article_id)
                                break

                        if article_obj:
                            # Update the label to match the unique article number
                            unique_article_number = article_obj.get("article_number")
                            node["label"] = f"Article {unique_article_number}"

                            # Update metadata.article_range to match the complete article identifier
                            # This ensures consistency between metadata.article_range and article_content.article_number
                            node["metadata"]["article_range"] = unique_article_number

                            node["article_content"] = {
                                "article_number": unique_article_number,
                                "anchor_id": article_obj.get("anchor_id"),
                                "content": article_obj.get("content", {})
                            }
                            node["footnotes"] = article_obj.get("footnotes", [])
                            node["footnote_references"] = article_obj.get("footnote_references", [])
                        else:
                            logger.warning(f"No more unused Article {article_num} objects available")
                    else:
                        logger.warning(f"Article {article_num} not found in extracted articles")
                else:
                    # Multiple articles - create child nodes for each
                    node["children"] = []
                    for article_num in article_numbers:
                        # Extract base article number for matching (same logic as article map building)
                        base_article_num = article_num.split()[0] if article_num else ""
                        if base_article_num in article_map:
                            article_list = article_map[base_article_num]

                            # Find the first unused article with this number
                            article_obj = None
                            for candidate in article_list:
                                article_id = id(candidate)  # Use object ID as unique identifier
                                if article_id not in used_articles:
                                    article_obj = candidate
                                    used_articles.add(article_id)
                                    break

                            if article_obj:
                                # Use the unique article number for the label
                                unique_article_number = article_obj.get("article_number")
                                child_node = {
                                    "type": "article",
                                    "label": f"Article {unique_article_number}",
                                    "metadata": {
                                        "article_range": article_num,  # Keep original for metadata
                                        "rank": 5
                                    },
                                    "article_content": {
                                        "article_number": unique_article_number,
                                        "anchor_id": article_obj.get("anchor_id"),
                                        "content": article_obj.get("content", {})
                                    },
                                    "footnotes": article_obj.get("footnotes", []),
                                    "footnote_references": article_obj.get("footnote_references", [])
                                }
                                node["children"].append(child_node)
                            else:
                                logger.warning(f"No more unused Article {article_num} objects available")
                        else:
                            logger.warning(f"Article {article_num} not found in extracted articles")
            else:
                # Recursively process children
                for child in node.get("children", []):
                    populate_node(child)

        # Process all root nodes
        for node in tree_nodes:
            populate_node(node)

        return tree_nodes

    def extract_articles_with_tree_structure(self, content: str, document_id: str = None) -> List[Dict[str, Any]]:
        """Extract articles and organize them in hierarchical tree structure.

        This method parses the actual document content structure to create
        a complete tree structure with embedded article content.

        Returns:
            List of root-level tree nodes with articles embedded as leaf nodes
        """
        # First, extract all articles using existing logic (preserves all functionality)
        articles = self.extract_articles(content, document_id)
        logger.info(f"Extracted {len(articles)} articles using existing logic")

        # Parse actual document content into tree structure
        try:
            from .hierarchy_parser import HierarchyParser
        except ImportError:
            from hierarchy_parser import HierarchyParser
        hierarchy_parser = HierarchyParser(self.utils)
        tree_structure = hierarchy_parser.parse_document_content_to_tree(content)

        # Populate tree with article content
        populated_tree = self.populate_tree_with_articles(tree_structure, articles)

        logger.info(f"Created hierarchical tree structure with {len(populated_tree)} root nodes")
        return populated_tree

    def _clean_footnote_references_intelligently(self, text: str, footnote_references: List[Dict[str, Any]]) -> str:
        """
        Comprehensively clean all footnote references and markers from text.
        Enhanced to handle Belgian legal document footnote patterns completely.
        """
        import re

        logger.info(f"Starting comprehensive footnote cleaning for text with {len(footnote_references)} footnote references")
        original_text = text
        cleaned_text = text

        # Strategy 1: Clean legal citation markers first (they often contain footnote numbers)
        cleaned_text = self._clean_legal_citation_markers(cleaned_text)

        # Strategy 2: Clean known footnote patterns from footnote_references
        if footnote_references:
            cleaned_text = self._clean_known_footnote_patterns(cleaned_text, footnote_references)

        # Strategy 3: Clean any remaining Belgian footnote patterns with comprehensive regex
        cleaned_text = self._clean_remaining_footnote_patterns(cleaned_text)

        # Strategy 4: Final cleanup of any orphaned brackets or markers
        cleaned_text = self._final_cleanup_orphaned_markers(cleaned_text)

        # Log cleaning results
        if original_text != cleaned_text:
            logger.info(f"✅ Footnote cleaning successful. Text length: {len(original_text)} → {len(cleaned_text)}")
            logger.debug(f"Original preview: {original_text[:100]}...")
            logger.debug(f"Cleaned preview: {cleaned_text[:100]}...")
        else:
            logger.info("ℹ️ No footnote markers found to clean")

        return cleaned_text

    def _remove_table_content_from_main_text(self, text: str) -> str:
        """
        Remove table content from main text for clean display.
        This ensures tables don't appear in both main_text and as separate table sections.
        """
        if not text:
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

    def _clean_legal_citation_markers(self, text: str) -> str:
        """
        Remove legal citation markers that are footnote references, but preserve
        legal citations that are part of the main article content (like insertion notices).

        Only removes legal citations that are clearly footnote markers:
        - Preceded by footnote numbers like (1)<L ...>
        - Not legitimate article modification notices
        """
        import re

        # Pattern for footnote-style legal citations: (NUMBER)<TYPE [date](url), details>
        # This removes legal citations that are clearly footnote references
        footnote_legal_citation_pattern = re.compile(
            r'\(\d+\)<(?:Inséré par\s+)?[A-Z]+\s+\[[^\]]+\]\([^)]+\)[^>]*(?:\*\*En vigueur\s*:\*\*[^>]*)?>',
            re.IGNORECASE | re.DOTALL
        )

        cleaned_text = footnote_legal_citation_pattern.sub('', text)

        if cleaned_text != text:
            logger.debug(f"✅ Removed footnote-style legal citation markers")
        else:
            logger.debug(f"ℹ️ No footnote-style legal citations found to remove")

        return cleaned_text

    def _clean_known_footnote_patterns(self, text: str, footnote_references: List[Dict[str, Any]]) -> str:
        """
        Clean footnote patterns that were identified during footnote extraction.
        Enhanced to ensure proper spacing between preceding words and footnote content.
        """
        cleaned_text = text
        successful_replacements = 0

        # Sort by pattern length (longest first) to handle nested patterns correctly
        sorted_refs = sorted(footnote_references, key=lambda x: len(x.get("bracket_pattern", "")), reverse=True)

        for ref in sorted_refs:
            pattern = ref.get("bracket_pattern", "")
            content = ref.get("referenced_text", "").strip()

            if pattern and pattern in cleaned_text:
                # Find the pattern in the text and check for proper spacing
                pattern_start = cleaned_text.find(pattern)
                if pattern_start > 0:
                    # Check if there's a word character immediately before the pattern
                    preceding_char = cleaned_text[pattern_start - 1]
                    if preceding_char.isalnum():
                        # Add space between word and footnote content
                        replacement = f" {content}"
                    else:
                        # Keep original content if there's already proper spacing
                        replacement = content
                else:
                    # Pattern at start of text
                    replacement = content

                # Replace the footnote pattern with properly spaced content
                cleaned_text = cleaned_text.replace(pattern, replacement, 1)
                successful_replacements += 1
                logger.debug(f"✅ Cleaned known footnote pattern for ref {ref.get('reference_number', 'unknown')}")

        logger.info(f"Cleaned {successful_replacements}/{len(footnote_references)} known footnote patterns")
        return cleaned_text

    def _clean_remaining_footnote_patterns(self, text: str) -> str:
        """
        Clean any remaining Belgian footnote patterns using comprehensive regex patterns.
        """
        import re

        cleaned_text = text
        patterns_cleaned = 0

        # Belgian footnote patterns to clean (including malformed patterns with HTML artifacts)
        footnote_patterns = [
            # Format: [NUMBER content][NUMBER] - Belgian nested footnote format
            r'\[(\d+)\s+([^\]]+)\]\1',
            # Format: [NUMBER] content ][NUMBER] - Belgian spaced footnote format
            r'\[(\d+)\]\s*([^\]]+)\]\[?\1\]?',
            # Malformed footnote patterns with HTML/markdown artifacts - VERY SPECIFIC
            r'\[(\d+)\]>"\)\s*([^,\]]{1,50}),?\]\[?\1?\]?>"\)',  # [1]>") content,][1]>") - limited content length
            r'\[(\d+)\]>"\)\s*([^,\]]{1,30})',  # [1]>") content - limited content length
            r'\]\[(\d+)\]>"\)',  # ][1]>") - exact pattern only
            # Simple footnote references: [1], [2], etc.
            r'\[(\d+)\]',
            # Orphaned closing brackets with numbers: ]1, ]2, etc.
            r'\](\d+)',
            # Double brackets: ][NUMBER]
            r'\]\[(\d+)\]',
            # HTML/markdown artifacts - VERY SPECIFIC to avoid removing content
            r'>"\)',  # Orphaned >") - exact pattern only
        ]

        for pattern in footnote_patterns:
            matches = list(re.finditer(pattern, cleaned_text))
            if matches:
                # Process matches from end to start to maintain positions
                for match in reversed(matches):
                    # For patterns with content groups, keep the content
                    if match.lastindex and match.lastindex >= 2:
                        # Keep the content (group 2), remove the footnote markers
                        content = match.group(2).strip()

                        # Check if we need to add space before the content
                        replacement = content
                        if match.start() > 0:
                            preceding_char = cleaned_text[match.start() - 1]
                            if preceding_char.isalnum():
                                # Add space between word and footnote content
                                replacement = f" {content}"

                        cleaned_text = cleaned_text[:match.start()] + replacement + cleaned_text[match.end():]
                    else:
                        # Just remove the footnote marker
                        cleaned_text = cleaned_text[:match.start()] + cleaned_text[match.end():]
                    patterns_cleaned += 1

        if patterns_cleaned > 0:
            logger.info(f"✅ Cleaned {patterns_cleaned} remaining footnote patterns")

        return cleaned_text

    def _final_cleanup_orphaned_markers(self, text: str) -> str:
        """
        Final cleanup of any orphaned brackets, extra spaces, and formatting issues.
        """
        import re

        cleaned_text = text

        # Clean up orphaned brackets and markers
        cleanup_patterns = [
            # Multiple consecutive spaces
            (r'\s{2,}', ' '),
            # Orphaned closing brackets at start of text
            (r'^\s*\]\s*', ''),
            # Orphaned opening brackets at end of text
            (r'\s*\[\s*$', ''),
            # Empty bracket pairs
            (r'\[\s*\]', ''),
            # Spaces before punctuation
            (r'\s+([.,:;!?])', r'\1'),
            # Multiple newlines
            (r'\n{3,}', '\n\n'),
        ]

        for pattern, replacement in cleanup_patterns:
            old_text = cleaned_text
            cleaned_text = re.sub(pattern, replacement, cleaned_text)
            if old_text != cleaned_text:
                logger.debug(f"✅ Applied cleanup pattern: {pattern}")

        return cleaned_text.strip()

    def _extract_legal_citation_markers(self, text):
        """
        Extract legal citation markers from the beginning of article text.

        IMPORTANT: This method now preserves citations in the article content
        while still extracting metadata for backward compatibility.

        Citations like "Abrogé par" (repealed by) are critical legal information
        that users need to see in the article content.

        Returns:
            tuple: (original_text_preserved, legal_citation_dict or None)
        """
        if not text or not text.strip():
            return text, None

        text_stripped = text.strip()
        match = self.legal_citation_pattern.match(text_stripped)
        if not match:
            return text, None

        # Extract the citation content (without angle brackets)
        citation_content = match.group(1).strip()

        # PRESERVE the citation in the main text - do NOT remove it
        # This ensures important legal information like "Abrogé par" remains visible
        preserved_text = text_stripped

        # Extract URLs from the citation content using pre-compiled pattern
        urls = [url_match.group(1) for url_match in self.url_pattern.finditer(citation_content)]

        # Build legal citation structure for backward compatibility
        legal_citation = {
            "full_text": citation_content,
            "urls": urls
        }

        return preserved_text, legal_citation

    def _clean_with_regex_approach(self, text: str, footnote_references: List[Dict[str, Any]]) -> str:
        """
        Use regex patterns to clean footnote references based on reference numbers.
        This handles cases where LLM breaks down complex nested footnotes.
        """
        import re
        cleaned_text = text

        # Group footnotes by reference number
        footnotes_by_number = {}
        for ref in footnote_references:
            ref_num = ref["reference_number"]
            if ref_num not in footnotes_by_number:
                footnotes_by_number[ref_num] = []
            footnotes_by_number[ref_num].append(ref)

        # Process each footnote number
        for ref_num, refs in footnotes_by_number.items():
            # Try different regex patterns for this footnote number
            patterns_to_try = [
                # Format A: [NUMBER] content][NUMBER]
                rf'\[{re.escape(ref_num)}\](.*?)\]{re.escape(ref_num)}',
                # Format B: [NUMBER content]NUMBER
                rf'\[{re.escape(ref_num)}\s+(.*?)\]{re.escape(ref_num)}',
                # Nested format: [NUMBER content [OTHER] content][NUMBER]
                rf'\[{re.escape(ref_num)}\](.*?)\]{re.escape(ref_num)}',
            ]

            for pattern in patterns_to_try:
                matches = list(re.finditer(pattern, cleaned_text, re.DOTALL))
                if matches:
                    # Replace from last to first to maintain positions
                    for match in reversed(matches):
                        content = match.group(1).strip()
                        cleaned_text = cleaned_text[:match.start()] + content + cleaned_text[match.end():]
                        logger.debug(f"✅ Regex replacement successful for footnote {ref_num}")
                    break

        return cleaned_text

    def _clean_with_sequential_approach(self, text: str, footnote_references: List[Dict[str, Any]]) -> str:
        """
        Sequential approach: process footnotes from shortest to longest pattern.
        This handles deeply nested footnote structures.
        """
        cleaned_text = text

        # Sort footnotes by pattern length (shortest first) to handle nesting
        sorted_refs = sorted(footnote_references, key=lambda x: len(x["bracket_pattern"]))

        for ref in sorted_refs:
            pattern = ref["bracket_pattern"]
            content = ref["referenced_text"]

            # Try exact match first
            if pattern in cleaned_text:
                cleaned_text = cleaned_text.replace(pattern, content, 1)
                logger.debug(f"✅ Sequential replacement successful for footnote {ref['reference_number']}")
            else:
                # Try fuzzy matching for slight variations
                import difflib
                # Find the closest match in the text
                text_chunks = [cleaned_text[i:i+len(pattern)] for i in range(len(cleaned_text) - len(pattern) + 1)]
                closest_matches = difflib.get_close_matches(pattern, text_chunks, n=1, cutoff=0.8)

                if closest_matches:
                    closest_match = closest_matches[0]
                    cleaned_text = cleaned_text.replace(closest_match, content, 1)
                    logger.debug(f"✅ Fuzzy replacement successful for footnote {ref['reference_number']}")

        return cleaned_text

    def _still_has_footnote_markers(self, text: str) -> bool:
        """Check if text still contains footnote reference markers."""
        import re
        # Look for patterns like [NUMBER] or [NUMBER text]NUMBER
        footnote_pattern = r'\[\d+[^\]]*\]\d*|\[\d+\s+[^\]]*\]\d+'
        return bool(re.search(footnote_pattern, text))
