import os
import re

def process_files(input_dir, output_dir, start_delimiter, end_delimiter, skip_delimiter=False):
    # Check if output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get list of all txt files in the input directory
    files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

    # Initialize a counter for tracking progress
    total_files = len(files)
    processed_files = 0

    for file in files:
        with open(os.path.join(input_dir, file), 'r', encoding='utf-8') as f:
            content = f.read()

        if skip_delimiter:
            # Use regular expressions to find and protect content between delimiters
            pattern = re.compile(f'{re.escape(start_delimiter)}.*?{re.escape(end_delimiter)}', re.DOTALL | re.IGNORECASE)
###            pattern = re.compile(f'{re.escape(start_delimiter)}.*?{re.escape(end_delimiter)}', re.DOTALL) ### REPLACE PREVIOUS LINE FOR CASE-SENSITIVITY (REGARDING THE CONTENT OF THE DELIMITERS)
            protected_content = pattern.findall(content)
            for i, block in enumerate(protected_content):
                content = content.replace(block, f'__PROTECTED_BLOCK_{i}__')

        # Perform the required replacements
        content = content.replace("<BR><BR>&nbsp;&nbsp;<BR><BR>", "<BR><BR>")
        content = content.replace("<BR>&nbsp;&nbsp;<BR><BR>", "<BR><BR>")
        content = content.replace("<BR><BR>&nbsp;&nbsp;<BR><BR>&nbsp;&nbsp;", "<BR><BR>&nbsp;&nbsp;")
        content = content.replace("<BR>&nbsp;&nbsp;<BR><BR>&nbsp;&nbsp;", "<BR><BR>&nbsp;&nbsp;")
        content = content.replace("<BR>&nbsp;&nbsp;<BR>&nbsp;&nbsp;<BR>&nbsp;&nbsp;", "<BR><BR>&nbsp;&nbsp;")
        content = content.replace("<BR>&nbsp;&nbsp;<BR>&nbsp;&nbsp;", "<BR><BR>&nbsp;&nbsp;")

        if skip_delimiter:
            # Restore protected content
            for i, block in enumerate(protected_content):
                content = content.replace(f'__PROTECTED_BLOCK_{i}__', block)

        # Write the modified content to a new file in the output directory
        with open(os.path.join(output_dir, file), 'w', encoding='utf-8') as f:
            f.write(content)

        # Update and print the progress
        processed_files += 1
        print(f"Processed {processed_files} out of {total_files} files.")

# Usage:
process_files('output/12', 'output/13', '<table', '</table>', skip_delimiter=True)
