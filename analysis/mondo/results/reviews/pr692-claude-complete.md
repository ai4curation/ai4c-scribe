---
ontology: mondo
issue_number: 9873
pr_number: 10126
eval_repo_pr: 692
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.435
precision: 0.417
recall: 0.455
jaccard: 0.278
outcome: partial_success
failure_modes: [missed_requirement, over_editing]
case_quality: poor
case_quality_reason: gold_id_range_unmatchable
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/opencode added a valid STARI term with the correct parent, both synonyms, and both canonical-prefix xrefs, but **omitted the `transmitted_by NCBITaxon:6943` vector axiom** that the gold includes and that the stronger cohort attempts (#77/#58/#40/#173) captured. The metadiff F1 0.435 is depressed primarily by the case-wide unmatchable `MONDO:1010205` (gold) vs `MONDO:7770018` (agent, per config instruction) ID/locus artifact, but here the low score is **partly substantive**: the missing vector relationship and a dropped definition PMID are real gaps versus the gold. Output is byte-identical to attempt #747 (same blob `e694a3e`).

## Strengths

- Correct parent `is_a: MONDO:0025294` (tick-borne infectious disease) exactly as requested in the issue.
- Both synonyms present with correct scopes: `"Masters disease" EXACT`, `"STARI" EXACT ABBREVIATION`.
- Both xrefs qualified `{source="MONDO:equivalentTo"}` with the **canonical `SCTID:444100007` prefix**, correctly translated from the issue's literal `SNOMED:444100007`.
- Correct provenance: submitter ORCID `0000-0001-5705-7831` as `dcterms:creator`, `IAO:0000233` term_tracker_item pointing to issue 9873.
- Scientifically accurate definition (etiology-uncertain framing, erythema migrans-like rash, lone star tick) — the vector species is named in the prose even though it is not encoded as an axiom.

## Issues

- **Missed requirement (substantive)**: no `relationship: transmitted_by NCBITaxon:6943 ! Amblyomma americanum` axiom. This is one of the explicit discriminating criteria for this case — the gold encodes the vector logically and 7/9 cohort attempts reproduced it. Here the lone star tick appears only as definition text, so the vector is not machine-queryable. This is the main reason this attempt ranks below #77/#58/#40.
- **Omission (minor)**: the definition reference bracket retains only `PMID:36116832, PMID:40267428` (plus `NCIT:C128427`); `PMID:19522220` is demoted into the synonym source lists rather than kept as a definition source. The issue listed all three PMIDs as definition support.
- **Over-editing (precision-reducing, harmless)**: `NCIT:C128427` and `SCTID:444100007` stuffed into both synonym source brackets — not erroneous but gratuitous and not in the gold.
- **Style**: `is_a` carries a single `{source="PMID:36116832"}` annotation vs the gold's four-source annotation; defensible but thinner provenance.
- F1 0.435 is mostly the case-wide ID/locus metadiff artifact (case flagged poor), but unlike the success-grade attempts this run also has a genuine substantive gap (vector axiom + one def PMID), so this is a partial success, not a full one.
