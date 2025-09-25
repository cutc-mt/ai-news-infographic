# 本プロジェクトの約束
- 特別な指示がない限りは、ユーザから入力された情報ソースから、@info-graphic-prompt.mdの指示に従って、HTML形式で情報を整理してください。ファイル名には入力された情報ソースにふさわしい名前とprefixとして日時をYYYYMMDD-の形式で付けて下さい。
- ソースが英語や日本語以外の言語であったとしても、作成するインフォグラフィックスは日本語で作成してください。
- `info-graphic-prompt.md`に従ってHTMLファイルを生成した後は、自動的にgit add、commit、pushを実行してください。コミットメッセージは「feat: Add new infographic YYYYMMDD-トピック名」のように、生成したファイル名を含めてください。
- 新しい記事HTMLファイルが生成された後、`index.html`を更新してください。更新内容は以下の通りです。
    1. プロジェクトルートにあるすべての`YYYYMMDD-*.html`形式のファイルをリストアップします。
    2. 各ファイルから日付とタイトルを抽出し、日付の新しい順にソートします。
    3. `index.html`の`<ul>`タグ内に、各記事へのリンクを`<li><a href="ファイル名">タイトル</a></li>`の形式で追加します。
    4. 更新された`index.html`を自動的にgit add、commit、pushを実行してください。コミットメッセージは「feat: Update index.html with new articles」のようにしてください。