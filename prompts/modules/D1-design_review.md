---
id: D-1
modes: [review]
role: Constructor
---

# Design Review (Constructor's Lens)

> Architect's plan meets Builder's reality.

## Purpose

Validate `implementation_plan.md` before coding begins.

## Review Checklist

### 1. Feasibility

- [ ] Can this run on target environment (Termux/Android)?
- [ ] Are all dependencies available (no forbidden libs)?

### 2. Completeness

- [ ] Test plan defined?
- [ ] Edge cases considered?
- [ ] Rollback strategy if it fails?

### 3. Ripple Effect

- [ ] Impact on existing files identified?
- [ ] Breaking changes documented?

### 4. Effort Estimate

- [ ] Is scope realistic for one session?
- [ ] Should it be split into smaller tasks?

## Output Format

```markdown
## Design Review: [Plan Name]

| Aspect | Status | Notes |
|---|---|---|
| Feasibility | ✅/⚠️/❌ | ... |
| Completeness | ✅/⚠️/❌ | ... |
| Ripple Effect | ✅/⚠️/❌ | ... |
| Effort | ✅/⚠️/❌ | ... |

### Verdict
- [ ] **APPROVED** — Proceed to implementation.
- [ ] **NEEDS REVISION** — Return to Architect with notes below.

### Revision Notes (if any)
1. ...
```
