# YouTube監視レポート 2026-10-12

## 📺 監視結果（朝の実行）
- 37チャンネル監視、3件POST成功（news_id 7200001〜7200003）
- 自動フィルタ: カレーちゃん1本・No Priors 2本・Julian Goldie 5本が5分未満でスキップ
- 未解決チャンネル警告なし → handle修正不要

## 📺 監視結果（夜の実行・本セッション）
- 37チャンネル監視、4件POST（3新規: 7230001〜7230003、1重複スキップ: 5C1oUBTUv8M）
- 自動フィルタ: カレーちゃん1本・No Priors 1本・Julian Goldie 5本が5分未満でスキップ
- 未解決チャンネル警告なし → handle修正不要
- ⏭️ 5C1oUBTUv8M Daniel「Rekomi Review」は朝の実行で企業PR（#ad sponsored）スキップ判定済みのため対象外

## ✅ 処理結果（夜: 3件生成）
- 7230001 PowGPxsIwlo カレーちゃんのAIニュース「堀井雄二さんがClaudeで作ったゲーム…Math 2.0スライド」
  → docs/20261012_horii_yuji_claude_game_math20_curry.html（commit 59e7048）h2=18・API PUT 200・Pages 200
  - 配色: サンフラワーイエロー #422006→#A16207→#FDE047
- 7230002 nAaPV4pfZpw まさおAIじっくり解説ch「【本音で語る】AI 生成か本質論か」
  → docs/20261012_ai_vs_essence_creator_strategy_masao.html（commit cbb5494）h2=18・API PUT 200・Pages 200
  - 配色: エディトリアル新聞風ライト #FAFAF9/#1C1917/#B91C1C（サイト内唯一のライトテーマ）
- 7230003 -7wdCVCbH7w PIVOT公式チャンネル「【米中AI競争の行方】AIの“暴走”は本当か」
  → docs/20261012_us_china_ai_race_pivot.html（commit 4ed8873）h2=18・API PUT 200・Pages 200
  - 配色: 米中デュアル #111827/#1F2937 + #3B82F6 vs #EF4444

## ✅ 処理結果（朝: 2件生成・1件スキップ）
- 7200001 KKrlXFwvcDo World of AI（現: Universe of AI）「Claude Opus 6 Could Launch Next WEEK」
  → docs/20261012_claude_opus6_launch_worldofai.html（commit 010c5a6）API更新済・Pages 200
- 7200002 -9QRsy2arfM Manu AGI「Trending OSS GitHub Projects #300」
  → docs/20261012_oss_github_projects300_manu.html（commit 9345138）API更新済・Pages 200
- 7200003 5C1oUBTUv8M Daniel | Tech & Data「Rekomi Review (2026)」
  → ⏭️ スキップ: 説明欄に「This video was sponsored by Rekomi」「#ad」＝企業PR動画のため対象外

## 💡 学び
- monitor.shは企業PR動画をフィルタしない（5分未満・Shortsのみ）。PR判定は説明欄の #ad / sponsored 表記で手動判断が必要
- World of AI チャンネルはYouTube上で「Universe of AI」に改名済みだが handle @intheworldofai は有効。ファイル名接尾辞は従来通り worldofai を使用
- video_id がハイフン始まりの場合（-9QRsy2arfM）は fetch_transcript.py に `--` 区切りで渡す
