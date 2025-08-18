import { connectMongoDB, getDB, closeMongoDB } from '../mongodb/mongoConnect';
import { ReadOnlyDatabaseService, connectPostgreSQL } from '../postgres/pgConnect';
import logger from '../utils/logger';




async function getArticlesList() {
  try {
    logger.info('Connecting to PostgreSQL...');
    await connectPostgreSQL();
    
    let query: string;
    let params: any[];
    query = 'SELECT id,document_number.article_number FROM public.article_contents';
    
    const result = await ReadOnlyDatabaseService.query(query);
    
const articles = result.rows;
    logger.info(`Found ${articles.length} laws to process`);
    return articles;
    
  } catch (error) {
    console.error('Error getting laws list:', error);
    return null;
  } 
}


async function getArticleFromPostgres(document_number: string,article_number:string): Promise<any> {
     try { 
      const query = 'SELECT public.article_with_relations($1,$2) as law_data';
      const result = await ReadOnlyDatabaseService.query(query, [document_number,article_number]);
      
      if (result.rows.length === 0 || !result.rows[0].law_data) {
        logger.info(`No data for ${document_number}`);
        return null;
      }
      
      const lawData = 
        typeof result.rows[0].law_data === 'string'
          ? JSON.parse(result.rows[0].law_data)
          : result.rows[0].law_data;
      
      logger.info(`✓ Successfully fetched ${document_number}`);
      return lawData;
    } catch (error: unknown) {
    return null;
  }
}


export async function moveArticlesToMongo() {
  const startTime = Date.now();
  let processedCount = 0;
  let successCount = 0;
  let errorCount = 0;
  
  try {
    logger.info('Starting conservative migration...');
    
    // Connect to databases
    await connectPostgreSQL();
    await connectMongoDB();
    
    const db = getDB();
    const collection = db.collection('article_roots');
    const articleList: any[] | null = await getArticlesList();
    
    // Use for...of loop to properly handle async operations
    for (const article of articleList!) {
      processedCount++;
      
      try {
        
        const result = await getArticleFromPostgres(article.document_number,article.article_number);
        
        if (!result) {
          logger.info(`⚠️  No data for ${article.document_number}`);
          continue;
        }
        await collection.replaceOne(
          { document_number: article.document_number, article_number: article.article_number },
          { $set: result },
          { upsert: true }
        );
        
        successCount++;
        
        // Progress report every 100 articles
        if (processedCount % 100 === 0) {
          const elapsed = (Date.now() - startTime) / 1000;
          const rate = Math.round(processedCount / elapsed);
        }
        
      } catch (error) {
        errorCount++;
        console.error(`❌ Error processing ${article.document_number}:`, error);
      }
    }
    
    // Final report
    
  } catch (error) {
    console.error('Fatal error in conservative migration:', error);
    process.exit(1);
  } finally {
    await closeMongoDB();
    logger.info('Connections closed');
  }
}