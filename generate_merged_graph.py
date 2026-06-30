#!/usr/bin/env python3
"""Generate the AI News Infographic merged graph HTML."""
import os
import json

CARD_TEMPLATE = """
<div class="card fi">
    <div class="icon-box"><i class="{icon} fa-5x" style="color:var(--c{color});{anim}"></i><h2>{num} {title}</h2></div>
    <div class="cc"><ul class="kl">{items}</ul>{bubble}</div>
</div>"""

ITEM_TEMPLATE = '<li><i class="{icon}"></i><span>{text}</span></li>'

BUBBLE_TEMPLATE = '<div class="bub{variant}"><span class="hw"><i class="{icon}" style="color:var(--c{color})"></i> {text}</span></div>'
BUBBLE_TOP = '<div class="bub{variant} t"><span class="hw"><i class="{icon}" style="color:var(--c{color})"></i> {text}</span></div>'
BUBBLE_RIGHT = '<div class="bub{variant} r"><span class="hw"><i class="{icon}" style="color:var(--c{color})"></i> {text}</span></div>'

def get_color_for_community(community):
    """Get color based on community number"""
    colors = [1, 2, 3, 4, 5, 6, 7, 8]
    return colors[community % len(colors)]

def get_icon_for_file_type(file_type):
    """Get icon based on file type"""
    icon_map = {
        "code": "fa-solid fa-code",
        "news": "fa-solid fa-newspaper",
        "agent": "fa-solid fa-robot",
        "architecture": "fa-solid fa-sitemap",
        "service": "fa-solid fa-cloud"
    }
    return icon_map.get(file_type, "fa-solid fa-circle")

# Read the merged graph JSON
graph_file = os.path.join(os.path.dirname(__file__), 'graphify-merged', 'merged-graph.json')
if os.path.exists(graph_file):
    with open(graph_file, 'r', encoding='utf-8') as f:
        graph_data = json.load(f)
else:
    graph_data = {"nodes": [], "links": []}

cards = []

for node in graph_data['nodes']:
    community = node.get('community', 0)
    file_type = node.get('file_type', 'unknown')
    
    # Generate items based on node information
    items = [
        (get_icon_for_file_type(file_type), f"Type: {file_type}"),
        ("fa-solid fa-users", f"Community: {community}"),
        ("fa-solid fa-tag", f"ID: {node.get('id', 'N/A')}")
    ]
    
    # Add related nodes information
    related_count = len([link for link in graph_data['links'] 
                       if link.get('source') == node.get('id') or link.get('target') == node.get('id')])
    items.append(("fa-solid fa-link", f"Connections: {related_count}"))
    
    card = {
        "icon": get_icon_for_file_type(file_type),
        "color": get_color_for_community(community),
        "anim": "",
        "num": f"#{len(cards) + 1}",
        "title": node['label'],
        "items": items,
        "bubble": "",
        "bubble_icon": "fa-solid fa-info-circle",
        "bubble_color": get_color_for_community(community),
        "bubble_variant": ""
    }
    cards.append(card)

# HTML generation
html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI News Infographic - Merged Graph 2026年6月</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ 
            background: #0a0a0a; 
            color: #ffffff; 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; 
            padding: 20px; 
            line-height: 1.6;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{ text-align: center; margin-bottom: 40px; color: #4ecdc4; font-size: 2.5em; }}
        .cards-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 20px; margin-bottom: 40px; }}
        .card {{ 
            background: #1a1a1a; 
            border: 1px solid #333; 
            border-radius: 12px; 
            padding: 20px; 
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 30px rgba(78, 205, 196, 0.3); }}
        .icon-box {{ text-align: center; margin-bottom: 15px; }}
        .icon-box i {{ margin-bottom: 10px; }}
        .icon-box h2 {{ font-size: 1.5em; margin: 0; color: #ffffff; }}
        .cc {{ padding: 0; }}
        .kl {{ list-style: none; padding: 0; margin: 0; }}
        .kl li {{ 
            display: flex; 
            align-items: center; 
            padding: 8px 0; 
            border-bottom: 1px solid #2a2a2a;
        }}
        .kl li:last-child {{ border-bottom: none; }}
        .kl li i {{ margin-right: 10px; width: 16px; }}
        .kl li span {{ flex: 1; }}
        .bub {{ 
            background: rgba(78, 205, 196, 0.1); 
            border: 1px solid rgba(78, 205, 196, 0.3); 
            border-radius: 8px; 
            margin-top: 15px; 
            padding: 12px;
        }}
        .bub .hw {{ display: flex; align-items: center; }}
        .bub .hw i {{ margin-right: 8px; }}
        .bub.t {{ text-align: center; }}
        .bub.r {{ text-align: right; }}
        .tag {{ background: #4ecdc4; color: #000; padding: 2px 6px; border-radius: 4px; font-size: 0.8em; font-weight: bold; }}
        .hl {{ color: #ffd93d; font-weight: bold; }}
        .stats {{ background: #1a1a1a; border-radius: 8px; padding: 20px; margin-top: 20px; }}
        .stats h3 {{ color: #4ecdc4; margin-bottom: 15px; }}
        .stat-item {{ display: flex; justify-content: space-between; margin-bottom: 10px; padding-bottom: 10px; border-bottom: 1px solid #333; }}
        .stat-item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 AI News Infographic - 2026年6月マージグラフ</h1>
        
        <div class="stats">
            <h3>📊 グラフ統計</h3>
            <div class="stat-item">
                <span>ノード数:</span>
                <span>{len(graph_data['nodes'])}</span>
            </div>
            <div class="stat-item">
                <span>エッジ数:</span>
                <span>{len(graph_data['links'])}</span>
            </div>
            <div class="stat-item">
                <span>コミュニティ数:</span>
                <span>{len(set(node.get('community', 0) for node in graph_data['nodes']))}</span>
            </div>
        </div>
        
        <div class="cards-grid">
"""

# Add cards to HTML
for card in cards:
    html_content += "            " + CARD_TEMPLATE.format(**card) + "\n"
    
    # Add items
    for item_icon, item_text in card["items"]:
        html_content += "                " + ITEM_TEMPLATE.format(icon=item_icon, text=item_text) + "\n"
    
    # Add bubble
    if card["bubble"]:
        bubble_content = BUBBLE_TEMPLATE.format(
            variant=card["bubble"]["variant"],
            icon=card["bubble"]["icon"],
            color=card["bubble"]["color"],
            text=card["bubble"]["text"]
        )
        html_content += "                " + bubble_content + "\n"
    
    html_content += "        </div>\n"

html_content += """        <div style="text-align: center; margin-top: 40px; padding: 20px; background: #1a1a1a; border-radius: 8px;">
            <p style="color: #4ecdc4; margin-bottom: 10px;">
                <i class="fas fa-calendar"></i> 生成日時: 2026年7月1日
            </p>
            <p style="color: #888; font-size: 0.9em;">
                AIニュースインフォグラフィック - 2026年6月のナレッジグラフ統合版
            </p>
        </div>
    </div>
</body>
</html>"""

# Write the HTML file
output_file = os.path.join(os.path.dirname(__file__), 'graphify-merged', 'merged-graph.html')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated merged graph HTML: {output_file}")
print(f"Total nodes: {len(graph_data['nodes'])}")
print(f"Total links: {len(graph_data['links'])}")