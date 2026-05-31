---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 145
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

A second gpt-5.5/opencode run on the same case, producing a substantively identical and correct obsoletion of GO:0009095: name/def prefixed, all logical axioms + synonyms + `xref: MetaCyc:PWY-3481` removed, `is_obsolete: true`, and both `consider: GO:0009094` and `consider: GO:0006571` added. The diff is clean (base blob `ccb7aa216`, no contamination) and the F1 of 0.927 accurately reflects a near-perfect result; the sole deviation from the human gold is retention of the #31091 tracker alongside the added #32005.

## Strengths

- Matches the merged human PR #32026 in all material respects: obsoletion metadata, axiom removal, MetaCyc xref dropped, and the same two `consider` targets.
- Explicitly justified `consider` over `replaced_by` on the grounds that neither GO:0009094 nor GO:0006571 alone replaces the combined term — exactly the issue author's and gold curator's logic.
- Documented methodology: pre/post `make travis_build` passed, candidate terms and references to GO:0009095 checked, taxon constraints checked, PMID support verified via web fetch and `linkml-reference-validator` (transparently noting NCBI rate-limiting prevented caching two PMIDs).
- Correctly treated annotation migration as separate annotation-review work, consistent with the issue checklist.
- Reproducibility: this run is byte-identical in the GO:0009095 stanza to attempt #163 (same blob `995aa71`), demonstrating stable behavior for this model/runtime.

## Issues

- Same single-line style deviation as #163: kept the historical #31091 `term_tracker_item` and appended #32005, while the human replaced it. Defensible (preserves creation provenance) and the only cause of F1 < 1.0. Not an error.
- Comment is briefer than the gold's, but accurate and standards-compliant. Purely stylistic.
