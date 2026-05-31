---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 64
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.667
precision: 0.667
recall: 0.667
jaccard: 0.5
outcome: success
failure_modes: [missed_requirement]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is the same gpt-5.5/opencode agent producing an identical diff (blob `6b9c134`) to attempt #84 — a substantively correct TSEN2-related NDD term with placeholder ID `MONDO:7770736`, correct genus-differentia definition with all 7 issue PMIDs + ClinGen URL, the ClinGen-qualified EXACT synonym, the correct logical definition and asserted gene relationship to `HGNC:28422`, and the tracker annotation. F1=0.667 ties for the best of all 14 attempts and **under-represents quality**: the ceiling is the standard new_term canonical-ID / insertion-location artifact, not agent error.

## Strengths

- Identical correct content to #84: logical def `intersection_of: MONDO:0700092` + `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`, matching gold's substance.
- Explicitly named and applied the `disease_series_by_gene` design pattern, the correct Mondo pattern for ClinGen monogenic disease requests.
- Strong process narrative: read `__issue_context__.json`, checked existing `MONDO:0012890`, verified `TSEN2`=`HGNC:28422` via HGNC REST, ran `make NORM`, `robot convert`, and `robot reason --reasoner ELK` successfully.
- Sound curatorial judgment articulated: declined to rewire `MONDO:0012890` as a child because the issue specified "Children terms: N/A" and the logical definition is sufficient for reasoner-based classification.
- Correctly used a placeholder NTR-range ID rather than guessing the canonical one.

## Issues

- **Omission (defensible)**: missing the gold curator's second parent `is_a: MONDO:0002254` (syndromic disease); issue requested only `MONDO:0700092`, so a reasonable scoping decision.
- **Minor scope addition**: extra `is_a: MONDO:0100500` (Mendelian neurodevelopmental disorder) and `subset: rare` not in gold; defensible but unrequested, and the MONDO:0100500 parent is redundant with MONDO:0700092.
- Creator attribution differs from the human ORCID (unavoidable artifact).
- **Case quality note**: F1 ceiling is a new_term scoring artifact — see METADATA Curation Note.
