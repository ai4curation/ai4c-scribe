---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31948
pr_number: 31994
issue_title: 'Obsoletion request: glycoprotein cargo receptor activity'
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-28'
task_type: obsoletion
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 7
generated_at: '2026-05-15'
domain_area: molecular_function
best_f1: 0.9
best_model: claude-sonnet-4.5
---

# PR #31994 — Obsoletion request: glycoprotein cargo receptor activity

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31948](https://github.com/geneontology/go-ontology/issues/31948) | [PR #31994](https://github.com/geneontology/go-ontology/pull/31994) | @dragon-ai-agent | merged 2026-04-28

`obsoletion` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #31948 flagged GO:7770028 "glycoprotein cargo receptor activity" for obsoletion. The term was added in error because most vesicle cargo proteins are glycoproteins, making "glycoprotein cargo receptor" an uninformative specialization of "cargo receptor activity" (GO:0038024). Classifying cargo receptors by whether their substrate happens to be glycosylated introduces an unhelpful and non-orthogonal axis of classification.

## Changes Made

In `src/ontology/go-edit.obo`, GO:7770028 was obsoleted:
- Marked `is_obsolete: true`
- Added `replaced_by: GO:0038024` (cargo receptor activity)
- Removed logical axioms
- Obsoletion reason documented in the comment field

## Resolution

Merged directly. The ontological argument was clear: the glycoprotein distinction does not represent a meaningful functional difference in receptor mechanism. This is a good example of quality control catching a term that, while technically valid biologically, creates a misleading classification axis.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1855cac26..f53920e0d 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -616908,12 +616908,13 @@ created_by: dragon-ai-agent
 
 [Term]
 id: GO:7770028
-name: glycoprotein cargo receptor activity
+name: obsolete glycoprotein cargo receptor activity
 namespace: molecular_function
-def: "Binding specifically to a glycoprotein (cargo) to deliver it to a transport vesicle. Glycoprotein cargo receptors span membranes, binding simultaneously to cargo molecules and coat adaptors, to efficiently recruit the cargo molecules to nascent vesicles." [PMID:41203586]
-is_a: GO:0038024 ! cargo receptor activity
-property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31038" xsd:anyURI
-created_by: dragon-ai-agent
+def: "OBSOLETE. Binding specifically to a glycoprotein (cargo) to deliver it to a transport vesicle. Glycoprotein cargo receptors span membranes, binding simultaneously to cargo molecules and coat adaptors, to efficiently recruit the cargo molecules to nascent vesicles." [PMID:41203586]
+comment: The reason for obsoletion is that this term was added in error. Most vesicle cargo are glycoproteins, so classifying cargo receptors by glycoprotein substrate introduces an additional, unhelpful axis of classification. Cargo receptor activities should instead be organized by transport domain (i.e., the vesicles they connect cargo to), with substrates captured via has_input.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31948" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0038024
 
 [Term]
 id: GO:7770029

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.900 | 0.900 | 0.900 | [#462](https://github.com/ai4curation/eval-ont-agent-go/pull/462) | [attempt](attempts/pr462.md) |
| 2 | claude-opus-4.7 | claude | 0.900 | 0.900 | 0.900 | [#341](https://github.com/ai4curation/eval-ont-agent-go/pull/341) | [attempt](attempts/pr341.md) |
| 3 | gemma-4-31b | opencode | 0.900 | 0.900 | 0.900 | [#237](https://github.com/ai4curation/eval-ont-agent-go/pull/237) | [attempt](attempts/pr237.md) |
| 4 | gpt-5.5 | codex | 0.842 | 0.800 | 0.889 | [#542](https://github.com/ai4curation/eval-ont-agent-go/pull/542) | [attempt](attempts/pr542.md) |
| 5 | claude-sonnet-4.5 | copilot | 0.842 | 0.800 | 0.889 | [#390](https://github.com/ai4curation/eval-ont-agent-go/pull/390) | [attempt](attempts/pr390.md) |
| 6 | kimi-k2.6 | opencode | 0.842 | 0.800 | 0.889 | [#270](https://github.com/ai4curation/eval-ont-agent-go/pull/270) | [attempt](attempts/pr270.md) |
| 7 | claude-haiku-4.5 | claude | 0.800 | 0.800 | 0.800 | [#405](https://github.com/ai4curation/eval-ont-agent-go/pull/405) | [attempt](attempts/pr405.md) |
