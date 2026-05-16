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
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [31677]
scoring_caveat: >-
  Issue #31670 was resolved by TWO human PRs. The gold pr_number #31676 covers only
  the only_in_taxon.tsv additions (GO:0141065, GO:0000958, GO:0000956 -> Eukaryota)
  plus an incidental GO:0140494 migrasome formatting fix. Companion PR #31677
  ("fixes #31670") separately added GO:1990074 polyuridylation-dependent mRNA
  catabolic process -> Bacteria to never_in_taxon.tsv. The metadiff vs #31676 only
  covers the only_in_taxon sub-step; it also penalizes the (build-product) migrasome
  cleanup which no agent could derive from the issue, and gives no credit for the
  never_in_taxon path. Judge attempts against the issue text and the union of
  #31676 + #31677, not the single gold PR.
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
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

## Curation Note (data quality)

**Flagged poor for scoring: gold PR is partial (multi-PR human resolution).**

Issue #31670 (reporter asked for `never_in_taxon: 2` Bacteria on GO:0070478 and
similar NMD terms) was resolved by the curator (@pgaudet) across **two** human PRs:

1. **PR #31676** (the configured `pr_number`, "Add new GO terms for Eukaryota and
   Bacteria"): added `only_in_taxon: NCBITaxon:2759` (Eukaryota) for **GO:0141065**
   maternal mRNA clearance, **GO:0000958** mitochondrial mRNA catabolic process, and
   **GO:0000956** nuclear-transcribed mRNA catabolic process to
   `src/taxon_constraints/only_in_taxon.tsv`, plus an incidental cleanup of a
   malformed **GO:0140494** migrasome row (stray extra `NCBITaxon:7742` column).
2. **PR #31677** ("Add entry for polyuridylation-dependent mRNA catabolism", body
   = "fixes #31670"): separately added **GO:1990074** polyuridylation-dependent
   mRNA catabolic process → Bacteria to `src/taxon_constraints/never_in_taxon.tsv`
   (the human PR also bundled unrelated GO:1901174 / GO:0046905 phytoene rows —
   scope creep in the human PR itself).

Implications for scoring:

- The metadiff compares attempts against **#31676 only**. Best attempts
  (pr263, pr177) reach F1 0.571 with recall 1.000, so the gold is not *entirely*
  partial — but it omits the companion `never_in_taxon` step and penalizes the
  un-derivable migrasome formatting fix.
- The curator chose a **different modeling than the reporter requested**
  (`only_in_taxon: Eukaryota` on parents rather than `never_in_taxon: Bacteria`
  on leaves). Attempts that faithfully implemented the *literal* request via
  `never_in_taxon.tsv` (pr413 Sonnet/copilot, pr199 Haiku) score F1 0.000 against
  the gold despite being biologically correct and instruction-faithful. These are
  defensible alternative resolutions, not failures.
- Several attempts (pr92/pr67/pr64 gpt-5.5; pr328 opus) made the *correct* source
  TSV edit but committed regenerated `only_in_taxon.ofn` / `go_taxon_constraints.owl`
  build products, producing thousands of lines of blank-node renumbering. Their
  near-zero F1 is a derived-file artifact, not a semantic error.

Recommendation: down-weight or exclude this case from aggregate metadiff scoring,
or re-score against the union of #31676 + #31677 and against the issue text. Judge
attempts on whether they (a) constrained the nuclear-transcribed mRNA decay branch
to exclude bacteria via either modeling, and (b) kept the diff minimal (source TSV
only, no regenerated artifacts, no full-file reorder).
