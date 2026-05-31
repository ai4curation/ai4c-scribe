---
ontology: mondo
issue_number: 9873
pr_number: 10126
eval_repo_pr: 747
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

gpt-5.4/opencode (run #747) is **byte-identical** to attempt #692 (same blob `e694a3e`, same model/runtime): a valid STARI term with the correct parent, both synonyms, and both canonical-prefix xrefs, but **missing the `transmitted_by NCBITaxon:6943` vector axiom** that the gold and the stronger cohort attempts include. The metadiff F1 0.435 is depressed mostly by the case-wide unmatchable `MONDO:1010205` vs `MONDO:7770018` ID/locus artifact (case flagged poor), but here it is **partly a true quality signal**: the absent vector relationship and a demoted definition PMID are real gaps versus the gold. This run also includes a detailed PR comment documenting its process.

## Strengths

- Correct parent `is_a: MONDO:0025294` (tick-borne infectious disease) as requested.
- Both synonyms with correct scopes: `"Masters disease" EXACT`, `"STARI" EXACT ABBREVIATION`.
- Both xrefs qualified `{source="MONDO:equivalentTo"}` with the **canonical `SCTID:444100007` prefix**, correctly translated from the issue's `SNOMED:444100007`.
- Correct provenance: submitter ORCID `0000-0001-5705-7831` creator, `IAO:0000233` to issue 9873.
- **Well-documented methodology** in the PR comment: confirmed no existing MONDO coverage, verified the parent term exists, checked all three PMIDs on PubMed, validated NCIT/SCTID identifiers, and transparently disclosed it could not run the ODK Docker normalization (`make NORM`, `robot convert`) because Docker was unavailable — an honest limitation note.

## Issues

- **Missed requirement (substantive)**: no `relationship: transmitted_by NCBITaxon:6943 ! Amblyomma americanum` axiom. The gold encodes the lone star tick vector logically and most cohort attempts reproduced it; here it is only definition prose, so the vector is not queryable. This is the principal reason this run ranks below #77/#58/#40.
- **Omission (minor)**: definition bracket keeps only `PMID:36116832, PMID:40267428` (+`NCIT:C128427`); `PMID:19522220` is moved into the synonym sources rather than retained as a definition source, though the issue cited all three for the definition.
- **Over-editing (precision-reducing, harmless)**: `NCIT:C128427` and `SCTID:444100007` added into both synonym source brackets — not in the gold and not requested.
- **Style**: single-source `is_a` annotation (`{source="PMID:36116832"}`) vs the gold's four-source form; defensible but thinner.
- F1 0.435 is largely the case-wide ID/locus metadiff artifact, but the genuine substantive gap (vector axiom + one def PMID) makes this a partial success rather than a clean one. The thorough, honest process documentation is a positive distinguishing feature of this run.
