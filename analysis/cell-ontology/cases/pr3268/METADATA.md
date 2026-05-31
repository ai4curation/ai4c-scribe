---
repo: obophenotype/cell-ontology
issue_number: 3267
pr_number: 3268
issue_title: "Update claude.md instructions for GitHub Copilot"
issue_created_at: "2025-08-27"
issue_closed_at: "2025-10-29"
pr_author: Caroline-99
pr_merged_at: "2025-10-29"
pr_num_commits: 2
files_changed:
  - path: CLAUDE.md
    additions: 3
    deletions: 3
  - path: src/sparql/illegal-annotation-property-violation.sparql
    additions: 1
    deletions: 0
scoping: mostly_scoped
scoping_notes: >-
  Primary change is CLAUDE.md update, with a minor incidental SPARQL file addition.
task_type: documentation
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: infrastructure
tags:
  - documentation
  - CLAUDE-md
  - agent-instructions
  - GitHub-Copilot
  - dc-creator
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Documentation update for AI agent instructions, demonstrating how ontology repos configure agent behavior
case_quality: good
case_quality_reason: single_complete_documentation_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

The cell ontology repository uses a CLAUDE.md file to provide instructions to AI agents (Claude, GitHub Copilot) working on the codebase. The instructions needed updating to specify how GitHub Copilot should add `dc:creator` attribution when making changes, ensuring proper provenance tracking for AI-generated contributions.

## Changes Made

Modified 3 lines in `CLAUDE.md` to update the agent instructions for dc:creator attribution. Also added 1 line to a SPARQL file for detecting illegal annotation property violations. The documentation change is the primary focus.

## Resolution

Approved on first review. Simple difficulty because this is a documentation-only change, but it is an interesting case study for understanding how ontology repositories configure AI agent behavior and maintain contributor attribution standards.
