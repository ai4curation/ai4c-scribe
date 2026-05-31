---
repo: geneontology/go-ontology
issue_number: 31601
pr_number: 32007
issue_title: "Textual definition update: protein carrier activity and unfolded protein holdase activity"
issue_created_at: "2026-02-18"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-28"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 1
    deletions: 1
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - textual-definition
  - protein-carrier
  - definition-update
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Minimal single-line definition change demonstrating how definition consistency is maintained across parent-child term pairs
case_quality: poor
case_quality_reason: base_contamination
companion_prs: [31602]
scoring_caveat: "Every one of the 12 eval PRs contains an identical, unrelated GO:0102067 (geranylgeranyl diphosphate reductase activity) definition/xref change that originates from source PR #32006 (refs #31963), not from any agent. It is present even in the no-op runs from gemma/kimi, so it is eval base/scaffold contamination, not over-editing. This caps achievable precision/F1 at ~0.667 for a fully correct attempt. Judge attempts against the issue's actual ask (the single GO:0140597 def revision = gold PR #32007); the round-1 holdase fix (PR #31602) is already baked into the eval base, so GO:0140309 needs no further edit for this round."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

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
