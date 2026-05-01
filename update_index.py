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

    # --- Add nav link after <h1> if not already present ---
    nav_html = '<nav style="margin-bottom:2em;">\n  <a href="#knowledge-graph">🧠 ナレッジグラフ</a>\n</nav>'
    if 'id="knowledge-graph"' not in updated_index_content:
        # Insert nav after <h1>
        updated_index_content = updated_index_content.replace(
            '<h1>AI News Infographics</h1>',
            '<h1>AI News Infographics</h1>\n' + nav_html
        )

        # --- Add knowledge graph section after </ul> ---
        graph_section = """
<hr id="knowledge-graph">
<h2>🧠 AIニュースナレッジグラフ</h2>
<p>全インフォグラフィックをグラフ化したナレッジベース（Graphify）</p>
<ul>
  <li><a href="docs/graph/merged-graph.html">統合グラフ（4,331 nodes、〜2026年4月まで）</a></li>
  <li><a href="docs/graph/202509.html">2025年9月</a></li>
  <li><a href="docs/graph/202510.html">2025年10月</a></li>
  <li><a href="docs/graph/202511.html">2025年11月</a></li>
  <li><a href="docs/graph/202512.html">2025年12月</a></li>
  <li><a href="docs/graph/202601.html">2026年1月</a></li>
  <li><a href="docs/graph/202602.html">2026年2月</a></li>
  <li><a href="docs/graph/202603.html">2026年3月</a></li>
  <li><a href="docs/graph/202604.html">2026年4月</a></li>
  <li><a href="docs/graph/202605-wip.html">🔄 2026年5月（暫定版）</a></li>
</ul>
"""
        updated_index_content = updated_index_content.replace(
            '</ul>\n</body>',
            '</ul>\n' + graph_section + '</body>'
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