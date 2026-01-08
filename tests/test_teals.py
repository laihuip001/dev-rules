
import pytest
import os
from src.infra.teals_adapter import TEALSAdapter
from src.infra.teals.models import AuditLog

@pytest.fixture
def teals(tmp_path):
    # Use tmp_path for isolation
    db_file = tmp_path / "test_audit.db"
    return TEALSAdapter(db_path=str(db_file))

def test_log_and_verify(teals):
    assert teals.log_action("INSERT", "test_table", after={"foo": "bar"}) is True
    assert teals.verify_integrity() is True

def test_tamper_detection(teals):
    # 1. Log something
    teals.log_action("INSERT", "test_table", after={"val": 100})
    assert teals.verify_integrity() is True
    
    # 2. Tamper directly
    session = teals.Session()
    log = session.query(AuditLog).first()
    log.after_data = '{"val": 999}' # Tampered
    session.commit()
    session.close()
    
    # 3. Verify failure
    assert teals.verify_integrity() is False

def test_isolation_mode(teals):
    teals.enter_isolation_mode()
    assert teals.log_action("INSERT", "test", after={"a":1}) is False
