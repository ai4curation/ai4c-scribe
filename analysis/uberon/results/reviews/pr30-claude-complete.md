---
ontology: uberon
issue_number: 3447
pr_number: 3560
eval_repo_pr: 30
agent: std_codex_gpt55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: reclassification
difficulty: medium
f1: 0.211
precision: 1.000
recall: 0.118
jaccard: 0.118
outcome: success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The gpt-5.5 / codex run made the **correct core change** — `relationship: part_of UBERON:0000956 ! cerebral cortex` → `relationship: part_of UBERON:0000451 ! prefrontal cortex` on UBERON:0009834 — and additionally appended `property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3447" xsd:anyURI` to the stanza. It then ran `robot convert`, producing the same annotation-qualifier reordering churn as #246/#158/#76 (blob `b49547e`, slightly different from `89aefac` only because of the extra `term_tracker_item` line). F1=0.211 (P=1.0, R=0.118) — marginally lower than the other churn attempts solely due to the one extra provenance line — **drastically under-represents quality**: this is a robot-convert serialization-order artifact plus one conventional provenance addition, not an agent error.

## Strengths

- Correct ontological reclassification: DLPFC placed `part_of` prefrontal cortex (UBERON:0000451), exactly as @dosumis requested and consistent with the Allen Brain Atlas. The PR comment correctly notes UBERON:0000451 is itself `part_of` cerebral cortex, so the broader placement is preserved while making the immediate parent more specific.
- Most thorough validation of the codex attempts: read `__issue_context__.json`, checked the UBERON:0009834 stanza and the proposed parent for consistency, used `obo-checkout.pl`/`obo-checkin.pl`, validated OBO parsing with a temp `robot convert`, and ran `git diff --check` for whitespace.
- Adding `term_tracker_item` for issue #3447 is a defensible OBO provenance practice.

## Issues

- Over-editing via tooling and provenance (not reasoning errors): `robot convert` reserialization reordered annotation qualifiers on ~7 unrelated lines and reordered `has_part`/`part_of` on UBERON:8910024 (airway hillock); separately, an extra `term_tracker_item` line was added beyond the minimal gold diff.
- Together these are the entire cause of recall=0.118. The `term_tracker_item` is defensible provenance; the dominant penalty is the serialization churn from faithfully running the config's `robot convert` step against a non-reserialized eval base. Treat F1 as non-indicative of agent quality (see METADATA scoring caveat).
