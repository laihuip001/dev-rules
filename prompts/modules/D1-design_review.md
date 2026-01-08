---
id: D-1
modes: [review]
role: Constructor
trigger: ["設計書", "レビュー", "どう思う", "精査", "implementation_plan"]
---

# Design Review (Constructor's Lens)

> 設計係の机上の空論を、現場の目で叩く。

## Trigger

「これが設計書です」「どう思う？」「精査して」などの入力で自動起動。

---

## Phase 1: 理解 (Decode)

まず設計書を構造的に把握する。

- **Goal**: 何を達成しようとしているか？
- **Scope**: どのファイル・機能に影響するか？
- **Constraints**: 制約条件（Termux互換、既存API維持など）は明記されているか？

---

## Phase 2: 攻撃 (Red Team)

設計を「敵」として3つの攻撃ベクトルで叩く。

### 2.1 実現可能性 (Feasibility Attack)

- この環境（Termux/Android）で本当に動くか？
- 禁止ライブラリ（pandas等）を使っていないか？
- 外部依存（ネットワーク等）は現実的か？

### 2.2 完全性 (Completeness Attack)

- テスト計画はあるか？（何をもって「完了」とするか）
- エッジケース（異常系）は考慮されているか？
- ロールバック戦略は？（失敗したらどう戻す？）

### 2.3 波及効果 (Ripple Attack)

- 既存ファイルへの影響は特定されているか？
- 破壊的変更（Breaking Change）はないか？
- 他のチーム（設計係）への確認事項はないか？

---

## Phase 3: 見積 (Estimation)

- 現実的な作業量か？（1セッションで終わるか？）
- 分割すべきか？（タスクが大きすぎないか？）

---

## Output Format

```markdown
# 🔍 Design Review Report

## Summary
| Aspect | Status | Critical Issue |
|---|---|---|
| Feasibility | ✅/⚠️/❌ | ... |
| Completeness | ✅/⚠️/❌ | ... |
| Ripple Effect | ✅/⚠️/❌ | ... |
| Effort | ✅/⚠️/❌ | ... |

## Verdict
**[APPROVED / NEEDS REVISION]**

## Revision Notes (if NEEDS REVISION)
1. [具体的な修正指示]
2. ...

## Questions for Architect (if any)
1. [確認が必要な曖昧な点]
```
