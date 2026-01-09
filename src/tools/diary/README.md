# Development Diary Tool

その日の開発作業を自動要約し、Markdown日記として保存するツール。

## Features

- 📊 Git履歴から当日のコミットを収集
- 🤖 Gemini APIで自動要約
- 📝 構造化されたMarkdown日記を生成
- 📤 自動でGitにコミット・プッシュ

## Usage

```bash
# dev-rulesリポジトリ内で実行
cd C:\Users\laihuip001\開発（太郎）\dev-rules

# 日記生成（プッシュなし）
python -m src.tools.diary.main --dry-run

# 日記生成＋GitHubへプッシュ
python -m src.tools.diary.main

# 別リポジトリの日記を生成
python -m src.tools.diary.main --target-repo "C:\path\to\other\repo"
```

## Requirements

- Python 3.10+
- Git
- `google-generativeai` (Gemini API)

```bash
pip install google-generativeai
```

## Environment Variables

- `GEMINI_API_KEY`: Gemini APIキー（必須）

## Output

`diary/YYYY-MM-DD.md` に以下の構造で出力:

- **Summary**: 今日の作業概要
- **File Changes**: 変更ファイル一覧
- **Decisions**: 設計判断・意思決定
- **Learnings**: 学びや気づき
- **Next Steps**: 次のアクション

## GitHub Links

- Repository: https://github.com/laihuip001/dev-rules
