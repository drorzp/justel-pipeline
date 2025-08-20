import { MongoClient, Db } from 'mongodb';
import { config } from 'dotenv';
import mongoose from 'mongoose';
config();

let client: MongoClient;
let db: Db;

export const connectMongoDB = async () => {
  try {
    const dbName = 'lawyers';
    const uri = process.env.MONGO_URI || `mongodb://lawyer:l123456@localhost:27017/${dbName}?authSource=admin`;
    
    const options = {
          auth: {
            username: 'lawyer',
            password: 'l123456'
          }
        };
    
    client = new MongoClient(uri, options);
    await client.connect();
    db = client.db(dbName);

    // Ensure Mongoose is connected as well for Mongoose models (LawRoot, Article)
    if (mongoose.connection.readyState === 0) {
      await mongoose.connect(uri);
    }
    
    console.info('MongoDB connected successfully');
    console.info('MongoDB URI:', uri);
    console.info('Database:', dbName);
    
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
    console.info('MongoDB connection closed');
  }
  if (mongoose.connection.readyState !== 0) {
    await mongoose.connection.close();
    console.info('Mongoose connection closed');
  }
};