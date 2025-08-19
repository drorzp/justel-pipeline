import * as fs from 'fs';
import * as path from 'path';
import * as util from 'util';

type LogLevel = 'LOG' | 'ERROR' | 'WARN' | 'INFO' | 'DEBUG';

interface OriginalConsole {
    log: typeof console.log;
    error: typeof console.error;
    warn: typeof console.warn;
    info: typeof console.info;
    debug: typeof console.debug;
}

class FileLogger {
    private logStream: fs.WriteStream;
    private logFile: string;
    private originalConsole: OriginalConsole;
    private logsDir: string;

    constructor(logsDirName: string = 'logs', filePrefix: string = 'pipeline') {
        // Create logs directory if it doesn't exist
        this.logsDir = path.join(process.cwd(), logsDirName);
        if (!fs.existsSync(this.logsDir)) {
            fs.mkdirSync(this.logsDir, { recursive: true });
        }

        // Create log file with timestamp
        const timestamp = new Date().toISOString().split('T')[0];
        this.logFile = path.join(this.logsDir, `${filePrefix}-${timestamp}.log`);
        this.logStream = fs.createWriteStream(this.logFile, { flags: 'a' });

        // Store original console methods
        this.originalConsole = {
            log: console.log.bind(console),
            error: console.error.bind(console),
            warn: console.warn.bind(console),
            info: console.info.bind(console),
            debug: console.debug.bind(console)
        };

        this.setupConsoleOverrides();
        // Announce where logs are written (visible in both console and file)
        console.info('Logger initialized. Writing to:', this.logFile);
        this.setupProcessHandlers();
    }

    private formatMessage(level: LogLevel, args: any[]): string {
        const timestamp = new Date().toISOString();
        const message = util.format(...args);
        
        // Get caller information (optional, can be removed if performance is critical)
        const stack = new Error().stack;
        let caller = 'unknown';
        if (stack) {
            const stackLines = stack.split('\n');
            if (stackLines[3]) {
                const match = stackLines[3].match(/\s+at\s+(.+?)\s+\(/);
                if (match) {
                    caller = match[1];
                }
            }
        }
        
        return `[${timestamp}] [${level}] [${caller}] ${message}\n`;
    }

    private writeLog(level: LogLevel, args: any[]): void {
        const message = this.formatMessage(level, args);
        this.logStream.write(message);
    }

    private setupConsoleOverrides(): void {
        const self = this;

        // Override console.log
        console.log = function(...args: any[]): void {
            self.writeLog('LOG', args);
            self.originalConsole.log(...args);
        };

        // Override console.error
        console.error = function(...args: any[]): void {
            self.writeLog('ERROR', args);
            self.originalConsole.error(...args);
        };

        // Override console.warn
        console.warn = function(...args: any[]): void {
            self.writeLog('WARN', args);
            self.originalConsole.warn(...args);
        };

        // Override console.info
        console.info = function(...args: any[]): void {
            self.writeLog('INFO', args);
            self.originalConsole.info(...args);
        };

        // Override console.debug
        console.debug = function(...args: any[]): void {
            self.writeLog('DEBUG', args);
            self.originalConsole.debug(...args);
        };
    }

    private setupProcessHandlers(): void {
        // Handle process exit - ensure logs are flushed
        process.on('exit', () => {
            this.logStream.end();
        });

        // Handle uncaught exceptions
        process.on('uncaughtException', (err: Error) => {
            console.error('Uncaught Exception:', err);
            this.logStream.end(() => process.exit(1));
        });

        // Handle unhandled promise rejections
        process.on('unhandledRejection', (reason: any, promise: Promise<any>) => {
            console.error('Unhandled Rejection at:', promise, 'reason:', reason);
        });

        // Handle SIGINT (Ctrl+C)
        process.on('SIGINT', () => {
            console.info('Process interrupted (SIGINT)');
            this.close(() => process.exit(0));
        });

        // Handle SIGTERM
        process.on('SIGTERM', () => {
            console.info('Process terminated (SIGTERM)');
            this.close(() => process.exit(0));
        });
    }

    public restoreConsole(): void {
        console.log = this.originalConsole.log;
        console.error = this.originalConsole.error;
        console.warn = this.originalConsole.warn;
        console.info = this.originalConsole.info;
        console.debug = this.originalConsole.debug;
    }

    public close(callback?: () => void): void {
        this.restoreConsole();
        if (callback) {
            this.logStream.end(callback);
        } else {
            this.logStream.end();
        }
    }

    public getLogFile(): string {
        return this.logFile;
    }

    public getLogsDirectory(): string {
        return this.logsDir;
    }

    // Utility method to log objects with pretty printing
    public logObject(label: string, obj: any, level: LogLevel = 'LOG'): void {
        const prettyJson = JSON.stringify(obj, null, 2);
        const message = `${label}:\n${prettyJson}`;
        this.writeLog(level, [message]);
        
        // Also log to original console
        if (level === 'ERROR') {
            this.originalConsole.error(label, obj);
        } else {
            this.originalConsole.log(label, obj);
        }
    }

    // Method to create a scoped logger for specific modules
    public createScopedLogger(scope: string) {
        return {
            log: (...args: any[]) => console.log(`[${scope}]`, ...args),
            error: (...args: any[]) => console.error(`[${scope}]`, ...args),
            warn: (...args: any[]) => console.warn(`[${scope}]`, ...args),
            info: (...args: any[]) => console.info(`[${scope}]`, ...args),
            debug: (...args: any[]) => console.debug(`[${scope}]`, ...args),
        };
    }
}

// Create singleton instance
const logger = new FileLogger();

// Export for use in other modules
export default logger;
export { FileLogger, LogLevel };

/* Usage Examples:

// In your main pipeline script (index.ts):
import logger from './logger';

// The logger is automatically initialized and console methods are overridden
console.log('This will be logged to both console and file');
console.error('Errors are logged too');

// Use scoped logger for specific modules
const dbLogger = logger.createScopedLogger('DATABASE');
dbLogger.log('Connected to database');
dbLogger.error('Connection failed');

// Log objects with pretty printing
logger.logObject('Configuration', { 
    host: 'localhost', 
    port: 3000,
    debug: true 
});

// Get log file path
console.log('Logs are being written to:', logger.getLogFile());

// Restore original console if needed
// logger.restoreConsole();

// Close logger when done
// logger.close();

*/