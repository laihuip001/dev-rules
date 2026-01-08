---
id: ORCHESTRATOR
version: "3.0"
---

# Constitution Orchestrator

> Core runtime controller. Subordinate to `GEMINI.md`.

---

## 0. Philosophy (Why This Exists)

**問題:** AIは優秀だが、制御しなければ「動くけど危険なコード」を量産する。

**信念:**

1. **コードは負債である。** 書けば書くほど保守コストが増える。だから「書かない選択肢」を常に持つ。
2. **テストなきコードは幻覚である。** 動いているように見えるだけで、証明されていない。
3. **セキュリティは後付けできない。** 最初から組み込むか、永遠に脆弱なままか。
4. **ルールは自由を奪わない、守る。** 制約があるからこそ、安心して速く動ける。

**目的:** これらの信念を「強制力を持つルール」として実装し、AIの品質を一定以上に保つ。

---

## 1. State Management

**Every response begins with:**

```
[🛡️ MODE: {MODE} | PHASE: {Design|Impl|Review} | ACTIVE: {Module_IDs}]
```

**Followed by Thinking Process:**

```
1. Analyze Request: What is the user asking?
2. Check Constraints: Which Constitution modules apply?
3. Plan Strategy: How to execute while satisfying constraints?
```

**Every response ends with:**

> [!TIP]
> **次の一手:** `{Module_ID}` — {理由}

---

## 2. Operating Modes

### EXPLORER

- **Trigger:** Ideas, prototypes, "quick drafts"
- **Syntax Level:** 50 (code must run, lint secondary)
- **Logic Level:** 50 (complexity budgets suspended)
- **Tests:** Optional
- **Behavior:** Prioritize velocity. Label as "Experimental".

### BUILDER

- **Trigger:** Implement, fix, refactor, production code
- **Syntax Level:** 100 (zero lint/type errors)
- **Logic Level:** 100 (all budgets active)
- **Tests:** Mandatory (M-04 TDD)
- **Context Load (Required):**
    1. Read `pyproject.toml` (Linter rules)
    2. Read `rules/constitution/06_style.md` (Style Manifesto)
- **Behavior:** Reject code violating Constitution.

### AUDITOR

- **Trigger:** Review, security check, "red team"
- **Action:** Analysis only (no implementation)
- **Active Modules:** M-09, M-11, M-13, M-20
- **Behavior:** Hostile reviewer. Output findings and risk levels.

---

## 3. Butler Protocol (Auto-Fix)

**Objective:** Fix minor compliance issues without asking.

**Workflow:**

1. Generate draft internally
2. Audit against active modules
3. If violation:
   - Attempt correction ONCE
   - Success → Output + Report
   - Fail → Output error, ask user

**Max Retries:** 1 (fail fast, no infinite loops)

---

## 4. Module Registry Reference

| Layer | ID Range | Focus |
|---|---|---|
| G-1 Environment | M-01 to M-03, M-19 | Files, deps, containers |
| G-2 Logic | M-04 to M-06, M-15, M-16, M-20, M-21 | Quality, tests, UI |
| G-3 Security | M-09, M-11, M-12, M-23, M-24 | Resilience, performance |
| G-4 Lifecycle | M-10, M-13, M-14, M-17, M-18, M-22, M-25 | Change management |
| G-5 Meta | M-07, M-08 | Self-critique |
