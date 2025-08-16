import 'dotenv/config';
import { pool, connectPostgreSQL } from './postgres/pgConnect';
import { createS3, deleteS3 } from './s3';
import { runS3Batch } from './import-to-pg/process';
import {  moveArticlesToMongo } from './transfer-to-mongo/articles';
import { moveLawsToMongo } from './transfer-to-mongo/laws';
import { applyTitlesUpdate, main as runLlmTitle } from './import-to-pg/llm_title';

async function main() {

  await connectPostgreSQL();
  try {
    const { rows } = await pool.query('SELECT NOW() as now');
    console.log('DB connected. Time:', rows[0].now);

    // TODO: Place your batch task logic here
    // Example: await runMyBatch(pool)

    // S3 flow: create a folder and then delete it
    const folder = await createS3();
    console.log('Created S3 folder:', folder);
    // shahars code goes here 
    await runS3Batch('process');
    // change titles
    await runLlmTitle();
    await applyTitlesUpdate
    // add Vector DB
    await moveLawsToMongo();
    await moveArticlesToMongo();
    await deleteS3(folder);
    console.log('Deleted S3 folder:', folder);

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
