import * as fs from 'fs/promises';
import * as path from 'path';
import { S3Client, ListObjectsV2Command, GetObjectCommand } from '@aws-sdk/client-s3';
import { Readable } from 'stream';
import * as yauzl from 'yauzl';
import { rimraf } from 'rimraf';
import { DocumentProcessor, ProcessingSummary } from './import';
import * as dotenv from 'dotenv';
import logger from '../utils/logger';

// Load environment variables
dotenv.config();

interface S3Config {
  region: string;
  bucket: string;
  prefix?: string;
  accessKeyId?: string;
  secretAccessKey?: string;
}

interface ProcessingState {
  lastProcessedFile: string | null;
  totalFilesProcessed: number;
  totalDocumentsProcessed: number;
  totalDocumentsSuccessful: number;
  totalDocumentsFailed: number;
  startTime: string;
  lastUpdateTime: string;
  errors: Array<{
    zipFile: string;
    error: string;
    timestamp: string;
  }>;
  failedDocuments: Array<{
    zipFile: string;
    documentPath: string;
    error: string;
    timestamp: string;
  }>;
  processedZipFiles: Array<{
    fileName: string;
    processedAt: string;
    documentsProcessed: number;
    documentsSuccessful: number;
    documentsFailed: number;
    successRate: string;
    processingTimeMs: number;
    errors: Array<{
      documentPath: string;
      error: string;
      timestamp: string;
    }>;
  }>;
}

interface ZipFileInfo {
  key: string;
  size: number;
  lastModified: Date;
}

class S3BatchProcessor {
  private s3Client: S3Client;
  private config: S3Config;
  private stateFilePath: string;
  private documentsDir: string;
  private zippedDir: string;
  private errorsDir: string;
  private state: ProcessingState;

  constructor(config: S3Config) {
    this.config = config;
    this.s3Client = new S3Client({
      region: config.region,
      credentials: config.accessKeyId && config.secretAccessKey ? {
        accessKeyId: config.accessKeyId,
        secretAccessKey: config.secretAccessKey
      } : undefined
    });
    
    this.stateFilePath = path.join(process.cwd(), 'processing-state.json');
    this.documentsDir = path.join(process.cwd(), 'documents');
    this.zippedDir = path.join(process.cwd(), 'zipped');
    this.errorsDir = path.join(process.cwd(), 'errors');
    
    this.state = {
      lastProcessedFile: null,
      totalFilesProcessed: 0,
      totalDocumentsProcessed: 0,
      totalDocumentsSuccessful: 0,
      totalDocumentsFailed: 0,
      startTime: new Date().toISOString(),
      lastUpdateTime: new Date().toISOString(),
      errors: [],
      failedDocuments: [],
      processedZipFiles: []
    };
  }

  private async loadState(): Promise<void> {
    try {
      const stateData = await fs.readFile(this.stateFilePath, 'utf-8');
      this.state = JSON.parse(stateData);
      
      // Ensure backward compatibility - initialize new fields if they don't exist
      if (!this.state.failedDocuments) {
        this.state.failedDocuments = [];
      }
      if (!this.state.processedZipFiles) {
        this.state.processedZipFiles = [];
      }
      
      logger.info(`📂 Loaded existing state: ${this.state.totalFilesProcessed} files processed`);
    } catch (error) {
      logger.info('📝 No existing state found, starting fresh');
      this.state = {
        lastProcessedFile: null,
        totalFilesProcessed: 0,
        totalDocumentsProcessed: 0,
        totalDocumentsSuccessful: 0,
        totalDocumentsFailed: 0,
        startTime: new Date().toISOString(),
        lastUpdateTime: new Date().toISOString(),
        errors: [],
        failedDocuments: [],
        processedZipFiles: []
      };
    }
  }

  private async saveState(): Promise<void> {
    this.state.lastUpdateTime = new Date().toISOString();
    await fs.writeFile(this.stateFilePath, JSON.stringify(this.state, null, 2));
  }

  private async ensureDirectories(): Promise<void> {
    await fs.mkdir(this.documentsDir, { recursive: true });
    await fs.mkdir(this.zippedDir, { recursive: true });
    await fs.mkdir(this.errorsDir, { recursive: true });
  }

  private async listS3ZipFiles(): Promise<ZipFileInfo[]> {
    const command = new ListObjectsV2Command({
      Bucket: this.config.bucket,
      Prefix: this.config.prefix || '',
      MaxKeys: 1000
    });

    const response = await this.s3Client.send(command);
    const zipFiles: ZipFileInfo[] = [];

    if (response.Contents) {
      for (const object of response.Contents) {
        if (object.Key && object.Key.toLowerCase().endsWith('.zip')) {
          zipFiles.push({
            key: object.Key,
            size: object.Size || 0,
            lastModified: object.LastModified || new Date()
          });
        }
      }
    }

    // Sort by key to ensure consistent processing order
    zipFiles.sort((a, b) => a.key.localeCompare(b.key));
    
    logger.info(`📦 Found ${zipFiles.length} zip files in S3`);
    return zipFiles;
  }

  private async downloadZipFile(zipFileInfo: ZipFileInfo): Promise<string> {
    const fileName = path.basename(zipFileInfo.key);
    const localPath = path.join(this.zippedDir, fileName);

    logger.info(`⬇️  Downloading ${zipFileInfo.key} (${(zipFileInfo.size / 1024 / 1024).toFixed(2)} MB)`);

    const command = new GetObjectCommand({
      Bucket: this.config.bucket,
      Key: zipFileInfo.key
    });

    const response = await this.s3Client.send(command);
    
    if (!response.Body) {
      throw new Error(`No body in S3 response for ${zipFileInfo.key}`);
    }

    const stream = response.Body as Readable;
    const writeStream = await fs.open(localPath, 'w');
    
    try {
      for await (const chunk of stream) {
        await writeStream.write(chunk);
      }
    } finally {
      await writeStream.close();
    }

    logger.info(`✅ Downloaded ${fileName}`);
    return localPath;
  }

  private async extractZipFile(zipPath: string): Promise<void> {
    return new Promise((resolve, reject) => {
      yauzl.open(zipPath, { lazyEntries: true }, (err: Error | null, zipfile?: yauzl.ZipFile) => {
        if (err) {
          reject(err);
          return;
        }

        if (!zipfile) {
          reject(new Error('Failed to open zip file'));
          return;
        }

        let extractedCount = 0;
        let totalEntries = 0;

        zipfile.readEntry();

        zipfile.on('entry', async (entry: yauzl.Entry) => {
          totalEntries++;
          
          if (/\/$/.test(entry.fileName)) {
            // Directory entry
            zipfile.readEntry();
            return;
          }

          // File entry
          const outputPath = path.join(this.documentsDir, entry.fileName);
          
          // Ensure directory exists
          await fs.mkdir(path.dirname(outputPath), { recursive: true });

          zipfile.openReadStream(entry, (err: Error | null, readStream?: NodeJS.ReadableStream) => {
            if (err) {
              reject(err);
              return;
            }

            if (!readStream) {
              reject(new Error('Failed to create read stream'));
              return;
            }

            const writeStream = require('fs').createWriteStream(outputPath);
            
            readStream.on('end', () => {
              extractedCount++;
              zipfile.readEntry();
            });

            readStream.on('error', reject);
            writeStream.on('error', reject);
            
            readStream.pipe(writeStream);
          });
        });

        zipfile.on('end', () => {
          logger.info(`📂 Extracted ${extractedCount} files from zip`);
          resolve();
        });

        zipfile.on('error', reject);
      });
    });
  }

  private async moveFailedDocuments(zipFileName: string, failures: Array<{filename: string, reason: string}>): Promise<void> {
    if (!failures || failures.length === 0) {
      return;
    }

    logger.info(`📁 Moving ${failures.length} failed documents to errors directory...`);
    
    // Create errors directory structure: errors/zipFileName/
    const zipBaseName = path.basename(zipFileName, '.zip');
    const errorSubDir = path.join(this.errorsDir, zipBaseName);
    
    try {
      await fs.mkdir(errorSubDir, { recursive: true });
      
      for (const failure of failures) {
        const sourcePath = path.join(this.documentsDir, failure.filename);
        const targetPath = path.join(errorSubDir, failure.filename);
        
        try {
          // Check if source file exists before moving
          await fs.access(sourcePath);
          await fs.rename(sourcePath, targetPath);
          logger.info(`📄 Moved failed document: ${failure.filename} → errors/${zipBaseName}/`);
        } catch (moveError) {
          console.warn(`⚠️  Could not move ${failure.filename}:`, moveError);
        }
      }
      
      // Create a summary file with error details
      const errorSummary = {
        zipFile: zipFileName,
        processedAt: new Date().toISOString(),
        failedDocuments: failures.map(f => ({
          filename: f.filename,
          error: f.reason
        }))
      };
      
      const summaryPath = path.join(errorSubDir, '_error_summary.json');
      await fs.writeFile(summaryPath, JSON.stringify(errorSummary, null, 2));
      logger.info(`📋 Created error summary: errors/${zipBaseName}/_error_summary.json`);
      
    } catch (error) {
      console.error('❌ Error moving failed documents:', error);
    }
  }

  private async cleanupDirectories(): Promise<void> {
    logger.info('🧹 Cleaning up directories...');
    
    try {
      await rimraf(this.documentsDir);
      await rimraf(this.zippedDir);
      await this.ensureDirectories();
      logger.info('✅ Directories cleaned');
    } catch (error) {
      console.error('❌ Error cleaning directories:', error);
      throw error;
    }
  }

  private async processDocuments(): Promise<ProcessingSummary> {
    logger.info('📄 Processing documents...');
    
    const processor = new DocumentProcessor();
    const summary = await processor.processDirectory(this.documentsDir);
    
    logger.info(`📊 Processing complete: ${summary.successful}/${summary.total} successful`);
    
    return summary;
  }

  private shouldProcessFile(zipFileInfo: ZipFileInfo): boolean {
    if (!this.state.lastProcessedFile) {
      return true; // No previous processing, start from beginning
    }
    
    // Only process files that come after the last processed file (alphabetically)
    return zipFileInfo.key > this.state.lastProcessedFile;
  }

  private async processZipFile(zipFileInfo: ZipFileInfo): Promise<void> {
    logger.info(`\n🔄 Processing ${zipFileInfo.key}...`);
    
    try {
      // Download zip file
      const localZipPath = await this.downloadZipFile(zipFileInfo);
      
      // Extract zip file
      await this.extractZipFile(localZipPath);
      
      // Process documents
      const startTime = Date.now();
      const summary = await this.processDocuments();
      const endTime = Date.now();
      
      // Move failed documents to errors directory before cleanup
      if (summary.failures && summary.failures.length > 0) {
        await this.moveFailedDocuments(zipFileInfo.key, summary.failures);
        
        // Record individual document failures in state
        for (const failure of summary.failures) {
          this.state.failedDocuments.push({
            zipFile: zipFileInfo.key,
            documentPath: failure.filename,
            error: failure.reason,
            timestamp: new Date().toISOString()
          });
        }
      }
      
      // Update state
      this.state.lastProcessedFile = zipFileInfo.key;
      this.state.totalFilesProcessed++;
      this.state.totalDocumentsProcessed += summary.total;
      this.state.totalDocumentsSuccessful += summary.successful;
      this.state.totalDocumentsFailed += summary.failed;
      
      // Record zip file processing result
      if (!this.state.processedZipFiles) {
        this.state.processedZipFiles = [];
      }
      
      this.state.processedZipFiles.push({
        fileName: zipFileInfo.key,
        processedAt: new Date().toISOString(),
        documentsProcessed: summary.total,
        documentsSuccessful: summary.successful,
        documentsFailed: summary.failed,
        successRate: summary.total > 0 ? `${(summary.successful / summary.total * 100).toFixed(2)}%` : '0%',
        processingTimeMs: endTime - startTime,
        errors: summary.failures ? summary.failures.map(f => ({
          documentPath: f.filename,
          error: f.reason,
          timestamp: new Date().toISOString()
        })) : []
      });
      
      // Save state after each successful zip file
      await this.saveState();
      
      logger.info(`✅ Successfully processed ${zipFileInfo.key}`);
      logger.info(`📈 Progress: ${this.state.totalFilesProcessed} zip files, ${this.state.totalDocumentsSuccessful}/${this.state.totalDocumentsProcessed} documents successful`);
      
    } catch (error: any) {
      console.error(`❌ Error processing ${zipFileInfo.key}:`, error.message);
      
      // Record error but continue with next file
      this.state.errors.push({
        zipFile: zipFileInfo.key,
        error: error.message,
        timestamp: new Date().toISOString()
      });
      
      await this.saveState();
      throw error; // Re-throw to be handled by caller
    } finally {
      // Always cleanup after processing each zip file
      await this.cleanupDirectories();
    }
  }

  async processAllZipFiles(): Promise<void> {
    logger.info('🚀 Starting S3 batch processing...');
    
    try {
      // Load previous state
      await this.loadState();
      
      // Ensure directories exist
      await this.ensureDirectories();
      
      // Get list of zip files from S3
      const zipFiles = await this.listS3ZipFiles();
      
      if (zipFiles.length === 0) {
        logger.info('📭 No zip files found in S3');
        return;
      }
      
      // Filter files to process (skip already processed ones)
      const filesToProcess = zipFiles.filter(file => this.shouldProcessFile(file));
      
      if (filesToProcess.length === 0) {
        logger.info('✅ All zip files have already been processed');
        return;
      }
      
      logger.info(`📋 ${filesToProcess.length} zip files to process (${zipFiles.length - filesToProcess.length} already processed)`);
      
      // Process each zip file
      for (const zipFile of filesToProcess) {
        try {
          await this.processZipFile(zipFile);
        } catch (error) {
          console.error(`⚠️  Skipping ${zipFile.key} due to error, continuing with next file...`);
          // Continue with next file even if current one fails
        }
      }
      
      // Final summary
      logger.info('\n🎉 Batch processing complete!');
      logger.info(`📊 Final Summary:`);
      logger.info(`   - Zip files processed: ${this.state.totalFilesProcessed}`);
      logger.info(`   - Documents processed: ${this.state.totalDocumentsProcessed}`);
      logger.info(`   - Documents successful: ${this.state.totalDocumentsSuccessful}`);
      logger.info(`   - Documents failed: ${this.state.totalDocumentsFailed}`);
      logger.info(`   - Errors encountered: ${this.state.errors.length}`);
      
      if (this.state.errors.length > 0) {
        logger.info('\n❌ Errors:');
        this.state.errors.forEach(error => {
          logger.info(`   - ${error.zipFile}: ${error.error}`);
        });
      }
      
    } catch (error) {
      console.error('💥 Fatal error in batch processing:', error);
      throw error;
    }
  }

  async resetState(): Promise<void> {
    logger.info('🔄 Resetting processing state...');
    
    this.state = {
      lastProcessedFile: null,
      totalFilesProcessed: 0,
      totalDocumentsProcessed: 0,
      totalDocumentsSuccessful: 0,
      totalDocumentsFailed: 0,
      startTime: new Date().toISOString(),
      lastUpdateTime: new Date().toISOString(),
      errors: [],
      failedDocuments: [],
      processedZipFiles: []
    };
    
    await this.saveState();
    logger.info('✅ State reset complete');
  }

  async showStatus(): Promise<void> {
    await this.loadState();
    
    logger.info('\n📊 Current Processing Status:');
    logger.info(`   Last processed file: ${this.state.lastProcessedFile || 'none'}`);
    logger.info(`   Zip files processed: ${this.state.totalFilesProcessed}`);
    logger.info(`   Documents processed: ${this.state.totalDocumentsProcessed}`);
    logger.info(`   Documents successful: ${this.state.totalDocumentsSuccessful}`);
    logger.info(`   Documents failed: ${this.state.totalDocumentsFailed}`);
    logger.info(`   Start time: ${this.state.startTime}`);
    logger.info(`   Last update: ${this.state.lastUpdateTime}`);
    logger.info(`   Errors: ${this.state.errors.length}`);
    
    if (this.state.errors.length > 0) {
      logger.info('\n❌ Recent Errors:');
      this.state.errors.slice(-5).forEach(error => {
        logger.info(`   - ${error.zipFile}: ${error.error}`);
      });
    }
  }
}

async function main(): Promise<void> {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    logger.info('Usage: ts-node s3-batch-processor.ts <command>');
    logger.info('');
    logger.info('Commands:');
    logger.info('  process                    - Process all zip files from S3 bucket');
    logger.info('  status                     - Show current processing status');
    logger.info('  reset                      - Reset processing state');
    logger.info('');
    logger.info('Configuration (via .env file or environment variables):');
    logger.info('  AWS_REGION                 - AWS region (default: us-east-1)');
    logger.info('  AWS_ACCESS_KEY_ID          - AWS access key (optional if using IAM roles)');
    logger.info('  AWS_SECRET_ACCESS_KEY      - AWS secret key (optional if using IAM roles)');
    logger.info('  S3_BUCKET                  - S3 bucket name (required)');
    logger.info('  S3_PREFIX                  - S3 prefix/folder (optional)');
    logger.info('');
    logger.info('Examples:');
    logger.info('  ts-node s3-batch-processor.ts process');
    logger.info('  ts-node s3-batch-processor.ts status');
    logger.info('  ts-node s3-batch-processor.ts reset');
    process.exit(1);
  }

  const command = args[0];
  
  // Read configuration from environment variables
  const config: S3Config = {
    region: process.env.AWS_REGION || 'us-east-1',
    bucket: process.env.S3_BUCKET || '',
    prefix: process.env.S3_PREFIX || '',
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY
  };

  // Validate required configuration
  if (!config.bucket) {
    console.error('❌ S3_BUCKET environment variable is required');
    console.error('💡 Please set S3_BUCKET in your .env file or environment variables');
    process.exit(1);
  }

  logger.info(`🔧 Configuration:`);
  logger.info(`   Region: ${config.region}`);
  logger.info(`   Bucket: ${config.bucket}`);
  logger.info(`   Prefix: ${config.prefix || '(none)'}`);
  logger.info(`   Using AWS credentials: ${config.accessKeyId ? 'Yes (from env)' : 'No (using IAM/default)'}`);
  logger.info('');

  const processor = new S3BatchProcessor(config);

  try {
    switch (command) {
      case 'process':
        await processor.processAllZipFiles();
        break;
        
      case 'status':
        await processor.showStatus();
        break;
        
      case 'reset':
        await processor.resetState();
        break;
        
      default:
        console.error(`❌ Unknown command: ${command}`);
        process.exit(1);
    }
  } catch (error) {
    console.error('💥 Process failed:', error);
    process.exit(1);
  }
}

// Run if executed directly
if (require.main === module) {
  main().catch(error => {
    console.error('💥 Unhandled error:', error);
    process.exit(1);
  });
}

// Programmatic API for calling from other modules (e.g., index.ts)
export function buildS3ConfigFromEnv(overrides: Partial<S3Config> = {}): S3Config {
  return {
    region: process.env.AWS_REGION || 'us-east-2',
    bucket: overrides.bucket ?? (process.env.S3_BUCKET || ''),
    prefix: overrides.prefix ?? (process.env.S3_PREFIX || ''),
    accessKeyId: overrides.accessKeyId ?? process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: overrides.secretAccessKey ?? process.env.AWS_SECRET_ACCESS_KEY,
  };
}

export async function runS3Batch()
: Promise<void> {
  const config = buildS3ConfigFromEnv();

  const processor = new S3BatchProcessor(config);
  await processor.processAllZipFiles();

}

