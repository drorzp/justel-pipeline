import { Pool, PoolConfig } from 'pg';
import * as dotenv from 'dotenv';



// SELECT 
//     t1.document_number,
//     t1.article_number,
//     t1.main_text_hash as table1_hash,
//     t2.main_text_hash as table2_hash
// FROM article_contents_saver t1
// JOIN article_contents_saver_v2 t2  -- or whatever your second table is named
//     ON t1.document_number = t2.document_number 
//     AND t1.article_number = t2.article_number
// WHERE t1.main_text_hash != t2.main_text_hash;



dotenv.config();

// Write-capable pool config aligned with src/import-to-pg/import.ts
const dbConfig: PoolConfig = {
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT || '5433'),
  database: process.env.DB_NAME || 'lawyers',
  user: process.env.DB_USER || 'postgres',
  password: process.env.DB_PASSWORD || 'strongpassword',
};

const pool = new Pool(dbConfig);

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
  'external_links',
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

  const sql = `TRUNCATE TABLE ${qualified.join(', ')} ${parts.join(' ')};`;

  const client = await pool.connect();
  try {
    await client.query('BEGIN');
    await client.query(sql);
    await client.query('COMMIT');
  } catch (err) {
    await client.query('ROLLBACK');
    throw err;
  } finally {
    client.release();
  }
}

export async function truncateImportTables(options: TruncateOptions = {}): Promise<void> {
  // Order matters for TRUNCATE without CASCADE; with CASCADE it's safe.
  // We still pass all in one statement for efficiency.
  await truncateTables(DEFAULT_IMPORT_TABLES, { cascade: true, restartIdentity: true, ...options });
}

// Optional CLI entrypoint: ts-node src/import-to-pg/truncate.ts documents,articles
if (require.main === module) {
  (async () => {
    const args = process.argv.slice(2);
    try {
      if (args.length > 0) {
        await truncateTables(args);
        console.log(`Truncated: ${args.join(', ')}`);
      } else {
        await truncateImportTables();
        console.log('Truncated default import tables');
      }
    } catch (err) {
      console.error('Failed to truncate tables:', err);
      process.exit(1);
    } finally {
      await pool.end();
    }
  })();
}
