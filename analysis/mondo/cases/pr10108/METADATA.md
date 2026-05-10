---
repo: monarch-initiative/mondo
issue_number: 9795
pr_number: 10108
issue_title: "[Obsolete] OMIM merges"
issue_created_at: "2025-11-26"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 4
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 36
    deletions: 44
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: changes_requested
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Multi-step term merge that required adding a definition and recovering missing annotations, demonstrating the complexity of merging terms with rich metadata.
---

## Context

Issue #9795 listed multiple OMIM merges needed in Mondo. This PR merged "hereditary sensory and autonomic neuropathy type 1B" into MONDO:0044720 (cerebellar ataxia with neuropathy and bilateral vestibular areflexia syndrome). The merge followed OMIM:615490's incorporation into OMIM:614455, reflecting updated understanding that these represent the same SPTLC1-associated condition.

## Changes Made

The PR required 4 commits across multiple contributors. The first commit performed the initial merge. The second added a definition to the surviving term MONDO:0044720, which previously lacked one. The third commit recovered annotations that were accidentally lost during merging. The fourth was a merge with master by a reviewer. The 36 additions and 44 deletions reflect substantial metadata consolidation between two richly annotated neurology terms.

## Resolution

Moderate difficulty due to the iterative nature of the merge. When merging terms with complementary metadata (one has a good definition, the other has good xrefs), the curator must carefully combine both without losing information. The multiple commits show that this process benefits from review, as missing annotations were caught and restored in a follow-up commit.
