# DESIGN DOC: CI/CD Pipeline v2.0

> **From:** Architect → **To:** Constructor

---

## Spec

| Item | Value |
|------|-------|
| **Goal** | Architect → Constructor → Termux パイプライン |
| **Files** | `.github/workflows/flow.yml`, `requirements.txt`, `tests/test_teals.py`, `.python-version` |

---

## .python-version

```
3.11
```

---

## requirements.txt

```txt
sqlalchemy>=2.0.0
pytest>=8.0.0
ruff>=0.1.0
```

---

## CI: GitHub Actions

```yaml
name: Flow CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install ruff && ruff check . --ignore E501
```

---

## CD: Termux Deploy

```bash
cd ~/flow
git pull origin main
git submodule update --init --recursive
PID=$(ps aux | grep "[p]ython main.py" | awk '{print $2}')
[ -n "$PID" ] && kill $PID
nohup python main.py > /dev/null 2>&1 &
```

### Health Check (cron)

```bash
# ~/flow/health_check.sh
#!/bin/bash
pgrep -f "python main.py" || (cd ~/flow && nohup python main.py > /dev/null 2>&1 &)
```

```bash
crontab -e
*/5 * * * * ~/flow/health_check.sh
```

---

## Tests

```python
# tests/test_teals.py
import pytest
from src.infra.teals_adapter import TEALSAdapter
from src.infra.teals.models import AuditLog

@pytest.fixture
def teals(tmp_path):
    return TEALSAdapter(db_path=str(tmp_path / "test.db"))

def test_log_and_verify(teals):
    teals.log_action("INSERT", "test", after={"key": "value"})
    assert teals.verify_integrity() is True

def test_tamper_detection(teals):
    teals.log_action("INSERT", "test", after={"key": "value"})
    session = teals.Session()
    session.query(AuditLog).first().after_data = '{"key": "TAMPERED"}'
    session.commit()
    session.close()
    assert teals.verify_integrity() is False
```

---

## Acceptance Criteria

- [ ] GitHub Actions緑
- [ ] `test_tamper_detection` PASS
