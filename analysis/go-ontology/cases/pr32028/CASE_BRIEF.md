---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31114
pr_number: 32028
issue_title: 'NTR: Terreic acid biosynthetic process'
pr_author: dragon-ai-agent
pr_merged_at: '2026-05-05'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: changes_requested
num_agent_attempts: 9
generated_at: '2026-05-15'
domain_area: biological_process
best_f1: 0.0
best_model: gpt-5.5
---

# PR #32028 — NTR: Terreic acid biosynthetic process

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31114](https://github.com/geneontology/go-ontology/issues/31114) | [PR #32028](https://github.com/geneontology/go-ontology/pull/32028) | @dragon-ai-agent | merged 2026-05-05

`axiom_repair` `simple` `tightly_scoped` `changes_requested`

## Context

Issue #31114 originally requested new terms for terreic acid biosynthetic processes. During implementation, it was noticed that three terms had `created_by: PomBase:vw` instead of the expected GO convention. This PR attempted to fix them by changing to `GOC:vw`.

## Changes Made

In `src/ontology/go-edit.obo`, the `created_by` field on three terms was changed from `PomBase:vw` to `GOC:vw`:
- GO:0180067 (terreate biosynthetic process)
- GO:0180068 (negative regulation of terreate biosynthetic process)
- One additional related term

## Resolution

While the PR was merged, @pgaudet subsequently clarified that the correct format uses bare initials (`vw`) without any prefix. This prompted a follow-up PR (#32032) to make the final correction. This case demonstrates the importance of verifying metadata conventions with experienced curators rather than guessing at the pattern.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1b7244e11..eaa8ef407 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -483087,7 +483087,7 @@ is_a: GO:0009058 ! biosynthetic process
 intersection_of: GO:0009058 ! biosynthetic process
 intersection_of: has_primary_output CHEBI:233617 ! terreate
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T10:27:33Z
 
 [Term]
@@ -483097,7 +483097,7 @@ namespace: biological_process
 def: "Any process that  that stops, prevents, or reduces the frequency, rate or extent of carbohydrate utilization." [GOC:vw]
 is_a: GO:0043610 ! regulation of carbohydrate utilization
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31261" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-01-19T11:52:03Z
 
 [Term]
@@ -483109,7 +483109,7 @@ is_a: GO:0009889 ! regulation of biosynthetic process
 intersection_of: GO:0065007 ! biological regulation
 intersection_of: positively_regulates GO:0180067 ! terreate biosynthetic process
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31114" xsd:anyURI
-created_by: PomBase:vw
+created_by: GOC:vw
 creation_date: 2026-02-23T15:24:17Z
 
 [Term]

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | [#543](https://github.com/ai4curation/eval-ont-agent-go/pull/543) | [attempt](attempts/pr543.md) |
| 2 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | [#452](https://github.com/ai4curation/eval-ont-agent-go/pull/452) | [attempt](attempts/pr452.md) |
| 3 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | [#451](https://github.com/ai4curation/eval-ont-agent-go/pull/451) | [attempt](attempts/pr451.md) |
| 4 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | [#441](https://github.com/ai4curation/eval-ont-agent-go/pull/441) | [attempt](attempts/pr441.md) |
| 5 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#411](https://github.com/ai4curation/eval-ont-agent-go/pull/411) | [attempt](attempts/pr411.md) |
| 6 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | [#375](https://github.com/ai4curation/eval-ont-agent-go/pull/375) | [attempt](attempts/pr375.md) |
| 7 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | [#336](https://github.com/ai4curation/eval-ont-agent-go/pull/336) | [attempt](attempts/pr336.md) |
| 8 | kimi-k2.6 | opencode | 0.000 | 0.000 | 0.000 | [#267](https://github.com/ai4curation/eval-ont-agent-go/pull/267) | [attempt](attempts/pr267.md) |
| 9 | gemma-4-31b | opencode | 0.000 | 0.000 | 0.000 | [#242](https://github.com/ai4curation/eval-ont-agent-go/pull/242) | [attempt](attempts/pr242.md) |
