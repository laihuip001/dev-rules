---
id: G-9
layer: Architecture (Structure)
version: "1.0"
---

# G-9: ファイル構成規約

> 構造が**意図を語る**。ファイルを見れば設計が分かる状態を保て。

---

## 1. 基本ディレクトリ構造

### Python プロジェクト

```
project/
├── src/                    # ソースコード
│   ├── core/               # ビジネスロジック
│   ├── api/                # API エンドポイント
│   └── utils/              # 共通ユーティリティ
├── tests/                  # テストコード
│   ├── fixtures/           # テストデータ
│   └── test_*.py
├── docs/                   # ドキュメント
├── .github/                # GitHub設定
│   └── workflows/          # CI/CD
├── .gitignore
├── pyproject.toml          # 依存関係・設定
├── requirements.txt        # 依存関係（互換用）
└── README.md
```

### GAS プロジェクト

```
project/
├── automation/
│   └── gas/
│       ├── config.gs       # 設定（秘密情報）
│       ├── main.gs         # メイン処理
│       └── utils.gs        # ユーティリティ
├── docs/
│   ├── manual/             # 運用マニュアル
│   └── decisions/          # 意思決定記録
└── README.md
```

---

## 2. ファイル配置ルール

### ✅ Do

| ファイル種別 | 配置場所 | 理由 |
|---|---|---|
| ビジネスロジック | `src/core/` | 中心的な価値をここに集約 |
| 外部連携 | `src/api/`, `src/integrations/` | 境界を明確に |
| 設定ファイル | プロジェクトルート | 発見しやすく |
| テスト | `tests/` | 本番コードと分離 |
| ドキュメント | `docs/` | 一箇所に集約 |

### ⛔ Don't

| アンチパターン | 問題 |
|---|---|
| `src/helpers.py` (巨大) | 責務不明確、何でも入れがち |
| `src/utils/misc.py` | 名前が曖昧、整理放棄 |
| `テスト.py` (日本語) | パス問題、互換性リスク |
| ネストが5階層超 | ナビゲーションコスト増大、パス長制限リスク |

> [!TIP]
> **なぜ5階層まで？** 人間が「あのファイルどこだっけ」と迷わずに辿れる限界。また、Windows のパス長制限 (260文字) に近づくリスクも増す。

---

## 3. 命名規則

### ディレクトリ名

| 規約 | 例 |
|---|---|
| 小文字 + アンダースコア | `user_management/`, `api_client/` |
| 複数形は内容による | `utils/` (単一責務), `handlers/` (複数ハンドラ) |

### ファイル名

| 言語 | 規約 | 例 |
|---|---|---|
| Python | `snake_case.py` | `user_repository.py` |
| JavaScript | `camelCase.js` または `PascalCase.js` (クラス) | `fileProcessor.js` |
| Markdown | `UPPER_CASE.md` または `kebab-case.md` | `README.md`, `setup-guide.md` |

---

## 4. モジュール分割基準

> **単一責任の原則**: 1ファイル = 1つの責務

### 分割タイミング

| 条件 | アクション |
|---|---|
| 300行を超えた | 分割を検討 |
| 複数の概念が混在 | 概念ごとに分割 |
| テストが書きにくい | 依存関係を整理して分割 |
| import が10個以上 | 責務過多、分割 |

### 分割例

```
# Before: 巨大な1ファイル
sync_to_github.gs (500行)

# After: 責務ごとに分割
sync_to_github.gs  (メイン処理, 50行)
├── scanner.gs     (フォルダスキャン, 80行)
├── parser.gs      (ファイル名パース, 60行)
├── markdown.gs    (Markdown生成, 70行)
├── github.gs      (GitHub API連携, 100行)
└── notify.gs      (通知処理, 40行)
```

---

## 5. 特殊ディレクトリ

| ディレクトリ | 用途 | 注意 |
|---|---|---|
| `.github/` | GitHub固有設定 | Actions, テンプレート |
| `.vscode/` | エディタ設定 | 共有すべきもののみコミット |
| `__pycache__/` | Pythonキャッシュ | .gitignore必須 |
| `node_modules/` | npm依存 | .gitignore必須 |
| `dist/`, `build/` | ビルド成果物 | .gitignore推奨 |

---

## 6. ドキュメント配置

```
docs/
├── README.md              # プロジェクト概要
├── CONTEXT.md             # 前提条件・制約
├── manual/                # 運用マニュアル
│   └── 利用者向け.md
├── decisions/             # 意思決定記録 (ADR)
│   ├── 000-template.md
│   └── 001-automation-platform.md
└── api/                   # API仕様
    └── endpoints.md
```

---

## 7. Living Samples

| 用途 | 参照 | 模倣ポイント |
|---|---|---|
| Python構造 | `dev-rules/src/` | core/tools分離 |
| GAS構造 | `現場連携Template/automation/gas/` | config分離 |
| ドキュメント | `現場連携Template/docs/` | CONTEXT + decisions |

> [!IMPORTANT]
> Living Sample への変更はレビュー必須。
