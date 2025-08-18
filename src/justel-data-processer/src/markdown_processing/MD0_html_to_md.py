import os
import html2text
import re

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

def convert_html_to_markdown(source_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize the html2text converter
    h = html2text.HTML2Text()
    h.ignore_links = False         # Convert links to Markdown
    h.ignore_images = True        # Convert images to Markdown
    h.ignore_emphasis = False      # Retain emphasis tags like <em> and <i>
    h.bypass_tables = True        # Convert tables to Markdown
    h.skip_internal_links = False  # Convert internal links (anchors)
    h.ignore_tables = False        # Convert tables to Markdown
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

                # Preserve Belgian footnote references before conversion
                preserved_content = preserve_belgian_footnotes(html_content)

                # Convert to markdown
                markdown_content = h.handle(preserved_content)

                # Write the markdown content to the output folder
                output_filename = os.path.splitext(filename)[0] + '.md'
                output_path = os.path.join(output_folder, output_filename)
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(markdown_content)
            print(f"Converted {filename} to {output_filename} (Belgian footnotes preserved)")

if __name__ == "__main__":
    source_folder = "output/15"  # Source folder with HTML files
    output_folder = "output/16"  # Output folder for Markdown files
    convert_html_to_markdown(source_folder, output_folder)
