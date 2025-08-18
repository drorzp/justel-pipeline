#!/usr/bin/env python3
"""
extraction_utils.py - Utility functions and regex patterns for Belgian Legal Document Processing

This module contains common utility functions, regex patterns, and helper methods
used across the Belgian legal document extraction pipeline.

Author: Augment Agent
Date: 2025-07-13
"""

import re
import logging
from typing import Dict, List, Any, Optional, Tuple

logger = logging.getLogger(__name__)


class ExtractionUtils:
    """
    Utility class containing regex patterns and helper functions for Belgian legal document extraction.
    """
    
    def __init__(self):
        """Initialize regex patterns for Belgian legal documents."""
        # Belgian footnote reference pattern - captures both valid footnote reference formats:
        # Format A: [NUMBER] text content][NUMBER] (space after number + bracket pair closing)
        # Format B: [NUMBER text content]NUMBER (no space + single number closing)
        # Both formats require matching opening and closing numbers to be valid footnote references
        self.footnote_reference_pattern = re.compile(r'\[(\d+)\]\s*([^\]]+)\]\[(\d+)\]|\[(\d+)\s+([^\]]+)\](\d+)')

        # Legal citation pattern for footnotes - comprehensive pattern for all citation types
        # Matches: (1)<L [date](url), art. X, Y; En vigueur : date>
        #          (1)<DRW [date](url), art. X, Y; En vigueur : date>
        #          (1)<AR [date](url), art. X, Y; En vigueur : date>
        #          (1)<Inséré par L [date](url), art. X, Y; En vigueur : date>
        self.legal_citation_pattern = re.compile(
            r'\((\d+)\)<(?:Inséré par\s+)?([A-Z]+)\s+\[([^\]]+)\]\(([^)]+)\),\s*([^;]+);\s*En vigueur\s*:\s*([^>]+)>'
        )

        # Article pattern - comprehensive regex to capture all article variations
        # Matches multiple formats with CASE-INSENSITIVE support for both Art. and art.:
        # 1. **ARTICLE**[Art.] [NUMBER]. (standard format with brackets)
        # 2. **ARTICLE**[Art.] NUMBER. (format without brackets around number, including slashes like 555/16)
        # 3. **ARTICLE**Article [NUMBER] (ordinal format like [1er])
        # 4. **ARTICLE**[Art.] N. (placeholder format)
        # 5. **ARTICLE**Article NUMBER\. (format without brackets like Article 50\.)
        # 6. **ARTICLE**[Art.] NUMBER\. (format with literal backslash-period like [Art.] 3\.) - NEW from output/22 analysis
        # 7. **ARTICLE**Art. [NUMBER] (format without brackets around Art like Art. [58]) - NEW from output/22 analysis
        # 8. **TITLE**[art.] variations (lowercase equivalents for all above patterns)
        # Enhanced article pattern matching - Claude Opus 4 improved approach
        # Multi-line format for better readability and maintainability
        # BACKWARDS COMPATIBLE: All original patterns preserved, with case-insensitive extensions
        self.article_pattern = re.compile(
            r'\*\*(?:ARTICLE|TITLE)\*\*(?:'
            # UPPERCASE Art. patterns (Groups 1-7, preserved for backwards compatibility)
            r'\[Art\.\]\s*\[([^\]]+)\]\.'  # Group 1: [Art.] [NUMBER].
            r'|\[Art\.\]\s*(\d+(?:\.\d+)*(?:/\d+)?(?:bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?)\.(?=\s|[A-Z])'  # Group 2: [Art.] NUMBER. (supports multi-decimal numbers like 8.39, 9.1.54)
            r'|\[Art\.\]\s*([A-Z]+\d*)\.?'  # Group 3: [Art.] N. or N3.
            r'|\[Art\.\]\s*(\d+(?:\.\d+)*(?:/\d+)?(?:er|e|eme|ème|bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?)\\\.'  # Group 4: [Art.] NUMBER\. (FIXED: single backslash, supports multi-decimal numbers)
            r'|Art\.\s*\[([^\]]+)\]\.?'  # Group 5: Art. [NUMBER]
            r'|Article\s*\[([^\]]+)\]\.'  # Group 6: Article [NUMBER].
            r'|Article\s*(\d+(?:\.\d+)*(?:er|e|eme|ème|bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?)\\\.'  # Group 7: Article NUMBER\. (FIXED: single backslash, supports multi-decimal numbers)
            # MALFORMED patterns (Groups 8-9, preserved for backwards compatibility)
            r'|\[}?Art\.\]\s*\[([^\]]+)\]'  # Group 8: [}Art.] [NUMBER] - handles malformed brackets from TITLE conversion
            # LOWERCASE art. patterns (Groups 9-15, case-insensitive equivalents)
            r'|\[art\.\]\s*\[([^\]]+)\]\.'  # Group 9: [art.] [NUMBER]. - UPDATED: added period for consistency
            r'|\[art\.\]\s*(\d+(?:\.\d+)*(?:/\d+)?(?:bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?)\.(?=\s|[A-Z])'  # Group 10: [art.] NUMBER. (supports multi-decimal numbers like 8.39, 9.1.54)
            r'|\[art\.\]\s*([A-Z]+\d*)\.?'  # Group 11: [art.] N. or N3.
            r'|\[art\.\]\s*(\d+(?:\.\d+)*(?:/\d+)?(?:er|e|eme|ème|bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?)\\\.'  # Group 12: [art.] NUMBER\. (supports multi-decimal numbers)
            r'|art\.\s*\[([^\]]+)\]\.?'  # Group 13: art. [NUMBER]
            r'|article\s*\[([^\]]+)\]\.'  # Group 14: article [NUMBER].
            r'|article\s*(\d+(?:\.\d+)*(?:er|e|eme|ème|bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?)\\\.'  # Group 15: article NUMBER\. (supports multi-decimal numbers)
            r'|\[}?art\.\]\s*\[([^\]]+)\]'  # Group 16: [}art.] [NUMBER] - handles malformed brackets with lowercase
            r')'
        )

        # Alternative robust pattern that handles both escaped and unescaped periods
        # This provides a fallback for edge cases and better debugging
        self.robust_article_pattern = re.compile(
            r'\*\*(?:ARTICLE|TITLE)\*\*(?:'
            # Standard formats with brackets
            r'\[Art\.\]\s*\[([^\]]+)\]\.'
            # [Art.] NUMBER with various endings (handles both . and \., supports multi-decimal numbers)
            r'|\[Art\.\]\s*(\d+(?:\.\d+)*(?:/\d+)?(?:er|e|eme|ème|bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?)(?:\\)?\.(?=\s|[A-Z]|$)'
            # Placeholder format (letters optionally followed by numbers)
            r'|\[Art\.\]\s*([A-Z]+\d*)\.?'
            # Art. without brackets around it
            r'|Art\.\s*\[([^\]]+)\]\.?'
            # Article formats
            r'|Article\s*\[([^\]]+)\]\.'
            r'|Article\s*(\d+(?:er|e|eme|ème|bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)?)(?:\\)?\.(?=\s|[A-Z]|$)'
            # Malformed brackets from TITLE conversion
            r'|\[}?Art\.\]\s*\[([^\]]+)\]'
            r'|\[art\.\]\s*\[([^\]]+)\]'
            r')'
        )

        # Document structure patterns - Updated to handle HTML format with proper entity handling
        # Updated to handle cases where title has no content after the type (e.g., **TITLE**[CHAPITRE Ier.])
        self.title_pattern = re.compile(r'\*\*TITLE\*\*\[([^\]]+)\]\s*(.*)')
        # Markdown format patterns for processed content - Updated to handle ** bold format and spaces in decoded entities
        # These patterns handle both HTML and Markdown formats, accounting for spaces in decoded HTML entities
        # Updated to handle both embedded format (in title) and separate line format (in document body)
        self.publication_date_pattern = re.compile(r'(?:<strong>|\*\*)Publication:\s*(?:</strong>|\*\*)\s*([^<\n*]+?)(?=\*\*|<|$|\n)', re.IGNORECASE)
        self.page_pattern = re.compile(r'(?:<strong>|\*\*)page:\s*(?:</strong>|\*\*)\s*([^<\n*]+?)(?=\s*\*\*|<|$|\n)', re.IGNORECASE)
        # Updated to handle spaces in "num ero" from HTML entity decoding
        self.dossier_pattern = re.compile(r'(?:<strong>|\*\*)Dossier\s+num\s*(?:&eacute;|é|e)?\s*ro:\s*(?:</strong>|\*\*)\s*([^<\n*]+?)(?=\*\*|<|$|\n)', re.IGNORECASE)
        # Enhanced pattern for minimal documents with "Dossier numéro : [number]" (French) or "Dossiernummer : [number]" (Dutch) format
        self.dossier_minimal_pattern = re.compile(r'(?:Dossier numéro|Dossiernummer)\s*:\s*(\d{10})')
        # Updated to handle spaces in "Entr ee" from HTML entity decoding
        self.effective_date_pattern = re.compile(r'(?:<strong>|\*\*)Entr\s*(?:&eacute;|é|e)?\s*e\s+en\s+vigueur\s*:\s*(?:</strong>|\*\*)\s*([^<\n*]+?)(?=\*\*|<|$|\n)', re.IGNORECASE)
        # Pattern for end of validity date (Fin de validité)
        self.end_validity_date_pattern = re.compile(r'(?:<strong>|\*\*)Fin\s+de\s+validit\s*(?:&eacute;|é|e)?\s*:\s*(?:</strong>|\*\*)\s*([^<\n*]+?)(?=\*\*|<|$|\n)', re.IGNORECASE)
        self.source_pattern = re.compile(r'(?:<strong>|\*\*)Source:\s*(?:</strong>|\*\*)\s*([^<\n*]+?)(?=\*\*|<|$|\n)', re.IGNORECASE)

        # NUMAC pattern (10-character identifier) - Updated to handle both numeric and alphanumeric formats
        # Supports both pure numeric (e.g., "1234567890") and alphanumeric (e.g., "1870A30450") document numbers
        self.numac_content_pattern = re.compile(r'(?:<strong>|\*\*)Num\s*(?:&eacute;|é|e)?\s*ro:\s*(?:</strong>|\*\*)\s*([A-Z0-9]{10})', re.IGNORECASE)
        self.numac_filename_pattern = re.compile(r'([A-Z0-9]{10})', re.IGNORECASE)

        # Document title pattern - captures the full title with date and notes
        self.document_title_pattern = re.compile(r'^(\d{1,2}\s+[A-Z]+\s+\d{4})\.\s*-\s*(.+)', re.MULTILINE)

        # Version information patterns
        self.archived_versions_pattern = re.compile(r'\*\*\[(\d+)\s+versions\s+archivees\]')
        self.execution_orders_pattern = re.compile(r'\*\*\[(\d+)\s+arrêtes\s+d\'execution\]')

        # Document type extraction from title
        self.document_type_pattern = re.compile(r'(Loi|Arrêté|Décret|Ordonnance|Code|Constitution)', re.IGNORECASE)

        # Footnote section separator
        self.footnote_separator = re.compile(r'\\-{5,}')

        # Pattern for numbered provisions
        # Updated to handle both multi-line and inline provisions (separated by semicolons)
        # Captures provisions that end at semicolons, closing brackets, or before the next provision
        # Uses a two-step approach: first capture, then filter out citations in post-processing
        # This fixes the issue where provision 7° was missed in Article 37 WALLONNE due to inline formatting
        self.numbered_provision_pattern = re.compile(r'(\d+°)\s+([^;]+?)(?=\s*[;\]]|\s*\d+°|$)', re.MULTILINE)

        # Markdown escape sequence patterns for unescaping
        # Only unescape patterns that are commonly used in Belgian legal documents
        # and are likely to be markdown escape sequences, not legitimate backslashes
        self.markdown_escape_patterns = [
            # First, handle URL-like patterns to preserve them
            (r'https\\:', 'https\\:'),  # Preserve https\: in URLs
            (r'http\\:', 'http\\:'),    # Preserve http\: in URLs

            # Then handle regular escape sequences
            (r'\\-', '-'),      # Escaped hyphen: \- → - (very common in lists)
            (r'\\;', ';'),      # Escaped semicolon: \; → ; (common in legal text)
            (r'\\\!', '!'),     # Escaped exclamation: \! → !
            (r'\\\?', '?'),     # Escaped question mark: \? → ?
            (r'\\\(', '('),     # Escaped parenthesis: \( → (
            (r'\\\)', ')'),     # Escaped parenthesis: \) → )
            (r'\\\[', '['),     # Escaped bracket: \[ → [
            (r'\\\]', ']'),     # Escaped bracket: \] → ]
            (r'\\\.', '.'),     # Escaped period: \. → .
            (r'\\,', ','),      # Escaped comma: \, → ,

            # Handle colons - be more careful with context to avoid breaking URLs
            (r'par\s+\\:\s', 'par : '),   # "par \: " pattern (definition start): par \: → par :
            (r'\\:$', ':'),     # Escaped colon at end of line: \: → :
        ]

    def extract_numac_from_filename(self, filename: str) -> str:
        """Extract NUMAC from filename."""
        match = self.numac_filename_pattern.search(filename)
        return match.group(1) if match else ""

    def unescape_markdown_sequences(self, text: str) -> str:
        """
        Unescape markdown escape sequences to prevent double-escaping in JSON output.

        This function converts markdown escape sequences like \- back to their
        unescaped form - to prevent them from becoming \\- in JSON serialization.

        Args:
            text: Text containing markdown escape sequences

        Returns:
            Text with escape sequences unescaped
        """
        if not text:
            return text

        unescaped_text = text

        # Apply each escape pattern replacement
        for escaped_pattern, unescaped_replacement in self.markdown_escape_patterns:
            unescaped_text = re.sub(escaped_pattern, unescaped_replacement, unescaped_text)

        return unescaped_text

    def parse_date_to_iso(self, date_str: str) -> str:
        """Parse Belgian date format to ISO format (YYYY-MM-DD)."""
        if not date_str:
            return ""

        date_str = date_str.strip()

        # Handle format: "29 décembre 2016"
        french_months = {
            'janvier': '01', 'février': '02', 'mars': '03', 'avril': '04',
            'mai': '05', 'juin': '06', 'juillet': '07', 'août': '08',
            'septembre': '09', 'octobre': '10', 'novembre': '11', 'décembre': '12'
        }

        # Try to parse French date format
        for french_month, month_num in french_months.items():
            if french_month in date_str.lower():
                parts = date_str.lower().split()
                if len(parts) >= 3:
                    try:
                        day = parts[0].zfill(2)
                        year = parts[2]
                        return f"{year}-{month_num}-{day}"
                    except (ValueError, IndexError):
                        pass
                break

        # Try DD-MM-YYYY format (e.g., "05-07-2022")
        dd_mm_yyyy_pattern = r'^(\d{1,2})-(\d{1,2})-(\d{4})$'
        dd_mm_yyyy_match = re.match(dd_mm_yyyy_pattern, date_str)
        if dd_mm_yyyy_match:
            day = dd_mm_yyyy_match.group(1).zfill(2)
            month = dd_mm_yyyy_match.group(2).zfill(2)
            year = dd_mm_yyyy_match.group(3)
            return f"{year}-{month}-{day}"

        # If all parsing fails, return as-is
        return date_str

    def parse_page_number(self, page_str: str) -> int:
        """Parse page number to integer."""
        if not page_str:
            return 0

        try:
            # Extract numeric part
            page_num = re.search(r'\d+', page_str.strip())
            return int(page_num.group()) if page_num else 0
        except (ValueError, AttributeError):
            return 0

    def determine_hierarchy_level(self, title_type: str) -> int:
        """Determine the hierarchy level based on title type."""
        title_upper = title_type.upper()

        if "TITRE" in title_upper:
            return 0  # Top level
        elif "CHAPITRE" in title_upper:
            return 1  # Chapter level
        elif "SOUS-SECTION" in title_upper:
            return 3  # Subsection level - Check BEFORE "SECTION" to avoid false matches
        elif "SECTION" in title_upper:
            return 2  # Section level
        else:
            return 4  # Other/lowest level

    def get_hierarchy_rank(self, title_type: str) -> int:
        """Determine hierarchy rank for a title type.

        Belgian legal document hierarchy:
        - LIVRE → rank 0 (topmost level)
        - TITRE/ANNEXE → rank 1
        - CHAPITRE → rank 2
        - Section → rank 3
        - Sous-section → rank 4
        - Article → rank 5 (always leaf)
        """
        title_lower = title_type.lower()

        if 'livre' in title_lower:
            return 0  # LIVRE is the topmost hierarchical level
        elif 'titre' in title_lower or 'annexe' in title_lower:
            return 1
        elif 'chapitre' in title_lower:
            return 2
        elif 'sous-section' in title_lower:
            return 4  # Check for sous-section BEFORE section to avoid false matches
        elif 'section' in title_lower:
            return 3
        else:
            # Default to section level for unknown types
            return 3

    def normalize_type_name(self, title_type: str) -> str:
        """Normalize title type to standard names."""
        title_lower = title_type.lower()

        if 'livre' in title_lower:
            return 'livre'
        elif 'titre' in title_lower:
            return 'titre'
        elif 'chapitre' in title_lower:
            return 'chapitre'
        elif 'section' in title_lower and 'sous' not in title_lower:
            return 'section'
        elif 'sous-section' in title_lower:
            return 'sous-section'
        elif 'annexe' in title_lower:
            return 'annexe'
        else:
            return 'section'  # Default

    def parse_article_range(self, article_range: str) -> List[str]:
        """Parse article range string into individual article numbers."""
        articles = []

        # Handle None or empty article_range
        if not article_range:
            # Return a special marker indicating we should extract all articles
            # This allows the caller to fall back to full document extraction
            # instead of skipping article extraction entirely
            return ["__EXTRACT_ALL_ARTICLES__"]

        # Handle different formats: "1", "2-4", "5-6", "N", etc.
        parts = article_range.split(',')

        for part in parts:
            part = part.strip()
            if '-' in part:
                # Range format like "2-4"
                try:
                    start, end = part.split('-')
                    start_num = int(start.strip())
                    end_num = int(end.strip())
                    articles.extend([str(i) for i in range(start_num, end_num + 1)])
                except ValueError:
                    # Handle non-numeric ranges
                    articles.append(part)
            else:
                # Single article
                articles.append(part)

        return articles

    def article_matches_range(self, article_number: str, expected_articles: List[str]) -> bool:
        """
        Check if an article number matches any of the expected articles from a range.

        This handles cases where table of contents shows "1-5" but document contains
        articles like "1bis", "2ter", etc. that should still be considered part of the range.

        Args:
            article_number: The actual article number found (e.g., "1bis", "2ter")
            expected_articles: List from parse_article_range (e.g., ["1", "2", "3", "4", "5"])

        Returns:
            True if the article should be considered part of the range
        """
        if not article_number or not expected_articles:
            return False

        # Direct match
        if article_number in expected_articles:
            return True

        # Check if article number is a suffixed version of an expected base number
        # Extract base number from article_number (remove suffixes)
        import re
        base_match = re.match(r'^(\d+)', article_number)
        if base_match:
            base_number = base_match.group(1)
            if base_number in expected_articles:
                return True

        return False

    def extract_document_type_from_url(self, official_justel_url: str) -> str:
        """
        Extract document type from the official_justel_url field.

        Maps URL segments to standardized document types:
        - /constitution/ -> CONSTITUTION
        - /loi/ -> LOI
        - /decret/ -> DECRET
        - /ordonnance/ -> ORDONNANCE
        - /arrete/ -> ARRETE

        Args:
            official_justel_url: The ELI canonical URL from the document metadata

        Returns:
            Standardized document type string
        """
        if not official_justel_url:
            return "unknown"

        try:
            # Extract the document type from the URL path segment after /eli/
            # Pattern: https://www.ejustice.just.fgov.be/eli/{document_type}/...
            import re
            url_pattern = r'https://www\.ejustice\.just\.fgov\.be/eli/([^/]+)/'
            match = re.search(url_pattern, official_justel_url)

            if match:
                url_segment = match.group(1).lower()

                # Map URL segments to standardized document types
                url_type_mapping = {
                    'constitution': 'CONSTITUTION',
                    'loi': 'LOI',
                    'decret': 'DECRET',
                    'ordonnance': 'ORDONNANCE',
                    'arrete': 'ARRETE'
                }

                return url_type_mapping.get(url_segment, url_segment.upper())

        except Exception as e:
            # Log the error but don't fail the extraction
            print(f"Warning: Could not extract document type from URL {official_justel_url}: {e}")

        return "unknown"

    def extract_document_type(self, title: str) -> str:
        """
        Extract document type from title (legacy method for backwards compatibility).

        Note: This method is kept for backwards compatibility but should be replaced
        with extract_document_type_from_url() for more reliable extraction.
        """
        if not title:
            return "unknown"

        type_match = self.document_type_pattern.search(title)
        if type_match:
            doc_type = type_match.group(1).lower()
            # Normalize document types to match URL-based extraction format
            type_mapping = {
                'loi': 'LOI',
                'arrêté': 'ARRETE',
                'décret': 'DECRET',
                'ordonnance': 'ORDONNANCE',
                'code': 'CODE',
                'constitution': 'CONSTITUTION'
            }
            return type_mapping.get(doc_type, doc_type.upper())

        return "unknown"
