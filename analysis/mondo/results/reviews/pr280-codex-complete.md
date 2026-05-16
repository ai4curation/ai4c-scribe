---
ontology: mondo
issue_number: 9859
pr_number: 10219
eval_repo_pr: 280
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: reclassification
difficulty: hard
f1: 0.235
precision: 0.146
recall: 0.6
jaccard: 0.133
outcome: failure
failure_modes: [under_editing, missed_requirement, over_editing, wrong_pattern]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9859
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10219
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/280
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9859 --repo monarch-initiative/mondo
    gh pr diff 10219 --repo monarch-initiative/mondo
    gh pr diff 280 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10219 addressed `reclassification` for issue #9859: primary hypophysitis synonyms. Human
resolution summary: The PR relabeled MONDO:0019835 to "lymphocytic hypophysitis" and restructured
all histological and anatomical subtypes as child terms under the main hypophysitis term. With 6
commits, 45 additions and 18 deletions, this involved modifying multiple term stanzas to correct
parent-child relationships and update labels. This attempt changed `src/ontology/mondo-edit.obo` and
scored F1=0.235 (precision=0.146, recall=0.6). It matched 13/42 accepted additions and 2/18 accepted
deletions.

## Strengths

- Matched 15 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9859" xsd:anyURI`
- Matched accepted addition: `name: lymphocytic hypophysitis`
- Matched accepted addition: `[Term]`
- Matched accepted deletion: `synonym: "autoimmune hypophysitis" EXACT [NCIT:C132055, Orphanet:95506]`
- Matched accepted deletion: `synonym: "lymphocytic hypophysitis" EXACT [NCIT:C132055]`

## Issues

- Missing accepted changes: 29 additions and 16 deletions from the human PR were not reproduced.
- Missing accepted addition: `def: "A hypophysitis characterized by an inflammation of the posterior pituitary and the stalk. The major clinical manifestation is diabetes insipi...`
- Missing accepted addition: `is_a: MONDO:0021156 {source="Orphanet:238305"} ! hypophysitis`
- Missing accepted addition: `def: "An autoimmune condition affecting the pituitary gland, characterized by lymphocytic infiltration, commonly presenting with pituitary hormone ...`
- Missing accepted addition: `synonym: "autoimmune hypophysitis" EXACT [NCIT:C132055]`
- Missing accepted addition: `synonym: "primary hypophysitis" RELATED [PMID:34528683]`
- Missing accepted deletion: `is_a: MONDO:0019835 {source="Orphanet:238305"} ! primary hypophysitis`
- Missing accepted deletion: `name: primary hypophysitis`
- Missing accepted deletion: `def: "Immune-mediated inflammation of the pituitary gland often associated with other autoimmune diseases (e.g., hashimoto disease; graves disease;...`
- Missing accepted deletion: `subset: disease_grouping`
- Extra changes beyond the accepted PR: 5 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `id: MONDO:7770747`
- Extra agent addition: `def: "An autoimmune inflammatory disorder of the pituitary gland characterized by lymphocytic infiltration. It is the most common histopathological...`
- Extra agent addition: `synonym: "autoimmune hypophysitis" EXACT [PMID:29547162, PMID:32965926]`
- Extra agent addition: `is_a: MONDO:0019835 {source="PMID:29547162", source="PMID:32965926"} ! primary hypophysitis`
- Extra agent addition: `property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3`
- Overall this is a failure because the accepted edit was largely missed or buried under substantial unrelated change.
