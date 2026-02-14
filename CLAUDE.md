# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a multi-stage ETL pipeline for processing Belgian legal documents from Justel. The pipeline scrapes documents, enriches them with AI-generated titles, normalizes HTML content, generates vector embeddings, and transfers data to MongoDB for web application use.

**Stack:** TypeScript (Node.js) orchestration + Python data collection

## Common Commands

```bash
# Install dependencies
npm install

# Build TypeScript to dist/
npm run build

# Run the full pipeline (production)
npm start

# Run the pipeline in development mode
npm run dev

# Run title synchronization utility
npm run sync:titles

# Run vector hashing utility
npm run qdrant:hash

# Python scraper (in src/justel-data-processer/)
cd src/justel-data-processer
pip install -r requirements.txt
python 000_Master.py
```

## Architecture

### Python Scraping Pipeline (runPythonDataPipeline)

Scrapes Belgian legal documents from `https://www.ejustice.just.fgov.be`:

1. **populate_full_list.py** - Discover new document URLs since last run, append to `data/csv_data/full-list.csv`
2. **run_comprehensive_html_scraping.py** - Download HTML for each URL (35 concurrent, ~23 URLs/sec) → `input/*.txt`
3. **comprehensive_pipeline.py** - Parse HTML → JSON, validate, output to `data/step1/valid/` and `data/step1/invalid/`

### Pipeline Stages (executed sequentially in src/index.ts)

1. **Clear Local Folder** - Remove old files from `data/step1/`
2. **Python Data Collection** - Run scraper via `runPythonDataPipeline()`, outputs JSON to `data/step1/`
3. **Save Content Snapshot** - Backup original HTML to `article_contents_saver` table
4. **Title Sync** - Synchronize existing titles via `sync_document_title()`
5. **Truncate Import Tables** - Clear staging tables
6. **Local Folder Import** - Load JSON files from `data/step1/valid/` and `data/step1/invalid/`
7. **Flag Unchanged** - Mark documents with unchanged content via `titles_not_changed()`
8. **LLM Title Generation** - Generate clean titles via Azure OpenAI gpt-4o (300 concurrent, batch 2000)
9. **HTML Restoration** - Restore original HTML for unchanged articles, diff-based for changed
10. **Update Gen** - Update generation metadata via `updateGet()`
11. **MongoDB Transfer** - Move laws (batch 20) and articles to MongoDB
12. **Vector Embeddings** - Generate embeddings for Qdrant

### Key Modules

- **src/import-to-pg/** - Local folder processing, document validation, PostgreSQL import, LLM title generation
- **src/add-to-vector/** - Vector embedding generation with Qdrant, token management with tiktoken
- **src/transfer-to-mongo/** - MongoDB transfer with Mongoose models
- **src/html-transformer/** - HTML content normalization
- **src/justel-data-processer/** - Python scraper and preprocessor

### Data Flow

```
Python Scraper → data/step1/ (JSON files) → PostgreSQL (staging/enrichment) → MongoDB (final storage)
                                                      ↓
                                            Qdrant (vector embeddings)
```

### Database Functions

PostgreSQL uses PL/pgSQL functions for data retrieval:
- `get_document_data($1)` - Fetch law document with full structure
- `get_article_with_relations1($1, $2)` - Fetch article with relations

## Environment Variables

Key variables needed in `.env`:
- `POSTGRES_*` - PostgreSQL connection (host, user, password, db, port)
- `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, `AZURE_API_VERSION` - Azure OpenAI for title generation
- `MONGO_URI` - MongoDB connection string

## Logging

The pipeline uses a file-based logging system (src/logger.ts) that:
- Creates timestamped log files in `logs/` directory
- Intercepts all console methods
- Captures uncaught exceptions
- Supports scoped loggers per module

## LLM Configuration

Title generation uses Azure OpenAI (configured in `src/index.ts`):
- Model: `gpt-4o`
- Concurrent requests: 300
- Batch size: 2000
