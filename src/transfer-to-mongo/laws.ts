import { connectMongoDB, getDB, closeMongoDB } from '../mongodb/mongoConnect';
import { ReadOnlyDatabaseService, connectPostgreSQL } from '../postgres/pgConnect';
import logger from '../utils/logger';
import { Law } from './models/Law';
import { LawRoot } from './models/RootLaw';



async function getLawsList(startFromId?: string, endId?: string) {
  try {
    logger.info('Connecting to PostgreSQL...');
    await connectPostgreSQL();
    
    let query: string;
    let params: any[];
    query = 'SELECT id,document_number FROM public.documents ORDER BY id';
    
    const result = await ReadOnlyDatabaseService.query(query);
    
const laws = result.rows;
    logger.info(`Found ${laws.length} laws to process`);
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


export async function moveLawsToMongo(startId?: string, endId?: string) {
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
    const collection = db.collection('lawroots');
    const LawsList: any[] | null = await getLawsList();
    
    // Use for...of loop to properly handle async operations
    for (const law of LawsList!) {
      processedCount++;
      
      try {
        
        const result = await getLawFromPostgres(law.document_number);
        
        if (!result) {
          logger.info(`⚠️  No data for ${law.document_number}`);
          continue;
        }
        await LawRoot.findOneAndUpdate(
          { 
            document_number: law.document_number},
            result,  // Mongoose will handle $set automatically
            { 
              upsert: true, 
              new: true,
              timestamps: true,
              overwrite: true  // Makes it behave like replace
            }
          ).lean();

          const existingLaw = await Law.findOne({document_number: law.document_number});
          
          if(existingLaw){
            await Law.findOneAndUpdate(
              { 
                document_number: law.document_number},
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
    logger.info('Connections closed');
  }
}