---
repo: geneontology/go-ontology
issue_number: 30894
pr_number: 32011
issue_title: "NTR: [Ferritin-specific autophagy]"
issue_labels:
  - New term request
  - pending_closure
issue_created_at: "2025-10-07"
issue_closed_at: "2026-04-29"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-29"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 11
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds exactly one new term stanza with no unrelated changes.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - autophagy
  - selective-autophagy
  - ferritin
  - NCOA4
  - PMID:25327288
  - PMID:26436293
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: New term requiring correct hierarchy placement and literature-backed definition using genus-differentia pattern
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

A new term request (NTR) was filed for "ferritinophagy" — the selective degradation of ferritin via macroautophagy to release iron. This is a well-characterized selective autophagy pathway (PMID:25327288, PMID:26436293) mediated by NCOA4 as the cargo receptor. The issue was open for ~6 months before resolution.

## Changes Made

Added new term GO:7770069 to `src/ontology/go-edit.obo`:

- **ID**: GO:7770069
- **Name**: ferritinophagy
- **Definition**: "The selective degradation of ferritin to release iron by macroautophagy." [PMID:25327288, PMID:26436293, PMID:38714719]
- **Synonym**: "ferritin-specific autophagy" (EXACT)
- **Parent**: is_a GO:0016236 (macroautophagy)
- **Provenance**: Three PMIDs supporting the term, term_tracker_item linking to issue #30894

## Resolution

The key decisions were:
1. **Hierarchy placement**: Under macroautophagy (GO:0016236) rather than generic autophagy, since ferritinophagy is specifically a macroautophagy process
2. **Definition style**: Genus-differentia pattern — "The selective degradation of [cargo] ... by [mechanism]"
3. **Evidence**: Three supporting publications spanning the discovery and characterization of the pathway

Medium difficulty because it requires knowledge of the selective autophagy hierarchy and the specific mechanism (macroautophagy vs other autophagy types). An agent would need to determine the correct parent by understanding that ferritinophagy operates via the macroautophagy machinery.
