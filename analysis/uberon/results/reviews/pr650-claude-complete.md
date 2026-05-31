---
ontology: uberon
issue_number: 3475
pr_number: 3477
eval_repo_pr: 650
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

This gpt-5.4/opencode attempt addressed **both** explicit asks of issue #3475: it removed the incorrect placement of UBERON:0002835 (thoracic dorsal root ganglion) under UBERON:0000961, and it renamed UBERON:0000961 from "thoracic ganglion" to "thoracic paravertebral ganglion" with a rewritten definition and synonym restructuring. The metadiff F1 of 0.222 (P=1.0, R=0.125) **severely under-represents** the conceptual quality — it is low only because gold PR #3477 did just the one-line `is_a` deletion and never performed the rename the issue explicitly demanded (established poor case, `gold_pr_is_partial`). The reason this is graded `partial_success` rather than `success` is a real modeling defect in ask #1: instead of *deleting* `is_a: UBERON:0000961`, the agent **replaced** it with `is_a: UBERON:0000044 ! dorsal root ganglion`, which is logically redundant.

## Strengths

- **Both issue asks attempted.** The wrong parent (UBERON:0000961, the paravertebral/sympathetic ganglion) is removed from UBERON:0002835, achieving the core conceptual fix that a sensory dorsal root ganglion must not be classified as a thoracic paravertebral/sympathetic ganglion.
- **Rename (ask #2) done well.** Renamed UBERON:0000961 → "thoracic paravertebral ganglion", rewrote the WP-derived def into a concise class-appropriate definition ("A paravertebral ganglion that is part of the thoracic sympathetic nerve trunk..."), and converted the now-ambiguous "thoracic ganglion" string into a RELATED synonym rather than dropping it — consistent with the issue's reasoning that "thoracic ganglion" is too broad.
- **Tight scope and good methodology.** No tracker-item noise, no `def` damage elsewhere, and (per the PR comment) the agent explicitly inspected UBERON:0000961/0002835/0000044/0009630, used the obo-checkout/checkin workflow, and stripped serializer-driven label churn before committing — avoiding the file-regeneration contamination seen in #11/#193.
- Honest, accurate neuroanatomical rationale in the PR narrative, including correctly noting the ID/label drift in the current snapshot.

## Issues

- **Redundant `is_a` re-assertion (wrong pattern, ask #1).** Gold deleted the `is_a: UBERON:0000961` line cleanly. This attempt instead rewrote it to `is_a: UBERON:0000044 ! dorsal root ganglion`. UBERON:0002835 already carries `intersection_of: UBERON:0000044` + `intersection_of: extends_fibers_into UBERON:0009630`, so `is_a: UBERON:0000044` is already entailed by the equivalence axiom; asserting it explicitly is redundant per Uberon's genus-differentia convention. This is the same defect as #96 and is less clean than #319's pure deletion. Not a correctness error (the entailed hierarchy is right), but a modeling-hygiene flaw.
- **Lost MA provenance.** Promoting "thoracic paravertebral ganglion" (previously `synonym: ... EXACT [MA:0001159]`) to the primary label dropped the explicit `[MA:0001159]` provenance annotation. A curator might have retained it as an `xref` or a provenance-bearing synonym. Same minor issue as #319/#232.
- **RELATED vs EXACT demotion.** Demoting the old primary "thoracic ganglion" to a RELATED synonym is defensible but weaker than #319's EXACT demotion — "thoracic ganglion" is a true exact-string label for this class in MA/FMA usage, just ambiguous; EXACT preserves searchability better.
- **Minor out-of-scope edit.** The diff removes a trailing blank line at EOF (after the `vessel_supplies_blood_to` typedef). This is a `robot convert` serializer artifact, not issue-relevant; harmless but slightly outside scope.

Graded `partial_success`: the conceptual resolution of both issue asks is sound, but the redundant `is_a: UBERON:0000044` re-assertion (rather than a clean deletion) is a genuine pattern defect. Note #319 remains the cleanest full resolution of this issue. Low metadiff is a poor-case artifact (see METADATA.md), not a quality signal.
