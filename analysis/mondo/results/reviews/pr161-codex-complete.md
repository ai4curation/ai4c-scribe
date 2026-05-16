---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 161
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: simple
f1: 0.533
precision: 0.571
recall: 0.5
jaccard: 0.364
outcome: partial_success
failure_modes: [under_editing, missed_requirement, over_editing, missing_metadata]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9781
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10111
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/161
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9781 --repo monarch-initiative/mondo
    gh pr diff 10111 --repo monarch-initiative/mondo
    gh pr diff 161 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10111 addressed `new_term` for issue #9781: Request for new term [preneoplastic lesion].
Human resolution summary: Added MONDO:1060215 (preneoplastic lesion) to
`src/ontology/mondo-edit.obo` with 8 lines. The term is compact, containing an ID, name, definition,
and parent classification. No logical axioms or complex cross-references were needed for this
grouping term. This attempt changed `src/ontology/mondo-edit.obo` and scored F1=0.533
(precision=0.571, recall=0.5). It matched 3/7 accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 3 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `[Term]`
- Matched accepted addition: `name: preneoplastic lesion`
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9781" xsd:anyURI`

## Issues

- Missing accepted changes: 4 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `id: MONDO:1060215`
- Missing accepted addition: `def: "A precancerous condition characterized by accumulation of some molecular alterations necessary for malignant transformation in a clonal proli...`
- Missing accepted addition: `is_a: MONDO:0021074 {source="PMID:37775701", source="PMID:40684183", source="https://orcid.org/0000-0002-2336-2552"} ! precancerous condition`
- Missing accepted addition: `property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659`
- Extra changes beyond the accepted PR: 5 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `id: MONDO:7770012`
- Extra agent addition: `def: "A precancerous condition characterized by a localized abnormal tissue lesion in which cells have accumulated some, but not all, alterations n...`
- Extra agent addition: `synonym: "pre-neoplastic lesion" EXACT [https://orcid.org/0000-0002-2336-2552]`
- Extra agent addition: `is_a: MONDO:0021074 {source="https://github.com/monarch-initiative/mondo/issues/9781", source="https://orcid.org/0000-0002-2336-2552"} ! precancero...`
- Extra agent addition: `property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
