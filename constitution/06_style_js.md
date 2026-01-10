---
id: G-6-JS
layer: Style (Code DNA - JavaScript/GAS)
version: "1.0"
---

# G-6-JS: JavaScript / GAS スタイルガイド

> Google Apps Script および Web フロントエンド向けコード規約。

---

## 1. 基本原則

> Python版 (`06_style.md`) の3原則をJSにも適用する。

| 原則 | 意味 |
|---|---|
| **Guard** | 重要データには触らせない（`const` 優先） |
| **Prove** | 動くと言う前にテストで示せ |
| **Undo** | 全変更は可逆に（ログ、バックアップ） |

---

## 2. 変数宣言

> `var` は使わない。`const` を基本とし、再代入が必要な場合のみ `let`。

### ✅ Do

```javascript
const CONFIG = {
  FOLDER_ID: '...',
  API_URL: 'https://...',
};

let counter = 0;
counter += 1;
```

### ⛔ Don't

```javascript
var data = [];  // var は禁止
let constant = 'never changes';  // 再代入しないなら const
```

---

## 3. 命名規則

| 対象 | 規約 | 例 |
|---|---|---|
| 変数/関数 | `camelCase` | `getUserName`, `fileCount` |
| クラス | `PascalCase` | `FileProcessor`, `ConfigManager` |
| 定数 | `UPPER_SNAKE_CASE` | `MAX_RETRY_COUNT`, `API_BASE_URL` |
| プライベート関数 | `trailingUnderscore_` | `parseFileName_`, `sendNotification_` |

### ⛔ 禁止される名前

`data`, `tmp`, `info`, `result`, `value`, 1文字変数 (ループ `i`, `j` 除く)

---

## 4. 関数定義

> アロー関数を優先。ただし `this` バインドが必要な場合は `function` を使用。

### ✅ Do

```javascript
// アロー関数（推奨）
const processFiles = (files) => {
  return files.map(f => f.name);
};

// コールバック
files.forEach(file => {
  Logger.log(file.name);
});
```

### ⛔ Don't

```javascript
// 不要な function キーワード
const processFiles = function(files) {
  return files.map(function(f) {
    return f.name;
  });
};
```

---

## 5. エラーハンドリング

> エラーは握りつぶさない。ログ出力後、再送出または適切な処理を行う。

### ✅ Do

```javascript
try {
  doSomething();
} catch (error) {
  Logger.log(`エラー発生: ${error.message}`);
  // 通知を送信してから再送出
  sendErrorNotification_(error);
  throw error;
}
```

### ⛔ Don't

```javascript
try {
  doSomething();
} catch (error) {
  // 沈黙の失敗 - 絶対禁止
}
```

---

## 6. GAS 固有のルール

### 6.1 CONFIG パターン

> 設定値は `config.gs` に集約し、`CONFIG` オブジェクトで管理。

```javascript
// config.gs
const CONFIG = {
  RELEASE_FOLDER_ID: '...',
  SPREADSHEET_ID: '...',
  GITHUB_TOKEN: '...', // ⚠️ 絶対にGitHubにPushしない
};
```

### 6.2 プライベート関数マーカー

> 内部使用関数は `trailingUnderscore_` で命名。GASでは `private` キーワードがないため、これが慣例。

```javascript
// 公開関数
function syncToGitHub() { ... }

// 内部関数（外部から呼ばない）
function parseFileName_(fileName) { ... }
function sendNotification_(message) { ... }
```

### 6.3 Drive API の有効化

> `Drive.Revisions.list()` など Advanced Services を使う場合は、明示的に有効化が必要。

```javascript
// サービス追加: エディタ左側「サービス +」→「Drive API」
const revisions = Drive.Revisions.list(fileId);
```

---

## 7. ドキュメンテーション

> JSDoc形式でコメントを記述。

```javascript
/**
 * ファイル名をパースしてカテゴリ・ID・タイトルを抽出
 * @param {string} fileName - 処理対象のファイル名
 * @returns {{category: string, docId: string, title: string}} パース結果
 */
function parseFileName_(fileName) {
  // ...
}
```

---

## 8. テンプレートリテラル

> 文字列結合には `+` ではなくテンプレートリテラルを使用。

### ✅ Do

```javascript
const message = `検出されたファイル数: ${files.length}`;
const url = `https://api.github.com/repos/${owner}/${repo}/contents`;
```

### ⛔ Don't

```javascript
const message = '検出されたファイル数: ' + files.length;
const url = 'https://api.github.com/repos/' + owner + '/' + repo + '/contents';
```

---

## 9. Living Samples

| 用途 | 参照ファイル | 模倣ポイント |
|---|---|---|
| GAS設定 | `現場連携Template/automation/gas/config.gs` | CONFIG パターン |
| GAS処理 | `現場連携Template/automation/gas/sync_to_github.gs` | プライベート関数, エラーハンドリング |

> [!IMPORTANT]
> Living Sample への変更はレビュー必須。
