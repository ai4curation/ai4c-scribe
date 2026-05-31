---
repo: obophenotype/cell-ontology
issue_number: 3163
pr_number: 3545
issue_title: "Add CD14 lacks to human dendritic cell terms"
issue_created_at: "2025-07-02"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-05"
pr_num_commits: 5
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 4
    deletions: 4
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: immunology
tags:
  - lacks-annotation
  - CD14
  - dendritic-cell
  - phenotype
  - surface-marker
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Adding negative marker phenotype annotations to multiple dendritic cell terms using the lacks_plasma_membrane_part pattern
case_quality: ok
case_quality_reason: sound_gold_no_agent_coverage
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
agent_coverage: none
agent_coverage_note: "no eval attempts generated as of 2026-05-16"
---

## Context

Human myeloid and plasmacytoid dendritic cells are characteristically CD14-negative, but this phenotypic information was not captured in CL. Issue #3163 requested adding `lacks_plasma_membrane_part` annotations for CD14 (PR:000001889) to the relevant human dendritic cell terms. Negative marker annotations are important for distinguishing dendritic cells from monocytes, which are CD14-positive.

## Changes Made

Updated `cl-edit.owl` with 4 additions and 4 deletions, adding `lacks_plasma_membrane_part some PR:000001889` (CD14) axioms to the human myeloid dendritic cell and plasmacytoid dendritic cell terms. The deletions reflect replacement of existing axioms with the updated versions that include the negative marker annotation.

## Resolution

Approved on first review in 5 commits. Simple difficulty because the `lacks_plasma_membrane_part` pattern is well-established in CL for representing negative surface marker phenotypes, and the specific CD14-negative status of these dendritic cell types is well-documented immunological knowledge.
