# AI News Infographic Generator - Claude Instructions

## プロジェクト概要
YouTube動画からAIニュースのインフォグラフィックHTML（18カード形式）を自動生成し、GitHubにコミット・プッシュするワークフロー。

## 基本ワークフロー
1. ユーザーがYouTube URLを提供
2. `mcp__youtube-transcript__get_video_info` でビデオ情報取得
3. `mcp__youtube-transcript__get_transcript` で文字起こし取得
4. 18カードHTMLインフォグラフィック作成
5. `python update_index.py` でインデックス更新
6. Git add → commit → push

## HTMLファイル命名規則
形式: `docs/YYYYMMDD-{主題}-{キーワード1}-{キーワード2}-{チャンネル名}.html`

例:
- `docs/20260110-OpenCode無料Opus4.5-Antigravity認証-Anthropic規制-AICodeKing.html`
- `docs/20260110-ClaudeCanvas-TUIツールキット-ターミナルUI-メール-カレンダー-WorldofAI.html`

## 日本語スタイルガイドライン ⚠️ 重要

### ❌ 避けるべき不自然な表現（漢字の連続）
```
悪い例:
- "言語Model入力内容Token単位分割処理実行仕組"
- "Feature特徴量指定Target指定自動学習完了"
- "広告費・季節・曜日→売上予測問題設定Example明確提示"
- "Claude Code活用Programming不要誰Model構築可能証明"
```

### ✅ 推奨される自然な日本語表現
```
良い例:
- "言語モデルは入力をトークン単位に分割して処理する仕組み"
- "特徴量とターゲットを指定すると自動で学習が完了"
- "広告費・季節・曜日から売上を予測する問題設定を明確に提示"
- "Claude Codeを活用すればプログラミング不要で誰でもモデル構築が可能"
```

### 自然な日本語のための原則
1. **助詞を適切に使用**: 「は」「が」「を」「に」「で」「と」などを省略しない
2. **ひらがなと漢字のバランス**: 漢字が3-4文字以上連続する場合はひらがなを挟む
3. **カタカナ語は適度に**: モデル、トークン、フィーチャーなどはカタカナで
4. **読点（、）の活用**: 長い文は読点で区切る
5. **体言止めの適度な使用**: 全て体言止めではなく、文末は「です・ます」も混ぜる

### 圧縮表現のガイドライン
情報を圧縮する必要がある場合でも、以下を守る:
- ❌ 「Anthropic規制開始Claude Max締出」
- ✅ 「Anthropicが規制を開始してClaude Maxを締め出し」

- ❌ 「Token化数字距離計算不可」
- ✅ 「トークン化により数字の距離が計算できない」

- ❌ 「Model構築数分LightGBM Install学習即完了」
- ✅ 「モデル構築は数分でLightGBMをインストールして学習が即完了」

### 句読点・記号の使用
- 。（句点）: 文末に必ず付ける
- 、（読点）: 長い文は適度に区切る
- スペース: 単語間に適度にスペースを入れる
- 英数字: 半角を使用

## HTMLテンプレート構造

### カラーテーマ（動画ごとに変更）
各動画に合わせたグラデーションカラーを選択:
```css
:root {
    --color-1: #主色;
    --color-2: #主色の暗め;
    --color-3: #主色の明るめ;
    --color-4: #主色の最暗;
    --color-5: #主色の最明;
}
```

過去の例:
- Purple系: AIニュースまとめ
- Teal系: 開発者ツール
- Green系: オープンソース
- Rose系: プロジェクト管理
- Cyan系: GitHub/開発ツール集
- Orange系: 警告・論争系
- Indigo系: エディタ比較
- Emerald系: データサイエンス・機械学習

### カード構造（18カード）
```html
<div class="card">
    <div class="card-icon"><i class="fas fa-適切なアイコン"></i></div>
    <h2>①タイトル: 要約（日本語として自然に）</h2>
    <p>本文の説明。<span class="highlight">重要ポイント</span>。補足説明や詳細。</p>
</div>
```

### カードタイトルの形式
- `①②③...⑱` の丸数字を使用
- コロン（:）で区切る
- 簡潔で分かりやすく

### highlightクラスの使用
各カードで1-2箇所、最も重要なポイントを`<span class="highlight">`で強調

## Gitコミットメッセージ
```bash
git commit -m "$(cat <<'EOF'
feat: 1個の新しいインフォグラフィック YYYYMMDD

{動画タイトル要約1行}

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

## Font Awesome アイコン選択ガイド
- `fa-exclamation-triangle`: 警告・問題
- `fa-rocket`: 新機能・革新
- `fa-code`: コーディング
- `fa-brain`: AI・学習
- `fa-dollar-sign`: 料金・コスト
- `fa-users`: コミュニティ
- `fa-shield-alt`: セキュリティ・安全性
- `fa-chart-line`: 成長・統計
- `fa-book`: ドキュメント・教育

## 注意事項
- 各動画は独自のカラーテーマを使用（過去の動画と被らないように）
- 18カードすべてを必ず作成
- 動画の内容を網羅的にカバー
- 技術的な正確性を保つ
- **日本語は自然で読みやすく**（最重要）

## 例: 良い日本語表現の実例

### カードタイトル例
- ❌ 「①Anthropic規制開始: Claude Max締出」
- ✅ 「①Anthropicが規制を開始: Claude Maxを締め出し」

- ❌ 「②Token化数字処理: 距離計算不可問題」
- ✅ 「②トークン化による数字処理: 距離計算ができない問題」

### カード本文例
❌ 悪い例（漢字が多すぎて読みにくい）:
```
サードパーティツール利用突然遮断実施。OpenCode・Crush等エラー続出事態。
公式CLI以外認証拒否強制措置発動。$200月額払ってもツール選択不可状態。
開発者コミュニティ炎上激怒混乱発生。
```

✅ 良い例（自然な日本語）:
```
サードパーティツールの利用が突然遮断された。OpenCodeやCrushなどでエラーが続出。
公式CLI以外は認証を拒否する強制措置が発動。月額$200を払ってもツール選択ができない状態に。
開発者コミュニティでは炎上と混乱が発生している。
```

## 実装時のチェックリスト
- [ ] 動画情報と文字起こしを取得
- [ ] 18カードすべて作成
- [ ] 各カードにFont Awesomeアイコン
- [ ] highlightクラスで重要ポイント強調
- [ ] 独自のカラーテーマ適用
- [ ] **日本語が自然で読みやすいか確認** ⚠️
- [ ] update_index.py実行
- [ ] git add, commit, push実行
