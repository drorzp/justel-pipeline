import { connectMongoDB, getDB, closeMongoDB } from '../mongodb/mongoConnect';
import { ReadOnlyDatabaseService, connectPostgreSQL } from '../postgres/pgConnect';


async function findLastLawInMongo(): Promise<string | null> {
  try {
    const db = getDB();
    const collection = db.collection('lawroots');
    
    console.log('🔍 Finding last law_id in MongoDB...');
    
    // Find the document with the highest article_id
    const lastLaw = await collection
      .findOne(
        {}, 
        { 
          sort: { id: -1 }, 
          projection: { id: 1, } 
        }
      );
    
    if (lastLaw) {
      console.log(`📍 Last law_id found in MongoDB: ${lastLaw.id}`);
      return lastLaw.id;
    } else {
      console.log('📍 No laws found in MongoDB, starting from beginning');
      return null;
    }
    
  } catch (error) {
    console.error('❌ Error finding last law in MongoDB:', error);
    return null;
  }
}

async function getLawsList(startFromId?: string, endId?: string) {
  try {
    console.log('Connecting to PostgreSQL...');
    await connectPostgreSQL();
    
    let query: string;
    let params: any[];
    
    if (startFromId && endId) {
      query = 'SELECT id,document_number FROM public.documents WHERE id >= $1 AND id <= $2 ORDER BY id';
      params = [startFromId, endId];
      console.log(`📊 Getting laws between: ${startFromId} and ${endId}`);
    } else if (startFromId) {
      query = 'SELECT id,document_number FROM public.documents WHERE id >= $1 ORDER BY id';
      params = [startFromId];
      console.log(`📊 Getting laws from: ${startFromId}`);
    } else if (endId) {
      query = 'SELECT id,document_number FROM public.documents WHERE id <= $1 ORDER BY id';
      params = [endId];
      console.log(`📊 Getting laws up to: ${endId}`);
    } else {
      query = 'SELECT id,document_number FROM public.documents ORDER BY id';
      params = [];
      console.log('📊 Getting all laws from beginning');
    }
    
    const result = await ReadOnlyDatabaseService.query(query, params);
    
const laws = result.rows;
    console.log(`Found ${laws.length} laws to process`);
    return laws;
    
  } catch (error) {
    console.error('Error getting laws list:', error);
    return null;
  } 
}


async function getLawFromPostgres(document_number: string): Promise<any> {
     try { 
      const query = 'SELECT public.get_document_data($1) as law_data';
      const result = await ReadOnlyDatabaseService.query(query, [document_number]);
      
      if (result.rows.length === 0 || !result.rows[0].law_data) {
        console.log(`No data for ${document_number}`);
        return null;
      }
      
      const lawData = 
        typeof result.rows[0].law_data === 'string'
          ? JSON.parse(result.rows[0].law_data)
          : result.rows[0].law_data;
      
      console.log(`✓ Successfully fetched ${document_number}`);
      return lawData;
    } catch (error: unknown) {
    return null;
  }
}


export async function moveLawsToMongo(startId?: string, endId?: string) {
  const startTime = Date.now();
  let processedCount = 0;
  let successCount = 0;
  let errorCount = 0;
  
  try {
    console.log('Starting conservative migration...');
    
    // Connect to databases
    await connectPostgreSQL();
    await connectMongoDB();
    
    const db = getDB();
    const collection = db.collection('lawroots');
    const collections = await db.listCollections().toArray();
    console.log('Collections in database:', collections.map(c => c.name));

    
    // Find last article in MongoDB to resume from
    const lastLawId = await findLastLawInMongo();
    
    const LawsList: any[] | null = await getLawsList(startId || lastLawId || undefined, endId);
    
    if (!LawsList) {
      console.error('Failed to get laws list');
      return;
    }
    
    console.log(`Processing ${LawsList.length} laws sequentially...`);
    
    // Use for...of loop to properly handle async operations
    for (const law of LawsList) {
      processedCount++;
      
      try {
        
        const result = await getLawFromPostgres(law.document_number);
        
        if (!result) {
          console.log(`⚠️  No data for ${law.document_number}`);
          continue;
        }
        
        await collection.insertOne(result);
        
        successCount++;
        
        // Progress report every 100 articles
        if (processedCount % 100 === 0) {
          const elapsed = (Date.now() - startTime) / 1000;
          const rate = Math.round(processedCount / elapsed);
        }
        
      } catch (error) {
        errorCount++;
        console.error(`❌ Error processing ${law.document_number}:`, error);
      }
    }
    
    // Final report
    
  } catch (error) {
    console.error('Fatal error in conservative migration:', error);
    process.exit(1);
  } finally {
    await closeMongoDB();
    console.log('Connections closed');
  }
}