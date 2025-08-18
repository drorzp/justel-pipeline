import { Pool, PoolConfig } from 'pg';
import * as dotenv from 'dotenv';

dotenv.config();

function isSafeIdentifier(id: string): boolean {
  return /^[a-zA-Z_][a-zA-Z0-9_]*$/.test(id);
}

function qualifyProc(schema: string | undefined, proc: string): string {
  const s = schema || 'public';
  if (!isSafeIdentifier(s) || !isSafeIdentifier(proc)) {
    throw new Error(`Unsafe identifier for procedure: ${s}.${proc}`);
  }
  return `${s}.${proc}`;
}

// Calls stored procedure: COPY CONTENT ARTICLE
// Default schema is public; override if needed.
export async function callCopyContentArticle(dbConfig: PoolConfig, schema: string = 'public'): Promise<void> {
  const pool = new Pool(dbConfig);
  const qualified = qualifyProc(schema, 'reset_and_insert_from_article_content');
  const client = await pool.connect();
  try {
    await client.query('BEGIN');
    await client.query(`CALL ${qualified}()`);
    await client.query('COMMIT');
  } catch (err) {
    await client.query('ROLLBACK');
    throw err;
  } finally {
    client.release();
  }
}
