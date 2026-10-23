# 2026-10-16 YouTube監視インフォグラフィック生成（担当2本）

## 担当
- news_id 7560001: Manu AGI「Top Dev Tool Projects」(Qed85xmiaY0)
- news_id 7560002: Daniel | Tech & Data「5 Best FREE AI Detectors (2026)」(QkGXJjlnCfg)

## 完了内容
1. **20261016_dev_tools_ghidra_airllm_manu.html**（26カード）
   - OSS開発ツール20選。Ghidra/airllm/xtool/Shaders/ts-rust/DigUpほか20プロジェクト全網羅
   - 説明欄のGitHub URLで固有名詞補正: 「9-Right-Oaf」→REA (morluto/rea)、「Taleris」→Talorys (rociiu/talorys)、「PenGrub」→Pangram、「SkillsforRealEngineers」→mattpocock/skills、「Birth」はShipyardのデーモン名、「XToolnew/XTooldev」→xtool new/dev
   - 配色: バーガンディ(#6B1230)+焦げ茶オレンジ(#B95518) — 既存12ファイルと重複なし
2. **20261016_free_ai_detectors_daniel.html**（20カード）
   - AI検出器5ツール比較。Clever(S)/GPTZero・Copyleaks・Pangram(A)/ZeroGPT(B)のS/A/B格付け
   - ZeroGPTの100%→29.7%激減実験、スコアバーで視覚化
   - 配色: ディープティール(#155E63)+ベリー(#C05780) — 重複なし
3. セキュリティスキャン: 両ファイル exit 0
4. git push: 2c57687（2ファイル分のコミット）→競合なし1回で成功
5. API PUT: 7560001/7560002ともHTTP 200
6. GitHub Pages: 両URLとも200確認（2回目の試行で反映、約1分）
7. index.html更新+push: 6dff2d7

## 教訓
- 大量のHTMLを一気に書くとタイポが混入する（`<m i`、`上en-name`、`cpu-color`など16箇所）。書いた後必ず html.parser でタグバランス検証＋grepでタイポ扫描が有効
- トランスクリプトの固有名詞はyt-dlpの説明欄取得（`--write-description`）で公式表記を確認してから使う
- fetch_transcript.pyは2本とも成功。browser_navigateの代替は不要だった
