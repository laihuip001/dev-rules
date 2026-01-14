---
module_id: "M-31"
name: "Checkpoint"
description: "状態保存とコンテキスト維持"
---

# M-31: Checkpoint (チェックポイント)

## 概要

長期間のセッションや複雑なタスクにおいて、コンテキスト（文脈）の喪失を防ぐために、定期的に現在の状態を記録・保存する。

## アクション

1. **Task Boundary**:
    * タスクの区切りで `task_boundary` を適切に更新し、現状（Status）と履歴（Summary）を最新に保つ。

2. **Artifacts**:
    * 重要な決定事項、計画、調査結果は、チャットログではなく Artifact (Markdownファイル) として保存する。これにより、セッションが変わっても情報を引き継げる。
    * 例: `implementation_plan.md`, `audit_report.md`

3. **Git Commit**:
    * 「動く状態」になったらこまめにコミットする。コミットメッセージ自体が作業ログとなる。

4. **Artifact Directory**:
    * 50ターンを超えるような長いセッションでは、重要なファイルパスや外部ディレクトリの情報を Artifact に書き出し、コンテキストウィンドウから溢れても参照できるようにする。
