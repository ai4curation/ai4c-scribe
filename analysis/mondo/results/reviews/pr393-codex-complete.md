---
ontology: mondo
issue_number: 9826
pr_number: 10142
eval_repo_pr: 393
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.872
precision: 0.773
recall: 1.0
jaccard: 0.773
outcome: partial_success
failure_modes: [over_editing]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9826
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10142
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/393
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9826 --repo monarch-initiative/mondo
    gh pr diff 10142 --repo monarch-initiative/mondo
    gh pr diff 393 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10142 addressed `obsoletion` for issue #9826: [Merge] short-rib thoracic dysplasia 22
without polydactyly & thoracic dysostosis, isolated. Human resolution summary: The PR obsoleted
MONDO:0008549 and merged its metadata into MONDO:0979242. The 13 additions include obsoletion
annotations on the source term (replaced_by pointing to MONDO:0979242) and an added definition for
the surviving term. The 9 deletions remove the active classification axioms and synonyms from the
obsoleted term. All changes are confined to `src/ontology/mondo-edit.obo`. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.872 (precision=0.773, recall=1.0). It matched 8/13
accepted additions and 9/9 accepted deletions.

## Strengths

- Matched 17 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: obsolete thoracic dysostosis, isolated`
- Matched accepted addition: `property_value: IAO:0000231 MONDO:TermsMerged`
- Matched accepted addition: `is_obsolete: true`
- Matched accepted addition: `replaced_by: MONDO:0979242`
- Matched accepted deletion: `name: thoracic dysostosis, isolated`
- Matched accepted deletion: `comment: This term is scheduled to be merged with MONDO:0979242 short-rib thoracic dysplasia 22 without polydactyly, based on the fact that the con...`
- Matched accepted deletion: `subset: obsoletion_candidate`
- High recall indicates the agent covered most accepted changes.

## Issues

- Missing accepted changes: 5 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `def: "Any Jeune syndrome in which the cause of the disease is a mutation in the FGF4 gene, characterized by a small thorax with short ribs, resulti...`
- Missing accepted addition: `is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease`
- Missing accepted addition: `intersection_of: MONDO:0018770 ! Jeune syndrome`
- Missing accepted addition: `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/3682 ! FGF4`
- Missing accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9826" xsd:anyURI`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
