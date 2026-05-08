---
repo: geneontology/go-ontology
issue_number: 31964
pr_number: 31982
issue_title: "GO:0052597 diamine oxidase activity terms"
issue_created_at: "2026-04-24"
pr_author: sjm41
pr_merged_at: "2026-04-27"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 3
    deletions: 2
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Precise hierarchy cleanup requiring understanding of EC enzyme classification scope and the distinction between broad vs. exact cross-references
---

## Context

The diamine oxidase activity sub-hierarchy had two issues identified during an enzyme term review: GO:0052598 `histamine oxidase activity` carried a redundant `xref: EC:1.4.3.22 {source="skos:broadMatch"}` that duplicated the broadMatch already present on its parent term GO:0052597, and GO:0004720 `protein-lysine 6-oxidase activity` was incorrectly parented under the diamine oxidase group when it belongs under a different oxidoreductase class.

## Changes Made

Two surgical edits were made in `go-edit.obo`. First, the redundant EC:1.4.3.22 broadMatch was removed from GO:0052598 `histamine oxidase activity`, since EC:1.4.3.22 covers the entire diamine oxidase group and the broadMatch is only appropriate on the parent term (GO:0052597). The RHEA:25625 exactMatch on the child term was retained. Second, GO:0004720 `protein-lysine 6-oxidase activity` was reparented from GO:0052597 to a more appropriate oxidoreductase parent, correcting a misclassification in the hierarchy.

## Resolution

Medium difficulty because the changes required understanding EC enzyme classification scope: EC:1.4.3.22 covers a group of diamine oxidases, so a broadMatch is appropriate on the parent but redundant (and potentially misleading) on a substrate-specific child. The reparenting decision required knowing that lysyl oxidase, despite sharing a copper amine oxidase mechanism, is not a diamine oxidase in the strict sense. The minimal line changes (3 additions, 2 deletions) reflect the surgical precision of the edits.
