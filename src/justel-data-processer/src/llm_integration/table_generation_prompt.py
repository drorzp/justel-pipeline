#!/usr/bin/env python3
"""
table_generation_prompt.py - Enhanced prompt templates for table HTML generation using LLM

This module provides improved prompt templates for converting pipe-separated table text
into properly formatted HTML tables for Belgian legal documents.

Author: Enhanced Version (Claude Opus + Augment Agent)
Date: 2025-07-24
"""

import re
import logging
from typing import List, Optional, Dict, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class TableType(Enum):
    """Enumeration of table types in legal documents."""
    STANDARD = "standard"
    BILINGUAL = "bilingual"
    BILINGUAL_PAIRED = "bilingual_paired"  # Dutch/French in alternating rows
    BILINGUAL_SPLIT = "bilingual_split"    # Dutch/French in separate columns


@dataclass
class TableMetadata:
    """Metadata about detected table structure."""
    table_type: TableType
    num_columns: int
    num_rows: int
    has_header: bool
    language_pairs: List[Tuple[str, str]] = None

# Enhanced prompt template with better structure detection
TABLE_GENERATION_PROMPT = """You are an expert at parsing bilingual (Dutch/French) legal document tables. Convert pipe-separated tables to clean HTML.

Rules:
1. Create a proper HTML table with <thead> and <tbody>
2. Add class="legal-table" to the <table> element
3. Add scope="col" to all <th> elements in the header
4. Headers should combine French/Dutch with <br> between them
5. Court names in cells should be "French / Dutch" format
6. Preserve all numbers exactly
7. Output ONLY the HTML table, no explanations

Example output structure:
<table class="legal-table">
  <thead>
    <tr>
      <th scope="col">Juridiction</th>
      <th scope="col">Présidents de chambre /<br>Kamervoorzitters</th>
      ...
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cour d'appel / Hof van beroep</td>
      <td>16</td>
      ...
    </tr>
  </tbody>
</table>

Here is the input data: {table_text}"""


def analyze_table_structure(table_text: str) -> TableMetadata:
    """
    Analyze table structure to determine type and metadata.

    Args:
        table_text: Cleaned table text

    Returns:
        TableMetadata object with analysis results
    """
    lines = table_text.strip().split('\n')
    if not lines:
        return None

    # Count columns from first row
    first_row = lines[0].split('|')
    num_columns = len([col for col in first_row if col.strip()])

    # Detect bilingual indicators
    bilingual_indicators = {
        'nl': ['Hoven', 'Rechtbanken', 'Rechters', 'Substituten', 'Griffiers',
                'Nederlandstalige', 'Nederlandse', 'Kamervoorzitters', 'Raadsheren'],
        'fr': ['Cours', 'Tribunaux', 'Juges', 'Substituts', 'Greffiers',
               'Franstalige', 'Française', 'Présidents', 'Conseillers', 'Avocats']
    }

    # Check for bilingual content
    full_text = ' '.join(lines).lower()
    has_dutch = any(indicator.lower() in full_text for indicator in bilingual_indicators['nl'])
    has_french = any(indicator.lower() in full_text for indicator in bilingual_indicators['fr'])

    # Determine table type
    table_type = TableType.STANDARD
    if has_dutch and has_french:
        # Check if languages are in separate columns or rows
        if len(lines) > 1:
            # Look for pattern of alternating language rows
            if ('nederlandstalige' in lines[1].lower() and
                len(lines) > 2 and 'française' in lines[2].lower()):
                table_type = TableType.BILINGUAL_PAIRED
            else:
                table_type = TableType.BILINGUAL_SPLIT
        else:
            table_type = TableType.BILINGUAL

    # Detect if first row is header
    has_header = any(word in lines[0] for word in
                    ['Hoven', 'Cours', 'Rechtbanken', 'Tribunaux', 'Rechters', 'Juges'])

    return TableMetadata(
        table_type=table_type,
        num_columns=num_columns,
        num_rows=len(lines),
        has_header=has_header
    )


def get_table_generation_prompt(table_text: str, metadata: Optional[TableMetadata] = None) -> str:
    """
    Generate the complete prompt for table HTML generation.

    Args:
        table_text: The pipe-separated table text to convert
        metadata: Optional metadata about table structure (unused in simplified version)

    Returns:
        Complete prompt string for the LLM
    """
    # metadata parameter kept for backwards compatibility but not used in simplified version
    _ = metadata  # Suppress unused parameter warning

    # Clean the table text first
    cleaned_text = clean_table_text(table_text)

    # Use the simplified prompt format
    return TABLE_GENERATION_PROMPT.format(table_text=cleaned_text)


def validate_table_html(html_output: str) -> Tuple[bool, List[str]]:
    """
    Enhanced validation for LLM HTML output with detailed error reporting.

    Args:
        html_output: The HTML output from the LLM

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []

    if not html_output or not html_output.strip():
        return False, ["Empty output"]

    html = html_output.strip()

    # Check for basic table structure
    required_elements = [
        ('<table', '</table>'),
        ('<tr', '</tr>'),
        ('<th', '</th>'),  # At least some headers expected
    ]

    for open_tag, close_tag in required_elements:
        if open_tag not in html:
            errors.append(f"Missing {open_tag}")
        if close_tag not in html:
            errors.append(f"Missing {close_tag}")

    # Check for CSS classes
    if 'legal-table' not in html:
        errors.append("Missing 'legal-table' CSS class")

    # Validate structure hierarchy
    if '<table' in html:
        table_start = html.find('<table')
        table_end = html.rfind('</table>')

        if table_start > 0:
            errors.append("Content before <table> tag")
        if table_end < len(html) - len('</table>'):
            errors.append("Content after </table> tag")

    # Check for proper nesting
    if '<thead>' in html:
        if '</thead>' not in html:
            errors.append("Unclosed <thead> tag")
        if '<tbody>' in html:
            thead_end = html.find('</thead>')
            tbody_start = html.find('<tbody>')
            if thead_end > tbody_start:
                errors.append("Invalid nesting: <tbody> before </thead>")

    # Validate accessibility attributes (optional warning)
    if '<th' in html and 'scope=' not in html:
        errors.append("Missing scope attributes on <th> elements (accessibility)")

    return len(errors) == 0, errors


# Backward compatibility function
def validate_table_html_simple(html_output: str) -> bool:
    """
    Simple validation function for backward compatibility.

    Args:
        html_output: The HTML output from the LLM

    Returns:
        True if the output appears to be a valid HTML table
    """
    is_valid, _ = validate_table_html(html_output)
    return is_valid


def extract_table_from_text(text: str) -> List[str]:
    """
    Extract all pipe-separated tables from text.
    
    Tables are identified by:
    1. Lines starting with "|" 
    2. Usually preceded by an empty line or paragraph text
    3. End when there's a non-table line (no pipes) or empty line

    Args:
        text: Text that may contain table content

    Returns:
        List of extracted table texts
    """
    logger.info(f"🔍 extract_table_from_text called with text length: {len(text) if text else 0}")
    
    tables = []
    lines = text.split('\n')
    current_table = []
    in_table = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check if this line contains pipes (table indicator)
        if '|' in line:
            # Start a new table if we're not in one
            if not in_table:
                in_table = True
                current_table = []
            
            # Add this line to the current table
            current_table.append(stripped if stripped else line)
            
        else:
            # No pipes - we've left the table
            if in_table and current_table:
                # Save the table if it has content
                table_text = '\n'.join(current_table)
                # Clean up the table text
                cleaned_table = clean_table_text(table_text)
                if cleaned_table and len(cleaned_table.split('\n')) >= 1:  # At least 1 row
                    tables.append(cleaned_table)
                
                # Reset for next table
                current_table = []
                in_table = False
    
    # Don't forget the last table if text ends with a table
    if in_table and current_table:
        table_text = '\n'.join(current_table)
        cleaned_table = clean_table_text(table_text)
        if cleaned_table and len(cleaned_table.split('\n')) >= 1:
            tables.append(cleaned_table)

    logger.info(f"📊 Found {len(tables)} tables")

    return tables


def _detect_and_split_multiple_tables(line: str) -> List[str]:
    """
    Detect if a single line contains multiple tables and split them.
    
    This uses pattern recognition to identify table boundaries:
    1. Look for repeating header-like patterns
    2. Detect significant gaps in numeric sequences
    3. Find semantic boundaries (similar column headers repeating)
    """
    cells = [cell.strip() for cell in line.split('|')]
    
    # Clean empty cells
    while cells and not cells[0]:
        cells.pop(0)
    while cells and not cells[-1]:
        cells.pop()
    
    if len(cells) < 20:  # Too small to be multiple tables
        return [_reconstruct_table_from_single_line(line)]
    
    # Strategy 1: Look for major section headers that indicate new tables
    # In Belgian legal docs, major sections like "Rechtbanken/Tribunaux" after "Hoven/Cours" indicate new tables
    major_section_headers = [
        ('Hoven', 'Cours'),
        ('Rechtbanken', 'Tribunaux'),
        ('Politierechtbank', 'Tribunal de police'),
        ('Arbeidsrechtbank', 'Tribunal du travail'),
        ('Ondernemingsrechtbank', 'Tribunal de l\'entreprise')
    ]
    
    # Find cells that contain major section headers
    section_boundaries = []
    
    for i, cell in enumerate(cells):
        cell_lower = cell.lower()
        
        # Check if this cell contains a major section header
        for nl_term, fr_term in major_section_headers:
            if nl_term.lower() in cell_lower or fr_term.lower() in cell_lower:
                # Check if we have a neighboring cell with the paired term
                # This helps confirm it's a section header
                found_pair = False
                for j in range(max(0, i-3), min(len(cells), i+4)):
                    if j != i:
                        neighbor = cells[j].lower()
                        if (nl_term.lower() in cell_lower and fr_term.lower() in neighbor) or \
                           (fr_term.lower() in cell_lower and nl_term.lower() in neighbor):
                            found_pair = True
                            break
                
                # If we found a pair or this is clearly a section header
                if found_pair or (nl_term.lower() in cell_lower and fr_term.lower() in cell_lower):
                    section_boundaries.append(i)
                    break
    
    # Strategy 2: Look for numeric pattern breaks
    # Tables often have numeric columns, and a break in the pattern might indicate a new table
    numeric_positions = []
    for i, cell in enumerate(cells):
        if cell.replace(' ', '').replace(',', '').replace('.', '').isdigit():
            numeric_positions.append(i)
    
    if len(numeric_positions) >= 10:
        # Look for large gaps in numeric positions
        for i in range(1, len(numeric_positions)):
            gap = numeric_positions[i] - numeric_positions[i-1]
            if gap > 15:  # Large gap might indicate table boundary
                # Find the midpoint of the gap
                boundary = numeric_positions[i-1] + gap // 2
                if boundary not in table_starts:
                    table_starts.append(boundary)
    
    # Sort and deduplicate table starts
    table_starts = sorted(list(set(table_starts)))
    
    # If we found multiple table starts, split the tables
    if len(table_starts) > 1:
        tables = []
        
        for idx in range(len(table_starts)):
            start = table_starts[idx]
            end = table_starts[idx + 1] if idx + 1 < len(table_starts) else len(cells)
            
            # Extract cells for this table
            table_cells = cells[start:end]
            
            # Reconstruct the table
            if len(table_cells) >= 5:  # Minimum cells for a table
                reconstructed = _reconstruct_table_from_cells(table_cells, 'generic')
                if reconstructed:
                    tables.append(reconstructed)
        
        # If we successfully split into multiple tables, return them
        if len(tables) > 1:
            return tables
    
    # Fallback: return as single table
    return [_reconstruct_table_from_single_line(line)]


def _split_combined_tables(line: str) -> List[str]:
    """
    Split a line that contains multiple tables based on detecting section headers.
    
    This is a generic approach that looks for patterns indicating new table sections.
    """
    cells = [cell.strip() for cell in line.split('|')]
    
    # Clean empty cells
    while cells and not cells[0]:
        cells.pop(0)
    while cells and not cells[-1]:
        cells.pop()
    
    # Look for potential table section boundaries
    # A section boundary is typically where we see a pattern like:
    # - A cell with a header-like term (e.g., containing 'Court', 'Tribunal', etc.)
    # - Followed by another similar header cell
    # - With relatively few cells between them (typical header row)
    
    section_starts = []
    header_terms = ['Hoven', 'Cours', 'Rechtbanken', 'Tribunaux', 'Court', 'Tribunal', 
                    'Cour', 'Hof', 'Judges', 'Juges', 'Rechters']
    
    for i, cell in enumerate(cells):
        # Check if this cell contains header terms
        if any(term in cell for term in header_terms):
            # Look ahead to see if there's another header term nearby
            for j in range(i + 1, min(i + 15, len(cells))):  # Look ahead up to 15 cells
                if any(term in cells[j] for term in header_terms):
                    # Found a potential header row
                    section_starts.append(i)
                    break
    
    # If we found multiple section starts, split the tables
    if len(section_starts) > 1:
        tables = []
        for idx, start in enumerate(section_starts):
            end = section_starts[idx + 1] if idx + 1 < len(section_starts) else len(cells)
            section_cells = cells[start:end]
            
            # Reconstruct this section as a table
            reconstructed = _reconstruct_table_section(section_cells, cells[:start] if idx == 0 else [])
            if reconstructed:
                tables.append(reconstructed)
        
        return tables
    else:
        # No clear sections found, return as single table
        return [_reconstruct_table_from_single_line(line)]


def _reconstruct_table_section(section_cells: List[str], prefix_cells: List[str] = None) -> str:
    """
    Reconstruct a table section from cells.
    
    Args:
        section_cells: The cells that belong to this table section
        prefix_cells: Any cells before the section that might contain context
    """
    # Combine prefix cells if any (for context)
    all_cells = (prefix_cells or []) + section_cells
    
    # Try to detect the table structure
    # Look for patterns to determine column count
    
    # For Belgian legal tables, common patterns:
    # - Bilingual headers (Dutch | French | numbers...)
    # - Court/tribunal names followed by numbers
    
    # Try to find a reasonable column count by looking for repeating numeric patterns
    numeric_sequences = []
    for i, cell in enumerate(all_cells):
        if cell.replace(' ', '').isdigit():
            numeric_sequences.append(i)
    
    # Estimate column count from numeric patterns
    if len(numeric_sequences) >= 4:
        # Look at gaps between numbers to estimate columns
        gaps = [numeric_sequences[i+1] - numeric_sequences[i] for i in range(len(numeric_sequences)-1)]
        most_common_gap = max(set(gaps), key=gaps.count) if gaps else 10
        estimated_columns = most_common_gap + 1
    else:
        # Fallback: try common column counts
        estimated_columns = 10
    
    # Build rows
    rows = []
    i = 0
    while i < len(section_cells):
        row_cells = section_cells[i:i + estimated_columns]
        if row_cells:
            rows.append(' | '.join(row_cells))
        i += estimated_columns
    
    return '\n'.join(rows) if rows else None


def _estimate_column_count(cells: List[str]) -> int:
    """
    Estimate the number of columns in a table based on cell patterns.
    
    Uses multiple heuristics:
    1. Look for repeating patterns of numeric cells
    2. Look for symmetry in header patterns (bilingual tables)
    3. Common column counts for legal tables
    """
    # Method 1: Look for numeric patterns
    numeric_positions = []
    for i, cell in enumerate(cells):
        if cell.replace(' ', '').replace(',', '').replace('.', '').isdigit():
            numeric_positions.append(i)
    
    if len(numeric_positions) >= 4:
        # Calculate gaps between consecutive numbers
        gaps = []
        for i in range(1, len(numeric_positions)):
            gap = numeric_positions[i] - numeric_positions[i-1]
            if gap > 0 and gap < 20:  # Reasonable gap size
                gaps.append(gap)
        
        if gaps:
            # Find the most common gap
            from collections import Counter
            gap_counts = Counter(gaps)
            most_common_gap = gap_counts.most_common(1)[0][0]
            
            # If this gap appears frequently, it's likely our column count
            if gap_counts[most_common_gap] >= 2:
                return most_common_gap
    
    # Method 2: Look for bilingual header patterns
    # Belgian tables often have Dutch | French pairs
    header_terms = ['Hoven', 'Cours', 'Rechtbanken', 'Tribunaux', 'Rechters', 'Juges']
    header_positions = []
    for i, cell in enumerate(cells[:30]):  # Check first 30 cells
        if any(term in cell for term in header_terms):
            header_positions.append(i)
    
    if len(header_positions) >= 2:
        # If we have multiple headers, the distance might indicate column structure
        first_gap = header_positions[1] - header_positions[0]
        if 8 <= first_gap <= 14:  # Common range for Belgian legal tables
            return first_gap + 2  # Add some buffer
    
    # Method 3: Fallback to common column counts
    total_cells = len(cells)
    common_columns = [14, 12, 10, 8, 6]
    
    for col_count in common_columns:
        if total_cells % col_count < col_count * 0.2:  # Allow up to 20% incomplete last row
            return col_count
    
    # Default fallback
    return 10


def _reconstruct_table_from_single_line(line: str) -> str:
    """
    Reconstruct table structure from a single line with many pipes.

    This handles the case where table content is flattened into one line
    during text processing but still contains the pipe separators.
    """
    # Split by pipes and clean
    cells = [cell.strip() for cell in line.split('|')]

    # Remove empty cells at start/end
    while cells and not cells[0]:
        cells.pop(0)
    while cells and not cells[-1]:
        cells.pop()

    if len(cells) < 10:  # Need substantial content for a table
        return None

    # Try to auto-detect column count based on patterns
    column_count = _estimate_column_count(cells)
    
    # Build rows based on estimated column count
    rows = []
    i = 0
    while i < len(cells):
        row_cells = cells[i:i + column_count]
        if row_cells:
            rows.append(' | '.join(row_cells))
        i += column_count
    
    return '\n'.join(rows) if len(rows) >= 2 else None


def _reconstruct_table_from_cells(cells: List[str], table_type: str = 'generic') -> str:
    """
    Reconstruct a table from a list of cells.
    
    Args:
        cells: List of cell contents
        table_type: Type of table ('hoven', 'rechtbanken', or 'generic')
    
    Returns:
        Reconstructed table as multi-line string
    """
    if not cells or len(cells) < 4:
        return None
    
    # Clean cells
    cleaned_cells = []
    for cell in cells:
        cell = cell.strip()
        if cell:  # Keep non-empty cells
            cleaned_cells.append(cell)
    
    if not cleaned_cells:
        return None
    
    # Determine column count based on table type
    if table_type == 'hoven':
        # Hoven/Cours table typically has 14 columns in Article 186
        # Header: Hoven | Cours | | Kamer-voor-zitters | Raads-heren | ... | | Présidents de chambre | Conseillers | ...
        estimated_columns = 14
    elif table_type == 'rechtbanken':
        # Rechtbanken/Tribunaux table typically has 10 columns
        # Header: Rechtbanken | Tribunaux | | Rechters | Substituten | Griffiers | | Juges | Substituts | Greffiers
        estimated_columns = 10
    else:
        # Generic estimation
        estimated_columns = _estimate_column_count(cleaned_cells)
    
    # Build rows
    rows = []
    i = 0
    
    # For bilingual tables, we need to handle the header specially
    if table_type in ['hoven', 'rechtbanken']:
        # First row is typically the header with bilingual column names
        header_length = estimated_columns
        if len(cleaned_cells) >= header_length:
            header_cells = cleaned_cells[:header_length]
            rows.append(' | '.join(header_cells))
            i = header_length
    
    # Process remaining cells into rows
    while i < len(cleaned_cells):
        # For data rows, we might have varying lengths
        row_cells = []
        row_end = min(i + estimated_columns, len(cleaned_cells))
        
        for j in range(i, row_end):
            row_cells.append(cleaned_cells[j])
        
        if row_cells:
            rows.append(' | '.join(row_cells))
        
        i = row_end
    
    return '\n'.join(rows) if len(rows) >= 2 else None


def _reconstruct_article_186_style_table(cells: List[str]) -> str:
    """Reconstruct Article 186 style bilingual table with proper section separators."""
    # Article 186 has this structure:
    # Header: Hoven | Cours | | Kamer-voor-zitters | Raads-heren | ... | | Présidents de chambre | Conseillers | ...
    # Section 1: Courts (Hof van beroep, Arbeids-hof)
    # Section separator: Rechtbanken | Tribunaux
    # Section 2: Tribunals (various tribunals)

    rows = []

    # Try to find the header row (contains Hoven, Cours)
    header_start = None
    for i, cell in enumerate(cells):
        if 'Hoven' in cell:
            header_start = i
            break

    if header_start is None:
        return None

    # Extract header row (approximately 14 columns for Article 186)
    header_cells = cells[header_start:header_start + 14]
    if len(header_cells) >= 10:  # Need substantial header
        rows.append(' | '.join(header_cells))

    # Extract data rows
    remaining_cells = cells[header_start + 14:]

    # Section separators that should end the first table
    section_separators = ['Rechtbanken', 'Tribunaux']

    # Court names that start new rows
    court_indicators = ['Hof van beroep', 'Cour d\'appel', 'Arbeids-hof', 'Cour du travail']

    i = 0
    while i < len(remaining_cells):
        current_cell = remaining_cells[i]

        # Check if this is a section separator - if so, stop processing this table
        if any(separator in current_cell for separator in section_separators):
            # Stop here - "Rechtbanken | Tribunaux" starts a new table, not part of this one
            break
            
        # Check if this is a court name that starts a new row
        elif any(indicator in current_cell for indicator in court_indicators):
            # Take the next several cells as a row, but check each cell for section separator
            row_length = min(8, len(remaining_cells) - i)
            
            # Check if any of the cells in this row contain a section separator
            row_has_separator = False
            for j in range(i, min(i + row_length, len(remaining_cells))):
                if any(separator in remaining_cells[j] for separator in section_separators):
                    row_length = j - i  # Stop the row before the separator
                    row_has_separator = True
                    break
            
            if row_length > 0:
                row_cells = remaining_cells[i:i + row_length]
                rows.append(' | '.join(row_cells))
            
            if row_has_separator:
                break  # Stop processing after this row
                
            i += row_length
        else:
            i += 1

    return '\n'.join(rows) if len(rows) >= 2 else None


def _reconstruct_rechtbanken_style_table(cells: List[str]) -> str:
    """Reconstruct Rechtbanken/Tribunaux style table (second table in Article 186)."""
    rows = []
    
    # Find where Rechtbanken starts
    rechtbanken_start = None
    for i, cell in enumerate(cells):
        if 'Rechtbanken' in cell:
            rechtbanken_start = i
            break
    
    if rechtbanken_start is None:
        return None
    
    # Extract header row starting from Rechtbanken
    # Pattern: Rechtbanken | Tribunaux | | Rechters | Substituten | Griffiers | | Juges | Substituts | Greffiers
    header_cells = cells[rechtbanken_start:rechtbanken_start + 10]
    if len(header_cells) >= 8:
        rows.append(' | '.join(header_cells))
    
    # Extract data rows
    remaining_cells = cells[rechtbanken_start + 10:]
    
    # Tribunal names that start new rows
    tribunal_indicators = ['rechtbank', 'Tribunal', 'arbeidsrechtbank', 'ondernemingsrechtbank', 'politierechtbank']
    
    i = 0
    while i < len(remaining_cells):
        current_cell = remaining_cells[i]
        
        # Check if this is a tribunal name that starts a new row
        if any(indicator in current_cell for indicator in tribunal_indicators):
            # Take the next several cells as a row (typically 6-8 cells per row)
            row_length = min(10, len(remaining_cells) - i)
            row_cells = remaining_cells[i:i + row_length]
            rows.append(' | '.join(row_cells))
            i += row_length
        else:
            i += 1
    
    return '\n'.join(rows) if len(rows) >= 2 else None


def _reconstruct_generic_table(cells: List[str]) -> str:
    """Generic table reconstruction fallback."""
    # Simple approach: try to group cells into rows of reasonable length
    if len(cells) < 10:
        return None

    # Estimate column count (common table sizes: 6, 8, 10, 12, 14)
    possible_col_counts = [6, 8, 10, 12, 14]

    for col_count in possible_col_counts:
        if len(cells) % col_count == 0 or len(cells) // col_count >= 2:
            rows = []
            for i in range(0, len(cells), col_count):
                row_cells = cells[i:i + col_count]
                if len(row_cells) >= col_count // 2:  # At least half the columns
                    rows.append(' | '.join(row_cells))

            if len(rows) >= 2:
                return '\n'.join(rows)

    return None


def clean_table_text(table_text: str) -> str:
    """
    Enhanced cleaning and normalization of table text.

    Args:
        table_text: Raw table text

    Returns:
        Cleaned table text
    """
    lines = table_text.split('\n')
    cleaned_lines = []

    for line in lines:
        line = line.strip()
        if line and '|' in line:
            # Split by pipe and clean each cell
            cells = line.split('|')
            cleaned_cells = []

            for cell in cells:
                cell = cell.strip()
                # Preserve empty cells but normalize whitespace in non-empty ones
                if cell:
                    # Normalize internal whitespace
                    cell = ' '.join(cell.split())
                cleaned_cells.append(cell)

            # Reconstruct line with consistent spacing
            cleaned_line = ' | '.join(cleaned_cells)
            cleaned_lines.append(cleaned_line)

    return '\n'.join(cleaned_lines)


def post_process_html(html: str) -> str:
    """
    Post-process the generated HTML to ensure consistency.

    Args:
        html: Generated HTML table

    Returns:
        Post-processed HTML
    """
    import re

    # Ensure numeric cells have proper class
    html = re.sub(r'<td>(\d+)</td>', r'<td class="numeric">\1</td>', html)

    # Ensure empty cells have non-breaking space
    html = re.sub(r'<td></td>', '<td>&nbsp;</td>', html)
    html = re.sub(r'<th></th>', '<th>&nbsp;</th>', html)

    # Add newlines for readability
    html = re.sub(r'><', '>\n<', html)

    # Proper indentation
    lines = html.split('\n')
    indented_lines = []
    indent_level = 0
    indent_str = '  '

    for line in lines:
        line = line.strip()
        if line:
            # Decrease indent for closing tags
            if line.startswith('</'):
                indent_level = max(0, indent_level - 1)

            indented_lines.append(indent_str * indent_level + line)

            # Increase indent for opening tags (not self-closing)
            if line.startswith('<') and not line.startswith('</') and not line.endswith('/>'):
                # Don't increase for single-line elements
                if not (line.startswith('<td') or line.startswith('<th')) or '>' not in line[3:]:
                    indent_level += 1

    return '\n'.join(indented_lines)


# Enhanced configuration
TABLE_GENERATION_CONFIG = {
    'bilingual_indicators': {
        'nl': ['Hoven', 'Rechtbanken', 'Rechters', 'Substituten', 'Griffiers',
               'Nederlandstalige', 'Nederlandse', 'Kamervoorzitters', 'Raadsheren',
               'Advocaten-generaal', 'rechtbank', 'hof'],
        'fr': ['Cours', 'Tribunaux', 'Juges', 'Substituts', 'Greffiers',
               'Franstalige', 'Française', 'Présidents', 'Conseillers',
               'Avocats généraux', 'tribunal', 'cour']
    },
    'max_table_size': 100,  # Increased for larger legal documents
    'min_table_rows': 2,
    'min_columns': 2,
    'auto_detect_structure': True,
    'post_process_output': True
}


# Complete pipeline function
def convert_table_to_html(table_text: str, llm_function) -> Tuple[str, Dict]:
    """
    Complete pipeline to convert table text to HTML using an LLM.

    Args:
        table_text: Raw table text
        llm_function: Function that takes a prompt and returns generated text

    Returns:
        Tuple of (html_output, metadata_dict)
    """
    # Extract and clean table
    tables = extract_table_from_text(table_text)
    if not tables:
        return "", {"error": "No table found in text"}

    # Use first table
    table = tables[0]

    # Analyze structure
    metadata = analyze_table_structure(table)

    # Generate prompt
    prompt = get_table_generation_prompt(table, metadata)

    # Call LLM
    html_output = llm_function(prompt)

    # Validate output
    is_valid, errors = validate_table_html(html_output)

    if is_valid and TABLE_GENERATION_CONFIG['post_process_output']:
        html_output = post_process_html(html_output)

    return html_output, {
        "metadata": metadata,
        "is_valid": is_valid,
        "errors": errors,
        "tables_found": len(tables)
    }
