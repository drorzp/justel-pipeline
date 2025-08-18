#!/usr/bin/env python3
"""
title_cleaning_prompt.py - LLM Prompt for Belgian Legal Document Title Cleaning

This module contains the prompt template and configuration for cleaning Belgian legal document titles
using Google Gemini 2.5 Flash-Lite Preview 06-17.

Author: Augment Agent
Date: 2025-07-21
"""

import logging

logger = logging.getLogger(__name__)

TITLE_CLEANING_PROMPT = """You are an expert legal document titling assistant for Belgian legal documents. Transform complex raw titles into clear, concise titles for UI display.

**Objective:**
Create readable, scannable titles that preserve legal accuracy while removing clutter. Dates and metadata will be shown separately in the UI.

**Key Rules:**
1. **Focus on Content**: Include the main law/act name and subject matter
2. **Remove Clutter**: Exclude dates, document numbers, publication info, modification notes, and URLs
3. **Keep It Concise**: Aim for 80 characters or less when possible
4. **Preserve Legal Terms**: Maintain French legal terminology and document types (Loi, Décret, Code, etc.)
5. **Article Numbers**: Only include if essential for distinguishing document scope

**Format Guidelines:**
- Use Title Case for main elements
- Use hyphens or colons as separators
- One cleaned title per line
- No extra text or explanations

**Examples:**

Raw Title:
1967101053 10 OCTOBRE 1967. - CODE JUDICIAIRE - Deuxième partie : L'ORGANISATION JUDICIAIRE (article 58 à 555/16)(NOTE 1...)

Cleaned Title:
Code Judiciaire - Organisation Judiciaire

Raw Title:
1911081250 12 AOUT 1911. - Loi pour la conservation de la beauté des paysages.**Publication:**19 août 1911**Numéro:**1911081250

Cleaned Title:
Loi pour la Conservation de la Beauté des Paysages

Raw Title:
REGLEMENT (UE) 2016/679 DU PARLEMENT EUROPÉEN ET DU CONSEIL du 27 avril 2016 relatif à la protection des personnes physiques

Cleaned Title:
Règlement UE - Protection des Données Personnelles

**Process the following raw titles:**
"""

def get_title_cleaning_prompt(raw_titles: list) -> str:
    """
    Generate the complete prompt with the provided raw titles.
    
    Args:
        raw_titles: List of raw document titles to be cleaned
        
    Returns:
        Complete prompt string ready for LLM processing
    """
    if not raw_titles:
        return TITLE_CLEANING_PROMPT + "\n[No titles provided]"
    
    titles_text = "\n".join(raw_titles)
    return TITLE_CLEANING_PROMPT + "\n" + titles_text

def validate_cleaned_titles(raw_titles: list, cleaned_titles: list) -> bool:
    """
    Validate that the cleaned titles match the expected format and count.
    Relaxed validation rules to reduce false rejections.

    Args:
        raw_titles: Original raw titles
        cleaned_titles: LLM-generated cleaned titles

    Returns:
        True if validation passes, False otherwise
    """
    import re
    import logging

    logger = logging.getLogger(__name__)

    if len(raw_titles) != len(cleaned_titles):
        logger.warning(f"Title count mismatch: {len(raw_titles)} raw vs {len(cleaned_titles)} cleaned")
        return False

    for i, cleaned_title in enumerate(cleaned_titles):
        # Basic validation rules
        if not cleaned_title.strip():
            logger.warning(f"Empty title at index {i}")
            return False

        if len(cleaned_title) > 150:  # Increased from 120 to 150 characters
            logger.warning(f"Title too long ({len(cleaned_title)} chars): {cleaned_title[:50]}...")
            return False

        # Check for leftover metadata patterns (case-insensitive but less aggressive)
        metadata_patterns = [
            r'\bpublication\s*:', r'\bnuméro\s*:', r'\bpage\s*:',
            r'\bdossier\s+numéro\s*:', r'\bnote\s+\d+\s*:',
            r'\bversions\s+archivées\b', r'\barrêtés\s+d[\'"]exécution\b'
        ]
        if any(re.search(pattern, cleaned_title, re.IGNORECASE) for pattern in metadata_patterns):
            logger.warning(f"Metadata pattern found in title: {cleaned_title}")
            return False

        # More specific date patterns - only catch actual dates, not article numbers
        date_patterns = [
            r'\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b',  # DD/MM/YYYY or DD-MM-YYYY
            r'\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b',  # YYYY/MM/DD or YYYY-MM-DD
            r'\(\d{4}\)',  # Years in parentheses like (2003)
            r'\b\d{1,2}\s+(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s+\d{4}\b'  # French dates
        ]
        if any(re.search(pattern, cleaned_title, re.IGNORECASE) for pattern in date_patterns):
            logger.warning(f"Date pattern found in title: {cleaned_title}")
            return False

    return True

# Configuration for different cleaning modes
CLEANING_MODES = {
    'ui_optimized': {
        'max_length': 80,
        'preserve_dates': False,
        'preserve_article_ranges': 'selective',  # Only when essential for scope distinction
        'aggressive_abbreviation': False,
        'focus': 'readability_and_scannability'
    },
    'compact': {
        'max_length': 60,
        'preserve_dates': False,
        'preserve_article_ranges': False,
        'aggressive_abbreviation': True,
        'focus': 'maximum_brevity'
    },
    'descriptive': {
        'max_length': 100,
        'preserve_dates': False,
        'preserve_article_ranges': 'selective',
        'aggressive_abbreviation': False,
        'focus': 'legal_context_preservation'
    }
}
