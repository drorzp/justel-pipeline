#!/usr/bin/env python3
"""
Script to filter and copy JSON files with non-empty document_hierarchy from all files in output/24 folder.
"""

import os
import json
import shutil
import sys

def get_all_json_files():
    """Get the list of all JSON files from the output/24 directory."""

    json_dir = 'output/24'

    if not os.path.exists(json_dir):
        print(f"Error: {json_dir} directory not found.")
        return []

    # Get all JSON files in the directory
    all_files = []
    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):
            # Remove .json extension to get the base filename
            base_filename = filename[:-5]
            all_files.append(base_filename)

    all_files.sort()  # Sort for consistent processing order

    print(f"Found {len(all_files)} JSON files in {json_dir}")

    return all_files

def analyze_json_file(json_path):
    """Analyze a JSON file to check if document_hierarchy is non-empty."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check if document_hierarchy exists and is non-empty
        document_hierarchy = data.get('document_hierarchy', [])
        
        if isinstance(document_hierarchy, list) and len(document_hierarchy) > 0:
            return True, len(document_hierarchy)
        else:
            return False, 0
            
    except Exception as e:
        print(f"Error reading {json_path}: {e}")
        return False, 0

def filter_valid_jsons():
    """Filter and copy JSON files with non-empty document_hierarchy."""

    # Create valid_jsons directory
    valid_jsons_dir = 'valid_jsons'
    os.makedirs(valid_jsons_dir, exist_ok=True)
    print(f"Created directory: {valid_jsons_dir}")

    # Get all JSON files from output/24
    all_files = get_all_json_files()

    if not all_files:
        print("Error: No JSON files found in output/24 directory.")
        return

    # Analyze JSON files
    json_dir = 'output/24'

    total_analyzed = 0
    valid_files = []
    invalid_files = []

    print(f"\nAnalyzing {len(all_files)} JSON files in {json_dir}...")

    for filename in all_files:
        json_filename = f"{filename}.json"
        json_path = os.path.join(json_dir, json_filename)

        if os.path.exists(json_path):
            total_analyzed += 1
            is_valid, hierarchy_count = analyze_json_file(json_path)

            if is_valid:
                # Copy to valid_jsons folder
                dest_path = os.path.join(valid_jsons_dir, json_filename)
                shutil.copy2(json_path, dest_path)
                valid_files.append((filename, hierarchy_count))

                if total_analyzed % 50 == 0:
                    print(f"  Analyzed {total_analyzed} files...")
            else:
                invalid_files.append(filename)
        else:
            print(f"Warning: JSON file not found: {json_path}")
    
    # Print summary
    print(f"\n{'='*60}")
    print("FILTERING SUMMARY")
    print(f"{'='*60}")
    print(f"Total JSON files analyzed: {total_analyzed}")
    print(f"Files with valid (non-empty) document_hierarchy: {len(valid_files)}")
    print(f"Files with empty document_hierarchy: {len(invalid_files)}")
    print(f"Files copied to valid_jsons folder: {len(valid_files)}")
    
    # Show examples
    if valid_files:
        print(f"\nExamples of files copied (with hierarchy count):")
        for i, (filename, count) in enumerate(valid_files[:5]):
            print(f"  ✅ {filename}.json (hierarchy elements: {count})")
        if len(valid_files) > 5:
            print(f"  ... and {len(valid_files) - 5} more files")
    
    if invalid_files:
        print(f"\nExamples of files excluded (empty hierarchy):")
        for i, filename in enumerate(invalid_files[:5]):
            print(f"  ❌ {filename}.json")
        if len(invalid_files) > 5:
            print(f"  ... and {len(invalid_files) - 5} more files")
    
    print(f"\nValid JSON files are now available in: {valid_jsons_dir}/")
    
    return len(valid_files), len(invalid_files)

if __name__ == "__main__":
    filter_valid_jsons()
