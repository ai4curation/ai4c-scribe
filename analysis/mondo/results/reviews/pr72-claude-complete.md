---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 72
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.414
precision: 0.854
recall: 0.273
jaccard: 0.261
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall is floored for every attempt because the three correct companion merges count as extra. F1 ~0.41 under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Poor evaluation case (multi-PR partial gold; see scoring_caveat). This attempt correctly performed all four OMIM-driven merges the issue asked for and transferred surviving-term metadata thoroughly. The metadiff F1=0.414 / recall=0.263 reflects only the Usher sub-step #10110 and badly under-represents the work; precision=0.854 confirms the edits it makes are on-target. Judged against the issue, this is a complete and high-quality resolution with one defensible-but-debatable classification choice.

## Strengths

- All four requested merges performed with correct `replaced_by` targets exactly as listed in the issue.
- Obsolete stanzas reduced to the canonical minimal merge form matching the gold #10110 pattern (`IAO:0000231 MONDO:TermsMerged`, issue link, `is_obsolete: true`, `replaced_by`).
- Genuinely thorough metadata transfer to survivors: e.g. for MONDO:0007402 it migrated `synonym: "cramps, familial adolescent"`, `xref: MEDGEN:347475`, `xref: OMIM:218050`, `xref: UMLS:C1857533`, the MalaCards `curated_content_resource`, and the ORCID source on `is_a: MONDO:0003847` — substantively more complete than the human's per-PR transfers.
- Stripped `subset: obsoletion_candidate` and the `IAO:0006012` scheduled-obsoletion date from survivors so they are not re-flagged for obsoletion — correct cleanup the haiku/copilot attempts missed.
- Explicitly declined to add the historically-incorrect Usher/HSAN `is_a` parents onto the nonsyndromic survivors, directly engaging with the syndromic-vs-nonsyndromic judgment that defines this case's difficulty.
- `robot convert` syntax check and `robot verify` merge QC reported clean.

## Issues

- On the scored Usher portion it transferred Usher `is_a` parents (MONDO:0010168, MONDO:0019501) onto MONDO:0012273 and added `CIB2 Usher syndrome` / `Usher syndrome ...` synonyms — the human #10110 deliberately did NOT make nonsyndromic hearing loss a subclass of Usher syndrome. This is the one substantive divergence from gold, and it is the conceptually hard call the case is designed around; the agent's choice is defensible (OMIM treats them as equivalent) but the human's narrower choice is preferable.
- Did not reproduce the human's `MONDO:preferredExternal` source additions or the deletion of the two NARROW deafness synonyms on MONDO:0012273 — minor metadata-precision deltas.
- Uses `MONDO:equivalentObsolete` vs the case's other conventions inconsistently in places; cosmetic, curator-normalizable.
