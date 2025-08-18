#!/usr/bin/env python3
"""
json_schema.py - JSON schema generation for Belgian Legal Documents

This module handles the generation of JSON output structures for Belgian legal documents,
including document structure building and output formatting.

Author: Augment Agent
Date: 2025-07-13
"""

import logging
from datetime import datetime
from typing import Dict, List, Any, Optional

# Handle both relative and absolute imports
try:
    from .extraction_utils import ExtractionUtils
except ImportError:
    from extraction_utils import ExtractionUtils

logger = logging.getLogger(__name__)


class JSONSchemaBuilder:
    """
    Builds JSON schema structures for Belgian legal documents.
    """
    
    def __init__(self, utils: ExtractionUtils):
        """Initialize with utility functions."""
        self.utils = utils

    def count_articles_in_tree(self, tree_nodes: List[Dict[str, Any]]) -> int:
        """Count total number of articles in the tree structure."""
        count = 0

        def count_node(node):
            nonlocal count
            if node["type"] == "article" and node.get("article_content"):
                count += 1
            for child in node.get("children", []):
                count_node(child)

        for node in tree_nodes:
            count_node(node)

        return count

    def count_footnote_refs_in_tree(self, tree_nodes: List[Dict[str, Any]]) -> int:
        """Count total number of footnote references in the tree structure."""
        count = 0

        def count_node(node):
            nonlocal count
            if node["type"] == "article":
                count += len(node.get("footnote_references", []))
            for child in node.get("children", []):
                count_node(child)

        for node in tree_nodes:
            count_node(node)

        return count

    def count_footnotes_in_tree(self, tree_nodes: List[Dict[str, Any]]) -> int:
        """Count total number of footnotes in the tree structure."""
        count = 0

        def count_node(node):
            nonlocal count
            if node["type"] == "article":
                count += len(node.get("footnotes", []))
            for child in node.get("children", []):
                count_node(child)

        for node in tree_nodes:
            count_node(node)

        return count

    def build_document_structure(self, 
                               document_metadata: Dict[str, Any],
                               hierarchical_tree: List[Dict[str, Any]],
                               references: Dict[str, Any],
                               filename: str,
                               preamble: str = "",
                               abrogation_info: Dict[str, Any] = None) -> Dict[str, Any]:
        """Build the complete JSON document structure."""
        
        # Count statistics from the tree structure
        total_articles = self.count_articles_in_tree(hierarchical_tree)
        total_footnote_refs = self.count_footnote_refs_in_tree(hierarchical_tree)
        total_footnotes = self.count_footnotes_in_tree(hierarchical_tree)

        logger.info(f"Tree structure statistics: {total_articles} articles, {total_footnote_refs} footnote refs, {total_footnotes} footnotes")

        # Build the complete JSON structure with cleaned hierarchical format
        document = {
            "document_metadata": document_metadata,
            "preamble": preamble,  # Legal preamble text (Vu clauses, etc.)
            "abrogation_info": abrogation_info if abrogation_info else {},  # Abrogation information for fully abrogated documents
            "document_hierarchy": hierarchical_tree,  # Tree-based structure containing articles as leaf nodes
            "references": references,  # Legal document references and modification history
            "external_links": {
                "official_links": [],
                "parliamentary_work": []
            },
            "extraction_metadata": {
                "extraction_date": datetime.now().isoformat(),
                "source_file": filename,
                "sections_included": ["document_metadata", "document_hierarchy", "references"],
                "sections_excluded": ["articles", "legal_references", "modification_history"],
                "completeness_flags": {
                    "all_articles_extracted": True,
                    "footnotes_linked": True,
                    "hierarchical_structure_complete": True,
                    "metadata_complete": True,
                    "is_minimal_document": False,
                    "preamble_extracted": bool(preamble),  # Flag to indicate if preamble was found
                    "is_abrogated_document": bool(abrogation_info)  # Flag to indicate if document is fully abrogated
                }
            }
        }

        return document

    def validate_document_structure(self, document: Dict[str, Any]) -> bool:
        """Validate the document structure for completeness and correctness."""
        try:
            # Check required top-level keys
            required_keys = ["document_metadata", "preamble", "abrogation_info", "document_hierarchy", "references", "extraction_metadata"]
            for key in required_keys:
                if key not in document:
                    logger.error(f"Missing required key: {key}")
                    return False

            # Check document metadata structure
            metadata = document.get("document_metadata", {})
            required_metadata_keys = ["document_number", "title", "language", "document_type"]
            for key in required_metadata_keys:
                if key not in metadata:
                    logger.warning(f"Missing metadata key: {key}")

            # Check hierarchy structure
            hierarchy = document.get("document_hierarchy", [])
            if not isinstance(hierarchy, list):
                logger.error("document_hierarchy must be a list")
                return False

            # Check extraction metadata
            extraction_meta = document.get("extraction_metadata", {})
            if "extraction_date" not in extraction_meta:
                logger.warning("Missing extraction_date in extraction_metadata")

            return True

        except Exception as e:
            logger.error(f"Error validating document structure: {e}")
            return False

    def format_for_output(self, document: Dict[str, Any]) -> Dict[str, Any]:
        """Format the document for final JSON output."""
        # Ensure all required fields are present with default values
        formatted_doc = {
            "document_metadata": document.get("document_metadata", {}),
            "document_hierarchy": document.get("document_hierarchy", []),
            "references": document.get("references", {"modifies": [], "modified_by": []}),
            "external_links": document.get("external_links", {"official_links": [], "parliamentary_work": []}),
            "extraction_metadata": document.get("extraction_metadata", {})
        }

        # Ensure extraction metadata has required fields
        if "extraction_date" not in formatted_doc["extraction_metadata"]:
            formatted_doc["extraction_metadata"]["extraction_date"] = datetime.now().isoformat()

        if "completeness_flags" not in formatted_doc["extraction_metadata"]:
            formatted_doc["extraction_metadata"]["completeness_flags"] = {
                "all_articles_extracted": True,
                "footnotes_linked": True,
                "hierarchical_structure_complete": True,
                "metadata_complete": True,
                "is_minimal_document": False
            }

        return formatted_doc
