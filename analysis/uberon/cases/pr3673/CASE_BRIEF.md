---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3672
pr_number: 3673
issue_title: add 'addedByHRA' subset tag
pr_author: nicolevasilevsky
pr_merged_at: '2026-03-19'
task_type: other
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 4
generated_at: '2026-05-15'
domain_area: metadata
best_f1: 1.0
best_model: gemma-4-31b
---

# PR #3673 — add 'addedByHRA' subset tag

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3672](https://github.com/obophenotype/uberon/issues/3672) | [PR #3673](https://github.com/obophenotype/uberon/pull/3673) | @nicolevasilevsky | merged 2026-03-19

`other` `simple` `tightly_scoped` `approved_first_time`

## Context

The Human Reference Atlas (HRA) project needed a new subset tag "added_by_HRA" to track which terms in Uberon were contributed by HRA. This requires adding a subsetdef declaration to the OBO file header.

## Changes Made

A single line was added to the ontology header in uberon-edit.obo declaring the new subset "added_by_HRA" with a description. This is a minimal change that only modifies the file header, not any term stanzas.

## Resolution

Simple metadata addition. An agent would need to know where subset declarations go in OBO format (in the header section) and follow the existing subsetdef pattern. Approved on first review.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 87628d1c8..f7788e570 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -1,4 +1,5 @@
 format-version: 1.2
+subsetdef: added_by_HRA "Classes tagged with this subset property were added on request from HuBMAP to support the HuBMAP Human Reference Atlas (HRA)."
 subsetdef: added_for_HCA "Classes tagged with this subset property were added upon request from the Human Cell Atlas (HCA)."
 subsetdef: common_anatomy "Terms applicable across life, not restricted to Metazoa"
 subsetdef: cumbo "CUMBO"

```

## Agent Attempts (4)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gemma-4-31b | opencode | 1.000 | 1.000 | 1.000 | `6298fc1` | [#125](https://github.com/ai4curation/eval-ont-agent-uberon/pull/125) | [attempt](attempts/pr125.md) |
| 2 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `6490409` | [#315](https://github.com/ai4curation/eval-ont-agent-uberon/pull/315) | [attempt](attempts/pr315.md) |
| 3 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `1994ec1` | [#281](https://github.com/ai4curation/eval-ont-agent-uberon/pull/281) | [attempt](attempts/pr281.md) |
| 4 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `1994ec1` | [#183](https://github.com/ai4curation/eval-ont-agent-uberon/pull/183) | [attempt](attempts/pr183.md) |
