---
ontology: mondo
issue_number: 9873
pr_number: 10126
eval_repo_pr: 77
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
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_id_range_unmatchable
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.5/opencode produced a substantively complete and correct STARI term — correct parent, both synonyms with correct scopes, both xrefs with the canonical `SCTID:` prefix, and the `transmitted_by NCBITaxon:6943` vector axiom that the gold includes. The metadiff F1 0.5 **severely under-represents** quality: the score is depressed almost entirely by the unmatchable `MONDO:1010205` (gold) vs `MONDO:7770018` (agent, per config instruction) ID and the different file-insertion locus, not by any substantive defect. Output is byte-identical to attempt #58 (same blob `02b16b1`).

## Strengths

- Correct parent `is_a: MONDO:0025294` (tick-borne infectious disease) as requested, with multi-PMID source annotation matching the gold's annotation pattern.
- Included `relationship: transmitted_by NCBITaxon:6943 ! Amblyomma americanum` with PMID sources — matches the gold and correctly encodes the vector as a logical axiom.
- Correct `SCTID:` prefix for SNOMED (translated from the issue's `SNOMED:`), both xrefs qualified `{source="MONDO:equivalentTo"}`.
- Both synonyms with correct scopes: `"Masters disease" EXACT`, `"STARI" EXACT ABBREVIATION`.
- Definition accurate and retained all three PMIDs.
- Correct provenance: submitter ORCID creator, `IAO:0000233` term_tracker_item to issue 9873.

## Issues

- **No substantive issues.** The ontological content is essentially equivalent to the gold.
- **Style**: definition wording ("erythema migrans-like rash at the site of a lone star tick bite") differs from the curator's final rewrite, which only emerged through a review round unavailable to the agent. Scientifically accurate; not a defect.
- **Style**: synonym sources cite PMIDs rather than the gold's `[PMID:18452807]`; the issue gave no synonym source, so this is a defensible choice.
- **Creator ORCID**: submitter ORCID vs gold's curator ORCID — house convention, not inferable from the issue.
- F1 0.5 here is a metadiff artifact (ID range + insertion locus), not a quality signal; this attempt is among the best in the cohort despite scoring mid-pack.
