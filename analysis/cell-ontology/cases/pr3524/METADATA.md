---
repo: obophenotype/cell-ontology
issue_number: 3523
pr_number: 3524
issue_title: "Revise textual definition of Retinal Ganglion Cell A into Alpha retinal ganglion cell"
issue_created_at: "2025-12-09"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-17"
pr_num_commits: 14
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 4
    deletions: 3
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: neuroscience
tags:
  - definition-update
  - retinal-ganglion-cell
  - rename
  - alpha-RGC
  - mouse
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Rename and definition revision for alpha RGC aligning label with current nomenclature and adding species specificity
case_quality: poor
case_quality_reason: gold_label_renegotiated_in_pr_comments
companion_prs: []
scoring_caveat: "Issue #3523 specifies the label as 'alpha retinal ganglion cell'. The gold PR #3524 was initially built to that exact spec, but curator RiveraAndrea83 then requested 'alpha retinal ganglion cell (Mmus)' in a PR review comment (2025-12-15). The '(Mmus)' suffix is not derivable from the issue the agents received, so metadiff F1 (max ~0.571) systematically under-represents attempt quality. Judge attempts against the issue text, not the renegotiated gold label."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

CL_0004117 was labeled "Retinal Ganglion Cell A" using an older naming convention. Issue #3523 requested renaming it to "alpha retinal ganglion cell (Mmus)" to align with current RGC nomenclature and to make the mouse-specific taxon scope explicit. This is part of the broader RGC refactoring effort (epic #2844) to modernize retinal ganglion cell terminology in CL.

## Changes Made

Updated `cl-edit.owl` with 4 additions and 3 deletions: the primary label was changed from "Retinal Ganglion Cell A" to "alpha retinal ganglion cell (Mmus)", the textual definition was revised to reference the alpha RGC classification and its large soma size and brisk transient responses, and a species-specific qualifier was added.

## Resolution

Approved on first review despite requiring 14 commits to finalize. Simple difficulty because the change is primarily a label and definition text update following the RGC nomenclature standardization pattern established across the series.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16.**

This is a single-PR resolution (search of issue #3523 / "alpha retinal
ganglion cell" returns only #3524 as the resolving PR — no companion PRs),
so it is **not** a multi-PR partial-gold case. However it is a poor
*evaluation* case because the gold label was renegotiated after the agents'
information cut-off:

- Issue #3523 explicitly states `**Revised cell label** alpha retinal
  ganglion cell` and supplies the exact definition text and references.
- The gold PR #3524 was initially built to exactly that spec (label =
  "alpha retinal ganglion cell"). Then on 2025-12-15 curator RiveraAndrea83
  left a PR comment: *"@copilot please change label to: alpha retinal
  ganglion cell (Mmus)"*, and Copilot amended the label in commit 120a536.
- The `(Mmus)` species qualifier therefore appears in the gold diff but is
  **not present anywhere in the issue** the eval agents were given. No agent
  relying only on the issue could produce it.

Consequence: the metadiff F1 ceiling for this case is ~0.571 (gemma-4-31b)
and the two claude attempts land at 0.429, even though **all three attempts
correctly and faithfully implement every change the issue actually
requested**. The residual gap is the renegotiated label, an en-dash vs hyphen
typographic difference in `non[-/–]direction-selective`, synonym casing
("Retinal ganglion cell A" vs gold's lowercased "retinal ganglion cell A"),
and (sonnet only) one unrequested `terms:date` annotation.

Recommendation for downstream scoring: treat metadiff for this case as a
**lower bound**; the substantive outcome for all three attempts is
`success` against the issue as written. Down-weight or exclude this case from
F1-based aggregation, or re-score against the issue spec rather than the
post-comment gold label.
