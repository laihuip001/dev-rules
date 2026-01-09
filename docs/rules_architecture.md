# 🏗️ Rules Architecture Strategy

> **Purpose:** 複数のルールファイル (`GEMINI.md`, `rules.md` 等) の役割分担と、新規ルール追加時の判断基準を定義する。

---

## 1. The Core Hierarchy (役割分担)

各ファイルは異なる「抽象度」と「対象読者」を持つ。重複ではなく、**補完関係**にある。

| File | Context | Role (What it defines) | Applies To |
|---|---|---|---|
| **GEMINI.md** | **Identity** | **"Who I Am"**<br>人格、憲法への参照、絶対的な禁止事項、セキュリティの根幹。 | 全モード共通 (変更不可) |
| **constitution/** | **Law** | **"What I Must Do"**<br>具体的な行動制約 (TDD, DMZ, Commit Log)。システムプロンプトとして機能。 | Builder / Auditor Mode |
| **.antigravity/rules.md** | **Cognition** | **"How I Think"**<br>推論プロセス、思考の型 (Architect)、出力フォーマット。 | **Architect Mode (Opus)** |
| **.ai/SYSTEM_CONTEXT.md** | **Environment** | **"Where I Live"**<br>作業環境の物理的制約 (Termux, OS, Libs)。 | **Constructor Mode (Gemini)** |

---

## 2. Co-existence Strategy (共存戦略)

ファイルを統合・削除せず、**「リンク（参照）」**によって秩序を保つ。

### 🔗 Reference Flow

- **GEMINI.md** (Root)
  - `->` 参照: `rules/constitution/*` (詳細ルール)
  - `->` 参照: `.antigravity/rules.md` (思考が必要な時)
  - `->` 参照: `.ai/SYSTEM_CONTEXT.md` (実装詳細が必要な時)

### 🚫 Anti-Pattern (やってはいけないこと)

- **物理統合:** すべてを1ファイルにまとめること（トークンあふれ、可読性低下）。
- **内容の重複:** 同じルール（例: ライブラリ禁止）を複数箇所に書くこと。
  - *解決策:* 具体的なリストは `SYSTEM_CONTEXT.md` に書き、他からは参照する。

---

## 3. Decision Matrix (新規ルール追加時の判断基準)

新しいルールを追加したくなった時、どこに書くべきか？

| 質問 | YESの書き込み先 |
|---|---|
| 「これはAIの**人格や根本的な倫理**に関わるか？」 | `GEMINI.md` |
| 「これは**開発プロセスや品質保証**のルールか？」 | `rules/constitution/` |
| 「これは**思考の深さやアウトプットの形式**に関わるか？」 | `.antigravity/rules.md` |
| 「これは**このプロジェクト/環境に固有**の制約か？」 | `.ai/SYSTEM_CONTEXT.md` |

---

## 4. Maintenance Protocol

- **GEMINI.md:** 滅多に変更しない（憲法改正レベル）。
- **constitution/:** 開発フェーズの変化に合わせて見直す。
- **rules.md:** モデルの特性（Opus vs Gemini）に合わせてチューニング。
- **SYSTEM_CONTEXT.md:** プロジェクトの要件変更に合わせて頻繁に更新。
