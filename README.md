# dev-rules

> **AI-Powered Development Constitution & Prompt Engineering Framework**
>
> A systematic approach to AI-assisted software development.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![AI](https://img.shields.io/badge/AI-Gemini%20%7C%20Claude-green.svg)

---

## 🎯 What is this?

このリポジトリは、**AIエージェント（Gemini/Claude）と協業するための「開発憲法」**です。

| 課題 | このシステムの解決策 |
|------|---------------------|
| AIの出力が一貫しない | Constitution（不変ルール）でガードレールを設定 |
| プロンプトが属人化 | モジュール化されたPrompt Libraryで再利用可能に |
| 開発履歴が追えない | 自動生成される開発日記（Diary）で追跡可能 |

---

## 🎓 What I Learned (このプロジェクトで得た知見)

1. **プロンプトエンジニアリング** - AIへの指示を構造化・モジュール化する技術
2. **Constitution設計** - 「やってはいけないこと」を明文化し、AIの暴走を防ぐ
3. **AI支援開発ワークフロー** - 人間とAIの役割分担（Architect vs Constructor）
4. **ナレッジマネジメント** - 開発中に生まれた知見を体系的に蓄積する方法

## 📘 概要

このリポジトリは、AI駆動の開発ワークフローを統制するためのルールシステムです。

- **Constitution**: 不変の開発ルール（6レイヤー）
- **Prompts**: 再利用可能なプロンプトモジュール（19+）
- **Diary**: 自動生成される開発日記
- **Knowledge**: 共有ナレッジベース

---

## 📂 Directory Structure

```
dev-rules/
├── GEMINI.md              # 🤖 Entry Point - Agent Persona
├── ARCHITECTURE.md        # 📐 System Architecture
├── MANUAL.md              # 📖 Integrated Manual
│
├── constitution/          # 🔒 Immutable Rules (L0-L1)
│   ├── 00_orchestration.md
│   ├── 01_environment.md   # G-1: DMZ
│   ├── 02_logic.md         # G-2: TDD
│   ├── 03_security.md      # G-3: Red Teaming
│   ├── 04_lifecycle.md     # G-4: Rollback
│   ├── 05_meta_cognition.md# G-5: Devil's Advocate
│   └── 06_style.md         # G-6: Code DNA
│
├── prompts/               # 📦 Reusable Modules
├── docs/                  # 📄 Documentation
├── diary/                 # 📝 Development Diary
├── src/                   # 💻 Source Code
└── shared/knowledge/      # 🧠 Knowledge Base
```

---

## 🚀 Quick Start

### 設計担当（Designer / Architect）向け

1. **ルールの確認**

   ```
   GEMINI.md → ARCHITECTURE.md → constitution/
   ```

2. **プロンプト活用**

   ```
   prompts/_index.md で利用可能モジュールを確認
   ```

3. **ワークフロー**

   ```
   /execution-prime  # System Instructions生成
   /inquisitor       # 品質審問
   /prompt-architect # プロンプト監査
   ```

### 実装担当（Implementer / Constructor）向け

1. **開発環境セットアップ**

   ```powershell
   # リポジトリクローン
   git clone https://github.com/laihuip001/dev-rules.git
   cd dev-rules

   # 依存関係インストール
   pip install -r requirements.txt

   # 環境変数設定（.envファイル作成）
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

2. **開発日記の生成**

   ```powershell
   # 日記生成（テスト実行）
   python -m src.tools.diary.main --dry-run

   # 日記生成＋GitHubへプッシュ
   python -m src.tools.diary.main
   ```

3. **コード作業**
   - `src/` 配下で実装
   - `tests/` でテスト追加
   - `diary/` に作業ログを記録（[テンプレート使用](diary/TEMPLATE.md)）

---

## 🔐 権限ルール

| ディレクトリ | Designer | Implementer |
|-------------|:--------:|:-----------:|
| `GEMINI.md`, `constitution/` | ✅ RW | 🔒 R |
| `prompts/` | ✅ RW | 📝 Propose |
| `src/`, `tests/` | 📝 Review | ✅ RW |
| `diary/`, `docs/` | ✅ RW | ✅ RW |

詳細: [docs/ACCESS_CONTROL.md](docs/ACCESS_CONTROL.md)

---

## 📚 主要ドキュメント

| ドキュメント | 概要 |
|-------------|------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | システム全体構造 |
| [MANUAL.md](MANUAL.md) | 統合マニュアル |
| [docs/ACCESS_CONTROL.md](docs/ACCESS_CONTROL.md) | 権限ルール |
| [constitution/_index.md](constitution/_index.md) | Constitution層リファレンス |
| [prompts/_index.md](prompts/_index.md) | プロンプトモジュール一覧 |

---

## 🔧 開発ツール

| ツール | 用途 |
|--------|------|
| `src/tools/diary/` | 開発日記自動生成 |
| `run_diary.ps1` | 日記生成スクリプト（PowerShell） |

---

## 📝 License

MIT License - See [LICENSE](LICENSE) for details.

# Test task 3 - 2026-01-27 20:37
