---
repo: obophenotype/cell-ontology
issue_number: 3010
pr_number: 3225
issue_title: "[Obsolete] structural cell"
issue_created_at: "2024-11-01"
pr_author: Caroline-99
pr_merged_at: "2025-08-07"
pr_num_commits: 2
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 9
    deletions: 7
scoping: loosely_scoped
scoping_notes: "PR obsoletes CL:0000293 and also rewires two dependent classes (scleral cell, choroidal cell) to point to CL:0000000 instead. Multiple conceptual operations in one PR."
eval_suitability: unusable
eval_suitability_notes: "PR was auto-linked to issue #3224 (skos:prefLabel import bug) but actually addresses issue #3010 (obsolete structural cell). Agent given #3224 cannot produce the expected diff."
task_type: obsoletion
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: ontology-maintenance
tags:
  - obsoletion
  - structural-cell
  - cascade-fix
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Obsoletion with cascading fixes to dependent terms. Agent must understand that obsoleting a term requires also rewiring all classes that reference it.
agent_coverage: none
agent_coverage_note: "no eval attempts generated as of 2026-05-16"
case_quality: poor
case_quality_reason: issue_pr_mismatch_thin_issue
companion_prs: []
scoring_caveat: "PR #3225 is GitHub-auto-linked to issue #3224 (skos:prefLabel import bug) but actually resolves issue #3010 (obsolete structural cell), evidenced only by the IAO:0000233 tracking annotation in the diff. Issue #3010 has an empty body and no comments. An agent prompted with #3224 cannot produce this diff; an agent prompted with the near-empty #3010 has almost no signal. Closed predecessor PR #3222 (same author) was superseded by #3225 — no companion PRs. Gold edit itself is ontologically sound; the case is poor for scoring, not the gold for correctness. Consistent with the existing eval_suitability: unusable flag."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3010 requested obsoleting CL:0000293 "structural cell" — a grouping term with only two subclasses that was deemed unsustainable. Note: the PR was automatically linked to issue #3224 (a `skos:prefLabel` import bug from MBAO) but the actual work is driven by #3010, as evidenced by the `IAO:0000233` tracking annotation in the diff.

## Changes Made

Modified `cl-edit.owl` with 9 additions and 7 deletions across three classes:

1. **CL:0000293 (structural cell)**: obsoleted — added deprecated flag, "OBSOLETE" prefix to definition, obsoletion reason comment, tracking issue link
2. **CL:0000347 (scleral cell)**: rewired equivalence axiom from `CL_0000293` to `CL_0000000` (cell)
3. **CL:0000348 (choroidal cell)**: rewired equivalence axiom from `CL_0000293` to `CL_0000000`, updated definition to remove "structural cell" reference

## Resolution

Approved on first review. Hard difficulty because the agent must understand the obsoletion cascade: you cannot just deprecate a term — you must also find and fix all downstream references. The two dependent classes needed their logical definitions rewritten to point to a new parent.

## Curation Note (data quality)

Flagged `case_quality: poor` on 2026-05-16 by claude-opus-4.7.

This case has **no eval attempts** (`num_agent_attempts: 0`, no `attempts/`
directory) as of 2026-05-16 — an eval-coverage gap, not an agent failure.
(The CASE_BRIEF.md prose claim "All three agent attempts scored 0.0 F1" is a
stale brief-generation artifact inconsistent with the empty case directory.)

Two compounding poor-case problems make this an unreliable scoring reference,
independent of the missing attempts:

1. **Issue/PR mismatch.** PR #3225 is GitHub-auto-linked to issue **#3224**
   (a `skos:prefLabel` MBAO import bug), and the PR body says the work was
   "manually editing the cl-edit.owl file related to issue #3224". The actual
   driving issue is **#3010** (obsolete structural cell), evidenced only by
   the `IAO:0000233` tracking annotation inside the diff. The metadiff target
   is unreachable from either prompt framing.
2. **Thin issue.** Issue #3010 has an empty body and no comments — only the
   title "Only has 2 subclasses! Some work needed to find new homes for
   these". No CL ID, no reparenting target, no obsoletion-reason text.

There are **no companion PRs**: the only related PR, #3222 (same author
@Caroline-99, "obsoleted structural cell"), was closed and superseded by
#3225, which is the whole human resolution.

The gold edit (CL:0000293 obsoleted; CL:0000347/CL:0000348 equivalence
axioms rewired CL_0000293→CL_0000000; CL:2000070 reparented at classified
level) is **ontologically sound and exemplary** — retain for qualitative use.
Recommend **exclude or heavily down-weight** in quantitative agent aggregates
(consistent with the pre-existing `eval_suitability: unusable`).
