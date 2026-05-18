---
repo: obophenotype/uberon
issue_number: 3637
pr_number: 3638
issue_title: "[NTR] 'uterine fundus'"
issue_labels:
  - new term request
issue_created_at: "2025-12-03"
issue_closed_at: "2025-12-03"
pr_author: dragon-ai-agent
pr_merged_at: "2025-12-03"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 13
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: reproductive-anatomy
tags:
  - new-term
  - uterus
  - reproductive-system
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Standard NTR with definition, synonyms, and partonomy relationships for a well-known anatomical structure
case_quality: ok
case_quality_reason: sound_gold_but_new_term_requires_anatomical_detail_and_exact_synonym_provenance
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

A new term request was filed for "uterine fundus," the superior dome-shaped portion of the uterus. This is a well-established anatomical structure that was missing from Uberon.

## Changes Made

Added UBERON:9900001 for "uterine fundus" with a textual definition, Latin and English synonyms (fundus uteri, fundus of uterus), and appropriate relationships including part_of the uterus. The term follows standard Uberon patterns for anatomical part terms.

## Resolution

Medium difficulty because while the anatomy is well-defined, the agent must correctly place the term in the partonomy, choose the right parent class, provide an adequate definition with references, and add appropriate synonyms including Latin nomenclature. Approved on first review the same day the issue was filed.
