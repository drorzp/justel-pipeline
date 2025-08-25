import { spawn } from 'child_process';
import * as path from 'path';

interface PythonScriptOptions {
  args?: string[];
  cwd?: string;
  env?: NodeJS.ProcessEnv;
  showOutput?: boolean;
}

export async function runPythonScript(
  scriptPath: string,
  options: PythonScriptOptions = {}
): Promise<{ stdout: string; stderr: string; exitCode: number }> {
  return new Promise((resolve, reject) => {
    const { args = [], cwd, env = process.env, showOutput = true } = options;
    
    // Resolve the full path to the Python script
    const fullScriptPath = path.resolve(scriptPath);
    
    console.log(`🐍 Running Python script: ${path.basename(fullScriptPath)}`);
    if (args.length > 0) {
      console.log(`   Arguments: ${args.join(' ')}`);
    }
    
    // Spawn the Python process
    const pythonProcess = spawn('python3', [fullScriptPath, ...args], {
      cwd: cwd || path.dirname(fullScriptPath),
      env,
    });
    
    let stdout = '';
    let stderr = '';
    
    // Collect stdout data
    pythonProcess.stdout.on('data', (data) => {
      const output = data.toString();
      stdout += output;
      if (showOutput) {
        process.stdout.write(output);
      }
    });
    
    // Collect stderr data
    pythonProcess.stderr.on('data', (data) => {
      const output = data.toString();
      stderr += output;
      if (showOutput) {
        process.stderr.write(output);
      }
    });
    
    // Handle process exit
    pythonProcess.on('close', (code) => {
      const exitCode = code || 0;
      
      if (exitCode === 0) {
        console.log(`✅ Python script completed successfully: ${path.basename(fullScriptPath)}`);
        resolve({ stdout, stderr, exitCode });
      } else {
        console.error(`❌ Python script failed with exit code ${exitCode}: ${path.basename(fullScriptPath)}`);
        reject(new Error(`Python script exited with code ${exitCode}\n${stderr}`));
      }
    });
    
    // Handle process errors
    pythonProcess.on('error', (error) => {
      console.error(`❌ Failed to start Python script: ${error.message}`);
      reject(error);
    });
  });
}

export async function runPythonDataPipeline(): Promise<void> {
  const srcDir = path.resolve(__dirname, '../../src');
  const pythonScriptsDir = path.join(srcDir, 'justel-data-processer');
  
  try {
    console.log('\n' + '='.repeat(70));
    console.log('🚀 STARTING PYTHON DATA PIPELINE');
    console.log('='.repeat(70));
    
    // Step 1: Update the full-list.csv with newest URLs
    console.log('\n📋 Step 1: Updating full-list.csv with newest URLs...');
     await runPythonScript(
     path.join(pythonScriptsDir, 'populate_full_list.py'),
     // {
       // cwd: pythonScriptsDir,
        //showOutput: true
     // }
    //);
    
    // Step 2: Run HTML scraping
    //console.log('\n📥 Step 2: Running HTML scraping (full production mode)...');
    //await runPythonScript(
     // path.join(pythonScriptsDir, 'run_comprehensive_html_scraping.py'),
      //{
       // args: [
         // '--concurrent', '35',  // 35 concurrent requests
         // '--delay', '0.02',     // 0.02s delay between batches
         // '--resume'             // Resume from checkpoint if exists
       // ],
        //cwd: pythonScriptsDir,
       // showOutput: true
     // }
    //);
    
    // Step 3: Run comprehensive pipeline
    console.log('\n📊 Step 3: Running comprehensive pipeline (full production mode)...');
    await runPythonScript(
      path.join(pythonScriptsDir, 'comprehensive_pipeline.py'),
      {
        args: [
          '--process-all',       // Process all files
          '--batch-size', '1000' // Process 1000 files per batch
        ],
        cwd: pythonScriptsDir,
        showOutput: true
      }
    );
    
    console.log('\n' + '='.repeat(70));
    console.log('✅ PYTHON DATA PIPELINE COMPLETED SUCCESSFULLY');
    console.log('='.repeat(70) + '\n');
    
    // Add a pause to ensure all files are written and processes are complete
    console.log('⏸️  Pausing for 2 seconds to ensure all files are written...');
    await new Promise(resolve => setTimeout(resolve, 2000));
    console.log('▶️  Continuing with Node.js pipeline...\n');
    
  } catch (error) {
    console.error('\n' + '='.repeat(70));
    console.error('❌ PYTHON DATA PIPELINE FAILED');
    console.error('='.repeat(70));
    throw error;
  }
}
