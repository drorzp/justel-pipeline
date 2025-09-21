import { Pool, PoolClient } from 'pg';
import * as dotenv from 'dotenv';
import { smartUpsert } from './qdrantCreate.service';

dotenv.config();


/**
 * For all (document_number, article_number) where the hash differs between
 * article_contents_saver and article_contents_saver_v2, update article_contents
 * with the v2 main_text fields.
 */
export async function updateArticleVector(pool: Pool): Promise<void> {
  const client: PoolClient = await pool.connect();
  const MAX_CHARS = 30000; // Roughly ~6000 tokens to stay under 8192 limit
  
  try {
    // const selectSql = `
    //   SELECT
    //     t1.id,
    //     t1.document_number,
    //     t1.article_number,
    //     t1.main_text_raw AS main_text_raw_v1,
    //     t1.main_text AS main_text_v1,
    //     t1.main_text_hash AS main_text_hash_v1,
    //     t2.main_text_raw AS main_text_raw_v2,
    //     t2.main_text AS main_text_v2,
    //     t2.main_text_hash AS main_text_hash_v2
    //   FROM article_contents t1
    //   // LEFT JOIN article_contents_saver t2
    //   //   ON t1.document_number = t2.document_number
    //   //   AND t1.article_number = t2.article_number
    //   // WHERE t2.document_number IS NULL  -- t2 doesn't exist
    //   //   OR t1.main_text_hash <> t2.main_text_hash  -- or hashes don't match
    // `;


    const selectSql = `
  SELECT 
      t1.id,
      t1.document_number,
      t1.article_number,
      t1.main_text_raw AS main_text_raw_v1,
      t1.main_text AS main_text_v1,
      t1.main_text_hash AS main_text_hash_v1,
      t2.effective_date
  FROM article_contents t1
  LEFT JOIN documents t2 ON t1.document_number = t2.document_number`

    const { rows } = await client.query(selectSql);
    console.log(`[INFO] Rows with differing hashes: ${rows.length}`);

    // Will write to qdrant
    let updated = 0;
    for (const row of rows) {
      const document_number: string = row.document_number;
      const effective_date: Date = row.effective_date;
      const article_number: string = row.article_number;
      const main_text_raw_v1: string | null = row.main_text_raw_v1;
      const id: number | null = row.id ?? null;

      if (!id) {
        console.warn(`Skipping ${document_number}-${article_number}: missing id`);
        continue;
      }

      if (!main_text_raw_v1) {
        console.warn(`Skipping ${document_number}-${article_number}: missing main_text_raw_v1`);
        continue;
      }

      // Truncate text to avoid token limit
      const truncatedText = main_text_raw_v1.substring(0, MAX_CHARS);
      
      // Optional: Log when truncation occurs
      if (main_text_raw_v1.length > MAX_CHARS) {
        console.log(`[INFO] Truncated ${document_number}-${article_number}: ${main_text_raw_v1.length} -> ${MAX_CHARS} chars`);
      }

      await smartUpsert(id, truncatedText, document_number, article_number,effective_date);
      updated++;
    }

    console.log(`[SUCCESS] Upserted vectors for rows: ${updated}`);
  } catch (err) {
    console.error('[ERROR] Failed to upsert article vectors', err);
    throw err;
  } finally {
    client.release();
  }
}
