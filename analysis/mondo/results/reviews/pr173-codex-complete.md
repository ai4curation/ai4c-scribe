---
ontology: mondo
issue_number: 9873
pr_number: 10126
eval_repo_pr: 173
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.64
precision: 0.667
recall: 0.615
jaccard: 0.471
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/173
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9873 --repo monarch-initiative/mondo
    gh pr diff 10126 --repo monarch-initiative/mondo
    gh pr diff 173 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10126 addressed `new_term` for issue #9873: Request for new term Southern tick-associated
rash illness. Human resolution summary: The PR added 13 lines to `src/ontology/mondo-edit.obo`
introducing a new term stanza classified under MONDO:0025294 "tick-borne infectious disease." The 8
commits reflect review iteration: the initial submission received a CHANGES_REQUESTED review from a
senior curator asking for an updated definition, after which the definition was revised and the PR
was approved. Cross-references to NCIT and SNOMED were included fo... This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.64 (precision=0.667, recall=0.615). It matched 5/12
accepted additions and 0/0 accepted deletions.

## Strengths

- Matched 5 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `[Term]`
- Matched accepted addition: `name: southern tick-associated rash illness`
- Matched accepted addition: `xref: NCIT:C128427 {source="MONDO:equivalentTo"}`
- Matched accepted addition: `xref: SCTID:444100007 {source="MONDO:equivalentTo"}`

## Issues

- Missing accepted changes: 7 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `id: MONDO:1010205`
- Missing accepted addition: `def: "A tick-borne infectious disease transmitted by the lone star tick, Amblyomma americanum, and causing an erythema migrans\u2013like rash with ...`
- Missing accepted addition: `synonym: "Masters disease" EXACT [PMID:18452807]`
- Missing accepted addition: `synonym: "STARI" EXACT ABBREVIATION [PMID:18452807]`
- Missing accepted addition: `is_a: MONDO:0025294 {source="PMID:19522220", source="PMID:36116832", source="PMID:40267428", source="https://orcid.org/0000-0001-5705-7831"} ! tick...`
- Extra changes beyond the accepted PR: 8 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `id: MONDO:7770018`
- Extra agent addition: `def: "A tick-borne infectious disease characterized by an expanding erythema migrans-like rash and other acute manifestations similar to Lyme disea...`
- Extra agent addition: `subset: ncit {source="NCIT:C128427"}`
- Extra agent addition: `synonym: "Masters disease" EXACT [PMID:17028220]`
- Extra agent addition: `synonym: "STARI" EXACT ABBREVIATION [PMID:36116832]`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
