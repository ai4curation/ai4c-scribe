---
ontology: mondo
issue_number: 9963
pr_number: 10222
eval_repo_pr: 67
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.583
precision: 0.7
recall: 0.5
jaccard: 0.412
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/67
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9963 --repo monarch-initiative/mondo
    gh pr diff 10222 --repo monarch-initiative/mondo
    gh pr diff 67 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10222 addressed `new_term` for issue #9963: RNU12 - related minor spliceopathy disorder.
Human resolution summary: Added a single new term stanza to `src/ontology/mondo-edit.obo` with 15
lines of additions. The term includes a definition, logical axioms linking to RNU12 via germline
mutation, and appropriate classification. This is a straightforward new term addition following
established Mondo patterns for gene-disease terms. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.583 (precision=0.7, recall=0.5). It matched 8/14
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
- Missing accepted addition: `property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659`
- Extra changes beyond the accepted PR: 10 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `is_a: MONDO:7770747 {source="PMID:39802771", source="https://clinicalgenome.org/affiliation/40060/"} ! RNU12-related minor spliceopathy disorder`
- Extra agent addition: `id: MONDO:7770747`
- Extra agent addition: `def: "A hereditary disease caused by pathogenic variation in RNU12 that disrupts minor spliceosome-mediated pre-mRNA splicing. The disease spectrum...`
- Extra agent addition: `subset: clingen {source="MONDO:CLINGEN"}`
- Extra agent addition: `subset: rare`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
