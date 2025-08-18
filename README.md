# justel-pipeline
pipeline that scrapes  from justel and add to postgres/mongo

## Pipeline overview
The entry point is `src/index.ts`. It connects to PostgreSQL and then runs a sequence of import, sync, enrichment, and transfer steps.

## Steps executed in `src/index.ts`
1. __Copy raw HTML into saver table__ — `callCopyContentArticle()` from `src/import-to-pg/copyContentArticle.ts`
   - Truncates `article_contents_saver` and copies all article HTML into it (staging snapshot before transformations).

2. __Clean import tables__ — `truncateImportTables()` from `src/import-to-pg/truncate.ts`
   - Clears import-related tables to ensure a fresh run.

3. __Ingest from S3__ — `runS3Batch()` from `src/import-to-pg/process.ts`
   - Creates/loads tables from S3 batch data (foundational load into Postgres).

4. __Sync existing document titles__ — `sync_document_title()` from `src/import-to-pg/sync_document_title.ts`
   - Aligns titles for documents that already have a known title from the source.

5. __Mark unchanged documents__ — `sync_not_changed()` from `src/import-to-pg/sync_document_title.ts`
   - Flags docs whose content didn’t change, to minimize unnecessary updates.

6. __Generate/normalize titles with LLM (high throughput)__
   - Constructs `DocumentTitleProcessor` (`src/import-to-pg/llm_title.ts`) with `llmConfig` (model: `gpt-4o-mini`).
   - Calls `processAllDocumentTitles()` to fill or standardize titles at scale.

7. __Restore article HTML for unchanged docs__ — `updateArticleContentsFromSaver()` from `src/import-to-pg/updateFromSaver.ts`
   - Restores original HTML for items detected as unchanged.

8. __Apply diff-based HTML restoration for changed docs__ — `updateArticleContentsFromSaverV2Diff()` from `src/import-to-pg/updateFromSaverV2.ts`
   - Restores/merges HTML for items that changed using a diff-aware approach.

9. __Update vector embeddings__ — `updateArticleVector()` from `src/add-to-vector/loop_over_articles.ts`
   - Computes/updates embeddings and writes them to the vector store (Qdrant).

10. __Transfer laws to MongoDB__ — `moveLawsToMongo()` from `src/transfer-to-mongo/laws.ts`
    - Pushes law entities from Postgres into Mongo.

11. __Transfer articles to MongoDB__ — `moveArticlesToMongo()` from `src/transfer-to-mongo/articles.ts`
    - Moves articles into Mongo; may operate record-by-record.

## Configuration
- Postgres connection: `src/postgres/pgConnect.ts` (env: `POSTGRES_*`).
- OpenAI/LLM config: `llmConfig` in `src/index.ts` (env: `OPENAI_API_KEY`).
- Example env: see `.env.example`.

## Run
- Install deps: `npm i`
- Build/run (TS): `npm run build && node dist/index.js` or `ts-node src/index.ts`
- Ensure Postgres, Mongo, and S3 credentials are configured in your environment.
