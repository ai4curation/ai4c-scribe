---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31601
pr_number: 32007
issue_title: 'Textual definition update: protein carrier activity and unfolded protein
  holdase activity'
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-28'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-15'
domain_area: molecular_function
best_f1: 0.667
best_model: claude-sonnet-4.5
---

# PR #32007 — Textual definition update: protein carrier activity and unfolded protein holdase activity

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31601](https://github.com/geneontology/go-ontology/issues/31601) | [PR #32007](https://github.com/geneontology/go-ontology/pull/32007) | @dragon-ai-agent | merged 2026-04-28

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #31601 requested updates to the textual definitions of "protein carrier activity" (GO:0140597) and "unfolded protein holdase activity" to improve clarity and structural consistency. This PR addresses the protein carrier activity definition specifically, aligning its wording with the parent term "molecular carrier activity" (GO:0140596).

## Changes Made

In `src/ontology/go-edit.obo`, a single line was changed: the `def:` field of GO:0140597 was revised to mirror the structural pattern used by its parent term. This ensures that child term definitions are recognizable specializations of their parent's definition, a key GO editorial principle.

## Resolution

Merged directly as a minimal, well-motivated definition improvement. The change was requested by @hattrill and the implementation faithfully followed the requested wording. This type of definition harmonization is common in GO maintenance and represents low-risk editorial work.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index ccb7aa216..8262d5a8a 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -468391,7 +468391,7 @@ creation_date: 2021-02-09T19:43:51Z
 id: GO:0140597
 name: protein carrier activity
 namespace: molecular_function
-def: "Binding to and carrying a protein to an acceptor molecule or to a specific location by moving along with the target protein." [PMID:7628437]
+def: "Directly binding to a protein and delivering it either to an acceptor molecule or to a specific location." [PMID:7628437]
 synonym: "protein carrier chaperone" EXACT []
 synonym: "protein chaperone" BROAD []
 intersection_of: GO:0140104 ! molecular carrier activity

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | copilot | 0.667 | 1.000 | 0.500 | `8262d5a` | [#403](https://github.com/ai4curation/eval-ont-agent-go/pull/403) | [attempt](attempts/pr403.md) |
| 2 | claude-haiku-4.5 | claude | 0.667 | 1.000 | 0.500 | `8262d5a` | [#221](https://github.com/ai4curation/eval-ont-agent-go/pull/221) | [attempt](attempts/pr221.md) |
| 3 | gpt-5.5 | codex | 0.667 | 1.000 | 0.500 | `cf5bf65` | [#119](https://github.com/ai4curation/eval-ont-agent-go/pull/119) | [attempt](attempts/pr119.md) |
| 4 | claude-sonnet-4.5 | claude | 0.500 | 1.000 | 0.333 | `ec98408` | [#490](https://github.com/ai4curation/eval-ont-agent-go/pull/490) | [attempt](attempts/pr490.md) |
| 5 | claude-sonnet-4.5 | claude | 0.500 | 1.000 | 0.333 | `ec98408` | [#486](https://github.com/ai4curation/eval-ont-agent-go/pull/486) | [attempt](attempts/pr486.md) |
| 6 | gpt-5.4 | codex | 0.500 | 1.000 | 0.333 | `2631049` | [#182](https://github.com/ai4curation/eval-ont-agent-go/pull/182) | [attempt](attempts/pr182.md) |
| 7 | gpt-5.5 | opencode | 0.500 | 1.000 | 0.333 | `59ca8d7` | [#169](https://github.com/ai4curation/eval-ont-agent-go/pull/169) | [attempt](attempts/pr169.md) |
| 8 | gpt-5.5 | opencode | 0.500 | 1.000 | 0.333 | `59ca8d7` | [#139](https://github.com/ai4curation/eval-ont-agent-go/pull/139) | [attempt](attempts/pr139.md) |
| 9 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | `ccb7aa2` | [#524](https://github.com/ai4curation/eval-ont-agent-go/pull/524) | [attempt](attempts/pr524.md) |
| 10 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `ccb7aa2` | [#443](https://github.com/ai4curation/eval-ont-agent-go/pull/443) | [attempt](attempts/pr443.md) |
| 11 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `ccb7aa2` | [#323](https://github.com/ai4curation/eval-ont-agent-go/pull/323) | [attempt](attempts/pr323.md) |
| 12 | kimi-k2.6 | opencode | 0.000 | 0.000 | 0.000 | `ccb7aa2` | [#284](https://github.com/ai4curation/eval-ont-agent-go/pull/284) | [attempt](attempts/pr284.md) |
