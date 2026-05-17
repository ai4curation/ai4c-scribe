---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 383
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.571
precision: 0.667
recall: 0.5
jaccard: 0.4
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9937
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10112
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/383
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9937 --repo monarch-initiative/mondo
    gh pr diff 10112 --repo monarch-initiative/mondo
    gh pr diff 383 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10112 addressed `new_term` for issue #9937: NTR/KY. Human resolution summary: Added a new
term stanza to `src/ontology/mondo-edit.obo` with 15 lines. The term includes a definition,
gene-disease logical axioms linking the disease to KY via germline mutation, classification under
the neuromyopathy hierarchy, and appropriate ClinGen provenance annotations. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.571 (precision=0.667, recall=0.5). It matched 7/14
accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 7 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `[Term]`
- Matched accepted addition: `name: KY-related neuromyopathy`
- Matched accepted addition: `synonym: "KY-related neuromyopathy" EXACT [https://clinicalgenome.org/affiliation/40151/] {OMO:0002001="https://w3id.org/information-resource-regis...`
- Matched accepted addition: `is_a: MONDO:0100546 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! hereditary neuromusc...`

## Issues

- Missing accepted changes: 7 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `is_a: MONDO:1010194 {source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy`
- Missing accepted addition: `relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql`
- Missing accepted addition: `id: MONDO:1010194`
- Missing accepted addition: `def: "Any neuromyopathy in which the cause of the disease is mutation in the KY gene." [https://clinicalgenome.org/affiliation/40151/, https://orci...`
- Missing accepted addition: `property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648`
- Extra changes beyond the accepted PR: 11 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyop...`
- Extra agent addition: `id: MONDO:7770012`
- Extra agent addition: `def: "Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene." [https://clinicalgenome.org/affiliation...`
- Extra agent addition: `subset: clingen {source="MONDO:CLINGEN"}`
- Extra agent addition: `subset: disease_grouping`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
