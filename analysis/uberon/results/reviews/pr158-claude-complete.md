---
ontology: uberon
issue_number: 3447
pr_number: 3560
eval_repo_pr: 158
agent: std_opencode_gem4
model: togetherai/google/gemma-4-31B-it
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: reclassification
difficulty: medium
f1: 0.222
precision: 1.000
recall: 0.125
jaccard: 0.125
outcome: success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The gemma-4-31b / opencode run made the **correct and only substantive change** — `relationship: part_of UBERON:0000956 ! cerebral cortex` → `relationship: part_of UBERON:0000451 ! prefrontal cortex` on UBERON:0009834 — byte-identical to the gold PR #3560 hunk. It then reserialized via `robot convert` (per agent-config guidance), producing the same ~8-line annotation-qualifier reordering churn seen in attempts #246/#76/#30. F1=0.222 (P=1.0, R=0.125) **drastically under-represents quality**: this is a robot-convert reserialization-order artifact, not an ontology error. The blob (`89aefac`) is identical to attempts #246 and #76, confirming the diff is the correct DLPFC change plus deterministic serialization noise.

## Strengths

- Correct ontological reclassification despite being the smallest model: DLPFC placed `part_of` prefrontal cortex (UBERON:0000451), exactly as @dosumis requested and consistent with the Allen Brain Atlas.
- The PR comment articulates correct partonomic reasoning: DLPFC is part of prefrontal cortex, which is in turn part of cerebral cortex, so moving to the more specific parent improves hierarchical accuracy without losing the broader placement.
- Documented methodology: verified both IDs, used `obo-checkout`/`obo-checkin`, and verified the change with `git diff`.

## Issues

- Over-editing via tooling (not a reasoning error): the documented `robot convert` reserialization reordered annotation qualifiers on ~7 unrelated lines (Otomorpha `never_in_taxon`, `taxon_notes` on UBERON:0001464/0003623/0003624, accessory-nerve `dubious_for_taxon`, spleen-marginal-sinus `xref: EMAPA:37964`, UBERON:0012292 `taxon_notes`) and reordered `has_part`/`part_of` on UBERON:8910024 (airway hillock). All are semantically null permutations.
- This churn is the sole cause of recall=0.125. The agent's reasoning and target edit are exactly correct; the metadiff penalizes faithful execution of the config's `robot convert` step against a non-reserialized eval base. Treat F1 as non-indicative here (see METADATA scoring caveat). The same gemma model without `robot convert` (attempt #109) scored a clean F1=1.0.
