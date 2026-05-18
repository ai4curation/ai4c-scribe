---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 737
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

Poor evaluation case (multi-PR partial gold; see scoring_caveat). This is effectively a replay of attempt #739 (same gpt-5.4/opencode, identical blob `a7c5e25`, same F1/P/R): all four OMIM merges performed correctly with survivor metadata transfer, but again using the non-standard `MONDO:obsoleteEquivalent` source qualifier instead of the conventional `MONDO:equivalentObsolete`. Scope coverage of the issue is complete; the precision penalty is part partial-gold artifact and part genuine pattern defect.

## Strengths

- All four requested merges performed with correct `replaced_by` targets, fully resolving the issue's four-row request.
- Obsolete stanzas reduced to the canonical minimal merge form matching gold #10110's MONDO:0013935 stanza.
- Transferred historical synonyms and obsolete-source xrefs onto the four surviving terms (e.g. `cramps, familial adolescent` RELATED + `OMIM:218050` onto MONDO:0007402; `USH1J`, `Usher syndrome type Ij` + `OMIM:614869` onto MONDO:0012273) plus `IAO:0000233 .../9795` provenance — preserving the OMIM/MedGen mapping continuity #696 dropped.
- Correctly omitted the misleading Usher `is_a` parents from the nonsyndromic survivor MONDO:0012273, matching the human's conservative choice.
- Reported its PMID:12870133 / PMID:16311270 PubMed validation and the docker/aurelian environment limitations transparently; ran `robot convert` syntax check.

## Issues

- **Non-standard source qualifier (wrong_pattern):** Same defect as #739 — obsolete-OMIM xrefs added to survivors as `source="MONDO:obsoleteEquivalent"` instead of the canonical `source="MONDO:equivalentObsolete"`. Genuine precision-depressing defect independent of the partial-gold artifact.
- Demoted transferred survivor synonyms to RELATED with OMIM evidence where gold/strong runs keep them EXACT — debatable, slightly less faithful to the stated merged-concept equivalence.
- Did not reproduce gold's `MONDO:preferredExternal` additions or the NARROW deafness-synonym deletions on MONDO:0012273 — minor deltas, largely a partial-gold artifact.
- Functionally duplicates #739 (same model/runtime/blob); no independent signal beyond confirming reproducibility.
