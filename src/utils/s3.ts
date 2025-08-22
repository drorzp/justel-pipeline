import 'dotenv/config';
import {
  S3Client,
  PutObjectCommand,
  ListObjectsV2Command,
  DeleteObjectsCommand,
  ListObjectsV2CommandOutput,
  _Object,
} from '@aws-sdk/client-s3';

function getS3Client() {
  const region = process.env.AWS_REGION || 'us-east-1';
  return new S3Client({ region });
}

function getBucket(): string {
  const bucket = process.env.S3_BUCKET;
  if (!bucket) throw new Error('S3_BUCKET is not set in environment');
  return bucket;
}

function yymmdd(date = new Date()): string {
  const yy = String(date.getFullYear()).slice(-2);
  const mm = String(date.getMonth() + 1).padStart(2, '0');
  const dd = String(date.getDate()).padStart(2, '0');
  return `${yy}${mm}${dd}`;
}

export async function createS3(): Promise<string> {
  const client = getS3Client();
  const bucket = getBucket();
  const folder = `justel${yymmdd()}`;
  const key = `${folder}/`; // S3 'folder' convention

  await client.send(
    new PutObjectCommand({ Bucket: bucket, Key: key, Body: new Uint8Array(0) })
  );

  return folder;
}

export async function deleteS3(folder: string): Promise<void> {
  const client = getS3Client();
  const bucket = getBucket();
  const prefix = folder.endsWith('/') ? folder : `${folder}/`;

  // List and delete in batches
  let continuationToken: string | undefined = undefined;
  do {
    const listResp: ListObjectsV2CommandOutput = await client.send(
      new ListObjectsV2Command({ Bucket: bucket, Prefix: prefix, ContinuationToken: continuationToken })
    );

    const contents: _Object[] = listResp.Contents || [];
    if (contents.length > 0) {
      const objects = contents.map((o) => ({ Key: o.Key! }));
      await client.send(
        new DeleteObjectsCommand({
          Bucket: bucket,
          Delete: { Objects: objects, Quiet: true },
        })
      );
    }

    continuationToken = listResp.IsTruncated ? listResp.NextContinuationToken : undefined;
  } while (continuationToken);
}

export async function clearS3ZipFiles(folders: string[]): Promise<void> {
  const client = getS3Client();
  const bucket = getBucket();
  
  console.log(`🗑️  Clearing ZIP files from S3 folders: ${folders.join(', ')}`);
  
  for (const folder of folders) {
    const prefix = folder.endsWith('/') ? folder : `${folder}/`;
    let totalDeleted = 0;
    let continuationToken: string | undefined = undefined;
    
    do {
      const listResp: ListObjectsV2CommandOutput = await client.send(
        new ListObjectsV2Command({ 
          Bucket: bucket, 
          Prefix: prefix, 
          ContinuationToken: continuationToken,
          MaxKeys: 1000 
        })
      );

      const contents: _Object[] = listResp.Contents || [];
      const zipFiles = contents.filter(obj => obj.Key?.endsWith('.zip'));
      
      if (zipFiles.length > 0) {
        const objects = zipFiles.map((o) => ({ Key: o.Key! }));
        await client.send(
          new DeleteObjectsCommand({
            Bucket: bucket,
            Delete: { Objects: objects, Quiet: true },
          })
        );
        totalDeleted += zipFiles.length;
      }

      continuationToken = listResp.IsTruncated ? listResp.NextContinuationToken : undefined;
    } while (continuationToken);
    
    console.log(`   ✅ Deleted ${totalDeleted} ZIP files from ${prefix}`);
  }
}
