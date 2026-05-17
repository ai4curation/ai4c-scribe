---
ontology: mondo
issue_number: 9873
pr_number: 10126
eval_repo_pr: 58
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.5
precision: 0.5
recall: 0.5
jaccard: 0.333
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9873
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10126
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/58
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9873 --repo monarch-initiative/mondo
    gh pr diff 10126 --repo monarch-initiative/mondo
    gh pr diff 58 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10126 addressed `new_term` for issue #9873: Request for new term Southern tick-associated
rash illness. Human resolution summary: The PR added 13 lines to `src/ontology/mondo-edit.obo`
introducing a new term stanza classified under MONDO:0025294 "tick-borne infectious disease." The 8
commits reflect review iteration: the initial submission received a CHANGES_REQUESTED review from a
senior curator asking for an updated definition, after which the definition was revised and the PR
was approved. Cross-references to NCIT and SNOMED were included fo... This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.5 (precision=0.5, recall=0.5). It matched 4/12
accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 4 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `[Term]`
- Matched accepted addition: `xref: NCIT:C128427 {source="MONDO:equivalentTo"}`
- Matched accepted addition: `xref: SCTID:444100007 {source="MONDO:equivalentTo"}`
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9873" xsd:anyURI`

## Issues

- Missing accepted changes: 8 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `id: MONDO:1010205`
- Missing accepted addition: `name: southern tick-associated rash illness`
- Missing accepted addition: `def: "A tick-borne infectious disease transmitted by the lone star tick, Amblyomma americanum, and causing an erythema migrans\u2013like rash with ...`
- Missing accepted addition: `synonym: "Masters disease" EXACT [PMID:18452807]`
- Missing accepted addition: `synonym: "STARI" EXACT ABBREVIATION [PMID:18452807]`
- Extra changes beyond the accepted PR: 8 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `id: MONDO:7770018`
- Extra agent addition: `name: Southern tick-associated rash illness`
- Extra agent addition: `def: "A tick-borne infectious disease with acute manifestations similar to Lyme disease, characterized by an erythema migrans-like rash at the site...`
- Extra agent addition: `synonym: "Masters disease" EXACT [PMID:19522220]`
- Extra agent addition: `synonym: "STARI" EXACT ABBREVIATION [PMID:19522220, PMID:36116832, PMID:40267428]`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
