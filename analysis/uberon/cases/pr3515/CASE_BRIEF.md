---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3509
pr_number: 3515
issue_title: Definition of common hepatic artery is truncated
pr_author: ar-ibrahim
pr_merged_at: '2025-05-08'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
domain_area: vascular-anatomy
best_f1: 0.5
best_model: claude-haiku-4.5
---

# PR #3515 — Definition of common hepatic artery is truncated

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3509](https://github.com/obophenotype/uberon/issues/3509) | [PR #3515](https://github.com/obophenotype/uberon/pull/3515) | @ar-ibrahim | merged 2025-05-08

`axiom_repair` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #3509 reported that the text definition of the common hepatic artery was truncated, likely due to a data entry or import error. The definition was incomplete and needed to be restored to its full text.

## Changes Made

The PR made a single line change in src/ontology/uberon-edit.obo, replacing the truncated definition with the complete text for the common hepatic artery term. Despite the minimal change, three commits were needed, possibly due to formatting corrections during review.

## Resolution

Simple difficulty. This is a straightforward text correction requiring an agent to identify the truncated definition and supply the complete text. The main challenge is sourcing the correct full definition text, which could be obtained from anatomical references or the term's cross-references to other ontologies.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e3220d8bc9..887747153c 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -101453,7 +101453,7 @@ property_value: taxon_notes "In dogs, it is located to the left and often ventra
 [Term]
 id: UBERON:0005436
 name: common hepatic artery
-def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine) and pancreas. It arises from the celiac artery and has the following branches:." [Wikipedia:Common_hepatic_artery]
+def: "In anatomy, the common hepatic artery is a short blood vessel that supplies oxygenated blood to the liver, pylorus (a part of the stomach), duodenum (a part of the small intestine), pancreas, and gall bladder. It arises from the celiac artery and has the following branches: the hepatic artery proper, the gastroduodenal artery and the right gastric artery." [https://www.elsevier.com/resources/anatomy/cardiovascular-system/arteries/common-hepatic-artery/22763, Wikipedia:Common_hepatic_artery]
 synonym: "arteria hepatica communis" RELATED OMO:0003011 [Wikipedia:Common_hepatic_artery]
 synonym: "common hepatic" RELATED [Wikipedia:Common_hepatic_artery]
 xref: EHDAA2:0000308

```

## Agent Attempts (8)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | [#327](https://github.com/ai4curation/eval-ont-agent-uberon/pull/327) | [attempt](attempts/pr327.md) |
| 2 | claude-sonnet-4.5 | claude | 0.500 | 0.500 | 0.500 | [#288](https://github.com/ai4curation/eval-ont-agent-uberon/pull/288) | [attempt](attempts/pr288.md) |
| 3 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | [#269](https://github.com/ai4curation/eval-ont-agent-uberon/pull/269) | [attempt](attempts/pr269.md) |
| 4 | claude-opus-4.7 | claude | 0.500 | 0.500 | 0.500 | [#242](https://github.com/ai4curation/eval-ont-agent-uberon/pull/242) | [attempt](attempts/pr242.md) |
| 5 | gemma-4-31b | opencode | 0.500 | 0.500 | 0.500 | [#113](https://github.com/ai4curation/eval-ont-agent-uberon/pull/113) | [attempt](attempts/pr113.md) |
| 6 | gpt-5.5 | codex | 0.500 | 0.500 | 0.500 | [#28](https://github.com/ai4curation/eval-ont-agent-uberon/pull/28) | [attempt](attempts/pr28.md) |
| 7 | gpt-5.5 | opencode | 0.400 | 0.500 | 0.333 | [#63](https://github.com/ai4curation/eval-ont-agent-uberon/pull/63) | [attempt](attempts/pr63.md) |
| 8 | gpt-5.5 | opencode | 0.400 | 0.500 | 0.333 | [#44](https://github.com/ai4curation/eval-ont-agent-uberon/pull/44) | [attempt](attempts/pr44.md) |
