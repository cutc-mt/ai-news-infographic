import os
import re
from bs4 import BeautifulSoup

def extract_title_and_date(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        title = soup.title.string if soup.title else 'No Title'
        
        # Extract date from filename
        match = re.match(r'\d{8}', os.path.basename(file_path))
        date = match.group(0) if match else '99999999' # Default to a high value to sort last if no date

        return date, title

def update_index_html():
    docs_dir = 'docs'
    articles = []

    # List all YYYYMMDD-*.html files
    for filename in os.listdir(docs_dir):
        if re.match(r'\d{8}-.*\.html', filename):
            file_path = os.path.join(docs_dir, filename)
            date, title = extract_title_and_date(file_path)
            articles.append({'date': date, 'title': title, 'filename': os.path.join(docs_dir, filename)})

    # Sort articles by date in descending order
    articles.sort(key=lambda x: x['date'], reverse=True)

    # Generate new <ul> content
    new_ul_content = []
    for article in articles:
        new_ul_content.append(f'<li><a href="{article["filename"]}">{article["title"]}</a></li>')
    
    new_ul_tag = '<ul>\n' + '\n'.join(new_ul_content) + '\n</ul>'

    # Read existing index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_html_content = f.read()

    # Find and replace the <ul> tag
    soup = BeautifulSoup(index_html_content, 'html.parser')
    
    # Find the existing <ul> tag within the body
    existing_ul = soup.body.find('ul')

    if existing_ul:
        existing_ul.replace_with(BeautifulSoup(new_ul_tag, 'html.parser'))
    else:
        # If no <ul> tag exists, append it after the <p> tag
        p_tag = soup.body.find('p', string='記事一覧')
        if p_tag:
            p_tag.insert_after(BeautifulSoup(new_ul_tag, 'html.parser'))
        else:
            # Fallback: append to body if no specific insertion point
            soup.body.append(BeautifulSoup(new_ul_tag, 'html.parser'))

    # Write updated index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    update_index_html()
