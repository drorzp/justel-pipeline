import { connectMongoDB, getDB, closeMongoDB } from '../mongodb/mongoConnect';
import { Pool, PoolClient} from 'pg';
import { Law } from './models/Laws';



async function getLawsList(client:PoolClient) {
  try {
    console.info('Connecting to PostgreSQL...');

    
    let query: string;
    let params: any[];
    query = 'SELECT id,document_number FROM public.documents ORDER BY id';
    
    const result = await client.query(query);
    
const laws = result.rows;
    console.info(`Found ${laws.length} laws to process`);
    return laws;
    
  } catch (error) {
    console.error('Error getting laws list:', error);
    return null;
  } 
}


async function getLawFromPostgres(client:PoolClient,document_number: string): Promise<any> {
     try { 
      const query = 'SELECT public.get_document_data($1) as law_data';
      const result = await client.query(query, [document_number]);
      
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
  }
}


async function processLaw(pool: Pool, law: { id: number; document_number: string }): Promise<{ success: boolean; document_number: string }> {
  const client = await pool.connect();
  try {
    const result = await getLawFromPostgres(client, law.document_number);
    
    if (!result) {
      console.info(`⚠️  No data for ${law.document_number}`);
      return { success: false, document_number: law.document_number };
    }
    
    await Law.findOneAndReplace(
      { document_number: result.document_number },
      result,
      { 
        upsert: true, 
        new: true,
        timestamps: true,
        overwrite: true
      }
    ).lean();
    
    return { success: true, document_number: law.document_number };
  } catch (error) {
    console.error(`❌ Error processing ${law.document_number}:`, error);
    return { success: false, document_number: law.document_number };
  } finally {
    client.release();
  }
}

export async function moveLawsToMongo(pool: Pool, batchSize = 80) {
  try {
    console.info('Starting concurrent migration...');
    
    const client: PoolClient = await pool.connect();
    await connectMongoDB();
    
    const LawsList: any[] | null = await getLawsList(client);
    client.release();
    
    if (!LawsList || LawsList.length === 0) {
      console.info('No laws to process');
      return;
    }
    
    let processedCount = 0;
    let errorCount = 0;
    const totalLaws = LawsList.length;
    
    // Process in parallel batches
    for (let i = 0; i < totalLaws; i += batchSize) {
      const batch = LawsList.slice(i, i + batchSize);
      
      const results = await Promise.all(
        batch.map(law => processLaw(pool, law))
      );
      
      results.forEach(result => {
        processedCount++;
        if (!result.success) errorCount++;
      });
      
      console.info(`Progress: ${processedCount}/${totalLaws} (${errorCount} errors)`);
    }
    
    console.info(`✓ Migration complete: ${processedCount} processed, ${errorCount} errors`);
    
  } catch (error) {
    console.error('Fatal error in concurrent migration:', error);
    process.exit(1);
  } finally {
    await closeMongoDB();
    console.info('Connections closed');
  }
}