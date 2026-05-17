---
ontology: mondo
issue_number: 9873
pr_number: 10126
eval_repo_pr: 58
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

gpt-5.5/opencode (run #58) is **byte-identical** to attempt #77 (same blob `02b16b1`, same model/runtime) and is one of the strongest attempts in the cohort: correct parent, both synonyms, both xrefs with the canonical `SCTID:` prefix, and the `transmitted_by NCBITaxon:6943` vector axiom present in the gold. This run additionally documents the most thorough validation methodology of any attempt. F1 0.5 **severely under-represents** quality and is driven by the unmatchable `MONDO:1010205` vs `MONDO:7770018` ID and differing insertion locus (case flagged poor), not by substance.

## Strengths

- Substantively equivalent to the gold: correct parent `is_a: MONDO:0025294`, `transmitted_by NCBITaxon:6943 ! Amblyomma americanum` axiom, both synonyms (`"Masters disease" EXACT`, `"STARI" EXACT ABBREVIATION`), both xrefs qualified `{source="MONDO:equivalentTo"}`.
- Canonical `SCTID:` prefix used in place of the issue's `SNOMED:`.
- Definition accurate; all three PMIDs retained.
- **Best-documented methodology of the nine attempts**: duplicate check via `obo-grep.pl`, PMID verification via PubMed pages (honestly noting `aurelian` unavailable), NCIT/SNOMED xref verification, `terms/` + `obo-checkin.pl` workflow, `make NORM`, `robot convert` syntax validation, and `robot reason` ELK reasoning validation. Transparently noted Docker/ODK-wrapper limitation.
- Correct provenance: submitter ORCID creator, `IAO:0000233` term_tracker_item to issue 9873.

## Issues

- **No substantive issues.** Content matches the gold modeling.
- **Reproducibility note**: identical to #77; treat the pair as a single data point in aggregation.
- **Style**: definition wording and synonym/creator sourcing differ from the curator's post-review final, which the agent could not access; not defects.
- F1 0.5 is a metadiff artifact (ID range + insertion locus); on substance this is a success.
