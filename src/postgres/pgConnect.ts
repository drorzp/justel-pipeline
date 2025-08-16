import { Pool, PoolConfig } from 'pg';
import { config } from 'dotenv';

config(); // Load environment variables from .env file

// 🔍 READ-ONLY DATABASE OPTIMIZED CONFIGURATION
const readOnlyPoolConfig: PoolConfig = {
  host: process.env.POSTGRES_HOST || 'localhost',
  port: Number(process.env.POSTGRES_PORT) || 5433,
  user: process.env.POSTGRES_USER,
  password: process.env.POSTGRES_PASSWORD,
  database: process.env.POSTGRES_DB,
  
  // 📚 READ-HEAVY OPTIMIZATIONS
  max: 50,                    // Higher connections for read-only
  idleTimeoutMillis: 60000,   // Longer idle time (reads are frequent)
  connectionTimeoutMillis: 2000, // Fast connection for reads
  
  // 🚀 READ PERFORMANCE TUNING
  keepAlive: true,
  keepAliveInitialDelayMillis: 0, // Immediate keep-alive for reads
  
  // 📖 READ-ONLY SPECIFIC SETTINGS
  allowExitOnIdle: false,
  maxUses: 10000,            // Higher reuse for read queries
  
  // 🔍 QUERY OPTIMIZATIONS
  statement_timeout: 30000,   // Shorter timeout for reads (30s)
  query_timeout: 30000,
  
  // 🏷️ APPLICATION IDENTIFICATION
  application_name: `lawyer_api_readonly_${process.env.NODE_ENV || 'development'}`,
  
  // 🔒 SSL CONFIGURATION
  // ssl: process.env.NODE_ENV === 'production' ? {
  //   rejectUnauthorized: false
  // } : false
  ssl: false
};

// 📊 MULTIPLE READ POOLS FOR LOAD DISTRIBUTION
let primaryReadPool = new Pool(readOnlyPoolConfig);

// Optional: Secondary read pool for heavy analytics queries
const analyticsPoolConfig: PoolConfig = {
  ...readOnlyPoolConfig,
  max: 10,                   // Fewer connections for heavy queries
  statement_timeout: 300000, // Longer timeout for analytics (5 min)
  query_timeout: 300000,
  application_name: `lawyer_api_analytics_${process.env.NODE_ENV || 'development'}`
};

let analyticsPool = new Pool(analyticsPoolConfig);

// 🎯 ENHANCED LOGGING FOR READ-ONLY

// 📈 READ-OPTIMIZED MONITORING
let resetting = false;
const monitorReadPool = (pool: Pool, poolName: string) => {
  pool.on('connect', () => {
    // Connection established to Postgres for this pool
  });

  pool.on('acquire', () => {
    // Client acquired from pool
  });

  pool.on('error', async (err) => {
    console.error(`[pg:${poolName}] Pool error:`, err?.message || err);
    const msg = String(err?.message || '').toLowerCase();
    const fatal = msg.includes('terminat') || msg.includes('server closed the connection') || msg.includes('connection error');
    if (fatal && !resetting) {
      resetting = true;
      try {
        console.warn(`[pg:${poolName}] Fatal error detected. Resetting read pools...`);
        await resetReadPools();
      } catch (e) {
        console.error('[pg] Failed to reset pools:', e);
      } finally {
        resetting = false;
      }
    }
  });
};

monitorReadPool(primaryReadPool, 'Primary');
monitorReadPool(analyticsPool, 'Analytics');

// 🔍 READ-ONLY CONNECTION TESTING
const connectPostgreSQL = async () => {
  try {
    // Test primary read connection
    const primaryClient = await primaryReadPool.connect();
    const primaryResult = await primaryClient.query(`
      SELECT 
        NOW() as server_time, 
        version(),
        current_database(),
        current_user,
        pg_is_in_recovery() as is_replica
    `);
    primaryClient.release();
    
    

    // Test analytics connection
    const analyticsClient = await analyticsPool.connect();
    const analyticsResult = await analyticsClient.query('SELECT NOW() as server_time');
    analyticsClient.release();
    
    

  } catch (error: unknown) {
   
    process.exit(1);
  }
};

// 🔁 Ability to reset read pools (e.g., after .end() was called elsewhere)
const resetReadPools = async () => {
  try {
    // Best-effort end old pools
    await Promise.allSettled([
      primaryReadPool.end(),
      analyticsPool.end(),
    ]);
  } catch {}

  primaryReadPool = new Pool(readOnlyPoolConfig);
  analyticsPool = new Pool(analyticsPoolConfig);

  monitorReadPool(primaryReadPool, 'Primary');
  monitorReadPool(analyticsPool, 'Analytics');
};

// 📊 READ-ONLY POOL STATS
const getPoolStats = () => {
  return {
    primary: {
      totalCount: primaryReadPool.totalCount,
      idleCount: primaryReadPool.idleCount,
      waitingCount: primaryReadPool.waitingCount,
      maxConnections: readOnlyPoolConfig.max,
      purpose: 'fast_reads'
    },
    analytics: {
      totalCount: analyticsPool.totalCount,
      idleCount: analyticsPool.idleCount,
      waitingCount: analyticsPool.waitingCount,
      maxConnections: analyticsPoolConfig.max,
      purpose: 'heavy_analytics'
    },
    readOnly: true,
    timestamp: new Date().toISOString()
  };
};

// 🧹 GRACEFUL SHUTDOWN
const gracefulShutdown = async () => {
  
  try {
    await Promise.all([
      primaryReadPool.end(),
      analyticsPool.end()
    ]);

  } catch (error) {
  
  }
};

process.on('SIGTERM', gracefulShutdown);
process.on('SIGINT', gracefulShutdown);

// 🎯 READ-ONLY DATABASE SERVICE
class ReadOnlyDatabaseService {
  // Fast queries (user lookups, decisions, folders)
  static async query(text: string, params?: any[]) {
    const start = Date.now();
    try {
      const result = await primaryReadPool.query(text, params);
      const duration = Date.now() - start;
    
      
      return result;
    } catch (error) {
      throw error;
    }
  }

  // Heavy analytics queries (reports, aggregations)
  static async analyticsQuery(text: string, params?: any[]) {
    const start = Date.now();
    try {
      const result = await analyticsPool.query(text, params);
      const duration = Date.now() - start;
      
    
      
      return result;
    } catch (error) {
    
      throw error;
    }
  }

  // Query with automatic pool selection
  static async smartQuery(text: string, params?: any[]) {
    const queryUpper = text.trim().toUpperCase();
    
    // Use analytics pool for heavy operations
    if (queryUpper.includes('COUNT(*)') || 
        queryUpper.includes('GROUP BY') || 
        queryUpper.includes('ORDER BY') ||
        queryUpper.includes('AGGREGATE') ||
        text.length > 500) {
      return this.analyticsQuery(text, params);
    }
    
    // Use primary pool for fast queries
    return this.query(text, params);
  }

  // Get a client for manual connection management
  static async getClient() {
    return primaryReadPool.connect();
  }

  // Get analytics client for heavy operations
  static async getAnalyticsClient() {
    return analyticsPool.connect();
  }

  // Long-running client for heavy functions (e.g., 5+ minutes)
  static async getLongClient() {
    // Use analytics pool which is configured with higher timeouts
    return analyticsPool.connect();
  }
}

// 🔍 READ-ONLY QUERY PERFORMANCE MONITORING
const trackQueryPerformance = () => {
  const stats = {
    fastQueries: 0,
    analyticsQueries: 0,
    avgFastQueryTime: 0,
    avgAnalyticsQueryTime: 0,
    lastReset: new Date()
  };
  
  return stats;
};

export { 
  primaryReadPool as pool, // Backward compatibility
  analyticsPool,
  connectPostgreSQL, 
  getPoolStats,
  gracefulShutdown,
  ReadOnlyDatabaseService,
  trackQueryPerformance,
  resetReadPools
};