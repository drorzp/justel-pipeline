# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Multi-stage ETL pipeline for processing Belgian legal documents from Justel. Scrapes documents, enriches them with AI-generated titles, normalizes HTML content, generates vector embeddings, and transfers data to MongoDB for a web application.

**Stack:** TypeScript (Node.js) orchestration + Python data collection

## Common Commands

```bash
npm install              # Install dependencies
npm run build            # Build TypeScript to dist/
npm start                # Run full pipeline (production) - requires build first
npm run dev              # Run pipeline in development mode (ts-node)
npm run sync:titles      # Run title synchronization utility
npm run qdrant:hash      # Run vector hashing utility
npm run compare          # Compare documents (current/valid vs older/)
```

Python scraper (in `src/justel-data-processer/`):
```bash
cd src/justel-data-processer && pip install -r requirements.txt && python 000_Master.py
```

No test suite exists (`npm test` is a placeholder).

## Architecture

### Active Pipeline (src/index.ts)

The pipeline runs these stages sequentially:

1. **clearValidFolders()** — Deletes and recreates 5 data folders (current/valid, current/invalid, current/ready/valid, current/ready/invalid, new/valid)
2. **runPythonDataPipeline()** — Spawns 3 Python scripts: `populate_full_list.py` → `run_comprehensive_html_scraping.py` (35 concurrent) → `comprehensive_pipeline.py`
3. **filterJSON()** — Uses `fast-json-patch` to diff current JSON against `data/older/`, copies changed files to `current/ready/` folders. Returns `ArticleChangeInfo[]` listing which articles changed per document.
4. **runLocalFolderBatch()** — 4 calls processing new/valid, new/invalid (insert mode), current/ready/valid, current/ready/invalid (update mode)
5. **updateGet()** — Denormalizes hierarchy labels (gen_1/gen_2/gen_3) into article_contents table
6. **updateOlderFolder()** — Archives all processed JSON files to `data/older/` as baseline for next run

**Commented-out stages:** MongoDB transfer (`moveLawsToMongo`, `moveArticlesToMongo`), LLM batch title generation, HTML restoration, vector embeddings, content snapshots.

### Key Patterns

- **Single pg.Pool** created in `main()`, shared across all stages, closed in `finally`
- **Error signaling:** `process.exitCode = 1` (not `process.exit(1)`) in orchestrator; transfer-to-mongo modules use `process.exit(1)` directly
- **Transaction handling:** Each document processed in its own `BEGIN/COMMIT/ROLLBACK` block (in `DocumentProcessor.processDocument()`)
- **Invalid documents** are imported with `skipArticleContents: true` — only metadata and hierarchy, no article text
- **Processing state** persisted to `src/import-to-pg/processing-state-{prefix}.json` files (gitignored); tracks processed files, errors, timestamps
- **Failed documents** moved to `data/step1/errors/{prefix}/` with `.error.json` sidecar

### Module Guide

| Module | Purpose |
|--------|---------|
| `src/import-to-pg/import.ts` | `DatabaseOperations` class — static methods for all PostgreSQL insert/update/delete operations. Methods take `PoolClient`, caller manages transactions. |
| `src/import-to-pg/process.ts` | `runLocalFolderBatch()` — orchestrates folder processing with state persistence and error handling |
| `src/import-to-pg/llm_title.ts` | Azure OpenAI title generation. `generateNewTitle()` for single docs (called during import), `processAllDocumentTitles()` for batch. Two-pass: if title >80 chars, `refineLongTitle()` retries targeting 70 chars. Regex `createFallbackTitle()` on LLM failure. |
| `src/import-to-pg/updateFromSaverV2.ts` | HTML transformation — `updateArticleContentsFromSaverV2Single()` called inline during import; `updateArticleContentsFromSaverV2Diff()` for batch (currently unused) |
| `src/import-to-pg/upgete_gen_on_articles.ts` | `updateGet()` — denormalizes 3 hierarchy ancestor labels into article_contents rows |
| `src/html-transformer/transform-html.ts` | AI HTML normalization. Singleton `HtmlTransformer` routes by token count: <16K output tokens → Azure GPT-4o, <55K → Gemini 2.5 Flash, above → skip. Only transforms articles matching specific patterns (footnotes, provisions, `° et `). |
| `src/add-to-vector/qdrantCreate.service.ts` | Vector upsert to Qdrant. Collection: `articles_of_law_3072`, model: `text-embedding-3-large` (3072 dims). Chunks text with 7000 token target, 200 overlap. UUID v5 IDs. MD5 hash-based skip for unchanged content. |
| `src/add-to-vector/token-utils.ts` | Tiktoken (`cl100k_base`) utilities — paragraph-aware chunker falls back to sentence splitting then raw token slicing |
| `src/transfer-to-mongo/` | Fetch from PostgreSQL functions (`get_document_data`, `get_article_with_relations1`), `findOneAndReplace` with upsert to MongoDB |
| `src/utils/filterJSON.ts` | Change detection via `fast-json-patch`. Strips timestamps before comparison. For invalid docs, only compares title. 50-concurrent file comparisons via `p-limit`. |
| `src/utils/pythonRunner.ts` | Spawns `python3` subprocesses. `__dirname` resolves to `dist/utils/` in production — Python paths use `../../src` relative. |

### Database Schema (PostgreSQL)

Tables: `documents`, `document_versions`, `document_modifies`, `document_modified_by`, `modified_articles`, `hierarchy_elements`, `article_contents`, `article_contents_saver`, `external_links`, `extraction_metadata`, `document_title`

Stored procedures: `get_document_data($1)`, `get_article_with_relations1($1, $2)`, `reset_and_insert_from_article_content()`

Default PostgreSQL port is **5433** (not 5432).

### MongoDB

Database name hardcoded as `lawyers` in `src/mongodb/mongoConnect.ts`. Uses both native `MongoClient` and Mongoose. Models: `Law` (laws collection), `Article` (compound unique index on article_number + document_number).

### Data Flow

```
Python Scraper → data/step1/ (JSON) → filterJSON (diff against data/older/)
                                                ↓
                          data/step1/new/valid    data/step1/current/ready/valid
                                    ↓                      ↓
                          PostgreSQL (insert)    PostgreSQL (update)
                                    ↓                      ↓
                          MongoDB (final) ← Qdrant (vectors)
```

### Folder Structure

- `data/step1/current/valid/` and `current/invalid/` — Current run output (compared against older)
- `data/step1/current/ready/valid/` and `ready/invalid/` — Changed documents to update
- `data/step1/new/valid/` and `new/invalid/` — New documents to insert
- `data/older/` — Flat archive of all previously processed files (baseline for change detection)
- `data/step1/errors/{prefix}/` — Failed documents with error sidecars
- `logs/` — `pipeline-YYYY-MM-DD.log` (appended all day, not rolled per run)

### Logging

`src/logger.ts` is a singleton `FileLogger` that monkey-patches all `console.*` methods. Imported via side-effect (`import './logger'`). Format: `[ISO-timestamp] [LEVEL] [caller] message`. Supports `createScopedLogger(scope)` for per-module prefixes.

## Environment Variables

Required in `.env`:
- `POSTGRES_HOST`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, `POSTGRES_PORT` (default 5433), `POSTGRES_POOL_MAX` (default 20)
- `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, `AZURE_API_VERSION` — Azure OpenAI for title generation and HTML transformation
- `MONGO_URI` — MongoDB connection (default: `mongodb://lawyer:l123456@localhost:27017/lawyers?authSource=admin`)
- `GOOGLE_API_KEY` or `GEMINI_API_KEY` — Gemini for large HTML transformations
- `OPENAI_API_KEY` — OpenAI for vector embeddings
- `QDRANT_URL` — Qdrant vector DB (default: `http://localhost:6333`)

## TypeScript

- Strict mode enabled, target ES2020, CommonJS modules
- Source in `src/`, builds to `dist/`
- Uses `ts-node` for dev mode
