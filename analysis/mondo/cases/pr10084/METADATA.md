---
repo: monarch-initiative/mondo
issue_number: 9849
pr_number: 10084
issue_title: "Request for new term 'reticular pseudodrusen'"
issue_created_at: "2025-12-22"
pr_author: MeeSiing
pr_merged_at: "2026-03-30"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 13
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: New term creation for an ophthalmic condition requiring evidence evaluation and synonym scope decisions based on clinical literature.
---

## Context

Issue #9849 requested a new term for "reticular pseudodrusen" (also known as subretinal drusenoid deposits/SDD/RPD), which are subretinal deposits located internal to the retinal pigment epithelium. The request included exact synonyms and two abbreviations, a definition, and multiple PMIDs as evidence. The curator noted that one suggested PMID (34752962) was incorrect evidence and excluded it.

## Changes Made

The PR created MONDO:1060213 with 13 additions to mondo-edit.obo. The new term includes the label "reticular pseudodrusen", a revised definition based on the provided PMIDs, exact synonyms ("subretinal drusenoid deposits", "SDD", "RPD"), parent classification, and ORCID-attributed evidence annotations. The curator critically evaluated the suggested references and excluded one that did not support the term.

## Resolution

Moderate difficulty because new term creation requires evaluating evidence quality. The curator demonstrated critical assessment by rejecting an inappropriate PMID while accepting others. The synonym scope decisions (abbreviations as EXACT rather than RELATED) and parent term placement both require ophthalmology domain knowledge. An agent would need literature verification capabilities to replicate this evidence evaluation step.
