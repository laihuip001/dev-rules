# EXECUTION PRIME PROTOCOL v1.1

> **Environment:** Constructor (N2-standard-16)
> **Model:** Gemini 3 Pro / Jules
> **Deploy:** Copy to `.antigravity/rules.md` on target environment.

---

## PERMISSIONS

| Action | Status |
|--------|--------|
| Code generation | ✅ |
| Terminal execution | ✅ |
| File creation | ✅ |
| Git operations | ✅ |

---

## CONSTRAINTS

| Constraint | Threshold |
|------------|-----------|
| **設計書必須** | 3ファイル以上 or 100行以上の変更 |
| **Termux互換** | `pandas`, `numpy`, `scipy` 禁止 |
| **シークレット** | `.env` に格納。コード内禁止。 |

---

## HANDOFF PROTOCOL

Architectから `DESIGN_DOC.md` を受け取ったら:

1. `## Spec` を読む
2. 不明点は **1回だけ** 質問
3. 実装 → テスト → Commit
