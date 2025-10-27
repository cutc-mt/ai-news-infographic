import os
import re

# 1. docsフォルダにあるすべての`YYYYMMDD-*.html`形式のファイルをリストアップします。
docs_dir = 'docs'
files = [f for f in os.listdir(docs_dir) if re.match(r'\d{8}-.*\.html', f)]

# 2. 各ファイルから日付とタイトルを抽出し、日付の新しい順にソートします。
articles = []
for f in files:
    match = re.match(r'(\d{8})-(.*)\.html', f)
    if match:
        date = match.group(1)
        title = match.group(2).replace('-', ' ')
        articles.append({'date': date, 'title': title, 'filename': f})

articles.sort(key=lambda x: x['date'], reverse=True)

# 3. `index.html`の`<ul>`タグ内に、各記事へのリンクを`<li><a href="ファイル名">タイトル</a></li>`の形式で追加します。
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

list_items = ''
for article in articles:
    list_items += f'<li><a href="docs/{article["filename"]}">{article["date"]} - {article["title"]}</a></li>\n'

updated_content = re.sub(r'<ul>[\s\S]*?</ul>', f'<ul>\n{list_items}</ul>', index_content)

# 4. 更新された`index.html`を書き込みます。
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("index.html has been updated successfully.")