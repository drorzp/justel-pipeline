import { Pool, PoolClient } from 'pg';
import * as dotenv from 'dotenv';

// Load env
dotenv.config();



/**
 * Insert missing rows into public.document_title for all documents
 * that don't yet have a corresponding entry. Sets new_title to empty string.
 */
export async function sync_document_title(pool:Pool): Promise<void> {
  const client: PoolClient = await pool.connect();
  try {
    await client.query('BEGIN');

    const sql = `
      INSERT INTO public.document_title (document_number, old_title, new_title)
      SELECT 
          d.document_number,
          d.title AS old_title,
          ''
      FROM public.documents d
      LEFT JOIN public.document_title dt 
          ON d.document_number = dt.document_number
      WHERE dt.document_number IS NULL
    `;

    const result = await client.query(sql);
    await client.query('COMMIT');
    console.log(`[SUCCESS] Inserted ${result.rowCount ?? 0} missing document_title rows.`);
  } catch (err) {
    await client.query('ROLLBACK');
    console.error('[ERROR] Failed to sync document_title', err);
    throw err;
  } finally {
    client.release();
  }
}

/**
 * Update documents.title to dt.new_title only when the current title equals dt.old_title
 * and new_title is present and non-empty.
 */
export async function sync_not_changed(pool:Pool): Promise<void> {
  const client: PoolClient = await pool.connect();
  try {
    await client.query('BEGIN');

    const sql = `
      UPDATE public.documents d 
      SET title = dt.new_title 
      FROM public.document_title dt 
      WHERE d.document_number = dt.document_number 
        AND d.title = dt.old_title 
        AND dt.new_title IS NOT NULL 
        and trim(dt.new_title) !=trim(d.title)
        AND dt.new_title != '';
    `;

    const result = await client.query(sql);
    await client.query('COMMIT');
    console.log(`[SUCCESS] Updated ${result.rowCount ?? 0} document titles where unchanged.`);
  } catch (err) {
    await client.query('ROLLBACK');
    console.error('[ERROR] Failed to apply not-changed title updates', err);
    throw err;
  } finally {
    client.release();
  }
}


