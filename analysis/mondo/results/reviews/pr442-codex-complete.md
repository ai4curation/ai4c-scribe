---
ontology: mondo
issue_number: 9963
pr_number: 10222
eval_repo_pr: 442
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.5
precision: 0.7
recall: 0.389
jaccard: 0.333
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9963
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10222
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/442
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9963 --repo monarch-initiative/mondo
    gh pr diff 10222 --repo monarch-initiative/mondo
    gh pr diff 442 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10222 addressed `new_term` for issue #9963: RNU12 - related minor spliceopathy disorder.
Human resolution summary: Added a single new term stanza to `src/ontology/mondo-edit.obo` with 15
lines of additions. The term includes a definition, logical axioms linking to RNU12 via germline
mutation, and appropriate classification. This is a straightforward new term addition following
established Mondo patterns for gene-disease terms. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.5 (precision=0.7, recall=0.389). It matched 8/14
accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 8 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9963" xsd:anyURI`
- Matched accepted addition: `relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19380 {source="PMID:39802771", source="https://clinicalgenome....`
- Matched accepted addition: `[Term]`
- Matched accepted addition: `name: RNU12-related minor spliceopathy disorder`

## Issues

- Missing accepted changes: 6 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `is_a: MONDO:1060223 {source="PMID:39802771", source="https://clinicalgenome.org/affiliation/40060/"} ! RNU12-related minor spliceopathy disorder`
- Missing accepted addition: `id: MONDO:1060223`
- Missing accepted addition: `def: "Any hereditary disease caused by a variation in the RNU12 gene, resulting in abnormal splicing of pre-mRNA via the minor spliceosome. The phe...`
- Missing accepted addition: `synonym: "RNU12-related minor spliceopathy disorder" EXACT [https://clinicalgenome.org/affiliation/40060/] {OMO:0002001="https://w3id.org/informati...`
- Missing accepted addition: `is_a: MONDO:0003847 {source="PMID:39802771", source="https://clinicalgenome.org/affiliation/40060/"} ! hereditary disease`
- Extra changes beyond the accepted PR: 14 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `is_a: MONDO:7770747 {source="PMID:39802771", source="https://clinicalgenome.org/affiliation/40060/"} ! RNU12-related minor spliceopathy disorder`
- Extra agent addition: `id: MONDO:7770747`
- Extra agent addition: `def: "Any hereditary disease in which the cause of the disease is a mutation in the RNU12 gene. This condition is characterized by abnormal splicin...`
- Extra agent addition: `subset: rare`
- Extra agent addition: `synonym: "CDAGS syndrome" RELATED [https://clinicalgenome.org/affiliation/40060/]`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
