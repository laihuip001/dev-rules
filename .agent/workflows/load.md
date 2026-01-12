---
description: プロンプトモジュールをIDで現在のセッションにロード
---

# /load ワークフロー

指定されたモジュールIDに基づき、プロンプトモジュールの内容を読み込んで適用する。

## 使用方法

```
/load <module-id> [<module-id2> ...]
```

## 例

```
/load C-4        # Code Audit モジュールをロード
/load G-3        # Security レイヤーをロード
/load G-1 G-2    # 複数モジュールを同時ロード
```

## 実行ステップ

1. **引数の解析**
   - ユーザーが指定したモジュールIDを抽出

2. **モジュールの特定**
   - Gプレフィックス (G-1〜G-7) → `constitution/` から読み込み
     - G-1: `01_environment.md`
     - G-2: `02_logic.md`
     - G-3: `03_security.md`
     - G-4: `04_lifecycle.md`
     - G-5: `05_meta_cognition.md`
     - G-6: `06_style.md`
     - G-7: `07_implementation.md`
   - その他 (C-*, Q-*, A-*, etc.) → `prompts/modules/` から読み込み
     - 例: C-4 → `C4C5-code.md`

3. **ファイルの読み込み**
   - `view_file` ツールで対象ファイルを読み込む

4. **コンテキストへの適用**
   - 読み込んだ内容をセッションコンテキストとして保持
   - 以降の応答でモジュールのルールを適用

## モジュールID対応表

| ID | File | Category |
|---|---|---|
| G-1 | constitution/01_environment.md | Environment |
| G-2 | constitution/02_logic.md | Logic |
| G-3 | constitution/03_security.md | Security |
| G-4 | constitution/04_lifecycle.md | Lifecycle |
| G-5 | constitution/05_meta_cognition.md | Meta |
| G-6 | constitution/06_style.md | Style |
| G-7 | constitution/07_implementation.md | Implementation |
| C-1-2 | prompts/modules/C1C2-adversarial.md | Critical |
| C-3 | prompts/modules/C3-structural_audit.md | Critical |
| C-4-5 | prompts/modules/C4C5-code.md | Critical |
| C-6-7 | prompts/modules/C6C7-prompt.md | Critical |
| Q-1 | prompts/modules/Q1-feynman_filter.md | Quality |
| Q-2 | prompts/modules/Q2-second_order_thinking.md | Quality |
| Q-3 | prompts/modules/Q3-occams_razor.md | Quality |
| Q-4 | prompts/modules/Q4-aesthetic_audit.md | Quality |
