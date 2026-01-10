# 開発憲法 (Development Constitution)

> 25 modules → 6 files → **3 principles.**

---

## 🎯 3原則

| # | 原則 | 意味 | 関連モジュール |
|---|---|---|---|
| 1 | **Guard** | 大事なものには触らせない | M-01, M-02, M-03 |
| 2 | **Prove** | 動くと言う前にテストで示せ | M-04, M-09, M-11 |
| 3 | **Undo** | 何をしても元に戻せる状態を保て | M-25, M-18 |

---

## 📚 レイヤー構成

| ファイル | レイヤー | 内容 |
|---|---|---|
| [00_orchestration](./00_orchestration.md) | Core | 状態管理、モード、バトラー |
| [01_environment](./01_environment.md) | G-1 Iron Cage | 環境保護、DMZ |
| [02_logic](./02_logic.md) | G-2 Logic Gate | ロジック規約、関数設計 |
| [03_security](./03_security.md) | G-3 Shield | セキュリティ、テスト |
| [04_lifecycle](./04_lifecycle.md) | G-4 Lifecycle | ライフサイクル、ロールバック |
| [05_meta_cognition](./05_meta_cognition.md) | G-5 Meta | メタ認知、自己批判 |
| [06_style](./06_style.md) | G-6 Style (Python) | 型ヒント、命名規則、Docstring |
| [06_style_js](./06_style_js.md) | G-6 Style (JS/GAS) | JavaScript/GAS 向けスタイル |

> *M-19 (Container First) は **Phase 2 のみ** — Termux開発中は保留。

---

## ⚙️ 最適化の記録

- YAML frontmatter (`id:`, `layer:`) による構造化
- XML → Markdown へのフラット化
- アーキテクチャレイヤーごとのグルーピング
- 圧縮率: 26ファイル (~2,200行) → 8ファイル (~700行)

---

## 🔗 関連リソース

| リソース | 場所 |
|---|---|
| AI動作規約 (KERNEL) | [GEMINI.md](../GEMINI.md) |
| AI動作規約 (フル版) | [GEMINI_FULL.md](../GEMINI_FULL.md) |
| 統合マニュアル | [MANUAL.md](../MANUAL.md) |
| システム構造図 | [ARCHITECTURE.md](../ARCHITECTURE.md) |
