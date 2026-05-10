---
repo: geneontology/go-ontology
issue_number: 31863
pr_number: 32012
issue_title: "NTR: MF vesicle membrane tethering activity"
issue_created_at: "2026-04-10"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-29"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 40
    deletions: 30
scoping: tightly_scoped
task_type: obsoletion
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - obsoletion
  - MF_in_BP
  - vesicle-tethering
  - complex-rewiring
  - multi-term
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Complex multi-term obsoletion with relationship rewiring, demonstrating how namespace corrections cascade through the ontology graph
---

## Context

Issue #31863 requested a new MF term for vesicle membrane tethering activity, which was added in PR #31895 as GO:7770062. This follow-up PR completes the namespace correction by obsoleting 5 biological_process terms that described vesicle tethering activities and rewiring their associated protein complexes to point at the new MF term.

## Changes Made

In `src/ontology/go-edit.obo` (net +10 lines from 40 additions / 30 deletions):
- Obsoleted 5 vesicle-tethering BP terms that represented molecular functions
- Rewired protein complex terms that previously had `part_of` relationships to the obsoleted BP terms, pointing them instead to the new MF term GO:7770062
- Added appropriate `replaced_by` and `consider` tags for annotation migration guidance
- Updated relationship axioms on complex terms to maintain graph connectivity

## Resolution

Merged directly despite the complexity. This was a well-planned cascade from the new term addition in PR #31895, with clear obsoletion rationale (MF_in_BP correction) and explicit curator approval in the issue discussion. The 40-line addition reflects both obsoletion metadata and the relationship rewiring needed to maintain ontology coherence.
