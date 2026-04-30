#!/bin/bash
# Graphify: 月別分割 → グラフ化 → 順次マージ
# 使い方: bash graphify-merge.sh

set -e
BASE=~/work/ai-news-infographic/docs
OUT=~/work/ai-news-infographic/docs/graphify-out-monthly
MERGED=$OUT/merged-graph.json
mkdir -p "$OUT"

MONTHS=(202509 202510 202511 202512 202601 202602 202603 202604)
TEMP_FIRST=""

echo "=== Graphify Monthly Merge Pipeline ==="

for i in "${!MONTHS[@]}"; do
  MONTH="${MONTHS[$i]}"
  COUNT=$(ls "$BASE"/${MONTH}*.html 2>/dev/null | wc -l)
  if [ "$COUNT" -eq 0 ]; then
    echo "[$MONTH] No files, skipping."
    continue
  fi

  MONTH_DIR="$OUT/monthly-$MONTH"
  echo ""
  echo "━━━ [$((i+1))/${#MONTHS[@]}] $MONTH ($COUNT files) ━━━"

  # Create temp dir with symlinks for this month
  mkdir -p "$MONTH_DIR"
  ln -sf "$BASE"/${MONTH}*.html "$MONTH_DIR/" 2>/dev/null || true

  # Clean previous graphify output
  rm -rf "$MONTH_DIR/graphify-out"

  # Run graphify via Claude Code
  echo "  Running /graphify on $MONTH ..."
  cd "$MONTH_DIR"
  claude -p --dangerously-skip-permissions "/graphify ." 2>&1 | tail -3

  GRAPH_JSON="$MONTH_DIR/graphify-out/graph.json"
  if [ ! -f "$GRAPH_JSON" ]; then
    echo "  ⚠️  graph.json not found for $MONTH, skipping merge."
    continue
  fi

  # Merge: first month = base, subsequent = merge
  if [ -z "$TEMP_FIRST" ]; then
    cp "$GRAPH_JSON" "$MERGED"
    TEMP_FIRST="done"
    echo "  ✅ Set as base graph"
  else
    echo "  Merging into combined graph..."
    graphify merge-graphs "$MERGED" "$GRAPH_JSON" --out "$MERGED" 2>&1 | tail -2
    echo "  ✅ Merged"
  fi

  # Cleanup symlinks to save space
  rm -f "$MONTH_DIR"/*.html
  echo "  Disk cleaned."
done

echo ""
echo "=== Done! ==="
echo "Merged graph: $MERGED"
echo ""
echo "To generate report & HTML from merged graph:"
echo "  graphify cluster-only $MERGED"
echo "  # then check $OUT/ for output"

# Final: regenerate report from merged graph
if [ -f "$MERGED" ]; then
  echo ""
  echo "Generating final report..."
  cd "$OUT"
  graphify cluster-only "$MERGED" 2>&1 | tail -3
  echo "✅ Final graph.html + GRAPH_REPORT.md in $OUT/"
fi
