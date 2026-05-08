---
repo: obophenotype/uberon
issue_number: 3604
pr_number: 3607
issue_title: "dGTEx terms needed in Uberon"
issue_labels:
  - new term request
issue_created_at: "2025-08-29"
issue_closed_at: "2025-09-11"
pr_author: dragon-ai-agent
pr_merged_at: "2025-09-11"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 13
    deletions: 0
scoping: mostly_scoped
scoping_notes: >-
  The issue requested multiple dGTEx terms but this PR only addresses the kidney
  interpolar region. Other terms from the same issue were handled in separate PRs.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: renal-anatomy
tags:
  - new-term
  - kidney
  - dGTEx
  - renal
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: NTR from a multi-term request showing how a single term is carved out and addressed independently
---

## Context

The dGTEx (developmental Genotype-Tissue Expression) project needed several anatomical terms added to Uberon. This PR addressed one of those terms: the kidney interpolar region, which is the central portion of the kidney between the upper and lower poles.

## Changes Made

Added UBERON:7770009 "kidney interpolar region" with synonyms ("central pole of kidney", "interpolar region of kidney"), a definition, is_a organ part classification, and part_of kidney relationship. Attribution was included via ORCID for the requesting contributor.

## Resolution

Medium difficulty because the agent must understand renal anatomy well enough to define the interpolar region correctly and place it in the partonomy. The term also needed proper contributor attribution. This was one term from a multi-term request, so the agent needed to scope appropriately.
