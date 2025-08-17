import crypto from 'crypto';
import { QdrantClient } from '@qdrant/js-client-rest';

const qdrant = new QdrantClient({ url: 'http://localhost:6333' });
function hashText(text: string) {
  return crypto.createHash('md5').update(text).digest('hex');
}
// Narrow type for payload fields we use
interface TextPayload {
  text: string;
  text_hash?: string;
  [key: string]: unknown;
}
export async function batchAddHashToPayloads(collectionName:string) {
    try {
      let offset = null;
      let totalUpdated = 0;
      const batchSize = 100;

      while (true) {
        // Scroll through points
        const scrollResult = await qdrant.scroll(collectionName, {
          limit: batchSize,
          offset,
          with_payload: true,
          with_vector: false,
        });

        if (scrollResult.points.length === 0) break;

        // Filter points that need updating
        const pointsToUpdate = scrollResult.points.filter(point => {
          const payload = point.payload as Partial<TextPayload> | undefined;
          return typeof payload?.text === 'string' && !payload?.text_hash;
        });

        if (pointsToUpdate.length > 0) {
          // Apply per-point payload merges using setPayload
          await Promise.all(
            pointsToUpdate.map(async point => {
              const payload = point.payload as TextPayload; // safe due to filter above
              return qdrant.setPayload(collectionName, {
                points: [point.id],
                payload: {
                  text_hash: hashText(payload.text),
                  hash_added_at: new Date().toISOString(),
                },
              });
            })
          );

          totalUpdated += pointsToUpdate.length;
          console.log(`Updated batch: ${pointsToUpdate.length} points (Total: ${totalUpdated})`);
        }

        offset = scrollResult.next_page_offset;
        if (!offset) break;
      }

      console.log(`✅ Completed! Total points updated: ${totalUpdated}`);
      return totalUpdated;
      
    } catch (error) {
      console.error('Error in batch update:', error);
      throw error;
    }
  }

// Allow running this file directly: `ts-node src/add-to-vector/qdrant.ts <collectionName>`
if (require.main === module) {
  (async () => {
    const collectionName = process.argv[2];
    if (!collectionName) {
      console.error('Usage: ts-node src/add-to-vector/qdrant.ts <collectionName>');
      process.exit(1);
    }
    try {
      const updated = await batchAddHashToPayloads(collectionName);
      console.log(`Done. Updated ${updated} points in collection "${collectionName}".`);
      process.exit(0);
    } catch (e) {
      process.exit(1);
    }
  })();
}