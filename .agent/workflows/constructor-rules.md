---
description: 実装担当（Constructor）が従うべき行動規範
---

# Constructor Operating Rules

このワークフローは、実装担当が新しいタスクを開始する際に確認すべきチェックリストである。

## 実行フロー

1. **Context Load（文脈読み込み）**
   - 対象ファイルを `view_file` で読み込む
   - 関連する憲法モジュールをロード: `/load G-2 G-7`

2. **Plan（計画）**
   - 変更概要を `implementation_plan.md` に記載
   - ユーザー承認を待つ（`notify_user`）

3. **Test First（テスト先行）**
   - 再現テスト or 検証スクリプトを作成
   - テストが失敗することを確認（Red）

4. **Implement（実装）**
   - コードを記述
   - テストが成功することを確認（Green）

5. **Verify（検証）**
   - Lint/Type Check を実行
   - ブラウザ検証（該当する場合）

6. **Commit（コミット）**
   - Narrative Commit形式でコミット
   - ロールバック手順を併記
