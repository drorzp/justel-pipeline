import OpenAI from 'openai';
import * as https from 'https';
import * as dotenv from 'dotenv';
import { GoogleGenerativeAI } from '@google/generative-ai';

dotenv.config();

export interface TransformationInput {
    document_number: string;
    article_number: string;
    main_text: string;
    main_text_raw: string;
}

export interface TransformationResult {
    success: boolean;
    transformedHtml?: string;
    error?: string;
    validationErrors?: string[];
    model?: 'deepseek' | 'gemini-2.5-flash';
    skipped?: boolean;
    skipReason?: string;
}

class HtmlTransformer {
    private deepseek: OpenAI;
    private gemini: GoogleGenerativeAI | null = null;
    private readonly RETRY_ATTEMPTS = 2;
    private readonly RETRY_DELAY = 100;
    private readonly DEEPSEEK_TOKEN_LIMIT = 6000;
    private readonly GEMINI_INPUT_TOKEN_LIMIT = 1000000; // 1M tokens
    private readonly GEMINI_OUTPUT_TOKEN_LIMIT = 55000; // 65K tokens

    constructor() {
        const deepseekApiKey = process.env.DEEPSEEK_API_KEY;
        if (!deepseekApiKey || deepseekApiKey === 'YOUR_DEEPSEEK_API_KEY_HERE') {
            throw new Error('DEEPSEEK_API_KEY not configured in .env file');
        }
        
        // Initialize Gemini if API key is available
        const googleApiKey = process.env.GOOGLE_API_KEY;
        console.log('🔍 Checking for GOOGLE_API_KEY:', !!googleApiKey);
        if (googleApiKey && googleApiKey !== 'YOUR_GOOGLE_API_KEY_HERE') {
            try {
                this.gemini = new GoogleGenerativeAI(googleApiKey);
                console.log('✅ Gemini 2.5 Flash initialized as fallback for large articles');
            } catch (error) {
                console.warn('⚠️ Failed to initialize Gemini:', error);
                this.gemini = null;
            }
        } else {
            console.log('ℹ️ GOOGLE_API_KEY not configured - Gemini fallback disabled');
        }

        const keepAliveAgent = new https.Agent({
            keepAlive: true,
            keepAliveMsecs: 1000,
            maxSockets: 200,
            maxFreeSockets: 50,
            timeout: 60000,
            scheduling: 'lifo'
        });

        this.deepseek = new OpenAI({
            apiKey: deepseekApiKey,
            baseURL: 'https://api.deepseek.com/v1',
            httpAgent: keepAliveAgent,
        } as any);
    }

    private buildPrompt(input: TransformationInput): string {
        return `You are an expert at restructuring Belgian legal HTML documents. Transform the following broken HTML into clean, well-structured HTML.

Article Number: ${input.article_number}

TASK: Create properly structured HTML for this legal article. The output should be clean, semantic HTML that preserves all content while fixing structural issues.

KEY REQUIREMENTS:
1. **PRESERVE ALL FOOTNOTES**: Any <span class="footnote-ref"> elements with their data-footnote-id, data-referenced-text, and data-direct-article-url attributes MUST be kept exactly as they appear with ALL attributes intact
2. **Smart list detection**: When you see numbered items (1°, 2°, 3°, etc.) that are clearly separate provisions or points (not just references within sentences), structure them as an ordered list with proper CSS classes
3. **Legal citations**: Preserve <L 1987-03-31/52...> style citations with appropriate styling
4. **Semantic structure**: Use proper HTML structure with appropriate CSS classes
5. **Complete content preservation**: Every word, punctuation mark, and special element must be preserved

CRITICAL: Footnote spans look like:
<span class="footnote-ref" data-footnote-id="[id]" data-referenced-text="[full text]" data-direct-article-url="[url]">[inline text]</span>
These are ESSENTIAL and must be preserved exactly where they appear with ALL data attributes intact.

INPUT HTML (broken/malformed):
${input.main_text}

PLAIN TEXT (for reference):
${input.main_text_raw}

OUTPUT REQUIREMENTS:
- Start with <article class="legal-article">
- Include a header with the article number  
- Use your intelligence to determine proper document structure
- Preserve footnotes and legal citations exactly
- Return ONLY the clean HTML code, no explanations

Generate the clean HTML:`;
    }

    private estimateTokens(html: string, plainText: string): number {
        const wordCount = plainText.split(/\s+/).filter(word => word.length > 0).length;
        const htmlOverhead = html.length > plainText.length 
            ? (html.length / plainText.length - 1) * 0.3 
            : 0;
        const legalComplexity = 1.1;
        const totalTokens = Math.ceil(wordCount * 1.3 * (1 + htmlOverhead) * legalComplexity * 2);
        return totalTokens;
    }
    
    private estimateOutputTokens(inputTokens: number): number {
        // HTML transformation typically produces 1.5-2x the input size
        // We'll use 1.8x as a conservative estimate
        return Math.ceil(inputTokens * 1.8);
    }

    private extractFootnoteIds(html: string): string[] {
        const footnoteRegex = /data-footnote-id="([^"]+)"/g;
        const ids: string[] = [];
        let match;
        while ((match = footnoteRegex.exec(html)) !== null) {
            ids.push(match[1]);
        }
        return ids;
    }

    private extractTextContent(html: string): string {
        return html
            .replace(/<[^>]*>/g, ' ')
            .replace(/\s+/g, ' ')
            .trim();
    }

    private shouldTransform(mainText: string): boolean {
        // Check if the HTML contains any of the required patterns
        const hasFootnoteRef = mainText.includes('<span class="footnote-ref"');
        const hasSectionSymbol = mainText.includes('§');
        const hasProvisionList = mainText.includes('<li class="provision"');
        
        return hasFootnoteRef || hasSectionSymbol || hasProvisionList;
    }

    private validateTransformation(original: string, transformed: string, articleNumber: string): {
        isValid: boolean;
        errors: string[];
    } {
        const errors: string[] = [];
        
        if (!transformed.includes('class="legal-article"')) {
            errors.push('Missing legal-article class');
        }
        
        if (!transformed.includes('class="article-number"') && 
            !transformed.includes('Article ' + articleNumber)) {
            errors.push('Missing article number in output');
        }
        
        const originalFootnotes = this.extractFootnoteIds(original);
        const transformedFootnotes = this.extractFootnoteIds(transformed);
        
        const missingFootnotes = originalFootnotes.filter(id => !transformedFootnotes.includes(id));
        if (missingFootnotes.length > 0) {
            errors.push(`Missing footnotes: ${missingFootnotes.join(', ')}`);
        }
        
        const transformedText = this.extractTextContent(transformed);
        if (transformedText.length < 50) {
            errors.push('Transformed content seems too short');
        }
        
        return {
            isValid: errors.length === 0,
            errors
        };
    }

    private async processWithGemini(input: TransformationInput, attempt: number = 1): Promise<string> {
        if (!this.gemini) {
            throw new Error('Gemini is not initialized');
        }
        
        try {
            const prompt = this.buildPrompt(input);
            
            const model = this.gemini.getGenerativeModel({ model: 'gemini-2.5-flash' });
            const result = await model.generateContent({
                contents: [{
                    role: 'user',
                    parts: [{ text: prompt }]
                }],
                generationConfig: {
                    temperature: 0.1,
                    maxOutputTokens: 8192, // Conservative limit for safety
                },
            });
            
            const response = result.response.candidates?.[0]?.content?.parts?.[0]?.text || '';
            
            if (!response || response.trim().length === 0) {
                throw new Error('Empty response from Gemini');
            }
            
            // Clean the response
            let cleanedResponse = response
                .replace(/^```html\s*/i, '')
                .replace(/\s*```$/i, '')
                .replace(/^```\s*/i, '')
                .replace(/\s*```$/i, '')
                .trim();
            
            if (!cleanedResponse.includes('class="legal-article"')) {
                throw new Error('Invalid HTML structure in response - missing legal-article class');
            }
            
            return cleanedResponse;
        } catch (error: any) {
            if (attempt < this.RETRY_ATTEMPTS) {
                const delay = this.RETRY_DELAY * attempt;
                await new Promise(resolve => setTimeout(resolve, delay));
                return this.processWithGemini(input, attempt + 1);
            }
            
            throw error;
        }
    }
    
    private async processWithRetry(input: TransformationInput, attempt: number = 1): Promise<string> {
        try {
            const prompt = this.buildPrompt(input);
            
            const completion = await this.deepseek.chat.completions.create({
                model: 'deepseek-chat',
                messages: [
                    {
                        role: 'system',
                        content: 'You are an expert HTML transformer for legal documents. You output only clean, valid HTML code without any markdown formatting or explanations.'
                    },
                    {
                        role: 'user',
                        content: prompt
                    }
                ],
                temperature: 0.1,
                max_tokens: 8192,
            });
            
            const response = completion.choices[0]?.message?.content || '';
            
            if (!response || response.trim().length === 0) {
                throw new Error('Empty response from DeepSeek');
            }
            
            let cleanedResponse = response
                .replace(/^```html\s*/i, '')
                .replace(/\s*```$/i, '')
                .replace(/^```\s*/i, '')
                .replace(/\s*```$/i, '')
                .trim();
            
            if (!cleanedResponse.includes('class="legal-article"')) {
                throw new Error('Invalid HTML structure in response - missing legal-article class');
            }
            
            return cleanedResponse;
        } catch (error: any) {
            if (attempt < this.RETRY_ATTEMPTS) {
                const delay = this.RETRY_DELAY * attempt;
                await new Promise(resolve => setTimeout(resolve, delay));
                return this.processWithRetry(input, attempt + 1);
            }
            
            throw error;
        }
    }

    async transform(input: TransformationInput): Promise<TransformationResult> {
        try {
            // Check if the content needs transformation
            if (!this.shouldTransform(input.main_text)) {
                console.log(`⏭️ Skipping transformation for article ${input.article_number} - no relevant patterns found`);
                return {
                    success: true,
                    skipped: true,
                    skipReason: 'No footnotes, section symbols, or provision lists found in content'
                };
            }
            
            // Check token limits and route to appropriate model
            const estimatedInputTokens = this.estimateTokens(input.main_text, input.main_text_raw);
            const estimatedOutputTokens = this.estimateOutputTokens(estimatedInputTokens);
            
            let transformedHtml: string;
            let modelUsed: 'deepseek' | 'gemini-2.5-flash';
            
            // Intelligent routing based on token counts
            if (estimatedInputTokens <= this.DEEPSEEK_TOKEN_LIMIT) {
                // Use DeepSeek for smaller articles
                console.log(`\ud83c\udfaf Using DeepSeek (${estimatedInputTokens} tokens)`);
                modelUsed = 'deepseek';
                transformedHtml = await this.processWithRetry(input);
                
            } else if (this.gemini && estimatedOutputTokens <= this.GEMINI_OUTPUT_TOKEN_LIMIT) {
                // Use Gemini for larger articles that fit within output limits
                console.log(`\ud83c\udf1f Using Gemini 2.5 Flash (${estimatedInputTokens} input tokens, ~${estimatedOutputTokens} estimated output)`);
                modelUsed = 'gemini-2.5-flash';
                transformedHtml = await this.processWithGemini(input);
                
            } else {
                // Article too large even for Gemini
                const reason = !this.gemini 
                    ? 'Article exceeds DeepSeek limit and Gemini is not configured'
                    : `Estimated output (${estimatedOutputTokens} tokens) exceeds Gemini limit (${this.GEMINI_OUTPUT_TOKEN_LIMIT} tokens)`;
                    
                return {
                    success: false,
                    error: `Cannot process article: ${reason}. Input: ${estimatedInputTokens} tokens`
                };
            }
            
            // Validate the transformation
            const validation = this.validateTransformation(
                input.main_text,
                transformedHtml,
                input.article_number
            );
            
            if (!validation.isValid) {
                return {
                    success: false,
                    transformedHtml,
                    validationErrors: validation.errors,
                    model: modelUsed
                };
            }
            
            return {
                success: true,
                transformedHtml,
                model: modelUsed
            };
            
        } catch (error: any) {
            // If DeepSeek fails for non-token reasons, try Gemini as fallback
            if (error.message && !error.message.includes('token') && this.gemini) {
                console.log('\u26a0\ufe0f DeepSeek failed, trying Gemini as fallback...');
                try {
                    const transformedHtml = await this.processWithGemini(input);
                    const validation = this.validateTransformation(
                        input.main_text,
                        transformedHtml,
                        input.article_number
                    );
                    
                    if (!validation.isValid) {
                        return {
                            success: false,
                            transformedHtml,
                            validationErrors: validation.errors,
                            model: 'gemini-2.5-flash'
                        };
                    }
                    
                    return {
                        success: true,
                        transformedHtml,
                        model: 'gemini-2.5-flash'
                    };
                } catch (geminiError: any) {
                    return {
                        success: false,
                        error: `Both models failed. DeepSeek: ${error.message}, Gemini: ${geminiError.message}`
                    };
                }
            }
            
            return {
                success: false,
                error: error.message || 'Unknown error during transformation'
            };
        }
    }
}

// Singleton instance
let transformerInstance: HtmlTransformer | null = null;

/**
 * Main export function to transform HTML for a single article
 * @param input The article data to transform
 * @returns Promise<TransformationResult> with success status and transformed HTML or error details
 */
export async function transformArticleHtml(input: TransformationInput): Promise<TransformationResult> {
    // Create singleton instance on first use
    if (!transformerInstance) {
        try {
            transformerInstance = new HtmlTransformer();
        } catch (error: any) {
            return {
                success: false,
                error: `Failed to initialize transformer: ${error.message}`
            };
        }
    }
    
    return transformerInstance.transform(input);
}