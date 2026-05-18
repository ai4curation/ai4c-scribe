---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 11
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v2
case_type: new_term
difficulty: medium
f1: 0.609
precision: 0.583
recall: 0.636
jaccard: 0.438
outcome: success
failure_modes: [missed_requirement]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.5/codex produced a substantively correct, mergeable new term with placeholder ID `MONDO:7770736`: a genus-differentia definition citing all 7 issue PMIDs plus a relevant 8th (`PMID:34964109`) and the ClinGen URL, the correct logical definition (`intersection_of: MONDO:0700092` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`), the asserted gene relationship, the ClinGen-qualified EXACT synonym, and the issue tracker annotation. F1=0.609 **under-represents** quality — the ceiling is the new_term canonical-ID / insertion-location / creator artifact, not agent error.

## Strengths

- Correct logical definition and asserted `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`; verified TSEN2=HGNC:28422 via HGNC REST.
- Included the ClinGen-qualified EXACT synonym with `OMO:0002001` qualifier and the ClinGen URL — matches gold's synonym substance.
- Definition cites all 7 issue PMIDs plus the ClinGen affiliation URL (gold's exact source set) and adds `PMID:34964109` (TSEN2 aHUS/TRACK) — a defensible literature addition supporting the TMA phenotype.
- Kept the requested single parent `MONDO:0700092`; correctly used a placeholder NTR ID rather than guessing canonical `MONDO:1060216`.
- Solid process: read issue context, checked existing `MONDO:0012890`/PCH terms, ran `make NORM` and `robot convert` validation.

## Issues

- **Defensible synonym addition**: added `"TRACK syndrome" NARROW [PMID:34964109]`. TRACK syndrome is a real TSEN2-associated entity in the literature, so this is a reasonable NARROW synonym, but it was not requested and is not in gold.
- **Omission (defensible)**: missing gold's second parent `is_a: MONDO:0002254` (syndromic disease); issue requested only `MONDO:0700092`.
- **Minor omission**: no `property_value: creator` line at all (gold has the human ORCID; most agents emit the design-pattern DOI). Low impact.
- **Case quality note**: F1 ceiling is the new_term scoring artifact — see METADATA Curation Note.
