import subprocess
import os
import glob
import logging

# Configuration for batch processing
INPUT_DIR = "data/text_input"
OUTPUT_DIR = "output"

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/batch_processing.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def get_files_to_process():
    """Get list of .txt files to process"""
    try:
        # Get all .txt files from input directory
        txt_files = glob.glob(os.path.join(INPUT_DIR, "*.txt"))

        # Sort alphabetically by filename
        txt_files.sort(key=lambda x: os.path.basename(x))

        logger.info(f"Found {len(txt_files)} .txt files in {INPUT_DIR}")
        logger.info(f"Will process all {len(txt_files)} files")

        return txt_files
    except Exception as e:
        logger.error(f"Error getting files to process: {e}")
        return []

# List of scripts to run in order
scripts = [
    "src/text_processing/0-1_replaceValues.py",
    "src/text_processing/0-2_eraseSequence.py",
    "src/text_processing/0-3_replaceValues.py",
    "src/text_processing/1-1_replaceValues.py",
    "src/text_processing/1-2_replaceValues.py",
    "src/text_processing/1-3_replaceValues.py",
    "src/text_processing/2-1_replaceValues.py",
    "src/text_processing/2-2_eraseSequence.py",
    "src/text_processing/2-3_replaceValues.py",
    "src/text_processing/3-1_replaceValues.py",
    "src/text_processing/3-2_eraseSequence.py",
    "src/text_processing/3-3_replaceValues.py",
    "src/text_processing/4-1_replaceValues.py",
    "src/text_processing/4-2_replaceValues.py",
    "src/text_processing/4-3_replaceValues.py",
    "src/markdown_processing/MD0_html_to_md_preserve_tables.py",
    "src/markdown_processing/MD1_eraseSequence.py",
    "src/markdown_processing/MD2_replaceValues.py",
    "src/markdown_processing/MD3_replaceValues.py",
    "src/markdown_processing/MD4_replaceValues.py",
    "src/markdown_processing/MD5_replaceValues.py",
    "src/markdown_processing/MD6_replaceValues.py",
    "src/markdown_processing/MD7_Split.py",
    "src/markdown_processing/MD8_extract_to_json.py",
    "src/markdown_processing/MD10_process_tables.py",
]

def run_script(script, total, current):
    """Run a single script with error handling and logging"""
    logger.info(f"Running {script}... ({current}/{total})")
    try:
        result = subprocess.run(["python3", script], capture_output=True, text=True, timeout=300)
        if result.returncode != 0:
            logger.error(f"Error running {script}: {result.stderr}")
            if result.stdout:
                logger.error(f"Script output: {result.stdout}")
            return False
        else:
            logger.info(f"Successfully ran {script}")
            return True
    except subprocess.TimeoutExpired:
        logger.error(f"Timeout running {script} (exceeded 5 minutes)")
        return False
    except Exception as e:
        logger.error(f"Unexpected error running {script}: {e}")
        return False

def process_all_files():
    """Process all files in the input directory through the entire pipeline"""
    logger.info("Processing all files in input directory through the pipeline")

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Run all scripts
    total_scripts = len(scripts)
    success_count = 0

    for i, script in enumerate(scripts, start=1):
        if run_script(script, total_scripts, i):
            success_count += 1
        else:
            logger.error(f"Script {script} failed")
            break  # Stop processing if a script fails

    logger.info(f"Pipeline completed: {success_count}/{total_scripts} scripts ran successfully")
    return success_count == total_scripts

def main():
    """Main function for processing all files in input directory"""
    # Change to the directory where the scripts are located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    logger.info("Starting Belgian Legal Document Processing Pipeline")
    logger.info("=" * 80)

    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Get files to process
    files_to_process = get_files_to_process()

    if not files_to_process:
        logger.error("No .txt files found to process. Exiting.")
        return

    total_files = len(files_to_process)
    logger.info(f"Found {total_files} files in input directory")
    logger.info(f"Files to process: {[os.path.basename(f) for f in files_to_process]}")

    # Process all files through the pipeline
    logger.info(f"\n{'='*60}")
    logger.info(f"PROCESSING ALL FILES THROUGH PIPELINE")
    logger.info(f"{'='*60}")

    try:
        if process_all_files():
            logger.info(f"✅ Successfully processed all files through the pipeline")
        else:
            logger.error(f"❌ Pipeline failed - check logs for details")
    except Exception as e:
        logger.error(f"❌ Unexpected error during processing: {e}")

    # Final summary
    logger.info(f"\n{'='*80}")
    logger.info("PROCESSING SUMMARY")
    logger.info(f"{'='*80}")
    logger.info(f"Total files in input: {total_files}")
    logger.info(f"Output directory: {OUTPUT_DIR}")
    logger.info("Processing completed!")

if __name__ == "__main__":
    main()
