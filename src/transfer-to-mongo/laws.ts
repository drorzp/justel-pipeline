import { connectMongoDB, getDB, closeMongoDB } from '../mongodb/mongoConnect';
import { Pool, PoolClient} from 'pg';
import { Law } from './models/Law';
import { LawRoot } from './models/RootLaw';



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


export async function moveLawsToMongo(pool:Pool, ) {
  const startTime = Date.now();
  let processedCount = 0;
  let successCount = 0;
  let errorCount = 0;
  
  try {
    console.info('Starting conservative migration...');
    
    // Connect to databases
    const client: PoolClient = await pool.connect();
    await connectMongoDB();
    
    const db = getDB();
    const collection = db.collection('lawroots');
    const LawsList: any[] | null = await getLawsList(client);
    
    // Use for...of loop to properly handle async operations
    for (const law of LawsList!) {
      processedCount++;
      
      try {
        
        const result = await getLawFromPostgres(client,law.document_number);
        
        if (!result) {
          console.info(`⚠️  No data for ${law.document_number}`);
          continue;
        }
        await LawRoot.findOneAndUpdate(
          { 
            document_number: result.document_number},
            result,  // Mongoose will handle $set automatically
            { 
              upsert: true, 
              new: true,
              timestamps: true,
              overwrite: true  // Makes it behave like replace
            }
          ).lean();

          const existingLaw = await Law.findOne({document_number: result.document_number});

          if(existingLaw){
            await Law.findOneAndUpdate(
              { 
                document_number: result.document_number},
                result,  // Mongoose will handle $set automatically
                { 
                  upsert: true, 
                  new: true,
                  timestamps: true,
                  overwrite: true  // Makes it behave like replace
                }
              ).lean();
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
    console.info('Connections closed');
  }
}