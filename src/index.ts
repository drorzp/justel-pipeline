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
import { filterJSON, updateOlderFolder } from './utils/filterJSON';
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

async function clearLocalFolder(folderPath: string): Promise<void> {
  const fullPath = path.join(process.cwd(), folderPath);
  await rimraf(fullPath);
  await fs.mkdir(fullPath, { recursive: true });
  console.log(`Cleared and recreated local folder: ${fullPath}`);
}

async function main() {

const pool = new Pool(dbConfig);

  try {
    console.log('Clear local data/step1 folder before running pipeline');
    await clearLocalFolder('data/step1');
    console.log('Cleared local folder data/step1');
    console.log('Collect data and store as json in data/step1');
    await runPythonDataPipeline();
    console.log('Complete Collect data');
    console.log('Filtering JSON files with changes...');
    await filterJSON();
    console.log('filterJSON completed');
    console.log('truncate article_conten_saver and copy article_content into it started');
//     await saveContentArticle(pool);
//     console.log('truncate article_conten_saver and copy article_content into it completed');
//     console.log('sync_document_title add all documents that does not exist in documents started');
//     await sync_document_title(pool);
//     console.log('sync_document_title completed');
//     console.log('truncate tables started');
//     await truncateImportTables(pool);
//     console.log('truncate tables completed');
//     console.log('runLocalFolderBatch valid started');
//     await runLocalFolderBatch(pool, 'valid');
//     console.log('runLocalFolderBatch valid completed');
//     console.log('runLocalFolderBatch invalid started');
//     await runLocalFolderBatch(pool, 'invalid');
//     console.log('runLocalFolderBatch invalid completed');
//     console.log('copy all non changed titles to law document started');
//   await titles_not_changed(pool);
//     console.log('copy all non changed titles to law document completed');
//     console.log('llm titles on all new/ changed law document started');
//  await processAllDocumentTitles(pool, llmConfig);
//     console.log('llm titles on all new/ changed law document completed');
//     console.log('copy back all html that was not changed started')
//  await updateArticleContentsFromSaver(pool);
//     console.log('copy back all html that was not changed completed')
//     console.log('llmall html that was changed/new started')
//  await updateArticleContentsFromSaverV2Diff(pool) 
//     console.log('llmall html that was changed/new completed')
//     console.log('Move to mongo document collection started');

//     console.log('update gen started');
//    await updateGet(pool);
//     console.log('update gen completed');

//  await moveLawsToMongo(pool, 20);
//     console.log('Move to mongo document collection completed');
//     console.log('moveArticlesToMongo started')
// await moveArticlesToMongo(pool) // has to replace one by one ???? delete small table 
//     console.log('moveArticlesToMongo completed')
//     console.log('updateArticleVector started')
//     await updateArticleVector(pool);
//     console.log('updateArticleVector completed');
//     console.log('process completed');

    console.log('Updating older folder with processed files...');
    await updateOlderFolder();
    console.log('updateOlderFolder completed');
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


