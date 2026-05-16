---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9795
pr_number: 10109
issue_title: '[Obsolete] OMIM merges'
pr_author: MeeSiing
pr_merged_at: '2026-04-02'
task_type: obsoletion
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 0
generated_at: '2026-05-15'
---

# PR #10109 — [Obsolete] OMIM merges

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9795](https://github.com/monarch-initiative/mondo/issues/9795) | [PR #10109](https://github.com/monarch-initiative/mondo/pull/10109) | @MeeSiing | merged 2026-04-02

`obsoletion` `medium` `tightly_scoped` `changes_requested`

## Context

Issue #9795 identified several OMIM entries that had been merged upstream and needed corresponding merges in Mondo. This PR specifically merged "Charcot-Marie-Tooth peroneal muscular atrophy and Friedreich ataxia, combined" into MONDO:0010549, following OMIM:214380's merge into OMIM:302800. The conditions share overlapping neuropathy features but were historically maintained as separate entries.

## Changes Made

The PR required 2 commits: the initial merge operation and a subsequent QC fix. The merge obsoleted one term and transferred its metadata (synonyms, xrefs, definitions) to MONDO:0010549. The 20 additions and 21 deletions reflect the standard merge pattern: adding replaced_by annotations, transferring cross-references, and removing the obsoleted term's active axioms. The QC failure in the first commit likely involved a missing annotation or invalid axiom pattern that automated checks caught.

## Resolution

Moderate difficulty because neurology term merges require understanding whether two clinical presentations truly represent the same underlying disease entity. The OMIM merge provides strong evidence, but the curator must still correctly execute the merge procedure and handle any QC issues that arise from combining annotation sets from different provenance sources.
