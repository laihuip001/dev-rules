# dev-rules - 開発規範モジュール

> **Titanium Strategist** - 全プロジェクト共通の開発規範

---

## 概要

このリポジトリは、AI支援開発における共通ルール・プロンプトモジュールを提供します。

---

## ⚠️ 配置要件（必須）

このリポジトリは以下のパスにクローンすること:

```
C:\Users\makaron8426\dev\dev-rules
```

**理由:** グローバル設定（`.gemini/GEMINI.md`）が上記パスを参照する二段階ロック構造を採用しているため。

```
.gemini/GEMINI.md (KERNEL_LOCK)
    ↓ view_file で参照
C:\Users\makaron8426\dev\dev-rules\GEMINI.md (詳細ルール)
```

---

## 利用方法

### 1. グローバル設定（推奨）

`~/.gemini/GEMINI.md` を本リポジトリの `GEMINI.md` にリンク:

```powershell
# Windows (ハードリンク)
cmd /c mklink /H "%USERPROFILE%\.gemini\GEMINI.md" "path\to\dev-rules\GEMINI.md"
```

### 2. プロジェクト固有ルール

各プロジェクトの `.gemini/rules.md` にプロジェクト固有ルールを記載。
共通ルールは自動的に適用されます。

### 3. プロンプトモジュール参照

`/load` ワークフローでモジュールをロード:

```
/load G-3        # Securityレイヤー
/load C-4-5      # Code Audit/Fix
```

---

## ディレクトリ構成

| パス | 内容 |
|------|------|
| `GEMINI.md` | エントリポイント（v3.1.0） |
| `constitution/` | 不変ルール（G-1〜G-7） |
| `prompts/modules/` | プロンプトモジュール（21件） |
| `.agent/workflows/` | ワークフロー定義 |

---

## 主要ドキュメント

- [GEMINI.md](./GEMINI.md) - Agent Persona
- [ARCHITECTURE.md](./ARCHITECTURE.md) - システム構造
- [MANUAL.md](./MANUAL.md) - 統合マニュアル
- [prompts/_index.md](./prompts/_index.md) - モジュールカタログ

---

## ライセンス

Private - Internal Use Only
