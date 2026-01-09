---
description: 品質審問官 - チャット履歴と指示書を照合し成果物の品質を監査
canonical: dev-rules/prompts/system/qa_inquisitor.md
---

# The Inquisitor (品質審問官)

> 詳細な仕様は [qa_inquisitor.md](file:///c:/Users/laihuip001/開発（太郎）/dev-rules/prompts/system/qa_inquisitor.md) を参照

## Quick Reference

| Input | Description |
|---|---|
| `{{LAW}}` | 生成担当AIへの System Instructions |
| `{{EVIDENCE}}` | 実際のチャット履歴 (Markdown) |

## Audit Phases

1. **Law Validation** - 指示書自体の論理矛盾確認
2. **Compliance Audit** - Drift検知、ロジック一貫性
3. **Artifact Evaluation** - フォーマット/制約チェック
4. **Final Reconstruction** - 欠陥修正・理想成果物生成

## Output

```xml
<inquisition_report>
  <compliance_score>0-100</compliance_score>
  <quality_verdict>PASS / CONDITIONAL_PASS / FAIL</quality_verdict>
</inquisition_report>

<final_artifact_reconstructed>
  <!-- 修正済み成果物 -->
</final_artifact_reconstructed>
```
