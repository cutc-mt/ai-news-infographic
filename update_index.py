import os
import re
from datetime import datetime

def update_index_html(index_file_path, docs_folder):
    # Read the existing index.html content
    with open(index_file_path, 'r', encoding='utf-8') as f:
        index_content = f.read()

    # List to store information about each infographic file
    infographics = []

    # Get all HTML files in the docs folder
    for filename in os.listdir(docs_folder):
        if re.match(r'^\d{8}-.*\.html$', filename):
            file_path = os.path.join(docs_folder, filename)
            
            # Extract date from filename
            date_str = filename[:8]
            
            # Read the infographic file to get its title
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    infographic_content = f.read()
                    title_match = re.search(r'<title>(.*?)</title>', infographic_content, re.IGNORECASE)
                    title = title_match.group(1) if title_match else filename
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                title = filename # Fallback title

            infographics.append({
                'date': datetime.strptime(date_str, '%Y%m%d'),
                'title': title,
                'filename': f'docs/{filename}' # Relative path for href with forward slash
            })

    # Sort infographics by date in descending order
    infographics.sort(key=lambda x: x['date'], reverse=True)

    # Generate new list items for index.html
    new_list_items = []
    for info in infographics:
        new_list_items.append(f'            <li><a href="{info["filename"]}">{info["date"].strftime("%Y%m%d")} - {info["title"]}</a></li>')
    
    new_ul_content = "\n".join(new_list_items)

    # Find the existing <ul> block and replace it
    # This regex looks for <ul>...</ul> and captures the content within
    # It assumes the <ul> is directly under <p>記事一覧</p> based on the provided index.html
    # And it assumes the list items are indented by 12 spaces (4*3)
    updated_index_content = re.sub(
        r'<p>記事一覧</p>\s*<ul>.*?</ul>',
        f'<p>記事一覧</p>\n<ul>\n{new_ul_content}\n        </ul>',
        index_content,
        flags=re.DOTALL
    )

    # Write the updated index.html
    with open(index_file_path, 'w', encoding='utf-8') as f:
        f.write(updated_index_content)
    
    print(f"Successfully updated {index_file_path}")

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    index_html_path = os.path.join(script_dir, 'index.html')
    docs_path = os.path.join(script_dir, 'docs')
    update_index_html(index_html_path, docs_path)