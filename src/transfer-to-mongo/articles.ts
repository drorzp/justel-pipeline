import { Pool, PoolClient } from 'pg';
import { connectMongoDB, getDB, closeMongoDB } from '../mongodb/mongoConnect';

import { Article } from './models/Articles';


async function getArticlesList(pool:Pool) {
  let client: PoolClient | null = null;
  try {
    console.info('Connecting to PostgreSQL...');
    client = await pool.connect();

    const query = 'SELECT id, document_number, article_number FROM public.article_contents';
    const result = await client.query(query);

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


async function getArticleFromPostgres(pool:Pool,document_number: string,article_number:string): Promise<any> {
  let client: PoolClient | null = null;
  try { 
    client = await pool.connect();
    const query = 'SELECT public.article_with_relations($1,$2) as law_data';
    const result = await client.query(query, [document_number,article_number]);
    
    if (result.rows.length === 0 || !result.rows[0].law_data) {
      console.info(`No data for ${document_number}`);
      return null;
    }
    
    const lawData = 
      typeof result.rows[0].law_data === 'string'
        ? JSON.parse(result.rows[0].law_data)
        : result.rows[0].law_data;
    
    console.info(`✓ Successfully fetched ${document_number}`);
    return lawData;
  } catch (error: unknown) {
    return null;
  } finally {
    try { client?.release(); } catch {}
  }
}

export async function moveArticlesToMongo(pool:Pool) {
  
  try {
    console.info('Starting conservative migration...');
    
    // Connect to databases
    await connectMongoDB();
    
    const db = getDB();
    // const collection = db.collection('article_roots');
    const articleList: any[] | null = await getArticlesList(pool);
    
    // Use for...of loop to properly handle async operations
    for (const article of articleList!) {

      
      try {
        
        const result = await getArticleFromPostgres(pool,article.document_number,article.article_number);
        
        if (!result) {
          console.info(`⚠️  No data for ${article.document_number}`);
          continue;
        }
          await Article.findOneAndUpdate(
            { 
            document_number: article.document_number, article_number: article.article_number },
            result,  // Mongoose will handle $set automatically
            { 
              upsert: true, 
              new: true,
              timestamps: true,
              overwrite: true  // Makes it behave like replace
            }
          ).lean();
          console.log(`Created new article: ${article.document_number}-${article.article_number}`);
        }
         catch (error) {
        console.error(`❌ Error processing ${article.document_number}:`, error);
      }
    }
    
    // Final report
    
  } catch (error) {
    console.error('Fatal error in conservative migration:', error);
    process.exit(1);
  } finally {
    await closeMongoDB();
    console.info('Connections closed');
  }
}