import * as fs from 'fs/promises';
import * as path from 'path';
import { compare } from 'fast-json-patch';
import pLimit from 'p-limit';

// Fields to ignore when comparing (timestamps that change every run)
const IGNORE_FIELDS = ['extraction_date', 'generation_timestamp'];

function stripTimestamps(obj: any): any {
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }

  if (Array.isArray(obj)) {
    return obj.map(stripTimestamps);
  }

  const result: any = {};
  for (const key of Object.keys(obj)) {
    if (!IGNORE_FIELDS.includes(key)) {
      result[key] = stripTimestamps(obj[key]);
    }
  }
  return result;
}

interface CompareStats {
  totalInCurrent: number;
  foundInOlder: number;
  notFoundInOlder: number;
  same: number;
  different: number;
}

interface PatchWithOldValue {
  op: string;
  path: string;
  value?: any;
  oldValue?: any;
}

interface CompareResult {
  found: boolean;
  same: boolean;
  filename: string;
  patches?: PatchWithOldValue[];
}

async function compareFile(
  filename: string,
  currentValidDir: string,
  olderDir: string
): Promise<CompareResult> {
  const currentPath = path.join(currentValidDir, filename);
  const olderPath = path.join(olderDir, filename);

  try {
    await fs.access(olderPath);
  } catch {
    return { found: false, same: false, filename };
  }

  const [currentData, olderData] = await Promise.all([
    fs.readFile(currentPath, 'utf-8').then(JSON.parse),
    fs.readFile(olderPath, 'utf-8').then(JSON.parse),
  ]);

  // Strip timestamps before comparing to ignore false positives
  const currentStripped = stripTimestamps(currentData);
  const olderStripped = stripTimestamps(olderData);

  const patches = compare(olderStripped, currentStripped);

  if (patches.length === 0) {
    return { found: true, same: true, filename };
  }

  // Add old values to patches for better readability
  const patchesWithOldValues: PatchWithOldValue[] = patches.map(patch => {
    const result: PatchWithOldValue = { ...patch };

    if (patch.op === 'replace' || patch.op === 'remove') {
      // Get old value from olderStripped using the path
      const pathParts = patch.path.split('/').filter(p => p !== '');
      let oldValue: any = olderStripped;
      for (const part of pathParts) {
        if (oldValue && typeof oldValue === 'object') {
          oldValue = oldValue[part];
        } else {
          oldValue = undefined;
          break;
        }
      }
      result.oldValue = oldValue;
    }

    return result;
  });

  return { found: true, same: false, filename, patches: patchesWithOldValues };
}

async function compareCurrentWithOlder(): Promise<void> {
  const currentValidDir = path.join(process.cwd(), 'data/step1/current/valid');
  const olderDir = path.join(process.cwd(), 'data/older');

  console.log('Starting comparison between current/valid and older...\n');

  const files = await fs.readdir(currentValidDir);
  const jsonFiles = files.filter(f => f.endsWith('.json'));

  console.log(`Found ${jsonFiles.length} JSON files in current/valid\n`);

  const limit = pLimit(50);

  const results = await Promise.all(
    jsonFiles.map(file => limit(() => compareFile(file, currentValidDir, olderDir)))
  );

  const stats: CompareStats = {
    totalInCurrent: jsonFiles.length,
    foundInOlder: 0,
    notFoundInOlder: 0,
    same: 0,
    different: 0,
  };

  const differentFiles: CompareResult[] = [];

  for (const result of results) {
    if (result.found) {
      stats.foundInOlder++;
      if (result.same) {
        stats.same++;
      } else {
        stats.different++;
        differentFiles.push(result);
      }
    } else {
      stats.notFoundInOlder++;
    }
  }

  // Log differences
  if (differentFiles.length > 0) {
    console.log('='.repeat(80));
    console.log('FILES WITH DIFFERENCES:');
    console.log('='.repeat(80));

    for (const file of differentFiles) {
      console.log(`\n--- ${file.filename} ---`);
      console.log(`Changes (${file.patches?.length || 0}):\n`);

      for (const patch of file.patches || []) {
        console.log(`  [${patch.op.toUpperCase()}] ${patch.path}`);
        if (patch.oldValue !== undefined) {
          console.log(`    OLD: ${JSON.stringify(patch.oldValue)}`);
        }
        if (patch.value !== undefined) {
          console.log(`    NEW: ${JSON.stringify(patch.value)}`);
        }
        console.log('');
      }
    }
    console.log('='.repeat(80));
  }

  // Print summary
  console.log('\n');
  console.log('='.repeat(50));
  console.log('COMPARISON SUMMARY');
  console.log('='.repeat(50));
  console.log(`Total files in current/valid:  ${stats.totalInCurrent}`);
  console.log(`Found in older:                ${stats.foundInOlder}`);
  console.log(`Not found in older (new):      ${stats.notFoundInOlder}`);
  console.log(`Same (no changes):             ${stats.same}`);
  console.log(`Different (has changes):       ${stats.different}`);
  console.log('='.repeat(50));
}

async function main() {
  try {
    await compareCurrentWithOlder();
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : 'Unknown error';
    console.error('Error running comparison:', message);
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}
