---
repo: geneontology/go-ontology
issue_number: 19185
pr_number: 31911
issue_title: "NTR actin-filament cross-linking activity (replace actin crosslink formation MF in BP ontology)"
issue_created_at: "2020-03-29"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-17"
pr_num_commits: 3
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 17
    deletions: 2
scoping: tightly_scoped
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Long-standing NTR (6 years open) addressing MF-in-BP misclassification, with new term creation and parent term rename in one PR
---

## Context

Issue #19185, open since March 2020, requested a molecular function term for actin-filament cross-linking activity to replace the existing biological process term `actin crosslink formation` which was misclassified as a BP when it actually describes a molecular function. The issue was tagged with multiple labels including "MF_in_BP", "MF refactoring", "Needed for GO-CAM", and "PomBase", indicating its importance across multiple annotation efforts.

## Changes Made

Two changes were made in `go-edit.obo`: a new MF term GO:7770064 `actin-filament cross-linking activity` was added as a child of GO:0008093 `cytoskeletal adaptor activity` with `has_part GO:0051015 actin filament binding`. The definition describes it as an adaptor activity that brings together two actin filaments for bundling or networking. Multiple exact synonyms were added for variant spellings (cross-linking vs. crosslinking). Additionally, GO:0008093 was renamed to better reflect its role as an adaptor activity for cytoskeletal components.

## Resolution

Hard difficulty because this 6-year-old issue required resolving a fundamental ontological misclassification (MF vs. BP), creating a new term with the correct molecular function semantics, and simultaneously renaming the parent term. The 3-commit history suggests iterative refinement. The term needed careful placement: actin cross-linking is an adaptor/scaffolding activity (bringing two filaments together), not a catalytic activity, which informed its classification under cytoskeletal adaptor activity.
