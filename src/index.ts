import 'dotenv/config';
import { PoolConfig } from 'pg';
import { pool, connectPostgreSQL } from './postgres/pgConnect';
import { runS3Batch } from './import-to-pg/process';
import {  moveArticlesToMongo } from './transfer-to-mongo/articles';
import { moveLawsToMongo } from './transfer-to-mongo/laws';
import { truncateImportTables } from './import-to-pg/truncate';
import { callCopyContentArticle } from './import-to-pg/copyContentArticle';
import { updateArticleContentsFromSaver } from './import-to-pg/updateFromSaver';
import { updateArticleContentsFromSaverV2Diff } from './import-to-pg/updateFromSaverV2';
import { updateArticleVector } from './add-to-vector/loop_over_articles';
import { sync_document_title, sync_not_changed } from './import-to-pg/sync_document_title';
import { DocumentTitleProcessor, LLMConfig } from './import-to-pg/llm_title';

export const llmConfig: LLMConfig = {
    openaiApiKey: process.env.OPENAI_API_KEY || '',
    model: 'gpt-4o-mini',
    maxRetries: 2, // Reduced retries for faster failure recovery
    retryDelay: 200, // Minimal retry delay
    requestDelay: 0, // No delay between requests (GPT-4o-mini has very high rate limits)
    concurrentRequests: 300, // EXTREME concurrency - GPT-4o-mini can handle this!
    batchSize: 2000, // Even larger batches for maximum throughput
};

// Pool configuration for DocumentTitleProcessor
const dbConfig: PoolConfig = {
  host: process.env.POSTGRES_HOST || 'localhost',
  port: Number(process.env.POSTGRES_PORT) || 5433,
  user: process.env.POSTGRES_USER,
  password: process.env.POSTGRES_PASSWORD,
  database: process.env.POSTGRES_DB,
  ssl: false,
};

async function main() {

  await connectPostgreSQL();
  try {
    const { rows } = await pool.query('SELECT NOW() as now');
    console.log('DB connected. Time:', rows[0].now);
    // shahars code goes here 
    await callCopyContentArticle();
    await truncateImportTables();
    await runS3Batch(); // create all tables 
    await sync_document_title();  
    await sync_not_changed();
    const llmTitleProcessor = new DocumentTitleProcessor(dbConfig, llmConfig);
    await llmTitleProcessor.connect();
    try {
      await llmTitleProcessor.processAllDocumentTitles();
    } finally {
      await llmTitleProcessor.disconnect();
    }
    updateArticleContentsFromSaver() // this one will restore the html that was not changed
    updateArticleContentsFromSaverV2Diff() // this one will restore the html that was not changed
    updateArticleVector();
    moveLawsToMongo();
    await moveArticlesToMongo() // has to replace one by one ???? delete small table 

    // Run S3 batch processor programmatically
  
  } catch (err) {
    console.error('Error running batch task:', err);
    process.exitCode = 1;
  } finally {
    await pool.end();
  }
}

if (require.main === module) {
  main();
}
