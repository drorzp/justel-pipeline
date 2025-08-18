#!/usr/bin/env python3
"""
LLM Integration Module for Belgian Legal Document Processing

This module provides LLM-powered title cleaning functionality for Belgian legal documents
using OpenAI's GPT-4o-mini model.

Components:
- openai_client: Low-level API client for OpenAI
- title_cleaning_service: High-level service for title cleaning integration
- title_cleaning_prompt: Prompt templates and validation
- clean_titles: Standalone script for title cleaning

Author: Augment Agent
Date: 2025-07-25
"""

# Import OpenAI client (with backward compatibility aliases)
try:
    from .openai_client import OpenAIClient, OpenAIConfig, OpenAIAPIError
    # Backward compatibility aliases
    GeminiClient = OpenAIClient
    GeminiConfig = OpenAIConfig
    GeminiAPIError = OpenAIAPIError
except ImportError:
    # Fallback if openai_client doesn't exist
    OpenAIClient = None
    OpenAIConfig = None
    OpenAIAPIError = None
    GeminiClient = None
    GeminiConfig = None
    GeminiAPIError = None

from .title_cleaning_service import TitleCleaningService, TitleCleaningConfig
from .title_cleaning_prompt import (
    get_title_cleaning_prompt,
    validate_cleaned_titles,
    TITLE_CLEANING_PROMPT,
    CLEANING_MODES
)
from .table_generation_service import TableGenerationService, TableGenerationConfig, generate_table_html_quick
from .table_generation_prompt import (
    get_table_generation_prompt,
    validate_table_html,
    validate_table_html_simple,
    extract_table_from_text,
    clean_table_text,
    analyze_table_structure,
    post_process_html,
    convert_table_to_html,
    TableType,
    TableMetadata,
    TABLE_GENERATION_CONFIG
)

__all__ = [
    'GeminiClient',
    'GeminiConfig',
    'GeminiAPIError',
    'OpenAIClient',
    'OpenAIConfig',
    'OpenAIAPIError',
    'TitleCleaningService',
    'TitleCleaningConfig',
    'get_title_cleaning_prompt',
    'validate_cleaned_titles',
    'TITLE_CLEANING_PROMPT',
    'CLEANING_MODES',
    'TableGenerationService',
    'TableGenerationConfig',
    'generate_table_html_quick',
    'get_table_generation_prompt',
    'validate_table_html',
    'validate_table_html_simple',
    'extract_table_from_text',
    'clean_table_text',
    'analyze_table_structure',
    'post_process_html',
    'convert_table_to_html',
    'TableType',
    'TableMetadata',
    'TABLE_GENERATION_CONFIG'
]

__version__ = "1.0.0"
