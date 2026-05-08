---
repo: geneontology/go-ontology
issue_number: 31916
pr_number: 32024
issue_title: "Review of Entner-Doudoroff pathways"
issue_created_at: "2026-04-17"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-04"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 37
    deletions: 47
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Batch obsoletion of 5 nested metabolic pathway variants consolidating to a single parent term, requiring understanding of pathway biochemistry
---

## Context

The Entner-Doudoroff pathway in GO had accumulated five overly specific variant terms (e.g., "through 6-phosphogluconate", "through gluconate", "non-phosphorylative") that were nested under the parent GO:0061678 `Entner-Doudoroff pathway`. A review by sjm41 with agreement from raymond91125 and pgaudet concluded that these variants introduced unnecessary granularity and should be consolidated to the single parent term.

## Changes Made

Five terms were obsoleted with `replaced_by` pointing to GO:0061678: GO:0009255 (through 6-phosphogluconate), GO:0061679 (through gluconate), GO:0061680 (non-phosphorylative), and two additional variants. Each obsoletion involved renaming with the "obsolete" prefix, marking definitions as OBSOLETE, removing logical axioms (is_a, part_of relationships), and adding replaced_by references. The net effect simplified the pathway hierarchy from six terms to one.

## Resolution

Medium difficulty because the decision to collapse pathway variants required understanding the biochemical distinctions between different Entner-Doudoroff pathway routes and whether those distinctions were meaningful for annotation. The prior discussion on issue #29539 provided the biological rationale that the variant pathways were not independently annotatable in practice. The large line changes (37 additions, 47 deletions) reflect the systematic obsoletion of five terms.
