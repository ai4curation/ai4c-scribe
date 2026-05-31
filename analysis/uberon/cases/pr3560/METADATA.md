---
repo: obophenotype/uberon
issue_number: 3447
pr_number: 3560
issue_title: "question on parentage of 'dorsolateral prefrontal cortex'"
issue_created_at: "2024-12-13"
issue_closed_at: "2025-06-16"
pr_author: dragon-ai-agent
pr_merged_at: "2025-06-16"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 1
    deletions: 1
scoping: tightly_scoped
task_type: reclassification
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - reclassification
  - prefrontal-cortex
  - brain-anatomy
  - partonomy
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Partonomy correction requiring neuroanatomical knowledge about cortical region organization
case_quality: ok
case_quality_reason: gold_clean_but_robot_convert_reserialization_artifact_distorts_subset
scoring_caveat: "Gold PR #3560 is a clean, complete, single-line resolution and is a good reference. F1=1.0 for attempts #283/#181/#109 is genuine. However, attempts #246 (opus-4.7), #158 (gemma), #76 (gpt-5.4), #30 (gpt-5.5) made the IDENTICAL correct core edit but then ran `robot convert` per agent-config guidance, which deterministically reordered annotation-value qualifiers on ~8 unrelated lines (and a has_part/part_of pair on UBERON:8910024). This is pure non-semantic serialization churn that craters recall to ~0.125 and F1 to ~0.22. For these four attempts the metadiff F1 is NON-INDICATIVE of agent quality — all four are substantively correct successes. Do not down-weight the agents; this is a case-design/tooling interaction (config recommends `robot convert` against a non-reserialized eval base)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

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
