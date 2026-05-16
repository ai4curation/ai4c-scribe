---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31956
pr_number: 31960
issue_title: 'Obsoletion request: GO:0005870 actin capping protein of dynactin complex
  (unused, direct replacement)'
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-23'
task_type: obsoletion
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 10
generated_at: '2026-05-15'
domain_area: cellular_component
best_f1: 0.9
best_model: claude-sonnet-4.5
---

# PR #31960 — Obsoletion request: GO:0005870 actin capping protein of dynactin complex (unused, direct replacement)

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31956](https://github.com/geneontology/go-ontology/issues/31956) | [PR #31960](https://github.com/geneontology/go-ontology/pull/31960) | @dragon-ai-agent | merged 2026-04-23

`obsoletion` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #31956 requested obsoletion of GO:0005870 "actin capping protein of dynactin complex". The term was logically defined as an F-actin capping protein complex (GO:0008290) that is `part_of` a dynactin complex -- essentially a redundant subclass that no annotations used. Since the compositional relationship can be captured in GO-CAM models rather than pre-composed CC terms, the overly specific term was marked for obsoletion.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0005870 was obsoleted:
- Marked `is_obsolete: true`
- Added `replaced_by: GO:0008290` (F-actin capping protein complex)
- Removed the `intersection_of` and `relationship: part_of` axioms that defined it as a subclass
- Retained the term stanza for provenance

## Resolution

Merged same-day. This is a textbook obsoletion case: unused term, clear 1:1 replacement, and the specificity it captured (being part of dynactin) is better modeled compositionally in GO-CAM rather than through pre-composed CC terms.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 4aa8b2aca..6dd226998 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -57936,11 +57936,13 @@ relationship: part_of GO:0015629 ! actin cytoskeleton
 
 [Term]
 id: GO:0005870
-name: actin capping protein of dynactin complex
+name: obsolete actin capping protein of dynactin complex
 namespace: cellular_component
-def: "A heterodimer consisting of alpha and beta subunits that binds to and caps the barbed ends of actin filaments, nucleates the polymerization of actin monomers but does not sever actin filaments, and which is a part of the dynactin complex." [GOC:jl, PMID:18221362, PMID:18544499]
-intersection_of: GO:0008290 ! F-actin capping protein complex
-intersection_of: part_of GO:0005869 ! dynactin complex
+def: "OBSOLETE. A heterodimer consisting of alpha and beta subunits that binds to and caps the barbed ends of actin filaments, nucleates the polymerization of actin monomers but does not sever actin filaments, and which is a part of the dynactin complex." [GOC:jl, PMID:18221362, PMID:18544499]
+comment: This term was obsoleted because it is redundant with GO:0008290 (F-actin capping protein complex). Annotations can be migrated to the replacement term.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31956" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0008290
 
 [Term]
 id: GO:0005871

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.900 | 0.900 | 0.900 | `44241dd` | [#471](https://github.com/ai4curation/eval-ont-agent-go/pull/471) | [attempt](attempts/pr471.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.900 | 0.900 | 0.900 | `ae5eb58` | [#388](https://github.com/ai4curation/eval-ont-agent-go/pull/388) | [attempt](attempts/pr388.md) |
| 3 | claude-opus-4.7 | claude | 0.900 | 0.900 | 0.900 | `eb67838` | [#342](https://github.com/ai4curation/eval-ont-agent-go/pull/342) | [attempt](attempts/pr342.md) |
| 4 | kimi-k2.6 | opencode | 0.900 | 0.900 | 0.900 | `207ee23` | [#272](https://github.com/ai4curation/eval-ont-agent-go/pull/272) | [attempt](attempts/pr272.md) |
| 5 | gemma-4-31b | opencode | 0.900 | 0.900 | 0.900 | `d89bc91` | [#243](https://github.com/ai4curation/eval-ont-agent-go/pull/243) | [attempt](attempts/pr243.md) |
| 6 | claude-haiku-4.5 | claude | 0.900 | 0.900 | 0.900 | `9a77745` | [#207](https://github.com/ai4curation/eval-ont-agent-go/pull/207) | [attempt](attempts/pr207.md) |
| 7 | gpt-5.4 | codex | 0.900 | 0.900 | 0.900 | `280f07d` | [#184](https://github.com/ai4curation/eval-ont-agent-go/pull/184) | [attempt](attempts/pr184.md) |
| 8 | gpt-5.5 | opencode | 0.900 | 0.900 | 0.900 | `9a77745` | [#151](https://github.com/ai4curation/eval-ont-agent-go/pull/151) | [attempt](attempts/pr151.md) |
| 9 | gpt-5.5 | opencode | 0.900 | 0.900 | 0.900 | `9a77745` | [#132](https://github.com/ai4curation/eval-ont-agent-go/pull/132) | [attempt](attempts/pr132.md) |
| 10 | gpt-5.5 | codex | 0.900 | 0.900 | 0.900 | `9a77745` | [#115](https://github.com/ai4curation/eval-ont-agent-go/pull/115) | [attempt](attempts/pr115.md) |
