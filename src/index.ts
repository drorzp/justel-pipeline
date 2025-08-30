import 'dotenv/config';
import { Pool, PoolConfig } from 'pg';
import { runS3Batch } from './import-to-pg/process';
import {  moveArticlesToMongo } from './transfer-to-mongo/articles';
import { moveLawsToMongo } from './transfer-to-mongo/laws';
import { truncateImportTables } from './import-to-pg/truncate';
import { saveContentArticle } from './import-to-pg/copyContentArticle';
import { updateArticleContentsFromSaver } from './import-to-pg/updateFromSaver';
import { updateArticleContentsFromSaverV2Diff } from './import-to-pg/updateFromSaverV2';
import { updateArticleVector } from './add-to-vector/loop_over_articles';
import { sync_document_title, titles_not_changed } from './import-to-pg/sync_document_title';
import { processAllDocumentTitles, LLMConfig } from './import-to-pg/llm_title';
import { runPythonDataPipeline } from './utils/pythonRunner';
import { clearS3ZipFiles } from './utils/s3';
import './logger';
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

const pool = new Pool(dbConfig);
  try {
    console.log('Clear S3 folders before running pipeline');
    await clearS3ZipFiles(['incoming3', 'incoming_no_articles3']);
    console.log('Cleared S3 ZIP files from incoming3 and incoming_no_articles3');
    console.log('Collect data and store as json in s3 ');
    await runPythonDataPipeline();
    console.log('Complete Collect data ');
    console.log('truncate article_conten_saver and copy article_content into it started');
    await saveContentArticle(pool); 
    console.log('truncate article_conten_saver and copy article_content into it completed');
    console.log('sync_document_title started')
    await sync_document_title(pool);  
    console.log('sync_document_title completed')
    console.log('truncate tables started');
    await truncateImportTables(pool);  
    console.log('truncate tables completed');
    console.log('runS3Batch incoming3 started');
    await runS3Batch(pool,'incoming3'); 
    console.log('runS3Batch incoming3 completed');
    console.log('runS3Batch incoming_no_articles3 started');
    await runS3Batch(pool,'incoming_no_articles3'); 
    console.log('runS3Batch incoming_no_articles3 completed');
    console.log('runS3Batch revenue_tax_code started');
    await runS3Batch(pool,'revenue_tax_code'); 
    console.log('runS3Batch revenue_tax_code completed');
    console.log('copy all non changed titles to law document started');
    await titles_not_changed(pool);
    console.log('copy all non changed titles to law document completed');
    console.log('llm titles on all new/ changed law document started');
    await processAllDocumentTitles(pool, llmConfig);
    console.log('llm titles on all new/ changed law document completed');
    console.log('copy back all html that was not changed started')
    await updateArticleContentsFromSaver(pool);
    console.log('copy back all html that was not changed completed')
    // console.log('llmall html that was changed/new started')
    // await updateArticleContentsFromSaverV2Diff(pool) 
    // console.log('llmall html that was changed/new completed')
    // console.log('Move to mongo document collection started');
    // await moveLawsToMongo(pool);
    // console.log('Move to mongo document collection completed');
    // await moveArticlesToMongo(pool) // has to replace one by one ???? delete small table 
    // console.log('moveArticlesToMongo started')
    // await updateArticleVector(pool);
    // console.log('moveArticlesToMongo completed')
    // console.log('updateArticleVector started')
    // await updateArticleVector(pool);
    // console.log('updateArticleVector completed');
    // console.log('process completed');
  } catch (err:unknown) {
    const message = err instanceof Error ? err.message : 'Unknown error';
    console.error('Error running batch task:', message);
    process.exitCode = 1;
  } finally {
    await pool.end(); // Temporarily disabled for testing
  }
}

if (require.main === module) {
  main();
}

