---
ontology: uberon
issue_number: 3475
pr_number: 3477
eval_repo_pr: 56
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: axiom_repair
difficulty: medium
f1: 0.154
precision: 1.000
recall: 0.083
jaccard: 0.083
outcome: partial_success
failure_modes: [over_editing]
case_quality: poor
case_quality_reason: gold_pr_is_partial
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent removed `is_a: UBERON:0000961` from UBERON:0002835 (ask #1) and renamed UBERON:0000961 → "thoracic paravertebral ganglion" (ask #2), addressing both explicit requests of issue #3475. It also rewrote the definition (fixing the "splancic"/"splanchic" misspellings), changed two automatic synonyms to BROAD scope, and added a term_tracker_item. The metadiff F1 of 0.154 under-represents the core correctness but the def rewrite is genuine scope creep. Outcome `partial_success`. Note: byte-identical agent diff to attempt #37 (same blob `f5512c1`). This is a `case_quality: poor` case (gold PR partial — see METADATA.md).

## Strengths

- **Both issue asks satisfied:** spurious is_a removed, UBERON:0000961 renamed to "thoracic paravertebral ganglion" per the issue text.
- **Best synonym scope choice of the rename attempts:** demoted `ganglion of thorax` and `thorax ganglion` to `BROAD` (rather than deleting them like #19/#11, or RELATED). BROAD is arguably the most defensible scope here — those strings denote a genuinely broader concept ("any ganglion in the thorax") relative to the now-narrowed paravertebral class — and it preserves searchability and the OBOL:automatic provenance.
- Methodology evidence: reviewed both stanzas, checked parent terms (`paravertebral ganglion`, `thoracic sympathetic nerve trunk`, `dorsal root ganglion`), reserialized and validated with ROBOT.
- No file-regeneration contamination (contrast #11/#193).

## Issues

- **Over-editing (def rewrite):** Replaced the curated Wikipedia-sourced definition with a paraphrase. It usefully corrects the "splancic"/"splanchic" typos and reads cleanly, but the issue did not request a definition change; rewriting curated text is out of scope and risks subtle meaning drift.
- **Scope creep:** Added `property_value: term_tracker_item ...` to UBERON:0002835 (not requested; gold did not).
- The `def` xref was changed from `[Wikipedia:Thoracic_ganglion]` retained but the `[WP,unvetted]` provenance marker in the def string was dropped along with the rewrite — minor provenance loss.
- Net: issue correctly resolved; recall (0.083) is depressed both by the partial gold and by the unrequested def/synonym edits.
