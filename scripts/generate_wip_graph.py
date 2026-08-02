#!/usr/bin/env python3
"""Generate a WIP knowledge graph HTML for a given month from infographic HTML files."""
import os, re, glob, html
from collections import Counter, defaultdict
from datetime import datetime

def extract_info(filepath):
    """Extract title, subtitle, date from an infographic HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read(5000)  # Only read header section

    basename = os.path.basename(filepath)
    # Extract date prefix from filename (YYYYMMDD)
    date_match = re.match(r'(\d{8})', basename)
    file_date = date_match.group(1) if date_match else '00000000'

    # Extract <title> tag
    title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    raw_title = title_match.group(1).strip() if title_match else basename
    # Clean up title - remove suffixes
    raw_title = re.sub(r'\s*[—–-]\s*AIニュースインフォグラフィック\s*$', '', raw_title)
    raw_title = re.sub(r'\s*\|.*$', '', raw_title)

    # Extract subtitle
    subtitle_match = re.search(r'class="subtitle">(.*?)</div>', content, re.DOTALL)
    subtitle = ''
    if subtitle_match:
        subtitle = re.sub(r'<[^>]+>', '', subtitle_match.group(1)).strip()

    # Extract date from content
    content_date_match = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', content)
    if content_date_match:
        y, m, d = content_date_match.groups()
        file_date = f"{y}{int(m):02d}{int(d):02d}"

    return {
        'filename': basename,
        'date': file_date,
        'title': raw_title,
        'subtitle': subtitle,
    }

def extract_keywords(titles):
    """Extract keywords from article titles."""
    # Common AI/tech terms to look for
    keyword_patterns = [
        r'DeepSeek(?:\s*V?4)?(?:\s*Flash)?', r'Claude(?:\s*\d)?', r'GPT[\d.]+',
        r'Gemini(?:\s*Spark)?', r'Grok(?:\s*Voice)?', r'Kimi(?:\s*K?\d)?',
        r'AI', r'MCP', r'Codex', r'Skills?', r'Agent', r'NotebookLM',
        r'OpenAI', r'Google', r'Anthropic', r'Qoder', r'HiggsField',
        r'Seedance', r'Playwright', r'Firecrawl', r'Obsidian', r'VSCode',
        r'GitHub', r'Canvas', r'GAS', r'OCR', r'YAGNI', r'Ponytail',
        r'Robotics', r'Voice', r'WorldofAI', r'ManuAGI', r'AICodeKing',
        r'まさおAI', r'KEITO', r'あきらパパ', r'ボイスアップラボ',
        r'にゃた', r'コケ先生', r'AI生態士', r'TheWAVE', r'AIエージェンシー',
        r'Opus', r'Sonnet', r'Spark', r'Luna', r'Terra', r'Qwen',
        r'Copilot', r'ChatGPT',
    ]
    
    keyword_counts = Counter()
    article_keywords = {}  # filename -> set of keywords
    
    for info in titles:
        title_text = info['filename'] + ' ' + info['title']
        found = set()
        for pattern in keyword_patterns:
            matches = re.findall(pattern, title_text, re.IGNORECASE)
            for m in matches:
                kw = m.strip()
                if len(kw) >= 2:
                    found.add(kw)
        article_keywords[info['filename']] = found
        for kw in found:
            keyword_counts[kw] += 1
    
    return keyword_counts, article_keywords

def compute_edges(article_keywords):
    """Compute edges between articles that share keywords."""
    edges = 0
    filenames = list(article_keywords.keys())
    for i in range(len(filenames)):
        for j in range(i + 1, len(filenames)):
            shared = article_keywords[filenames[i]] & article_keywords[filenames[j]]
            if shared:
                edges += 1
    return edges

def generate_graph_html(month, articles, keyword_counts, article_keywords):
    """Generate the WIP graph HTML."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    num_articles = len(articles)
    num_edges = compute_edges(article_keywords)
    
    # Sort articles by date then filename
    articles.sort(key=lambda x: (x['date'], x['filename']))
    
    # Group by date
    by_date = defaultdict(list)
    for a in articles:
        by_date[a['date']].append(a)
    
    # Top keywords (max 30)
    top_kws = keyword_counts.most_common(30)
    
    html_parts = []
    html_parts.append(f'''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI News Infographic - 2026年{int(month[4:6])}月 Knowledge Graph (WIP)</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }}
        .stats {{ background-color: #e9ecef; padding: 15px; border-radius: 5px; margin: 20px 0; }}
        .node-list {{ margin: 20px 0; }}
        .node {{ background-color: #f8f9fa; border: 1px solid #dee2e6; padding: 10px; margin: 5px 0; border-radius: 4px; }}
        .node-date {{ font-weight: bold; color: #007bff; margin-top: 15px; }}
        .node-title {{ font-size: 1.1em; margin: 5px 0; }}
        .node-link {{ color: #007bff; text-decoration: none; }}
        .node-link:hover {{ text-decoration: underline; }}
        .edge-info {{ background-color: #e9ecef; padding: 10px; border-radius: 4px; margin: 10px 0; font-size: 0.9em; }}
        .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #dee2e6; color: #6c757d; }}
        .keyword-cloud {{ margin: 15px 0; }}
        .keyword {{ display: inline-block; background: #e3f2fd; color: #1565c0; padding: 2px 8px; margin: 2px; border-radius: 3px; font-size: 0.85em; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>AI News Infographic - 2026年{int(month[4:6])}月 Knowledge Graph (WIP)</h1>
        
        <div class="stats">
            <h2>📊 Graph Statistics</h2>
            <p><strong>Nodes:</strong> {num_articles} articles</p>
            <p><strong>Edges:</strong> {num_edges} connections</p>
            <p><strong>Generated:</strong> {now}</p>
            <p><strong>Status:</strong> <span style="color: orange;">WIP - Work in Progress</span></p>
        </div>
''')

    # Keyword cloud
    if top_kws:
        html_parts.append('<div class="keyword-cloud"><h2>🔗 Top Keywords</h2>')
        for kw, count in top_kws:
            html_parts.append(f'<span class="keyword">{html.escape(kw)} ({count})</span>')
        html_parts.append('</div>')

    # Articles by date
    html_parts.append('<div class="node-list"><h2>📰 Articles by Date</h2>')
    for date in sorted(by_date.keys()):
        html_parts.append(f'<h3 class="node-date">{date}</h3>')
        for a in by_date[date]:
            safe_name = html.escape(a['filename'].replace('.html', ''))
            safe_title = html.escape(a['title'])
            safe_sub = html.escape(a['subtitle']) if a['subtitle'] else ''
            html_parts.append(f'''            <div class="node">
                <div class="node-title"><a class="node-link" href="../{a['filename']}">{safe_name}</a></div>
                <div><small>{safe_sub or safe_title}</small></div>
            </div>
''')
    html_parts.append('</div>')

    # Footer
    html_parts.append(f'''        <div class="footer">
            <p>AI News Infographic Knowledge Graph - Auto-generated WIP</p>
            <p>Generated by Frieren 🌸 at {now}</p>
        </div>
    </div>
</body>
</html>''')

    return '\n'.join(html_parts)

def main():
    import sys
    docs_dir = os.path.expanduser('~/work/ai-news-infographic/docs')
    
    if len(sys.argv) > 1:
        month = sys.argv[1]
    else:
        from datetime import datetime
        month = datetime.now().strftime('%Y%m')
    
    # Find all HTML files for this month
    pattern = os.path.join(docs_dir, f'{month}*.html')
    files = sorted(glob.glob(pattern))
    
    if not files:
        print(f"No HTML files found for month {month}")
        sys.exit(1)
    
    print(f"Found {len(files)} HTML files for {month}")
    
    # Extract info from each file
    articles = []
    for f in files:
        info = extract_info(f)
        articles.append(info)
        print(f"  {info['date']} - {info['title'][:60]}")
    
    # Extract keywords
    keyword_counts, article_keywords = extract_keywords(articles)
    print(f"\nTop keywords: {keyword_counts.most_common(10)}")
    
    # Generate HTML
    graph_html = generate_graph_html(month, articles, keyword_counts, article_keywords)
    
    # Write output
    graph_dir = os.path.join(docs_dir, 'graph')
    os.makedirs(graph_dir, exist_ok=True)
    out_path = os.path.join(graph_dir, f'{month}-wip.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(graph_html)
    
    print(f"\n✅ Generated: {out_path}")
    print(f"   Size: {os.path.getsize(out_path)} bytes")

if __name__ == '__main__':
    main()
