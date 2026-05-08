---
repo: monarch-initiative/mondo
issue_number: 9493
pr_number: 9726
issue_title: "Add parent term to MONDO:0005709 common cold"
issue_labels:
  - user request
  - everycure
  - ai-curation
  - ai-success
  - ai-needed-some-guidance
issue_created_at: "2025-08-22"
pr_author: dragon-ai-agent
pr_merged_at: "2025-12-01"
pr_num_commits: 2
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 2
    deletions: 0
scoping: tightly_scoped
scoping_notes: Adds a single is_a parent axiom to an existing term.
task_type: reclassification
difficulty: simple
scope: single_term
review_outcome: changes_requested
domain_area: infectious-disease
tags:
  - reclassification
  - ai-agent
  - common-cold
  - viral-infection
  - respiratory
  - dragon-ai
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: AI agent-authored PR demonstrating automated ontology curation with human guidance for a simple reclassification
---

## Context

An issue was filed requesting that "common cold" (MONDO:0005709) be given "viral respiratory tract infection" (MONDO:0024352) as a parent term. The common cold was missing this classification, which is important for grouping viral respiratory infections. The issue was addressed by the dragon-ai-agent, an automated curation system, making this one of the first AI-authored PRs in Mondo.

The AI agent analyzed multiple options from its issue analysis and selected the appropriate parent term addition. The issue labels indicate the AI succeeded but needed some human guidance during the process.

## Changes Made

Added 2 lines to `src/ontology/mondo-edit.obo`: an is_a relationship making "common cold" a subclass of "viral respiratory tract infection" and a source attribution annotation. This is a minimal but important classification fix that connects common cold to the broader respiratory infection hierarchy.

## Resolution

Easy difficulty for the ontology change itself (adding one parent axiom), but notable as an AI agent-authored PR. The main challenge was selecting the correct option from multiple possibilities discussed in the issue. An agent needs to understand disease classification well enough to determine that common cold should be classified as a viral respiratory tract infection rather than alternative groupings.
