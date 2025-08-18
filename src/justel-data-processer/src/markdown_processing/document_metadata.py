#!/usr/bin/env python3
"""
document_metadata.py - Document metadata extraction for Belgian Legal Documents

This module handles extraction of document metadata including NUMAC, publication information,
document titles, dates, and official links from Belgian legal documents.

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


class DocumentMetadataExtractor:
    """
    Extracts document metadata from Belgian legal documents.
    """
    
    def __init__(self, utils: ExtractionUtils):
        """Initialize with utility functions."""
        self.utils = utils

    def extract_publication_metadata(self, content: str) -> Dict[str, Any]:
        """Extract publication metadata from document header."""
        metadata = {
            "publication_date": "",
            "belgian_monitor_number": "",
            "page_number": "",
            "numac": "",
            "dossier_number": "",
            "effective_date": "",
            "end_validity_date": ""
        }

        # Extract publication date
        pub_match = self.utils.publication_date_pattern.search(content)
        if pub_match:
            metadata["publication_date"] = pub_match.group(1).strip()

        # Extract NUMAC from content
        numac_match = self.utils.numac_content_pattern.search(content)
        if numac_match:
            metadata["numac"] = numac_match.group(1).strip()

        # Extract page number
        page_match = self.utils.page_pattern.search(content)
        if page_match:
            metadata["page_number"] = page_match.group(1).strip()

        # Extract dossier number
        dossier_match = self.utils.dossier_pattern.search(content)
        if dossier_match:
            metadata["dossier_number"] = dossier_match.group(1).strip()
        else:
            # Fallback: Look for minimal document pattern "Dossier numéro : [number]"
            dossier_minimal_match = self.utils.dossier_minimal_pattern.search(content)
            if dossier_minimal_match:
                metadata["dossier_number"] = dossier_minimal_match.group(1).strip()

        # Extract effective date
        effective_match = self.utils.effective_date_pattern.search(content)
        if effective_match:
            metadata["effective_date"] = effective_match.group(1).strip()

        # Extract end of validity date
        end_validity_match = self.utils.end_validity_date_pattern.search(content)
        if end_validity_match:
            metadata["end_validity_date"] = end_validity_match.group(1).strip()

        return metadata

    def extract_full_document_title(self, content: str) -> str:
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
            # Skip NUMAC line (10-character alphanumeric document number)
            if len(line) == 10 and re.match(r'^[A-Z0-9]{10}$', line, re.IGNORECASE):
                continue
            if line.startswith("**"):  # Stop at metadata fields
                break
            title_lines.append(line)

        return ' '.join(title_lines).strip()

    def extract_document_source(self, content: str) -> str:
        """Extract the document source/authority."""
        source_match = self.utils.source_pattern.search(content)
        if source_match:
            return source_match.group(1).strip()
        return ""

    def extract_version_information(self, content: str) -> Dict[str, Any]:
        """Extract version and execution information."""
        version_info = {
            "archived_versions_count": 0,
            "archived_versions_url": "",
            "execution_orders_count": 0,
            "execution_orders_url": ""
        }

        # Extract archived versions
        archived_match = self.utils.archived_versions_pattern.search(content)
        if archived_match:
            version_info["archived_versions_count"] = int(archived_match.group(1))
            # Extract URL from the link
            archived_url_match = re.search(r'\*\*\[\d+\s+versions\s+archivees\]\(([^)]+)\)', content)
            if archived_url_match:
                version_info["archived_versions_url"] = archived_url_match.group(1)

        # Extract execution orders
        execution_match = self.utils.execution_orders_pattern.search(content)
        if execution_match:
            version_info["execution_orders_count"] = int(execution_match.group(1))
            # Extract URL from the link
            execution_url_match = re.search(r'\*\*\[\d+\s+arrêtes\s+d\'execution\]\(([^)]+)\)', content)
            if execution_url_match:
                version_info["execution_orders_url"] = execution_url_match.group(1)

        return version_info

    def extract_official_links(self, content: str) -> Dict[str, str]:
        """
        Extract official links from the '[5A] [6A] ## Lien [6B]s [5B]' section.

        Returns a dictionary with:
        - official_justel_url: The ELI canonical law link
        - official_publication_pdf_url: Link to the official publication PDF
        - consolidated_pdf_url: Link to the consolidated PDF version
        """
        links = {
            "official_justel_url": "",
            "official_publication_pdf_url": "",
            "consolidated_pdf_url": ""
        }

        try:
            # Extract the links section (first occurrence, not "externes")
            links_pattern = r'\[5A\] \[6A\] ## Lien \[6B\]s \[5B\]\s*\n(.*?)(?:\[5A\] \[6A\] ## Lien \[6B\]s \[5B\] externes|$)'
            links_match = re.search(links_pattern, content, re.DOTALL)

            if links_match:
                links_content = links_match.group(1).strip()

                # Extract canonical URL (ELI link) - typically in angle brackets
                canonical_pattern = r'<(https://www\.ejustice\.just\.fgov\.be/eli/[^>]+)>'
                canonical_match = re.search(canonical_pattern, links_content)
                if canonical_match:
                    links["official_justel_url"] = canonical_match.group(1)

                # Extract official publication PDF link
                publication_pattern = r'\[Image de la publication officielle\]\((https://www\.ejustice\.just\.fgov\.be/mopdf/[^)]+)\)'
                publication_match = re.search(publication_pattern, links_content)
                if publication_match:
                    links["official_publication_pdf_url"] = publication_match.group(1)

                # Extract consolidated PDF link
                consolidated_pattern = r'\[PDF version consolidée\]\((https://www\.ejustice\.just\.fgov\.be/img_l/pdf/[^)]+)\)'
                consolidated_match = re.search(consolidated_pattern, links_content)
                if consolidated_match:
                    links["consolidated_pdf_url"] = consolidated_match.group(1)

        except Exception as e:
            logger.warning(f"Error extracting official links: {str(e)}")

        return links

    def extract_references(self, content: str) -> Dict[str, Any]:
        """
        Extract legal document references from the source document.

        Returns a dictionary with:
        - modifies: List of documents this text modifies (from "Ce texte modifie les textes suivants" section)
        - modified_by: List of modifications made to this document (from "Fiche des modifications" section)
        """
        references = {
            "modifies": [],
            "modified_by": []
        }

        try:
            # Extract "modifies" section
            modifies_pattern = r'\*\*Ce texte modifie les textes suivants:\*\*\s*\n\s*(.+?)(?:\n\s*\n|\n\s*\*\*|$)'
            modifies_match = re.search(modifies_pattern, content, re.DOTALL)

            if modifies_match:
                modifies_text = modifies_match.group(1).strip()
                # Extract NUMAC and URL pairs from bracketed links
                link_pattern = r'\[(\d{10}[A-Z]?\d*)\]\((https://www\.ejustice\.just\.fgov\.be/cgi_loi/article\.pl\?[^)]+)\)'

                for match in re.finditer(link_pattern, modifies_text):
                    numac = match.group(1)
                    url = match.group(2)
                    references["modifies"].append({
                        "numac": numac,
                        "url": url
                    })

            # Extract "modified_by" section from Fiche des modifications
            fiche_pattern = r'\[4A\] ## Fiche des modifications \[4B\]\s*\n(.*?)(?:\[5A\]|\[6A\]|$)'
            fiche_match = re.search(fiche_pattern, content, re.DOTALL)

            if fiche_match:
                fiche_content = fiche_match.group(1).strip()

                # Parse modification entries
                # Pattern: bullet point with link, followed by "Articles modifiés" line
                modification_pattern = r'\*\s*\[([^\]]+)\]\(([^)]+)\)\s*\n\s*Articles? modifiés?\s*:\s*([^\n]+)'

                for match in re.finditer(modification_pattern, fiche_content):
                    modification_title = match.group(1).strip()
                    modification_url = match.group(2).strip()
                    modified_articles = match.group(3).strip()

                    # Parse modification details from title
                    # Expected format: "Type du date publié le date"
                    title_parts = modification_title.split(' publié le ')
                    modification_type_date = title_parts[0] if title_parts else modification_title
                    publication_date = title_parts[1] if len(title_parts) > 1 else ""

                    # Extract modification type and date
                    type_date_pattern = r'^([^d]+du\s+)([0-9-]+)'
                    type_date_match = re.search(type_date_pattern, modification_type_date)

                    modification_type = ""
                    modification_date = ""
                    if type_date_match:
                        modification_type = type_date_match.group(1).strip().rstrip(' du')
                        modification_date = type_date_match.group(2)

                    # Parse publication date to ISO format
                    pub_date_iso = self.utils.parse_date_to_iso(publication_date) if publication_date else ""
                    mod_date_iso = self.utils.parse_date_to_iso(modification_date) if modification_date else ""

                    # Parse modified articles list
                    articles_list = [art.strip() for art in modified_articles.replace(';', ',').split(',') if art.strip()]

                    references["modified_by"].append({
                        "modification_type": modification_type,
                        "modification_date": mod_date_iso,
                        "publication_date": pub_date_iso,
                        "modified_articles": articles_list,
                        "source_url": modification_url,
                        "full_title": modification_title
                    })

        except Exception as e:
            logger.warning(f"Error extracting references: {str(e)}")

        return references

    def extract_document_metadata(self, content: str, filename: str, publication_metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Extract comprehensive document metadata from the content."""
        # Extract NUMAC from filename as fallback
        numac_from_filename = self.utils.extract_numac_from_filename(filename)

        # Extract document number (NUMAC) - prefer from content, fallback to dossier number, then filename
        document_number = publication_metadata.get("numac", "")
        if not document_number:
            # Try dossier number as document number for minimal documents
            dossier_number = publication_metadata.get("dossier_number", "")
            # Check if dossier number is a valid 10-character alphanumeric document number
            if dossier_number and len(dossier_number) == 10 and re.match(r'^[A-Z0-9]{10}$', dossier_number, re.IGNORECASE):
                document_number = dossier_number
            else:
                # Final fallback to filename
                document_number = numac_from_filename

        # Extract full document title with all notes and version information
        title = self.extract_full_document_title(content)

        # Extract publication date and convert to ISO format
        publication_date = self.utils.parse_date_to_iso(publication_metadata.get("publication_date", ""))

        # Extract source/authority
        source = self.extract_document_source(content)

        # Extract page number as integer
        page_number = self.utils.parse_page_number(publication_metadata.get("page_number", ""))

        # Extract dossier number
        dossier_number = publication_metadata.get("dossier_number", "")

        # Extract effective date and convert to ISO format
        effective_date = self.utils.parse_date_to_iso(publication_metadata.get("effective_date", ""))

        # Extract end of validity date and convert to ISO format
        end_validity_date = self.utils.parse_date_to_iso(publication_metadata.get("end_validity_date", ""))

        # Extract version information
        version_info = self.extract_version_information(content)

        # Extract official links from the links section
        official_links = self.extract_official_links(content)

        # Determine document type from official_justel_url (preferred method)
        # Fall back to title-based extraction if URL is not available
        document_type = "unknown"
        if official_links.get("official_justel_url"):
            document_type = self.utils.extract_document_type_from_url(official_links["official_justel_url"])

        # Fallback to title-based extraction if URL method fails
        if document_type == "unknown":
            document_type = self.utils.extract_document_type(title)

        # Determine document status based on end of validity date
        status = "active"
        if end_validity_date:
            status = "abrogated"

        return {
            "document_number": document_number,
            "title": title,
            "publication_date": publication_date,
            "source": source,
            "page_number": page_number,
            "dossier_number": dossier_number,
            "effective_date": effective_date,
            "end_validity_date": end_validity_date,
            "language": "fr",  # Belgian legal documents are in French
            "document_type": document_type,
            "status": status,
            "version_info": version_info,
            "official_justel_url": official_links["official_justel_url"],
            "official_publication_pdf_url": official_links["official_publication_pdf_url"],
            "consolidated_pdf_url": official_links["consolidated_pdf_url"]
        }
