---
ontology: go-ontology
issue_number: 30894
pr_number: 32011
eval_repo_pr: 55
agent: std_codex_g55
model: gpt-5.5
runtime: codex
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

The agent added `GO:7770069 ferritinophagy` matching the accepted human PR #32011 on label, definition, synonym, parent, references, and provenance, but added one extra axiom — `relationship: has_primary_input GO:0070288 ! ferritin complex` — that the human deliberately omitted. The metadiff score (`f1: 0.941`, `precision: 1.0`, `recall: 0.889`) slightly understates the quality: the extra line is a single-axiom pattern divergence, not a correctness error, but it is a genuine scope/consistency issue the curator's accepted solution explicitly avoided.

## Strengths

- Created `GO:7770069` in `biological_process` with the standardized label `ferritinophagy` (from @ValWood's thread comment), not the issue body's `Ferritin-specific autophagy`.
- Used the exact accepted definition with `PMID:25327288`, `PMID:26436293`, `PMID:38714719` in gold order.
- Correct parent `is_a: GO:0016236 macroautophagy` (more specific than the issue body's `GO:0006914 autophagy`), correct `"ferritin-specific autophagy" EXACT []` synonym, correct `term_tracker_item`.
- Declined to add an `intersection_of`/equivalence axiom, correctly noting no dedicated DOSDP exists for "X-phagy" terms; cited specific sibling precedents (ribophagy, aggrephagy, lipophagy, reticulophagy, xenophagy).
- Strong methodology and reporting: `/research` and `/design-pattern` skills exercised, `make travis_build` pre/post, `linkml-reference-validator` on supporting excerpts, `terms/` + `obo-checkin.pl` workflow, scratch files left uncommitted.

## Issues

- **Over-editing / wrong pattern:** Added `relationship: has_primary_input GO:0070288 ! ferritin complex`, absent from the accepted PR. The human PR body explicitly says no logical axioms beyond `is_a GO:0016236` were added, for consistency with sibling selective-cargo macroautophagy terms (mitophagy, ribophagy, lipophagy, glycophagy, aggrephagy, pexophagy, reticulophagy, nucleophagy), none of which carry a cargo relationship. Adding it only here introduces a one-off inconsistency.
- The agent described the relationship as one it "added ... as a necessary relationship." This overstates the requirement and conflicts with the accepted curator judgment; cargo axioms for selective autophagy should be a coordinated design-pattern pass, not a single-term addition.
- This is the third gpt-5.5 run (with #81, #102) to make the same `has_primary_input` over-edit, confirming a consistent model-level pattern rather than chance. The axiom is biologically defensible (GO:0070288 is the correct cargo class), so this is a scope/consistency problem, not a factual error — partial_success rather than failure.
