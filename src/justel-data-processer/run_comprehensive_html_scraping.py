#!/usr/bin/env python3
"""
Run Comprehensive HTML Scraping for Belgian Legal Documents
Processes the complete 207,911 URL dataset discovered by the eJustice URL Discovery Scraper.
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from utilities.justel_web_scraper import JustelScraper, run_scraper


def main():
    """Main function for comprehensive HTML scraping."""
    
    print("🔧 Enhanced Belgian Legal Documents Text Scraping")
    print("=" * 70)
    print("📊 Dataset: Full Belgian legal document collection")
    print("📁 Input: data/csv_data/full-list.xlsx")
    print("📁 Output: input/")
    print("🔄 Features: French URL validation, resume capability, progress tracking, error handling")
    
    parser = argparse.ArgumentParser(description='Comprehensive HTML Scraping for Belgian Legal Documents')
    parser.add_argument('--test', '-t', action='store_true',
                       help='Run in test mode (process 20 URLs only)')
    parser.add_argument('--test-limit', type=int, default=20,
                       help='Number of URLs to process in test mode (default: 20)')
    parser.add_argument('--concurrent', '-c', type=int, default=35,
                       help='Number of concurrent requests (default: 35)')
    parser.add_argument('--delay', '-d', type=float, default=0.02,
                       help='Delay between batches in seconds (default: 0.02)')
    parser.add_argument('--resume', '-r', action='store_true',
                       help='Resume from checkpoint (automatic if checkpoint exists)')
    
    args = parser.parse_args()
    
    # Configuration
    input_excel = "data/csv_data/full-list.csv"  # Changed to CSV for better performance
    output_dir = "input"
    
    # Verify input file exists
    if not Path(input_excel).exists():
        print(f"❌ Error: Input Excel file not found: {input_excel}")
        print("   Please ensure the full-list.xlsx file is available.")
        return 1
    
    # Show configuration
    print(f"\n📋 Configuration:")
    print(f"  Input Excel: {input_excel}")
    print(f"  Output Directory: {output_dir}")
    print(f"  Concurrent Requests: {args.concurrent} (optimized)")
    print(f"  Delay Between Batches: {args.delay}s (optimized)")
    print(f"  Test Mode: {'Yes' if args.test else 'No'}")
    if args.test:
        print(f"  Test Limit: {args.test_limit} URLs")
    
    # Check for existing checkpoint
    checkpoint_file = Path(output_dir) / "scraping_checkpoint.json"
    if checkpoint_file.exists():
        print(f"  Resume Capability: ✅ Checkpoint found")
        print(f"  Checkpoint File: {checkpoint_file}")
    else:
        print(f"  Resume Capability: 🆕 Starting fresh")
    
    # Estimate processing time based on real-world performance
    if not args.test:
        # Based on actual performance: 13.3 URLs/second with 20 concurrent, 0.05s delay
        # Optimized: 35 concurrent, 0.02s delay should achieve ~23-25 URLs/second
        estimated_urls_per_second = 23.0  # Conservative estimate for optimized config
        estimated_seconds = 207911 / estimated_urls_per_second
        estimated_hours = estimated_seconds / 3600

        print(f"\n⏱️  Optimized Performance Estimates:")
        print(f"  Total URLs: 207,911")
        print(f"  Expected Speed: ~{estimated_urls_per_second} URLs/second (optimized)")
        print(f"  Estimated Time: {estimated_seconds/60:.1f} minutes ({estimated_hours:.1f} hours)")
        print(f"  Previous Performance: 4.3 hours → Target: ~2.5 hours (42% faster)")
        print(f"  Note: Conservative estimate - may be even faster in practice")
    
    # Confirm before starting
    # if not args.test:
    #     print(f"\n⚠️  This will process 207,911 URLs and may take several hours.")
    #     print(f"   The process can be interrupted and resumed using checkpoints.")
    #     print(f"   HTML files will be saved to: {output_dir}")
        
    #     response = input(f"\n🚀 Start comprehensive HTML scraping? (y/N): ")
    #     if response.lower() != 'y':
    #         print("❌ Operation cancelled.")
    #         return 0
    
    try:
        print(f"\n🏃 Starting comprehensive HTML scraping...")
        print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Initialize scraper with comprehensive dataset configuration
        scraper = JustelScraper(
            input_excel=input_excel,
            output_dir=output_dir,
            delay=args.delay,
            concurrent_requests=args.concurrent,
            test_mode=args.test,
            test_limit=args.test_limit
        )
        
        # Run the scraper
        run_scraper(scraper)
        
        print(f"\n✅ Enhanced text scraping completed!")
        print(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📁 TXT files saved in: {output_dir}")
        
        # Show next steps
        print(f"\n📋 Next Steps:")
        print(f"1. Process TXT files through 000_Master.py pipeline")
        print(f"2. Upload JSON results to S3 with zip compression")
        
        return 0
        
    except KeyboardInterrupt:
        print(f"\n⏹️  Scraping interrupted by user.")
        print(f"   Progress has been saved to checkpoint.")
        print(f"   Resume with: python {sys.argv[0]} --resume")
        return 1
        
    except Exception as e:
        print(f"\n❌ Scraping failed: {str(e)}")
        print(f"   Check logs for details.")
        print(f"   Resume with: python {sys.argv[0]} --resume")
        return 1


if __name__ == "__main__":
    sys.exit(main())
