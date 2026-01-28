"""
MASTER SCRIPT - Database Consolidation Pipeline
================================================
This script runs the complete database consolidation process:
1. Inspect database structure
2. Consolidate all sheets
3. Validate data quality
4. Extract to JSON format

Author: AI Assistant
Date: 2026-01-27
"""

import subprocess
import sys
import os
from datetime import datetime

def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")

def run_script(script_name, description):
    """Run a Python script and handle errors"""
    print_header(f"STEP: {description}")
    print(f"Running: {script_name}\n")
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        print(result.stdout)
        
        if result.stderr:
            print("STDERR:", result.stderr)
        
        if result.returncode != 0:
            print(f"❌ Error running {script_name}")
            return False
        
        print(f"✅ {description} completed successfully")
        return True
        
    except Exception as e:
        print(f"❌ Exception running {script_name}: {e}")
        return False

def check_file_exists(filename):
    """Check if a file exists"""
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"✅ {filename} exists ({size:,} bytes)")
        return True
    else:
        print(f"❌ {filename} not found")
        return False

def main():
    print_header("DATABASE CONSOLIDATION PIPELINE")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check if source file exists
    if not check_file_exists("ESTUDIANTES.xlsx"):
        print("\n❌ Source file 'ESTUDIANTES.xlsx' not found. Aborting.")
        return
    
    # Pipeline steps
    steps = [
        {
            'script': 'inspect_database.py',
            'description': 'Inspecting database structure',
            'output_file': 'inspection_results.txt'
        },
        {
            'script': 'consolidate_database.py',
            'description': 'Consolidating all sheets',
            'output_file': 'ESTUDIANTES_CONSOLIDADO.xlsx'
        },
        {
            'script': 'validate_data.py',
            'description': 'Validating data quality',
            'output_file': 'validation_report.txt'
        },
        {
            'script': 'extract_to_json.py',
            'description': 'Extracting to JSON format',
            'output_file': 'estudiantes_database.json'
        }
    ]
    
    # Execute pipeline
    success_count = 0
    
    for i, step in enumerate(steps, 1):
        print(f"\n{'─' * 70}")
        print(f"PIPELINE STEP {i}/{len(steps)}")
        print(f"{'─' * 70}")
        
        if run_script(step['script'], step['description']):
            success_count += 1
            
            # Verify output file was created
            if step['output_file']:
                print(f"\nVerifying output file...")
                check_file_exists(step['output_file'])
        else:
            print(f"\n⚠️ Step {i} failed. Continuing to next step...")
    
    # Summary
    print_header("PIPELINE SUMMARY")
    print(f"Completed: {success_count}/{len(steps)} steps")
    print(f"Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if success_count == len(steps):
        print("\n✅ ALL STEPS COMPLETED SUCCESSFULLY!")
        print("\nGenerated files:")
        print("  1. inspection_results.txt - Database structure analysis")
        print("  2. ESTUDIANTES_CONSOLIDADO.xlsx - Consolidated database")
        print("  3. validation_report.txt - Data quality report")
        print("  4. estudiantes_database.json - JSON format for AI agent")
        print("\n🎯 Next steps:")
        print("  - Review validation_report.txt for data quality issues")
        print("  - Open ESTUDIANTES_CONSOLIDADO.xlsx to verify consolidation")
        print("  - Use estudiantes_database.json in your n8n workflow")
    else:
        print(f"\n⚠️ {len(steps) - success_count} step(s) failed. Check errors above.")

if __name__ == "__main__":
    main()
