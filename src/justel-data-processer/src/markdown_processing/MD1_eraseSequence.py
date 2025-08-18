import os
import re

def remove_content(text, start_delimiter, end_delimiter, skip_delimiter=False):
    if skip_delimiter:
        # Use regular expressions to find and protect content between delimiters
        pattern = re.compile(f'{re.escape(start_delimiter)}.*?{re.escape(end_delimiter)}', re.DOTALL | re.IGNORECASE)
###        pattern = re.compile(f'{re.escape(start_delimiter)}.*?{re.escape(end_delimiter)}', re.DOTALL) ### REPLACE PREVIOUS LINE FOR CASE-SENSITIVITY (REGARDING THE CONTENT OF THE DELIMITERS)
        protected_content = pattern.findall(text)
        for i, block in enumerate(protected_content):
            text = text.replace(block, f'__PROTECTED_BLOCK_{i}__')

    pattern = r'\(#.*?\)'
    text = re.sub(pattern, '', text)

    if skip_delimiter:
        # Restore protected content
        for i, block in enumerate(protected_content):
            text = text.replace(f'__PROTECTED_BLOCK_{i}__', block)

    return text

def process_file(input_file, output_file, log_file, start_delimiter, end_delimiter, skip_delimiter=False):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified_content = remove_content(content, start_delimiter, end_delimiter, skip_delimiter)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(modified_content)
    
    erased_content = re.findall(r'\(#.*?\)', content)
    with open(log_file, 'a', encoding='utf-8') as file:
        file.write('\n'.join(erased_content))

def display_completion_rate(current, total):
    completion_rate = (current / total) * 100
    print(f"Processing file {current}/{total} - {completion_rate:.2f}%")

def handle_error(error):
    print(f"Error occurred: {error}")

def create_output_directory(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def main(input_dir, output_dir, log_file, start_delimiter, end_delimiter, skip_delimiter=False):
    create_output_directory(output_dir)
    
    total_files = len(os.listdir(input_dir))
    current_file = 1
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename)
            
            try:
                process_file(input_file, output_file, log_file, start_delimiter, end_delimiter, skip_delimiter)
            except Exception as e:
                handle_error(e)
            
            display_completion_rate(current_file, total_files)
            current_file += 1

if __name__ == "__main__":
    input_dir = "output/16"
    output_dir = "output/17"
    log_file = "logs/log_MD1.txt"
    start_delimiter = "<table"
    end_delimiter = "</table>"
    skip_delimiter = True

    main(input_dir, output_dir, log_file, start_delimiter, end_delimiter, skip_delimiter)
