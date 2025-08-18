# LLM Integration for Belgian Legal Document Title Cleaning

This module provides LLM-powered title cleaning functionality for Belgian legal documents using Google Gemini 2.5 Flash-Lite Preview 06-17.

## Overview

The LLM integration cleans and standardizes document titles for better UI display while preserving original data. It transforms complex, verbose legal document titles into concise, readable titles suitable for user interfaces.

## Features

- **LLM-Powered Cleaning**: Uses Google Gemini 2.5 Flash-Lite Preview 06-17 for intelligent title cleaning
- **Data Preservation**: Moves original titles to `raw_title` field, stores cleaned titles in `title` field
- **Backwards Compatibility**: Maintains existing JSON structure and adds new fields
- **Batch Processing**: Efficiently processes multiple documents with rate limiting
- **Error Handling**: Comprehensive error recovery and fallback mechanisms
- **Pipeline Integration**: Seamlessly integrates into existing processing pipeline
- **Standalone Usage**: Can be run independently on existing JSON files

## Components

### Core Modules

- **`gemini_client.py`**: Low-level API client for Google Gemini
- **`title_cleaning_service.py`**: High-level service for title cleaning integration
- **`title_cleaning_prompt.py`**: Prompt templates and validation logic
- **`clean_titles.py`**: Standalone script for title cleaning
- **`MD9_clean_titles.py`**: Pipeline integration script

### Configuration

The system uses the following API key by default:
```
AIzaSyCUlqC2-3r62pQojG4kANUdFd6BHG2uKeM
```

## Usage

### Standalone Script

Clean titles in a single file:
```bash
python src/llm_integration/clean_titles.py --file output/24/1967101053.json
```

Clean titles in all JSON files in a directory:
```bash
python src/llm_integration/clean_titles.py --directory output/24
```

Test API connection:
```bash
python src/llm_integration/clean_titles.py --test-connection
```

### Pipeline Integration

The title cleaning is automatically included in the main processing pipeline as step MD9. It runs after JSON extraction (MD8) and processes all generated JSON files.

### Programmatic Usage

```python
from src.llm_integration import TitleCleaningService, TitleCleaningConfig

# Configure the service
config = TitleCleaningConfig(
    api_key="your_api_key",
    batch_size=20,
    enable_cleaning=True
)

# Initialize service
service = TitleCleaningService(config)

# Process a directory
results = service.process_directory(Path("output/24"))
```

## Data Structure Changes

### Before Cleaning
```json
{
  "document_metadata": {
    "title": "1967101053 10 OCTOBRE 1967. - CODE JUDICIAIRE - Deuxième partie : L'ORGANISATION JUDICIAIRE (article 58 à 555/16)(NOTE 1 : art. 259bis-15 modifiés...)",
    "document_number": "1967101053"
  }
}
```

### After Cleaning
```json
{
  "document_metadata": {
    "title": "Code Judiciaire - Organisation Judiciaire (Art. 58-555/16)",
    "raw_title": "1967101053 10 OCTOBRE 1967. - CODE JUDICIAIRE - Deuxième partie : L'ORGANISATION JUDICIAIRE (article 58 à 555/16)(NOTE 1 : art. 259bis-15 modifiés...)",
    "document_number": "1967101053",
    "title_cleaning": {
      "cleaned_at": 1642781234.567,
      "cleaning_method": "gemini_llm",
      "original_length": 245,
      "cleaned_length": 52
    }
  }
}
```

## Title Cleaning Rules

The LLM follows these rules when cleaning titles:

### Include
- Main law or act name (e.g., "Code Judiciaire", "Loi sur la protection des données")
- Specific part or subject matter
- Important article ranges that define scope
- Essential dates for document identification

### Exclude
- Internal document identifiers (long numbers)
- Extensive modification notes (NOTE 1, NOTE 2, etc.)
- Links and URLs
- Archived versions and execution decree counts
- Repetitive metadata labels

### Format
- Title Case for main elements
- Clear separators (hyphens, colons)
- Maximum ~100 characters when feasible
- Clean article numbering (e.g., "Art. 58-555/16")

## Error Handling

The system includes comprehensive error handling:

- **API Failures**: Falls back to preserving original title with `raw_title` field
- **Rate Limiting**: Automatic retry with exponential backoff
- **Invalid Responses**: Validation and fallback mechanisms
- **Network Issues**: Timeout handling and retry logic
- **File Errors**: Graceful handling of malformed JSON files

## Configuration Options

### TitleCleaningConfig

- `api_key`: Google Gemini API key
- `batch_size`: Number of files to process in each batch (default: 20)
- `enable_cleaning`: Enable/disable LLM cleaning (default: True)
- `fallback_on_error`: Use fallback on API errors (default: True)
- `delay_between_batches`: Delay between API calls (default: 0.5s)
- `log_cleaning_results`: Log individual cleaning results (default: True)

### GeminiConfig

- `model`: Gemini model to use (default: "gemini-2.5-flash-lite-preview-06-17")
- `max_retries`: Maximum API retry attempts (default: 3)
- `timeout`: Request timeout in seconds (default: 30)
- `temperature`: Model temperature for consistency (default: 0.1)

## Testing

Run the comprehensive test suite:

```bash
python -m pytest tests/test_llm_title_cleaning.py -v
```

The tests cover:
- Prompt generation and validation
- API client functionality
- Service integration
- Error handling scenarios
- End-to-end processing

## Monitoring and Logging

The system provides detailed logging:

- Processing progress and statistics
- API call results and timing
- Error conditions and recovery
- Individual title cleaning results

Log files are created in the working directory:
- `title_cleaning.log`: Detailed processing log

## Performance Considerations

- **Batch Size**: Default 20 files per batch to balance efficiency and rate limits
- **Rate Limiting**: 0.5s delay between batches to avoid API throttling
- **Timeout**: 30s timeout per API request
- **Retries**: Up to 3 retries with exponential backoff

## Dependencies

- `requests`: HTTP client for API calls
- `pathlib`: File system operations
- `json`: JSON processing
- `logging`: Comprehensive logging
- `dataclasses`: Configuration objects

## API Costs

Google Gemini 2.5 Flash-Lite Preview 06-17 is designed for cost-effective processing. Typical costs for title cleaning are minimal due to:

- Short input texts (document titles)
- Short output texts (cleaned titles)
- Efficient batch processing
- Low temperature setting for consistency

## Troubleshooting

### Common Issues

1. **API Connection Failures**
   - Check API key validity
   - Verify network connectivity
   - Check rate limits

2. **Title Validation Failures**
   - Review prompt template
   - Check for unexpected response format
   - Verify title count matching

3. **File Processing Errors**
   - Ensure JSON files are valid
   - Check file permissions
   - Verify directory structure

### Debug Mode

Enable verbose logging for troubleshooting:

```bash
python src/llm_integration/clean_titles.py --directory output/24 --verbose
```
