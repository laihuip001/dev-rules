
import os
import logging
from pathlib import Path
from sqlalchemy import text

import sys
import logging
from typing import Dict, Any, Optional
from pathlib import Path

# Add TEALS submodule to sys.path to support absolute imports (e.g. "from models import ...")
teals_path = Path(__file__).parent / "teals"
if str(teals_path) not in sys.path:
    sys.path.insert(0, str(teals_path))

try:
    from models import init_db
    from log_manager import add_log
    from verifier import verify_all
except ImportError:
    # Fallback if path insertion failed or run differently
    from src.infra.teals.models import init_db
    from src.infra.teals.log_manager import add_log
    from src.infra.teals.verifier import verify_all

USER_ID = os.getenv("FLOW_USER_ID", "local_user")

class TEALSAdapter:
    def __init__(self, db_path: Optional[str] = None):
        if db_path is None:
            # Default: src/infra/../../data/flow_audit.db = project_root/data/flow_audit.db
            project_root = Path(__file__).parent.parent.parent
            db_path = str(project_root / "data" / "flow_audit.db")

        path_obj = Path(db_path)
        if not path_obj.parent.exists():
            path_obj.parent.mkdir(parents=True, exist_ok=True)
            
        self.engine, self.Session = init_db(db_path)
        
        # WAL Mode for concurrency
        try:
            with self.engine.connect() as conn:
                conn.execute(text("PRAGMA journal_mode=WAL;"))
        except Exception as e:
            logging.warning(f"Failed to enable WAL mode: {e}")
        
        self.integrity_warning = False
        self.read_only_mode = False
    
    def log_action(self, action: str, table: str, 
                   before: Dict[str, Any] = None, after: Dict[str, Any] = None) -> bool:
        if self.read_only_mode:
            logging.critical("TEALS: read-only mode active, skipping log")
            return False
            
        try:
            session = self.Session()
            add_log(session, USER_ID, action, table, before, after)
            session.close()
            return True
        except Exception as e:
            logging.exception(f"TEALS log failed")
            return False
    
    def verify_integrity(self) -> bool:
        try:
            session = self.Session()
            result = verify_all(session)
            session.close()
            # TEALS returns VerificationResult object
            return result.is_valid
        except Exception as e:
            logging.error(f"TEALS verify failed: {e}")
            return False

    def enter_isolation_mode(self):
        self.read_only_mode = True
        logging.critical("🚨 TEALS: Isolation mode activated")
