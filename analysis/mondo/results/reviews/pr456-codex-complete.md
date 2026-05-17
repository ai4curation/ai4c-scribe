---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 456
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.615
precision: 0.545
recall: 0.706
jaccard: 0.444
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9826
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10142
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/456
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9826 --repo monarch-initiative/mondo
    gh pr diff 10142 --repo monarch-initiative/mondo
    gh pr diff 456 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10142 addressed `obsoletion` for issue #9826: [Merge] short-rib thoracic dysplasia 22
without polydactyly & thoracic dysostosis, isolated. Human resolution summary: The PR obsoleted
MONDO:0008549 and merged its metadata into MONDO:0979242. The 13 additions include obsoletion
annotations on the source term (replaced_by pointing to MONDO:0979242) and an added definition for
the surviving term. The 9 deletions remove the active classification axioms and synonyms from the
obsoleted term. All changes are confined to `src/ontology/mondo-edit.obo`. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.615 (precision=0.545, recall=0.706). It matched 4/13
accepted additions and 8/9 accepted deletions.

## Strengths

- Matched 12 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: obsolete thoracic dysostosis, isolated`
- Matched accepted addition: `property_value: IAO:0000231 MONDO:TermsMerged`
- Matched accepted addition: `is_obsolete: true`
- Matched accepted addition: `replaced_by: MONDO:0979242`
- Matched accepted deletion: `name: thoracic dysostosis, isolated`
- Matched accepted deletion: `comment: This term is scheduled to be merged with MONDO:0979242 short-rib thoracic dysplasia 22 without polydactyly, based on the fact that the con...`
- Matched accepted deletion: `subset: obsoletion_candidate`

## Issues

- Missing accepted changes: 9 additions and 1 deletions from the human PR were not reproduced.
- Missing accepted addition: `def: "Any Jeune syndrome in which the cause of the disease is a mutation in the FGF4 gene, characterized by a small thorax with short ribs, resulti...`
- Missing accepted addition: `synonym: "thoracic dysostosis, isolated" EXACT [OMIM:187750]`
- Missing accepted addition: `xref: MESH:C566063 {source="MONDO:equivalentTo"}`
- Missing accepted addition: `xref: OMIM:187750 {source="MONDO:equivalentObsolete"}`
- Missing accepted addition: `is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease`
- Missing accepted deletion: `synonym: "thoracic dysostosis, isolated" EXACT []`
- Extra changes beyond the accepted PR: 5 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `xref: MESH:C566063 {source="MONDO:obsoleteEquivalent"}`
- Extra agent addition: `xref: OMIM:187750 {source="MONDO:obsoleteEquivalent"}`
- Extra agent addition: `property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659`
- Extra agent addition: `synonym: "thoracic dysostosis, isolated" EXACT [MONDO:0008549]`
- Extra agent addition: `xref: MESH:C566063 {source="MONDO:equivalentTo", source="MONDO:0008549"}`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
