---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 739
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.460
precision: 0.707
recall: 0.341
jaccard: 0.299
outcome: partial_success
failure_modes:
  - wrong_pattern
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall is floored for every attempt because the three correct companion merges count as extra. F1 ~0.46 under-represents scope coverage; precision additionally reflects a genuine non-standard source-qualifier defect."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Poor evaluation case (multi-PR partial gold; see scoring_caveat). This attempt correctly obsoleted all four OMIM-merge candidates with the right `replaced_by` targets and did transfer lightweight historical signal onto the surviving terms, so it is more complete than the bare-obsoletion run #696. However it used a non-standard `MONDO:obsoleteEquivalent` xref source qualifier instead of the conventional `MONDO:equivalentObsolete` used by the gold and by the canonical stanzas, which is a genuine pattern defect that depresses precision independently of the partial-gold scoring artifact.

## Strengths

- All four merges done with correct targets (MONDO:0009027→0007402, 0011961→0044720, 0010553→0010549, 0013935→0012273), fully covering the issue's four-row request.
- Obsolete stanzas reduced to the canonical minimal merge form (`obsolete` label, `IAO:0000231 MONDO:TermsMerged`, `IAO:0000233 .../9795`, `is_obsolete: true`, `replaced_by`) matching gold #10110's MONDO:0013935 stanza.
- Did transfer historical labels to survivors as RELATED synonyms (e.g. `cramps, familial adolescent` onto MONDO:0007402; `USH1J`, `Usher syndrome type Ij` onto MONDO:0012273) and added the obsolete OMIM IDs and `IAO:0000233 .../9795` provenance to survivors — preserving discoverability/mapping continuity that #696 dropped entirely.
- Correctly declined to transfer the misleading Usher `is_a` parents (MONDO:0010168, MONDO:0019501) onto the nonsyndromic survivor MONDO:0012273 — the conservative choice that aligns with the human #10110.
- Honestly reported the OMIM HTTP 403 limitation and that it relied on imported issue context and existing ontology identifiers rather than fabricating.

## Issues

- **Non-standard source qualifier (wrong_pattern):** Added obsolete-OMIM xrefs to survivors as `xref: OMIM:218050 {source="MONDO:obsoleteEquivalent"}` / `xref: OMIM:614869 {source="MONDO:obsoleteEquivalent"}` etc. The gold and the canonical Mondo convention use `source="MONDO:equivalentObsolete"`. `MONDO:obsoleteEquivalent` is not the established qualifier here; this is the same invalid-qualifier defect noted for several copilot runs in the METADATA. It depresses precision for real reasons, not just the partial-gold artifact.
- Demoted survivor synonyms to RELATED with OMIM evidence (e.g. `cramps, familial adolescent` RELATED) where the gold/strong runs keep them EXACT — debatable but less faithful to the merged-concept-equivalence framing the issue states.
- Did not reproduce the gold's `MONDO:preferredExternal` source additions or the deletion of the two NARROW deafness synonyms on MONDO:0012273 — minor metadata-precision deltas, largely a partial-gold artifact.
