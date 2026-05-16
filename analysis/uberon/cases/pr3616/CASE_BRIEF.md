---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3613
pr_number: 3616
issue_title: Typos in labels of UBERON:0009548 and UBERON:0009549
pr_author: dragon-ai-agent
pr_merged_at: '2025-11-03'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 5
generated_at: '2026-05-15'
domain_area: hepatic-anatomy
best_f1: 1.0
best_model: claude-sonnet-4.5
---

# PR #3616 — Typos in labels of UBERON:0009548 and UBERON:0009549

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3613](https://github.com/obophenotype/uberon/issues/3613) | [PR #3616](https://github.com/obophenotype/uberon/pull/3616) | @dragon-ai-agent | merged 2025-11-03

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Two hepatic sinusoid terms had typos in their labels: "hepatic sinusoid of left of lobe of liver" and "hepatic sinusoid of right of lobe of liver" each contained an extra "of" making the labels grammatically incorrect.

## Changes Made

Fixed the labels for UBERON:0009548 and UBERON:0009549 by removing the redundant "of" from each label. Changed "left of lobe" to "left lobe" and "right of lobe" to "right lobe" respectively. Two lines changed, two lines added.

## Resolution

Simple difficulty. The fix is a mechanical text correction in two term labels. An agent needs to locate the terms by ID and fix the obvious grammatical error. No domain knowledge is required beyond basic English grammar.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 45a291322..1554053e6 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -131431,7 +131431,7 @@ relationship: develops_from UBERON:0003324 ! mesenchyme of lower jaw
 
 [Term]
 id: UBERON:0009548
-name: hepatic sinusoid of left of lobe of liver
+name: hepatic sinusoid of left lobe of liver
 def: "A hepatic sinusoid that is part of a left lobe of liver." [OBOL:automatic]
 subset: emapa_ehdaa2
 synonym: "left lobe hepatic sinusoids" EXACT [VHOG:0000709]
@@ -131444,7 +131444,7 @@ relationship: develops_in UBERON:0001115 ! left lobe of liver
 
 [Term]
 id: UBERON:0009549
-name: hepatic sinusoid of right of lobe of liver
+name: hepatic sinusoid of right lobe of liver
 def: "A hepatic sinusoid that is part of a right lobe of liver." [OBOL:automatic]
 subset: emapa_ehdaa2
 synonym: "right lobe hepatic sinusoids" EXACT [VHOG:0000710]

```

## Agent Attempts (5)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 1.000 | 1.000 | 1.000 | `1554053` | [#312](https://github.com/ai4curation/eval-ont-agent-uberon/pull/312) | [attempt](attempts/pr312.md) |
| 2 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `1554053` | [#284](https://github.com/ai4curation/eval-ont-agent-uberon/pull/284) | [attempt](attempts/pr284.md) |
| 3 | claude-opus-4.7 | claude | 1.000 | 1.000 | 1.000 | `1554053` | [#254](https://github.com/ai4curation/eval-ont-agent-uberon/pull/254) | [attempt](attempts/pr254.md) |
| 4 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `1554053` | [#186](https://github.com/ai4curation/eval-ont-agent-uberon/pull/186) | [attempt](attempts/pr186.md) |
| 5 | gemma-4-31b | opencode | 1.000 | 1.000 | 1.000 | `1554053` | [#114](https://github.com/ai4curation/eval-ont-agent-uberon/pull/114) | [attempt](attempts/pr114.md) |
