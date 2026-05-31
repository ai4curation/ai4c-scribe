---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 421
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: simple
f1: 0.429
precision: 0.429
recall: 0.429
jaccard: 0.273
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9781
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10111
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/421
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9781 --repo monarch-initiative/mondo
    gh pr diff 10111 --repo monarch-initiative/mondo
    gh pr diff 421 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10111 addressed `new_term` for issue #9781: Request for new term [preneoplastic lesion].
Human resolution summary: Added MONDO:1060215 (preneoplastic lesion) to
`src/ontology/mondo-edit.obo` with 8 lines. The term is compact, containing an ID, name, definition,
and parent classification. No logical axioms or complex cross-references were needed for this
grouping term. This attempt changed `src/ontology/mondo-edit.obo` and scored F1=0.429
(precision=0.429, recall=0.429). It matched 2/7 accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 2 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `[Term]`
- Matched accepted addition: `name: preneoplastic lesion`

## Issues

- Missing accepted changes: 5 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `id: MONDO:1060215`
- Missing accepted addition: `def: "A precancerous condition characterized by accumulation of some molecular alterations necessary for malignant transformation in a clonal proli...`
- Missing accepted addition: `is_a: MONDO:0021074 {source="PMID:37775701", source="PMID:40684183", source="https://orcid.org/0000-0002-2336-2552"} ! precancerous condition`
- Missing accepted addition: `property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659`
- Missing accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9781" xsd:anyURI`
- Extra changes beyond the accepted PR: 5 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `id: MONDO:7770012`
- Extra agent addition: `def: "A clonal proliferation of cells that have accumulated some, but not all, molecular alterations necessary for malignant transformation, repres...`
- Extra agent addition: `is_a: MONDO:0021074 ! precancerous condition`
- Extra agent addition: `property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-2336-2552`
- Extra agent addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9781" xsd:string`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
