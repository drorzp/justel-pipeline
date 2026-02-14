import * as fs from 'fs/promises';
import * as path from 'path';
import { compare } from 'fast-json-patch';

export async function filterJSON(): Promise<void> {
  const currentValidDir = path.join(process.cwd(), 'data/step1/current/valid');
  const olderDir = path.join(process.cwd(), 'data/older');
  const readyDir = path.join(process.cwd(), 'data/step1/current/ready');

  // Ensure ready directory exists
  await fs.mkdir(readyDir, { recursive: true });

  const files = await fs.readdir(currentValidDir);
  const jsonFiles = files.filter(f => f.endsWith('.json'));

  let changed = 0;
  let notFound = 0;

  for (const filename of jsonFiles) {
    const currentPath = path.join(currentValidDir, filename);
    const olderPath = path.join(olderDir, filename);

    try {
      await fs.access(olderPath);
    } catch {
      // File not in older, skip
      notFound++;
      continue;
    }

    const currentData = JSON.parse(await fs.readFile(currentPath, 'utf-8'));
    const olderData = JSON.parse(await fs.readFile(olderPath, 'utf-8'));

    const patches = compare(olderData, currentData);

    if (patches.length > 0) {
      await fs.copyFile(currentPath, path.join(readyDir, filename));
      changed++;
    }
  }

  console.log(`filterJSON: ${jsonFiles.length} total, ${changed} changed, ${notFound} not in older`);
}

export async function updateOlderFolder(): Promise<void> {
  const readyDir = path.join(process.cwd(), 'data/step1/current/ready');
  const newValidDir = path.join(process.cwd(), 'data/step1/new/valid');
  const olderDir = path.join(process.cwd(), 'data/older');

  // Ensure older directory exists
  await fs.mkdir(olderDir, { recursive: true });

  let copiedFromReady = 0;
  let copiedFromNew = 0;

  // Copy from current/ready
  try {
    const readyFiles = await fs.readdir(readyDir);
    for (const file of readyFiles.filter(f => f.endsWith('.json'))) {
      await fs.copyFile(
        path.join(readyDir, file),
        path.join(olderDir, file)
      );
      copiedFromReady++;
    }
  } catch {
    // Directory may not exist if no files changed
  }

  // Copy from new/valid
  try {
    const newFiles = await fs.readdir(newValidDir);
    for (const file of newFiles.filter(f => f.endsWith('.json'))) {
      await fs.copyFile(
        path.join(newValidDir, file),
        path.join(olderDir, file)
      );
      copiedFromNew++;
    }
  } catch {
    // Directory may not exist if no new files
  }

  console.log(`updateOlderFolder: ${copiedFromReady} from ready, ${copiedFromNew} from new/valid`);
}
