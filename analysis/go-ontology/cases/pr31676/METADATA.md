---
repo: geneontology/go-ontology
issue_number: 31670
pr_number: 31676
issue_title: "Taxon constraint: please add for GO:0070478 and similar terms"
issue_labels:
  - taxon constraints
issue_created_at: "2026-03-05"
issue_closed_at: "2026-03-05"
pr_author: pgaudet
pr_merged_at: "2026-04-20"
pr_num_commits: 10
files_changed:
  - path: src/taxon_constraints/only_in_taxon.tsv
    additions: 4
    deletions: 1
scoping: mostly_scoped
scoping_notes: >-
  Primary goal was adding taxon constraints for specific terms. Also fixed a formatting
  error in the migrasome entry (extra NCBITaxon column) which was incidental cleanup.
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: multiple_rounds
domain_area: biological_process
tags:
  - taxon-constraint
  - eukaryota
  - bacteria
  - only_in_taxon
  - mRNA-catabolism
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: Multi-round review with 3 formal reviews and 10 commits, demonstrating iterative refinement of taxon scope decisions
---

## Context

A request was made to add "only_in_taxon" constraints for GO:0070478 and related terms. Taxon constraints restrict which organisms a GO term can be applied to (e.g., "maternal mRNA clearance" only makes sense in Eukaryota). The issue was closed quickly but the PR took 6 weeks to merge due to iterative review.

## Changes Made

In `src/taxon_constraints/only_in_taxon.tsv`:

**Added taxon constraints** (Eukaryota-only):
- GO:0141065 "maternal mRNA clearance" -> NCBITaxon:2759 (Eukaryota)
- GO:0000958 "mitochondrial mRNA catabolic process" -> NCBITaxon:2759 (Eukaryota)
- GO:0000956 "nuclear-transcribed mRNA catabolic process" -> NCBITaxon:2759 (Eukaryota)

**Fixed formatting**:
- GO:0140494 "migrasome": corrected malformed entry that had an extra NCBITaxon:7742 column

## Resolution

The PR went through 3 rounds of formal review over 10 commits. Key discussion points:
1. Whether "mitochondrial mRNA catabolic process" should be Eukaryota-only (bacteria have different mRNA degradation machinery but the term specifically refers to mitochondrial context)
2. Whether to add constraints to parent terms or only leaf terms
3. Formatting of the TSV entries (evidence column with PMIDs)

Hard difficulty because taxon constraint decisions require biological reasoning about which organisms possess the relevant cellular machinery, and reviewers disagreed on scope.
