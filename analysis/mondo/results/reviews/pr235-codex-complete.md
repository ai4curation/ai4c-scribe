---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 235
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.001
precision: 0.727
recall: 0.0
jaccard: 0.0
outcome: failure
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9826
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10142
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/235
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9826 --repo monarch-initiative/mondo
    gh pr diff 10142 --repo monarch-initiative/mondo
    gh pr diff 235 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10142 addressed `obsoletion` for issue #9826: [Merge] short-rib thoracic dysplasia 22
without polydactyly & thoracic dysostosis, isolated. Human resolution summary: The PR obsoleted
MONDO:0008549 and merged its metadata into MONDO:0979242. The 13 additions include obsoletion
annotations on the source term (replaced_by pointing to MONDO:0979242) and an added definition for
the surviving term. The 9 deletions remove the active classification axioms and synonyms from the
obsoleted term. All changes are confined to `src/ontology/mondo-edit.obo`. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.001 (precision=0.727, recall=0.0). It matched 7/13
accepted additions and 9/9 accepted deletions.

## Strengths

- Matched 16 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: obsolete thoracic dysostosis, isolated`
- Matched accepted addition: `property_value: IAO:0000231 MONDO:TermsMerged`
- Matched accepted addition: `is_obsolete: true`
- Matched accepted addition: `replaced_by: MONDO:0979242`
- Matched accepted deletion: `name: thoracic dysostosis, isolated`
- Matched accepted deletion: `comment: This term is scheduled to be merged with MONDO:0979242 short-rib thoracic dysplasia 22 without polydactyly, based on the fact that the con...`
- Matched accepted deletion: `subset: obsoletion_candidate`

## Issues

- Missing accepted changes: 6 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `def: "Any Jeune syndrome in which the cause of the disease is a mutation in the FGF4 gene, characterized by a small thorax with short ribs, resulti...`
- Missing accepted addition: `synonym: "thoracic dysostosis, isolated" EXACT [OMIM:187750]`
- Missing accepted addition: `is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease`
- Missing accepted addition: `intersection_of: MONDO:0018770 ! Jeune syndrome`
- Missing accepted addition: `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/3682 ! FGF4`
- Extra changes beyond the accepted PR: 41284 additions and 41282 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `property_value: http://xmlns.com/foaf/0.1/homepage http://obofoundry.org/ontology/mondo.html xsd:anyURI`
- Extra agent addition: `owl-axioms: Prefix(owl:=<http://www.w3.org/2002/07/owl#>)\nPrefix(rdf:=<http://www.w3.org/1999/02/22-rdf-syntax-ns#>)\nPrefix(xml:=<http://www.w3.o...`
- Extra agent addition: `property_value: curated_content_resource https://www.malacards.org/card/adrenal_cortical_hypofunction xsd:anyURI {source="MONDO:MalaCards"}`
- Extra agent addition: `property_value: IAO:0000233 https://github.com/monarch-initiative/mondo/issues/6877 xsd:anyURI`
- Extra agent addition: `property_value: curated_content_resource https://www.malacards.org/card/blood_platelet_disease xsd:anyURI {source="MONDO:MalaCards"}`
- Extra agent deletion: `property_value: http://xmlns.com/foaf/0.1/homepage "http://obofoundry.org/ontology/mondo.html" xsd:anyURI`
- Extra agent deletion: `property_value: curated_content_resource "https://www.malacards.org/card/adrenal_cortical_hypofunction" xsd:anyURI {source="MONDO:MalaCards"}`
- Extra agent deletion: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6877" xsd:anyURI`
- Extra agent deletion: `property_value: curated_content_resource "https://www.malacards.org/card/blood_platelet_disease" xsd:anyURI {source="MONDO:MalaCards"}`
- Overall this is a failure because the accepted edit was largely missed or buried under substantial unrelated change.
