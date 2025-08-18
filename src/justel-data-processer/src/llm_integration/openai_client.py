#!/usr/bin/env python3
"""
openai_client.py - OpenAI API Client for Belgian Legal Document Title Cleaning

This module provides a client for interacting with OpenAI's GPT-4o-mini model
to clean and standardize Belgian legal document titles.

Author: Augment Agent
Date: 2025-07-25
"""

import logging
import time
from typing import List, Dict, Any, Tuple
import openai
from dataclasses import dataclass

from .title_cleaning_prompt import get_title_cleaning_prompt, validate_cleaned_titles

logger = logging.getLogger(__name__)

@dataclass
class OpenAIConfig:
    """Configuration for OpenAI API client."""
    api_key: str
    model: str = "gpt-4o-mini"
    max_retries: int = 3
    retry_delay: float = 1.0
    timeout: int = 30
    max_tokens: int = 4096
    temperature: float = 0.1  # Low temperature for consistent output


class OpenAIAPIError(Exception):
    """Custom exception for OpenAI API errors."""
    pass


class OpenAIClient:
    """
    Client for interacting with OpenAI API for title cleaning.

    This client handles:
    - API authentication and requests
    - Batch processing of titles
    - Error handling and retries
    - Response validation
    """

    def __init__(self, config: OpenAIConfig):
        """
        Initialize the OpenAI client.

        Args:
            config: OpenAIConfig object with API settings
        """
        self.config = config

        # Validate API key
        if not self.config.api_key:
            raise ValueError("API key is required")

        # Initialize OpenAI client
        self.client = openai.OpenAI(api_key=self.config.api_key)

        logger.info(f"Initialized OpenAI client with model: {self.config.model}")

    def _make_api_request(self, prompt: str) -> str:
        """
        Make a single API request to OpenAI.

        Args:
            prompt: The prompt to send to the model

        Returns:
            The model's response text

        Raises:
            OpenAIAPIError: If the API request fails
        """
        for attempt in range(self.config.max_retries):
            try:
                logger.debug(f"Making API request (attempt {attempt + 1}/{self.config.max_retries})")

                response = self.client.chat.completions.create(
                    model=self.config.model,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert legal document titling assistant specializing in Belgian legal documents. Follow the instructions precisely and return only the cleaned titles, one per line."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=self.config.max_tokens,
                    temperature=self.config.temperature,
                    timeout=self.config.timeout
                )

                if response.choices and len(response.choices) > 0:
                    content = response.choices[0].message.content
                    if content:
                        return content.strip()

                raise OpenAIAPIError("Invalid response format from OpenAI API")

            except openai.RateLimitError as e:
                # Rate limit exceeded, wait longer
                wait_time = self.config.retry_delay * (2 ** attempt)
                logger.warning(f"Rate limit exceeded, waiting {wait_time}s before retry")
                time.sleep(wait_time)
                continue

            except openai.APIError as e:
                error_msg = f"OpenAI API error: {str(e)}"
                logger.error(error_msg)

                if attempt == self.config.max_retries - 1:
                    raise OpenAIAPIError(error_msg)

                time.sleep(self.config.retry_delay)
                continue

            except Exception as e:
                error_msg = f"Unexpected error: {str(e)}"
                logger.error(error_msg)

                if attempt == self.config.max_retries - 1:
                    raise OpenAIAPIError(error_msg)

                time.sleep(self.config.retry_delay)
                continue

        raise OpenAIAPIError("Max retries exceeded")
    
    def clean_titles(self, raw_titles: List[str]) -> Tuple[List[str], Dict[str, Any]]:
        """
        Clean a batch of raw titles using the OpenAI API.

        Args:
            raw_titles: List of raw document titles to clean

        Returns:
            Tuple of (cleaned_titles, metadata) where:
            - cleaned_titles: List of cleaned titles in the same order
            - metadata: Dictionary with processing information

        Raises:
            OpenAIAPIError: If the API request fails
            ValueError: If input validation fails
        """
        if not raw_titles:
            return [], {"status": "success", "titles_processed": 0}

        if len(raw_titles) > 50:  # Reasonable batch size limit
            raise ValueError("Batch size too large. Maximum 50 titles per batch.")

        logger.info(f"Cleaning {len(raw_titles)} titles using OpenAI API")

        # Generate the prompt
        prompt = get_title_cleaning_prompt(raw_titles)

        start_time = time.time()

        try:
            # Make the API request
            response_text = self._make_api_request(prompt)

            # Parse the response with improved robustness
            cleaned_titles = []
            for line in response_text.split('\n'):
                line = line.strip()
                # Remove common numbering patterns that OpenAI might add
                line = line.lstrip('0123456789.- ')
                if line:
                    cleaned_titles.append(line)

            # Validate the response with improved error logging
            validation_result = validate_cleaned_titles(raw_titles, cleaned_titles)
            if not validation_result:
                logger.warning(f"Validation failed for batch. Raw count: {len(raw_titles)}, Cleaned count: {len(cleaned_titles)}")
                logger.warning(f"Raw titles: {raw_titles[:3]}...")  # Log first 3 for debugging
                logger.warning(f"Cleaned titles: {cleaned_titles[:3]}...")  # Log first 3 for debugging
                raise OpenAIAPIError("Response validation failed: title count mismatch or invalid format")

            processing_time = time.time() - start_time

            metadata = {
                "status": "success",
                "titles_processed": len(raw_titles),
                "processing_time_seconds": round(processing_time, 2),
                "model_used": self.config.model,
                "timestamp": time.time()
            }

            logger.info(f"Successfully cleaned {len(cleaned_titles)} titles in {processing_time:.2f}s")

            return cleaned_titles, metadata

        except Exception as e:
            processing_time = time.time() - start_time

            metadata = {
                "status": "error",
                "error_message": str(e),
                "titles_processed": 0,
                "processing_time_seconds": round(processing_time, 2),
                "model_used": self.config.model,
                "timestamp": time.time()
            }

            logger.error(f"Failed to clean titles: {str(e)}")
            raise

    def test_connection(self) -> bool:
        """
        Test the connection to the OpenAI API.

        Returns:
            True if connection is successful, False otherwise
        """
        try:
            test_titles = ["Test title for connection verification"]
            _, metadata = self.clean_titles(test_titles)
            return metadata["status"] == "success"
        except Exception as e:
            logger.error(f"Connection test failed: {str(e)}")
            return False


# Backward compatibility aliases
GeminiConfig = OpenAIConfig
GeminiClient = OpenAIClient
GeminiAPIError = OpenAIAPIError
