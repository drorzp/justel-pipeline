import { config } from 'dotenv';
import { Dirent, promises as fs } from 'fs';
import path from 'path';
import { Pool, PoolClient } from 'pg';

config();

interface Article {
  id: number;
  documentNumber: string;
  articleNumber: string;
  transformedHtml: string;
  status: string;
  processedAt: Date;
}

async function listSubdirectories(baseDir: string): Promise<string[]> {
  const entries: Dirent[] = await fs.readdir(baseDir, { withFileTypes: true });
  return entries.filter(e => e.isDirectory()).map(e => path.join(baseDir, e.name));
}

async function listJsonFiles(dir: string): Promise<string[]> {
  const entries: Dirent[] = await fs.readdir(dir, { withFileTypes: true });
  return entries
    .filter(e => e.isFile() && e.name.toLowerCase().endsWith('.json'))
    .map(e => path.join(dir, e.name));
}

async function readJsonFile(filePath: string): Promise<Article> {
  const raw = await fs.readFile(filePath, 'utf-8');
  return JSON.parse(raw);
}

async function appendToEmptyList(documentNumber: string, articleNumber: string): Promise<void> {
  const emptyListPath = 'empty_list.txt';
  const entry = `${documentNumber} - ${articleNumber}\n`;
  
  try {
    // Append to file, creating it if it doesn't exist
    await fs.appendFile(emptyListPath, entry, 'utf-8');
  } catch (err) {
    console.error('Failed to write to empty_list.txt:', err);
    throw err;
  }
}

export async function updateHtml(pool: Pool, folderPath: string): Promise<void> {
  // Validate folder
  let updatedCount = 0;
  let skippedCount = 0;
  const client: PoolClient = await pool.connect();
  try {
    const subdirs = await listSubdirectories(folderPath);
    
    for (const dir of subdirs) {
      const files = await listJsonFiles(dir);
      
      for (const f of files) {
        const article = await readJsonFile(f);
        const document_number = article.documentNumber;
        const article_number = article.articleNumber;
        const original_html = article.transformedHtml;
        
        // Check if transformedHtml is empty or null
        if (!original_html || original_html.trim() === '') {
          console.log(`Skipping empty article: ${document_number} - ${article_number}`);
          await appendToEmptyList(document_number, article_number);
          skippedCount++;
          continue; // Skip this article and move to the next one
        }
        
        // Proceed with update if transformedHtml has content
        const res = await client.query(
          `UPDATE articles_content
           SET main_text = $1
           WHERE document_number = $2 and article_number = $3`,
          [original_html, document_number, article_number]
        );
        
        if (res.rowCount && res.rowCount > 0) {
          updatedCount++;
        }
      }
    }
    
    console.log(`Update completed: ${updatedCount} articles updated, ${skippedCount} articles skipped (empty content)`);
    
  } catch (err) {
    console.error('Update failed, transaction rolled back:', err);
    throw err;
  } finally {
    client.release();
  }
}