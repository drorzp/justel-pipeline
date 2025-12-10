import { Pool, PoolClient } from 'pg';
import { connectMongoDB, getDB, closeMongoDB } from '../mongodb/mongoConnect';

import { Article } from './models/Articles';


async function getArticlesList(pool:Pool) {
  let client: PoolClient | null = null;
  try {
    console.info('Connecting to PostgreSQL...');
    client = await pool.connect();

    const query = 'SELECT id, document_number, article_number FROM public.article_contents ';
    const result = await client.query(query, []);

    const articles = result.rows;
    console.info(`Found ${articles.length} articles to process`);
    return articles;

  } catch (error) {
    console.error('Error getting laws list:', error);
    return null;
  } finally {
    try { client?.release(); } catch {}
  }
}


async function getArticleFromPostgres(client:PoolClient,document_number: string,article_number:string): Promise<any> {

  try { 
    const query = 'SELECT public.get_article_with_relations1($1,$2) as article_data';
    const result = await client.query(query, [document_number,article_number]);

    if (result.rows.length === 0 || !result.rows[0].article_data) {
      console.info(`No data for ${document_number} {article_number}`);
      return null;
    }
    
    const articleData = 
      typeof result.rows[0].article_data === 'string'
        ? JSON.parse(result.rows[0].article_data)
        : result.rows[0].article_data;
    
    console.info(`✓ Successfully fetched ${document_number} ${article_number}`);
    return articleData;
  } catch (error: unknown) {
    return null;
  } 
}

async function processArticle(pool: Pool, article: { document_number: string; article_number: string }) {
  let client: PoolClient | null = null;
  try {
    client = await pool.connect();
    const result = await getArticleFromPostgres(client, article.document_number, article.article_number);
    
    if (!result) {
      console.info(`⚠️  No data for ${article.document_number} ${article.article_number}`);
      return;
    }
    
    await Article.findOneAndReplace(
      { document_number: article.document_number, article_number: article.article_number },
      result,
      { upsert: true, new: true, timestamps: true, overwrite: true }
    ).lean();
  } catch (error) {
    console.error(`❌ Error processing ${article.document_number} ${article.article_number}:`, error);
  } finally {
    client?.release();
  }
}

export async function moveArticlesToMongo(pool: Pool, batchSize = 50) {
  try {
    console.info('Starting concurrent migration...');
    
    await connectMongoDB();
    
    const articleList = await getArticlesList(pool);
    if (!articleList || articleList.length === 0) {
      console.info('No articles to process');
      return;
    }
    
    console.info(`Processing ${articleList.length} articles in batches of ${batchSize}...`);
    
    // Process in batches
    for (let i = 0; i < articleList.length; i += batchSize) {
      const batch = articleList.slice(i, i + batchSize);
      await Promise.all(batch.map(article => processArticle(pool, article)));
      console.info(`✓ Completed batch ${Math.floor(i / batchSize) + 1}/${Math.ceil(articleList.length / batchSize)}`);
    }
    
    console.info('Migration complete');
  } catch (error) {
    console.error('Fatal error in concurrent migration:', error);
    process.exit(1);
  } finally {
    await closeMongoDB();
    console.info('Connections closed');
  }
}