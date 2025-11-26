import * as dotenv from 'dotenv';
import { GoogleGenerativeAI } from '@google/generative-ai';
import { AzureOpenAI } from 'openai';
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
    private gemini: GoogleGenerativeAI | null = null;
    private azureOpenAI: AzureOpenAI | null = null;
    private readonly RETRY_ATTEMPTS = 2;
    private readonly RETRY_DELAY = 10;
    private readonly GPT4O_OUTPUT_TOKEN_LIMIT = 16000; // 16K token limit for GPT-4o
    private readonly GEMINI_OUTPUT_TOKEN_LIMIT = 55000; // 55K token limit for Gemini
    private readonly AZURE_MODEL_NAME = 'gpt-4o'; // Azure expects the base model name, not deployment name

    constructor() {
        let modelsAvailable = 0;

        // Initialize Gemini
        const googleApiKey = process.env.GOOGLE_API_KEY || process.env.GEMINI_API_KEY;
        if (googleApiKey) {
            this.gemini = new GoogleGenerativeAI(googleApiKey);
            console.log('✅ Gemini 2.5 Flash initialized');
            modelsAvailable++;
        } else {
            console.log('⚠️ Gemini not configured');
        }

        // Initialize Azure OpenAI
        const azureEndpoint = process.env.AZURE_OPENAI_ENDPOINT;
        const azureApiKey = process.env.AZURE_OPENAI_API_KEY;
        const azureApiVersion = process.env.AZURE_API_VERSION || '2024-10-01-preview';

        if (azureEndpoint && azureApiKey) {
            this.azureOpenAI = new AzureOpenAI({
                apiKey: azureApiKey,
                endpoint: azureEndpoint,
                apiVersion: azureApiVersion,
                defaultQuery: { 'api-version': azureApiVersion },
                defaultHeaders: { 'api-key': azureApiKey }
            });
            console.log(`✅ Azure OpenAI initialized (API version: ${azureApiVersion})`);
            modelsAvailable++;
        } else {
            console.log('⚠️ Azure OpenAI not configured');
        }

        // Ensure at least one model is configured
        if (modelsAvailable === 0) {
            throw new Error('No AI models configured. Please configure either Azure OpenAI or Gemini in your .env file.');
        }
    }

    private buildGPT4oPrompt(input: TransformationInput): string {
        // Exact prompt from batch processing script for OpenAI
        return `You are an expert legal document parser. Your task is to convert the provided raw Markdown (MD) text of a Belgian law article into a single, clean, and perfectly structured HTML document.

**Primary Directive:** The raw MD is the absolute source of truth for all text content. The final HTML must accurately represent all content and structure from the MD, while correctly incorporating pre-formatted tables from the reference HTML.

**Output Format:** Your response MUST be ONLY the raw HTML code. Start your response directly with <article and end with </article>. DO NOT wrap your response in markdown code blocks. DO NOT include \`\`\`html at the beginning or \`\`\` at the end. DO NOT add any text before or after the HTML. Output ONLY pure HTML.

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
\`${input.raw_markdown}\`

**2. HTML for Structural and Table Reference ONLY (Do NOT edit this, rebuild from MD):**
\`${input.main_text}\``;
    }

    private buildGeminiPrompt(input: TransformationInput): string {
        // Original Gemini prompt format
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

    private shouldTransform(mainText: string, rawMarkdown: string): boolean {
        // Check if the HTML contains any of the required patterns
        const hasFootnoteRef = mainText.includes('<span class="footnote-ref"');
        const hasSectionSymbol = mainText.includes('§');
        const hasProvisionList = mainText.includes('<li class="provision"');

        // Check if raw markdown contains "° et " pattern (like "1° et ", "2° et ", etc.)
        const hasDegreeEtPattern = rawMarkdown.includes('° et ');

        // Transform if it has the degree pattern OR any of the HTML patterns
        return hasDegreeEtPattern || hasFootnoteRef || hasSectionSymbol || hasProvisionList;
    }

    private isModelRefusal(response: string): boolean {
        const trimmed = response.trim();

        // Must start with < (any refusal is plain text)
        if (!trimmed.startsWith('<')) return true;

        // Must start with expected root tags
        if (!trimmed.startsWith('<article') && !trimmed.startsWith('<div')) {
            return true;
        }

        // Must contain the required class
        if (!trimmed.includes('class="legal-article"')) return true;

        return false;
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
            !transformed.includes('Article ' + articleNumber) &&
            !transformed.includes('id="article-' + articleNumber + '"')) {
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

    private async processWithGPT4o(input: TransformationInput, attempt: number = 1): Promise<string> {
        if (!this.azureOpenAI) {
            throw new Error('Azure OpenAI client not initialized');
        }

        try {
            const prompt = this.buildGPT4oPrompt(input);

            if (attempt > 1) {
                console.log(`   📤 Azure GPT-4o retry ${attempt} for article ${input.article_number}`);
            }

            const completion = await this.azureOpenAI.chat.completions.create({
                model: this.AZURE_MODEL_NAME, // Azure expects "gpt-4o" not deployment name
                messages: [
                    {
                        role: 'user',
                        content: prompt
                    }
                ],
                temperature: 0,
                top_p: 1,
                max_tokens: this.GPT4O_OUTPUT_TOKEN_LIMIT
            });

            const response = completion.choices[0]?.message?.content || '';

            if (!response || response.trim().length === 0) {
                throw new Error('Empty response from Azure GPT-4o');
            }

            // Clean response - GPT-4o might still include code blocks despite instructions
            let cleanedResponse = response.trim();
            if (cleanedResponse.startsWith('```html')) {
                cleanedResponse = cleanedResponse.substring(7);
            }
            if (cleanedResponse.endsWith('```')) {
                cleanedResponse = cleanedResponse.substring(0, cleanedResponse.length - 3);
            }
            cleanedResponse = cleanedResponse.trim();

            // Check for model refusal
            if (this.isModelRefusal(cleanedResponse)) {
                throw new Error('Model returned refusal or invalid response instead of HTML');
            }

            if (attempt > 1) {
                console.log(`   ✅ Received Azure GPT-4o response (${cleanedResponse.length} chars)`);
            }

            return cleanedResponse;
        } catch (error: any) {
            console.error(`⚠️ Azure GPT-4o attempt ${attempt} failed for article ${input.article_number}:`, error.message);

            if (attempt < this.RETRY_ATTEMPTS) {
                const delay = this.RETRY_DELAY * attempt;
                console.log(`⏳ Retrying Azure GPT-4o in ${delay}ms...`);
                await new Promise(resolve => setTimeout(resolve, delay));
                return this.processWithGPT4o(input, attempt + 1);
            }

            throw error;
        }
    }

    private async processWithGemini(input: TransformationInput, attempt: number = 1): Promise<string> {
        if (!this.gemini) {
            throw new Error('Gemini client not initialized');
        }

        try {
            const prompt = this.buildGeminiPrompt(input);
            
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

            // Check for model refusal
            if (this.isModelRefusal(cleanedResponse)) {
                throw new Error('Model returned refusal or invalid response instead of HTML');
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
            if (!this.shouldTransform(input.main_text, input.raw_markdown)) {
                console.log(`⏭️ Skipping transformation for article ${input.article_number} - no relevant patterns found`);
                return {
                    success: true,
                    skipped: true,
                    skipReason: 'No "° et " pattern in markdown and no footnotes, section symbols, or provision lists found in content'
                };
            }
            
            // Estimate tokens for model selection
            const estimatedInputTokens = this.estimateTokens(input.raw_markdown, input.main_text);
            const estimatedOutputTokens = this.estimateOutputTokens(estimatedInputTokens);

            // Model selection based on estimated output tokens
            let transformedHtml: string;
            let modelUsed: string;

            if (estimatedOutputTokens < this.GPT4O_OUTPUT_TOKEN_LIMIT && this.azureOpenAI) {
                // Use Azure GPT-4o for smaller articles
                modelUsed = 'Azure GPT-4o';
                console.log(`🤖 Processing article ${input.article_number} with ${modelUsed} (est. ${estimatedOutputTokens} output tokens)`);
                transformedHtml = await this.processWithGPT4o(input);

            } else if (estimatedOutputTokens < this.GEMINI_OUTPUT_TOKEN_LIMIT && this.gemini) {
                // Use Gemini for larger articles
                modelUsed = 'Gemini 2.5 Flash';
                console.log(`🌟 Processing article ${input.article_number} with ${modelUsed} (est. ${estimatedOutputTokens} output tokens)`);
                transformedHtml = await this.processWithGemini(input);

            } else {
                // Article too large for any model
                const reason = `Estimated output (${estimatedOutputTokens} tokens) exceeds all model limits`;
                console.log(`⚠️ Skipping article ${input.article_number} - ${reason}`);

                return {
                    success: false,
                    error: reason
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
                    validationErrors: validation.errors
                };
            }
            
            console.log(`✅ Successfully transformed with ${modelUsed}`);

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