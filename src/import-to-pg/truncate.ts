import { Pool } from 'pg';
import * as dotenv from 'dotenv';

dotenv.config();

// Default tables involved in the import pipeline
export const DEFAULT_IMPORT_TABLES = [
  'article_contents',
  'hierarchy_elements',
  'document_versions',
  'document_modifies',
  'document_modified_by',
  'modified_articles',
  'external_links',
  'extraction_metadata',
  'documents'
];

export type TruncateOptions = {
  schema?: string;           // default: 'public'
  cascade?: boolean;         // default: true
  restartIdentity?: boolean; // default: true
};

function isSafeIdentifier(id: string): boolean {
  // Very conservative: allow only letters, numbers and underscores, optionally with a single dot for schema.table
  return /^[a-zA-Z_][a-zA-Z0-9_]*$/.test(id);
}

function qualify(schema: string | undefined, table: string): string {
  const s = (schema || 'public');
  if (!isSafeIdentifier(s) || !isSafeIdentifier(table)) {
    throw new Error(`Unsafe identifier detected (schema=${schema}, table=${table})`);
  }
  return `${s}.${table}`;
}

export async function truncateTables(
  pool: Pool,
  tables: string[],
  options: TruncateOptions = {}
): Promise<void> {
  if (!tables || tables.length === 0) return;

  const { schema = 'public', cascade = true, restartIdentity = true } = options;

  const qualified = tables.map((t) => qualify(schema, t));
  const parts: string[] = [];
  // Always include RESTART IDENTITY per request
  parts.push('RESTART IDENTITY');
  if (cascade) parts.push('CASCADE');

  const client = await pool.connect();
  try {
    const info = await client.query("select current_database() as db, current_user as usr");
    console.log("[truncate] Target:", info.rows[0]);
    await client.query('BEGIN');
    // Truncate one-by-one to allow per-table success logging
    for (const q of qualified) {
      const sql = `TRUNCATE TABLE ${q} ${parts.join(' ')};`;
      await client.query(sql);
      console.log(`[truncate] Success: ${q}`);
    }
    await client.query('COMMIT');
  } catch (err) {
    await client.query('ROLLBACK');
    throw err;
  } finally {
    client.release();
  }
}

export async function truncateImportTables(pool:Pool, options: TruncateOptions = {}): Promise<void> {
  // Order matters for TRUNCATE without CASCADE; with CASCADE it's safe.
  // We still pass all in one statement for efficiency.
  await truncateTables(pool , DEFAULT_IMPORT_TABLES, { cascade: true, restartIdentity: true, ...options });
}

