---
ontology: go-ontology
issue_number: 30894
pr_number: 32011
eval_repo_pr: 81
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.941
precision: 1.0
recall: 0.889
jaccard: 0.889
outcome: partial_success
failure_modes:
  - over_editing
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added `GO:7770069 ferritinophagy` matching the accepted human PR #32011 on label, definition, synonym, parent, references, and provenance, but added one extra axiom — `relationship: has_primary_input GO:0070288 ! ferritin complex` — that the human deliberately omitted. The agent diff is identical to attempt #102 (same `fc67f17` blob). The metadiff score (`f1: 0.941`, `precision: 1.0`, `recall: 0.889`) slightly understates the quality: the extra line is a single-axiom pattern divergence, not a correctness error, but it is a genuine scope/consistency issue the curator's solution avoided.

## Strengths

- Created `GO:7770069` in `biological_process` with the standardized label `ferritinophagy` (from @ValWood's thread), not the issue body's `Ferritin-specific autophagy`.
- Used the exact accepted definition with `PMID:25327288`, `PMID:26436293`, `PMID:38714719` in gold order.
- Correct parent `is_a: GO:0016236 macroautophagy`, correct `"ferritin-specific autophagy" EXACT []` synonym, correct `term_tracker_item`.
- Correctly declined to add an `intersection_of`/equivalence axiom (no DOSDP for selective macroautophagy) and recognized that the iron mention does not warrant a CHEBI axiom.
- Sound validation: `make travis_build` pre/post, `linkml-reference-validator`, `terms/` + `obo-checkin.pl` workflow.

## Issues

- **Over-editing / wrong pattern:** Added `relationship: has_primary_input GO:0070288 ! ferritin complex`, absent from the accepted PR. The human PR body explicitly avoided any logical axiom beyond `is_a GO:0016236` to keep `GO:7770069` consistent with sibling selective-cargo macroautophagy terms (mitophagy, ribophagy, lipophagy, glycophagy, aggrephagy, pexophagy, reticulophagy, nucleophagy), none of which carry a cargo relationship.
- This is the same divergence as the other two gpt-5.5 runs (#55, #102), indicating a model-level tendency to over-axiomatize selective-autophagy cargo rather than a one-off slip.
- The axiom is biologically defensible (GO:0070288 ferritin complex is the correct cargo), so this is a scope/consistency problem rather than a factual error — partial_success rather than failure.
