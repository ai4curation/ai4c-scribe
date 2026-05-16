---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 163
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.927
precision: 0.905
recall: 0.95
jaccard: 0.864
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly obsoleted GO:0009095 "aromatic amino acid biosynthetic process, prephenate pathway" exactly as requested in issue #32005: name prefixed `obsolete`, definition prefixed `OBSOLETE.`, all logical axioms (`is_a: GO:0009073`, the three `intersection_of` axioms), the five synonyms, and `xref: MetaCyc:PWY-3481` removed, `is_obsolete: true` set, and both `consider: GO:0009094` (L-phenylalanine) and `consider: GO:0006571` (L-tyrosine) added. The diff is clean (no base-state contamination) and the metadiff F1 of 0.927 fairly represents a near-perfect outcome — the only deviation from the human gold is that the agent retained the historical `term_tracker_item` for #31091 in addition to adding #32005, whereas the human replaced it.

## Strengths

- Substantively identical to the merged human PR #32026: same obsoletion mechanics, same two `consider` targets, MetaCyc xref removed (matching gold; note the human also dropped the xref).
- Correctly chose `consider` over `replaced_by` and justified it: the obsoleted term bundled two pathways (PWY-3462 → GO:0009094, PWY-3461 → GO:0006571) so no single replacement is appropriate. This matches the issue author's and gold curator's reasoning precisely.
- Strong methodology evidence: pre/post `make travis_build` validation passed, `obo-grep.pl` confirmed GO:0009095 has no remaining internal references, taxon-constraint files checked, PMIDs from the issue validated with `linkml-reference-validator`.
- Correctly scoped the annotation work as out-of-band (the 4 EXP annotations are handled by the annotation-review process, not this ontology PR) — matching the issue's curator checklist and the gold author's own note.
- Clean diff anchored at base blob `ccb7aa216` with no foreign edits, unlike the 9 contaminated attempts on this case.

## Issues

- Minor style deviation: retained `property_value: term_tracker_item ".../31091"` and appended `.../32005`, whereas the human PR replaced #31091 with #32005. Both are defensible (keeping creation provenance is arguably better practice), but this single-line difference is the entire reason F1 is 0.927 rather than ~1.0. Not an error.
- Comment wording is terser than the gold's ("represents a pre-composed superpathway combining L-phenylalanine and L-tyrosine biosynthesis via prephenate" vs. the gold's fuller MetaCyc decomposition explanation). Adequate and accurate; purely stylistic.
