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
num_agent_attempts: 8
generated_at: '2026-05-15'
domain_area: thoracic-anatomy
best_f1: 1.0
best_model: claude-sonnet-4.5
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

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 1.000 | 1.000 | 1.000 | `aa95b29` | [#310](https://github.com/ai4curation/eval-ont-agent-uberon/pull/310) | [attempt](attempts/pr310.md) |
| 2 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `aa95b29` | [#188](https://github.com/ai4curation/eval-ont-agent-uberon/pull/188) | [attempt](attempts/pr188.md) |
| 3 | gemma-4-31b | opencode | 1.000 | 1.000 | 1.000 | `aa95b29` | [#138](https://github.com/ai4curation/eval-ont-agent-uberon/pull/138) | [attempt](attempts/pr138.md) |
| 4 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `aa95b29` | [#103](https://github.com/ai4curation/eval-ont-agent-uberon/pull/103) | [attempt](attempts/pr103.md) |
| 5 | gpt-5.4 | codex | 1.000 | 1.000 | 1.000 | `aa95b29` | [#86](https://github.com/ai4curation/eval-ont-agent-uberon/pull/86) | [attempt](attempts/pr86.md) |
| 6 | gpt-5.5 | opencode | 0.857 | 1.000 | 0.750 | `30e675a` | [#70](https://github.com/ai4curation/eval-ont-agent-uberon/pull/70) | [attempt](attempts/pr70.md) |
| 7 | claude-opus-4.7 | claude | 0.300 | 1.000 | 0.176 | `74f84e1` | [#248](https://github.com/ai4curation/eval-ont-agent-uberon/pull/248) | [attempt](attempts/pr248.md) |
| 8 | gpt-5.5 | codex | 0.300 | 1.000 | 0.176 | `74f84e1` | [#32](https://github.com/ai4curation/eval-ont-agent-uberon/pull/32) | [attempt](attempts/pr32.md) |
