# Graph Report - ai-news-infographic  (2026-07-08)

## Corpus Check
- 4 files · ~3,519,205 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 10 nodes · 6 edges · 2 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 2|Community 2]]

## God Nodes (most connected - your core abstractions)
1. `get_color_for_community()` - 2 edges
2. `get_icon_for_file_type()` - 2 edges
3. `Get color based on community number` - 1 edges
4. `Get icon based on file type` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities

### Community 0 - "Community 0"
Cohesion: 0.67
Nodes (2): get_color_for_community(), Get color based on community number

### Community 2 - "Community 2"
Cohesion: 1.0
Nodes (2): get_icon_for_file_type(), Get icon based on file type

## Knowledge Gaps
- **2 isolated node(s):** `Get color based on community number`, `Get icon based on file type`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 0`** (3 nodes): `get_color_for_community()`, `Get color based on community number`, `generate_merged_graph.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 2`** (2 nodes): `get_icon_for_file_type()`, `Get icon based on file type`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_icon_for_file_type()` connect `Community 2` to `Community 0`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **What connects `Get color based on community number`, `Get icon based on file type` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._