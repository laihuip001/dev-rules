# 開発美学規範 (Aesthetic Development Standard)

> **Codename:** Elegance Protocol
> **Version:** 1.0
> **Applies to:** All artifacts, configs, and documentation in this project.

---

## 🍎 Core Principles (Apple/PRADA Aesthetic)

### 1. Radical Simplicity

- **本質以外は削れ。** 1行削除して意味が変わらなければ、その行は不要。
- **説明するな、制約せよ。** Good/Bad例は不要。禁止パターンだけ示せ。

### 2. Cognitive Fluency

- **3秒ルール:** ドキュメントを開いて3秒で目的がわかるか？
- **Tier構造:** 情報は重要度で階層化。全件フラットに並べるな。

### 3. Hidden Complexity

- **メタ情報は分離:** `_comment`, `_verification` は設定ファイルから追い出せ。
- **設定ファイルはクリーン:** 実行時に参照されないデータを混ぜるな。

### 4. Plain Language (脱・専門用語)

- **中学生にわかる言葉で:** 専門用語（Jargon）は禁止。
- **翻訳責任:** "Deploy" ではなく "配置"。"Commit" ではなく "記録"。概念言葉を使うな。

---

## 🚫 Forbidden Anti-Patterns

| Anti-Pattern | Example | Fix |
|--------------|---------|-----|
| **説明書的記述** | 「これがGoodでこれがBad」 | Badだけ残す |
| **フラットリスト** | 252行のファイル一覧 | Tier分類 + 1行要約 |
| **冗長なセクション** | `## はじめに`, `## まとめ` | 削除 |
| **実行時不要なメタ** | JSON内の `_comment` | 別ファイルへ |

---

## ✅ Verification Checklist

Before committing any artifact, ask:

1. [ ] **削れる行はないか？** (Radical Simplicity)
2. [ ] **3秒で目的がわかるか？** (Cognitive Fluency)
3. [ ] **メタ情報が混在していないか？** (Hidden Complexity)
4. [ ] **Tier構造は適切か？** (Information Architecture)

---

**This standard is the law.**
