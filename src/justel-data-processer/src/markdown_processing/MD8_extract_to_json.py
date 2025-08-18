#!/usr/bin/env python3
"""
MD8_extract_to_json.py - Step 24 of Belgian Legal Document Processing Pipeline

This script extracts structured data from final processed Markdown files and converts them
into comprehensive JSON format, preserving the Belgian footnote system.

Author: Augment Agent
Date: 2025-07-02
"""

import os
import re
import json
import logging
from typing import Dict, List, Any, Optional, Tuple

# Import refactored modules - handle both relative and absolute imports
try:
    # Try relative imports first (when used as a module)
    from .extraction_utils import ExtractionUtils
    from .document_metadata import DocumentMetadataExtractor
    from .footnote_processor import FootnoteProcessor
    from .hierarchy_parser import HierarchyParser
    from .article_extractor import ArticleExtractor
    from .json_schema import JSONSchemaBuilder
except ImportError:
    # Fall back to absolute imports (when run as a script)
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from extraction_utils import ExtractionUtils
    from document_metadata import DocumentMetadataExtractor
    from footnote_processor import FootnoteProcessor
    from hierarchy_parser import HierarchyParser
    from article_extractor import ArticleExtractor
    from json_schema import JSONSchemaBuilder

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class BelgianLegalDocumentExtractor:
    """
    Extracts structured data from Belgian legal documents in Markdown format.
    Preserves the Belgian footnote system and generates comprehensive JSON output.

    This class now uses modular components for better maintainability while
    preserving all existing functionality and public interface.
    """

    def __init__(self, api_key: str = None, preserved_tables_dir: str = None):
        """
        Initialize the extractor with modular components.

        Args:
            api_key: Optional Gemini API key for LLM-based table generation
            preserved_tables_dir: Optional directory containing preserved HTML tables
        """
        # Initialize utility functions and modular components
        self.utils = ExtractionUtils()
        self.metadata_extractor = DocumentMetadataExtractor(self.utils)
        self.footnote_processor = FootnoteProcessor(self.utils)
        self.hierarchy_parser = HierarchyParser(self.utils)
        self.article_extractor = ArticleExtractor(self.utils, self.footnote_processor, api_key=api_key, preserved_tables_dir=preserved_tables_dir)
        self.json_builder = JSONSchemaBuilder(self.utils)
        self.preserved_tables_dir = preserved_tables_dir

        # Maintain backward compatibility by exposing key patterns as instance attributes
        self.footnote_reference_pattern = self.utils.footnote_reference_pattern
        self.legal_citation_pattern = self.utils.legal_citation_pattern
        self.article_pattern = self.utils.article_pattern
        self.title_pattern = self.utils.title_pattern
        self.publication_date_pattern = self.utils.publication_date_pattern
        self.page_pattern = self.utils.page_pattern
        self.dossier_pattern = self.utils.dossier_pattern
        self.dossier_minimal_pattern = self.utils.dossier_minimal_pattern
        self.effective_date_pattern = self.utils.effective_date_pattern
        self.source_pattern = self.utils.source_pattern
        self.numac_content_pattern = self.utils.numac_content_pattern
        self.numac_filename_pattern = self.utils.numac_filename_pattern
        self.document_title_pattern = self.utils.document_title_pattern
        self.archived_versions_pattern = self.utils.archived_versions_pattern
        self.execution_orders_pattern = self.utils.execution_orders_pattern
        self.document_type_pattern = self.utils.document_type_pattern
        self.footnote_separator = self.utils.footnote_separator
        self.numbered_provision_pattern = self.utils.numbered_provision_pattern
    
    def extract_numac(self, filename: str) -> str:
        """Extract NUMAC from filename."""
        return self.utils.extract_numac_from_filename(filename)

    def extract_references(self, content: str) -> Dict[str, Any]:
        """
        Extract legal document references from the source document.

        Returns a dictionary with:
        - modifies: List of documents this text modifies (from "Ce texte modifie les textes suivants" section)
        - modified_by: List of modifications made to this document (from "Fiche des modifications" section)
        """
        return self.metadata_extractor.extract_references(content)

    def extract_official_links(self, content: str) -> Dict[str, str]:
        """
        Extract official links from the '[5A] [6A] ## Lien [6B]s [5B]' section.

        Returns a dictionary with:
        - official_justel_url: The ELI canonical law link
        - official_publication_pdf_url: Link to the official publication PDF
        - consolidated_pdf_url: Link to the consolidated PDF version
        """
        return self.metadata_extractor.extract_official_links(content)

    def extract_document_metadata(self, content: str, filename: str, publication_metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Extract comprehensive document metadata from the content."""
        return self.metadata_extractor.extract_document_metadata(content, filename, publication_metadata)

    def _extract_full_document_title(self, content: str) -> str:
        """Extract the complete document title including all notes and version information."""
        # Look for the title in the [1A] ## Titre [1B] section
        title_section_start = content.find("[1A] ## Titre [1B]")
        if title_section_start == -1:
            return ""

        # Find the end of the title section (next section marker or source)
        title_section_end = content.find("**Source:**", title_section_start)
        if title_section_end == -1:
            title_section_end = content.find("[2A]", title_section_start)

        if title_section_end == -1:
            title_section = content[title_section_start:]
        else:
            title_section = content[title_section_start:title_section_end]

        # Extract the main title line (after NUMAC, before Source)
        lines = title_section.split('\n')
        title_lines = []

        for line in lines[1:]:  # Skip the section header
            line = line.strip()
            if not line:
                continue
            if line.isdigit() and len(line) == 10:  # Skip NUMAC line
                continue
            if line.startswith("**"):  # Stop at metadata fields
                break
            title_lines.append(line)

        return ' '.join(title_lines).strip()

    def _extract_document_source(self, content: str) -> str:
        """Extract the document source/authority."""
        source_match = self.source_pattern.search(content)
        if source_match:
            return source_match.group(1).strip()
        return ""

    def _parse_date_to_iso(self, date_str: str) -> str:
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

    def _parse_page_number(self, page_str: str) -> int:
        """Parse page number to integer."""
        if not page_str:
            return 0

        try:
            # Extract numeric part
            page_num = re.search(r'\d+', page_str.strip())
            return int(page_num.group()) if page_num else 0
        except (ValueError, AttributeError):
            return 0

    def _extract_document_type(self, title: str) -> str:
        """Extract document type from title."""
        if not title:
            return "unknown"

        type_match = self.document_type_pattern.search(title)
        if type_match:
            doc_type = type_match.group(1).lower()
            # Normalize document types
            type_mapping = {
                'loi': 'loi',
                'arrêté': 'arrete',
                'décret': 'decret',
                'ordonnance': 'ordonnance',
                'code': 'code',
                'constitution': 'constitution'
            }
            return type_mapping.get(doc_type, doc_type)

        return "unknown"

    def _extract_version_information(self, content: str) -> Dict[str, Any]:
        """Extract version and execution information."""
        version_info = {
            "archived_versions_count": 0,
            "archived_versions_url": "",
            "execution_orders_count": 0,
            "execution_orders_url": ""
        }

        # Extract archived versions
        archived_match = self.archived_versions_pattern.search(content)
        if archived_match:
            version_info["archived_versions_count"] = int(archived_match.group(1))
            # Extract URL from the link
            archived_url_match = re.search(r'\*\*\[\d+\s+versions\s+archivees\]\(([^)]+)\)', content)
            if archived_url_match:
                version_info["archived_versions_url"] = archived_url_match.group(1)

        # Extract execution orders
        execution_match = self.execution_orders_pattern.search(content)
        if execution_match:
            version_info["execution_orders_count"] = int(execution_match.group(1))
            # Extract URL from the link
            execution_url_match = re.search(r'\*\*\[\d+\s+arrêtes\s+d\'execution\]\(([^)]+)\)', content)
            if execution_url_match:
                version_info["execution_orders_url"] = execution_url_match.group(1)

        return version_info

    def extract_publication_metadata(self, content: str) -> Dict[str, Any]:
        """Extract publication metadata from document header."""
        return self.metadata_extractor.extract_publication_metadata(content)

    def parse_table_of_contents_to_tree(self, content: str) -> List[Dict[str, Any]]:
        """Parse the Table of Contents section into a hierarchical tree structure.

        Returns a list of top-level nodes, each containing nested children.
        Uses stack-based algorithm with hierarchy ranking system:
        - TITRE/ANNEXE → rank 1 (top level)
        - CHAPITRE → rank 2
        - Section → rank 3
        - Sous-section → rank 4
        - Article → rank 5 (always leaf)
        """
        return self.hierarchy_parser.parse_table_of_contents_to_tree(content)

    def _populate_tree_with_articles(self, tree_nodes: List[Dict[str, Any]], articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Populate the tree structure with actual article content.

        Args:
            tree_nodes: The hierarchical tree structure from parse_table_of_contents_to_tree
            articles: List of extracted articles with full content

        Returns:
            Updated tree structure with article content embedded
        """
        # Create a mapping of article numbers to article objects
        article_map = {}
        for article in articles:
            article_number = article.get("article_number", "")
            article_map[article_number] = article

        # Recursively populate tree nodes
        def populate_node(node):
            if node["type"] == "article":
                # Extract article numbers from the range
                article_range = node["metadata"].get("article_range", "")
                article_numbers = self._parse_article_range(article_range)

                if len(article_numbers) == 1:
                    # Single article - embed the full article object
                    article_num = article_numbers[0]
                    if article_num in article_map:
                        article_obj = article_map[article_num]

                        # Update metadata.article_range to match the complete article identifier
                        # This ensures consistency between metadata.article_range and article_content.article_number
                        unique_article_number = article_obj.get("article_number")
                        node["metadata"]["article_range"] = unique_article_number

                        node["article_content"] = {
                            "article_number": unique_article_number,
                            "anchor_id": article_obj.get("anchor_id"),
                            "content": article_obj.get("content", {}),
                            "structured_content_html": article_obj.get("structured_content_html"),
                            "structured_content_metadata": article_obj.get("structured_content_metadata")
                        }
                        node["footnotes"] = article_obj.get("footnotes", [])
                        node["footnote_references"] = article_obj.get("footnote_references", [])
                    else:
                        logger.warning(f"Article {article_num} not found in extracted articles")
                else:
                    # Multiple articles - create child nodes for each
                    node["children"] = []
                    for article_num in article_numbers:
                        if article_num in article_map:
                            article_obj = article_map[article_num]
                            child_node = {
                                "type": "article",
                                "label": f"Art. {article_num}",
                                "metadata": {
                                    "article_range": article_num,
                                    "rank": 5
                                },
                                "article_content": {
                                    "article_number": article_obj.get("article_number"),
                                    "anchor_id": article_obj.get("anchor_id"),
                                    "content": article_obj.get("content", {}),
                                    "structured_content_html": article_obj.get("structured_content_html"),
                                    "structured_content_metadata": article_obj.get("structured_content_metadata")
                                },
                                "footnotes": article_obj.get("footnotes", []),
                                "footnote_references": article_obj.get("footnote_references", [])
                            }
                            node["children"].append(child_node)
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

    def _get_hierarchy_rank(self, title_type: str) -> int:
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
        elif 'section' in title_lower:
            return 3
        elif 'sous-section' in title_lower:
            return 4
        else:
            # Default to section level for unknown types
            return 3

    def _normalize_type_name(self, title_type: str) -> str:
        """Normalize title type to standard names."""
        title_lower = title_type.lower()

        if 'titre' in title_lower:
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

    def extract_articles_with_tree_structure(self, content: str, document_id: str = None) -> List[Dict[str, Any]]:
        """Extract articles and organize them in hierarchical tree structure.

        This method parses the actual document content structure to create
        a complete tree structure with embedded article content.

        Args:
            content: Document content to parse
            document_id: Optional document ID for preserved tables lookup

        Returns:
            List of root-level tree nodes with articles embedded as leaf nodes
        """
        return self.article_extractor.extract_articles_with_tree_structure(content, document_id)

    def parse_document_content_to_tree(self, content: str) -> List[Dict[str, Any]]:
        """Parse the actual document content to build hierarchical tree structure.

        This method parses the [3A] ## Texte [3B] section to extract the real
        document structure from TITLE and ARTICLE markers.

        Returns:
            List of root-level tree nodes
        """
        return self.hierarchy_parser.parse_document_content_to_tree(content)

    def _count_articles_in_tree(self, tree_nodes: List[Dict[str, Any]]) -> int:
        """Count total number of articles in the tree structure."""
        return self.json_builder.count_articles_in_tree(tree_nodes)

    def _count_footnote_refs_in_tree(self, tree_nodes: List[Dict[str, Any]]) -> int:
        """Count total number of footnote references in the tree structure."""
        return self.json_builder.count_footnote_refs_in_tree(tree_nodes)

    def _count_footnotes_in_tree(self, tree_nodes: List[Dict[str, Any]]) -> int:
        """Count total number of footnotes in the tree structure."""
        return self.json_builder.count_footnotes_in_tree(tree_nodes)

    def parse_table_of_contents(self, content: str) -> Dict[str, Any]:
        """Parse the Table of Contents section to understand document structure and article mappings."""
        return self.hierarchy_parser.parse_table_of_contents(content)



    def _determine_hierarchy_level(self, title_type: str) -> int:
        """Determine the hierarchy level based on title type."""
        return self.utils.determine_hierarchy_level(title_type)

    def _parse_article_range(self, article_range: str) -> List[str]:
        """Parse article range string into individual article numbers."""
        return self.utils.parse_article_range(article_range)

    def extract_document_hierarchy(self, content: str) -> Dict[str, List[Dict[str, Any]]]:
        """Extract document hierarchical structure with enhanced ToC-based analysis."""
        return self.hierarchy_parser.extract_document_hierarchy(content)

    def find_article_parent_structure(self, article_number: str, hierarchy: Dict[str, List[Dict[str, Any]]]) -> Dict[str, str]:
        """Find the parent structural elements for an article using ToC-based mapping."""
        return self.hierarchy_parser.find_article_parent_structure(article_number, hierarchy)

    def _find_article_parent_structure_by_position(self, article_number: str, hierarchy: Dict[str, List[Dict[str, Any]]]) -> Dict[str, str]:
        """Fallback method to find parent structure based on article position in content."""
        return self.hierarchy_parser._find_article_parent_structure_by_position(article_number, hierarchy)

    def extract_footnote_references_from_text(self, text: str) -> List[Dict[str, Any]]:
        """Extract Belgian footnote references from article text."""
        return self.footnote_processor.extract_footnote_references_from_text(text)

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
        return self.footnote_processor.extract_footnote_urls(footnote_content, law_url, article_number)

    def extract_footnotes_from_section(self, footnote_section: str, article_number: str = "") -> List[Dict[str, Any]]:
        """Extract footnotes from a footnote section with URL extraction."""
        return self.footnote_processor.extract_footnotes_from_section(footnote_section, article_number)
    
    def split_article_content_and_footnotes(self, article_text: str, article_number: str = "") -> Tuple[str, List[Dict[str, Any]]]:
        """Split article text into main content and footnote section."""
        return self.footnote_processor.split_article_content_and_footnotes(article_text, article_number)
    
    def parse_numbered_provisions(self, text: str) -> List[Dict[str, Any]]:
        """Parse numbered provisions from article text."""
        return self.article_extractor.parse_numbered_provisions(text)
    
    def extract_articles_with_hierarchy(self, content: str, hierarchy: Dict[str, List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
        """Extract all articles from the document content with hierarchy information."""
        return self.article_extractor.extract_articles_with_hierarchy(content, hierarchy)

    def extract_articles(self, content: str) -> List[Dict[str, Any]]:
        """Extract all articles from the document content."""
        return self.article_extractor.extract_articles(content)
    
    def extract_preamble(self, content: str) -> str:
        """Extract the preamble section from the document if it exists.
        
        The preamble is marked with [9A] ## Préambule [9B] and contains
        the legal preamble text (typically "Vu..." clauses and "Arrête:").
        
        Returns:
            The preamble text if found, empty string otherwise.
        """
        # Look for the preamble section marker
        preamble_start = content.find("[9A] ## Préambule [9B]")
        if preamble_start == -1:
            # Try alternative spellings/formats
            preamble_start = content.find("[9A] ## PREAMBULE [9B]")
            if preamble_start == -1:
                preamble_start = content.find("[9A] ## préambule [9B]")
                if preamble_start == -1:
                    return ""
        
        # Find the end of the preamble section (next section marker)
        # Common section markers that could follow the preamble
        section_markers = [
            "[5A]", "[6A]", "[4A]", "[10A]", "[11A]", "[12A]",
            "## Lien", "## Fiche des modifications"
        ]
        
        preamble_end = len(content)  # Default to end of content
        for marker in section_markers:
            marker_pos = content.find(marker, preamble_start)
            if marker_pos != -1 and marker_pos < preamble_end:
                preamble_end = marker_pos
        
        # Extract the preamble text
        preamble_text = content[preamble_start:preamble_end]
        
        # Remove the section marker and clean up
        preamble_text = preamble_text.replace("[9A] ## Préambule [9B]", "")
        preamble_text = preamble_text.replace("[9A] ## PREAMBULE [9B]", "")
        preamble_text = preamble_text.replace("[9A] ## préambule [9B]", "")
        
        # Clean up whitespace
        preamble_text = preamble_text.strip()
        
        return preamble_text

    def extract_abrogation_info(self, content: str) -> Dict[str, Any]:
        """Extract abrogation information from documents that are fully abrogated.
        
        For documents that contain only abrogation text in the Text section,
        this extracts and parses the abrogation information.
        
        Returns:
            Dictionary with abrogation information or empty dict if not abrogated
        """
        abrogation_info = {}
        
        # Look for the Text section
        text_start = content.find("[3A] ## Texte [3B]")
        if text_start == -1:
            return abrogation_info
        
        # Find the end of the Text section
        text_end = content.find("[4A]", text_start)
        if text_end == -1:
            text_end = content.find("[5A]", text_start) 
            if text_end == -1:
                text_end = len(content)
        
        text_content = content[text_start:text_end].strip()
        
        # Check if the text contains only abrogation information
        # Pattern: (abrogé) <LAW_REFERENCE, ARTICLE, ENTRY; En vigueur : DATE>
        abrogation_pattern = re.compile(
            r'\(abrogé\)\s*<([^,]+),\s*([^,]+),\s*([^;]+);\s*(?:\*\*)?En vigueur\s*:\s*(?:\*\*)?([^>]+)>'
        )
        
        match = abrogation_pattern.search(text_content)
        if match:
            abrogation_info = {
                "is_fully_abrogated": True,
                "abrogation_text": "(abrogé)",
                "abrogating_law": match.group(1).strip(),
                "abrogating_article": match.group(2).strip(),
                "abrogation_entry": match.group(3).strip(),
                "abrogation_date": self.utils.parse_date_to_iso(match.group(4).strip()),
                "raw_abrogation_text": match.group(0)
            }
        
        return abrogation_info

    def process_document(self, file_path: str) -> Dict[str, Any]:
        """Process a single document and return structured JSON data."""
        logger.info(f"Processing document: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        filename = os.path.basename(file_path)

        # Extract publication metadata
        publication_metadata = self.extract_publication_metadata(content)
        document_metadata = self.extract_document_metadata(content, filename, publication_metadata)

        # Extract legal document references
        references = self.extract_references(content)

        # Extract preamble if present
        preamble = self.extract_preamble(content)

        # Extract abrogation information if document is abrogated
        abrogation_info = self.extract_abrogation_info(content)

        # Extract document ID (filename without extension)
        document_id = os.path.splitext(filename)[0]
        
        # Extract articles with hierarchical tree structure
        hierarchical_tree = self.extract_articles_with_tree_structure(content, document_id)

        # Build the complete JSON structure using the JSON builder
        document = self.json_builder.build_document_structure(
            document_metadata, hierarchical_tree, references, filename, preamble, abrogation_info
        )

        return document


def main():
    """Main execution function."""
    # Get API key for LLM table generation (OpenAI for tables, Gemini for titles)
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        logger.info("🤖 OpenAI API key found - LLM table generation enabled")
    else:
        logger.info("⚠️  No OpenAI API key found - using fallback table generation")

    # Get preserved tables directory from command line argument or environment
    preserved_tables_dir = None
    if '--preserved-tables-dir' in sys.argv:
        idx = sys.argv.index('--preserved-tables-dir')
        if idx + 1 < len(sys.argv):
            preserved_tables_dir = sys.argv[idx + 1]
            logger.info(f"📊 Using preserved tables from: {preserved_tables_dir}")
    
    extractor = BelgianLegalDocumentExtractor(api_key=api_key, preserved_tables_dir=preserved_tables_dir)

    # Define input and output directories
    # Check for isolated environment first, then fall back to regular directories
    input_dir = "output/22"
    if not os.path.exists(input_dir) or len(os.listdir(input_dir)) == 0:
        input_dir = "output/single_file_test_txt/22"

    output_dir = "output/24"
    if not os.path.exists(os.path.dirname(output_dir)) or input_dir.startswith("output/single_file_test_txt"):
        output_dir = "output/single_file_test_txt/24"

    if not os.path.exists(input_dir):
        logger.error(f"Input directory not found: {input_dir}")
        return

    logger.info(f"Using input directory: {input_dir}")
    logger.info(f"Using output directory: {output_dir}")

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Process all .md files in the input directory
    processed_count = 0
    files_in_dir = os.listdir(input_dir)
    logger.info(f"Found {len(files_in_dir)} files in input directory: {files_in_dir}")

    for filename in files_in_dir:
        if filename.endswith('.md'):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename.replace('.md', '.json'))

            try:
                # Process the document
                document_data = extractor.process_document(input_file)

                # Count statistics from the processed document
                total_articles = extractor._count_articles_in_tree(document_data['document_hierarchy'])
                total_footnotes = extractor._count_footnotes_in_tree(document_data['document_hierarchy'])

                # Save to JSON file
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(document_data, f, indent=2, ensure_ascii=False)

                logger.info(f"Successfully processed: {filename}")
                logger.info(f"  - Articles extracted: {total_articles}")
                logger.info(f"  - Footnotes extracted: {total_footnotes}")
                logger.info(f"  - Output saved to: {output_file}")

                processed_count += 1

            except Exception as e:
                logger.error(f"Error processing {filename}: {str(e)}")

    logger.info(f"Processing complete. {processed_count} files processed successfully.")


if __name__ == "__main__":
    main()
