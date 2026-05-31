---
ontology: mondo
issue_number: 9873
pr_number: 10126
eval_repo_pr: 281
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.417
precision: 0.417
recall: 0.417
jaccard: 0.263
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_id_range_unmatchable
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

kimi-k2.6/opencode produced a substantively complete and correct STARI term — correct parent, both synonyms, both xrefs with the canonical `SCTID:` prefix, and the `transmitted_by NCBITaxon:6943` vector axiom present in the gold — with notably rigorous, well-documented validation. The metadiff F1 0.417 (lowest tier) **drastically under-represents** quality: it is an artifact of the unmatchable `MONDO:1010205` vs `MONDO:7770018` ID, the different insertion locus, and ORCID-as-source for synonyms/axioms (defensible but line-divergent from the gold's PMID sourcing). The definition reference list closely matches the gold's (`[ORCID, PMID:19522220, PMID:36116832, PMID:40267428]`).

## Strengths

- Substantively equivalent to the gold: correct parent `is_a: MONDO:0025294`, `transmitted_by NCBITaxon:6943 ! Amblyomma americanum` axiom present, both synonyms with correct scopes, both xrefs qualified `{source="MONDO:equivalentTo"}`.
- Canonical `SCTID:444100007` used in place of the issue's `SNOMED:444100007`.
- Definition reference list `[https://orcid.org/0000-0001-5705-7831, PMID:19522220, PMID:36116832, PMID:40267428]` is the closest of any attempt to the gold's reference list (gold uses the same set).
- **Strongest PMID verification of any attempt**: looked up and reported the actual titles/years of all three PMIDs via NCBI E-utilities (PMID:19522220 2009 STARI spirochetosis, PMID:36116832 2022 EM mimics, PMID:40267428 2025 NEJM STARI), confirming they genuinely support the term.
- Sound parent justification (Ixodidae family reasoning for *Amblyomma americanum* under tick-borne infectious disease) and NCIT/SNOMED xref verification.
- Correct provenance: submitter ORCID creator, `IAO:0000233` term_tracker_item to issue 9873; `make NORM` + `robot convert` run.

## Issues

- **No substantive ontological issues.** Content is equivalent to the gold modeling.
- **Provenance style (metadiff-penalized, defensible)**: synonyms and `is_a` sourced to the submitter ORCID rather than PMIDs (gold synonyms use `[PMID:18452807]`). The `transmitted_by` axiom is sourced to a single `PMID:36116832` vs the gold's four sources. The issue supplied no synonym source, so ORCID is acceptable, but it maximizes line divergence from the gold and depresses F1.
- **Style**: definition wording is the issue's verbatim text, not the curator's post-review rewrite (unavailable to the agent); not a defect.
- F1 0.417 is a metadiff artifact (ID range + insertion locus + sourcing convention); on substance this is a success with the best PMID-verification methodology in the cohort.
