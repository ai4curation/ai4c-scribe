---
repo: obophenotype/uberon
issue_number: 3627
pr_number: 3628
issue_title: "Fix issue with inferred equivalences for uberon terms for BG"
issue_created_at: "2025-11-12"
issue_closed_at: "2025-11-12"
pr_author: dragon-ai-agent
pr_merged_at: "2025-11-12"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 0
    deletions: 5
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - xref-removal
  - DHBA
  - brain-anatomy
  - inferred-equivalence
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Cross-reference cleanup requiring understanding of how xrefs can cause unintended OWL equivalence inferences
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Specific DHBA (Developing Human Brain Atlas) cross-references on five Uberon brain anatomy terms were causing unintended inferred equivalences, as reported in a downstream ontology project. The xrefs needed to be removed to fix reasoning errors.

## Changes Made

Removed incorrect DHBA xrefs from five brain anatomy terms in uberon-edit.obo. Each removal was a single line deletion (the xref annotation). No other modifications were made to the affected term stanzas.

## Resolution

Medium difficulty because an agent must understand that in OBO/OWL ontologies, cross-references (xrefs) can serve as the basis for automated equivalence mappings. Removing the wrong xref could break legitimate mappings, so the agent needs to verify which specific xrefs are causing the problematic inferences. The fix itself is mechanically simple (delete 5 lines) but requires reasoning about semantic consequences.
