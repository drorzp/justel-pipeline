import { Pool, PoolClient, PoolConfig } from 'pg';
import OpenAI from 'openai';
import * as dotenv from 'dotenv';

// Load env variables
dotenv.config();

// Types
export interface LLMConfig {
    openaiApiKey: string;
    model: string;
    maxRetries: number;
    retryDelay: number;
    requestDelay: number;
    concurrentRequests: number;
    batchSize: number;
}

export interface DocumentTitleRecord {
    id: number;
    document_number: string;
    old_title: string | null;
    new_title: string | null;
}

// Functional utilities and main processing entry

export async function getAllDocumentTitles(client: PoolClient, startFromId?: number): Promise<DocumentTitleRecord[]> {
    try {
        const query = `
        SELECT id, document_number, old_title, new_title
        FROM public.document_title
        WHERE old_title IS NOT NULL
        AND old_title != ''
        AND (new_title IS NULL OR new_title = '')`;

        const result = await client.query(query);
        console.info(`Found ${result.rows.length} documents needing title generation${startFromId ? ` (starting from ID ${startFromId})` : ''}`);
        console.info(`📋 These documents have old_title but missing new_title`);

        return result.rows as DocumentTitleRecord[];
    } catch (error) {
        console.error('Error fetching document titles:', error);
        throw error;
    }
}

export async function generateNewTitle(openai: OpenAI, config: LLMConfig, oldTitle: string, documentNumber: string): Promise<string> {
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
    while (retries < config.maxRetries) {
        try {
            const completion = await openai.chat.completions.create({
                model: config.model,
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
                console.info(`Title too long (${newTitle.length} chars), applying second pass refinement...`);
                const refinedTitle = await refineLongTitle(openai, config, newTitle);
                newTitle = refinedTitle || newTitle; // Fallback to original if refinement fails
            }

            return newTitle;
        } catch (error) {
            retries++;
            console.error(`Error generating title (attempt ${retries}/${config.maxRetries}):`, error);

            if (retries >= config.maxRetries) {
                throw new Error(`Failed to generate title after ${config.maxRetries} attempts: ${error}`);
            }

            // Wait before retrying
            await delay(config.retryDelay * retries);
        }
    }

    throw new Error('Unexpected error in generateNewTitle');
}

export async function refineLongTitle(openai: OpenAI, config: LLMConfig, longTitle: string): Promise<string | null> {
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
        const completion = await openai.chat.completions.create({
            model: config.model,
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
            console.info(`Refined title: "${refinedTitle}" (${refinedTitle.length} chars)`);
            return refinedTitle;
        }
        return null;
    } catch (error) {
        console.error('Error refining long title:', error);
        return null;
    }
}

export function createFallbackTitle(originalTitle: string): string {
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

export async function updateDocumentTitle(client: PoolClient, id: number, newTitle: string): Promise<void> {
    try {
        const query = `
        UPDATE public.document_title
        SET new_title = $1
        WHERE id = $2
      `;

        await client.query(query, [newTitle, id]);
    } catch (error) {
        console.error(`Error updating document title for ID ${id}:`, error);
        throw error;
    }
}

// Synchronize finalized titles into documents table
export async function applyNewTitlesToDocuments(client: PoolClient): Promise<number> {
    try {
        const query = `
                UPDATE public.documents AS d
                SET title = dt.new_title
                FROM public.document_title AS dt
                WHERE d.document_number = dt.document_number
                  AND dt.new_title IS NOT NULL
            `;
        const result = await client.query(query);
        console.info(`Updated ${result.rowCount ?? 0} document titles in documents table`);
        return result.rowCount ?? 0;
    } catch (error) {
        console.error('Error applying new titles to documents:', error);
        throw error;
    }
}

export async function processAllDocumentTitles(pool:Pool, config: LLMConfig): Promise<void> {
    const client = await pool.connect();
    const openai = new OpenAI({ apiKey: config.openaiApiKey });

    try {
        console.info('Starting document title processing...');

        const documents = await getAllDocumentTitles(client);

        if (documents.length === 0) {
            console.info('No documents found to process');
            return;
        }

        let processed = 0;
        let errors = 0;

        for (const doc of documents) {
            try {
                console.info(`Processing document ${processed + 1}/${documents.length} (ID: ${doc.id})`);

                // Check if old_title exists
                if (!doc.old_title) {
                    throw new Error(`Document ID ${doc.id} has no old_title to process`);
                }

                console.info(`Original title: "${doc.old_title}"`);

                // Generate new title using LLM
                const newTitle = await generateNewTitle(openai, config, doc.old_title, doc.document_number);
                console.info(`Generated title: "${newTitle}"`);

                // Update database
                await updateDocumentTitle(client, doc.id, newTitle);

                processed++;
                console.info(`✅ Successfully processed document ID ${doc.id}\n`);

                // Removed rate limiting delay for faster processing
            } catch (error) {
                errors++;
                console.error(`❌ Failed to process document ID ${doc.id}:`, error);
                
                // Create a fallback title to avoid leaving empty titles
                const fallbackTitle = createFallbackTitle(doc.old_title || `Document ${doc.document_number}`);
                console.info(`Using fallback title: "${fallbackTitle}"`);
                
                try {
                    await updateDocumentTitle(client, doc.id, fallbackTitle);
                    console.info(`✅ Updated with fallback title for document ID ${doc.id}`);
                } catch (updateError) {
                    console.error(`❌ Failed to update fallback title for document ID ${doc.id}:`, updateError);
                }
                
                console.info('Continuing with next document...\n');
            }
        }
        await applyNewTitlesToDocuments(client);
        console.info('\n=== Processing Complete ===');
        console.info(`Total documents: ${documents.length}`);
        console.info(`Successfully processed: ${processed}`);
        console.info(`Errors: ${errors}`);

    } catch (error) {
        console.error('Error in processAllDocumentTitles:', error);
        throw error;
    } finally {
        try {
            client?.release();
        } catch {}
    }
}

export async function delay(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
}

