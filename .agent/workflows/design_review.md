---
description: Review implementation plan before coding (Constructor's duty)
---

# Design Review Workflow

Before starting implementation, Constructor must review the Architect's plan.

## Steps

1. Open `implementation_plan.md` (pulled from git or provided by Architect).
2. Invoke the review module:
   - Copy content of `prompts/modules/D1-design_review.md` into chat.
   - Paste `implementation_plan.md` content.
3. Fill in the review checklist (Feasibility, Completeness, Ripple Effect, Effort).
4. Output verdict:
   - **APPROVED**: Proceed to implementation.
   - **NEEDS REVISION**: Document issues and return to Architect.
5. If approved, update `task.md` with `[/]` (in progress) and begin coding.
