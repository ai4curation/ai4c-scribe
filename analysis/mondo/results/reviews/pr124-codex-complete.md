---
ontology: mondo
issue_number: 9896
pr_number: 10207
eval_repo_pr: 124
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.235
precision: 0.5
recall: 0.154
jaccard: 0.133
outcome: failure
failure_modes: [under_editing, missed_requirement, over_editing, wrong_pattern, missed_synonym]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9896
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10207
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/124
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9896 --repo monarch-initiative/mondo
    gh pr diff 10207 --repo monarch-initiative/mondo
    gh pr diff 124 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10207 addressed `synonym_update` for issue #9896: GCSH-related glycine encephalopathy.
Human resolution summary: The PR was completed in 2 commits. The first added "GCSH-related glycine
encephalopathy" as an exact synonym to MONDO:0957382. The second commit removed an incorrect subset
annotation that was discovered during the initial edit. The net result is 4 additions with no
deletions, adding the synonym and cleaning up metadata. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.235 (precision=0.5, recall=0.154). It matched 2/4
accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 2 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `synonym: "GCSH-related glycine encephalopathy" EXACT [https://clinicalgenome.org/affiliation/40011/, https://orcid.org/0000-0002-7437-8060] {OMO:00...`
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9896" xsd:anyURI`

## Issues

- Missing accepted changes: 2 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `def: "Any multiple mitochondrial dysfunctions syndrome in which the cause of the disease is a mutation in the GCSH gene. It is characterized by a c...`
- Missing accepted addition: `is_a: MONDO:0011612 {source="https://clinicalgenome.org/affiliation/40011/"} ! glycine encephalopathy`
- Extra changes beyond the accepted PR: 9 additions and 2 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `name: GCSH-related glycine encephalopathy`
- Extra agent addition: `def: "Any glycine encephalopathy in which the cause of the disease is a mutation in the GCSH gene." [https://clinicalgenome.org/affiliation/40011/,...`
- Extra agent addition: `subset: clingen {source="MONDO:CLINGEN"}`
- Extra agent addition: `synonym: "multiple mitochondrial dysfunctions syndrome 7" EXACT [OMIM:620423]`
- Extra agent addition: `is_a: MONDO:0011612 {source="https://clinicalgenome.org/affiliation/40011/", source="https://orcid.org/0000-0002-7437-8060"} ! glycine encephalopathy`
- Extra agent deletion: `name: multiple mitochondrial dysfunctions syndrome 7`
- Extra agent deletion: `relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4208 {source="OMIM:620423"} ! GCSH`
- Overall this is a failure because the accepted edit was largely missed or buried under substantial unrelated change.
