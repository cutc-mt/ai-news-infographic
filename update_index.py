import re
import os

docs_dir = 'docs'
try:
    file_list = [f for f in os.listdir(docs_dir) if f.endswith('.html')]
except FileNotFoundError:
    print(f"Error: The directory '{docs_dir}' was not found.")
    exit()

articles = []
for filename in file_list:
    match = re.match(r"(\d{8})-(.*)\.html", filename)
    if match:
        date = match.group(1)
        title = match.group(2).replace('-', ' ')
        articles.append({"date": date, "filename": filename, "title": title})

# Sort by date in descending order
articles.sort(key=lambda x: x["date"], reverse=True)

# Generate the new UL content
new_ul_content = "<ul>\n"
for article in articles:
    new_ul_content += f'            <li><a href="docs/{article["filename"]}">{article["date"]} - {article["title"]}</a></li>\n'
new_ul_content += "        </ul>"

# Read the current index.html content
index_html_path = "index.html"
try:
    with open(index_html_path, 'r', encoding='utf-8') as f:
        current_index_html = f.read()
except FileNotFoundError:
    print(f"Error: '{index_html_path}' not found.")
    exit()


# Replace the old UL with the new UL
# Use re.DOTALL to make '.' match newlines as well
updated_index_html = re.sub(r"<ul>.*?</ul>", new_ul_content, current_index_html, flags=re.DOTALL)

# Write the updated content back to index.html
with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(updated_index_html)

print("index.html updated successfully.")
