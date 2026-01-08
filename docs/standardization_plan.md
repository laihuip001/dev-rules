# AI Code Standardization: The 2-Pillar Protocol

## Objective

AIエージェントが生成するコードのスタイルと構造を標準化し、一貫性・保守性・プロジェクト固有の「DNA」との整合性を確保する。

---

## Pillar 1: The Machine (Linter)

機械的に強制可能なルールは、すべてLinter設定に委ねる。

**Action:** `pyproject.toml` を唯一の情報源として確立する。

- **Tool:** `ruff` を推奨（速度と網羅性）。
- **Policy:**
  - AIはコード生成**前**にLinter設定を読み込むこと。
  - `tests/` および `scripts/` には `per-file-ignores` でルールを緩和し、過剰な品質要求とトークン消費を防止する。

---

## Pillar 2: The Spirit (Style Manifesto)

Linterでは拾えない「設計思想」と「具体例 (Living Samples)」を言語化する。

**Action:** `rules/constitution/06_style.md` を作成する。

### Content Focus

Linterルールと重複しない「アーキテクチャ上の意思決定」に厳密に集中する。

- **Examples:**
  - `pathlib` の強制使用 (`os.path` 禁止)。
  - 型ヒントの厳格度 (例: `Any` 禁止)。
  - エラーハンドリング方針 (伝播 vs キャッチ)。

### Living Samples (模範コード参照)

静的な「ゴールデンサンプル」ではなく、`src/` 内の**現行の高品質コード**を参照する（ドキュメントの陳腐化を防止）。

- **Constraint (Crucial):** ファイル名だけでなく、**何を模倣すべきか**を明記すること（「Confused Junior」対策）。
  - *Bad:* "`src/core/dto.py` を模倣せよ。"
  - *Good:* "`src/core/dto.py` を参照。特に: 1) `from_dict` ファクトリパターン、2) `frozen=True` の dataclass 使用。"

---

## Implementation Roadmap

1. ✅ **`rules/constitution/06_style.md` を作成:** コアとなるアーキテクチャルールと、明示的な模倣ポイント付きのLiving Sample参照を定義する。
2. ⬜ **`pyproject.toml` を設定:** 適切な除外設定を含む `ruff` ルールを設定する。
3. ⬜ **`prompts/modules/C4C5-code.md` を更新:** `06_style.md` への準拠チェックを追加する。
4. ✅ **`constitution/00_orchestration.md` を更新:** タスク開始時のコンテキスト読み込み手順を追加する。

---

## Audit History

本計画の策定過程における監査ログは [audit_log.md](./audit_log.md) を参照。
