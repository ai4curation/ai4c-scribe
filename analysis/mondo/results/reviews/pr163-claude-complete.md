---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 163
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.464
precision: 0.707
recall: 0.345
jaccard: 0.302
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Issue #9795 explicitly requests four OMIM-driven term merges; the human resolved it across four PRs (#10107, #10108, #10109, #10110). The metadiff scores only against #10110 (the Usher syndrome type 1J → MONDO:0012273 sub-step), so the three correct companion merges count as 'extra' and floor recall for every attempt. F1 ~0.46 here grossly under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is a **poor evaluation case**: issue #9795 explicitly asks for four term merges (MONDO:0009027→MONDO:0007402, MONDO:0011961→MONDO:0044720, MONDO:0010553→MONDO:0010549, MONDO:0013935→MONDO:0012273) and the human curator (MeeSiing) split the work into four PRs. The scored gold PR #10110 is only the Usher syndrome 1J sub-step. This attempt correctly performed **all four** merges requested by the issue, so the headline F1=0.464 (the best of all 16 attempts) substantially under-represents its quality — most of the "extra" 16 additions / 52 deletions penalising recall are the three legitimate companion merges. Judged against the issue's actual ask, this is a strong, complete resolution.

## Strengths

- Addressed every one of the four merges named in the issue table, with the correct `replaced_by` targets, matching the issue's own "Suggested term to consider" list exactly.
- Each obsolete stanza reduced to the canonical merge skeleton: `name: obsolete ...`, `property_value: IAO:0000231 MONDO:TermsMerged`, the `IAO:0000233` issue link, `is_obsolete: true`, `replaced_by:` — exactly matching the gold pattern used in #10110 for MONDO:0013935.
- On the Usher sub-step that is actually scored, it matched the high-value diff lines (`name: obsolete Usher syndrome type 1J`, `IAO:0000231 MONDO:TermsMerged`, `is_obsolete: true`, removal of the def/comment/obsoletion_candidate metadata).
- Conservative, defensible scoping choice: deliberately did NOT transfer historical/incorrect parent axioms onto survivors and only carried forward legacy OMIM IDs as `xref ... {source="MONDO:obsoleteEquivalent"}` — this avoids the syndromic-vs-nonsyndromic misclassification that is the stated crux of the case's "medium" difficulty.
- Ran `make NORM`, `robot convert` syntax validation, and six targeted merge QC SPARQL queries (proxy-merge, misused-replaced-by, obsoletion-reason, deprecated-class-reference, xref-without-precision, duplicate-exact-synonym) with 0 violations.

## Issues

- Even on the scored Usher portion, it did not reproduce three human stylistic choices in #10110: the human added `source="MONDO:preferredExternal"` to MEDGEN:332149 / UMLS:C1836199, deleted the two NARROW synonyms `autosomal recessive deafness 48` / `autosomal recessive nonsyndromic deafness 48`, and used `[OMIM:609439]` (the survivor's own OMIM) as evidence for the `USH1J` / `Usher syndrome type 1J` synonyms. This agent used `RELATED [OMIM:614869]` instead. These are minor metadata-precision differences, not substantive errors.
- The `MONDO:obsoleteEquivalent` source qualifier the agent uses for transferred legacy xrefs is not the convention the human used (`MONDO:equivalentObsolete`); a curator would normalize this, but it does not change the ontological meaning.
- No correctness, syntax, or scope errors; the only real "issue" here is the broken evaluation harness, not the agent's work.
