---
ontology: mondo
issue_number: 10149
pr_number: 10156
eval_repo_pr: 392
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.381
precision: 0.333
recall: 0.444
jaccard: 0.235
outcome: partial_success
failure_modes: [under_editing, missed_requirement, over_editing, missing_metadata]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/10149
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10156
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/392
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 10149 --repo monarch-initiative/mondo
    gh pr diff 10156 --repo monarch-initiative/mondo
    gh pr diff 392 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10156 addressed `new_term` for issue #10149: Request for new term [podocytopathy]. Human
resolution summary: Added the new term "podocytopathy" to `src/ontology/mondo-edit.obo` with 17
lines of additions. The PR created the parent term with a definition and also reclassified three
existing disease terms as children of the new grouping class. No lines were deleted, indicating
clean additions to the hierarchy. This attempt changed `src/ontology/mondo-edit.obo` and scored
F1=0.381 (precision=0.333, recall=0.444). It matched 6/16 accepted additions and 0/0 accepted
deletions.

## Strengths

- Matched 6 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10149" xsd:anyURI`
- Matched accepted addition: `[Term]`
- Matched accepted addition: `name: podocytopathy`

## Issues

- Missing accepted changes: 10 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `is_a: MONDO:0700328 {source="PMID:41381622"} ! podocytopathy`
- Missing accepted addition: `is_a: MONDO:0700328 {source="PMID:17699461", source="PMID:25684864", source="PMID:38804512", source="PMID:41381622"} ! podocytopathy`
- Missing accepted addition: `id: MONDO:0700328`
- Missing accepted addition: `def: "A glomerular disorder caused by the structural or functional impairment of podocytes, which leads to proteinuria and often nephrotic syndrome...`
- Missing accepted addition: `xref: SCTID:1367669003 {source="MONDO:equivalentTo"}`
- Extra changes beyond the accepted PR: 7 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `is_a: MONDO:7770018 {source="https://github.com/monarch-initiative/mondo/issues/10149", source="https://orcid.org/0009-0009-0876-0331", source="PMI...`
- Extra agent addition: `id: MONDO:7770018`
- Extra agent addition: `def: "A group of glomerular diseases caused by the structural or functional impairment of podocytes which drive proteinuria or nephrotic syndrome."...`
- Extra agent addition: `synonym: "podocytopathies" EXACT [PMID:32792490]`
- Extra agent addition: `is_a: MONDO:0019722 {source="https://orcid.org/0009-0009-0876-0331", source="PMID:25684864", source="PMID:32792490"} ! glomerular disorder`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
