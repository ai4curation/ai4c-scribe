---
repo: geneontology/go-ontology
issue_number: 31945
pr_number: 32013
issue_title: "Obsoletion request: GO:0003400 regulation of COPII vesicle coating"
issue_created_at: "2026-04-22"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-29"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 13
    deletions: 11
scoping: tightly_scoped
task_type: reclassification
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Combined obsoletion and reclassification affecting three COPII vesicle transport terms, requiring understanding of vesicle coating vs. regulation semantics
---

## Context

GO:0003400 `regulation of COPII vesicle coating` was identified as biologically inappropriate because the proteins annotated to it are actually participants in the COPII vesicle coating process itself, not upstream regulators. The issue also identified that the primary COPII term (GO:0048208) had a misleading name and that GO:0006901 needed a label update.

## Changes Made

Three terms were modified in `go-edit.obo`: GO:0003400 was obsoleted with `replaced_by GO:0048208`, since annotated proteins are part of the coating process rather than regulators. GO:0048208 was renamed from `COPII vesicle coating` to `COPII vesicle coat assembly`, promoting the previous exact synonym to the primary label. GO:0006901 also received a label update. The old names were retained as synonyms to preserve searchability.

## Resolution

Medium difficulty because the changes required understanding the biological distinction between regulation of a process and participation in that process. In vesicle biology, COPII coat proteins like Sec23/Sec24 are components of the coating machinery, not regulators of it. The obsoletion of the regulation term and simultaneous renaming of the target term ensured that annotation migration would be semantically correct.
