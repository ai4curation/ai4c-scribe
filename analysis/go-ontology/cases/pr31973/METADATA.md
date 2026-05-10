---
repo: geneontology/go-ontology
issue_number: 31877
pr_number: 31973
issue_title: "Obsoletion request: GO:0010381 peroxisome-chloroplast membrane tethering and NEW TERM peroxisome-chloroplast membrane tether activity"
issue_created_at: "2026-04-10"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-27"
pr_num_commits: 5
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 6
    deletions: 4
  - path: src/ontology/imports/go_taxon_constraints.owl
    additions: 481
    deletions: 558
  - path: src/taxon_constraints/never_in_taxon.ofn
    additions: 0
    deletions: 20
  - path: src/taxon_constraints/never_in_taxon.tsv
    additions: 0
    deletions: 4
scoping: mostly_scoped
scoping_notes: >-
  Primary change was obsoletion of GO:0010381 but the PR also touched taxon constraint
  files due to cascading effects of the obsoletion on constraint imports.
task_type: obsoletion
difficulty: hard
scope: single_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - obsoletion
  - MF_in_BP
  - membrane-tethering
  - peroxisome
  - chloroplast
  - taxon-constraint-cleanup
  - multi-file
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Multi-file obsoletion requiring taxon constraint cascade cleanup across OWL and TSV files, with 5 commits showing iterative resolution
---

## Context

Issue #31877 requested both obsoletion of GO:0010381 "peroxisome-chloroplast membrane tethering" (BP) and creation of a replacement MF term. The new term GO:7770065 was added in PR #31929. This PR handles the obsoletion and the resulting cleanup cascade: when a term with taxon constraints is obsoleted, those constraints must be removed from multiple files.

## Changes Made

Four files were modified across 5 commits:
1. `src/ontology/go-edit.obo`: Obsoleted GO:0010381 with standard obsoletion metadata
2. `src/ontology/imports/go_taxon_constraints.owl`: Large OWL file regenerated (-558/+481 lines) reflecting removal of constraints on the obsoleted term
3. `src/taxon_constraints/never_in_taxon.ofn`: Removed 20 lines of OWL axioms for constraints on GO:0010381
4. `src/taxon_constraints/never_in_taxon.tsv`: Removed 4 TSV rows for the term's taxon constraints

## Resolution

The 5 commits show iterative resolution of CI failures: the initial obsoletion passed validation but the taxon constraint files needed manual cleanup to remove references to the now-obsolete term. This case demonstrates that GO obsoletion is not always a single-file operation -- terms with taxon constraints require coordinated changes across the constraint pipeline.
