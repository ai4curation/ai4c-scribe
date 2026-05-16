---
ontology: mondo
issue_number: 5726
pr_number: 10155
eval_repo_pr: 71
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: hard
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/5726
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10155
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/71
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 5726 --repo monarch-initiative/mondo
    gh pr diff 10155 --repo monarch-initiative/mondo
    gh pr diff 71 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10155 addressed `new_term` for issue #5726: Add non-human animal diseases from VeNom.
Human resolution summary: The PR added 9,006 lines to `src/ontology/mondo-edit.obo` across 3
commits, with zero deletions. Each new term stanza includes a label, definition, VeNom
cross-reference, and classification under the non-human animal disease hierarchy. The scale of this
change required careful curation to map VeNom diagnoses to appropriate Mondo parent classes and to
exclude entries that are phenotypes rather than diseases. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=1.0 (precision=1.0, recall=1.0). It matched 44/44
accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 44 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `relationship: disease_has_infectious_agent NCBITaxon:10880 {source="https://orcid.org/0000-0002-5002-8648"}`
- Matched accepted addition: `relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql`
- Matched accepted addition: `relationship: disease_has_infectious_agent NCBITaxon:11974 {source="https://orcid.org/0000-0002-5002-8648"} ! Caliciviridae`
- Matched accepted addition: `relationship: disease_has_infectious_agent NCBITaxon:3044472 {source="https://orcid.org/0000-0002-5002-8648"} ! Orthoherpesviridae`
- High precision indicates the agent mostly edited within the accepted change surface.
- High recall indicates the agent covered most accepted changes.

## Issues

- Extra changes beyond the accepted PR: 5986 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `subset: venom_equine {source="VeNom:81073"}`
- Extra agent addition: `subset: venom_farm_animal {source="VeNom:81073"}`
- Extra agent addition: `xref: VeNom:81073 {source="MONDO:equivalentTo"}`
- Extra agent addition: `id: MONDO:1013000`
- Extra agent addition: `name: liver abscess (disease), non-human animal`
- Overall this is a successful attempt; any differences above are minor relative to the requested curation.
