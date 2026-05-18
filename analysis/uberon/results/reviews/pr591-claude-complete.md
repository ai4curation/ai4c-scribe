---
ontology: uberon
issue_number: 3475
pr_number: 3477
eval_repo_pr: 591
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: axiom_repair
difficulty: medium
f1: 0.222
precision: 1.000
recall: 0.125
jaccard: 0.125
outcome: partial_success
failure_modes:
  - wrong_pattern
case_quality: poor
case_quality_reason: gold_pr_is_partial
scoring_caveat: "Issue #3475 explicitly requested TWO changes: (1) remove is_a UBERON:0000961 from UBERON:0002835, and (2) rename UBERON:0000961 'thoracic ganglion' -> 'thoracic paravertebral ganglion'. Gold PR #3477 performed only change (1) (a single-line deletion, 0 additions). Change (2) was never made by curators (Uberon HEAD still has name: thoracic ganglion; no companion PR found). Metadiff vs #3477 therefore rewards minimal/partial answers and penalizes attempts that correctly did BOTH issue asks. Judge attempts against the issue text, not the partial gold."
companion_prs: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This gpt-5.4/opencode attempt (#591) produces a diff **byte-identical** to attempt #650 (same blob `567d5d1`, same F1=0.222 / P=1.0 / R=0.125) — a stable, reproducible output from the same model/runtime. It addressed **both** explicit asks of issue #3475: removed the incorrect placement of UBERON:0002835 (thoracic dorsal root ganglion) under UBERON:0000961, and renamed UBERON:0000961 "thoracic ganglion" → "thoracic paravertebral ganglion" with a rewritten def and synonym restructuring. The metadiff **severely under-represents** quality (gold PR #3477 did only the one-line `is_a` deletion, never the rename — established poor case, `gold_pr_is_partial`). Graded `partial_success` for the same modeling defect as #650: ask #1 was done by *replacing* `is_a: UBERON:0000961` with a redundant `is_a: UBERON:0000044` rather than deleting the line.

## Strengths

- **Both issue asks satisfied conceptually.** UBERON:0002835 no longer sits under the paravertebral/sympathetic UBERON:0000961 (core fix: a sensory DRG must not be a sympathetic ganglion), and UBERON:0000961 is renamed to "thoracic paravertebral ganglion" exactly as the issue requested.
- **Clean rename handling.** Def rewritten to a concise, class-accurate statement ("A paravertebral ganglion that is part of the thoracic sympathetic nerve trunk..."); the now-ambiguous "thoracic ganglion" string retained as a RELATED synonym instead of being dropped.
- **Tightly scoped.** No tracker-item noise, no def damage on unrelated terms, no ODK file-regeneration contamination (contrast #11/#193). Single file touched.
- **Reproducibility.** Identical to #650 — indicates a deterministic, non-flaky approach for this case from gpt-5.4/opencode.

## Issues

- **Redundant `is_a` re-assertion (wrong pattern, ask #1).** Like #650/#96, rewrote `is_a: UBERON:0000961` → `is_a: UBERON:0000044 ! dorsal root ganglion` instead of deleting it. UBERON:0002835 already has `intersection_of: UBERON:0000044` + `intersection_of: extends_fibers_into UBERON:0009630`, so `is_a: UBERON:0000044` is already entailed; asserting it explicitly is redundant under Uberon genus-differentia convention and less clean than gold's / #319's pure deletion. Hierarchy is correct, but the pattern is a modeling-hygiene flaw.
- **Lost MA provenance.** Promoting "thoracic paravertebral ganglion" (was `synonym: ... EXACT [MA:0001159]`) to the primary label dropped the explicit `[MA:0001159]` provenance. Minor; same as #319/#232/#650.
- **RELATED vs EXACT demotion.** Demoting "thoracic ganglion" to RELATED is defensible but weaker than #319's EXACT demotion for a true (if ambiguous) exact label.
- **Minor out-of-scope edit.** Removes a trailing EOF blank line after the `vessel_supplies_blood_to` typedef — a `robot convert` serializer artifact, not issue-relevant. Harmless.
- **No agent PR/issue comment captured** in the attempt record (unlike #650, which had a detailed rationale), so methodology can only be inferred from the diff; the diff itself is well-scoped.

Graded `partial_success`: conceptually resolves both issue asks, but the redundant `is_a: UBERON:0000044` (rather than a clean deletion) is a genuine pattern defect. #319 remains the cleanest full resolution. Low metadiff is a poor-case artifact (see METADATA.md), not a quality signal.
