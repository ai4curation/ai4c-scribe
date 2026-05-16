---
ontology: mondo
issue_number: 5726
pr_number: 10155
eval_repo_pr: 153
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: hard
f1: 0.002
precision: 0.001
recall: 1.0
jaccard: 0.001
outcome: failure
failure_modes: [over_editing, wrong_pattern, scope_creep]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/5726
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10155
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/153
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 5726 --repo monarch-initiative/mondo
    gh pr diff 10155 --repo monarch-initiative/mondo
    gh pr diff 153 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10155 addressed `new_term` for issue #5726: Add non-human animal diseases from VeNom.
Human resolution summary: The PR added 9,006 lines to `src/ontology/mondo-edit.obo` across 3
commits, with zero deletions. Each new term stanza includes a label, definition, VeNom
cross-reference, and classification under the non-human animal disease hierarchy. The scale of this
change required careful curation to map VeNom diagnoses to appropriate Mondo parent classes and to
exclude entries that are phenotypes rather than diseases. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.002 (precision=0.001, recall=1.0). It matched 7/44
accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 7 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/5726" xsd:anyURI`
- Matched accepted addition: `xref: VeNom:2090 {source="MONDO:equivalentTo"}`
- Matched accepted addition: `xref: VeNom:81076 {source="MONDO:equivalentTo"}`
- High recall indicates the agent covered most accepted changes.

## Issues

- Missing accepted changes: 37 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `relationship: disease_has_infectious_agent NCBITaxon:10880 {source="https://orcid.org/0000-0002-5002-8648"}`
- Missing accepted addition: `relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql`
- Missing accepted addition: `relationship: disease_has_infectious_agent NCBITaxon:11974 {source="https://orcid.org/0000-0002-5002-8648"} ! Caliciviridae`
- Missing accepted addition: `relationship: disease_has_infectious_agent NCBITaxon:3044472 {source="https://orcid.org/0000-0002-5002-8648"} ! Orthoherpesviridae`
- Missing accepted addition: `[Term]`
- Overall this is a failure because the accepted edit was largely missed or buried under substantial unrelated change.
