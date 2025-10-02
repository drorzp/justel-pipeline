import { Pool } from 'pg';

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
export async function saveContentArticle(pool: Pool, schema: string = 'public'): Promise<void> {
  const qualified = qualifyProc(schema, 'reset_and_insert_from_article_content');
  const client = await pool.connect();
  try {
    console.log(`COPY CONTENT ARTICLE ${qualified}`);
    await client.query(`CALL ${qualified}()`);
  } catch (err) {
    throw err;
  } finally {
    client.release();
  }
}
