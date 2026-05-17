---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 36
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.5
precision: 0.5
recall: 0.5
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

  Source issue: https://github.com/monarch-initiative/mondo/issues/9937
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10112
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/36
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9937 --repo monarch-initiative/mondo
    gh pr diff 10112 --repo monarch-initiative/mondo
    gh pr diff 36 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10112 addressed `new_term` for issue #9937: NTR/KY. Human resolution summary: Added a new
term stanza to `src/ontology/mondo-edit.obo` with 15 lines. The term includes a definition,
gene-disease logical axioms linking the disease to KY via germline mutation, classification under
the neuromyopathy hierarchy, and appropriate ClinGen provenance annotations. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.5 (precision=0.5, recall=0.5). It matched 5/14
accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 5 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `[Term]`
- Matched accepted addition: `name: KY-related neuromyopathy`
- Matched accepted addition: `intersection_of: MONDO:0100546 ! hereditary neuromuscular disease`
- Matched accepted addition: `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY`

## Issues

- Missing accepted changes: 9 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `is_a: MONDO:1010194 {source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy`
- Missing accepted addition: `relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql`
- Missing accepted addition: `id: MONDO:1010194`
- Missing accepted addition: `def: "Any neuromyopathy in which the cause of the disease is mutation in the KY gene." [https://clinicalgenome.org/affiliation/40151/, https://orci...`
- Missing accepted addition: `synonym: "KY-related neuromyopathy" EXACT [https://clinicalgenome.org/affiliation/40151/] {OMO:0002001="https://w3id.org/information-resource-regis...`
- Extra changes beyond the accepted PR: 9 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `is_a: MONDO:7770012 {source="PMID:27484770", source="PMID:27485408", source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyop...`
- Extra agent addition: `is_a: MONDO:7770012 {source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyop...`
- Extra agent addition: `id: MONDO:7770012`
- Extra agent addition: `def: "Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene." [https://clinicalgenome.org/affiliation...`
- Extra agent addition: `subset: rare`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
