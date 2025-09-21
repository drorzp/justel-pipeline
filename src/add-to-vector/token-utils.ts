// token-utils.ts
import { get_encoding } from '@dqbd/tiktoken';

const enc = get_encoding('cl100k_base');

// Normalizes tiktoken decode output across versions/typings.
function decodeToString(tokens: Uint32Array): string {
  const out = enc.decode(tokens as any) as unknown;
  return typeof out === 'string'
    ? out
    : new TextDecoder().decode(out as Uint8Array);
}

export function countTokens(text: string): number {
  return enc.encode(text).length;
}

export function sliceTokens(
  text: string,
  maxTokens: number,
  overlapTokens = 0
): string[] {
  const toks: Uint32Array = enc.encode(text);
  const res: string[] = [];
  let i = 0;

  const safeOverlap = Math.min(overlapTokens, Math.max(0, Math.floor(maxTokens / 4)));

  while (i < toks.length) {
    const end = Math.min(i + maxTokens, toks.length);
    const sub: Uint32Array = toks.subarray(i, end);
    const seg = decodeToString(sub);              // ← use helper
    res.push(seg);
    if (end === toks.length) break;

    i = end - safeOverlap;
    if (i < 0) i = 0;
  }
  return res;
}

export function splitByTokens(
  text: string,
  {
    maxTokens = 7000,
    overlapTokens = 200,
  }: { maxTokens?: number; overlapTokens?: number } = {}
): string[] {
  const normalize = text.replace(/\r\n/g, '\n').trim();
  let paras = normalize.split(/\n{2,}/).map(s => s.trim()).filter(Boolean);
  if (paras.length === 0) paras = [normalize];

  const chunks: string[] = [];
  let buffer = '';

  const flushBuffer = () => {
    if (!buffer) return;

    if (countTokens(buffer) <= maxTokens) {
      chunks.push(buffer);
      buffer = '';
      return;
    }

    const sentences = buffer.split(/(?<=[\.!?])\s+/);
    if (sentences.length > 1) {
      let cur = '';
      for (const s of sentences) {
        const candidate = cur ? `${cur} ${s}` : s;
        if (countTokens(candidate) > maxTokens) {
          if (cur) chunks.push(cur);

          // overlap from previous cur
          let overlap = '';
          if (overlapTokens > 0 && cur) {
            const toks: Uint32Array = enc.encode(cur);
            const start = Math.max(0, toks.length - overlapTokens);
            const sub: Uint32Array = toks.subarray(start);
            overlap = decodeToString(sub);        // ← use helper
          }
          cur = overlap ? `${overlap} ${s}` : s;

          if (countTokens(cur) > maxTokens) {
            chunks.push(...sliceTokens(cur, maxTokens, overlapTokens));
            cur = '';
          }
        } else {
          cur = candidate;
        }
      }
      if (cur) chunks.push(cur);
      buffer = '';
      return;
    }

    chunks.push(...sliceTokens(buffer, maxTokens, overlapTokens));
    buffer = '';
  };

  for (const p of paras) {
    const candidate = buffer ? `${buffer}\n\n${p}` : p;
    if (countTokens(candidate) > maxTokens) {
      flushBuffer();
      buffer = p;
      if (countTokens(buffer) > maxTokens) {
        flushBuffer();
      }
    } else {
      buffer = candidate;
    }
  }
  flushBuffer();

  return chunks.flatMap(c =>
    countTokens(c) <= maxTokens ? [c] : sliceTokens(c, maxTokens, overlapTokens)
  );
}
