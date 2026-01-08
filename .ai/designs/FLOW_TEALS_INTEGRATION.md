# DESIGN DOC: Flow ↔ TEALS Integration v1.3

> **From:** Architect → **To:** Constructor
> **Date:** 2026-01-08

---

## Spec

| Item | Value |
|------|-------|
| **Goal** | Flowの操作履歴をTEALSに記録し、改ざん検知を実現 |
| **Files** | `src/infra/teals_adapter.py` (NEW), `src/core/processor.py` (MODIFY) |
| **Scope** | 2 files, 80-120 lines |

---

## Step 1: TEALS導入

```bash
mkdir -p src/infra
git submodule add https://github.com/laihuip001/TEALS.git src/infra/teals
mkdir -p data
```

---

## Step 2: Constructor Task

> **Constructor: `src/core/processor.py` を確認し、クリップボード処理メソッド末尾にフックを挿入。**

---

## Step 3: Interface Implementation

```python
# src/infra/teals_adapter.py

import os
import logging
from pathlib import Path
from sqlalchemy import text

from src.infra.teals.models import init_db
from src.infra.teals.log_manager import add_log
from src.infra.teals.verifier import verify_all

# 環境変数から取得（マルチユーザー対応）
USER_ID = os.getenv("FLOW_USER_ID", "local_user")

class TEALSAdapter:
    def __init__(self, db_path: str = "data/flow_audit.db"):
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.engine, self.Session = init_db(db_path)
        
        # WALモード有効化（並行アクセス対応）
        with self.engine.connect() as conn:
            conn.execute(text("PRAGMA journal_mode=WAL;"))
        
        self.integrity_warning = False
        self.read_only_mode = False
    
    def log_action(self, action: str, table: str, 
                   before: dict = None, after: dict = None) -> bool:
        if self.read_only_mode:
            logging.warning("TEALS: read-only mode, skipping log")
            return False
        try:
            session = self.Session()
            add_log(session, USER_ID, action, table, before, after)
            session.close()
            return True
        except Exception as e:
            logging.error(f"TEALS log failed: {e}")
            return False
    
    def verify_integrity(self) -> bool:
        try:
            session = self.Session()
            result = verify_all(session)
            session.close()
            return "正常" in result or "OK" in result
        except Exception as e:
            logging.error(f"TEALS verify failed: {e}")
            return False
    
    def enter_isolation_mode(self):
        """改ざん検知時に呼び出し: 書き込み禁止"""
        self.read_only_mode = True
        logging.critical("🚨 TEALS: Isolation mode activated")
```

---

## Verification Failure Handling

```python
def startup_check(teals: TEALSAdapter):
    if not teals.verify_integrity():
        logging.warning("⚠️ TEALS: 改ざんの可能性を検知")
        teals.integrity_warning = True
        teals.enter_isolation_mode()  # 隔離モード
```

---

## Few-Shot Examples

```python
teals.log_action("INSERT", "clipboard", after={"content": "text"})
teals.log_action("UPDATE", "settings", before={"k": "v1"}, after={"k": "v2"})
teals.log_action("DELETE", "clipboard", before={"id": 123})
```

---

## Negative Constraints

| ❌ 禁止 | ✅ 正解 |
|--------|--------|
| `processor.py` に直接import | `TEALSAdapter` 経由 |
| `log_action()` 戻り値無視 | `if not teals.log_action(...): ...` |
| ハードコード `user_id` | `os.getenv("FLOW_USER_ID")` |

---

## Acceptance Criteria

- [ ] `PRAGMA journal_mode` が `wal` を返す
- [ ] `FLOW_USER_ID` 環境変数でuser_id変更可能
- [ ] 改ざん検知時 `read_only_mode = True`
