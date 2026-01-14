---
module_id: "M-30"
name: "Pre-Verify"
description: "事前存在確認プロトコル"
---

# M-30: Pre-Verify (事前確認)

## 概要

「AIの幻覚 (Hallucination)」によるファイルパスの間違いや、存在しないツールの呼び出しを防ぐため、アクションを起こす前に必ず対象の存在を確認する。

## ルール

1. **Look before you leap**:
    * `view_file`, `replace_file_content` などを使う前に、そのファイルが本当にそこにあるか `list_dir` や `find_by_name` で確認する。
    * 特に相対パスや、ユーザーから曖昧に指定されたパスの場合は必須。

2. **Check Tools**:
    * シェルコマンドを実行する際は、そのコマンドがインストールされているか（パスが通っているか）を疑う。
    * `gh`, `npm`, `python` など、環境によってあったりなかったりするものは注意。

3. **Validate Output**:
    * ツールの実行結果（Exit Code, Stdout/Stderr）を必ず確認する。「実行したから成功したはず」と思い込まない。
