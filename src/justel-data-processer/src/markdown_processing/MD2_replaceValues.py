import os
import re

def replace_values(text, replacements, start_delimiter, end_delimiter, skip_delimiter=False):
    if skip_delimiter:
        # Use regular expressions to find and protect content between delimiters
        pattern = re.compile(f'{re.escape(start_delimiter)}.*?{re.escape(end_delimiter)}', re.DOTALL | re.IGNORECASE)
###        pattern = re.compile(f'{re.escape(start_delimiter)}.*?{re.escape(end_delimiter)}', re.DOTALL) ### REPLACE PREVIOUS LINE FOR CASE-SENSITIVITY (REGARDING THE CONTENT OF THE DELIMITERS)
        protected_content = pattern.findall(text)
        for i, block in enumerate(protected_content):
            text = text.replace(block, f'__PROTECTED_BLOCK_{i}__')

    # Transform Belgian footnote references from [NUMBER] text content][NUMBER] to [NUMBER text content]NUMBER
    belgian_footnote_pattern = re.compile(r'\[(\d+)\] ([^\]]+)\]\[(\d+)\]')

    def fix_belgian_footnote(match):
        number1, text_content, number2 = match.groups()
        # Validate that both numbers match
        if number1 != number2:
            print(f"Warning: Mismatched Belgian footnote numbers: {number1} vs {number2}")
        # Convert to target format: [NUMBER text content]NUMBER
        return f'[{number1} {text_content}]{number1}'

    text = belgian_footnote_pattern.sub(fix_belgian_footnote, text)

    for old_value, new_value in replacements.items():
        text = text.replace(old_value, new_value)

    if skip_delimiter:
        # Restore protected content
        for i, block in enumerate(protected_content):
            text = text.replace(f'__PROTECTED_BLOCK_{i}__', block)

    return text

def process_file(input_file, output_file, log_file, replacements, start_delimiter, end_delimiter, skip_delimiter=False):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    modified_content = replace_values(content, replacements, start_delimiter, end_delimiter, skip_delimiter)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(modified_content)

    # Log replacements
    for old_value, new_value in replacements.items():
        if old_value in content:
            log_entry = f"Replaced '{old_value}' with '{new_value}' in {input_file}\n"
            with open(log_file, 'a', encoding='utf-8') as log:
                log.write(log_entry)

def display_completion_rate(current, total):
    completion_rate = (current / total) * 100
    print(f"Processing file {current}/{total} - {completion_rate:.2f}%")

def handle_error(error):
    print(f"Error occurred: {error}")

def create_output_directory(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def main(input_dir, output_dir, log_file, replacements, start_delimiter, end_delimiter, skip_delimiter=False):
    create_output_directory(output_dir)
    
    total_files = len(os.listdir(input_dir))
    current_file = 1
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename)
            
            try:
                process_file(input_file, output_file, log_file, replacements, start_delimiter, end_delimiter, skip_delimiter)
            except Exception as e:
                handle_error(e)
            
            display_completion_rate(current_file, total_files)
            current_file += 1

if __name__ == "__main__":
    input_dir = "output/17"
    output_dir = "output/18"
    log_file = "logs/log_MD2.txt"

    # Define the replacements as a dictionary
    replacements = {
        "](/": "](https://www.ejustice.just.fgov.be/",
        "](article": "](https://www.ejustice.just.fgov.be/cgi_loi/article",
        "   ]": "]",
        "  ]": "]",
        " ]": "]",
        "   )": ")",
        "  )": ")",
        " )": ")",
        "[   ": "[",
        "[  ": "[",
        "[ ": "[",
        "(   ": "(",
        "(  ": "(",
        "( ": "(",
        "    (": " (",
        "   (": " (",
        "  (": " (",
        "    [": " [",
        "   [": " [",
        "  [": " [",
        "]    ": "] ",
        "]   ": "] ",
        "]  ": "] ",
        ")    ": ") ",
        ")   ": ") ",
        ")  ": ") ",
#        "(": " (",
#        ")": ") ",
#        "[": " [",
#        "]": "] ",
        "## Titel": "## Titre",
        "## Inhoudstafel": "## Table des matières",
        "## Tekst": "## Texte",
        "## Wijziging(en)": "## Fiche des modifications",
        "## Link": "## Lien",
        "## Externe link": "## Lien externe",
        "## Aanhef": "## Préambule",
        "## Verslag aan de Koning": "## Rapport au Roi",
        "## Handtekening": "## Signatures",
        "## Parlementaire werkzaamheden": "## Travaux parlementaires",
#        "## Links": "## Liens",
#        "## Externe links": "## Liens externes",
    }

    start_delimiter = "<table"
    end_delimiter = "</table>"
    skip_delimiter = True
    
    main(input_dir, output_dir, log_file, replacements, start_delimiter, end_delimiter, skip_delimiter)
