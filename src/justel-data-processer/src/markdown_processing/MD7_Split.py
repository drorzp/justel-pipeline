import os
import re

def split_content_by_headers(file_content):
    """Split content based on headers into categories."""
    # Regular expressions to identify sections
    title_pattern = re.compile(r"## Titre")
    toc_pattern = re.compile(r"## Table des matières")
    text_pattern = re.compile(r"## Texte")
    
    # Find the positions of each section
    title_pos = title_pattern.search(file_content)
    toc_pos = toc_pattern.search(file_content)
    text_pos = text_pattern.search(file_content)
    
    # Ensure all required headers are found
    if not title_pos or not toc_pos or not text_pos:
        return None, None, None, None
    
    # Extract content for each category
    title_content = file_content[title_pos.start():toc_pos.start()].strip()
    toc_content = file_content[toc_pos.start():text_pos.start()].strip()
    remaining_content = file_content[text_pos.start():].strip()
    
    # Define the headers that indicate the end of the text section
    end_text_section_headers = [
        r"## Signatures",
        r"## Préambule",
        r"## Fiche des modifications",
        r"## Liens",
        r"## Lien externe",
        r"## Liens externes",
        r"## Travaux parlementaires"
    ]
    
    # Create a combined regular expression to find the first occurrence of any of these headers
    combined_pattern = re.compile("|".join(end_text_section_headers))

    # Find the next header that marks the end of the text section
    next_header_match = combined_pattern.search(remaining_content)
    if next_header_match:
        text_content = remaining_content[:next_header_match.start()].strip()
        other_content = remaining_content[next_header_match.start():].strip()
    else:
        text_content = remaining_content.strip()
        other_content = None
    
    return title_content, toc_content, text_content, other_content

def save_content_to_file(content, output_dir, file_name):
    """Save content to a file if content is not None."""
    if content:
        with open(output_dir, 'w', encoding='utf-8') as output_file:
            output_file.write(content)

def process_files_for_splitting(input_dir, base_output_dir):
    """Process all markdown files in the input directory to split and categorize content."""
    # Define sub-folder names and paths
    subfolders = {
        'Titles': '1. Titles',
        'Tables of Contents': '2. Tables of Contents',
        'Texts': '3. Texts',
        'Other': '4. Other'
    }
    
    # Create sub-folders if they don't exist
    for subfolder in subfolders.values():
        subfolder_path = os.path.join(base_output_dir, subfolder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
    
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.md'):
            input_file_path = os.path.join(input_dir, file_name)

            try:
                with open(input_file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()

                # Split the content into categories
                title_content, toc_content, text_content, other_content = split_content_by_headers(file_content)
                
                if title_content is None or toc_content is None or text_content is None:
                    print(f"Skipping {file_name}: Required headers not found.")
                    continue

                # Save the split content into corresponding sub-folders
                save_content_to_file(title_content, os.path.join(base_output_dir, subfolders['Titles'], file_name), file_name)
                save_content_to_file(toc_content, os.path.join(base_output_dir, subfolders['Tables of Contents'], file_name), file_name)
                save_content_to_file(text_content, os.path.join(base_output_dir, subfolders['Texts'], file_name), file_name)
                if other_content:
                    save_content_to_file(other_content, os.path.join(base_output_dir, subfolders['Other'], file_name), file_name)

                print(f"Processed {file_name} successfully.")

            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")

if __name__ == "__main__":
    # Define input and output directories
    input_dir = "output/22"  # Directory containing markdown files
    base_output_dir = "output/MD7_split"

    # Run the splitting function
    process_files_for_splitting(input_dir, base_output_dir)
