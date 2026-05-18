---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31981
pr_number: 31995
issue_title: 'Missing parent: GO:0072318 clathrin coat disassembly'
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-28'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 13
generated_at: '2026-05-17'
best_f1: 1.0
best_model: gpt-5.4
---

# PR #31995 — Missing parent: GO:0072318 clathrin coat disassembly

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31981](https://github.com/geneontology/go-ontology/issues/31981) | [PR #31995](https://github.com/geneontology/go-ontology/pull/31995) | @dragon-ai-agent | merged 2026-04-28

`axiom_repair` `simple` `tightly_scoped` `approved_first_time`

## Context

GO:0072318 `clathrin coat disassembly` was missing a `part_of` relationship to `GO:0072583 clathrin-dependent endocytosis`. While its parent term GO:0072319 `vesicle uncoating` already had a `part_of` to the more general `GO:0016192 vesicle-mediated transport`, the specific connection to clathrin-dependent endocytosis was absent. This gap was identified by ValWood during a review of vesicle-mediated transport term relationships.

## Changes Made

Two lines were added to the GO:0072318 stanza in `go-edit.obo`: a `relationship: part_of GO:0072583 ! clathrin-dependent endocytosis` axiom and a `property_value: term_tracker_item` linking back to issue #31981. No existing content was modified or removed. The addition makes explicit that clathrin coat disassembly is a step within clathrin-dependent endocytosis, complementing the existing is_a parent `vesicle uncoating`.

## Resolution

Easy difficulty because this was a straightforward addition of a missing axiom with no ambiguity about the biological relationship. Clathrin coat disassembly (uncoating) is universally recognized as a step in clathrin-dependent endocytosis, occurring after the clathrin-coated vesicle has pinched off from the plasma membrane. The minimal 2-line addition reflects the surgical nature of the fix.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index f53920e0d..5b4d6c89f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -401425,6 +401425,8 @@ synonym: "clathrin-coated vesicle uncoating" EXACT [GOC:mah]
 is_a: GO:0072319 ! vesicle uncoating
 intersection_of: GO:0022411 ! cellular component disassembly
 intersection_of: results_in_disassembly_of GO:0030118 ! clathrin coat
+relationship: part_of GO:0072583 ! clathrin-dependent endocytosis
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31981" xsd:anyURI
 created_by: mah
 creation_date: 2010-10-26T12:03:37Z
 

```

## Agent Attempts (13)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 1.000 | 1.000 | 1.000 | `5b4d6c8` | [#657](https://github.com/ai4curation/eval-ont-agent-go/pull/657) | [attempt](attempts/pr657.md) |
| 2 | gpt-5.4 | opencode | 1.000 | 1.000 | 1.000 | `5b4d6c8` | [#609](https://github.com/ai4curation/eval-ont-agent-go/pull/609) | [attempt](attempts/pr609.md) |
| 3 | claude-sonnet-4.5 | copilot | 1.000 | 1.000 | 1.000 | `5b4d6c8` | [#493](https://github.com/ai4curation/eval-ont-agent-go/pull/493) | [attempt](attempts/pr493.md) |
| 4 | claude-sonnet-4.5 | claude | 1.000 | 1.000 | 1.000 | `5b4d6c8` | [#478](https://github.com/ai4curation/eval-ont-agent-go/pull/478) | [attempt](attempts/pr478.md) |
| 5 | claude-sonnet-4.5 | copilot | 1.000 | 1.000 | 1.000 | `5b4d6c8` | [#428](https://github.com/ai4curation/eval-ont-agent-go/pull/428) | [attempt](attempts/pr428.md) |
| 6 | claude-opus-4.7 | claude | 1.000 | 1.000 | 1.000 | `5b4d6c8` | [#345](https://github.com/ai4curation/eval-ont-agent-go/pull/345) | [attempt](attempts/pr345.md) |
| 7 | kimi-k2.6 | opencode | 1.000 | 1.000 | 1.000 | `5b4d6c8` | [#281](https://github.com/ai4curation/eval-ont-agent-go/pull/281) | [attempt](attempts/pr281.md) |
| 8 | gemma-4-31b | opencode | 1.000 | 1.000 | 1.000 | `c0cbbc2` | [#248](https://github.com/ai4curation/eval-ont-agent-go/pull/248) | [attempt](attempts/pr248.md) |
| 9 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | `ae07bb5` | [#215](https://github.com/ai4curation/eval-ont-agent-go/pull/215) | [attempt](attempts/pr215.md) |
| 10 | gpt-5.4 | codex | 1.000 | 1.000 | 1.000 | `5b4d6c8` | [#197](https://github.com/ai4curation/eval-ont-agent-go/pull/197) | [attempt](attempts/pr197.md) |
| 11 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `5b4d6c8` | [#97](https://github.com/ai4curation/eval-ont-agent-go/pull/97) | [attempt](attempts/pr97.md) |
| 12 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `5b4d6c8` | [#80](https://github.com/ai4curation/eval-ont-agent-go/pull/80) | [attempt](attempts/pr80.md) |
| 13 | gpt-5.5 | codex | 1.000 | 1.000 | 1.000 | `5b4d6c8` | [#57](https://github.com/ai4curation/eval-ont-agent-go/pull/57) | [attempt](attempts/pr57.md) |
