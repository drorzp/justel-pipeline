import os
import html2text
import re
import json
from bs4 import BeautifulSoup

def extract_and_preserve_tables(html_content):
    """
    Extract HTML tables and replace them with placeholders.
    Returns the modified HTML and a dictionary of extracted tables.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')
    
    preserved_tables = {}
    
    for i, table in enumerate(tables):
        # Generate a unique placeholder
        table_id = f"TABLE_PLACEHOLDER_{i:04d}"
        
        # Store the original HTML table
        preserved_tables[table_id] = str(table)
        
        # Replace the table with a placeholder
        placeholder = soup.new_tag('p')
        placeholder.string = f"[{table_id}]"
        table.replace_with(placeholder)
    
    return str(soup), preserved_tables

def preserve_belgian_footnotes(html_content):
    """
    Preserve Belgian footnote references before html2text conversion.
    Converts complex HTML footnote patterns to simple placeholder format that survives html2text.
    """
    # Belgian footnote reference pattern (actual pattern found in the HTML):
    # [<sup><font color=red>NUMBER</font></sup> text content]<sup><font color=red>NUMBER</font></sup>
    footnote_pattern = re.compile(
        r'\[<sup><font color=red>(\d+)</font></sup>'
        r'(.*?)'
        r'\]<sup><font color=red>(\d+)</font></sup>',
        re.DOTALL | re.IGNORECASE
    )

    def replace_footnote(match):
        number1, referenced_text, number2 = match.groups()
        # Validate that both numbers match
        if number1 != number2:
            print(f"Warning: Mismatched footnote numbers: {number1} vs {number2}")
        # Convert to target format: [NUMBER text content]NUMBER
        # This matches the original HTML display format
        return f'[{number1}{referenced_text.strip()}]{number1}'

    # Replace Belgian footnote patterns with simplified format
    preserved_content = footnote_pattern.sub(replace_footnote, html_content)

    return preserved_content

def convert_html_to_markdown_preserve_tables(source_folder, output_folder):
    """
    Convert HTML to Markdown while preserving original HTML tables.
    Tables are stored in a separate JSON file for each document.
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Create a subfolder for preserved tables
    tables_folder = os.path.join(output_folder, 'preserved_tables')
    if not os.path.exists(tables_folder):
        os.makedirs(tables_folder)

    # Initialize the html2text converter
    h = html2text.HTML2Text()
    h.ignore_links = False         # Convert links to Markdown
    h.ignore_images = True         # Convert images to Markdown
    h.ignore_emphasis = False      # Retain emphasis tags like <em> and <i>
    h.bypass_tables = True         # Don't convert tables - we'll preserve them
    h.skip_internal_links = False  # Convert internal links (anchors)
    h.ignore_tables = True         # Ignore tables completely
    h.protect_links = False        # Convert links to Markdown format
    h.unicode_snob = False         # Convert Unicode to ASCII where possible
    h.body_width = 0               # Disable text wrapping
    h.wrap_links = False           # Do not wrap long links
    h.single_line_break = False    # Use double line breaks for paragraphs
    h.google_doc = False           # Not specifically converting Google Docs

    # Iterate over all text files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(source_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()

                # Extract and preserve tables
                modified_html, preserved_tables = extract_and_preserve_tables(html_content)
                
                # Preserve Belgian footnote references before conversion
                preserved_content = preserve_belgian_footnotes(modified_html)

                # Convert to markdown
                markdown_content = h.handle(preserved_content)
                
                # Save preserved tables to JSON
                if preserved_tables:
                    tables_filename = os.path.splitext(filename)[0] + '_tables.json'
                    tables_path = os.path.join(tables_folder, tables_filename)
                    with open(tables_path, 'w', encoding='utf-8') as tables_file:
                        json.dump(preserved_tables, tables_file, ensure_ascii=False, indent=2)
                    print(f"  - Preserved {len(preserved_tables)} tables in {tables_filename}")

                # Write the markdown content to the output folder
                output_filename = os.path.splitext(filename)[0] + '.md'
                output_path = os.path.join(output_folder, output_filename)
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(markdown_content)
            
            print(f"Converted {filename} to {output_filename} (tables preserved separately)")

if __name__ == "__main__":
    source_folder = "output/15"  # Source folder with HTML files
    output_folder = "output/16"  # Output folder for Markdown files
    convert_html_to_markdown_preserve_tables(source_folder, output_folder)