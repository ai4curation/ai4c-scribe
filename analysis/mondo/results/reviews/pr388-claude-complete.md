---
ontology: mondo
issue_number: 9873
pr_number: 10126
eval_repo_pr: 388
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
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

claude-opus-4.7/claude produced a substantively complete and correctly-modeled STARI term with the most carefully reasoned PR rationale of the cohort — correct parent, both synonyms, both xrefs with the canonical `SCTID:` prefix, and the `transmitted_by NCBITaxon:6943` vector axiom present in the gold. The metadiff F1 0.417 (one of the lowest) **drastically under-represents** quality and is an artifact of the unmatchable `MONDO:1010205` (gold) vs `MONDO:7770018` (agent, per config) ID, the different insertion locus, plus the agent sourcing synonyms/axioms to the submitter ORCID rather than PMIDs (a defensible provenance choice, heavily penalized line-wise by metadiff).

## Strengths

- Substantively equivalent to the gold: correct parent `is_a: MONDO:0025294`, `transmitted_by NCBITaxon:6943 ! Amblyomma americanum` axiom present, both synonyms with correct scopes (`"Masters disease" EXACT`, `"STARI" EXACT ABBREVIATION`), both xrefs qualified `{source="MONDO:equivalentTo"}`.
- **Best-reasoned scope/convention decisions of any attempt**: explicitly justified using `SCTID:` over the issue's `SNOMED:` by counting existing usage (`grep -c 'xref: SCTID:'` → 18067 vs 0 for `SNOMED:`); cited analogous Amblyomma-borne disease modeling (MONDO:0000232 Flinders island spotted fever, MONDO:0000234 Rickettsia parkeri spotted fever) as precedent for the `transmitted_by` axiom; verified `NCBITaxon:6943` is the established label-bearing ID for *Amblyomma americanum* via existing edit-file usage.
- All three PMIDs retained in the definition.
- Honest, detailed limitations section (could not run `aurelian` for PMID full text, no Docker for `make NORM`/`robot convert`; manually removed a stray duplicated OBO header from the `obo-checkin.pl` output).
- Correct provenance: submitter ORCID creator, `IAO:0000233` term_tracker_item to issue 9873.

## Issues

- **No substantive ontological issues.** Content is equivalent to the gold modeling.
- **Provenance style (metadiff-penalized, defensible)**: synonyms and the `is_a`/`transmitted_by` axioms are sourced to the submitter ORCID (`https://orcid.org/0000-0001-5705-7831`) rather than PMIDs. The gold sources synonyms to `[PMID:18452807]` and the axioms to the three PMIDs. The issue supplied no synonym/axiom source, and ORCID-as-source is a valid Mondo provenance pattern, but choosing ORCID over the available PMIDs maximizes line-level divergence from the gold and is the main reason F1 (0.417) is the lowest tier despite high actual quality.
- **Style**: definition is the issue's verbatim text rather than the curator's post-review rewrite (unavailable to the agent); not a defect.
- F1 0.417 here is almost entirely a metadiff artifact (ID range + insertion locus + ORCID-vs-PMID sourcing); on substance this is a success and arguably the best-reasoned attempt.
