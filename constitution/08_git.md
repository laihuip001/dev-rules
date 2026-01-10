---
id: G-8
layer: Shell (Command Execution)
enforcement_level: L0
---

# G-8: Shell Command Protocol

> Agent による破壊的シェルコマンドおよび Git コマンドの直接実行禁止

---

## Rule: Automated Execution Prohibition (ABSOLUTE)

**Agent は以下のカテゴリに属するコマンドを `run_command` で自動実行してはならない。**

### 1. Version Control (Git)

- `git add`, `commit`, `push`, `pull`, `merge`, `checkout`, `branch`
- **理由:** 環境依存（認証、日本語パス）エラー、コンフリクト時の制御不能リスク

### 2. Destructive Operations (File System)

- `rm`, `del`, `Remove-Item` (特に `-Recurse`, `-Force`)
- `mv`, `Move-Item` (大量のファイル移動を伴う場合)
- **理由:** 誤削除時の復旧困難性（Undo 原則の侵害）

---

## Protocol: User Execution Request

該当コマンドの実行が必要な場合、以下の手順を踏むこと:

1. **コマンドを生成・提示** する（実行しない）
2. **目的とリスク** を説明する
3. **ユーザーに実行を依頼** する

### 出力テンプレート

```markdown
## ⚠️ 手動操作が必要です (G-8 Protocol)

以下のコマンドを手動で実行してください:

### Git 操作
\`\`\`powershell
git add -A
git commit -m "{{message}}"
\`\`\`

### ファイル削除
\`\`\`powershell
# {{対象}} を削除
Get-ChildItem -Path "{{path}}" ... | Remove-Item ...
\`\`\`

完了したら「done」と入力してください。
```

---

## Exceptions (White List)

以下の「参照・無害」なコマンドは自動実行してよい:

- `ls`, `dir`, `Get-ChildItem`
- `cat`, `type`, `Get-Content`
- `grep`, `Select-String`
- `echo`, `Write-Output`
- `mkdir` (新規作成のみ)
