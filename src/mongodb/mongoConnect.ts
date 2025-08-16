import { MongoClient, Db } from 'mongodb';
import { config } from 'dotenv';
config();

let client: MongoClient;
let db: Db;

export const connectMongoDB = async () => {
  try {
    const uri = 'mongodb://lawyer:l123456@localhost:27017/?authSource=admin';
    const dbName = 'lawyers';
    
    const options = {
          auth: {
            username: 'lawyer',
            password: 'l123456'
          }
        };
    
    client = new MongoClient(uri, options);
    await client.connect();
    db = client.db(dbName);
    
    console.log('MongoDB connected successfully');
    console.log('MongoDB URI:', uri);
    console.log('Database:', dbName);
    
    return db;
  } catch (error) {
    console.error('MongoDB connection error:', error);
    process.exit(1);
  }
};

export const getDB = () => {
  if (!db) {
    throw new Error('Database not initialized. Call connectMongoDB first.');
  }
  return db;
};

export const closeMongoDB = async () => {
  if (client) {
    await client.close();
    console.log('MongoDB connection closed');
  }
};