---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31114
pr_number: 32032
issue_title: 'NTR: Terreic acid biosynthetic process'
pr_author: dragon-ai-agent
pr_merged_at: '2026-05-05'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 0
generated_at: '2026-05-15'
domain_area: biological_process
---

# PR #32032 — NTR: Terreic acid biosynthetic process

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31114](https://github.com/geneontology/go-ontology/issues/31114) | [PR #32032](https://github.com/geneontology/go-ontology/pull/32032) | @dragon-ai-agent | merged 2026-05-05

`axiom_repair` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #31114 was originally a new term request for "terreic acid biosynthetic process" terms. During that work, it was noticed that three terms (GO:0180067, GO:0180068, and related) had incorrect `created_by` values. After an initial fix in PR #32028 changed "PomBase:vw" to "GOC:vw", a curator clarified that the convention is bare initials ("vw"), not a prefixed form.

## Changes Made

In `src/ontology/go-edit.obo`, the `created_by` field on three terms was corrected from `GOC:vw` to `vw`:
- GO:0180067 (terreate biosynthetic process)
- GO:0180068 (negative regulation of terreate biosynthetic process)
- One additional related term

This was the second correction pass, following the curator's clarification that bare initials are the convention.

## Resolution

Merged directly without review. The fix was trivial and the correct format had been explicitly stated by @pgaudet in the issue discussion. This case illustrates how metadata convention errors can cascade through multiple fix attempts when the convention is not immediately obvious.
