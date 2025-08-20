

import crypto from 'crypto';
import { QdrantClient } from '@qdrant/js-client-rest';
import OpenAI from 'openai';

const qdrant = new QdrantClient({ url: 'http://localhost:6333' });
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

function hashText(text: string) {
  return crypto.createHash('md5').update(text, 'utf-8').digest('hex');
}

// Helper to get embeddings
async function getEmbedding(text: string) {
  const response = await openai.embeddings.create({
    model: 'text-embedding-3-small',
    input: text,
    dimensions: 512
  });
  return response.data[0].embedding;
}

// Smart upsert that checks for changes
export async function smartUpsert(id: number, newText: string, document_number: string, article_number: string) {
  try {
    if (id === null || id === undefined || Number.isNaN(id)) {
      throw new Error('Invalid point id');
    }
    if (!newText || typeof newText !== 'string') {
      throw new Error('Invalid text');
    }

    // Try to retrieve existing point
    const existingPoints = await qdrant.retrieve('articles_of_law', {
      ids: [id],
      with_payload: true,
    });

    if (existingPoints.length > 0) {
      const existingHash = existingPoints[0].payload?.text_hash;
      const newHash = hashText(newText);

      // Skip if text hasn't changed
      if (existingHash === newHash) {
        console.log(`Skipping ${id} - text unchanged`);
        return { updated: false, id };
      }
    }

    // Text is new or changed - get embedding and upsert
    const vector = await getEmbedding(newText);
    
    await qdrant.upsert('articles_of_law', {
      points: [
        {
          id,
          vector,
          payload: {
            text: newText,
            article_id: id,
            document_number: document_number,
            article_number: article_number,
            text_hash: hashText(newText),
            updated_at: new Date().toISOString(),
          },
        },
      ],
    });

    console.log(`Updated ${id}`);
    return { updated: true, id };
    
  } catch (error) {
    console.error(`Error upserting ${id}:`, error);
    throw error;
  }
}