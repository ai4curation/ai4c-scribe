---
ontology: go-ontology
issue_number: 30894
pr_number: 32011
eval_repo_pr: 102
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

The agent added `GO:7770069 ferritinophagy` with the same label, definition, synonym, parent, references, and provenance as the accepted human PR #32011, but added one extra axiom — `relationship: has_primary_input GO:0070288 ! ferritin complex` — that the human deliberately omitted. The metadiff score (`f1: 0.941`, `precision: 1.0`, `recall: 0.889`) slightly understates this: the extra line is a single-axiom pattern divergence, not a correctness error, but it is a genuine scope/consistency issue that the curator's accepted solution explicitly avoided.

## Strengths

- Created `GO:7770069` in `biological_process` with the standardized label `ferritinophagy` (from @ValWood's thread), not the issue body's `Ferritin-specific autophagy`.
- Used the exact accepted definition with `PMID:25327288`, `PMID:26436293`, `PMID:38714719` in gold order.
- Correct parent `is_a: GO:0016236 macroautophagy` (more specific than the issue body's `GO:0006914 autophagy`), correct `"ferritin-specific autophagy" EXACT []` synonym, correct `term_tracker_item`.
- Did not add an `intersection_of`/equivalence axiom, correctly noting no DOSDP pattern exists for selective macroautophagy.
- Sound validation: `make travis_build` pre/post, `linkml-reference-validator` on supporting excerpts, `terms/` + `obo-checkin.pl` workflow.

## Issues

- **Over-editing / wrong pattern:** Added `relationship: has_primary_input GO:0070288 ! ferritin complex`, which is absent from the accepted PR. The human PR body explicitly states no logical axioms beyond `is_a GO:0016236` were added, to stay consistent with sibling selective-cargo macroautophagy terms (mitophagy, ribophagy, lipophagy, glycophagy, aggrephagy, pexophagy, reticulophagy, nucleophagy), none of which carry a cargo relationship. Adding it only to `GO:7770069` creates a one-off inconsistency in the selective-autophagy cluster.
- The agent's rationale called the `has_primary_input` relationship "necessary." This overstates the modeling requirement and directly conflicts with the accepted curator judgment; if GO wants cargo axioms on selective-autophagy terms, that should be a coordinated design-pattern pass, not a single-term addition.
- The axiom is biologically defensible (ferritinophagy does target the ferritin complex, GO:0070288 is the correct cargo class), so this is a scope/consistency problem rather than a factual error — hence partial_success rather than failure.
