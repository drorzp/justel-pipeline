import * as fs from 'fs/promises';
import * as path from 'path';
import { compare } from 'fast-json-patch';
import pLimit from 'p-limit';

export interface ArticleChangeInfo {
  documentNumber: string;
  articles: string[];
}

export type ChangedArticlesMap = Map<string, Set<string>>;

export function buildChangedArticlesMap(list: ArticleChangeInfo[]): ChangedArticlesMap {
  const map = new Map<string, Set<string>>();
  for (const info of list) {
    map.set(info.documentNumber, new Set(info.articles));
  }
  return map;
}

interface CompareResult {
  changed: boolean;
  notFound: boolean;
  articleChanges?: ArticleChangeInfo;
}

const STEP1_DIR = path.join(process.cwd(), 'data/step1');
const OLDER_DIR = path.join(process.cwd(), 'data/older');

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

export function stripTimestamps(obj: any): any {
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
  currentDir: string,
  olderDir: string,
  readyDir: string,
  isInvalid: boolean = false
): Promise<CompareResult> {
  const currentPath = path.join(currentDir, filename);
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

  let hasChanges = false;

  if (isInvalid) {
    // For invalid documents, only compare title (document_hierarchy is empty)
    const currentTitle = currentData.document_metadata?.title || '';
    const olderTitle = olderData.document_metadata?.title || '';
    hasChanges = currentTitle !== olderTitle;
  } else {
    // Strip timestamps before comparing to ignore false positives
    const currentStripped = stripTimestamps(currentData);
    const olderStripped = stripTimestamps(olderData);
    const patches = compare(olderStripped, currentStripped);
    hasChanges = patches.length > 0;
  }

  if (hasChanges) {
    await fs.copyFile(currentPath, path.join(readyDir, filename));

    // Only track article changes for valid documents (invalid docs have no articles)
    if (!isInvalid) {
      const documentNumber = currentData.document_metadata?.document_number || '';
      const changedArticles = findChangedArticles(currentData, olderData);
      return {
        changed: true,
        notFound: false,
        articleChanges: { documentNumber, articles: changedArticles }
      };
    }

    return { changed: true, notFound: false };
  }

  return { changed: false, notFound: false };
}

async function processFolder(
  currentDir: string,
  olderDir: string,
  readyDir: string,
  isInvalid: boolean
): Promise<{ results: CompareResult[]; fileCount: number }> {
  await fs.mkdir(readyDir, { recursive: true });

  let files: string[] = [];
  try {
    files = await fs.readdir(currentDir);
  } catch {
    return { results: [], fileCount: 0 };
  }

  const jsonFiles = files.filter(f => f.endsWith('.json'));
  const limit = pLimit(50);

  const results = await Promise.all(
    jsonFiles.map(file => limit(() => compareAndCopyFile(file, currentDir, olderDir, readyDir, isInvalid)))
  );

  return { results, fileCount: jsonFiles.length };
}

export async function filterJSON(): Promise<ArticleChangeInfo[]> {
  // Process valid documents: current/valid → current/ready/valid
  const validResult = await processFolder(
    path.join(STEP1_DIR, 'current/valid'),
    OLDER_DIR,
    path.join(STEP1_DIR, 'current/ready/valid'),
    false
  );

  // Process invalid documents: current/invalid → current/ready/invalid (title-only comparison)
  const invalidResult = await processFolder(
    path.join(STEP1_DIR, 'current/invalid'),
    OLDER_DIR,
    path.join(STEP1_DIR, 'current/ready/invalid'),
    true
  );

  // Only valid documents contribute meaningful article changes
  const articleChanges = validResult.results
    .map(r => r.articleChanges)
    .filter((a): a is ArticleChangeInfo => a !== undefined);

  const logStats = (label: string, r: { results: CompareResult[]; fileCount: number }) => {
    const changed = r.results.filter(x => x.changed).length;
    const notFound = r.results.filter(x => x.notFound).length;
    console.log(`filterJSON ${label}: ${r.fileCount} total, ${changed} changed, ${notFound} not in older`);
  };

  logStats('valid', validResult);
  logStats('invalid', invalidResult);

  return articleChanges;
}

async function copyJsonFilesToOlder(sourceDir: string, olderDir: string): Promise<number> {
  let copied = 0;
  try {
    const files = await fs.readdir(sourceDir);
    for (const file of files.filter(f => f.endsWith('.json'))) {
      await fs.copyFile(
        path.join(sourceDir, file),
        path.join(olderDir, file)
      );
      copied++;
    }
  } catch {
    // Directory may not exist
  }
  return copied;
}

export async function updateOlderFolder(): Promise<void> {
  await fs.mkdir(OLDER_DIR, { recursive: true });

  const sourceFolders = ['current/ready/valid', 'current/ready/invalid', 'new/valid', 'new/invalid'];

  const counts: string[] = [];
  for (const folder of sourceFolders) {
    const copied = await copyJsonFilesToOlder(path.join(STEP1_DIR, folder), OLDER_DIR);
    if (copied > 0) {
      counts.push(`${copied} from ${folder}`);
    }
  }

  console.log(`updateOlderFolder: ${counts.length > 0 ? counts.join(', ') : 'no files copied'}`);
}
