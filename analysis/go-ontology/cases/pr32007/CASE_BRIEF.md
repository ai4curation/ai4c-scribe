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
num_agent_attempts: 14
generated_at: '2026-05-17'
domain_area: molecular_function
best_f1: 0.667
best_model: gpt-5.4
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

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-15 — base contamination, not partial gold.**

Issue #31601 was resolved by the human across **two** PRs:

- **PR #31602** ("updated definitions fixes #31601") — round 1: changed both
  `GO:0140597` and `GO:0140309` from "between two different locations" to
  "to an acceptor molecule or to a specific location", and added the
  `term_tracker_item` for #31601 to both terms.
- **PR #32007** (the selected gold) — round 2: after @hattrill reopened the
  issue asking for parent-aligned wording, changed only `GO:0140597` to
  `"Directly binding to a protein and delivering it either to an acceptor
  molecule or to a specific location."`

Round 1 (#31602) is **already present in the eval base branch**
(`eval-base-issue-31601`): the base already has the round-1 holdase wording,
so for this eval the agent only needed to make the single `GO:0140597`
revision = exactly gold PR #32007. The selected gold is therefore the correct
target for this run and the case is **not** a partial-gold problem.

The poor-case flag is for a different reason: **base/scaffold contamination.**
Every one of the 12 eval PRs — including the no-op runs from gemma-4-31b
(#524), claude-opus-4.7 (#323), and kimi-k2.6 (#284) that made no other change
— contains a byte-identical rewrite of the unrelated `GO:0102067`
(geranylgeranyl diphosphate reductase activity) definition and its xrefs
(`phytyl diphosphate ... [EC:1.3.1.83, PMID:9492312, RHEA:26229]`). This
wording comes from source PR #32006 ("Update GO:0102067 definition per sjm41
comments (refs #31963)"), which is unrelated to issue #31601. Because it
appears identically across completely different models and runtimes —
including runs that did literally nothing else — it cannot be independent
agent behavior; it is contamination of the eval base/scaffold (the round was
generated against a working tree where #32006's staged edit was present but
the metadiff base did not include it).

Consequences for scoring:

- A *fully correct* attempt (exact gold `GO:0140597` edit) is structurally
  capped at **F1 ≈ 0.667 / precision 1.0 / recall 0.5** by the phantom
  `GO:0102067` line — `best_f1: 0.667` is an artifact ceiling, not an agent
  quality limit.
- The four "F1 = 0.000" attempts (#524, #443, #323, #284) are **genuine
  failures / no-ops**: their entire diff is the contamination line and they
  never touched `GO:0140597`.
- The 0.667 attempts (#403, #221, #119) are substantively **correct
  successes**; F1 under-represents them.
- The 0.500 attempts (#490, #486, #182, #169, #139) additionally edited
  `GO:0140309` (grammar fix or full rewrite) — a genuine but defensible
  scope expansion beyond gold #32007's single-term scope.

Downstream aggregation should down-weight or exclude this case, or rescore
after subtracting the `GO:0102067` line from every attempt's diff. Companion
PR #31602 is recorded for provenance but did not need to be reproduced by the
agents (already in the eval base).

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

## Agent Attempts (14)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.667 | 1.000 | 0.500 | `8262d5a` | [#664](https://github.com/ai4curation/eval-ont-agent-go/pull/664) | [attempt](attempts/pr664.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.667 | 1.000 | 0.500 | `8262d5a` | [#403](https://github.com/ai4curation/eval-ont-agent-go/pull/403) | [attempt](attempts/pr403.md) |
| 3 | claude-haiku-4.5 | claude | 0.667 | 1.000 | 0.500 | `8262d5a` | [#221](https://github.com/ai4curation/eval-ont-agent-go/pull/221) | [attempt](attempts/pr221.md) |
| 4 | gpt-5.5 | codex | 0.667 | 1.000 | 0.500 | `cf5bf65` | [#119](https://github.com/ai4curation/eval-ont-agent-go/pull/119) | [attempt](attempts/pr119.md) |
| 5 | claude-sonnet-4.5 | claude | 0.500 | 1.000 | 0.333 | `ec98408` | [#490](https://github.com/ai4curation/eval-ont-agent-go/pull/490) | [attempt](attempts/pr490.md) |
| 6 | claude-sonnet-4.5 | claude | 0.500 | 1.000 | 0.333 | `ec98408` | [#486](https://github.com/ai4curation/eval-ont-agent-go/pull/486) | [attempt](attempts/pr486.md) |
| 7 | gpt-5.4 | codex | 0.500 | 1.000 | 0.333 | `2631049` | [#182](https://github.com/ai4curation/eval-ont-agent-go/pull/182) | [attempt](attempts/pr182.md) |
| 8 | gpt-5.5 | opencode | 0.500 | 1.000 | 0.333 | `59ca8d7` | [#169](https://github.com/ai4curation/eval-ont-agent-go/pull/169) | [attempt](attempts/pr169.md) |
| 9 | gpt-5.5 | opencode | 0.500 | 1.000 | 0.333 | `59ca8d7` | [#139](https://github.com/ai4curation/eval-ont-agent-go/pull/139) | [attempt](attempts/pr139.md) |
| 10 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `ccb7aa2` | [#624](https://github.com/ai4curation/eval-ont-agent-go/pull/624) | [attempt](attempts/pr624.md) |
| 11 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | `ccb7aa2` | [#524](https://github.com/ai4curation/eval-ont-agent-go/pull/524) | [attempt](attempts/pr524.md) |
| 12 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `ccb7aa2` | [#443](https://github.com/ai4curation/eval-ont-agent-go/pull/443) | [attempt](attempts/pr443.md) |
| 13 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `ccb7aa2` | [#323](https://github.com/ai4curation/eval-ont-agent-go/pull/323) | [attempt](attempts/pr323.md) |
| 14 | kimi-k2.6 | opencode | 0.000 | 0.000 | 0.000 | `ccb7aa2` | [#284](https://github.com/ai4curation/eval-ont-agent-go/pull/284) | [attempt](attempts/pr284.md) |
