import * as fs from 'fs/promises';
import * as path from 'path';

interface SummaryData {
  simmaryId: string;
  summary: string;
  keywordsCassation: string[];
  keywordsUtu: string[];
  keywordsFree: string;
  legalBasis: string[];
}

interface DecisionData {
  decision_id: string;
  summaries: SummaryData[];
  [key: string]: any;
}

interface TransformedSummary {
  decision_id: string;
  summary: string;
  legalbasis: string;
  created_at: string;
  updated_at: string;
}

class SummaryTransformer {
  
  /**
   * Transform a single decision JSON file to extract summaries for database insertion
   */
  static transformDecisionSummaries(decisionData: DecisionData): TransformedSummary[] {
    const transformedSummaries: TransformedSummary[] = [];
    const currentTimestamp = new Date().toISOString();
    
    if (!decisionData.summaries || decisionData.summaries.length === 0) {
      console.log(`No summaries found for decision: ${decisionData.decision_id}`);
      return transformedSummaries;
    }
    
    for (const summaryItem of decisionData.summaries) {
      // Join legal basis array into a single string, or use empty string if none
      const legalBasisString = summaryItem.legalBasis && summaryItem.legalBasis.length > 0 
        ? summaryItem.legalBasis.join('; ') 
        : '';
      
      const transformedSummary: TransformedSummary = {
        decision_id: decisionData.decision_id,
        summary: summaryItem.summary,
        legalbasis: legalBasisString,
        created_at: currentTimestamp,
        updated_at: currentTimestamp
      };
      
      transformedSummaries.push(transformedSummary);
    }
    
    return transformedSummaries;
  }
  
  /**
   * Process a single JSON file and return transformed summaries
   */
  static async processFile(filePath: string): Promise<TransformedSummary[]> {
    try {
      const fileContent = await fs.readFile(filePath, 'utf8');
      const decisionData: DecisionData = JSON.parse(fileContent);
      
      return this.transformDecisionSummaries(decisionData);
    } catch (error) {
      console.error(`Error processing file ${filePath}:`, error);
      return [];
    }
  }
  
  /**
   * Process all JSON files in a directory and return all transformed summaries
   */
  static async processDirectory(directoryPath: string): Promise<TransformedSummary[]> {
    const allSummaries: TransformedSummary[] = [];
    
    try {
      const files = await fs.readdir(directoryPath);
      const jsonFiles = files.filter(file => file.endsWith('.json'));
      
      console.log(`Found ${jsonFiles.length} JSON files to process`);
      
      for (const file of jsonFiles) {
        const filePath = path.join(directoryPath, file);
        const summaries = await this.processFile(filePath);
        allSummaries.push(...summaries);
        
        if (summaries.length > 0) {
          console.log(`Processed ${file}: ${summaries.length} summaries extracted`);
        }
      }
      
      return allSummaries;
    } catch (error) {
      console.error('Error processing directory:', error);
      throw error;
    }
  }
  
  /**
   * Generate SQL INSERT statements for the summaries
   */
  static generateInsertSQL(summaries: TransformedSummary[]): string {
    if (summaries.length === 0) {
      return '-- No summaries to insert';
    }
    
    const sqlLines: string[] = [
      'INSERT INTO public.summaries (decision_id, summary, legalbasis, created_at, updated_at)',
      'VALUES'
    ];
    
    const valueLines = summaries.map((summary, index) => {
      const isLast = index === summaries.length - 1;
      const escapedSummary = summary.summary.replace(/'/g, "''");
      const escapedLegalBasis = summary.legalbasis.replace(/'/g, "''");
      
      return `  ('${summary.decision_id}', '${escapedSummary}', '${escapedLegalBasis}', '${summary.created_at}', '${summary.updated_at}')${isLast ? ';' : ','}`;
    });
    
    sqlLines.push(...valueLines);
    
    return sqlLines.join('\n');
  }
  
  /**
   * Save transformed summaries to a JSON file
   */
  static async saveSummariesToJSON(summaries: TransformedSummary[], outputPath: string): Promise<void> {
    await fs.writeFile(outputPath, JSON.stringify(summaries, null, 2), 'utf8');
    console.log(`Saved ${summaries.length} summaries to ${outputPath}`);
  }
  
  /**
   * Save SQL INSERT statements to a file
   */
  static async saveSummariesToSQL(summaries: TransformedSummary[], outputPath: string): Promise<void> {
    const sql = this.generateInsertSQL(summaries);
    await fs.writeFile(outputPath, sql, 'utf8');
    console.log(`Saved SQL INSERT statements to ${outputPath}`);
  }
}

// Example usage function
async function main() {
  try {
    const inputDirectory = '/Users/drorzeplovitch/projects/justel-pipline/src/import-decisions';
    const outputJSONPath = path.join(inputDirectory, 'transformed-summaries.json');
    const outputSQLPath = path.join(inputDirectory, 'insert-summaries.sql');
    
    // Process all JSON files in the directory
    const transformedSummaries = await SummaryTransformer.processDirectory(inputDirectory);
    
    console.log(`\nTotal summaries extracted: ${transformedSummaries.length}`);
    
    if (transformedSummaries.length > 0) {
      // Save to JSON file
      await SummaryTransformer.saveSummariesToJSON(transformedSummaries, outputJSONPath);
      
      // Save to SQL file
      await SummaryTransformer.saveSummariesToSQL(transformedSummaries, outputSQLPath);
      
      // Show sample of first few summaries
      console.log('\nSample of transformed summaries:');
      transformedSummaries.slice(0, 3).forEach((summary, index) => {
        console.log(`\n${index + 1}. Decision: ${summary.decision_id}`);
        console.log(`   Summary: ${summary.summary.substring(0, 100)}...`);
        console.log(`   Legal Basis: ${summary.legalbasis}`);
      });
    }
    
  } catch (error) {
    console.error('Error in main process:', error);
  }
}

// Export for use in other modules
export { SummaryTransformer, TransformedSummary };

// Run if called directly
if (require.main === module) {
  main();
}
