#!/usr/bin/env python3
"""
enhanced_json_validator.py - Enhanced validation for Belgian legal document JSON files

This script validates Belgian legal documents using OR logic between two criteria groups:
- Group A: Non-empty document_hierarchy
- Group B: Complete metadata with all required fields populated

Validation Criteria (OR logic):
1. Non-empty document_hierarchy array, OR
2. Complete document_metadata with required fields:
   - document_number (not empty string)
   - title (not empty string)
   - publication_date (not empty string)
   - page_number (not empty string, "0" is valid)
   - dossier_number (not empty string)
   - effective_date (not empty string)

Author: Augment Agent
Date: 2025-07-15
"""

import os
import json
import shutil
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/enhanced_json_validator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class EnhancedJSONValidator:
    """
    Enhanced validator for Belgian legal document JSON files with multiple validation criteria.
    """
    
    def __init__(self, source_dir: str = "output/24", target_dir: str = "valid_jsons_enhanced"):
        """
        Initialize the enhanced validator.
        
        Args:
            source_dir: Directory containing JSON files to validate
            target_dir: Directory to copy valid JSON files
        """
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        
        # Required metadata fields for validation
        self.required_metadata_fields = [
            'document_number',
            'title',
            'publication_date',
            'page_number',
            'dossier_number',
            'effective_date'
        ]
        
        # Statistics tracking
        self.stats = {
            'total_files': 0,
            'hierarchy_valid_only': set(),
            'metadata_valid_only': set(),
            'both_criteria_valid': set(),
            'invalid_files': set(),
            'processing_errors': []
        }
    
    def validate_directories(self) -> bool:
        """Validate source directory and create target directory."""
        try:
            # Check source directory
            if not self.source_dir.exists():
                logger.error(f"Source directory does not exist: {self.source_dir}")
                return False
            
            if not self.source_dir.is_dir():
                logger.error(f"Source path is not a directory: {self.source_dir}")
                return False
            
            # Create target directory
            self.target_dir.mkdir(parents=True, exist_ok=True)
            logger.info(f"Target directory created/verified: {self.target_dir}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error validating directories: {e}")
            return False
    
    def get_json_files(self) -> List[Path]:
        """Get all JSON files from the source directory."""
        try:
            json_files = []
            for file_path in self.source_dir.iterdir():
                if file_path.is_file() and file_path.suffix.lower() == '.json':
                    json_files.append(file_path)
            
            # Sort files for consistent processing order
            json_files.sort(key=lambda x: x.name)
            
            logger.info(f"Found {len(json_files)} JSON files in {self.source_dir}")
            self.stats['total_files'] = len(json_files)
            return json_files
            
        except Exception as e:
            logger.error(f"Error reading JSON files from {self.source_dir}: {e}")
            return []
    
    def validate_document_hierarchy(self, data: Dict[str, Any]) -> bool:
        """
        Validate document_hierarchy criterion (existing validation).
        
        Args:
            data: Parsed JSON data
            
        Returns:
            True if document_hierarchy is non-empty
        """
        try:
            document_hierarchy = data.get('document_hierarchy', [])
            return isinstance(document_hierarchy, list) and len(document_hierarchy) > 0
        except Exception:
            return False
    
    def validate_metadata_completeness(self, data: Dict[str, Any]) -> bool:
        """
        Validate metadata completeness criterion.

        Args:
            data: Parsed JSON data

        Returns:
            True if all required metadata fields are populated (not empty strings)
        """
        try:
            document_metadata = data.get('document_metadata', {})

            if not isinstance(document_metadata, dict):
                return False

            # Check each required field
            for field in self.required_metadata_fields:
                value = document_metadata.get(field)

                # Field must exist and not be None
                if value is None:
                    return False

                # For strings, check if not empty string (but "0" is valid for page_number)
                if isinstance(value, str):
                    if value == "":  # Empty string is invalid
                        return False

                # For numbers, only reject if None (0 is valid for page_number)
                # No additional numeric validation needed

            return True

        except Exception:
            return False
    
    def validate_json_file(self, file_path: Path) -> Tuple[bool, bool, Dict[str, Any]]:
        """
        Validate a single JSON file against both criteria.
        
        Args:
            file_path: Path to JSON file
            
        Returns:
            Tuple of (hierarchy_valid, metadata_valid, parsed_data)
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            hierarchy_valid = self.validate_document_hierarchy(data)
            metadata_valid = self.validate_metadata_completeness(data)
            
            return hierarchy_valid, metadata_valid, data
            
        except json.JSONDecodeError as e:
            logger.warning(f"Invalid JSON in {file_path.name}: {e}")
            self.stats['processing_errors'].append(f"{file_path.name}: JSON decode error")
            return False, False, {}
        except Exception as e:
            logger.warning(f"Error processing {file_path.name}: {e}")
            self.stats['processing_errors'].append(f"{file_path.name}: {str(e)}")
            return False, False, {}
    
    def copy_valid_file(self, source_path: Path) -> bool:
        """Copy a valid file to the target directory."""
        try:
            target_path = self.target_dir / source_path.name
            shutil.copy2(source_path, target_path)
            return True
        except Exception as e:
            logger.error(f"Failed to copy {source_path.name}: {e}")
            return False
    
    def process_all_files(self) -> bool:
        """Process all JSON files and apply validation criteria."""
        try:
            logger.info("Starting enhanced JSON validation process...")
            
            # Validate directories
            if not self.validate_directories():
                return False
            
            # Get JSON files
            json_files = self.get_json_files()
            if not json_files:
                logger.warning("No JSON files found to process")
                return True
            
            # Process each file
            processed_count = 0
            for file_path in json_files:
                hierarchy_valid, metadata_valid, data = self.validate_json_file(file_path)
                
                filename = file_path.name
                
                # Categorize the file based on validation results
                if hierarchy_valid and metadata_valid:
                    self.stats['both_criteria_valid'].add(filename)
                elif hierarchy_valid and not metadata_valid:
                    self.stats['hierarchy_valid_only'].add(filename)
                elif not hierarchy_valid and metadata_valid:
                    self.stats['metadata_valid_only'].add(filename)
                else:
                    self.stats['invalid_files'].add(filename)

                # Copy file if it meets either criterion (OR logic)
                if hierarchy_valid or metadata_valid:
                    self.copy_valid_file(file_path)
                
                processed_count += 1
                
                # Progress indicator
                if processed_count % 100 == 0:
                    logger.info(f"Processed {processed_count}/{len(json_files)} files...")
            
            logger.info("Enhanced JSON validation completed successfully!")
            return True
            
        except Exception as e:
            logger.error(f"Error during validation process: {e}")
            return False
    
    def get_validation_statistics(self) -> Dict[str, Any]:
        """Calculate comprehensive validation statistics."""
        hierarchy_only_count = len(self.stats['hierarchy_valid_only'])
        metadata_only_count = len(self.stats['metadata_valid_only'])
        both_criteria_count = len(self.stats['both_criteria_valid'])
        invalid_count = len(self.stats['invalid_files'])
        
        # Total valid files (union of all valid categories)
        all_valid_files = (
            self.stats['hierarchy_valid_only'] | 
            self.stats['metadata_valid_only'] | 
            self.stats['both_criteria_valid']
        )
        total_valid_count = len(all_valid_files)
        
        # Files that meet hierarchy criterion (both old and new)
        hierarchy_criterion_total = hierarchy_only_count + both_criteria_count
        
        # Files that meet metadata criterion (new)
        metadata_criterion_total = metadata_only_count + both_criteria_count
        
        return {
            'total_files': self.stats['total_files'],
            'hierarchy_only_count': hierarchy_only_count,
            'metadata_only_count': metadata_only_count,
            'both_criteria_count': both_criteria_count,
            'total_valid_count': total_valid_count,
            'invalid_count': invalid_count,
            'hierarchy_criterion_total': hierarchy_criterion_total,
            'metadata_criterion_total': metadata_criterion_total,
            'processing_errors_count': len(self.stats['processing_errors']),
            'validation_success_rate': (total_valid_count / self.stats['total_files'] * 100) if self.stats['total_files'] > 0 else 0
        }

    def generate_detailed_report(self) -> str:
        """Generate a comprehensive validation report."""
        stats = self.get_validation_statistics()

        # Compare with previous validation results (1,321 valid files)
        previous_valid_count = 1321
        improvement = stats['total_valid_count'] - previous_valid_count
        improvement_percentage = (improvement / previous_valid_count * 100) if previous_valid_count > 0 else 0

        report_lines = [
            "=" * 100,
            "ENHANCED JSON VALIDATION REPORT - BELGIAN LEGAL DOCUMENTS",
            "=" * 100,
            f"Validation Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Source Directory: {self.source_dir}",
            f"Target Directory: {self.target_dir}",
            "",
            "VALIDATION CRITERIA (OR LOGIC):",
            "  1. Document Hierarchy: Non-empty document_hierarchy array, OR",
            "  2. Metadata Completeness: All required metadata fields populated (not empty strings)",
            f"     Required fields: {', '.join(self.required_metadata_fields)}",
            "     Note: page_number value '0' is considered valid, but '' is invalid",
            "",
            "PROCESSING SUMMARY:",
            f"  📊 Total files processed: {stats['total_files']:,}",
            f"  ✅ Total valid files: {stats['total_valid_count']:,} ({stats['validation_success_rate']:.1f}%)",
            f"  ❌ Invalid files: {stats['invalid_count']:,}",
            f"  ⚠️  Processing errors: {stats['processing_errors_count']:,}",
            "",
            "VALIDATION BREAKDOWN:",
            f"  📋 Valid by hierarchy criterion only: {stats['hierarchy_only_count']:,} files",
            f"  📝 Valid by metadata criterion only: {stats['metadata_only_count']:,} files",
            f"  🎯 Valid by both criteria: {stats['both_criteria_count']:,} files",
            "",
            "CRITERION TOTALS:",
            f"  📋 Total meeting hierarchy criterion: {stats['hierarchy_criterion_total']:,} files",
            f"  📝 Total meeting metadata criterion: {stats['metadata_criterion_total']:,} files",
            "",
            "COMPARISON WITH PREVIOUS VALIDATION:",
            f"  📈 Previous valid count (hierarchy only): {previous_valid_count:,} files",
            f"  📈 New valid count (enhanced criteria): {stats['total_valid_count']:,} files",
            f"  🚀 Improvement: {improvement:+,} files ({improvement_percentage:+.1f}%)",
            "",
            "DETAILED STATISTICS:",
        ]

        # Add sample files from each category
        if self.stats['hierarchy_valid_only']:
            sample_hierarchy = list(self.stats['hierarchy_valid_only'])[:5]
            report_lines.extend([
                f"  📋 Hierarchy-only valid files (sample of {len(sample_hierarchy)}):",
                f"     {', '.join(sample_hierarchy)}",
                ""
            ])

        if self.stats['metadata_valid_only']:
            sample_metadata = list(self.stats['metadata_valid_only'])[:5]
            report_lines.extend([
                f"  📝 Metadata-only valid files (sample of {len(sample_metadata)}):",
                f"     {', '.join(sample_metadata)}",
                ""
            ])

        if self.stats['both_criteria_valid']:
            sample_both = list(self.stats['both_criteria_valid'])[:5]
            report_lines.extend([
                f"  🎯 Both-criteria valid files (sample of {len(sample_both)}):",
                f"     {', '.join(sample_both)}",
                ""
            ])

        if self.stats['processing_errors']:
            report_lines.extend([
                "PROCESSING ERRORS:",
                *[f"  ❌ {error}" for error in self.stats['processing_errors'][:10]],
                ""
            ])

        report_lines.extend([
            "RECOMMENDATIONS:",
            f"  • Use the enhanced validation to recover {stats['metadata_only_count']:,} additional valid documents",
            f"  • Focus quality review on {stats['both_criteria_count']:,} files meeting both criteria (highest quality)",
            f"  • Consider manual review of {stats['invalid_count']:,} remaining invalid files for edge cases",
            "",
            "✅ Enhanced validation completed successfully!",
            f"📂 Valid files are available in: {self.target_dir}/",
            "=" * 100
        ])

        return "\n".join(report_lines)

    def save_report(self, report: str, filename: str = "enhanced_validation_report.txt") -> None:
        """Save the validation report to a file."""
        try:
            report_path = self.target_dir / filename
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
            logger.info(f"Validation report saved to: {report_path}")
        except Exception as e:
            logger.error(f"Failed to save report: {e}")


def main():
    """Main execution function."""
    try:
        # Create enhanced validator
        validator = EnhancedJSONValidator(
            source_dir="output/24",
            target_dir="valid_jsons_enhanced"
        )

        # Process all files with enhanced validation
        success = validator.process_all_files()

        if success:
            # Generate and display comprehensive report
            report = validator.generate_detailed_report()
            print(report)

            # Save report to file
            validator.save_report(report)

            return True
        else:
            logger.error("Enhanced validation failed")
            return False

    except Exception as e:
        logger.error(f"Unexpected error in main: {e}")
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
