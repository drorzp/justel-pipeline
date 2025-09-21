import crypto from 'crypto';
import { QdrantClient } from '@qdrant/js-client-rest';
import OpenAI from 'openai';
import { v5 as uuidv5 } from 'uuid';
import { splitByTokens, countTokens } from './token-utils'; // <-- NEW

const COLLECTION = 'articles_of_law_3072';
const QDRANT_NS = '16bec6a2-38b3-461c-a364-c41330234c48';
const qdrant = new QdrantClient({ url: 'http://localhost:6333' });
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY! });

// Safety thresholds (embedding model has 8192 token limit)
const HARD_MODEL_LIMIT = 8192;
const SAFE_MAX_TOKENS = 8000; // never send more than this
const CHUNK_MAX_TOKENS = 7000; // target size per chunk (gives headroom)
const CHUNK_OVERLAP_TOKENS = 200;

function chunkPointId(articleId: number | string, chunkIndex: number, fullTextHash: string) {
  const name = `${articleId}:${chunkIndex}:${fullTextHash.slice(0, 8)}`;
  return uuidv5(name, QDRANT_NS);
}

function md5(s: string) {
  return crypto.createHash('md5').update(s, 'utf-8').digest('hex');
}

async function getEmbeddingsBatch(texts: string[]) {
  // Final defensive check: nothing above SAFE_MAX_TOKENS
  const overs = texts.find(t => countTokens(t) > SAFE_MAX_TOKENS);
  if (overs) {
    throw new Error(
      `Invariant violated: a chunk has ${countTokens(overs)} tokens (> ${SAFE_MAX_TOKENS}).`
    );
  }

  const res = await openai.embeddings.create({
    model: 'text-embedding-3-large',
    input: texts,
    dimensions: 3072, // you’re using 3072-dim collection
  });
  return res.data.map(d => d.embedding);
}

/**
 * Scroll to find any existing chunk for this article_id,
 * then read its full_text_hash to compare.
 */
async function getExistingFullHash(articleId: number | string): Promise<string | null> {
  const filter = { must: [{ key: 'article_id', match: { value: articleId } }] };

  const { points } = await qdrant.scroll(COLLECTION, {
    filter,
    with_payload: true,
    limit: 1,
  });

  if (!points || points.length === 0) return null;
  const pld = points[0].payload as any;
  return (pld?.full_text_hash as string) ?? null;
}

async function deleteExistingChunks(articleId: number | string) {
  const filter = { must: [{ key: 'article_id', match: { value: articleId } }] };
  await qdrant.delete(COLLECTION, { filter });
}

/**
 * Smart upsert with token-safe chunking:
 * - Skip if unchanged (based on full_text_hash)
 * - Otherwise delete old chunks and reindex chunked embeddings
 * - Guarantees no chunk exceeds model token window
 */
export async function smartUpsert(
  id: number,
  newText: string,
  document_number: string,
  article_number: string,
  effective_date: Date | null
) {
  try {
    if (id === null || id === undefined || Number.isNaN(id)) {
      throw new Error('Invalid point id');
    }
    if (!newText || typeof newText !== 'string') {
      throw new Error('Invalid text');
    }

    const fullTextHash = md5(newText);

    // Skip if unchanged
    const existingFullHash = await getExistingFullHash(id);
    if (existingFullHash && existingFullHash === fullTextHash) {
      console.log(`Skipping ${id} - full text unchanged`);
      return { updated: false, id, chunks: 0, reason: 'unchanged' };
    }

    // Token-safe chunking
    const chunks = splitByTokens(newText, {
      maxTokens: CHUNK_MAX_TOKENS,
      overlapTokens: CHUNK_OVERLAP_TOKENS,
    });

    // Final safety: re-slice any outliers (shouldn’t exist)
    const safeChunks = chunks.flatMap(c =>
      countTokens(c) <= SAFE_MAX_TOKENS
        ? [c]
        : splitByTokens(c, { maxTokens: CHUNK_MAX_TOKENS, overlapTokens: CHUNK_OVERLAP_TOKENS })
    );

    // Clean up old chunks if changed
    if (existingFullHash) {
      await deleteExistingChunks(id);
    }

    // Embed in batches
    const BATCH = 64;
    const vectors: number[][] = [];
    for (let i = 0; i < safeChunks.length; i += BATCH) {
      const batch = safeChunks.slice(i, i + BATCH);

      // Additional defensive assertion (paranoia)
      for (const b of batch) {
        const tks = countTokens(b);
        if (tks > HARD_MODEL_LIMIT) {
          throw new Error(`Refusing to embed a ${tks}-token chunk (> ${HARD_MODEL_LIMIT}).`);
        }
      }

      const embs = await getEmbeddingsBatch(batch);
      vectors.push(...embs);
    }

    // Prepare points
    const nowIso = new Date().toISOString();
    const total = safeChunks.length;
    const points = safeChunks.map((chunk, i) => ({
      id: chunkPointId(id, i, fullTextHash),
      vector: vectors[i],
      payload: {
        article_id: id,
        effective_date: effective_date ? effective_date.toString() : null,
        document_number,
        article_number,
        chunk_index: i,
        total_chunks: total,
        text: chunk,
        chunk_hash: md5(chunk),
        full_text_hash: fullTextHash,
        updated_at: nowIso,
      },
    }));

    // Upsert all chunks
    await qdrant.upsert(COLLECTION, { points });

    console.log(`Updated article ${id} with ${total} chunk(s)`);
    return { updated: true, id, chunks: total };

  } catch (error) {
    console.error(`Error upserting ${id}:`, error);
    throw error;
  }
}
