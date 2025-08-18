#!/usr/bin/env python3
"""
hierarchy_parser.py - Hierarchical structure parsing for Belgian Legal Documents

This module handles parsing of document hierarchical structures including table of contents,
tree building, and article organization within the document hierarchy.

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


class HierarchyParser:
    """
    Parses hierarchical structures from Belgian legal documents.
    """
    
    def __init__(self, utils: ExtractionUtils):
        """Initialize with utility functions."""
        self.utils = utils

    def _clean_unmatched_brackets(self, text: str) -> str:
        """
        Remove unmatched curly brackets from text.
        Article labels and title_type fields should never have unmatched curly brackets.

        Args:
            text: The text to clean

        Returns:
            Text with unmatched curly brackets removed
        """
        if not text:
            return text

        # Count opening and closing brackets
        open_count = text.count('{')
        close_count = text.count('}')

        # If brackets are balanced, leave them alone
        if open_count == close_count and open_count > 0:
            return text

        # Remove all unmatched brackets (safer approach)
        # Remove standalone closing brackets at the beginning
        cleaned = text.lstrip('}')

        # Remove standalone opening brackets at the end
        cleaned = cleaned.rstrip('{')

        return cleaned

    def parse_table_of_contents(self, content: str) -> Dict[str, Any]:
        """Parse the Table of Contents section to understand document structure and article mappings."""
        toc_structure = {
            "hierarchy": [],
            "article_mappings": {}  # Maps article numbers to their hierarchical path
        }

        # Find the Table of Contents section
        toc_match = re.search(r'\[2A\] ## Table des matières \[2B\](.*?)(?=\[3A\]|\*\*ARTICLE\*\*|$)', content, re.DOTALL)
        if not toc_match:
            logger.warning("Table of Contents section not found")
            return toc_structure

        toc_content = toc_match.group(1)
        logger.info(f"DEBUG: ToC content length: {len(toc_content)}")
        logger.info(f"DEBUG: ToC content preview: {toc_content[:500]}")

        # Parse ToC entries with hierarchy tracking
        current_hierarchy = []

        # Pattern to match ToC entries: **TITLE**[TYPE] - CONTENT
        # Handle both normal titles and special format like [1- ... ]1 or [1 \- ... ]1
        title_pattern = re.compile(r'\*\*TITLE\*\*\[([^\]]+)\]\s*(?:\\?-\s*(.+?)|\s*\[1\s*\\?-?\s*(.+?)\]1)(?=\n|$)', re.MULTILINE)
        # Pattern to match article ranges: Art. followed by numbers/ranges
        article_pattern = re.compile(r'Art\.\s*([^\n]+)', re.MULTILINE)

        title_matches = list(title_pattern.finditer(toc_content))

        # Process each title and look for following article ranges
        for i, match in enumerate(title_matches):
            title_type = match.group(1).strip()
            # Handle different title content formats
            title_content = ""
            if match.group(2):  # Normal format: \- content
                title_content = match.group(2).strip()
            elif match.group(3):  # Special format: [1- content ]1
                title_content = match.group(3).strip()

            # Look for article range in the text following this title
            start_pos = match.end()
            end_pos = title_matches[i + 1].start() if i + 1 < len(title_matches) else len(toc_content)
            following_text = toc_content[start_pos:end_pos]

            # Find article range in the following text
            article_match = article_pattern.search(following_text)
            article_range = article_match.group(1).strip() if article_match else ""

            # Determine hierarchy level based on title type
            level = self.utils.determine_hierarchy_level(title_type)

            # Update current hierarchy path
            current_hierarchy = current_hierarchy[:level]  # Trim to current level

            hierarchy_entry = {
                "level": level,
                "type": title_type,
                "content": title_content,
                "full_title": f"{title_type} {title_content}",
                "article_range": article_range,
                "hierarchy_path": current_hierarchy.copy()
            }

            current_hierarchy.append(hierarchy_entry)
            toc_structure["hierarchy"].append(hierarchy_entry)

            # Parse article ranges and map to hierarchy
            if article_range:
                articles = self.utils.parse_article_range(article_range)

                for article_num in articles:
                    toc_structure["article_mappings"][article_num] = current_hierarchy.copy()

        return toc_structure

    def parse_table_of_contents_to_tree(self, content: str) -> List[Dict[str, Any]]:
        """Parse the Table of Contents section into a hierarchical tree structure.

        Returns a list of top-level nodes, each containing nested children.
        Uses stack-based algorithm with hierarchy ranking system:
        - LIVRE → rank 0 (topmost level)
        - TITRE/ANNEXE → rank 1
        - CHAPITRE → rank 2
        - Section → rank 3
        - Sous-section → rank 4
        - Article → rank 5 (always leaf)
        """
        # Find the Table of Contents section
        toc_match = re.search(r'\[2A\] ## Table des matières \[2B\](.*?)(?=\[3A\]|\*\*ARTICLE\*\*|$)', content, re.DOTALL)
        if not toc_match:
            logger.warning("Table of Contents section not found")
            return []

        toc_content = toc_match.group(1)
        logger.info(f"Parsing ToC into tree structure, content length: {len(toc_content)}")

        # Split content into lines for processing
        lines = toc_content.split('\n')

        # Stack to maintain current hierarchy path
        hierarchy_stack = []
        root_nodes = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Check for article patterns first (before general heading patterns)
            # This ensures **TITLE**[Art.] patterns are recognized as articles, not sections
            # Handle both clean and corrupted patterns: [Art.] and [}Art.]
            # CASE-INSENSITIVE: Support both [Art.] and [art.] patterns
            title_article_match = re.match(r'\*\*TITLE\*\*\[}?[Aa]rt\.\]\s*(.+)', line)

            # Check if this is a heading line (but exclude Art. patterns which are handled above)
            heading_match = re.match(r'\*\*TITLE\*\*\[([^\]]+)\]\s*(?:\\?-\s*(.+?)|\s*\[1\s*\\?-?\s*(.+?)\]1)$', line)
            if heading_match and heading_match.group(1).strip() in ["Art.", "}Art."]:
                heading_match = None  # Don't treat Art. patterns as general headings

            annexe_match = re.match(r'\*\*ANNEXE\*\*\[([^\]]+)\]', line)
            article_match = re.match(r'Art\.\s*(.+)', line)

            if title_article_match:
                # Handle **TITLE**[Art.] patterns as articles
                article_content = title_article_match.group(1).strip()

                # Extract article number/range from the content
                # Pattern: [NUMBER]. (REGION) or just [NUMBER].
                article_number_match = re.match(r'\[([^\]]+)\]\.?\s*(?:\(([^)]+)\))?', article_content)
                if article_number_match:
                    article_number = article_number_match.group(1).strip()
                    region_info = article_number_match.group(2)

                    # Clean unmatched curly brackets from article_number
                    article_number = self._clean_unmatched_brackets(article_number)

                    # Create full article range including region if present
                    if region_info:
                        # Clean and normalize region info
                        region_clean = self._clean_unmatched_brackets(region_info.strip())
                        article_range = f"{article_number}. ({region_clean})"
                    else:
                        article_range = f"{article_number}."

                    # Create article node
                    node = {
                        "type": "article",
                        "label": self._clean_unmatched_brackets(f"Article {article_range}"),
                        "metadata": {
                            "article_range": article_range,
                            "rank": 5  # Articles are always leaf nodes
                        },
                        "article_content": None,  # Will be populated later
                        "footnotes": [],
                        "footnote_references": []
                    }

                    # Add to current parent (articles are always leaves)
                    if hierarchy_stack:
                        hierarchy_stack[-1]["children"].append(node)
                    else:
                        # Orphaned article - create a default container
                        logger.warning(f"Orphaned article found: {article_range}")
                        root_nodes.append(node)

            elif heading_match:
                # Extract title type and content
                title_type = heading_match.group(1).strip()
                title_content = heading_match.group(2) or heading_match.group(3) or ""
                title_content = title_content.strip()

                # Clean unmatched curly brackets from title_type
                title_type = self._clean_unmatched_brackets(title_type)

                # Determine hierarchy rank
                rank = self.utils.get_hierarchy_rank(title_type)

                # Create node
                node = {
                    "type": self.utils.normalize_type_name(title_type),
                    "label": self._clean_unmatched_brackets(f"{title_type} {title_content}".strip()),
                    "metadata": {
                        "title_type": title_type,
                        "title_content": title_content,
                        "rank": rank
                    },
                    "children": []
                }

                # Pop stack while top rank >= current rank
                while hierarchy_stack and hierarchy_stack[-1]["metadata"]["rank"] >= rank:
                    hierarchy_stack.pop()

                # Add to parent or root
                if hierarchy_stack:
                    hierarchy_stack[-1]["children"].append(node)
                else:
                    root_nodes.append(node)

                # Push to stack
                hierarchy_stack.append(node)

            elif annexe_match:
                # Handle ANNEXE as rank 1 (same as TITRE, below LIVRE)
                annexe_type = annexe_match.group(1).strip()

                # Clean unmatched curly brackets from annexe_type
                annexe_type = self._clean_unmatched_brackets(annexe_type)

                node = {
                    "type": "annexe",
                    "label": self._clean_unmatched_brackets(f"ANNEXE {annexe_type}".strip()),
                    "metadata": {
                        "title_type": self._clean_unmatched_brackets(f"ANNEXE {annexe_type}"),
                        "title_content": "",
                        "rank": 1
                    },
                    "children": []
                }

                # Pop stack while top rank >= 1 (ANNEXE can be under LIVRE rank 0)
                while hierarchy_stack and hierarchy_stack[-1]["metadata"]["rank"] >= 1:
                    hierarchy_stack.pop()

                # Add to appropriate parent (LIVRE if exists, otherwise root)
                if hierarchy_stack:
                    hierarchy_stack[-1]["children"].append(node)
                else:
                    root_nodes.append(node)
                hierarchy_stack.append(node)

            elif article_match:
                # Handle article range
                article_range = article_match.group(1).strip()

                # Clean unmatched curly brackets from article_range
                article_range = self._clean_unmatched_brackets(article_range)

                node = {
                    "type": "article",
                    "label": self._clean_unmatched_brackets(f"Article {article_range}"),
                    "metadata": {
                        "article_range": article_range,
                        "rank": 5
                    },
                    "article_content": None,  # Will be populated later
                    "footnotes": [],
                    "footnote_references": []
                }

                # Add to current parent (articles are always leaves)
                if hierarchy_stack:
                    hierarchy_stack[-1]["children"].append(node)
                else:
                    # Orphaned article - create a default container
                    logger.warning(f"Orphaned article found: {article_range}")
                    root_nodes.append(node)

        logger.info(f"Created tree structure with {len(root_nodes)} root nodes")
        return root_nodes

    def parse_document_content_to_tree(self, content: str) -> List[Dict[str, Any]]:
        """Parse the actual document content to build hierarchical tree structure.

        This method parses the [3A] ## Texte [3B] section to extract the real
        document structure from TITLE and ARTICLE markers.

        Returns:
            List of root-level tree nodes
        """
        # Find the actual document content section
        texte_start = content.find("[3A] ## Texte [3B]")
        if texte_start == -1:
            logger.warning("Document content section not found")
            return []

        document_content = content[texte_start:]
        lines = document_content.split('\n')

        tree_structure = []
        hierarchy_stack = []  # Stack to track current hierarchy path

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Parse TITLE markers for hierarchical structure
            # Handle both patterns: **TITLE**[TYPE] \- content AND **TITLE**[TYPE] content
            if line.startswith('**TITLE**['):
                # Check for article patterns first (before general title patterns)
                # Handle both clean and corrupted patterns: [Art.] and [}Art.]
                # CASE-INSENSITIVE: Support both [Art.] and [art.] patterns
                title_article_match = re.match(r'\*\*TITLE\*\*\[}?[Aa]rt\.\]\s*(.+)', line)

                if title_article_match:
                    # Handle **TITLE**[Art.] patterns as articles
                    article_content = title_article_match.group(1).strip()

                    # Extract article number/range from the content
                    # Pattern: [NUMBER]. (REGION) or just [NUMBER].
                    article_number_match = re.match(r'\[([^\]]+)\]\.?\s*(?:\(([^)]+)\))?', article_content)
                    if article_number_match:
                        article_number = article_number_match.group(1).strip()
                        region_info = article_number_match.group(2)

                        # Clean unmatched curly brackets from article_number
                        article_number = self._clean_unmatched_brackets(article_number)

                        # Create full article range including region if present
                        if region_info:
                            # Clean and normalize region info
                            region_clean = self._clean_unmatched_brackets(region_info.strip())
                            article_range = f"{article_number}. ({region_clean})"
                        else:
                            article_range = f"{article_number}."

                        # Create article node
                        node = {
                            "type": "article",
                            "label": self._clean_unmatched_brackets(f"Art. {article_range}"),
                            "metadata": {
                                "article_range": article_range,
                                "rank": 5  # Articles are always leaf nodes
                            },
                            "article_content": None,  # Will be populated later
                            "footnotes": [],
                            "footnote_references": []
                        }

                        # Add to current hierarchy level
                        if hierarchy_stack:
                            hierarchy_stack[-1]["children"].append(node)
                        else:
                            # If no hierarchy, create a default structure
                            tree_structure.append(node)
                else:
                    # Use the general title pattern from extraction_utils
                    title_match = self.utils.title_pattern.match(line)
                    if title_match:
                        title_type = title_match.group(1).strip()
                        full_content = title_match.group(2).strip()

                        # Handle both patterns: with and without \- separator
                        if full_content.startswith('\\-'):
                            # Pattern: **TITLE**[TYPE] \- content
                            title_content = full_content[2:].strip()  # Remove \- and leading spaces
                        else:
                            # Pattern: **TITLE**[TYPE] content (no \- separator)
                            title_content = full_content

                        # Clean unmatched curly brackets from title_type
                        title_type = self._clean_unmatched_brackets(title_type)

                        # Determine hierarchy rank
                        rank = self.utils.get_hierarchy_rank(title_type)

                        # Create tree node
                        node = {
                            "type": self.utils.normalize_type_name(title_type),
                            "label": self._clean_unmatched_brackets(f"{title_type} {title_content}"),
                            "metadata": {
                                "title_type": title_type,
                                "title_content": title_content,
                                "rank": rank
                            },
                            "children": []
                        }

                    # Adjust hierarchy stack based on rank
                    while hierarchy_stack and hierarchy_stack[-1]["metadata"]["rank"] >= rank:
                        hierarchy_stack.pop()

                    # Add to appropriate parent
                    if hierarchy_stack:
                        hierarchy_stack[-1]["children"].append(node)
                    else:
                        tree_structure.append(node)

                    hierarchy_stack.append(node)

            # Parse ANNEXE markers for hierarchical structure
            # Handle pattern: **ANNEXE**[TYPE]
            elif line.startswith('**ANNEXE**['):
                # Extract ANNEXE type using regex pattern
                annexe_match = re.match(r'\*\*ANNEXE\*\*\[([^\]]+)\]', line)
                if annexe_match:
                    annexe_type = annexe_match.group(1).strip()

                    # Clean unmatched curly brackets from annexe_type
                    annexe_type = self._clean_unmatched_brackets(annexe_type)

                    # Handle label creation - avoid duplication if annexe_type already contains "ANNEXE"
                    if annexe_type.upper().startswith('ANNEXE'):
                        label = annexe_type
                        title_type = annexe_type
                    else:
                        label = f"ANNEXE {annexe_type}"
                        title_type = f"ANNEXE {annexe_type}"

                    # Create ANNEXE node with rank 1 (same as TITRE)
                    node = {
                        "type": "annexe",
                        "label": self._clean_unmatched_brackets(label),
                        "metadata": {
                            "title_type": self._clean_unmatched_brackets(title_type),
                            "title_content": "",
                            "rank": 1
                        },
                        "children": []
                    }

                    # Adjust hierarchy stack based on rank 1
                    while hierarchy_stack and hierarchy_stack[-1]["metadata"]["rank"] >= 1:
                        hierarchy_stack.pop()

                    # Add to appropriate parent (LIVRE if exists, otherwise root)
                    if hierarchy_stack:
                        hierarchy_stack[-1]["children"].append(node)
                    else:
                        tree_structure.append(node)

                    hierarchy_stack.append(node)

            # Parse ARTICLE markers for individual articles
            elif line.startswith('**ARTICLE**'):
                # Use the same article pattern from extraction_utils
                article_match = self.utils.article_pattern.match(line)
                if article_match:
                    # Extract article number from the appropriate capture group
                    # Updated for 7-group pattern (Claude Opus 4 improved approach):
                    # Group 1: [Art.] [NUMBER]. format
                    # Group 2: [Art.] NUMBER. format (without brackets) - FIXED: captures Article 57
                    # Group 3: [Art.] N. format (placeholder)
                    # Group 4: [Art.] NUMBER\. format (literal backslash-period) - NEW: captures Article 3
                    # Group 5: Art. [NUMBER] format (without brackets around Art) - NEW
                    # Group 6: Article [NUMBER]. format
                    # Group 7: Article NUMBER\. format (without brackets)
                    article_number = (article_match.group(1) or article_match.group(2) or article_match.group(3) or
                                    article_match.group(4) or article_match.group(5) or article_match.group(6) or article_match.group(7))

                    # Clean unmatched curly brackets from article_number
                    article_number = self._clean_unmatched_brackets(article_number)

                    # Create article node
                    article_node = {
                        "type": "article",
                        "label": self._clean_unmatched_brackets(f"Art. {article_number}"),
                        "metadata": {
                            "article_range": article_number,
                            "rank": 5  # Articles are always leaf nodes
                        },
                        "article_content": None,  # Will be populated later
                        "footnotes": [],
                        "footnote_references": []
                    }

                    # Add to current hierarchy level
                    if hierarchy_stack:
                        hierarchy_stack[-1]["children"].append(article_node)
                    else:
                        # If no hierarchy, create a default structure
                        tree_structure.append(article_node)

        logger.info(f"Parsed document content into tree with {len(tree_structure)} root nodes")
        return tree_structure

    def extract_document_hierarchy(self, content: str) -> Dict[str, List[Dict[str, Any]]]:
        """Extract document hierarchical structure with enhanced ToC-based analysis."""
        # Parse Table of Contents first
        toc_data = self.parse_table_of_contents(content)

        hierarchy = {
            "titles": [],
            "chapters": [],
            "sections": [],
            "subsections": [],
            "toc_structure": toc_data  # Include ToC data for parent structure mapping
        }

        # Counters for generating unique keys
        chapter_counter = 0
        section_counter = 0
        subsection_counter = 0
        title_counter = 0

        # Extract structural elements from the main content
        title_matches = self.utils.title_pattern.finditer(content)
        for match in title_matches:
            title_type = match.group(1).strip()
            title_content = match.group(2).strip()

            # Base entry structure
            base_entry = {
                "title_type": title_type,
                "title_content": title_content,
                "full_title": f"{title_type} {title_content}",
                "position": match.start()
            }

            # Categorize and add unique identifiers based on hierarchy level
            level = self.utils.determine_hierarchy_level(title_type)

            if level == 0:  # TITRE level
                title_counter += 1
                title_entry = {
                    **base_entry,
                    "title_key": f"title_{title_counter}",
                    "title_number": title_counter,
                    "level": level
                }
                hierarchy["titles"].append(title_entry)

            elif level == 1:  # CHAPITRE level
                chapter_counter += 1
                chapter_entry = {
                    **base_entry,
                    "chapter_key": f"chapter_{chapter_counter}",
                    "chapter_number": chapter_counter,
                    "level": level
                }
                hierarchy["chapters"].append(chapter_entry)

            elif level == 2:  # SECTION level
                section_counter += 1
                section_entry = {
                    **base_entry,
                    "section_key": f"section_{section_counter}",
                    "section_number": section_counter,
                    "level": level
                }
                hierarchy["sections"].append(section_entry)

            elif level == 3:  # SOUS-SECTION level
                subsection_counter += 1
                subsection_entry = {
                    **base_entry,
                    "subsection_key": f"subsection_{subsection_counter}",
                    "subsection_number": subsection_counter,
                    "level": level
                }
                hierarchy["subsections"].append(subsection_entry)

        return hierarchy

    def find_article_parent_structure(self, article_number: str, hierarchy: Dict[str, List[Dict[str, Any]]]) -> Dict[str, str]:
        """Find the parent structural elements for an article using ToC-based mapping."""
        parent_structure = {
            "title_key": "",
            "title_title": "",
            "chapter_key": "",
            "chapter_title": "",
            "section_key": "",
            "section_title": "",
            "paragraph_key": "",
            "paragraph_title": ""
        }

        # Get ToC structure if available
        toc_structure = hierarchy.get("toc_structure", {})
        article_mappings = toc_structure.get("article_mappings", {})

        # First try to find the article in ToC mappings
        if article_number in article_mappings:
            hierarchy_path = article_mappings[article_number]

            # Extract parent structure from hierarchy path
            for level_entry in hierarchy_path:
                level = level_entry.get("level", 4)

                if level == 0:  # TITRE level
                    parent_structure["title_key"] = f"title_{level_entry.get('type', '')}"
                    parent_structure["title_title"] = level_entry.get("full_title", "")
                elif level == 1:  # CHAPITRE level
                    parent_structure["chapter_key"] = f"chapter_{level_entry.get('type', '')}"
                    parent_structure["chapter_title"] = level_entry.get("full_title", "")
                elif level == 2:  # SECTION level
                    parent_structure["section_key"] = f"section_{level_entry.get('type', '')}"
                    parent_structure["section_title"] = level_entry.get("full_title", "")
                elif level == 3:  # SOUS-SECTION level
                    parent_structure["paragraph_key"] = f"subsection_{level_entry.get('type', '')}"
                    parent_structure["paragraph_title"] = level_entry.get("full_title", "")

            return parent_structure

        # Fallback: Use position-based approach for articles not in ToC
        logger.warning(f"Article {article_number} not found in ToC mappings, using position-based fallback")
        return self._find_article_parent_structure_by_position(article_number, hierarchy)

    def _find_article_parent_structure_by_position(self, article_number: str, hierarchy: Dict[str, List[Dict[str, Any]]]) -> Dict[str, str]:
        """Fallback method to find parent structure based on article position in content."""
        parent_structure = {
            "title_key": "",
            "title_title": "",
            "chapter_key": "",
            "chapter_title": "",
            "section_key": "",
            "section_title": "",
            "paragraph_key": "",
            "paragraph_title": ""
        }

        # This would require finding the article position in content first
        # For now, return empty structure as fallback
        # In a complete implementation, you would:
        # 1. Find the article's position in the content
        # 2. Look for the most recent structural elements before that position
        # 3. Build the parent structure accordingly

        return parent_structure
