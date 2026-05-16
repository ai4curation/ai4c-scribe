---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3490
pr_number: 3585
issue_title: consider allowing some whole cells in a 'multi cell part structure'
pr_author: gouttegd
pr_merged_at: '2025-07-14'
task_type: axiom_repair
difficulty: hard
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
domain_area: neuroanatomy
best_f1: 0.4
best_model: claude-haiku-4.5
---

# PR #3585 — consider allowing some whole cells in a 'multi cell part structure'

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3490](https://github.com/obophenotype/uberon/issues/3490) | [PR #3585](https://github.com/obophenotype/uberon/pull/3585) | @gouttegd | merged 2025-07-14

`axiom_repair` `hard` `tightly_scoped` `approved_first_time`

## Context

The term "multi cell part structure" (UBERON:0005162) had a definition that excluded any structure containing whole cells. However, structures like gray matter and white matter, which are classified under this term, do contain some whole cells (e.g., neuronal cell bodies in gray matter). The overly restrictive definition was inconsistent with biological reality.

## Changes Made

Broadened the textual definition of UBERON:0005162 to allow for the presence of some complete cells within a multi cell part structure, while maintaining the core concept that such structures are primarily composed of cell parts (e.g., axons, dendrites). A minimal 2-line addition, 1-line deletion.

## Resolution

Hard difficulty despite the small diff because this involves careful reasoning about how a definition change affects the semantics of an upper-level term. The agent must understand that gray matter contains neuronal cell bodies (whole cells) alongside axons and synapses (cell parts), and that the definition must accommodate this biological reality without making the term too broad. Four months elapsed between issue filing and resolution, indicating significant deliberation.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index ebc698f0d..8b109e477 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -97418,7 +97418,8 @@ property_value: curator_notes "this class refers to the external portion and its
 [Term]
 id: UBERON:0005162
 name: multi cell part structure
-def: "A structure consisting of multiple cell components but which is not itself a cell and does not have (complete) cells as a part." [CARO:0001000]
+def: "A structure consisting mainly of cell components, rather than complete cells." [CARO:0001000]
+comment: Such a structure may contain some complete cells in addition to partial cells (e.g., glia in nervous system regions).
 subset: upper_level
 synonym: "cell part cluster" RELATED [FMA:83115]
 synonym: "multi-cell-component structure" EXACT [CARO:0001000]

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.400 | 0.333 | 0.500 | [#169](https://github.com/ai4curation/eval-ont-agent-uberon/pull/169) | [attempt](attempts/pr169.md) |
| 2 | claude-haiku-4.5 | claude | 0.400 | 0.333 | 0.500 | [#98](https://github.com/ai4curation/eval-ont-agent-uberon/pull/98) | [attempt](attempts/pr98.md) |
| 3 | gemma-4-31b | opencode | 0.333 | 0.333 | 0.333 | [#135](https://github.com/ai4curation/eval-ont-agent-uberon/pull/135) | [attempt](attempts/pr135.md) |
| 4 | gpt-5.5 | opencode | 0.333 | 0.333 | 0.333 | [#68](https://github.com/ai4curation/eval-ont-agent-uberon/pull/68) | [attempt](attempts/pr68.md) |
| 5 | gpt-5.5 | opencode | 0.333 | 0.333 | 0.333 | [#51](https://github.com/ai4curation/eval-ont-agent-uberon/pull/51) | [attempt](attempts/pr51.md) |
| 6 | claude-sonnet-4.5 | claude | 0.286 | 0.333 | 0.250 | [#295](https://github.com/ai4curation/eval-ont-agent-uberon/pull/295) | [attempt](attempts/pr295.md) |
| 7 | claude-opus-4.7 | claude | 0.286 | 0.333 | 0.250 | [#249](https://github.com/ai4curation/eval-ont-agent-uberon/pull/249) | [attempt](attempts/pr249.md) |
| 8 | gpt-5.4 | codex | 0.250 | 0.333 | 0.200 | [#81](https://github.com/ai4curation/eval-ont-agent-uberon/pull/81) | [attempt](attempts/pr81.md) |
| 9 | gpt-5.5 | codex | 0.200 | 0.333 | 0.143 | [#33](https://github.com/ai4curation/eval-ont-agent-uberon/pull/33) | [attempt](attempts/pr33.md) |
