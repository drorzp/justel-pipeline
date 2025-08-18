"""
Enhanced Legal Citation Parser for Belgian Legal Documents

This module provides comprehensive parsing of legal citations that appear anywhere
within Belgian legal document content, including insertion notices, modifications,
and standard legal references.

Supports citation patterns like:
- <Inséré par L [1994-07-14/57], art. 2; En vigueur : 31-10-1994>
- <L [2008-12-22/33](https://www.ejustice.just.fgov.be/...), art. 105, 013; En vigueur : 08-01-2009>
- <intitulé modifié par L [2003-05-03/46], art. 2, 007; En vigueur : 02-06-2003>
"""

import re
import logging
from typing import List, Dict, Any, Optional, Tuple
from html import escape

logger = logging.getLogger(__name__)


class CitationParser:
    """
    Enhanced parser for legal citations in Belgian legal documents.
    
    Detects and parses legal citations anywhere within article content,
    extracting metadata for navigation and creating clickable HTML elements.
    """
    
    def __init__(self):
        """Initialize the citation parser with comprehensive regex patterns."""
        
        # Enhanced citation pattern to capture all citation types including regional citations
        # Groups: (1) prefix, (2) law_type, (3) dossier_brackets, (4) dossier_no_brackets, (5) url, (6) article, (7) sequence, (8) effective_date
        self.enhanced_citation_pattern = re.compile(
            r'<(?:(Inséré(?:\s+pour\s+la\s+Région\s+\w+)?\s+par|intitulé modifié par|Modifié par|Abrogé par|Remplacé par|modifié par)\s+)?'  # Optional prefix with regional support
            r'([A-Z]+)\s+'                                                                                # Law type (L, DRW, AR, etc.)
            r'(?:\[([^\]]+)\]|(\d{4}-\d{2}-\d{2}/\d+))'                                                  # Date in brackets OR without brackets
            r'(?:\(([^)]+)\))?'                                                                           # Optional URL in parentheses
            r'(?:,\s*art\.\s*([^,;]+))?'                                                                  # Optional article reference
            r'(?:,\s*([^;]+))?'                                                                           # Optional sequence/version
            r'(?:;\s*(?:\*\*)?En vigueur\s*:?\s*(?:\*\*)?([^>]+))?'                                     # Optional effective date
            r'>',
            re.IGNORECASE | re.DOTALL
        )
        
        # Pattern for extracting dossier number components
        self.dossier_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})/(\d+)', re.IGNORECASE)
        
        # Pattern for cleaning article numbers
        self.article_clean_pattern = re.compile(r'^\s*(\d+(?:[a-z]+)?(?:/\d+)?)\s*', re.IGNORECASE)
        
    def find_citations_in_text(self, text: str) -> List[Dict[str, Any]]:
        """
        Find all legal citations in the given text.
        
        Args:
            text: Text content to search for citations
            
        Returns:
            List of citation dictionaries with metadata and position information
        """
        citations = []
        
        for match in self.enhanced_citation_pattern.finditer(text):
            try:
                citation_data = self._parse_citation_match(match)
                if citation_data:
                    # Add position information
                    citation_data.update({
                        'start_pos': match.start(),
                        'end_pos': match.end(),
                        'matched_text': match.group(0)
                    })
                    citations.append(citation_data)
                    
            except Exception as e:
                logger.warning(f"Error parsing citation at position {match.start()}: {e}")
                continue
                
        return citations
    
    def _parse_citation_match(self, match: re.Match) -> Optional[Dict[str, Any]]:
        """
        Parse a regex match into citation metadata.
        
        Args:
            match: Regex match object from enhanced_citation_pattern
            
        Returns:
            Dictionary with parsed citation metadata or None if parsing fails
        """
        try:
            # Extract groups (updated for new pattern with optional brackets)
            prefix = match.group(1)  # "Inséré par", "modifié par", etc.
            law_type = match.group(2)  # "L", "DRW", "AR", etc.
            dossier_brackets = match.group(3)  # "2008-12-22/33" (in brackets)
            dossier_no_brackets = match.group(4)  # "1996-07-18/49" (no brackets)
            url = match.group(5)  # Full URL if present
            article_raw = match.group(6)  # "105", "2", etc.
            sequence = match.group(7)  # "013", "007", etc.
            effective_date = match.group(8)  # "08-01-2009"

            # Use whichever dossier format was found
            dossier_raw = dossier_brackets if dossier_brackets else dossier_no_brackets
            
            # Parse dossier number
            dossier_number = self._parse_dossier_number(dossier_raw)
            
            # Parse article number
            article_number = self._parse_article_number(article_raw)
            
            # Determine citation type
            citation_type = self._determine_citation_type(prefix)
            
            # Clean effective date
            effective_date_cleaned = self._clean_effective_date(effective_date)
            
            # Build citation data
            citation_data = {
                'citation_type': citation_type,
                'law_type': law_type.upper() if law_type else '',
                'dossier_number': dossier_number,
                'article_number': article_number,
                'sequence_number': sequence.strip() if sequence else '',
                'effective_date': effective_date_cleaned,
                'url': url.strip() if url else '',
                'full_text': match.group(0),
                'prefix': prefix.strip() if prefix else '',
                'raw_dossier': dossier_raw.strip() if dossier_raw else '',
                'raw_article': article_raw.strip() if article_raw else ''
            }
            
            return citation_data
            
        except Exception as e:
            logger.warning(f"Error parsing citation match: {e}")
            return None
    
    def _parse_dossier_number(self, dossier_raw: str) -> str:
        """
        Parse and clean dossier number.
        
        Args:
            dossier_raw: Raw dossier string like "2008-12-22/33"
            
        Returns:
            Cleaned dossier number
        """
        if not dossier_raw:
            return ''
            
        # Extract standard dossier format YYYY-MM-DD/NN
        match = self.dossier_pattern.search(dossier_raw)
        if match:
            return f"{match.group(1)}/{match.group(2)}"
        
        # Return cleaned raw if no standard format found
        return dossier_raw.strip()
    
    def _parse_article_number(self, article_raw: str) -> str:
        """
        Parse and clean article number.
        
        Args:
            article_raw: Raw article string like "105", "2bis", "3/1"
            
        Returns:
            Cleaned article number
        """
        if not article_raw:
            return ''
            
        # Extract article number (handles numbers with suffixes and fractions)
        match = self.article_clean_pattern.search(article_raw)
        if match:
            return match.group(1)
        
        # Return cleaned raw if no standard format found
        return article_raw.strip()
    
    def _determine_citation_type(self, prefix: str) -> str:
        """
        Determine the type of citation based on prefix.
        
        Args:
            prefix: Citation prefix like "Inséré par", "modifié par", etc.
            
        Returns:
            Citation type: 'insertion', 'modification', 'abrogation', 'replacement', or 'standard'
        """
        if not prefix:
            return 'standard'
            
        prefix_lower = prefix.lower()
        
        if 'inséré' in prefix_lower:
            return 'insertion'
        elif 'modifié' in prefix_lower:
            return 'modification'
        elif 'abrogé' in prefix_lower:
            return 'abrogation'
        elif 'remplacé' in prefix_lower:
            return 'replacement'
        else:
            return 'modification'  # Default for other modification types
    
    def _clean_effective_date(self, date_raw: str) -> str:
        """
        Clean and format effective date.
        
        Args:
            date_raw: Raw date string like "08-01-2009" or "**08-01-2009**"
            
        Returns:
            Cleaned date string
        """
        if not date_raw:
            return ''
            
        # Remove markdown formatting and extra whitespace
        cleaned = date_raw.replace('**', '').strip()
        
        # Remove any trailing punctuation
        cleaned = cleaned.rstrip('.,;')
        
        return cleaned
    
    def create_citation_html(self, citation_data: Dict[str, Any], preserve_original: bool = True) -> str:
        """
        Create HTML for a clickable citation element.

        Args:
            citation_data: Citation metadata dictionary
            preserve_original: Whether to preserve original citation text

        Returns:
            HTML string for clickable citation element
        """
        # Build data attributes (always include all attributes, even if empty)
        data_attrs = []

        data_attrs.append(f'data-citation-type="{escape(citation_data.get("citation_type", ""))}"')
        data_attrs.append(f'data-dossier-number="{escape(citation_data.get("dossier_number", ""))}"')
        data_attrs.append(f'data-article-number="{escape(citation_data.get("article_number", ""))}"')
        data_attrs.append(f'data-law-type="{escape(citation_data.get("law_type", ""))}"')
        data_attrs.append(f'data-effective-date="{escape(citation_data.get("effective_date", ""))}"')

        if citation_data.get('url'):
            data_attrs.append(f'data-citation-url="{escape(citation_data["url"])}"')

        # Determine CSS class based on citation type
        css_class = f"legal-citation legal-citation-{citation_data.get('citation_type', 'standard')}"

        # Build HTML
        attrs_str = ' '.join(data_attrs)
        if attrs_str:
            attrs_str = ' ' + attrs_str

        # Create clean display text without URLs
        display_text = self._create_clean_display_text(citation_data)
        # Escape the display text for safe HTML output
        escaped_display_text = escape(display_text)

        return f'<span class="{css_class}"{attrs_str}>{escaped_display_text}</span>'

    def _create_clean_display_text(self, citation_data: Dict[str, Any]) -> str:
        """
        Create clean display text for citation with angle brackets but without URLs.

        Args:
            citation_data: Citation metadata dictionary

        Returns:
            Clean display text with angle brackets but without URLs
        """
        # Build clean display text from parsed components instead of using full_text
        # This preserves the angle brackets for proper legal citation formatting

        parts = []

        # Add prefix if present (e.g., "Inséré par", "modifié par")
        prefix = citation_data.get('prefix', '').strip()
        if prefix:
            parts.append(prefix)

        # Add law type and dossier
        law_type = citation_data.get('law_type', '').strip()
        dossier = citation_data.get('dossier_number', '').strip()
        if law_type and dossier:
            parts.append(f"{law_type} {dossier}")

        # Add article if present
        article = citation_data.get('article_number', '').strip()
        if article:
            parts.append(f"art. {article}")

        # Add sequence number if present
        sequence = citation_data.get('sequence_number', '').strip()
        if sequence:
            parts.append(sequence)

        # Add effective date if present
        effective_date = citation_data.get('effective_date', '').strip()
        if effective_date:
            parts.append(f"En vigueur : {effective_date}")

        # Join parts with appropriate separators
        if len(parts) <= 1:
            citation_content = ', '.join(parts)
        else:
            # Join most parts with ", " and add "; " before the effective date
            if effective_date and len(parts) > 1:
                main_parts = parts[:-1]
                citation_content = ', '.join(main_parts) + '; ' + parts[-1]
            else:
                citation_content = ', '.join(parts)

        # Wrap the citation content in angle brackets for proper legal formatting
        return f"<{citation_content}>"

    def process_text_with_citations(self, text: str) -> Tuple[str, List[Dict[str, Any]]]:
        """
        Process text to replace citations with clickable HTML elements.
        
        Args:
            text: Original text content
            
        Returns:
            Tuple of (processed_text, citations_list)
        """
        citations = self.find_citations_in_text(text)
        
        if not citations:
            return text, []
        
        # Sort citations by position (reverse order for replacement)
        citations_sorted = sorted(citations, key=lambda x: x['start_pos'], reverse=True)
        
        processed_text = text
        
        # Replace citations with HTML elements (from end to start to preserve positions)
        for citation in citations_sorted:
            start_pos = citation['start_pos']
            end_pos = citation['end_pos']
            
            # Create HTML element
            citation_html = self.create_citation_html(citation)
            
            # Replace in text
            processed_text = processed_text[:start_pos] + citation_html + processed_text[end_pos:]
        
        return processed_text, citations
