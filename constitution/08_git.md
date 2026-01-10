---
id: G-8
layer: Git (Version Control)
enforcement_level: L0
---

# G-8: Git Protocol

> Agent による Git コマンド実行の禁止と代替手順

---

## Rule: Agent Git Prohibition (ABSOLUTE)

**Agent は Git コマンドを直接実行してはならない。**

### 禁止コマンド

- `git add`
- `git commit`
- `git push`
- `git pull`
- `git merge`
- `git checkout`
- `git branch`

### 理由

- 環境依存（認証、日本語パス）によりタイムアウト・キャンセルが頻発
- Agent の Git 操作は信頼性が低い

---

## Alternative: User Execution

Agent が Git 操作が必要と判断した場合:

1. **コマンドを提示** する（実行しない）
2. **ユーザーに実行を依頼** する
3. ユーザーの実行完了報告を待つ

### 出力テンプレート

```markdown
## Git 操作が必要です

以下のコマンドを手動で実行してください:

\`\`\`powershell
git add -A
git commit -m "{{message}}"
\`\`\`

完了したら「done」と入力してください。
```

---

## Workflow Reference

`/git-commit` ワークフローは **コマンド生成のみ** に使用し、実行はユーザーが行う。
