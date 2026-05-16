---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3471
pr_number: 3472
issue_title: '[Text Def] UBERON:0022232 secondary visual cortex has no textual definition'
pr_author: shawntanzk
pr_merged_at: '2025-02-04'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
domain_area: neuroanatomy
best_f1: 0.667
best_model: gemma-4-31b
---

# PR #3472 — [Text Def] UBERON:0022232 secondary visual cortex has no textual definition

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3471](https://github.com/obophenotype/uberon/issues/3471) | [PR #3472](https://github.com/obophenotype/uberon/pull/3472) | @shawntanzk | merged 2025-02-04

`axiom_repair` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #3471 reported that UBERON:0022232 (secondary visual cortex) lacked a textual definition. This is a well-characterized brain region (also known as V2 or Brodmann area 18) adjacent to the primary visual cortex, responsible for further processing of visual information.

## Changes Made

The PR added a single definition line to the secondary visual cortex term stanza in src/ontology/uberon-edit.obo. The definition describes the region's location, function in visual processing, and relationship to the primary visual cortex.

## Resolution

Simple difficulty. Adding a text definition to an existing term is a mechanical operation in OBO format. An agent needs to locate the term stanza and add a properly formatted def tag with an accurate definition. The same-day turnaround from issue to merge confirms the straightforward nature of this task.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index e9503de8d9..bbcb79658c 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -174270,6 +174270,7 @@ relationship: part_of UBERON:0002421 {source="ABA"} ! hippocampal formation
 [Term]
 id: UBERON:0022232
 name: secondary visual cortex
+def: "A functional part of the visual cortex that plays a crucial role in the integration of information from various visual modalities and contribute to higher-order visual functions, including colour, object recognition and spatial awareness." [ISBN:978-0-323-10027-4, ISSN:0072-9752, WikipediaVersioned:Visual_cortex&oldid=1268682728]
 xref: EMAPA:35758
 xref: MA:0000915
 is_a: UBERON:0035014 {source="cjm"} ! functional part of brain

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gemma-4-31b | opencode | 0.667 | 1.000 | 0.500 | `a9193a7` | [#112](https://github.com/ai4curation/eval-ont-agent-uberon/pull/112) | [attempt](attempts/pr112.md) |
| 2 | claude-haiku-4.5 | claude | 0.667 | 1.000 | 0.500 | `a9193a7` | [#95](https://github.com/ai4curation/eval-ont-agent-uberon/pull/95) | [attempt](attempts/pr95.md) |
| 3 | claude-sonnet-4.5 | claude | 0.500 | 1.000 | 0.333 | `9eed620` | [#306](https://github.com/ai4curation/eval-ont-agent-uberon/pull/306) | [attempt](attempts/pr306.md) |
| 4 | claude-sonnet-4.5 | copilot | 0.154 | 1.000 | 0.083 | `b81455e` | [#192](https://github.com/ai4curation/eval-ont-agent-uberon/pull/192) | [attempt](attempts/pr192.md) |
| 5 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `fefb6da` | [#231](https://github.com/ai4curation/eval-ont-agent-uberon/pull/231) | [attempt](attempts/pr231.md) |
| 6 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | `11c20b9` | [#79](https://github.com/ai4curation/eval-ont-agent-uberon/pull/79) | [attempt](attempts/pr79.md) |
| 7 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `1f7ecba` | [#55](https://github.com/ai4curation/eval-ont-agent-uberon/pull/55) | [attempt](attempts/pr55.md) |
| 8 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `1f7ecba` | [#36](https://github.com/ai4curation/eval-ont-agent-uberon/pull/36) | [attempt](attempts/pr36.md) |
| 9 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | `6381313` | [#18](https://github.com/ai4curation/eval-ont-agent-uberon/pull/18) | [attempt](attempts/pr18.md) |
