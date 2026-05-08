---
repo: geneontology/go-ontology
issue_number: 31295
pr_number: 32040
issue_title: "NTR: p24 cargo receptor complex"
issue_created_at: "2026-01-07"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-06"
pr_num_commits: 2
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 15
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Cellular component NTR for a well-characterized protein complex needed for GO-CAM modeling, with a 4-month lag from issue to PR
---

## Context

A new term request was filed for `p24 cargo receptor complex` (GO:7770070), a cellular component term needed for GO-CAM annotation of vesicle-mediated transport pathways. The p24 family forms hetero-oligomeric complexes that cycle between the ER and Golgi, selectively recruiting GPI-anchored proteins and other secretory cargo into COPII vesicles. The issue was tagged "Needed for GO-CAM" and "vesicle-mediated-transport", indicating it was blocking functional annotation work.

## Changes Made

The PR added GO:7770070 as a child of `GO:0062137 cargo receptor complex`. The definition describes the hetero-oligomeric (typically tetrameric) nature of the complex, its cycling between ER and Golgi, and its role in selectively recruiting GPI-anchored proteins into COPII vesicles. The term required two commits, suggesting a minor revision was needed after the initial submission.

## Resolution

Despite the issue being open since January 2026, the PR was created and merged in May, reflecting the backlog of new term requests. The 2-commit history suggests a small correction was needed. Medium difficulty because the definition needed to accurately capture the composition and functional role of p24 complexes in vesicular transport, and the parent term placement under `cargo receptor complex` rather than a more specific transport complex class required domain knowledge.
