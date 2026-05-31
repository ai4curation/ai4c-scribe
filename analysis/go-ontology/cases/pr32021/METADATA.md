---
repo: geneontology/go-ontology
issue_number: 32018
pr_number: 32021
issue_title: "Obsoletion request: ergothioneine biosynthetic process terms"
issue_created_at: "2026-04-30"
pr_author: edwong57
pr_merged_at: "2026-05-04"
pr_num_commits: 1
files_changed:
  - path: src/taxon_constraints/only_in_taxon.tsv
    additions: 0
    deletions: 2
scoping: tightly_scoped
task_type: obsoletion
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - taxon-constraint
  - only_in_taxon
  - ergothioneine
  - cleanup
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Simple taxon constraint removal as part of term obsoletion workflow, showing that obsoletion involves cleanup across multiple files
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [32023, 32069]
scoring_caveat: "metadiff vs #32021 only covers the taxon-constraint sub-step (2 line deletions); the full human resolution of issue #32018 is the union of #32021 + #32023 + #32069. Judge attempts against the issue and that union, not the metadiff F1."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #32018 requested obsoletion of ergothioneine biosynthetic process terms (GO:0140479 and GO:0052704). Before these terms could be fully obsoleted, their taxon constraints in `only_in_taxon.tsv` needed to be removed. This PR handles that specific cleanup step.

## Changes Made

In `src/taxon_constraints/only_in_taxon.tsv`, two rows were removed:
- The entry for GO:0140479 (ergothioneine biosynthetic process)
- The entry for GO:0052704 (related ergothioneine term)

This is a pure deletion with no additions, reflecting the removal of constraints that are no longer meaningful for terms being obsoleted.

## Resolution

Merged directly. This is a routine cleanup step in the GO obsoletion workflow: when a term is obsoleted, its taxon constraints must also be removed since they no longer serve a purpose. The change is purely mechanical and low-risk.

## Curation Note (data quality)

**This is a poor evaluation case — the selected gold PR is only a sub-step of the human resolution.**

Issue #32018 asked for the full obsoletion of `GO:0052704` and `GO:0140479`, replacement by the parent `GO:0052699`, and addition of two MetaCyc pathway xrefs (`PWY-7255`, `PWY-7550`) as `skos:narrowMatch` to `GO:0052699`. The humans split this work across **three** PRs:

- **#32021** (the selected `pr_number`/gold) — only deletes the two `only_in_taxon.tsv` rows (the taxon-constraint precondition; obsoletion CI fails until these are removed).
- **#32023** — adds the MetaCyc narrowMatch xrefs to `GO:0052699`, obsoletes `GO:0140479`, rewires the dependent MF `part_of` link.
- **#32069** — obsoletes `GO:0052704`, fixes the `GO:0052707` `replaced_by` chain, rewires its dependent MF `part_of` link.

Because the metadiff compares each attempt only against #32021 (≈2 lines of a much larger change), 10/11 attempts score F1 = 0.000 and the "best" is 0.148 — even though agents that did the full, correct obsoletion in a single PR (e.g. Attempt 1 / eval PR #222) effectively reproduced the union of all three human PRs.

**For scoring/aggregation:** exclude or down-weight this case's metadiff. **For review:** judge attempts against the issue text and the union of #32021 + #32023 + #32069, not the single gold PR.

Flagged by claude-opus-4.7 on 2026-05-15 during a `review-agent-pr` session.
