import { Pool, PoolClient } from 'pg';
import * as dotenv from 'dotenv';

dotenv.config();

// Align DB config with other modules

/**
 * For all (document_number, article_number) where the hash differs between
 * article_contents_saver and article_contents_saver_v2, update article_contents
 * with the v2 main_text fields.
 */
export async function updateArticleContentsFromSaverV2Diff(pool:Pool): Promise<void> {
  const client: PoolClient = await pool.connect();
  try {
    await client.query('BEGIN');

    const selectSql = `
SELECT
    t1.document_number,
    t1.article_number,
    t1.main_text_raw AS main_text_raw_v1,"Policies"
    t1.main_text AS main_text_v1,
    t1.main_text_hash AS main_text_hash_v1,
    t2.main_text_raw AS main_text_raw_v2,
    t2.main_text AS main_text_v2,
    t2.main_text_hash AS main_text_hash_v2
FROM article_contents t1
LEFT JOIN article_contents_saver t2
    ON t1.document_number = t2.document_number
    AND t1.article_number = t2.article_number
WHERE t2.document_number IS NULL  -- t2 doesn't exist
    OR t1.main_text_hash <> t2.main_text_hash  -- or hashes don't match
    `;

    const { rows } = await client.query(selectSql);
    console.log(`[INFO] Rows with differing hashes: ${rows.length}`);
    const updateSql = `
      UPDATE article_contents
      SET  main_text = $3
      WHERE document_number = $1 AND article_number = $2
    `;

    let updated = 0;
    for (const row of rows) {
      const document_number: string = row.document_number;
      const article_number: string = row.article_number;

      // shahar has to help me run the llm from here then i will update the html
      const translateToLLM:string="we need to llm it"
      

      await client.query(updateSql, [
        document_number,
        article_number,
        translateToLLM
      ]);
      updated++;
    }

    await client.query('COMMIT');
    console.log(`[SUCCESS] Updated article_contents rows: ${updated}`);
  } catch (err) {
    await client.query('ROLLBACK');
    console.error('[ERROR] Failed to update article_contents from saver_v2 diffs', err);
    throw err;
  } finally {
    client.release();
  }
}