#!/usr/bin/env python3
"""
footnote_processor.py - Footnote processing for Belgian Legal Documents

This module handles extraction and processing of footnotes and footnote references
from Belgian legal documents, including URL extraction and content parsing.

Author: Augment Agent
Date: 2025-07-13
"""

import re
import logging
from typing import Dict, List, Any, Optional, Tuple

# Handle both relative and absolute imports
try:
    from .extraction_utils import ExtractionUtils
except ImportError:
    from extraction_utils import ExtractionUtils

logger = logging.getLogger(__name__)


class FootnoteProcessor:
    """
    Processes footnotes and footnote references from Belgian legal documents.
    """
    
    def __init__(self, utils: ExtractionUtils):
        """Initialize with utility functions."""
        self.utils = utils

    def extract_footnote_references_from_text(self, text: str, article_number: str = "") -> List[Dict[str, Any]]:
        """Extract Belgian footnote references from article text."""
        references = []
        matches = self.utils.footnote_reference_pattern.finditer(text)

        for match in matches:
            # Handle alternation pattern: Format A uses groups (1,2,3), Format B uses groups (4,5,6)
            if match.group(1):  # Format A: [NUMBER] text][NUMBER]
                ref_number = match.group(1)
                ref_text = match.group(2)
                trailing_number = match.group(3)
            else:  # Format B: [NUMBER text]NUMBER
                ref_number = match.group(4)
                ref_text = match.group(5)
                trailing_number = match.group(6)

            if ref_number == trailing_number:  # Valid Belgian footnote format
                reference = {
                    "reference_number": ref_number,
                    "text_position": match.start(),
                    "referenced_text": ref_text.strip(),
                    "embedded_law_references": [],
                    "bracket_pattern": match.group(0)
                }
                references.append(reference)

        return references

    def extract_footnote_urls(self, footnote_content: str, law_url: str, article_number: str) -> Tuple[str, str]:
        """
        Extract direct_url and direct_article_url from footnote content.

        Args:
            footnote_content: The full footnote content text
            law_url: The URL extracted from the legal citation pattern
            article_number: The article number where this footnote appears

        Returns:
            Tuple of (direct_url, direct_article_url)
        """
        direct_url = ""
        direct_article_url = ""

        try:
            # Extract URL from footnote content using regex
            # Look for URLs in parentheses within the footnote content
            url_pattern = r'\((https://www\.ejustice\.just\.fgov\.be/[^)]+)\)'
            url_match = re.search(url_pattern, footnote_content)

            if url_match:
                direct_url = url_match.group(1)
            elif law_url:
                # Fallback to law_url if no URL found in content
                direct_url = law_url

            # Create direct_article_url by appending article anchor
            if direct_url and article_number:
                # Ensure proper URL formatting and add article anchor
                if direct_url.endswith('/'):
                    direct_url = direct_url.rstrip('/')
                direct_article_url = f"{direct_url}#Art.{article_number}"

        except Exception as e:
            logger.warning(f"Error extracting URLs from footnote: {e}")
            # Return empty strings on error
            direct_url = ""
            direct_article_url = ""

        return direct_url, direct_article_url

    def extract_footnotes_from_section(self, footnote_section: str, article_number: str = "") -> List[Dict[str, Any]]:
        """Extract footnotes from a footnote section with URL extraction."""
        footnotes = []

        # Find legal citations in footnote format
        citations = self.utils.legal_citation_pattern.finditer(footnote_section)

        for citation in citations:
            footnote_number = citation.group(1)
            law_type = citation.group(2)  # L, DRW, AR, etc.
            law_date = citation.group(3)
            law_url = citation.group(4)
            article_ref = citation.group(5)
            effective_date = citation.group(6)

            # Parse law reference first to get the referenced article number
            law_reference = {
                "law_type": law_type,  # Now captures actual type: L, DRW, AR, etc.
                "date_reference": law_date,
                "article_number": article_ref.split(',')[0].strip() if ',' in article_ref else article_ref,
                "sequence_number": article_ref.split(',')[1].strip() if ',' in article_ref else "",
                "full_reference": f"{law_type} [{law_date}]"
            }

            # Extract the referenced article number for URL generation
            referenced_article = law_reference["article_number"]
            # Clean up the article number (remove "art." prefix if present)
            if referenced_article.lower().startswith('art.'):
                referenced_article = referenced_article[4:].strip()
            elif referenced_article.lower().startswith('art '):
                referenced_article = referenced_article[4:].strip()

            # Extract URLs from footnote content using the referenced article number
            direct_url, direct_article_url = self.extract_footnote_urls(citation.group(0), law_url, referenced_article)

            footnote = {
                "footnote_number": footnote_number,
                "footnote_content": citation.group(0),
                "law_reference": law_reference,
                "effective_date": effective_date.strip(),
                "modification_type": "modification",  # Default, could be enhanced to detect type
                "direct_url": direct_url,
                "direct_article_url": direct_article_url
            }
            footnotes.append(footnote)

        return footnotes
    
    def split_article_content_and_footnotes(self, article_text: str, article_number: str = "") -> Tuple[str, List[Dict[str, Any]]]:
        """Split article text into main content and footnote section."""
        # Split by footnote separator
        parts = self.utils.footnote_separator.split(article_text, 1)

        main_content = parts[0].strip()
        footnotes = []

        if len(parts) > 1:
            footnote_section = parts[1].strip()
            footnotes = self.extract_footnotes_from_section(footnote_section, article_number)

        return main_content, footnotes
