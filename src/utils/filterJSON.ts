import * as fs from 'fs/promises';
import * as path from 'path';
import { compare } from 'fast-json-patch';
import pLimit from 'p-limit';

export interface ArticleChangeInfo {
  documentNumber: string;
  articles: string[];
}

interface CompareResult {
  changed: boolean;
  notFound: boolean;
  articleChanges?: ArticleChangeInfo;
}

// Fields to ignore when comparing (timestamps that change every run)
const IGNORE_FIELDS = ['extraction_date', 'generation_timestamp'];

// Fields to compare when detecting article-level changes
const ARTICLE_COMPARE_FIELDS = [
  'anchor_id',
  'main_text_raw',
  'numbered_provisions',
  'raw_markdown',
  'abrogation_status',
  'main_text',
  'enhanced_citations'
];

function stripTimestamps(obj: any): any {
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }

  if (Array.isArray(obj)) {
    return obj.map(stripTimestamps);
  }

  const result: any = {};
  for (const key of Object.keys(obj)) {
    if (!IGNORE_FIELDS.includes(key)) {
      result[key] = stripTimestamps(obj[key]);
    }
  }
  return result;
}

function collectArticles(obj: any): Map<string, any> {
  const articles = new Map<string, any>();

  function traverse(node: any): void {
    if (node === null || typeof node !== 'object') {
      return;
    }

    if (Array.isArray(node)) {
      for (const item of node) {
        traverse(item);
      }
      return;
    }

    if (node.type === 'article' && node.article_content?.article_number) {
      articles.set(node.article_content.article_number, node);
    }

    for (const value of Object.values(node)) {
      traverse(value);
    }
  }

  traverse(obj);
  return articles;
}

function extractArticleCompareData(article: any): any {
  const result: any = {};
  const content = article.article_content?.content;
  const articleContent = article.article_content;

  if (articleContent?.anchor_id !== undefined) {
    result.anchor_id = articleContent.anchor_id;
  }

  if (content && typeof content === 'object') {
    for (const field of ARTICLE_COMPARE_FIELDS) {
      if (field !== 'anchor_id' && content[field] !== undefined) {
        result[field] = content[field];
      }
    }
  }

  return result;
}

function findChangedArticles(currentData: any, olderData: any): string[] {
  const currentArticles = collectArticles(currentData);
  const olderArticles = collectArticles(olderData);
  const changedArticleNumbers: string[] = [];

  for (const [articleNumber, currentArticle] of currentArticles) {
    const olderArticle = olderArticles.get(articleNumber);

    if (!olderArticle) {
      changedArticleNumbers.push(articleNumber);
      continue;
    }

    const currentExtracted = extractArticleCompareData(currentArticle);
    const olderExtracted = extractArticleCompareData(olderArticle);

    const patches = compare(olderExtracted, currentExtracted);
    if (patches.length > 0) {
      changedArticleNumbers.push(articleNumber);
    }
  }

  return changedArticleNumbers;
}

async function compareAndCopyFile(
  filename: string,
  currentValidDir: string,
  olderDir: string,
  readyDir: string
): Promise<CompareResult> {
  const currentPath = path.join(currentValidDir, filename);
  const olderPath = path.join(olderDir, filename);

  try {
    await fs.access(olderPath);
  } catch {
    return { changed: false, notFound: true };
  }

  const [currentData, olderData] = await Promise.all([
    fs.readFile(currentPath, 'utf-8').then(JSON.parse),
    fs.readFile(olderPath, 'utf-8').then(JSON.parse),
  ]);

  // Strip timestamps before comparing to ignore false positives
  const currentStripped = stripTimestamps(currentData);
  const olderStripped = stripTimestamps(olderData);

  const patches = compare(olderStripped, currentStripped);

  if (patches.length > 0) {
    const changedArticles = findChangedArticles(currentData, olderData);
    const documentNumber = currentData.document_metadata?.document_number || '';

    await fs.copyFile(currentPath, path.join(readyDir, filename));
    return {
      changed: true,
      notFound: false,
      articleChanges: {
        documentNumber,
        articles: changedArticles
      }
    };
  }

  return { changed: false, notFound: false };
}

export async function filterJSON(): Promise<ArticleChangeInfo[]> {
  const currentValidDir = path.join(process.cwd(), 'data/step1/current/valid');
  const olderDir = path.join(process.cwd(), 'data/older');
  const readyDir = path.join(process.cwd(), 'data/step1/current/ready');

  await fs.mkdir(readyDir, { recursive: true });

  const files = await fs.readdir(currentValidDir);
  const jsonFiles = files.filter(f => f.endsWith('.json'));

  const limit = pLimit(50);

  const results = await Promise.all(
    jsonFiles.map(file => limit(() => compareAndCopyFile(file, currentValidDir, olderDir, readyDir)))
  );

  const changed = results.filter(r => r.changed).length;
  const notFound = results.filter(r => r.notFound).length;

  const articleChanges = results
    .filter(r => r.articleChanges)
    .map(r => r.articleChanges!);

  console.log(`filterJSON: ${jsonFiles.length} total, ${changed} changed, ${notFound} not in older`);

  return articleChanges;
}

export async function updateOlderFolder(): Promise<void> {
  const readyDir = path.join(process.cwd(), 'data/step1/current/ready');
  const newValidDir = path.join(process.cwd(), 'data/step1/new/valid');
  const olderDir = path.join(process.cwd(), 'data/older');

  // Ensure older directory exists
  await fs.mkdir(olderDir, { recursive: true });

  let copiedFromReady = 0;
  let copiedFromNew = 0;

  // Copy from current/ready
  try {
    const readyFiles = await fs.readdir(readyDir);
    for (const file of readyFiles.filter(f => f.endsWith('.json'))) {
      await fs.copyFile(
        path.join(readyDir, file),
        path.join(olderDir, file)
      );
      copiedFromReady++;
    }
  } catch {
    // Directory may not exist if no files changed
  }

  // Copy from new/valid
  try {
    const newFiles = await fs.readdir(newValidDir);
    for (const file of newFiles.filter(f => f.endsWith('.json'))) {
      await fs.copyFile(
        path.join(newValidDir, file),
        path.join(olderDir, file)
      );
      copiedFromNew++;
    }
  } catch {
    // Directory may not exist if no new files
  }

  console.log(`updateOlderFolder: ${copiedFromReady} from ready, ${copiedFromNew} from new/valid`);
}
