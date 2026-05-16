---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 127
agent: std_codex_g55
model: gpt-5.5
runtime: codex
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

gpt-5.5 under the codex runtime produced a clean, correct obsoletion of GO:0009095 equivalent to the two opencode runs (#163, #145) and to the merged human PR #32026: name/def prefixed, logical axioms + 5 synonyms + `xref: MetaCyc:PWY-3481` removed, `is_obsolete: true`, and `consider: GO:0009094` + `consider: GO:0006571` added. Clean diff (base blob `ccb7aa216`), F1 0.927 fairly represents a near-perfect result, with the only gold deviation being retention of the #31091 tracker alongside the added #32005.

## Strengths

- Substantively matches the human gold standard on every material edit, including dropping the MetaCyc xref (as the gold did) and selecting the correct dual `consider` targets.
- Clear, accurate rationale tying PWY-3481 (superpathway) to its decomposed members PWY-3462/PWY-3461 and their corresponding GO terms with narrowMatch xrefs — the same justification the issue author and gold curator used.
- Methodology: pre/post `make -C src/ontology travis_build` passed; `RESEARCH.md`/`DESIGN_PATTERNS.md` notes created; PMID support validated with `linkml-reference-validator` (3 valid). Transparent that local `runoak` failed due to an unrelated LinkML dependency error and that QuickGO was used as a fallback for annotation counts.
- Correctly deferred the 4 EXP annotations to the annotation-review process rather than touching annotations in the ontology PR.

## Issues

- Same minor style deviation as the sibling gpt-5.5 runs: kept `term_tracker_item ".../31091"` and added `.../32005`, where the human replaced it. Sole cause of F1 < 1.0; defensible, not an error.
- Comment phrasing ("better represented as a GO-CAM model") is slightly different from the gold's MetaCyc-decomposition wording but is accurate and consistent with the issue's stated obsoletion reason. Stylistic only.
