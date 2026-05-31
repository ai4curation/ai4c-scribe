---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3572
pr_number: 3573
issue_title: Revise esophagus and esophageal artery partonomy
pr_author: dragon-ai-agent
pr_merged_at: '2025-07-02'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-17'
domain_area: thoracic-anatomy
best_f1: 1.0
best_model: gpt-5.4
---

# PR #3573 — Revise esophagus and esophageal artery partonomy

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3572](https://github.com/obophenotype/uberon/issues/3572) | [PR #3573](https://github.com/obophenotype/uberon/pull/3573) | @dragon-ai-agent | merged 2025-07-02

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

The esophagus had a "located in thoracic cavity" relationship, but this is anatomically incorrect because the esophagus has cervical and abdominal portions that extend beyond the thorax. Additionally, the esophageal artery used "branching part of" instead of the correct "connecting branch of" relationship to the thoracic aorta.

## Changes Made

Removed the incorrect "located in thoracic cavity" relationship from the esophagus term (UBERON:0001043). Replaced the "branching part of" relationship with "connecting branch of" for the esophageal artery (UBERON:0035539) in relation to the thoracic aorta.

## Resolution

Medium difficulty because the agent must understand that the esophagus is a long tubular organ spanning the neck, thorax, and upper abdomen, so restricting its location to the thoracic cavity is incorrect. It also requires knowing the distinction between "branching part of" and "connecting branch of" in vascular partonomy.

## Curation Note (data quality)

Reviewed 2026-05-16 (claude-opus-4.7). This is fundamentally a **good** evaluation
case: issue #3572 states exactly two precise asks, and gold PR #3573 is the complete
and sole human resolution (the only other PR referenced in the PR comments, #3576, is
an unrelated `gogoeditdiff` tooling fix). Steps 3a/3b checked — no companion PRs, no
base contamination, no gold leakage. The five F1=1.0 attempts (#310, #188, #138, #103,
#86) are **genuine** exact matches, not artifacts.

However, the metadiff F1 materially under-represents quality on three attempts and this
should be accounted for in any aggregation:

- **#248 (claude-opus-4.7) and #32 (gpt-5.5/codex): F1=0.300 is a robot-convert
  reserialization-churn artifact, not an agent error.** Both made the two requested
  axiom edits exactly correctly (precision=1.0, byte-identical to gold for the
  issue-relevant hunks). They then ran `robot convert -f obo` which reserialized ~8
  unrelated annotation blocks (attribute reordering inside `{}` on
  UBERON:0001464/0001686/0003623/0003624/0012292/etc., and a `has_part`/`part_of`
  line-order swap on airway hillock UBERON:8910024). These edits are semantically
  neutral; recall=0.176 reflects serialization line-noise only. Substantively both
  are clean successes. Contrast codex #86, which ran `robot convert` but then
  explicitly reverted the incidental reorderings (commit `14b89f7`) and scored 1.0.
- **#70 (gpt-5.5/opencode): F1=0.857** only because it added benign
  `term_tracker_item` provenance to both edited terms (a defensible UBERON convention
  the human gold PR omitted). Substantively correct.

Downstream scoring should treat #248/#32 as successes (or down-weight the
serialization-churn penalty) and #70 as a defensible-extra success, rather than taking
F1 at face value. The case itself does not need exclusion; gold and issue are sound.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 48ea1df76..aa95b2944 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -11506,7 +11506,6 @@ is_a: UBERON:0000062 {source="FMA", source="MA"} ! organ
 is_a: UBERON:0004921 ! subdivision of digestive tract
 relationship: develops_from UBERON:0001041 ! foregut
 relationship: distally_connected_to UBERON:0000945 {gci_relation="part_of", gci_filler="NCBITaxon:40674", notes="only in species that have a stomach"} ! stomach
-relationship: located_in UBERON:0002224 ! thoracic cavity
 relationship: part_of UBERON:0004908 ! upper digestive tract
 relationship: proximally_connected_to UBERON:0001042 ! chordate pharynx
 property_value: depiction "http://upload.wikimedia.org/wikipedia/commons/d/d4/Illu01_head_neck.jpg" xsd:anyURI
@@ -184163,7 +184162,7 @@ xref: UMLS:C0226294
 is_a: UBERON:0004573 {source="FMA"} ! systemic artery
 intersection_of: UBERON:0001637 ! artery
 intersection_of: vessel_supplies_blood_to UBERON:0001043 ! esophagus
-relationship: branching_part_of UBERON:0001515 {source="FMA"} ! thoracic aorta
+relationship: connecting_branch_of UBERON:0001515 {source="FMA"} ! thoracic aorta
 
 [Term]
 id: UBERON:0035542

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 1.000 | 1.000 | 1.000 | `33e7979` | [#686](https://github.com/ai4curation/eval-ont-agent-uberon/pull/686) | [attempt](attempts/pr686.md) |
| 2 | gpt-5.4 | opencode | 1.000 | 1.000 | 1.000 | `33e7979` | [#685](https://github.com/ai4curation/eval-ont-agent-uberon/pull/685) | [attempt](attempts/pr685.md) |
| 3 | kimi-k2.6 | opencode | 1.000 | 1.000 | 1.000 | `aa95b29` | [#452](https://github.com/ai4curation/eval-ont-agent-uberon/pull/452) | [attempt](attempts/pr452.md) |
| 4 | claude-sonnet-4.5 | claude | 1.000 | 1.000 | 1.000 | `aa95b29` | [#310](https://github.com/ai4curation/eval-ont-agent-uberon/pull/310) | [attempt](attempts/pr310.md) |
| 5 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `aa95b29` | [#188](https://github.com/ai4curation/eval-ont-agent-uberon/pull/188) | [attempt](attempts/pr188.md) |
| 6 | gemma-4-31b | opencode | 1.000 | 1.000 | 1.000 | `aa95b29` | [#138](https://github.com/ai4curation/eval-ont-agent-uberon/pull/138) | [attempt](attempts/pr138.md) |
| 7 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `aa95b29` | [#103](https://github.com/ai4curation/eval-ont-agent-uberon/pull/103) | [attempt](attempts/pr103.md) |
| 8 | gpt-5.4 | codex | 1.000 | 1.000 | 1.000 | `aa95b29` | [#86](https://github.com/ai4curation/eval-ont-agent-uberon/pull/86) | [attempt](attempts/pr86.md) |
| 9 | gpt-5.5 | opencode | 0.857 | 1.000 | 0.750 | `30e675a` | [#70](https://github.com/ai4curation/eval-ont-agent-uberon/pull/70) | [attempt](attempts/pr70.md) |
| 10 | claude-opus-4.7 | claude | 0.300 | 1.000 | 0.176 | `74f84e1` | [#248](https://github.com/ai4curation/eval-ont-agent-uberon/pull/248) | [attempt](attempts/pr248.md) |
| 11 | gpt-5.5 | codex | 0.300 | 1.000 | 0.176 | `74f84e1` | [#32](https://github.com/ai4curation/eval-ont-agent-uberon/pull/32) | [attempt](attempts/pr32.md) |
