---
repo: monarch-initiative/mondo
issue_number: 9854
pr_number: 10116
issue_title: "Isolated megalencephaly Orphanet Xref"
issue_created_at: "2026-01-02"
pr_author: MeeSiing
pr_merged_at: "2026-04-08"
pr_num_commits: 3
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 11
    deletions: 8
scoping: tightly_scoped
task_type: other
difficulty: medium
scope: single_term
review_outcome: changes_requested
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Cross-reference correction requiring investigation of source annotation provenance when moving xrefs between terms.
---

## Context

Issue #9854 reported that the Orphanet xref for "Isolated megalencephaly" (ORPHANET:2477) was attached to MONDO:0016608 (megalencephaly) but should instead be on MONDO:0017089 (isolated megalencephaly). The distinction between the broader "megalencephaly" and the more specific "isolated megalencephaly" is clinically relevant for mapping to external databases.

## Changes Made

The PR required 3 commits to complete. The first moved the Orphanet xref to the correct term MONDO:0017089. The second removed a MedDRA xref (MedDRA:10050183) that was also incorrectly placed on isolated megalencephaly. The third commit addressed the source annotation for the MedDRA xref, as the curator was uncertain which source to assign after removing the Orphanet provenance link.

## Resolution

Moderate difficulty because cross-reference corrections require understanding provenance chains. When an xref is moved between terms, associated source annotations may need updating, and other xrefs that depended on the same provenance chain may be affected. The curator's uncertainty about the MedDRA source annotation illustrates a common challenge: maintaining annotation integrity when editing cross-references.
