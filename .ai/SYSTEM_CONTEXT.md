# SYSTEM CONTEXT: Flow AI v4.0 (Termux Edition)

## 0. 🎯 Strategy: "Dual-Face" Monorepo

| Mode | Target | Requirement | Philosophy |
|------|--------|-------------|------------|
| **Personal** | Termux (Android) | `requirements-termux.txt` | **Speed (Pre-processing)** <br> UIレス/API主体 |
| **Public** | Desktop/Portfolio | `requirements.txt` | **Experience (GUI)** <br> Flet/Web UI主体 |

- **Unified Core:** `src/core` は共有（二重管理防止）
- **Interface Separation:** `src/api` (Personal) vs `src/app` (Public)

## 1. 🌍 Runtime Environment Constraints (CRITICAL)

- **Target OS:** Android Termux (aarch64 / Linux)
- **Performance:** Low Memory, Battery constraint.
- **Library Restrictions:**
  - ❌ **BAN:** `pandas`, `numpy`, `scipy`, `tensorflow`, `playwright`, `selenium`
  - ✅ **USE:** `sqlite3`, `httpx`, `beautifulsoup4`, `uvicorn`, `fastapi`, `requests`
- **Strict Rule:** 新規ライブラリ追加時は、必ず「Termuxでビルド不要か（Pure Pythonか）」を確認せよ。

## 2. 🛡️ Security Protocols

- **Secrets:** APIキーやトークンは**絶対にコード内にハードコードしない**こと。
- **Env Vars:** すべての機密情報は `config.py` 経由で読み込む。
- **App Mode:** `APP_MODE="PERSONAL"` or `"PUBLIC"` で挙動（UI有無/チュートリアル）を切り替える。
- **PII Policy:** 個人情報は「自動置換」ではなく「検知と警告」に留める。

## 3. 💾 Database Strategy

- **ORM:** SQLAlchemyを使用。
- **Migration:** モデル変更時は `alembic` を使用すること。
- **WAL Mode:** SQLiteはWALモードで運用。
