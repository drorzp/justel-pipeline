import { Pool, PoolClient } from 'pg';
import * as dotenv from 'dotenv';
import { transformArticleHtml, TransformationInput } from '../html-transformer/transform-html';

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
    let failed = 0;
    
    for (const row of rows) { 
      const document_number: string = row.document_number;
      const article_number: string = row.article_number;

      // Transform the HTML using the new function
      const transformationInput: TransformationInput = {
        document_number,
        article_number,
        main_text: row.main_text_v1,
        main_text_raw: row.main_text_raw_v1
      };

      const result = await transformArticleHtml(transformationInput);
      
      if (result.success && result.transformedHtml) {
        // Update with the successfully transformed HTML
        const transformedHtml = result.transformedHtml;
        
        await client.query(updateSql, [
          document_number,
          article_number,
          transformedHtml
        ]);
        updated++;
        console.log(`[SUCCESS] Transformed article ${document_number}:${article_number}`);
      } else {
        // Handle transformation failure
        failed++;
        const errorMsg = result.error || (result.validationErrors ? result.validationErrors.join(', ') : 'Unknown error');
        console.error(`[ERROR] Failed to transform article ${document_number}:${article_number}: ${errorMsg}`);
        
        // Skip failed transformations - don't update the database
        continue;
      }
    }

    await client.query('COMMIT');
    console.log(`[SUCCESS] Updated article_contents rows: ${updated}`);
    if (failed > 0) {
      console.log(`[WARNING] Failed to transform ${failed} articles`);
    }
  } catch (err) {
    await client.query('ROLLBACK');
    console.error('[ERROR] Failed to update article_contents from saver_v2 diffs', err);
    throw err;
  } finally {
    client.release();
  }
}