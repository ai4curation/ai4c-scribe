---
repo: geneontology/go-ontology
issue_number: 31051
pr_number: 32037
issue_title: "Taxon constraint: GO:0046544 development of secondary male sexual characteristics"
issue_created_at: "2025-11-11"
pr_author: dragon-ai-agent
pr_merged_at: "2026-05-06"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 8
    deletions: 5
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - naming-convention
  - metazoa
  - taxon-constraint
  - synonym
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Straightforward naming convention change following established precedent, good example of follow-up PR after initial implementation
---

## Context

Issue #31051 requested taxon constraints for GO:0046544 (development of secondary male sexual characteristics). After the initial implementation in PR #32027 used a "sensu Metazoa" suffix, a reviewer pointed out that the GO naming convention uses an "animal" prefix (following precedent from GO:0048513 "animal organ development"). This follow-up PR switches from the suffix to the prefix style.

## Changes Made

In `src/ontology/go-edit.obo`, three terms were renamed:
- GO:0045136: "development of secondary sexual characteristics, sensu Metazoa" became "development of animal secondary sexual characteristics"
- GO:0046543: "development of secondary female sexual characteristics, sensu Metazoa" became "development of animal secondary female sexual characteristics"
- GO:0046544: "development of secondary male sexual characteristics, sensu Metazoa" became "development of animal secondary male sexual characteristics"

The previous labels were retained as EXACT synonyms to preserve backward compatibility.

## Resolution

This was a clean follow-up PR that applied a straightforward naming convention fix. No further review was required because the change simply implemented the reviewer's directive from the prior PR. The taxon constraint and softened definitions from PR #32027 were left unchanged.
