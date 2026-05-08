---
repo: obophenotype/uberon
issue_number: 3617
pr_number: 3619
issue_title: "Parent-child relationship between tracheal mucosa and nasal cavity mucosa"
issue_created_at: "2025-10-28"
issue_closed_at: "2025-11-03"
pr_author: dragon-ai-agent
pr_merged_at: "2025-11-03"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 2
    deletions: 2
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: single_term
review_outcome: multiple_rounds
domain_area: respiratory-anatomy
tags:
  - logical-definition
  - reasoner-error
  - tracheal-mucosa
  - respiratory-system
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Complex axiom repair requiring understanding of how logical definitions drive OWL reasoning and produce unintended inferences
---

## Context

The reasoner was incorrectly inferring that tracheal mucosa was a parent of nasal cavity mucosa due to an overly broad logical definition. The logical definition of tracheal mucosa (UBERON:0000379) used "part_of respiratory airway" which, through the class hierarchy, made nasal cavity mucosa classify as a subclass.

## Changes Made

Modified the logical definition of UBERON:0000379 (tracheal mucosa) to use a more specific anatomical context in the intersection_of axiom. Changed the part_of target from "respiratory airway" to "trachea" (or equivalent specific structure), preventing the incorrect inference chain.

## Resolution

Hard difficulty because this requires understanding OWL reasoning over intersection_of axioms. The agent must trace the inference chain: (1) tracheal mucosa is defined as mucosa that is part_of respiratory airway, (2) nasal cavity is a subclass of respiratory airway, (3) therefore nasal cavity mucosa satisfies the definition. The fix requires choosing a more specific part_of target that excludes nasal structures. The PR went through multiple rounds of review with changes requested.
