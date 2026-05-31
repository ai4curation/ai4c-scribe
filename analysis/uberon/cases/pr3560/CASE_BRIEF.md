---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3447
pr_number: 3560
issue_title: question on parentage of 'dorsolateral prefrontal cortex'
pr_author: dragon-ai-agent
pr_merged_at: '2025-06-16'
task_type: reclassification
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-17'
domain_area: neuroanatomy
best_f1: 1.0
best_model: gpt-5.5
---

# PR #3560 — question on parentage of 'dorsolateral prefrontal cortex'

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3447](https://github.com/obophenotype/uberon/issues/3447) | [PR #3560](https://github.com/obophenotype/uberon/pull/3560) | @dragon-ai-agent | merged 2025-06-16

`reclassification` `medium` `tightly_scoped` `approved_first_time`

## Context

The dorsolateral prefrontal cortex (UBERON:0009834) was incorrectly modeled as part_of the cerebral cortex directly, rather than being part_of the prefrontal cortex (UBERON:0000451). This skipped an intermediate level in the anatomical hierarchy.

## Changes Made

Changed the part_of relationship for dorsolateral prefrontal cortex from cerebral cortex to prefrontal cortex. A single line was modified in the term stanza. This correctly reflects that the dorsolateral prefrontal cortex is a subregion of the prefrontal cortex, which itself is part of the cerebral cortex.

## Resolution

Medium difficulty because the agent must understand brain regional organization well enough to know that the dorsolateral prefrontal cortex should be placed under the prefrontal cortex rather than directly under the broader cerebral cortex. The issue was open for six months before resolution, suggesting the fix required some deliberation.

## Curation Note (data quality)

**Flagged by:** claude-opus-4.7 on 2026-05-16.

**Gold quality:** The gold PR #3560 is a *good* reference — a clean, complete, single-line change (`relationship: part_of UBERON:0000956 ! cerebral cortex` → `relationship: part_of UBERON:0000451 ! prefrontal cortex` on UBERON:0009834). The issue (#3447) is unambiguous: @dosumis explicitly asked dragon-ai-agent to make exactly this change, citing the Allen Brain Atlas (structure 10172) as the source of truth. No companion PRs; PR #3560 is the entire human resolution. F1=1.0 for attempts #283/#181/#109 is genuine (blob `2c5b9bc` byte-identical to merged gold).

**Scoring artifact (affects 4 of 8 attempts):** Attempts #246 (claude-opus-4.7), #158 (gemma-4-31b), #76 (gpt-5.4), and #30 (gpt-5.5) all made the *identical correct core edit* but additionally ran `robot convert` to reserialize `uberon-edit.obo`, as recommended by the agent config (`ai4curation/uberon-agent-config@v3`). Against the non-reserialized eval base, `robot convert` deterministically permutes annotation-value qualifier order (e.g. `{seeAlso="...", source="bgee"}` → `{source="bgee", seeAlso="..."}`) on ~7 unrelated terms — UBERON Otomorpha `never_in_taxon`, `taxon_notes` on UBERON:0001464/0003623/0003624, accessory-nerve `dubious_for_taxon` (NCBITaxon:8292), spleen-marginal-sinus `xref: EMAPA:37964`, UBERON:0012292 `taxon_notes` — and reorders a `has_part CL:4030023`/`part_of UBERON:0007196` pair on UBERON:8910024 (airway hillock). These are semantically null serialization permutations that crater recall to ~0.125 and F1 to ~0.21–0.22.

This is the **OWL/robot-convert serialization-order reserialization-churn** poor-case signature. For attempts #246/#158/#76/#30 the metadiff F1 is **non-indicative of agent quality**; all four are substantively correct `success` outcomes (precision=1.0, every gold line reproduced). The same gemma model *without* `robot convert` (attempt #109) scored a clean F1=1.0, and the three top attempts succeeded precisely by not reserializing. Downstream aggregation should not penalize these agents on this case; the low scores reflect a case-design/tooling interaction, not reasoning failure. Attempt #313 (sonnet-4.5, F1=0.800) is a separate, minor over-editing case (added `dcterms-date` + `term_tracker_item`, no robot-convert churn).

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e4a1ef5284..2c5b9bc263 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -133364,7 +133364,7 @@ xref: FMA:276189
 xref: Wikipedia:Dorsolateral_prefrontal_cortex
 is_a: UBERON:0000481 ! multi-tissue structure
 relationship: overlaps UBERON:0006483 ! Brodmann (1909) area 46
-relationship: part_of UBERON:0000956 ! cerebral cortex
+relationship: part_of UBERON:0000451 ! prefrontal cortex
 property_value: editor_note "check dorsolateral prefrontal neocortex" xsd:string
 
 [Term]

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `2c5b9bc` | [#626](https://github.com/ai4curation/eval-ont-agent-uberon/pull/626) | [attempt](attempts/pr626.md) |
| 2 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `2c5b9bc` | [#569](https://github.com/ai4curation/eval-ont-agent-uberon/pull/569) | [attempt](attempts/pr569.md) |
| 3 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `2c5b9bc` | [#283](https://github.com/ai4curation/eval-ont-agent-uberon/pull/283) | [attempt](attempts/pr283.md) |
| 4 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `2c5b9bc` | [#181](https://github.com/ai4curation/eval-ont-agent-uberon/pull/181) | [attempt](attempts/pr181.md) |
| 5 | gemma-4-31b | opencode | 1.000 | 1.000 | 1.000 | `2c5b9bc` | [#109](https://github.com/ai4curation/eval-ont-agent-uberon/pull/109) | [attempt](attempts/pr109.md) |
| 6 | claude-sonnet-4.5 | claude | 0.800 | 1.000 | 0.667 | `283cd79` | [#313](https://github.com/ai4curation/eval-ont-agent-uberon/pull/313) | [attempt](attempts/pr313.md) |
| 7 | gpt-5.4 | opencode | 0.222 | 1.000 | 0.125 | `89aefac` | [#662](https://github.com/ai4curation/eval-ont-agent-uberon/pull/662) | [attempt](attempts/pr662.md) |
| 8 | gpt-5.4 | opencode | 0.222 | 1.000 | 0.125 | `89aefac` | [#604](https://github.com/ai4curation/eval-ont-agent-uberon/pull/604) | [attempt](attempts/pr604.md) |
| 9 | claude-opus-4.7 | claude | 0.222 | 1.000 | 0.125 | `89aefac` | [#246](https://github.com/ai4curation/eval-ont-agent-uberon/pull/246) | [attempt](attempts/pr246.md) |
| 10 | gemma-4-31b | opencode | 0.222 | 1.000 | 0.125 | `89aefac` | [#158](https://github.com/ai4curation/eval-ont-agent-uberon/pull/158) | [attempt](attempts/pr158.md) |
| 11 | gpt-5.4 | codex | 0.222 | 1.000 | 0.125 | `89aefac` | [#76](https://github.com/ai4curation/eval-ont-agent-uberon/pull/76) | [attempt](attempts/pr76.md) |
| 12 | gpt-5.5 | codex | 0.211 | 1.000 | 0.118 | `b49547e` | [#30](https://github.com/ai4curation/eval-ont-agent-uberon/pull/30) | [attempt](attempts/pr30.md) |
