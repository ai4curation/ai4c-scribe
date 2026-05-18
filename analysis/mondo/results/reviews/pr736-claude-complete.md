---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 736
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.395
precision: 0.756
recall: 0.267
jaccard: 0.246
outcome: partial_success
failure_modes:
  - wrong_pattern
  - syntax_error
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall is floored for every attempt because the three correct companion merges count as extra. F1 ~0.40 under-represents scope coverage; precision additionally reflects genuine pattern defects (non-standard source qualifier, duplicate subset line, NORM not run)."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Poor evaluation case (multi-PR partial gold; see scoring_caveat). This gpt-5.4/opencode run obsoleted all four OMIM-merge candidates with correct `replaced_by` targets and transferred historical signal to survivors, but it has the most pattern defects of this batch: the non-standard `MONDO:obsoleteEquivalent` source qualifier, an introduced **duplicate `subset: gard_rare` line** on MONDO:0012273, and it could not run the ODK `make NORM` normalization (no docker) so the stanzas are unsorted/un-normalized. Scope coverage of the issue is complete, but the unmerged-edits state would need curator cleanup.

## Strengths

- All four requested merges performed with correct targets (MONDO:0009027→0007402, 0011961→0044720, 0010553→0010549, 0013935→0012273), fully covering the issue's four-row request.
- Obsolete stanzas reduced to the canonical minimal merge form (`obsolete` label, `IAO:0000231 MONDO:TermsMerged`, `IAO:0000233 .../9795`, `is_obsolete: true`, `replaced_by`).
- Transferred historical synonyms and obsolete-source xrefs to survivors (e.g. `cramps, familial adolescent` + `OMIM:218050` onto MONDO:0007402; `USH1J`, `Usher syndrome ...` + `OMIM:614869`/`DOID:0110836`/`MEDGEN:766858`/`UMLS:C3553944` onto MONDO:0012273) with `IAO:0000233 .../9795` provenance — better mapping continuity than the bare-obsoletion #696.
- Correctly omitted the misleading Usher `is_a` parents from the nonsyndromic survivor.
- Transparently disclosed that docker/aurelian were unavailable and that NORM/robot-convert could not be run, rather than silently claiming validation.

## Issues

- **Duplicate subset line (syntax_error / un-normalized):** On MONDO:0012273 the diff adds a second standalone `subset: gard_rare {source="GARD:0015863", source="MONDO:GARD"}` while leaving the existing `subset: gard_rare {source="GARD:0022612", source="MONDO:GARD"}` — two separate `subset: gard_rare` lines. The gold and the stronger runs merge the GARD sources into a single `subset: gard_rare {source="GARD:0015863", source="GARD:0022612", source="MONDO:GARD"}`. Likewise xrefs/synonyms are inserted out of sorted order. `make NORM` would normally collapse/sort these, but the agent could not run it, so the defect ships in the diff.
- **Non-standard source qualifier (wrong_pattern):** obsolete-OMIM xrefs added to survivors as `source="MONDO:obsoleteEquivalent"` (and on MONDO:0012273 a malformed `xref: DOID:0110836 {source="MONDO:obsoleteEquivalent"}` plus `xref: OMIM:614869 {source="DOID:0110836", source="MONDO:obsoleteEquivalent"}`) instead of the canonical `MONDO:equivalentObsolete`. Genuine precision-depressing defect.
- For MONDO:0011961's obsolete stanza it retained the old `IAO:0000233 .../4521` tracker link alongside the new `.../9795` link rather than reducing to issue-9795-only as gold does — minor stanza-hygiene miss.
- No `make NORM` / no syntax validation actually executed, so the submission is not in a checkable, mergeable state — a curator would have to re-normalize and de-duplicate before merge.
