---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3591
pr_number: 3595
issue_title: '"carotid body" should not be part of the cardiovascular system'
pr_author: cmungall
pr_merged_at: '2025-09-15'
task_type: reclassification
difficulty: hard
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 0
generated_at: '2026-05-17'
domain_area: neuroanatomy
---

# PR #3595 — "carotid body" should not be part of the cardiovascular system

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3591](https://github.com/obophenotype/uberon/issues/3591) | [PR #3595](https://github.com/obophenotype/uberon/pull/3595) | @cmungall | merged 2025-09-15

`reclassification` `hard` `tightly_scoped` `approved_first_time`

## Context

The carotid body was incorrectly classified as part of the cardiovascular system in Uberon. While the carotid body is located near the carotid artery bifurcation, it is functionally a peripheral chemoreceptor organ belonging to the peripheral nervous system. The issue cited PMID:32965908 supporting reclassification.

## Changes Made

Corrected the classification of the carotid body by updating its is_a parent and system membership relationships. Removed the cardiovascular system association and added peripheral nervous system membership. The definition was also updated to emphasize its sensory organ role.

## Resolution

Hard difficulty because the carotid body's anatomical location (near the carotid artery) makes it easy to misclassify as cardiovascular. An agent must understand the distinction between spatial proximity and functional system membership, and know that the carotid body is a chemoreceptor, not a vascular structure. This requires genuine anatomical domain expertise.
