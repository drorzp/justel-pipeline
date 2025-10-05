import 'dotenv/config';
import { AzureOpenAI } from 'openai';
import { generateNewTitle, LLMConfig } from './llm_title';

async function testAzureTitleGeneration() {
    console.log('🧪 Testing Azure OpenAI Title Generation...\n');

    const config: LLMConfig = {
        azureEndpoint: process.env.AZURE_OPENAI_ENDPOINT || '',
        azureApiKey: process.env.AZURE_OPENAI_API_KEY || '',
        azureApiVersion: process.env.AZURE_API_VERSION || '2024-10-01-preview',
        model: 'gpt-4o',
        maxRetries: 2,
        retryDelay: 200,
        requestDelay: 0,
        concurrentRequests: 1,
        batchSize: 1,
    };

    // Verify config
    console.log('Configuration:');
    console.log(`  Endpoint: ${config.azureEndpoint}`);
    console.log(`  API Version: ${config.azureApiVersion}`);
    console.log(`  Model: ${config.model}`);
    console.log(`  API Key: ${config.azureApiKey ? '***' + config.azureApiKey.slice(-4) : 'NOT SET'}\n`);

    const azureOpenAI = new AzureOpenAI({
        apiKey: config.azureApiKey,
        endpoint: config.azureEndpoint,
        apiVersion: config.azureApiVersion,
        defaultQuery: { 'api-version': config.azureApiVersion },
        defaultHeaders: { 'api-key': config.azureApiKey }
    });

    // Test case: A verbose Belgian legal title
    const testTitle = '21 MARS 1804. - [ANCIEN] CODE CIVIL. - LIVRE III : Manières dont on acquiert la propriété. - TITRE I et II (art. 711-1100) (NOTE: consultation des versions antérieures à partir du 01-01-1990 et mise à jour au 14-01-2009)';
    const testDocNumber = 'TEST-2024-001';

    try {
        console.log('📝 Original Title:');
        console.log(`  "${testTitle}"\n`);

        console.log('⏳ Generating new title with Azure OpenAI...\n');

        const startTime = Date.now();
        const newTitle = await generateNewTitle(azureOpenAI, config, testTitle, testDocNumber);
        const duration = Date.now() - startTime;

        console.log('✅ Success!');
        console.log(`  New Title: "${newTitle}"`);
        console.log(`  Length: ${newTitle.length} characters`);
        console.log(`  Duration: ${duration}ms\n`);

        console.log('🎉 Azure OpenAI connection is working correctly!');

    } catch (error: any) {
        console.error('❌ Test Failed!');
        console.error(`  Error: ${error.message}`);
        if (error.code) {
            console.error(`  Code: ${error.code}`);
        }
        if (error.status) {
            console.error(`  Status: ${error.status}`);
        }
        process.exit(1);
    }
}

testAzureTitleGeneration();
