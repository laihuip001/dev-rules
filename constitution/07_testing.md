---
id: G-7
layer: Quality (Testing)
version: "1.0"
---

# G-7: テスト規約

> 動くと言う前に**テストで示せ**。テストなきコードは負債である。

---

## 1. テストの3原則

| 原則 | 意味 |
|---|---|
| **Fast** | テストは高速であるべき。1秒以上かかるテストは設計を見直せ。 |
| **Isolated** | テスト間は独立。順序依存や共有状態は禁止。 |
| **Repeatable** | 何度実行しても同じ結果。ランダム・時刻依存はモック化。 |

---

## 2. テストファイル命名規則

### Python

| 対象ファイル | テストファイル |
|---|---|
| `src/core/processor.py` | `tests/test_processor.py` |
| `src/api/main.py` | `tests/api/test_main.py` |

```
tests/
├── test_processor.py      # test_ プレフィックス必須
├── test_config.py
└── fixtures/              # 共有テストデータ
    └── sample_data.json
```

### JavaScript/GAS

GASは標準テストフレームワークがないため、以下のパターンを採用:

```javascript
// テスト関数には test_ プレフィックス
function test_parseFileName_() {
  const result = parseFileName_('A-01_テスト図面.pdf');
  if (result.docId !== 'A-01') {
    throw new Error('parseFileName_ failed');
  }
  Logger.log('✅ test_parseFileName_ passed');
}

// 全テスト実行関数
function runAllTests() {
  test_parseFileName_();
  test_generateMarkdown_();
  Logger.log('🎉 All tests passed');
}
```

---

## 3. テストの構造 (AAA パターン)

> **Arrange → Act → Assert** の3ステップで構造化。

```python
def test_process_text_trims_whitespace():
    # Arrange: 準備
    input_text = "  hello world  "
    
    # Act: 実行
    result = process_text(input_text)
    
    # Assert: 検証
    assert result == "hello world"
```

---

## 4. 何をテストするか

### ✅ テスト必須

| 対象 | 理由 |
|---|---|
| **公開関数** | 契約（インターフェース）を保証 |
| **境界値** | 0, 1, max, 空リスト, None |
| **エラーケース** | 例外が正しく発生するか |
| **ビジネスロジック** | 計算、分岐、変換処理 |

### ⛔ テスト不要

| 対象 | 理由 |
|---|---|
| **getter/setter のみ** | ロジックがない |
| **外部API直接呼び出し** | モック化して間接テスト |
| **プライベート関数** | 公開関数経由でカバー |

---

## 5. モック・スタブの使い方

> 外部依存（API、DB、ファイルシステム）はモック化する。

### Python (unittest.mock)

```python
from unittest.mock import patch, MagicMock

def test_fetch_data_returns_json():
    with patch('requests.get') as mock_get:
        mock_get.return_value = MagicMock(
            json=lambda: {'status': 'ok'}
        )
        result = fetch_data('https://api.example.com')
        assert result['status'] == 'ok'
```

### JavaScript (GAS)

```javascript
// GASにはモックライブラリがないため、関数を差し替え
function test_syncToGitHub_withMock() {
  // 元の関数を退避
  const originalCommit = commitToGitHub_;
  
  // モックを差し込み
  commitToGitHub_ = (content) => ({ updated: true, message: 'mocked' });
  
  try {
    syncToGitHub();
    Logger.log('✅ test_syncToGitHub passed');
  } finally {
    // 元に戻す
    commitToGitHub_ = originalCommit;
  }
}
```

---

## 6. カバレッジ基準

| レベル | 基準 | 適用範囲 |
|---|---|---|
| **コア** | 80%以上 | `src/core/`, ビジネスロジック |
| **API** | 70%以上 | エンドポイント、ハンドラー |
| **ツール** | 50%以上 | スクリプト、ユーティリティ |

> [!IMPORTANT]
> カバレッジは指標であって目標ではない。意味のないテストで数字を稼ぐのは禁止。

---

## 7. テスト実行コマンド

### Python

```bash
# 全テスト実行
pytest tests/ -v

# カバレッジ付き
pytest tests/ --cov=src --cov-report=html

# 特定ファイルのみ
pytest tests/test_processor.py -v
```

### GAS

```javascript
// スクリプトエディタで runAllTests を選択して実行
// または時間トリガーで定期実行
```

---

## 8. 失敗時の対応

1. **ローカルで再現** — 問題を理解
2. **最小再現コードを作成** — 不要な要素を削ぎ落とす
3. **修正前にテストを書く** — 回帰防止
4. **修正後、全テスト実行** — 副作用確認
