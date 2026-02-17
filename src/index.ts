import 'dotenv/config';
import { Pool, PoolConfig } from 'pg';
import { runLocalFolderBatch } from './import-to-pg/process';
import {  moveArticlesToMongo } from './transfer-to-mongo/articles';
import { moveLawsToMongo } from './transfer-to-mongo/laws';
import { truncateImportTables } from './import-to-pg/truncate';
import { saveContentArticle } from './import-to-pg/copyArticleContent';
import { updateArticleContentsFromSaver } from './import-to-pg/updateFromSaver';
import { updateArticleContentsFromSaverV2Diff } from './import-to-pg/updateFromSaverV2';
import { updateArticleVector } from './add-to-vector/loop_over_articles';
import { sync_document_title, titles_not_changed } from './import-to-pg/sync_document_title';
import { processAllDocumentTitles, LLMConfig } from './import-to-pg/llm_title';
import { runPythonDataPipeline } from './utils/pythonRunner';
import { ArticleChangeInfo, filterJSON, updateOlderFolder } from './utils/filterJSON';
import { updateGet } from './import-to-pg/upgete_gen_on_articles';
import './logger';
import { rimraf } from 'rimraf';
import * as fs from 'fs/promises';
import * as path from 'path';

export const llmConfig: LLMConfig = {
    azureEndpoint: process.env.AZURE_OPENAI_ENDPOINT || '',
    azureApiKey: process.env.AZURE_OPENAI_API_KEY || '',
    azureApiVersion: process.env.AZURE_API_VERSION || '2024-10-01-preview',
    model: 'gpt-4o',
    maxRetries: 2,
    retryDelay: 200,
    requestDelay: 0,
    concurrentRequests: 300,
    batchSize: 2000,
};

// Pool configuration for DocumentTitleProcessor
const dbConfig: PoolConfig = {
  host: process.env.POSTGRES_HOST || 'localhost',
  port: Number(process.env.POSTGRES_PORT) || 5433,
  user: process.env.POSTGRES_USER,
  password: process.env.POSTGRES_PASSWORD,
  database: process.env.POSTGRES_DB,
  ssl: false,
   max: Number(process.env.POSTGRES_POOL_MAX) || 20
};

async function clearValidFolders(): Promise<void> {
  const folders = [
    'data/step1/current/valid',
    'data/step1/current/invalid',
    'data/step1/current/ready/valid',
    'data/step1/current/ready/invalid',
    'data/step1/new/valid',
  ];

  await Promise.all(folders.map(async (folderPath) => {
    const fullPath = path.join(process.cwd(), folderPath);
    await rimraf(fullPath);
    await fs.mkdir(fullPath, { recursive: true });
  }));

  console.log('Cleared folders: current/valid, current/invalid, current/ready/valid, current/ready/invalid, new/valid');
}

async function main() {

const pool = new Pool(dbConfig);

  try {
    console.log('Clearing valid folders before running pipeline...');
    await clearValidFolders();
    console.log('Collect data and store as json in data/step1');
    await runPythonDataPipeline();
    console.log('Complete Collect data');
    console.log('Filtering JSON files with changes...');
    const result: ArticleChangeInfo[] = await filterJSON();
    console.log('filterJSON completed');
    console.log('runLocalFolderBatch started');
    await runLocalFolderBatch(pool, 'new/valid', true, [], llmConfig);
    await runLocalFolderBatch(pool, 'new/invalid', true, [], llmConfig);
    await runLocalFolderBatch(pool, 'current/ready/valid', false, result, llmConfig);
    await runLocalFolderBatch(pool, 'current/ready/invalid', false, [], llmConfig);
    await updateGet(pool);
    await updateOlderFolder();
    // await moveLawsToMongo(pool, 20);
    // await moveArticlesToMongo(pool)

   console.log('Pipeline completed successfully');

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


