---
ontology: uberon
issue_number: 3447
pr_number: 3560
eval_repo_pr: 604
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: reclassification
difficulty: medium
f1: 0.222
precision: 1.000
recall: 0.125
jaccard: 0.125
case_quality: ok
case_quality_reason: gold_clean_but_robot_convert_reserialization_artifact_distorts_subset
outcome: success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The gpt-5.4 / opencode run made the **correct and only substantive change** — on UBERON:0009834 (dorsolateral prefrontal cortex), `relationship: part_of UBERON:0000956 ! cerebral cortex` → `relationship: part_of UBERON:0000451 ! prefrontal cortex`, byte-identical to the gold PR #3560 hunk. It additionally ran `robot convert` (per agent-config guidance), which deterministically permuted annotation-value qualifier order on ~7 unrelated lines plus a `has_part`/`part_of` reorder on UBERON:8910024. The blob (`89aefac`) is identical to the other robot-convert attempts (#662/#246/#158/#76). F1=0.222 (P=1.0, R=0.125) **drastically under-represents quality**: this is the known OWL/robot-convert reserialization-churn artifact (see METADATA scoring caveat), not a reasoning failure.

## Strengths

- Correct ontological judgment: DLPFC (UBERON:0009834) is reparented to `part_of` prefrontal cortex (UBERON:0000451), exactly the change @dosumis requested in issue #3447 and consistent with the Allen Brain Atlas (structure 10172). Transitively sound, since UBERON:0000451 is itself `part_of` cerebral cortex (UBERON:0000956).
- Perfect precision (1.0): every gold line is reproduced; nothing the human did was omitted. The recall collapse is purely serialization noise, not under-editing of the issue's substance.
- Scope of intent is correct: the only *intended* edit is the single requested relationship change; all spurious lines are mechanical tool output, not deliberate edits.

## Issues

- Over-editing via tooling (not a reasoning error): `robot convert` reserialization touched ~8 unrelated lines — `never_in_taxon NCBITaxon:186634` (Otomorpha), `taxon_notes` on UBERON:0001464/UBERON:0003623/UBERON:0003624, `dubious_for_taxon NCBITaxon:8292` (accessory nerve, UBERON:0001686), `xref: EMAPA:37964` (spleen marginal sinus), `taxon_notes` on UBERON:0012292 (lateral malleolus), and a `has_part CL:4030023`/`part_of UBERON:0007196` reorder on UBERON:8910024 (airway hillock). All are qualifier/axiom order permutations with **zero semantic effect**.
- This churn is the entire cause of recall=0.125. The fault is over-faithful execution of the config's `robot convert` step against a non-reserialized eval base — a case-design/tooling interaction. The gpt-5.5 sibling runs (#626/#569) and the haiku/gemma top attempts (#283/#181/#109) succeeded by *not* reserializing. Metadiff F1 here is non-indicative of agent quality.
