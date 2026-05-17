---
ontology: mondo
issue_number: 9854
pr_number: 10116
eval_repo_pr: 319
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.2
precision: 0.111
recall: 1.0
jaccard: 0.111
outcome: failure
failure_modes:
  - over_editing
  - wrong_pattern
  - scope_creep
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9854
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10116
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/319
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9854 --repo monarch-initiative/mondo
    gh pr diff 10116 --repo monarch-initiative/mondo
    gh pr diff 319 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10116 addressed `other` for issue #9854: Isolated megalencephaly Orphanet Xref. Human
resolution summary: The PR required 3 commits to complete. The first moved the Orphanet xref to the
correct term MONDO:0017089. The second removed a MedDRA xref (MedDRA:10050183) that was also
incorrectly placed on isolated megalencephaly. The third commit addressed the source annotation for
the MedDRA xref, as the curator was uncertain which source to assign after removing the Orphanet
provenance link. This attempt changed `src/ontology/mondo-edit.obo` and scored F1=0.2
(precision=0.111, recall=1.0). It matched 1/11 accepted additions and 1/8 accepted deletions.

## Strengths

- Matched 2 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `xref: Orphanet:2477 {source="MONDO:equivalentTo"}`
- Matched accepted deletion: `xref: Orphanet:2477 {source="MONDO:equivalentTo"}`
- High recall indicates the agent covered most accepted changes.

## Issues

- Missing accepted changes: 10 additions and 7 deletions from the human PR were not reproduced.
- Missing accepted addition: `xref: ICD10CM:Q04.5 {source="https://orcid.org/0009-0001-6494-4831", source="MONDO:equivalentTo", source="https://orcid.org/0000-0002-5002-8648"}`
- Missing accepted addition: `xref: icd11.foundation:368780653 {source="MONDO:equivalentTo"}`
- Missing accepted addition: `xref: MedDRA:10050183 {source="MONDO:equivalentTo"}`
- Missing accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9854" xsd:anyURI`
- Missing accepted addition: `subset: ordo_disorder {source="Orphanet:2477"}`
- Missing accepted deletion: `subset: ordo_disorder {source="Orphanet:2477"}`
- Missing accepted deletion: `subset: ordo_malformation_syndrome {source="Orphanet:2477"}`
- Missing accepted deletion: `subset: orphanet {source="Orphanet:2477"}`
- Missing accepted deletion: `subset: orphanet_rare {source="Orphanet:2477"}`
- Overall this is a failure because the accepted edit was largely missed or buried under substantial unrelated change.
