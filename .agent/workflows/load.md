---
description: 動的モジュールロード - 必要なルールをオンデマンドで読み込む
---

# /load - Dynamic Module Loader

## Usage

```
/load <module_id>    # 単一モジュール
/load G-1 G-3        # 複数モジュール
/load C-4            # Prompt モジュール
```

## Module Reference

### Constitution Layers (dev-rules/constitution/)

| ID | File | Enforcement |
|---|---|---|
| `ORCH` | 00_orchestration.md | L0 (常時) |
| `G-1` | 01_environment.md | L1 |
| `G-2` | 02_logic.md | L1 |
| `G-3` | 03_security.md | L1 |
| `G-4` | 04_lifecycle.md | L2 |
| `G-5` | 05_meta_cognition.md | L0 (常時) |
| `G-6` | 06_style.md | L2 |

### Protocols (dev-rules/prompts/protocols/)

| ID | Name | Priority |
|---|---|---|
| `P01` | DMZ (Protected Assets) | CRITICAL |
| `P02` | Directory Topology Lock | HIGH |
| `P03` | Dependency Quarantine | HIGH |
| `P04` | TDD Enforcement | CRITICAL |
| `P05` | Domain Language | HIGH |
| `P06` | Complexity Budget | HIGH |
| `P07` | Devil's Advocate | CRITICAL |
| `P08` | Cognitive Checkpoint | MEDIUM |
| `P09` | Mutation Testing | ADVANCED |
| `P10` | Ripple Effect Analysis | HIGH |
| `P11` | Red Teaming | CRITICAL |
| `P12` | Chaos Monkey | HIGH |
| `P13` | Code Archaeology | MEDIUM |
| `P14` | Narrative Commit | MEDIUM |
| `P15` | Atomic Design | HIGH |
| `P16` | Accessibility (a11y) | HIGH |
| `P17` | Structured Logging | MEDIUM |
| `P18` | Feature Flags | HIGH |
| `P19` | Docker First | HIGH |
| `P20` | Dead Code Reaper | LOW |
| `P21` | TODO Expiration | LOW |
| `P22` | Auto-Documentation | MEDIUM |
| `P23` | Mock First | HIGH |
| `P24` | Performance Budget | HIGH |
| `P25` | Rollback Strategy | CRITICAL |

### Prompt Modules (dev-rules/prompts/modules/)

| ID | Name |
|---|---|
| `C-1-2` | Adversarial Review |
| `C-3` | Structural Audit |
| `C-4-5` | Code Review |
| `C-6-7` | Prompt Engineering |
| `Q-1` | Feynman Filter |
| `A-9` | First Principles |

## Enforcement Levels

| Level | 意味 | Override |
|---|---|---|
| **L0** | Immutable（絶対） | 不可 |
| **L1** | Enforced（原則遵守） | SUDO_OVERRIDE で一時停止可 |
| **L2** | Recommended（推奨） | 理由を明示すればスキップ可 |
| **L3** | Optional（参考） | 任意適用 |

## Behavior

1. コマンドを受け取ったら、指定されたモジュールファイルを `view_file` で読み込む
2. 読み込んだルールの要約を出力
3. **ACTIVE** モジュールリストを更新

## Example

```
User: /load G-3

Agent: ✅ G-3: Security Protocol をロードしました。
       - M-09: Mutation Testing
       - M-11: Red Teaming (CRITICAL)
       - M-12: Chaos Monkey
       - M-23: Mock First
       - M-24: Performance Budget
       
       [🛡️ ACTIVE: G-5, G-3]
```
