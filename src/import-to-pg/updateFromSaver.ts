import { Pool, PoolClient, PoolConfig } from 'pg';
import * as dotenv from 'dotenv';

dotenv.config();

// Align DB config with other modules
const dbConfig: PoolConfig = {
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT || '5433'),
  database: process.env.DB_NAME || 'lawyers',
  user: process.env.DB_USER || 'postgres',
  password: process.env.DB_PASSWORD || 'strongpassword',
};

const pool = new Pool(dbConfig);

/**
 * Executes a set-based UPDATE to copy main_text from article_contents_saver
 * into article_contents where (document_number, article_number) match and
 * the hashes are equal.
 */
export async function updateArticleContentsFromSaver(): Promise<void> {
  const client: PoolClient = await pool.connect();
  try {
    const updateSql = `
      UPDATE article_contents ac
      SET main_text = acs.main_text
      FROM article_contents_saver acs
      WHERE ac.document_number = acs.document_number
        AND ac.article_number = acs.article_number
        AND ac.main_text_hash = acs.main_text_hash;
    `;

    const result = await client.query(updateSql);
    console.log(`[SUCCESS] Updated rows: ${result.rowCount}`);
  } catch (err) {
    console.error('[ERROR] Failed to update article_contents from saver', err);
    throw err;
  } finally {
    client.release();
  }
}
