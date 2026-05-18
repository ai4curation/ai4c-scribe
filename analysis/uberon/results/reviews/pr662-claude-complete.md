---
ontology: uberon
issue_number: 3447
pr_number: 3560
eval_repo_pr: 662
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

The gpt-5.4 / opencode run made the **correct and only substantive change** — on UBERON:0009834 (dorsolateral prefrontal cortex), `relationship: part_of UBERON:0000956 ! cerebral cortex` → `relationship: part_of UBERON:0000451 ! prefrontal cortex`, byte-identical to the gold PR #3560 hunk. It then followed the agent-config guidance to reserialize via `robot convert`, which deterministically reordered annotation-value qualifiers on ~7 unrelated lines plus a `has_part`/`part_of` pair on UBERON:8910024. F1=0.222 (P=1.0, R=0.125) **drastically under-represents quality**: this is the known OWL/robot-convert reserialization-churn artifact (see METADATA scoring caveat), not an agent reasoning failure. Precision=1.0: every gold line is reproduced.

## Strengths

- Correct ontological judgment: DLPFC (UBERON:0009834) is reparented to `part_of` prefrontal cortex (UBERON:0000451) exactly as @dosumis requested, with correct rationale that the prior cerebral-cortex placement is preserved transitively (UBERON:0000451 is `part_of` UBERON:0000956) while the asserted parent becomes more specific.
- Transparent, well-documented methodology: the PR comment cites the Allen Brain Atlas, documents the `obo-checkout.pl`/`obo-checkin.pl` workflow, validation via `robot convert`, and a diff review — and the core edit is exactly right.
- Precision is perfect (1.0): no gold change was missed; the recall collapse is entirely non-semantic serialization noise, not omission.

## Issues

- Over-editing via tooling (not a reasoning error): `robot convert` reserialization permuted qualifier order on unrelated terms — `never_in_taxon NCBITaxon:186634` (Otomorpha), `taxon_notes` on UBERON:0001464/UBERON:0003623/UBERON:0003624, `dubious_for_taxon NCBITaxon:8292` (accessory nerve, UBERON:0001686), `xref: EMAPA:37964` (spleen marginal sinus), `taxon_notes` on UBERON:0012292 (lateral malleolus) — and reordered the `has_part CL:4030023`/`part_of UBERON:0007196` pair on UBERON:8910024 (airway hillock). All are order-only permutations with **zero semantic effect**.
- This serialization churn is the entire cause of recall=0.125. The agent's only fault is over-faithfully executing the config's `robot convert` step against a non-reserialized eval base. The gpt-5.5 sibling runs (#626/#569) and the haiku/gemma top attempts succeeded precisely by *not* emitting this churn. Metadiff F1 here is non-indicative of agent quality.
