import * as dotenv from 'dotenv';
import { GoogleGenerativeAI } from '@google/generative-ai';
import * as path from 'path';

// Load .env from the project root
dotenv.config({ path: path.join(__dirname, '../../.env') });

export interface TransformationInput {
    document_number: string;
    article_number: string;
    main_text: string;
    raw_markdown: string;
}

export interface TransformationResult {
    success: boolean;
    transformedHtml?: string;
    error?: string;
    validationErrors?: string[];
    skipped?: boolean;
    skipReason?: string;
}

class HtmlTransformer {
    private gemini: GoogleGenerativeAI;
    private readonly RETRY_ATTEMPTS = 2;
    private readonly RETRY_DELAY = 10;
    private readonly GEMINI_OUTPUT_TOKEN_LIMIT = 55000; // 55K token limit for output

    constructor() {
        // Initialize Gemini
        const googleApiKey = process.env.GOOGLE_API_KEY || process.env.GEMINI_API_KEY;
        if (!googleApiKey || googleApiKey === 'YOUR_GOOGLE_API_KEY_HERE') {
            throw new Error('GOOGLE_API_KEY/GEMINI_API_KEY not configured in .env file');
        }
        
        this.gemini = new GoogleGenerativeAI(googleApiKey);
        console.log('✅ Gemini 2.5 Flash initialized');
    }

    private buildPrompt(input: TransformationInput): string {
        return `You are an expert legal document parser. Your task is to convert the provided raw Markdown (MD) text of a Belgian law article into a single, clean, and perfectly structured HTML document.

**Primary Directive:** The raw MD is the absolute source of truth for all text content. The final HTML must accurately represent all content and structure from the MD, while correctly incorporating pre-formatted tables from the reference HTML.

**Output Format:** Your response MUST be only the raw HTML code. Do not include any explanations or markdown formatting like \`\`\`html.

---
### ## HTML Structure and Rules
Follow this structure precisely. Use the specified tags and CSS classes as seen in the structural reference HTML.

**1. Article Root:** The entire content must be wrapped in \`<article class="legal-article" id="...">\`.

**2. Paragraphs (§):**
* Each paragraph (e.g., \`§ 1er.\`) must be a \`<section class="paragraph">\`.
* The paragraph marker itself (e.g., \`§ 1er.\`) goes into an \`<h3 class="paragraph-marker">\`.
* The content of the paragraph goes into a \`<div class="paragraph-content">\`.

**3. Numbered Provisions (1°, 2°):**
* These lists must be rendered as an \`<ol class="numbered-provisions">\`.
* Each item (\`1°\`, \`2°bis\`) must be an \`<li class="provision" data-number="...">\`. The \`data-number\` attribute must contain the provision number (e.g., \`1°\`).
* The text of the provision must be wrapped in a \`<span class="provision-text">\`.

**4. Rule for Nested Lists (Sub-Provisions):**
* **Identifier:** Within the text of a single main provision, you must identify sequences of markers like \`a)\`, \`b)\`, \`-\`, etc. **Crucially, you must do this even if they appear on the same line and are separated by characters like semicolons.**
* **Action:** You must **split the text at each of these markers** to create a nested list. Render this as a nested ordered (\`<ol>\`) or unordered (\`<ul>\`) list *inside* the parent \`<li class="provision">\` element. Each item in this nested list should be an \`<li class="sub-provision">\` with a \`data-marker\` attribute (e.g., \`data-marker="a)"\`).

**5. Rule for Numbered Footnotes \`[1... ]1\`:**
* **Identifier:** In the raw MD, find text enclosed in numbered square brackets, like \`[1 some text ]1\`.
* **Action:** Wrap the text content (ensuring you **remove the surrounding square brackets and numbers**) in the HTML with a \`<span class="footnote footnote-reference">\`.
* **Scope and Nesting (IMPORTANT):** The \`<span>\` must wrap *all* content between its opening \`[number\` and closing \`]number\` markers, regardless of length. This content can span multiple paragraphs or even the entire article. Handle nested footnotes (e.g., \`[1... [2...]2 ...]1\`) by correctly nesting the corresponding \`<span>\` tags in the final HTML.
* **Data Source:** The details for this footnote are in the list at the end of the MD, identified by a corresponding number, like \`(1)<L [2013-06-28\/04]... >\`.
* **Data Extraction:** From the citation text (e.g., \`<L 2022-11-22\/06, art. 31, ...>\`), you must extract the following and add them as \`data-*\` attributes:
    * \`data-footnote-id\`: The number of the footnote (e.g., \`1\` from \`(1)\`).
    * \`data-dossier-number\`: The date-based identifier (e.g., \`2022-11-22\/06\`).
    * \`data-law-type\`: The preceding letter (\`L\`, \`AR\`, etc.).
    * \`data-article-number\`: The number following \`art.\` (e.g., \`31\`).

**6. Rule for In-line Legal Citations \`<...>\`:**
* **Identifier:** In the raw MD, find standalone legal citations enclosed in angle brackets, like \`<L 2000-03-24\/50, ...>\`. These can appear anywhere in the text.
* **Action:** Create a \`<span class="legal-citation legal-citation-standard">\` for this.
* **Content:** The text of the citation itself (e.g., \`<L 2000-03-24\/50, art. 4, 034; En vigueur : 14-05-2000>\`) should be placed inside this span.
* **Data Extraction:** From the citation text (e.g., \`<L 2000-03-24\/50, art. 4, ...>\`), you must extract the following and add them as \`data-*\` attributes:
    * \`data-dossier-number\`: The date-based identifier (e.g., \`2000-03-24\/50\`).
    * \`data-law-type\`: The preceding letter (\`L\`, \`AR\`, etc.).
    * \`data-article-number\`: The number following \`art.\` (e.g., \`4\`).

**7. Rule for Tables \`<table>...</table>\` (CRITICAL):**
* **Identifier:** The raw MD may contain tables formatted with numerous pipe separators (\`|\`). You must identify and completely discard this pipe-formatted table text.
* **Action:** Instead of using the MD version, find the corresponding, perfectly formatted \`<table>...</table>\` element in the "HTML for Structural and Table Reference".
* **IMPORTANT:** Insert this HTML table element, **completely unchanged**, into the correct position in the final output. Do not attempt to parse or rebuild the table from the MD.

---
### ## Inputs

**1. Raw Markdown (Source of Truth for Text):**
\`{{Markdown}}\`

**2. HTML for Structural and Table Reference ONLY (Do NOT edit this, rebuild from MD):**
\`{{HTML}}\``.replace('{{Markdown}}', input.raw_markdown).replace('{{HTML}}', input.main_text);
    }

    private estimateTokens(markdown: string, html: string): number {
        // Conservative token estimation for input
        const markdownWords = markdown.split(/\s+/).filter(word => word.length > 0).length;
        const htmlWords = html.split(/\s+/).filter(word => word.length > 0).length;
        
        // French/legal text is slightly more complex than average
        const legalComplexity = 1.3;
        
        // Estimate based on both markdown and HTML inputs
        const totalWords = markdownWords + htmlWords;
        const estimatedTokens = Math.ceil(totalWords * 1.5 * legalComplexity);
        
        return estimatedTokens;
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
        
        // Basic structure checks - accept both div and article tags
        if (!transformed.includes('class="legal-article"')) {
            errors.push('Missing legal-article class');
        }
        
        if (!transformed.includes('class="article-number"') && 
            !transformed.includes('Article ' + articleNumber)) {
            errors.push('Missing article number in output');
        }
        
        // Preserve footnotes if they exist
        const originalFootnotes = this.extractFootnoteIds(original);
        const transformedFootnotes = this.extractFootnoteIds(transformed);
        
        const missingFootnotes = originalFootnotes.filter(id => !transformedFootnotes.includes(id));
        if (missingFootnotes.length > 0) {
            errors.push(`Missing footnotes: ${missingFootnotes.join(', ')}`);
        }
        
        return {
            isValid: errors.length === 0,
            errors
        };
    }

    private async processWithGemini(input: TransformationInput, attempt: number = 1): Promise<string> {
        try {
            const prompt = this.buildPrompt(input);
            
            if (attempt > 1) {
                console.log(`   📤 Gemini retry ${attempt} for article ${input.article_number}`);
            }
            
            const model = this.gemini.getGenerativeModel({ model: 'gemini-2.5-flash' });
            const result = await model.generateContent({
                contents: [{
                    role: 'user',
                    parts: [{ text: prompt }]
                }],
                generationConfig: {
                    temperature: 0,
                    topP: 1,
                    maxOutputTokens: 65536, // Conservative limit for safety
                },
            });
            
            const response = result.response.candidates?.[0]?.content?.parts?.[0]?.text || '';
            
            if (!response || response.trim().length === 0) {
                throw new Error('Empty response from Gemini');
            }
            
            // The prompt instructs to return raw HTML only, so we just trim
            let cleanedResponse = response.trim();
            
            // Basic validation
            if (!cleanedResponse.includes('class="legal-article"')) {
                throw new Error('Invalid HTML structure in response - missing legal-article class');
            }
            
            if (attempt > 1) {
                console.log(`   ✅ Received Gemini response (${cleanedResponse.length} chars)`);
            }
            
            return cleanedResponse;
        } catch (error: any) {
            console.error(`⚠️ Gemini attempt ${attempt} failed for article ${input.article_number}:`, error.message);
            
            if (attempt < this.RETRY_ATTEMPTS) {
                const delay = this.RETRY_DELAY * attempt;
                console.log(`⏳ Retrying Gemini in ${delay}ms...`);
                await new Promise(resolve => setTimeout(resolve, delay));
                return this.processWithGemini(input, attempt + 1);
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
            
            // Check token limits
            const estimatedInputTokens = this.estimateTokens(input.raw_markdown, input.main_text);
            const estimatedOutputTokens = this.estimateOutputTokens(estimatedInputTokens);
            
            if (estimatedOutputTokens > this.GEMINI_OUTPUT_TOKEN_LIMIT) {
                // Article output would exceed token limit
                const reason = `Estimated output (${estimatedOutputTokens} tokens) exceeds Gemini limit (${this.GEMINI_OUTPUT_TOKEN_LIMIT} tokens)`;
                console.log(`⚠️ Skipping article ${input.article_number} - ${reason}`);
                
                return {
                    success: false,
                    error: reason
                };
            }
            
            console.log(`🌟 Processing article ${input.article_number} with Gemini 2.5 Flash (est. ${estimatedOutputTokens} output tokens)`);
            const transformedHtml = await this.processWithGemini(input);
            
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
                    validationErrors: validation.errors
                };
            }
            
            return {
                success: true,
                transformedHtml
            };
            
        } catch (error: any) {
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