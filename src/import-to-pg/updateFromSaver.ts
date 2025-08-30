import { Pool, PoolClient } from 'pg';


export async function updateArticleContentsFromSaver(pool: Pool): Promise<void> {
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
