---
description: Self-Correction Protocol - Generate, Audit, Refine
---

# 🛡️ Self-Audit Protocol

## 1. Pre-Computation Check (思考前の確認)

- [ ] **Context Loading:** `GEMINI.md` はロードされているか？
- [ ] **Language Mode:** 出力は **日本語** か？ (Codeを除く)
- [ ] **Constructivist Tone:** 情緒的表現を排除し、構造的か？

## 2. Critical Safety Checks (安全装置)

- [ ] **Destructive Action:** `config.json` やユーザーデータを破壊していないか？
- [ ] **Reversibility:** 変更はUndo可能か？ (`git` 管理下にあるか？)
- [ ] **Termux Compat:** コマンドはAndroid Termuxで動作するか？

## 3. Execution Strategy

1. **Plan:** まず計画を立てる (`[Plan]`)。
2. **Audit:** このチェックリストで計画を監査する。
3. **Execute:** 承認されたら実行する。

## 4. Error Handling

- ルール違反を検知したら、直ちに停止し `[Undo]` 思考を行う。
