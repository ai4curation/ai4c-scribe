---
repo: geneontology/go-ontology
issue_number: 31935
pr_number: 31946
issue_title: "Missing parent: GO:0061852 retrograde transporter complex, Golgi to ER (plus term label and definition)"
issue_created_at: "2026-04-21"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-22"
pr_num_commits: 2
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 6
    deletions: 4
scoping: tightly_scoped
task_type: reclassification
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Combined reclassification, rename, and definition update for a vesicle transport complex term requiring understanding of cargo receptor vs. transporter semantics
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

GO:0061852 was originally classified as a transporter complex with the label "retrograde transporter complex, Golgi to ER". ValWood identified that the term should actually be classified under `cargo receptor complex` rather than `transporter complex`, since the KDEL receptor and related proteins function as cargo receptors that recognize ER-retention signals, not as transporters that provide the energy for vesicle movement.

## Changes Made

The PR reclassified GO:0061852 by changing its parent from `GO:1990351 transporter complex` to `GO:0062137 cargo receptor complex`, renamed the primary label to `retrograde cargo receptor complex, Golgi to ER`, and refined the definition from "Transporter complex that recognises" to "Cargo receptor complex that recognizes" ER-retention signals. The two old transporter-based names were demoted to BROAD synonyms, and a new EXACT synonym was added for the specific KDEL receptor complex.

## Resolution

Medium difficulty because the reclassification required understanding the semantic distinction between cargo receptors (which recognize and bind cargo) and transporters (which provide energy for movement). In vesicle-mediated transport, KDEL receptors are cargo receptors that cycle between Golgi and ER to retrieve escaped ER-resident proteins, not transporters in the molecular function sense. The 2-commit history suggests a minor correction was needed after initial review.
