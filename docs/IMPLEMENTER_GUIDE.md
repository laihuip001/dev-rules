# Implementer Guide（実装担当ガイド）

> **現場監督（Constructor）向けの完全セットアップガイド**
>
> 最終更新: 2026-01-10

---

## 🎯 このガイドの対象者

- **実装担当（Implementer）**: コード実装、テスト実行、開発日記作成を担当
- 別名: Constructor、現場監督

---

## 🛠️ 環境セットアップ

### 1. 必要なソフトウェア

| ソフトウェア | バージョン | インストール |
|-------------|-----------|-------------|
| Python | 3.10+ | [python.org](https://www.python.org/downloads/) |
| Git | 最新版 | [git-scm.com](https://git-scm.com/) |
| VS Code | 推奨 | [code.visualstudio.com](https://code.visualstudio.com/) |

### 2. リポジトリのクローン

```powershell
# クローン
git clone https://github.com/laihuip001/dev-rules.git
cd dev-rules

# 依存関係インストール
pip install -r requirements.txt
```

### 3. 環境変数の設定

`.env` ファイルを作成（**絶対にGitにコミットしないこと**）:

```env
GEMINI_API_KEY=your_api_key_here
```

> [!CAUTION]
> APIキーは設計担当（Designer）から受け取ってください。
> このファイルは `.gitignore` に含まれているため、自動的にGit管理外になります。

---

## 📝 開発日記の作成

### 日記ツールの実行

```powershell
# dev-rulesディレクトリで実行
cd C:\Users\laihuip001\開発（太郎）\dev-rules

# テスト実行（GitHubへプッシュしない）
python -m src.tools.diary.main --dry-run

# 本番実行（日記生成 + GitHubへ自動プッシュ）
python -m src.tools.diary.main
```

### PowerShellスクリプトでの実行

```powershell
# より簡単に実行
.\run_diary.ps1
```

### 生成される日記の構造

`diary/YYYY-MM-DD.md` に以下が自動生成されます:

| セクション | 内容 |
|-----------|------|
| **Summary** | 今日の作業概要 |
| **File Changes** | 変更ファイル一覧 |
| **Decisions** | 設計判断・意思決定 |
| **Learnings** | 学びや気づき |
| **Next Steps** | 次のアクション |

---

## 🔄 日常業務フロー

### 1. 朝のルーチン

```powershell
# 最新の変更を取得
git pull origin main
```

### 2. 開発作業

1. `src/` 配下でコードを実装
2. `tests/` にテストを追加
3. こまめにコミット

```powershell
git add .
git commit -m "feat: 新機能の実装"
```

### 3. 夕方のルーチン

```powershell
# 開発日記を自動生成
python -m src.tools.diary.main

# または
.\run_diary.ps1
```

---

## 📊 権限について

実装担当が**読み書き可能**なディレクトリ:

| ディレクトリ | 用途 |
|-------------|------|
| `src/` | ソースコード |
| `tests/` | テストコード |
| `diary/` | 開発日記 |
| `docs/` | ドキュメント |
| `shared/knowledge/` | ナレッジベース |

実装担当が**読み取りのみ**のディレクトリ:

| ディレクトリ | 理由 |
|-------------|------|
| `GEMINI.md` | AIペルソナ定義 |
| `constitution/` | 不変ルール層 |
| `ARCHITECTURE.md` | システム構造 |

> [!NOTE]
> これらを変更したい場合は、設計担当（Designer）に提案してください。
> PR/Issueで提案 → レビュー → マージの流れになります。

---

## ❓ トラブルシューティング

### APIキーエラー

```
❌ GEMINI_API_KEY が設定されていません
```

→ `.env` ファイルを確認してください。

### モジュールが見つからない

```
ModuleNotFoundError: No module named 'google.generativeai'
```

→ `pip install google-generativeai` を実行してください。

### Gitプッシュ失敗

```
error: failed to push some refs
```

→ 先に `git pull` してから再度プッシュしてください。

---

## 📚 関連ドキュメント

- [README.md](../README.md) - リポジトリ概要
- [ACCESS_CONTROL.md](ACCESS_CONTROL.md) - 権限ルール詳細
- [src/tools/diary/README.md](../src/tools/diary/README.md) - 日記ツール詳細

---

## 📞 サポート

質問や問題がある場合:

1. GitHub Issueを作成
2. 設計担当（Designer）に連絡
