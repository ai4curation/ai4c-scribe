---
ontology: mondo
issue_number: 9877
pr_number: 10123
eval_repo_pr: 59
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.545
precision: 0.667
recall: 0.462
jaccard: 0.375
outcome: partial_success
failure_modes: [under_editing, missed_requirement, over_editing, missing_metadata]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9877
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10123
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/59
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9877 --repo monarch-initiative/mondo
    gh pr diff 10123 --repo monarch-initiative/mondo
    gh pr diff 59 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10123 addressed `new_term` for issue #9877: GPR161-related medulloblastoma
predisposition. Human resolution summary: Added a new term stanza to `src/ontology/mondo-edit.obo`
with 10 lines. The term includes a definition, gene-disease logical axioms linking to GPR161, and
classification under the cancer predisposition hierarchy. The compact size reflects a
well-structured new term following established patterns. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.545 (precision=0.667, recall=0.462). It matched 5/9
accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 5 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `[Term]`
- Matched accepted addition: `name: GPR161-related medulloblastoma predisposition`
- Matched accepted addition: `synonym: "GPR161-related medulloblastoma predisposition" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/infor...`
- Matched accepted addition: `relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 {source="https://clinicalgenome.org/affiliation/40157/"}`

## Issues

- Missing accepted changes: 4 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `id: MONDO:1010204`
- Missing accepted addition: `def: "A predisposition to medulloblastoma, a tumor that originates in the cerebellum and dorsal brainstem, has a peak incidence in childhood, and m...`
- Missing accepted addition: `is_a: MONDO:0015356 {source="https://clinicalgenome.org/affiliation/40157/"} ! hereditary neoplastic syndrome`
- Missing accepted addition: `property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648`
- Extra changes beyond the accepted PR: 8 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `id: MONDO:7770012`
- Extra agent addition: `def: "A susceptibility or predisposition to medulloblastoma in which the cause of the disease is a mutation in the GPR161 gene." [https://clinicalg...`
- Extra agent addition: `synonym: "medulloblastoma susceptibility, GPR161 form" EXACT [MONDO:patterns/susceptibility_by_gene]`
- Extra agent addition: `is_a: MONDO:0020573 {source="https://clinicalgenome.org/affiliation/40157/"} ! inherited disease susceptibility`
- Extra agent addition: `intersection_of: MONDO:0020573 ! inherited disease susceptibility`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
