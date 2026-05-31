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
num_agent_attempts: 12
generated_at: '2026-05-17'
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

## Curation Note (data quality)

`case_quality: poor` — `gold_pr_is_partial`. Flagged by claude-opus-4.7 on 2026-05-16.

Issue #3471 contained **two explicit asks**:

1. Add the suggested textual definition (verbatim wording + xrefs `ISBN:978-0-323-10027-4`, `ISSN:0072-9752`, `WikipediaVersioned:Visual_cortex&oldid=1268682728`).
2. Remove the redundant `relationship: part_of UBERON:0002021 ! occipital lobe` axiom (the reporter explicitly noted: "There already is 'part of' some 'visual cortex', and 'visual cortex' is 'part of' some 'occipital lobe'").

The gold PR #3472 (`add def for secondary visual cortex`, shawntanzk, merged 2025-02-04) only performed ask #1 — a single `+def:` line, `additions: 1, deletions: 0`. It never removed the redundant occipital-lobe axiom. Verified that the redundant `relationship: part_of UBERON:0002021 {source="MA"} ! occipital lobe` is **still present in upstream `obophenotype/uberon` master as of 2026-05-16**, and that the redundancy is genuine (UBERON:0022232 `part_of` UBERON:0000411 visual cortex, and UBERON:0000411 has `relationship: part_of UBERON:0002021 ! occipital lobe`, so the direct axiom is entailed by `part_of` transitivity). No companion PR resolved the redundancy (`gh search prs` for "3471"/"UBERON:0022232"/"secondary visual cortex" returns only #3472 as issue-linked).

Consequence: the metadiff scores systematically **under-represent** quality. All 9 agent attempts correctly removed the redundant axiom — i.e., they did the issue-mandated work that gold omitted — and are penalized on recall for it (capping F1 at ~0.667 even for byte-clean attempts, and producing F1=0.000 for attempts that paraphrased the def or carried serialization churn). Attempts should be judged against the union of the issue's two asks, not against the partial gold #3472. Downstream scoring should down-weight or exclude this case.

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

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gemma-4-31b | opencode | 0.667 | 1.000 | 0.500 | `a9193a7` | [#112](https://github.com/ai4curation/eval-ont-agent-uberon/pull/112) | [attempt](attempts/pr112.md) |
| 2 | claude-haiku-4.5 | claude | 0.667 | 1.000 | 0.500 | `a9193a7` | [#95](https://github.com/ai4curation/eval-ont-agent-uberon/pull/95) | [attempt](attempts/pr95.md) |
| 3 | claude-sonnet-4.5 | claude | 0.500 | 1.000 | 0.333 | `9eed620` | [#306](https://github.com/ai4curation/eval-ont-agent-uberon/pull/306) | [attempt](attempts/pr306.md) |
| 4 | claude-sonnet-4.5 | copilot | 0.154 | 1.000 | 0.083 | `b81455e` | [#192](https://github.com/ai4curation/eval-ont-agent-uberon/pull/192) | [attempt](attempts/pr192.md) |
| 5 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `a241a5d` | [#648](https://github.com/ai4curation/eval-ont-agent-uberon/pull/648) | [attempt](attempts/pr648.md) |
| 6 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `a241a5d` | [#590](https://github.com/ai4curation/eval-ont-agent-uberon/pull/590) | [attempt](attempts/pr590.md) |
| 7 | kimi-k2.6 | opencode | 0.000 | 0.000 | 0.000 | `fa76ca1` | [#451](https://github.com/ai4curation/eval-ont-agent-uberon/pull/451) | [attempt](attempts/pr451.md) |
| 8 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `fefb6da` | [#231](https://github.com/ai4curation/eval-ont-agent-uberon/pull/231) | [attempt](attempts/pr231.md) |
| 9 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | `11c20b9` | [#79](https://github.com/ai4curation/eval-ont-agent-uberon/pull/79) | [attempt](attempts/pr79.md) |
| 10 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `1f7ecba` | [#55](https://github.com/ai4curation/eval-ont-agent-uberon/pull/55) | [attempt](attempts/pr55.md) |
| 11 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `1f7ecba` | [#36](https://github.com/ai4curation/eval-ont-agent-uberon/pull/36) | [attempt](attempts/pr36.md) |
| 12 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | `6381313` | [#18](https://github.com/ai4curation/eval-ont-agent-uberon/pull/18) | [attempt](attempts/pr18.md) |
