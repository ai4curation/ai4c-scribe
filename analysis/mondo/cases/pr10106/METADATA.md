---
repo: monarch-initiative/mondo
issue_number: 9798
pr_number: 10106
issue_title: "[Obsolete] glass-chapman-hockley syndrome"
issue_created_at: "2025-11-28"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 15
    deletions: 20
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Term merge based on cross-database evidence that two terms represent the same craniosynostosis syndrome, requiring clinical judgment.
---

## Context

Issue #9798 proposed obsoleting MONDO:0023243 (Glass-Chapman-Hockley syndrome) because the matching SNOMED CT concept was retired and Orphanet evidence suggested equivalence with Muenke syndrome (MONDO:0011274). Both conditions involve FGFR3 mutations causing craniosynostosis, and the curator determined they represent the same disease entity.

## Changes Made

The PR merged MONDO:0023243 into MONDO:0011274 (Muenke syndrome) in a single commit. The 15 additions transfer metadata from the obsoleted term (synonyms including "Glass-Chapman-Hockley syndrome", cross-references, replaced_by annotation) to the Muenke syndrome entry. The 20 deletions remove the source term's active axioms and classification. The net reduction reflects that the obsoleted term's stanza shrinks more than the target grows, as some annotations were redundant.

## Resolution

Moderate difficulty because the merge decision required evaluating evidence from multiple sources (SNOMED CT retirement, Orphanet mapping, UMLS data) to confirm equivalence. Once the merge decision is made, the mechanical execution follows standard Mondo merge SOP. An agent would need access to external database lookups to validate such merge proposals.
