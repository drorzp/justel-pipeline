import { connectMongoDB, getDB, closeMongoDB } from '../mongodb/mongoConnect';
import { ReadOnlyDatabaseService, connectPostgreSQL } from '../postgres/pgConnect';
import logger from '../utils/logger';

interface ArticleRow {
  id: string;
  document_number: string;
  article_number: string;
}

async function findLastArticleInMongo(): Promise<string | null> {
  try {
    const db = getDB();
    const collection = db.collection('article_roots');
    
    logger.info('🔍 Finding last article_id in MongoDB...');
    
    // Find the document with the highest article_id
    const lastArticle = await collection
      .findOne(
        {}, 
        { 
          sort: { id: -1 }, 
          projection: { id: 1, _id: 0 } 
        }
      );
    
    if (lastArticle) {
      logger.info(`📍 Last article_id found in MongoDB: ${lastArticle.id}`);
      return lastArticle.id;
    } else {
      logger.info('📍 No articles found in MongoDB, starting from beginning');
      return null;
    }
    
  } catch (error) {
    console.error('❌ Error finding last article in MongoDB:', error);
    return null;
  }
}

async function getArticlesList(startFromId?: string, endId?: string) {
  try {
    logger.info('Connecting to PostgreSQL...');
    await connectPostgreSQL();
    
    let query: string;
    let params: any[];
    
    if (startFromId && endId) {
      query = 'SELECT id,document_number, article_number FROM public.article_contents WHERE id >= $1 AND id <= $2 ORDER BY id';
      params = [startFromId, endId];
      logger.info(`📊 Getting articles between: ${startFromId} and ${endId}`);
    } else if (startFromId) {
      query = 'SELECT id,document_number, article_number FROM public.article_contents WHERE id >= $1 ORDER BY id';
      params = [startFromId];
      logger.info(`📊 Getting articles from: ${startFromId}`);
    } else if (endId) {
      query = 'SELECT id,document_number, article_number FROM public.article_contents WHERE id <= $1 ORDER BY id';
      params = [endId];
      logger.info(`📊 Getting articles up to: ${endId}`);
    } else {
      query = 'SELECT id,document_number, article_number FROM public.article_contents ORDER BY id';
      params = [];
      logger.info('📊 Getting all articles from beginning');
    }
    
    const result = await ReadOnlyDatabaseService.query(query, params);
    
const articles = result.rows;
    logger.info(`Found ${articles.length} articles to process`);
    return articles;
    
  } catch (error) {
    console.error('Error getting articles list:', error);
    return null;
  } 
}


async function getArticleFromPostgres(document_number: string, article_number: string): Promise<any> {
     try { 
      const query = 'SELECT public.get_article_with_relations1($1,$2) as article_data';
      const result = await ReadOnlyDatabaseService.query(query, [document_number, article_number]);
      
      if (result.rows.length === 0 || !result.rows[0].article_data) {
        logger.info(`No data for ${document_number}.${article_number}`);
        return null;
      }
      
      const articleData = 
        typeof result.rows[0].article_data === 'string'
          ? JSON.parse(result.rows[0].article_data)
          : result.rows[0].article_data;
      
      logger.info(`✓ Successfully fetched ${document_number}.${article_number}`);
      return articleData;
    } catch (error: unknown) {
    return null;
  }
}


export async function moveArticlesToMongo(startId?: string, endId?: string) {
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
    
    // Create index for better performance (handle existing duplicates)
    try {
      await collection.createIndex({ document_number: 1, article_number: 1 }, { unique: true, background: true });
      logger.info('✅ Unique index created successfully');
    } catch (error: any) {
      if (error.code === 11000) {
        logger.info('⚠️  Unique index already exists or duplicates found, continuing without unique constraint...');
        // Try to create non-unique index instead
        try {
          await collection.createIndex({ document_number: 1, article_number: 1 }, { background: true });
          logger.info('✅ Non-unique index created successfully');
        } catch (indexError) {
          logger.info('⚠️  Index may already exist, continuing...');
        }
      } else {
        throw error; // Re-throw if it's not a duplicate key error
      }
    }
    
    // Find last article in MongoDB to resume from
    const lastArticleId = await findLastArticleInMongo();
    
    const ArticlesList: ArticleRow[] | null = await getArticlesList(startId || lastArticleId || undefined, endId);
    
    if (!ArticlesList) {
      console.error('Failed to get articles list');
      return;
    }
    
    logger.info(`Processing ${ArticlesList.length} articles sequentially...`);
    
    // Use for...of loop to properly handle async operations
    for (const article of ArticlesList) {
      const document_number = article.document_number;
      const article_number = article.article_number;
      processedCount++;
      
      try {
        
        // Check if article already exists
        const existing = await collection.findOne({ document_number: document_number, article_number: article_number });
        if (existing) {
          logger.info(`⏭️  Skipping ${document_number}.${article_number} (already exists)`);
          continue;
        }
        
        const result = await getArticleFromPostgres(document_number, article_number);
        
        if (!result) {
          logger.info(`⚠️  No data for ${document_number}.${article_number}`);
          continue;
        }
        
        logger.info(`📝 Inserting ${document_number}.${article_number}`);
        await collection.insertOne({
          id: article.id,
          document_number: document_number,
          article_number: article_number,
          ...result,
          imported_at: new Date()
        });
        
        successCount++;
        
        // Progress report every 100 articles
        if (processedCount % 100 === 0) {
          const elapsed = (Date.now() - startTime) / 1000;
          const rate = Math.round(processedCount / elapsed);
          logger.info(`Progress: ${processedCount}/${ArticlesList.length} (${((processedCount/ArticlesList.length)*100).toFixed(2)}%) - ${rate} articles/sec`);
          logger.info(`Success: ${successCount}, Errors: ${errorCount}`);
        }
        
      } catch (error) {
        errorCount++;
        console.error(`❌ Error processing ${document_number}.${article_number}:`, error);
      }
    }
    
    // Final report
    const totalElapsed = (Date.now() - startTime) / 1000;
    logger.info('\n✅ Conservative article migration complete!');
    logger.info(`Total time: ${(totalElapsed / 60).toFixed(2)} minutes`);
    logger.info(`Average rate: ${Math.round(processedCount / totalElapsed)} articles/sec`);
    logger.info(`- Total processed: ${processedCount}`);
    logger.info(`- Successfully imported: ${successCount}`);
    logger.info(`- Errors: ${errorCount}`);
    
  } catch (error) {
    console.error('Fatal error in conservative migration:', error);
    process.exit(1);
  } finally {
    await closeMongoDB();
    logger.info('Connections closed');
  }
}
