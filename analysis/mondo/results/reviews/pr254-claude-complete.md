---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 254
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.609
precision: 0.583
recall: 0.636
jaccard: 0.438
outcome: success
failure_modes: [missed_requirement, over_editing]
case_quality: poor
case_quality_reason: new_term_canonical_id_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added a substantively strong TSEN2-related NDD term. Notably it is the **only attempt that used the canonical ID `MONDO:1060216`** (matching gold) and inserted the stanza at the **same file location as gold** (line ~659045) — this is why its diff blob differs from the placeholder-ID attempts and why recall is comparatively higher (0.636). The definition is essentially identical to gold (genus-differentia stem, all 7 issue PMIDs + ClinGen URL), the ClinGen-qualified synonym is reproduced verbatim, and the logical definition is correct. F1=0.609 still under-represents quality because of remaining structural differences (creator value, source-list expansion on axioms), not substantive errors. I did not find evidence this was gold leakage — the ID/location match is plausibly the agent picking the next sequential `MONDO:106xxxx` ID and inserting in numeric order; the definition wording ("mutation in" vs gold's "variation in"), expanded per-axiom source lists, and the creator value all diverge from gold, confirming genuine agent work rather than a copied gold stanza.

## Strengths

- Definition matches gold almost verbatim, including the full clinical phenotype description and exactly the 7 issue PMIDs + ClinGen URL as def xrefs.
- ClinGen-qualified EXACT synonym reproduced verbatim with the `{OMO:0002001=...}` axiom annotation.
- Correct logical definition: `intersection_of: MONDO:0700092` + `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422`, plus the asserted `relationship` to the same HGNC IRI.
- Correct gene grounding (`HGNC:28422`), correct primary parent `MONDO:0700092`, correct tracker `IAO:0000233` → issue #9956.
- Good process: validated with `robot convert`, normalized with `make NORM`, checked existing `MONDO:0012890` and correctly left it unchanged.

## Issues

- **Omission (defensible)**: missing the gold curator's second parent `is_a: MONDO:0002254` (syndromic disease); issue requested only `MONDO:0700092`.
- **Over-editing on provenance**: attached all 7 PMIDs as `source=` qualifiers on both the `is_a: MONDO:0700092` axiom and the gene `relationship`. Gold uses a single concise `source="https://clinicalgenome.org/affiliation/40069/"` on each. The agent's verbose 8-source lists are noisy and not Mondo convention for these axioms — reduces precision.
- Creator attribution `doi:10.1186/s13326-024-00320-3` differs from the human ORCID (unavoidable, but the DOI choice is unusual).
- Definition says "mutation in" rather than gold's "variation in the TSEN2 gene" — trivial wording difference.
- **Case quality note**: F1 ceiling is a new_term scoring artifact — see METADATA Curation Note.
