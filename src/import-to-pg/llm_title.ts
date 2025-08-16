import { Client, ClientConfig } from 'pg';
import OpenAI from 'openai';
import * as dotenv from 'dotenv';
// UPDATE documents
// SET title = document_title.new_title 
// FROM document_title
// WHERE documents.document_number = document_title.document_number  and document_title.new_title is not null;
// Load environment variables
dotenv.config();

// Types
interface DocumentTitleRecord {
    id: number;
    old_title: string;
    document_number: string;
    new_title: string | null;
    document_id: number;
}

interface DatabaseConfig extends ClientConfig {
    user: string;
    host: string;
    database: string;
    password: string;
    port: number;
}

interface LLMConfig {
    openaiApiKey: string;
    model: 'gpt-4o-mini' | 'gpt-3.5-turbo';
    maxRetries: number;
    retryDelay: number;
    requestDelay: number;
    concurrentRequests: number;
    batchSize: number;
}

// Configuration
const dbConfig: DatabaseConfig = {
    user: process.env.DB_USER || 'postgres',
    host: '3.20.213.252',
    database: process.env.DB_NAME || 'lawyers',
    password: process.env.DB_PASSWORD || 'strongpassword',
    port: parseInt(process.env.DB_PORT || '5433'),
};

// MAXIMUM SPEED configuration - push the limits!
const llmConfig: LLMConfig = {
    openaiApiKey: process.env.OPENAI_API_KEY || '',
    model: 'gpt-4o-mini',
    maxRetries: 2, // Reduced retries for faster failure recovery
    retryDelay: 200, // Minimal retry delay
    requestDelay: 0, // No delay between requests (GPT-4o-mini has very high rate limits)
    concurrentRequests: 300, // EXTREME concurrency - GPT-4o-mini can handle this!
    batchSize: 2000, // Even larger batches for maximum throughput
};

class DocumentTitleProcessor {
    private client: Client;
    private openai: OpenAI;
    private config: LLMConfig;

    constructor(dbConfig: DatabaseConfig, llmConfig: LLMConfig) {
        this.client = new Client(dbConfig);
        this.openai = new OpenAI({
            apiKey: llmConfig.openaiApiKey,
        });
        this.config = llmConfig;
    }

    async connect(): Promise<void> {
        try {
            await this.client.connect();
            console.log('Connected to PostgreSQL database');
        } catch (error) {
            console.error('Failed to connect to database:', error);
            throw error;
        }
    }

    async disconnect(): Promise<void> {
        try {
            await this.client.end();
            console.log('Disconnected from PostgreSQL database');
        } catch (error) {
            console.error('Error disconnecting from database:', error);
        }
    }

    async getAllDocumentTitles(startFromId?: number): Promise<DocumentTitleRecord[]> {
        try {
            let query = `
        SELECT id, document_number, old_title, new_title, document_id
        FROM public.document_title
        WHERE old_title IS NOT NULL
        AND old_title != ''
        AND (new_title IS NULL OR new_title = '')`;

            if (startFromId) {
                query += ` AND id >= ${startFromId}`;
            }

            query += ` ORDER BY id`;

            const result = await this.client.query(query);
            console.log(`Found ${result.rows.length} documents needing title generation${startFromId ? ` (starting from ID ${startFromId})` : ''}`);
            console.log(`📋 These documents have old_title but missing new_title`);

            return result.rows as DocumentTitleRecord[];
        } catch (error) {
            console.error('Error fetching document titles:', error);
            throw error;
        }
    }

    async generateNewTitle(oldTitle: string, documentNumber: string): Promise<string> {
        const prompt = `
You are transforming Belgian legal document titles for web UI display. Create clean, consistent titles optimized for user interfaces.

Original Title: "${oldTitle}"
Document Number: ${documentNumber}

FORMATTING RULES:
1. Maximum 80 characters for optimal UI display
2. Use consistent format: "[Document Type] - [Main Subject] - [Specific Section]"
3. Remove all technical metadata (dates, version notes, URLs, consultation notes)
4. ⚠️ ABSOLUTELY CRITICAL: DO NOT INCLUDE ANY ARTICLE NUMBERS OR RANGES
5. ⚠️ NEVER include article information, even if mentioned in the original title
6. ⚠️ Remove all article references (Art., Articles, art. X-Y, etc.) from the output
7. Omit historical dates unless they're part of the document's common name
8. Use title case for main elements
9. DO NOT HALLUCINATE: Only transform what is actually present in the original title

EXAMPLES:
✅ CORRECT - Article range removed from output:
Input: "21 MARS 1804. - [ANCIEN] CODE CIVIL. - LIVRE III : Manières dont on acquiert la propriété. - TITRE I et II (art. 711-1100) (NOTE: consultation...)"
Output: "Code Civil - Livre III : Acquisition de la Propriété - Titres I-II"

✅ CORRECT - Clean title without article references:
Input: "10 SEPTEMBRE 1807. - CODE DE COMMERCE : LIVRE I. Du commerce en général. (NOTE: Consultation...)"
Output: "Code de Commerce - Livre I : Commerce en Général"

✅ CORRECT - Simple clean title:
Input: "12 DECEMBRE 1817. - Loi établissant des peines contre ceux qui favorisent la désertion..."
Output: "Loi - Peines Contre Favoriser la Désertion"

✅ CORRECT - Article range removed from output:
Input: "17 NOVEMBRE 1808. - CODE D'INSTRUCTION CRIMINELLE. - LIVRE PREMIER. (Art. 8 à 136ter) (Pour des raisons...)"
Output: "Code d'Instruction Criminelle - Livre Premier"

⚠️ REMEMBER: NEVER include article numbers or ranges in the output, even if they appear in the original!

🚫 FINAL WARNING: DO NOT INVENT ARTICLE NUMBERS. Only include them if they are clearly written in the original title.

Respond with only the transformed title, no additional text or explanation.
    `.trim();

        let retries = 0;
        while (retries < this.config.maxRetries) {
            try {
                const completion = await this.openai.chat.completions.create({
                    model: this.config.model,
                    messages: [
                        {
                            role: 'system',
                            content: 'You are a Belgian legal document title optimizer for web UI display. Transform verbose legal titles into clean, consistent, UI-friendly formats while preserving legal accuracy. CRITICAL: Never add information not present in the original title. Do not invent article numbers, dates, or any other details. Only transform and clean what actually exists in the source text. Follow the formatting rules exactly and keep titles under 80 characters when possible.'
                        },
                        {
                            role: 'user',
                            content: prompt
                        }
                    ],
                    max_tokens: 200,
                    temperature: 0.3,
                    top_p: 0.9,
                    frequency_penalty: 0.0,
                    presence_penalty: 0.0
                });

                let newTitle = completion.choices[0]?.message?.content?.trim();
                if (!newTitle) {
                    throw new Error('Empty response from OpenAI');
                }

                // Second pass for overly long titles
                if (newTitle.length > 80) {
                    console.log(`Title too long (${newTitle.length} chars), applying second pass refinement...`);
                    const refinedTitle = await this.refineLongTitle(newTitle);
                    newTitle = refinedTitle || newTitle; // Fallback to original if refinement fails
                }

                return newTitle;
            } catch (error) {
                retries++;
                console.error(`Error generating title (attempt ${retries}/${this.config.maxRetries}):`, error);

                if (retries >= this.config.maxRetries) {
                    throw new Error(`Failed to generate title after ${this.config.maxRetries} attempts: ${error}`);
                }

                // Wait before retrying
                await this.delay(this.config.retryDelay * retries);
            }
        }

        throw new Error('Unexpected error in generateNewTitle');
    }

    async refineLongTitle(longTitle: string): Promise<string | null> {
        const refinementPrompt = `
Make this Belgian legal document title more concise while preserving all essential legal information:

"${longTitle}"

RULES:
1. Maximum 70 characters
2. Remove any redundant words
3. Use abbreviations where appropriate (e.g., "Art." for "Articles")
4. Maintain legal accuracy
5. Keep the most important identifying elements

Respond with only the shortened title, no explanation.
    `.trim();

        try {
            const completion = await this.openai.chat.completions.create({
                model: this.config.model,
                messages: [
                    {
                        role: 'system',
                        content: 'You are a title compression specialist. Make legal titles more concise while preserving essential information.'
                    },
                    {
                        role: 'user',
                        content: refinementPrompt
                    }
                ],
                max_tokens: 100,
                temperature: 0.2,
                top_p: 0.9
            });

            const refinedTitle = completion.choices[0]?.message?.content?.trim();
            if (refinedTitle && refinedTitle.length < longTitle.length) {
                console.log(`Refined title: "${refinedTitle}" (${refinedTitle.length} chars)`);
                return refinedTitle;
            }
            return null;
        } catch (error) {
            console.error('Error refining long title:', error);
            return null;
        }
    }

    createFallbackTitle(originalTitle: string): string {
        // Simple rule-based fallback for when LLM fails
        let fallback = originalTitle
            // Remove dates at the beginning
            .replace(/^\d{1,2}\s+[A-Z]+\s+\d{4}\.?\s*-\s*/, '')
            // Remove technical notes and metadata
            .replace(/\(NOTE[^)]*\)/gi, '')
            .replace(/\(Intitulé[^)]*\)/gi, '')
            .replace(/\(Pour[^)]*\)/gi, '')
            .replace(/\[.*?\]/g, '')
            // Remove URLs
            .replace(/https?:\/\/[^\s)]+/g, '')
            // Clean up extra spaces and dashes
            .replace(/\s*-\s*-\s*/g, ' - ')
            .replace(/\s+/g, ' ')
            .trim();
        
        // Ensure it's not too long
        if (fallback.length > 80) {
            fallback = fallback.substring(0, 77) + '...';
        }
        
        // If still empty or too short, use a generic title
        if (fallback.length < 10) {
            fallback = 'Document Juridique';
        }
        
        return fallback;
    }

    async updateDocumentTitle(id: number, newTitle: string): Promise<void> {
        try {
            const query = `
        UPDATE public.document_title
        SET new_title = $1
        WHERE id = $2
      `;

            await this.client.query(query, [newTitle, id]);
        } catch (error) {
            console.error(`Error updating document title for ID ${id}:`, error);
            throw error;
        }
    }

    // Synchronize finalized titles into documents table
    async applyNewTitlesToDocuments(): Promise<number> {
        try {
            const query = `
                UPDATE public.documents AS d
                SET title = dt.new_title
                FROM public.document_title AS dt
                WHERE d.document_number = dt.document_number
                  AND dt.new_title IS NOT NULL
            `;
            const result = await this.client.query(query);
            console.log(`Updated ${result.rowCount ?? 0} document titles in documents table`);
            return result.rowCount ?? 0;
        } catch (error) {
            console.error('Error applying new titles to documents:', error);
            throw error;
        }
    }

    async processAllDocumentTitles(): Promise<void> {
        try {
            console.log('Starting document title processing...');

            const documents = await this.getAllDocumentTitles();

            if (documents.length === 0) {
                console.log('No documents found to process');
                return;
            }

            let processed = 0;
            let errors = 0;

            for (const doc of documents) {
                try {
                    console.log(`Processing document ${processed + 1}/${documents.length} (ID: ${doc.id})`);

                    // Check if old_title exists
                    if (!doc.old_title) {
                        throw new Error(`Document ID ${doc.id} has no old_title to process`);
                    }

                    console.log(`Original title: "${doc.old_title}"`);

                    // Generate new title using LLM
                    const newTitle = await this.generateNewTitle(doc.old_title, doc.document_number);
                    console.log(`Generated title: "${newTitle}"`);

                    // Update database
                    await this.updateDocumentTitle(doc.id, newTitle);

                    processed++;
                    console.log(`✅ Successfully processed document ID ${doc.id}\n`);

                    // Removed rate limiting delay for faster processing
                } catch (error) {
                    errors++;
                    console.error(`❌ Failed to process document ID ${doc.id}:`, error);
                    
                    // Create a fallback title to avoid leaving empty titles
                    const fallbackTitle = this.createFallbackTitle(doc.old_title || `Document ${doc.document_number}`);
                    console.log(`Using fallback title: "${fallbackTitle}"`);
                    
                    try {
                        await this.updateDocumentTitle(doc.id, fallbackTitle);
                        console.log(`✅ Updated with fallback title for document ID ${doc.id}`);
                    } catch (updateError) {
                        console.error(`❌ Failed to update fallback title for document ID ${doc.id}:`, updateError);
                    }
                    
                    console.log('Continuing with next document...\n');
                }
            }

            console.log('\n=== Processing Complete ===');
            console.log(`Total documents: ${documents.length}`);
            console.log(`Successfully processed: ${processed}`);
            console.log(`Errors: ${errors}`);

        } catch (error) {
            console.error('Error in processAllDocumentTitles:', error);
            throw error;
        }
    }

    private async delay(ms: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // Concurrent processing method
    async processAllDocumentTitlesConcurrent(startFromId?: number): Promise<void> {
        try {
            console.log('Starting concurrent document title processing...');
            const documents = await this.getAllDocumentTitles(startFromId);

            if (documents.length === 0) {
                console.log('No documents found to process');
                return;
            }

            console.log(`Found ${documents.length} documents to process`);
            console.log(`Using ${this.config.concurrentRequests} concurrent requests`);
            console.log(`Processing in batches of ${this.config.batchSize}`);

            let totalProcessed = 0;
            let totalErrors = 0;

            // Process documents in batches
            for (let i = 0; i < documents.length; i += this.config.batchSize) {
                const batch = documents.slice(i, i + this.config.batchSize);
                console.log(`\n=== Processing batch ${Math.floor(i / this.config.batchSize) + 1}/${Math.ceil(documents.length / this.config.batchSize)} (${batch.length} documents) ===`);

                const { processed, errors } = await this.processBatchConcurrent(batch, totalProcessed);
                totalProcessed += processed;
                totalErrors += errors;

                // Removed delay between batches for faster processing
                // GPT-4o-mini can handle high throughput
            }

            console.log('\n=== Processing Complete ===');
            console.log(`Total documents: ${documents.length}`);
            console.log(`Successfully processed: ${totalProcessed}`);
            console.log(`Errors: ${totalErrors}`);

        } catch (error) {
            console.error('Error in processAllDocumentTitlesConcurrent:', error);
            throw error;
        }
    }

    private async processBatchConcurrent(batch: DocumentTitleRecord[], startIndex: number): Promise<{ processed: number; errors: number }> {
        const semaphore = new Array(this.config.concurrentRequests).fill(null);
        let processed = 0;
        let errors = 0;
        let currentIndex = 0;

        const processDocument = async (doc: DocumentTitleRecord, docIndex: number): Promise<void> => {
            try {
                console.log(`Processing document ${startIndex + docIndex + 1} (ID: ${doc.id})`);

                // Check if old_title exists
                if (!doc.old_title) {
                    throw new Error(`Document ID ${doc.id} has no old_title to process`);
                }

                console.log(`Original title: "${doc.old_title.substring(0, 100)}${doc.old_title.length > 100 ? '...' : ''}"`); // Truncate long titles in logs

                const newTitle = await this.generateNewTitle(doc.old_title, doc.document_number);
                console.log(`Generated title: "${newTitle}"`);

                await this.updateDocumentTitle(doc.id, newTitle);
                processed++;
                console.log(`✅ Successfully processed document ID ${doc.id}`);

            } catch (error) {
                errors++;
                console.error(`❌ Failed to process document ID ${doc.id}:`, error);
            }
        };

        const worker = async (): Promise<void> => {
            while (currentIndex < batch.length) {
                const docIndex = currentIndex++;
                const doc = batch[docIndex];
                await processDocument(doc, docIndex);

                // Minimal delay only if configured (now 50ms instead of 500ms)
                if (this.config.requestDelay > 0) {
                    await this.delay(this.config.requestDelay);
                }
            }
        };

        // Start all workers
        const workers = semaphore.map(() => worker());
        await Promise.all(workers);

        return { processed, errors };
    }
}

// Helper to run only the cross-table UPDATE
export async function applyTitlesUpdate(): Promise<number> {
    const processor = new DocumentTitleProcessor(dbConfig, llmConfig);
    await processor.connect();
    try {
        const updated = await processor.applyNewTitlesToDocuments();
        return updated;
    } finally {
        await processor.disconnect();
    }
}

// Main execution function
export async function main(): Promise<void> {
    console.log('started')
    if (!llmConfig.openaiApiKey) {
        console.error('Error: OPENAI_API_KEY environment variable is required');
        process.exit(1);
    }
    // Check for command line argument to resume from specific ID
    const args = process.argv.slice(2);
    let startFromId: number | undefined;

    if (args.length > 0) {
        const resumeArg = args.find(arg => arg.startsWith('--resume='));
        if (resumeArg) {
            startFromId = parseInt(resumeArg.split('=')[1]);
            console.log(`🔄 Resuming processing from ID: ${startFromId}`);
        }
    }

    const processor = new DocumentTitleProcessor(dbConfig, llmConfig);

    try {
        console.log('connecting')
        await processor.connect();
        console.log('connected')
        console.log('DocumentTitleProcessor connected')
        await processor.processAllDocumentTitlesConcurrent(startFromId);
        console.log('DocumentTitleProcessor processed')
    } catch (error) {
        console.error('Fatal error:', error);
        process.exit(1);
    } finally {
        await processor.disconnect();
    }
}

// Run if this file is executed directly
if (require.main === module) {
    main().catch(console.error);
}
