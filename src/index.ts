import 'dotenv/config';
import { Pool, PoolConfig } from 'pg';
import { runS3Batch } from './import-to-pg/process';
import {  moveArticlesToMongo } from './transfer-to-mongo/articles';
import { moveLawsToMongo } from './transfer-to-mongo/laws';
import { truncateImportTables } from './import-to-pg/truncate';
import { copyContentArticle } from './import-to-pg/copyContentArticle';
import { updateArticleContentsFromSaver } from './import-to-pg/updateFromSaver';
import { updateArticleContentsFromSaverV2Diff } from './import-to-pg/updateFromSaverV2';
import { updateArticleVector } from './add-to-vector/loop_over_articles';
import { sync_document_title, sync_not_changed } from './import-to-pg/sync_document_title';
import { processAllDocumentTitles, LLMConfig } from './import-to-pg/llm_title';
import { runPythonDataPipeline } from './utils/pythonRunner';
import { clearS3ZipFiles } from './utils/s3';
import './logger';
import * as path from 'path';
import { downloadAndUnzip, processS3HtmlUpdate, updateHtml } from './import_article_html/import_article_html';
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
    // Clear S3 folders before running pipeline
    //  await clearS3ZipFiles(['incoming3', 'incoming_no_articles3']);
    // console.log('Cleared S3 ZIP files from incoming3 and incoming_no_articles3');
    // await runPythonDataPipeline();
    // console.log(`started `); // Fixed console.log syntax
    // await copyContentArticle(pool); 
    // // console.log('copyContentArticle')  // truncate the article_contents_saver table and copy all html into it
    // await truncateImportTables(pool);  
    // // console.log('truncateImportTables')   /// clean all tables
    // await runS3Batch(pool,'incoming3'); 
    // // console.log('runS3Batch incoming3'); // create all tables 
    // await runS3Batch(pool,'incoming_no_articles3'); 
    // // console.log('runS3Batch incoming_no_articles3/'); // create all tables 
    // // // Create Tax IRS Revenue Articles of Laws
    // await runS3Batch(pool,'revenue_tax_code'); 
    // console.log('runS3Batch revenue_tax_code/'); // create all tables 

    // await sync_document_title(pool);  
    // console.log('sync_document_title')
    // await sync_not_changed(pool);
    // console.log('sync_not_changed');
    // await processAllDocumentTitles(pool, llmConfig);
    // console.log('processAllDocumentTitles');
    // const HTML_FOLDER = path.join(__dirname, process.env.HTML_FOLDER_PATH!); // Adjust this path to your actual HTML data directory
    // console.log('update article html', HTML_FOLDER);
    // await updateHtml(pool,HTML_FOLDER);
    // downloadAndUnzip(pool, process.env.S3_BUCKET_NAME!, process.env.S3_ZIP_KEY!);
    // await updateArticleContentsFromSaver(pool);
    // console.log('updateArticleContentsFromSaver'); // not sure we need it since it is the same ? this one will restore the html that was not changed
    // await updateArticleContentsFromSaverV2Diff(pool) 
    // console.log('updateArticleContentsFromSaverV2Dif');
    // await processS3HtmlUpdate(pool, 'article-zip', 'htmls/htmls.zip');
    // console.log('processS3HtmlUpdate')
    await moveLawsToMongo(pool);
    console.log('moveLawsToMongo');
    await moveArticlesToMongo(pool) // has to replace one by one ???? delete small table 
    console.log('moveArticlesToMongo')
    // await updateArticleVector(pool);
    // console.log('updateArticleVector');


    console.log('update article html');
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

