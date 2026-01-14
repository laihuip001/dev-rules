---
description: セッション終了時に開発日記エントリを自動生成・追記する
---

# /diary - 開発日記生成ワークフロー

セッション終了時に、その日の開発作業を自動要約してMarkdown日記として保存する。

## 前提条件

- `GEMINI_API_KEY` 環境変数が設定されていること
- `dev-rules` リポジトリ内で実行すること

## 実行手順

### 1. 環境確認

`dev-rules` リポジトリのルートに移動していることを確認。

### 2. dry-run で内容確認（推奨）

```powershell
// turbo
python -m src.tools.diary.main --dry-run
```

生成される日記の内容を確認する。問題がなければ本実行へ。

### 3. 本実行（日記生成＋GitHubプッシュ）

```powershell
python -m src.tools.diary.main
```

または PowerShell ラッパーを使用：

```powershell
.\run_diary.ps1
```

## 出力

`diary/YYYY-MM-DD.md` に以下の構造で出力：

- **Summary**: 今日の作業概要
- **File Changes**: 変更ファイル一覧
- **Decisions**: 設計判断・意思決定
- **Learnings**: 学びや気づき
- **Next Steps**: 次のアクション

## 別リポジトリの日記生成

```powershell
python -m src.tools.diary.main --target-repo "C:\path\to\other\repo"
```

## トラブルシューティング

| 症状 | 対処 |
|---|---|
| `GEMINI_API_KEY が設定されていません` | `.env` ファイルに `GEMINI_API_KEY=your_key` を追加 |
| `No commits found today` | 当日のコミットがない場合は生成されない |
