---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 347
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.352
precision: 0.463
recall: 0.284
jaccard: 0.213
outcome: partial_success
failure_modes: [wrong_pattern, missed_requirement, wrong_term]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall floored for every attempt; but this attempt's low precision also reflects real obsoletion-reason and source-qualifier errors."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Poor evaluation case (multi-PR partial gold). sonnet-4.5 via copilot obsoleted all four requested terms with correct `replaced_by` targets, but the obsoletion pattern is wrong on several counts: it used `IAO:0000231 OMO:0001000` (generic "terms merged"/deprecation marker) instead of the MONDO-specific `MONDO:TermsMerged`, invented a curator ORCID `https://orcid.org/0009-0000-1074-3026`, used the non-existent qualifier `MONDO:obsoleteEquivalent` (correct is `MONDO:equivalentObsolete`), and transferred no metadata to the surviving terms. F1=0.352 reflects both the partial-gold harness and these genuine defects.

## Strengths

- All four merge pairs correctly identified with `is_obsolete: true` + `replaced_by:` + issue link + `obsolete ...` name prefix.
- Logical axioms and the `obsoletion_candidate` subset / scheduled-obsoletion date removed from the obsoleted stanzas.

## Issues

- **Wrong obsoletion reason**: `property_value: IAO:0000231 OMO:0001000` instead of `MONDO:TermsMerged`. The gold #10110 uses `MONDO:TermsMerged`; this is the wrong term for a merge and would fail MONDO's obsoletion-reason QC.
- **Fabricated provenance**: injected `property_value: http://purl.org/dc/terms/creator https://orcid.org/0009-0000-1074-3026` on every obsoleted term — an ORCID with no basis in the issue or environment.
- **Invalid source qualifier**: `MONDO:obsoleteEquivalent` is not a MONDO source value (the convention is `MONDO:equivalentObsolete`); applied broadly across DOID/MEDGEN/MESH/Orphanet/SCTID/UMLS xrefs.
- **Wrong merge pattern**: synonyms/xrefs left on the obsolete stanzas; nothing transferred to surviving terms, so the merges lose the external mappings the human moved onto MONDO:0007402/0044720/0010549/0012273.
- No engagement with the syndromic-vs-nonsyndromic judgment central to the case.
