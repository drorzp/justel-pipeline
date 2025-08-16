class Logger {
  static info(message: string, data: any = {}): void {
    console.log(`[INFO] ${new Date().toISOString()} - ${message}`, data);
  }

  static error(message: string, error: any = {}): void {
    console.error(`[ERROR] ${new Date().toISOString()} - ${message}`, error);
  }

  static success(message: string, data: any = {}): void {
    console.log(`[SUCCESS] ${new Date().toISOString()} - ${message}`, data);
  }

  static warning(message: string, data: any = {}): void {
    console.warn(`[WARNING] ${new Date().toISOString()} - ${message}`, data);
  }
}

export default Logger;
