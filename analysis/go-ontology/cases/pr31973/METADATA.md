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
case_quality: poor
case_quality_reason: gold_pr_self_contradicting_generated_artifact_noise
companion_prs: [31929]
scoring_caveat: >-
  The metadiff gold (#31973) is dominated by ~1000 lines of churn in
  src/ontology/imports/go_taxon_constraints.owl (+481/-558) and
  src/taxon_constraints/never_in_taxon.ofn (-20) that are AUTO-GENERATED
  post-processing artifacts. The responsible curator (raymond91125) explicitly
  instructed the human author NOT to commit these ("Other files are regenerated
  based on src/taxon_constraints/never_in_taxon.tsv by post-processing"); the
  author reverted them in commit 113327b7c but a later regenerate commit
  (e1cd54e5c) re-introduced them, so the merged PR contradicts the curator's
  own instruction. Additionally the OWL churn is overwhelmingly blank-node
  genidNNNN renumbering noise, not semantic content. F1 therefore measures
  reproduction of generated-file noise, not curation quality: agents that made
  the clean, curator-blessed edit (obsolete GO:0010381 in go-edit.obo with
  `consider: GO:7770065` + remove the 4 GO:0010381 rows from never_in_taxon.tsv
  ONLY) score F1~0.016-0.553 despite being substantively correct or better
  than the gold. Judge attempts against the issue + curator comments
  (consider: not replaced_by for cross-aspect BP->MF per pgaudet; .tsv-only TC
  removal per raymond91125), NOT against the metadiff.
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
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

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7, 2026-05-15.** This is a poor evaluation
case: the metadiff gold (#31973) is self-contradicting and dominated by
auto-generated artifact noise. Reviewing the issue thread (#31877) and PR
commit history establishes the following.

### The issue's actual asks and curator-blessed solution

1. The issue requested obsoletion of `GO:0010381` (BP) because it represents
   a molecular function, with reannotation to the new MF term `GO:7770065`
   (added separately in companion **PR #31929**, which is *not* in scope for
   this eval — agents were only asked to obsolete).
2. `raymond91125` triggered the obsoletion; `tberardini` (TAIR, the sole
   annotator) approved proceeding and asked the ticket stay open until she
   migrates the one EXP annotation.
3. **`consider:` is correct, `replaced_by:` is wrong.** The author first used
   `consider: GO:7770065` (cross-aspect BP→MF needs manual review, not
   automatic replacement). `pgaudet` confirmed in-thread: *"I dont think we
   want to `replace` terms across ontology aspects."* The merged gold's
   `go-edit.obo` final state uses `consider: GO:7770065`.
4. **TC cleanup is `.tsv`-only.** `raymond91125` explicitly instructed:
   *"please reverse the changes for taxon restrictions on files other than
   src/taxon_constraints/never_in_taxon.tsv. Other files are regenerated based
   on src/taxon_constraints/never_in_taxon.tsv by post-processing."* The only
   hand edit that should be in the PR is removing the 4 `GO:0010381` rows from
   `never_in_taxon.tsv` (Choanoflagellida, Metazoa, Fungi, Amoebozoa).

### Why the gold PR is a poor reference

The 5 commits are: (1) obsolete in go-edit.obo, (2) remove 4 `.tsv` rows,
(3) **`113327b7c` Revert post-processed taxon constraint files** (complying
with raymond91125), (4) merge master, (5) **`e1cd54e5c` Regenerate taxon
constraint OWL files** — which re-introduced exactly the `.ofn` (-20) and
`go_taxon_constraints.owl` (+481/-558) churn that commit 3 had reverted and
the curator had said must not be in the PR. The merged net diff therefore
contradicts the curator's own instruction, and its ~1000-line OWL delta is
overwhelmingly blank-node `genidNNNN` renumbering noise with no semantic
content (a single class removal shifts every downstream blank-node ID).

Consequently the metadiff F1 measures reproduction of generated-file noise,
not curation quality. Attempts that produced the clean, curator-blessed edit
score F1≈0.016 (go-edit.obo only) or F1≈0.553 (go-edit.obo + full TC
regeneration, which the curator explicitly rejected). All ten attempts should
be judged against the issue + curator comments, not the metadiff.
