---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 336
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.343
precision: 0.415
recall: 0.293
jaccard: 0.207
outcome: partial_success
failure_modes: [wrong_pattern, missed_requirement]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall floored for every attempt; this attempt's low precision also reflects retained definitions, a fabricated DOI creator, and no metadata transfer."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Poor evaluation case (multi-PR partial gold). sonnet-4.5 via copilot obsoleted all four requested terms with correct `replaced_by` targets and the correct `MONDO:TermsMerged` reason, but the obsoletion is the least clean of the copilot runs: it retained the definitions on the obsoleted stanzas with an "OBSOLETE." prefix, fabricated a `doi:` creator, used the invalid `MONDO:obsoleteEquivalent` qualifier, kept MalaCards links on the obsolete stanzas, and transferred no metadata to survivors. F1=0.343 (lowest in the set) reflects both the partial-gold harness and these defects.

## Strengths

- All four merge pairs correctly identified with `is_obsolete: true`, `replaced_by:`, `IAO:0000231 MONDO:TermsMerged`, issue link, and `obsolete ...` name prefix.
- `is_a` axioms and the `obsoletion_candidate` subset / scheduled-obsoletion date removed from obsoleted stanzas.

## Issues

- **Definitions retained on obsoleted terms** with an `OBSOLETE.`-prefixed def (e.g. MONDO:0011961, MONDO:0013935). Gold #10110 removes the def entirely for a merge; an OBSOLETE-prefixed def is the pattern for plain deprecation, not a TermsMerged merge.
- **Fabricated provenance**: `property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3` (a paper DOI, not a curator) injected on every obsoleted term.
- **Invalid source qualifier**: `MONDO:obsoleteEquivalent` instead of `MONDO:equivalentObsolete`.
- **Incomplete merge**: synonyms, xrefs, and the MalaCards `curated_content_resource` left on the obsolete stanzas; nothing transferred to MONDO:0007402/0044720/0010549/0012273, so the merges lose the external mappings the human moved onto the survivors.
- No engagement with the syndromic-vs-nonsyndromic judgment central to the case.
