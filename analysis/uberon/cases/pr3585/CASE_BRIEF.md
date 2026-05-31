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
num_agent_attempts: 12
generated_at: '2026-05-17'
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

## Curation Note (data quality)

Reviewed by claude-opus-4.7 on 2026-05-16 (all 9 attempts).

This is a **valid, well-formed reference case** (`case_quality: ok`), not a poor case: gold PR #3585 is the complete single-PR human resolution of issue #3490 — `gh search prs` confirms no companion PRs, there is no base-state contamination of the issue-relevant hunk, no metadiff-ignored gold field, no curator repudiation, and no out-of-scope gold extra. The issue body is the explicit ask and gold matches it.

However, scoring must be interpreted with care:

- The gold diff is **3 lines** (1 deletion + 2 additions) of pure free text: a reworded `def:` plus a new `comment:`, `[CARO:0001000]` retained. With OBO metadiff treating the def line atomically, F1 is **structurally capped near 0.40** for even a semantically perfect, scope-clean resolution. The observed best F1 is exactly 0.40.
- Gold's wording is adapted from the upstream **FBbt issue #2008** canonical proposal: def "A structure mainly consisting of cell components, rather than complete cells." and comment "May contain complete cells in addition to partial ones." Gold reordered to "consisting mainly" and expanded the comment with a glia example.
- Attempts **#135 (gemma), #295 (sonnet), #249 (opus), #33 (gpt-5.5 codex)** reproduced the FBbt canonical wording almost verbatim — conceptually **as correct as gold**, since gold itself derives from the same source — yet metadiff penalizes them for word order and comment phrasing. F1 here **under-represents quality** for scope-clean attempts.
- The genuine quality differentiator across attempts is **scope discipline**, not the definition text:
  - Cleanest: #169/#98 (haiku, single line, CARO xref kept) and #249 (opus, one extra `term_tracker_item`, strongest methodology — surveyed actual children UBERON:0012337/0018687/6040007/0012453).
  - Mild scope creep (defensible `term_tracker_item`): #68/#51 (gpt-5.5 opencode), #295 (sonnet, also added `dcterms-date` + `created_by: dragon-ai-agent`).
  - Real over-reach: #81 (gpt-5.4 codex) rewrote the `external_ontology_notes` curator-rationale free text; #33 (gpt-5.5 codex) **deleted `xref: CARO:0001000`** and swapped the def source bracket to the issue URL on a speculative equivalence-mapping argument — both unrequested and contrary to gold, which deliberately kept the CARO xref.
  - Syntax defects: #135 dropped `[CARO:0001000]` from the def and double-quoted the `comment:` value (non-standard OBO).

Net: all attempts identified the correct target term and the correct semantic change; outcomes range success → partial_success. No failures, no no_output. Downstream aggregation should treat the compressed F1 spread (0.20–0.40) as dominated by tiny-free-text metadiff geometry plus scope-creep penalties, not by correctness differences in the core definition edit.

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

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.400 | 0.333 | 0.500 | `a6f3dd8` | [#169](https://github.com/ai4curation/eval-ont-agent-uberon/pull/169) | [attempt](attempts/pr169.md) |
| 2 | claude-haiku-4.5 | claude | 0.400 | 0.333 | 0.500 | `a6f3dd8` | [#98](https://github.com/ai4curation/eval-ont-agent-uberon/pull/98) | [attempt](attempts/pr98.md) |
| 3 | gemma-4-31b | opencode | 0.333 | 0.333 | 0.333 | `a7adfde` | [#135](https://github.com/ai4curation/eval-ont-agent-uberon/pull/135) | [attempt](attempts/pr135.md) |
| 4 | gpt-5.5 | opencode | 0.333 | 0.333 | 0.333 | `fab794f` | [#68](https://github.com/ai4curation/eval-ont-agent-uberon/pull/68) | [attempt](attempts/pr68.md) |
| 5 | gpt-5.5 | opencode | 0.333 | 0.333 | 0.333 | `fab794f` | [#51](https://github.com/ai4curation/eval-ont-agent-uberon/pull/51) | [attempt](attempts/pr51.md) |
| 6 | gpt-5.4 | opencode | 0.286 | 0.333 | 0.250 | `67be0cf` | [#663](https://github.com/ai4curation/eval-ont-agent-uberon/pull/663) | [attempt](attempts/pr663.md) |
| 7 | gpt-5.4 | opencode | 0.286 | 0.333 | 0.250 | `67be0cf` | [#607](https://github.com/ai4curation/eval-ont-agent-uberon/pull/607) | [attempt](attempts/pr607.md) |
| 8 | claude-sonnet-4.5 | claude | 0.286 | 0.333 | 0.250 | `e354478` | [#295](https://github.com/ai4curation/eval-ont-agent-uberon/pull/295) | [attempt](attempts/pr295.md) |
| 9 | claude-opus-4.7 | claude | 0.286 | 0.333 | 0.250 | `a212d30` | [#249](https://github.com/ai4curation/eval-ont-agent-uberon/pull/249) | [attempt](attempts/pr249.md) |
| 10 | kimi-k2.6 | opencode | 0.250 | 0.333 | 0.200 | `610ffd9` | [#443](https://github.com/ai4curation/eval-ont-agent-uberon/pull/443) | [attempt](attempts/pr443.md) |
| 11 | gpt-5.4 | codex | 0.250 | 0.333 | 0.200 | `52e08a5` | [#81](https://github.com/ai4curation/eval-ont-agent-uberon/pull/81) | [attempt](attempts/pr81.md) |
| 12 | gpt-5.5 | codex | 0.200 | 0.333 | 0.143 | `e08fd81` | [#33](https://github.com/ai4curation/eval-ont-agent-uberon/pull/33) | [attempt](attempts/pr33.md) |
