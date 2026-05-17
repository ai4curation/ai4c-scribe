---
ontology: mondo
issue_number: 9707
pr_number: 9745
eval_repo_pr: 89
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: hard
f1: 0.311
precision: 0.292
recall: 0.333
jaccard: 0.184
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9707
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/9745
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/89
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9707 --repo monarch-initiative/mondo
    gh pr diff 9745 --repo monarch-initiative/mondo
    gh pr diff 89 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #9745 addressed `new_term` for issue #9707: Mondo request for SCN5A disease entity for
ClinGen. Human resolution summary: Added two new SCN5A-related disease terms to
`src/ontology/mondo-edit.obo` with associated child terms (40 additions), and reclassified
"atrioventricular dissociation" by updating its parent (1 deletion to remove the old parent). The 2
commits reflect the new term additions and the parent reclassification as separate logical changes.
This attempt changed `src/ontology/mondo-edit.obo` and scored F1=0.311 (precision=0.292,
recall=0.333). It matched 6/38 accepted additions and 0/1 accepted deletions.

## Strengths

- Matched 6 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `[Term]`
- Matched accepted addition: `name: cardiogenetic rhythm disorder`
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9707" xsd:anyURI`
- Matched accepted addition: `name: SCN5A-related cardiac rhythm disorder`

## Issues

- Missing accepted changes: 32 additions and 1 deletions from the human PR were not reproduced.
- Missing accepted addition: `is_a: MONDO:1010180 {source="https://www.clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder`
- Missing accepted addition: `is_a: MONDO:0100042 {source="https://www.ncbi.nlm.nih.gov/books/NBK563205/"} ! cardiac conduction defect`
- Missing accepted addition: `relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql`
- Missing accepted addition: `relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/mondo/qc-omim-subsumption.sparql`
- Missing accepted addition: `relationship: excluded_subClassOf MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432", source="https://orcid.org/0000-0002-5002-8648"} ! ...`
- Missing accepted deletion: `is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease`
- Extra changes beyond the accepted PR: 31 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `is_a: MONDO:7770003 {source="https://clinicalgenome.org/affiliation/40104/"} ! cardiogenetic rhythm disorder`
- Extra agent addition: `is_a: MONDO:7770004 {source="https://clinicalgenome.org/affiliation/40104/"} ! SCN5A-related cardiac rhythm disorder`
- Extra agent addition: `id: MONDO:7770003`
- Extra agent addition: `def: "A heterogeneous group of cardiac rhythm phenotypes with a monogenic etiology that include, but are not limited to, atrial fibrillation, sick ...`
- Extra agent addition: `synonym: "cardiogenetic rhythm disorders" EXACT [https://clinicalgenome.org/affiliation/40104/]`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
