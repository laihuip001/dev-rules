---
id: G-6
layer: Style (Code DNA)
version: "1.0"
---

# G-6: Style Protocol (コードスタイル憲法)

> Linterで拾えない「設計思想」を定義する。機械的ルールは `pyproject.toml` に委譲。

---

## 1. ライブラリ選定 (Library Selection)

### 強制 (MUST)

| 用途 | 使用ライブラリ | 禁止 |
|---|---|---|
| ファイルパス操作 | `pathlib.Path` | `os.path` |
| 環境変数 | `os.environ.get()` with default | 直接 `os.environ[]` |
| HTTP通信 | `requests` | `urllib` (可読性劣) |
| JSON処理 | 標準 `json` | なし |

### 禁止 (Termux互換性)

- `pandas`, `numpy`, `scipy`, `lxml` （Phase 1）

---

## 2. 型ヒント (Type Hints)

### ルール

- **関数シグネチャ:** 引数と戻り値に型ヒント**必須**。
- **`Any` 禁止:** 明示的な型か `Union` を使用。
- **Optional:** `None` を許容する場合は `Optional[T]` または `T | None` を使用。

### 例

```python
# ✅ Good
def process_text(text: str, max_len: int = 100) -> str:
    ...

# ❌ Bad
def process_text(text, max_len=100):
    ...
```

---

## 3. エラーハンドリング (Error Handling)

### 方針: 伝播優先 (Propagate First)

- **原則:** 例外はキャッチせず、呼び出し元に伝播させる。
- **キャッチ許可:** 以下の場合のみ。
    1. リソース解放が必要 (`finally`)
    2. 代替処理が可能 (フォールバック)
    3. ログ記録後に再送出 (`raise`)

### 禁止パターン

```python
# ❌ 握りつぶし禁止
try:
    do_something()
except Exception:
    pass  # NEVER DO THIS
```

---

## 4. 命名規則 (Naming Conventions)

### ルール

- **関数/変数:** `snake_case`
- **クラス:** `PascalCase`
- **定数:** `UPPER_SNAKE_CASE`
- **プライベート:** `_leading_underscore`

### 禁止

- 曖昧な名前: `data`, `tmp`, `info`, `result`, `value`
- 1文字変数 (ループカウンタ `i`, `j` を除く)

---

## 5. Living Samples (模範コード参照)

> 以下のファイルを「模範」として参照せよ。**模倣ポイント**を明記。

| カテゴリ | 参照ファイル | 模倣ポイント |
|---|---|---|
| DTO/データクラス | `src/core/dto.py` (作成予定) | `@dataclass(frozen=True)` の使用、`from_dict` ファクトリ |
| 設定管理 | `src/config.py` (作成予定) | 環境変数フォールバック、型安全なアクセス |

> [!NOTE]
> Living Samplesは「現行コード」を参照するため、ファイル変更時はセキュリティレビューを実施すること。

---

## 6. コメント/Docstring

### ルール

- **Docstring:** 公開関数・クラスには**必須**。Google Style。
- **インラインコメント:** 「なぜ (Why)」を説明。「何を (What)」はコード自体で表現。

### 例

```python
def calculate_score(items: list[Item]) -> float:
    """スコアを計算する。

    Args:
        items: 評価対象のアイテムリスト。

    Returns:
        0.0〜1.0 の正規化スコア。
    """
    # 空リストは早期リターン（ゼロ除算防止）
    if not items:
        return 0.0
    ...
```
