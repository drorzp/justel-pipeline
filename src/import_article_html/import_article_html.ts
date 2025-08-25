import { config } from 'dotenv';
import { createWriteStream, Dirent, promises as fs } from 'fs';
import path from 'path';
import { pipeline } from 'stream/promises';
import { Readable } from 'stream';
import AdmZip from 'adm-zip';
import { Pool, PoolClient } from 'pg';
import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';


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

export async function updateHtml(client: Pool, folderPath: string): Promise<void> {
  // Validate folder
  let updatedCount = 0;
  let skippedCount = 0;

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
  }
}

const s3Client = new S3Client({
    region: process.env.AWS_REGION || 'us-east-1',
    credentials: {
      accessKeyId: process.env.AWS_ACCESS_KEY_ID!,
      secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY!,
    },
  });

async function downloadFromS3(
    bucketName: string,
    s3Key: string,
    localPath: string
  ): Promise<void> {
    console.log(`Downloading ${s3Key} from S3 bucket ${bucketName}...`);
    
    try {
      // Get object from S3
      const command = new GetObjectCommand({
        Bucket: bucketName,
        Key: s3Key,
      });
      
      const response = await s3Client.send(command);
      
      if (!response.Body) {
        throw new Error('No body in S3 response');
      }
      
      // Ensure directory exists
      const dir = path.dirname(localPath);
      await fs.mkdir(dir, { recursive: true });
      
      // Convert Body to readable stream and write to file
      const writeStream = createWriteStream(localPath);
      const readableStream = response.Body as Readable;
      
      await pipeline(readableStream, writeStream);
      
      console.log(`Successfully downloaded to ${localPath}`);
    } catch (error) {
      console.error('Error downloading from S3:', error);
      throw error;
    }
  }
  async function cleanupTempFiles(tempZipPath: string): Promise<void> {
    try {
      await fs.unlink(tempZipPath);
      console.log(`Cleaned up temporary file: ${tempZipPath}`);
    } catch (error) {
      console.error('Error cleaning up temp files:', error);
      // Don't throw - cleanup errors shouldn't stop the process
    }
  }

  async function unzipFile(
    zipFilePath: string,
    extractToPath: string
  ): Promise<void> {
    console.log(`Unzipping ${zipFilePath} to ${extractToPath}...`);
    
    try {
      // Ensure extraction directory exists
      await fs.mkdir(extractToPath, { recursive: true });
      
      // Read zip file
      const zip = new AdmZip(zipFilePath);
      
      // Extract all files
      zip.extractAllTo(extractToPath, true); // true = overwrite existing files
      
      console.log(`Successfully unzipped to ${extractToPath}`);
    } catch (error) {
      console.error('Error unzipping file:', error);
      throw error;
    }
  }
  export async function processS3HtmlUpdate(
    pool: Pool,
    bucketName: string,
    s3Key: string,
    cleanupAfter: boolean = true
  ): Promise<void> {
    // Define paths
    const tempDir = path.join(__dirname, 'temp');
    const tempZipPath = path.join(tempDir, 'downloaded.zip');
    const extractPath = path.join(__dirname, process.env.HTML_FOLDER_PATH!);
    
    try {
      // Step 1: Download zip from S3
      await downloadFromS3(bucketName, s3Key, tempZipPath);
      
      // Step 2: Unzip the file
      await unzipFile(tempZipPath, extractPath);
      
      // Step 3: Process the unzipped HTML files
      console.log('Processing HTML files...');
      await updateHtml(pool, extractPath);
      
      // Step 4: Cleanup (optional)
      if (cleanupAfter) {
        await cleanupTempFiles(tempZipPath);
      }
      
      console.log('Process completed successfully!');
    } catch (error) {
      console.error('Process failed:', error);
      throw error;
    }
  }

  export async function downloadAndUnzip(
    pool:Pool,
    bucketName: string,
    s3Key: string
  ): Promise<string> {
    const tempDir = path.join(__dirname, 'temp');
    const tempZipPath = path.join(tempDir, 'downloaded.zip');
    const extractPath = path.join(__dirname, process.env.HTML_FOLDER_PATH!);
    
    // Download from S3
    await downloadFromS3(bucketName, s3Key, tempZipPath);
    
    // Unzip the file
    await unzipFile(tempZipPath, extractPath);
    
    return extractPath;
  }

 