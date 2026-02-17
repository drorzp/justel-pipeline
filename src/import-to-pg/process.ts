import * as fs from 'fs/promises';
import * as path from 'path';
import { DocumentProcessor } from './import';
import { Pool } from 'pg';
import { ArticleChangeInfo } from '../utils/filterJSON';

// Local Folder Processor for reading JSON files directly from data/step1/
interface LocalFolderProcessingState {
  lastProcessedFile: string | null;
  totalFilesProcessed: number;
  totalDocumentsProcessed: number;
  totalDocumentsSuccessful: number;
  totalDocumentsFailed: number;
  startTime: string;
  lastUpdateTime: string;
  processedFiles: string[];
  errors: Array<{
    file: string;
    error: string;
    timestamp: string;
  }>;
}

class LocalFolderProcessor {
  private pool: Pool;
  private sourceDir: string;
  private errorsDir: string;
  private stateFilePath: string;
  private state: LocalFolderProcessingState;
  private prefix: string;

  constructor(pool: Pool, prefix: string) {
    this.pool = pool;
    this.prefix = prefix;
    this.sourceDir = path.join(process.cwd(), 'data', 'step1', prefix);
    this.errorsDir = path.join(process.cwd(), 'data', 'step1', 'errors', prefix);
    this.stateFilePath = path.join(process.cwd(), 'src', 'import-to-pg', `processing-state-${prefix.replace(/\//g, '-')}.json`);
    this.state = this.getInitialState();
  }

  private getInitialState(): LocalFolderProcessingState {
    return {
      lastProcessedFile: null,
      totalFilesProcessed: 0,
      totalDocumentsProcessed: 0,
      totalDocumentsSuccessful: 0,
      totalDocumentsFailed: 0,
      startTime: new Date().toISOString(),
      lastUpdateTime: new Date().toISOString(),
      processedFiles: [],
      errors: []
    };
  }

  private async loadState(): Promise<void> {
    try {
      const stateData = await fs.readFile(this.stateFilePath, 'utf-8');
      this.state = JSON.parse(stateData);

      if (!this.state.processedFiles) {
        this.state.processedFiles = [];
      }

      console.info(`Loaded existing state for ${this.prefix}: ${this.state.totalFilesProcessed} files processed`);
    } catch (error) {
      console.info(`No existing state found for ${this.prefix}, starting fresh`);
      this.state = this.getInitialState();
    }
  }

  private async saveState(): Promise<void> {
    this.state.lastUpdateTime = new Date().toISOString();
    await fs.writeFile(this.stateFilePath, JSON.stringify(this.state, null, 2));
  }

  private async listJsonFiles(): Promise<string[]> {
    try {
      const files = await fs.readdir(this.sourceDir);
      return files.filter(f => f.endsWith('.json')).sort();
    } catch (error) {
      console.warn(`Source directory ${this.sourceDir} does not exist or is not readable`);
      return [];
    }
  }

  private async moveFailedDocument(filename: string, error: string): Promise<void> {
    try {
      await fs.mkdir(this.errorsDir, { recursive: true });

      const sourcePath = path.join(this.sourceDir, filename);
      const targetPath = path.join(this.errorsDir, filename);

      await fs.rename(sourcePath, targetPath);

      // Write error details
      const errorInfoPath = path.join(this.errorsDir, `${filename}.error.json`);
      await fs.writeFile(errorInfoPath, JSON.stringify({
        filename,
        error,
        timestamp: new Date().toISOString()
      }, null, 2));

      console.info(`Moved failed document: ${filename} -> errors/${this.prefix}/`);
    } catch (moveError) {
      console.warn(`Could not move ${filename}:`, moveError);
    }
  }

  async processAllFiles(isNew: boolean, articlesList: ArticleChangeInfo[], skipArticleContents: boolean): Promise<void> {
    console.info(`Starting local folder processing for ${this.prefix}...`);

    try {
      await this.loadState();
      const files = await this.listJsonFiles();

      if (files.length === 0) {
        console.info(`No JSON files found in ${this.sourceDir}`);
        return;
      }

      console.info(`Processing ${files.length} files from ${this.sourceDir}`);

      const processor = new DocumentProcessor();

      try {
        const summary = await processor.processDirectory(this.pool, this.sourceDir, isNew, articlesList, skipArticleContents);

        // Update state
        this.state.totalFilesProcessed = files.length;
        this.state.lastProcessedFile = files[files.length - 1] || null;
        this.state.processedFiles = files;
        this.state.totalDocumentsProcessed = summary.total;
        this.state.totalDocumentsSuccessful = summary.successful;
        this.state.totalDocumentsFailed = summary.failed;

        // Handle failures - move failed documents to errors directory
        if (summary.failures && summary.failures.length > 0) {
          for (const failure of summary.failures) {
            await this.moveFailedDocument(failure.filename, failure.reason);
          }
        }

        await this.saveState();

        console.info(`Processed ${summary.successful}/${summary.total} documents successfully`);

      } catch (error: any) {
        console.error(`Error processing directory ${this.sourceDir}:`, error.message);

        this.state.errors.push({
          file: this.sourceDir,
          error: error.message,
          timestamp: new Date().toISOString()
        });

        await this.saveState();
        throw error;
      }

      this.printSummary();

    } catch (error) {
      console.error(`Fatal error in local folder processing for ${this.prefix}:`, error);
      throw error;
    }
  }

  private printSummary(): void {
    console.info(`\nLocal folder processing complete for ${this.prefix}`);
    console.info(`Final Summary:`);
    console.info(`  Files processed: ${this.state.totalFilesProcessed}`);
    console.info(`  Documents processed: ${this.state.totalDocumentsProcessed}`);
    console.info(`  Documents successful: ${this.state.totalDocumentsSuccessful}`);
    console.info(`  Documents failed: ${this.state.totalDocumentsFailed}`);
    console.info(`  Errors encountered: ${this.state.errors.length}`);

    if (this.state.errors.length > 0) {
      console.info('\nErrors:');
      this.state.errors.forEach(error => {
        console.info(`  ${error.file}: ${error.error}`);
      });
    }
  }
}

export async function runLocalFolderBatch(pool: Pool, prefix: string, isNew: boolean, articlesList: ArticleChangeInfo[]): Promise<void> {
  const processor = new LocalFolderProcessor(pool, prefix);
  const skipArticleContents = prefix.includes('invalid');
  await processor.processAllFiles(isNew, articlesList, skipArticleContents);
}
