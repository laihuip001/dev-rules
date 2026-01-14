# GEMINI.md 整合性検証レポート

## 概要

`GEMINI.md` に導入された哲学的フレームワーク（方法的懐疑・反証可能性）に基づき、記述されているルールとファイルシステムの実態を検証しました。
その結果、**参照されているモジュールIDと実際のファイル構成に重大な乖離**が見つかりました。

## 🔴 発見された不整合 (Falsified Hypotheses)

`GEMINI.md` で定義されている以下のモジュールは、`prompts/modules/` ディレクトリ内に対応するファイルが存在しません。

| ID | Module Name | GEMINI.md 上の定義 | 実態 (File System) |
|----|-------------|-------------------|-------------------|
| **M-01** | DMZ | 重要ファイル保護 | ❌ **不在** |
| **M-07** | Devil's Advocate | 自己批判 | ⚠️ 不在 (類似: `敵対的レビュー凸.md`, `C1C2-adversarial.md`) |
| **M-25** | Rollback | 全変更は可逆 | ❌ **不在** |
| **M-30** | Pre-Verify | 存在確認必須 | ❌ **不在** |
| **M-31** | Checkpoint | 状態保存 | ❌ **不在** |
| **G-1** | - | Dynamic Loading 参照 | ❌ **不在** |
| **G-2** | - | Dynamic Loading 参照 | ❌ **不在** |
| **G-3** | - | Dynamic Loading 参照 | ❌ **不在** |
| **G-4** | - | Dynamic Loading 参照 | ❌ **不在** |
| **G-5** | - | Dynamic Loading 参照 | ❌ **不在** |

## 🟡 表記の揺れ

Metacognitive Hypervisor セクションでは、日本語ファイル名への参照行われています。これらはファイルが存在しますが、ID体系 (A-xx, C-xx) との整合性が取れていません。

| Symptom | Suggested Module (GEMINI.md) | File Exists? | ID Mapping (推定) |
|---------|------------------------------|--------------|------------|
| Circular Reasoning | `第一原理思考` | ✅ | `A9-first_principles.md` |
| False Dichotomy | `発散と収束` | ✅ | `X1X2-divergence_convergence.md` |
| Fuzzy Verb | `回答の解像度向上` | ✅ | (No ID prefix matched clearly) |

## 💡 考察 (Philosophical Insight)

「Prove (動くと言う前にテストで示せ)」という原則に照らすと、現在の `GEMINI.md` は「存在しないコマンド (`/load G-1`)」をユーザーおよびAIに提示しており、**誤った期待**を生じさせています。
これは「信頼できない思考」の典型例であり、即座に修正が必要です。

## 🛠 修正提案

1. **Mandatory Modules (M-xx) の扱い変更:**
    * これらは「ロードするプロンプト」ではなく「常時有効なルール」であるため、`/load` 対象から外し、本文中にルールとして明記する形に整理する。
    * あるいは、実体となるプロンプトファイル（空でもよいので参照用）を作成する。

2. **Dynamic Loading (G-xx) の修正:**
    * 架空のID (G-xx) を廃止し、実在するID（C-4, A-9等）への参照に書き換える。

3. **日本語ファイル名とIDの統一:**
    * 推奨モジュールをファイル名そのものではなく、IDまたは統一された英語名で記述する。
