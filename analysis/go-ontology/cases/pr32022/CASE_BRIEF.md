---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31873
pr_number: 32022
issue_title: 'Obsoletion request: GO:0061817 endoplasmic reticulum-plasma membrane
  tethering'
pr_author: dragon-ai-agent
pr_merged_at: '2026-05-04'
task_type: obsoletion
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 7
generated_at: '2026-05-15'
domain_area: biological_process
best_f1: 0.909
best_model: gpt-5.5
---

# PR #32022 — Obsoletion request: GO:0061817 endoplasmic reticulum-plasma membrane tethering

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31873](https://github.com/geneontology/go-ontology/issues/31873) | [PR #32022](https://github.com/geneontology/go-ontology/pull/32022) | @dragon-ai-agent | merged 2026-05-04

`obsoletion` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #31873 was part of a broader initiative to correct membrane tethering terms that were incorrectly placed in the biological_process namespace. GO:0061817 "endoplasmic reticulum-plasma membrane tethering" described what is fundamentally a molecular function (binding activity that brings two membranes together) rather than a biological process. This is one of many related obsoletion requests (tagged "MF_in_BP") addressing this systematic error.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0061817 was obsoleted:
- Marked `is_obsolete: true`
- Removed logical axioms and relationships
- Added appropriate `consider` tags pointing curators to the correct MF replacement terms
- The corresponding MF tether activity term already existed from earlier PRs in this series

## Resolution

Merged directly without review. The obsoletion was part of a well-established pattern where biological_process terms describing membrane-membrane tethering activities are being systematically obsoleted and replaced by molecular_function tether activity terms. The clear rationale and established precedent made this straightforward.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index fe2f8414b..1ae42d961 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -371189,12 +371189,14 @@ creation_date: 2016-12-01T20:21:28Z
 
 [Term]
 id: GO:0061817
-name: endoplasmic reticulum-plasma membrane tethering
+name: obsolete endoplasmic reticulum-plasma membrane tethering
 namespace: biological_process
-def: "The attachment of an endoplasmic reticulum membrane to the plasma membrane via molecular tethers." [GOC:dph, GOC:vw, PMID:23237950, PMID:26877082, PMID:27875684]
-synonym: "ER-plasma membrane tethering" EXACT [GOC:dph]
-is_a: GO:0051643 ! endoplasmic reticulum localization
-is_a: GO:0140056 ! organelle localization by membrane tethering
+def: "OBSOLETE. The attachment of an endoplasmic reticulum membrane to the plasma membrane via molecular tethers." [GOC:dph, GOC:vw, PMID:23237950, PMID:26877082, PMID:27875684]
+comment: This term was obsoleted because it represents a molecular function. Annotations should be migrated to GO:0160214 'endoplasmic reticulum-plasma membrane adaptor activity'; the biological process aspect (if any) is captured by GO:0051643 'endoplasmic reticulum localization'.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31873" xsd:anyURI
+is_obsolete: true
+consider: GO:0051643
+consider: GO:0160214
 created_by: dph
 creation_date: 2016-12-05T14:43:58Z
 

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | codex | 0.909 | 0.909 | 0.909 | `ff74649` | [#540](https://github.com/ai4curation/eval-ont-agent-go/pull/540) | [attempt](attempts/pr540.md) |
| 2 | claude-opus-4.7 | claude | 0.909 | 0.909 | 0.909 | `0e0e802` | [#330](https://github.com/ai4curation/eval-ont-agent-go/pull/330) | [attempt](attempts/pr330.md) |
| 3 | kimi-k2.6 | opencode | 0.870 | 0.909 | 0.833 | `ecbd519` | [#257](https://github.com/ai4curation/eval-ont-agent-go/pull/257) | [attempt](attempts/pr257.md) |
| 4 | claude-sonnet-4.5 | claude | 0.818 | 0.818 | 0.818 | `4d8147b` | [#461](https://github.com/ai4curation/eval-ont-agent-go/pull/461) | [attempt](attempts/pr461.md) |
| 5 | claude-haiku-4.5 | claude | 0.818 | 0.818 | 0.818 | `42962db` | [#412](https://github.com/ai4curation/eval-ont-agent-go/pull/412) | [attempt](attempts/pr412.md) |
| 6 | gemma-4-31b | opencode | 0.818 | 0.818 | 0.818 | `c0e3607` | [#238](https://github.com/ai4curation/eval-ont-agent-go/pull/238) | [attempt](attempts/pr238.md) |
| 7 | claude-sonnet-4.5 | copilot | 0.783 | 0.818 | 0.750 | `4412df6` | [#380](https://github.com/ai4curation/eval-ont-agent-go/pull/380) | [attempt](attempts/pr380.md) |
