// services/qdrantSearch.service.ts
import { QdrantClient } from '@qdrant/js-client-rest';
import OpenAI from 'openai';
import logger from '../utils/logger';
import { getErrorMessage } from '../utils/helper';

// Minimal type for Qdrant scored point results we care about
type QdrantScoredPoint<TPayload> = {
  payload?: TPayload;
  score: number;
};

export interface SearchResultArticle {
  rank: number;
  articleId: number;
  score: number;
  text: string;
  preview: string;
}


interface QdrantPayloadArticle {
  article_id: number;
  text: string;
}


// Initialize clients once
const qdrantClient = new QdrantClient({
  host: process.env.QDRANT_HOST || 'localhost',
  port: parseInt(process.env.QDRANT_PORT || '6333', 10),
});

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY as string,
});


// Add a new article to Qdrant 'articles_of_law' collection
export const addArticleToQdrant = async (id: number, text: string): Promise<void> => {
  try {
    // Create embedding for the article text (same settings as searchArticles)
    const embeddingResponse = await openai.embeddings.create({
      model: 'text-embedding-3-small',
      input: text,
      dimensions: 512,
    });

    const vector = embeddingResponse.data[0].embedding;

    // Upsert the point into Qdrant
    await qdrantClient.upsert('articles_of_law', {
      wait: true,
      points: [
        {
          id: id,
          vector: vector,
          payload: {
            text: text.slice(0, 1000),
            article_id: id,
          },
        },
      ],
    });

    logger.success('Upserted article to Qdrant', { id });
  } catch (error: unknown) {
    const message = getErrorMessage(error);
    logger.error('Failed to upsert article to Qdrant', { id, message });
    throw new Error(`Upsert failed: ${message}`);
  }
};

// Named exports are provided above; no default export is necessary.