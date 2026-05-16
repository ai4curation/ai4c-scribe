---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9795
pr_number: 10108
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

# PR #10108 — [Obsolete] OMIM merges

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9795](https://github.com/monarch-initiative/mondo/issues/9795) | [PR #10108](https://github.com/monarch-initiative/mondo/pull/10108) | @MeeSiing | merged 2026-04-02

`obsoletion` `medium` `tightly_scoped` `changes_requested`

## Context

Issue #9795 listed multiple OMIM merges needed in Mondo. This PR merged "hereditary sensory and autonomic neuropathy type 1B" into MONDO:0044720 (cerebellar ataxia with neuropathy and bilateral vestibular areflexia syndrome). The merge followed OMIM:615490's incorporation into OMIM:614455, reflecting updated understanding that these represent the same SPTLC1-associated condition.

## Changes Made

The PR required 4 commits across multiple contributors. The first commit performed the initial merge. The second added a definition to the surviving term MONDO:0044720, which previously lacked one. The third commit recovered annotations that were accidentally lost during merging. The fourth was a merge with master by a reviewer. The 36 additions and 44 deletions reflect substantial metadata consolidation between two richly annotated neurology terms.

## Resolution

Moderate difficulty due to the iterative nature of the merge. When merging terms with complementary metadata (one has a good definition, the other has good xrefs), the curator must carefully combine both without losing information. The multiple commits show that this process benefits from review, as missing annotations were caught and restored in a follow-up commit.
