---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31051
pr_number: 32037
issue_title: 'Taxon constraint: GO:0046544 development of secondary male sexual characteristics'
pr_author: dragon-ai-agent
pr_merged_at: '2026-05-06'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 7
generated_at: '2026-05-15'
domain_area: biological_process
best_f1: 0.917
best_model: claude-haiku-4.5
---

# PR #32037 — Taxon constraint: GO:0046544 development of secondary male sexual characteristics

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31051](https://github.com/geneontology/go-ontology/issues/31051) | [PR #32037](https://github.com/geneontology/go-ontology/pull/32037) | @dragon-ai-agent | merged 2026-05-06

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #31051 requested taxon constraints for GO:0046544 (development of secondary male sexual characteristics). After the initial implementation in PR #32027 used a "sensu Metazoa" suffix, a reviewer pointed out that the GO naming convention uses an "animal" prefix (following precedent from GO:0048513 "animal organ development"). This follow-up PR switches from the suffix to the prefix style.

## Changes Made

In `src/ontology/go-edit.obo`, three terms were renamed:
- GO:0045136: "development of secondary sexual characteristics, sensu Metazoa" became "development of animal secondary sexual characteristics"
- GO:0046543: "development of secondary female sexual characteristics, sensu Metazoa" became "development of animal secondary female sexual characteristics"
- GO:0046544: "development of secondary male sexual characteristics, sensu Metazoa" became "development of animal secondary male sexual characteristics"

The previous labels were retained as EXACT synonyms to preserve backward compatibility.

## Resolution

This was a clean follow-up PR that applied a straightforward naming convention fix. No further review was required because the change simply implemented the reviewer's directive from the prior PR. The taxon constraint and softened definitions from PR #32027 were left unchanged.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 455454c0f..31a6b69c4 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -270021,10 +270021,11 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0045136
-name: development of secondary sexual characteristics, sensu Metazoa
+name: development of animal secondary sexual characteristics
 namespace: biological_process
 def: "The process whose specific outcome is the progression of the secondary sexual characteristics over time, from their formation to the mature structures. In mammals, examples include growth of axillary, chest, and pubic hair, voice changes, testicular/penile enlargement, breast development and menstrual periods. Development occurs in response to sex hormone secretion." [GOC:ai]
 synonym: "development of secondary sexual characteristics" EXACT []
+synonym: "development of secondary sexual characteristics, sensu Metazoa" EXACT []
 is_a: GO:0003006 ! developmental process involved in reproduction
 relationship: part_of GO:0007275 ! multicellular organism development
 relationship: part_of GO:0007548 ! sex differentiation
@@ -285691,21 +285692,23 @@ consider: GO:0015833
 
 [Term]
 id: GO:0046543
-name: development of secondary female sexual characteristics, sensu Metazoa
+name: development of animal secondary female sexual characteristics
 namespace: biological_process
 def: "The process whose specific outcome is the progression of the secondary female sexual characteristics over time, from their formation to the mature structures. In female mammals, examples include growth of axillary and pubic hair, breast development and menstrual periods. Their development occurs in response to sex hormone secretion." [GOC:ai]
 synonym: "development of secondary female sexual characteristics" EXACT []
-is_a: GO:0045136 ! development of secondary sexual characteristics, sensu Metazoa
+synonym: "development of secondary female sexual characteristics, sensu Metazoa" EXACT []
+is_a: GO:0045136 ! development of animal secondary sexual characteristics
 relationship: part_of GO:0046660 ! female sex differentiation
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31051" xsd:anyURI
 
 [Term]
 id: GO:0046544
-name: development of secondary male sexual characteristics, sensu Metazoa
+name: development of animal secondary male sexual characteristics
 namespace: biological_process
 def: "The process whose specific outcome is the progression of the secondary male sexual characteristics over time, from their formation to the mature structures. In male mammals, examples include growth of axillary, chest, and pubic hair, voice changes, and testicular/penile enlargement. Development occurs in response to sex hormone secretion." [GOC:ai]
 synonym: "development of secondary male sexual characteristics" EXACT []
-is_a: GO:0045136 ! development of secondary sexual characteristics, sensu Metazoa
+synonym: "development of secondary male sexual characteristics, sensu Metazoa" EXACT []
+is_a: GO:0045136 ! development of animal secondary sexual characteristics
 relationship: part_of GO:0046661 ! male sex differentiation
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31051" xsd:anyURI
 

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-haiku-4.5 | claude | 0.917 | 1.000 | 0.846 | [#407](https://github.com/ai4curation/eval-ont-agent-go/pull/407) | [attempt](attempts/pr407.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.900 | 0.818 | 1.000 | [#371](https://github.com/ai4curation/eval-ont-agent-go/pull/371) | [attempt](attempts/pr371.md) |
| 3 | claude-sonnet-4.5 | claude | 0.846 | 1.000 | 0.733 | [#458](https://github.com/ai4curation/eval-ont-agent-go/pull/458) | [attempt](attempts/pr458.md) |
| 4 | claude-opus-4.7 | claude | 0.696 | 0.727 | 0.667 | [#326](https://github.com/ai4curation/eval-ont-agent-go/pull/326) | [attempt](attempts/pr326.md) |
| 5 | gemma-4-31b | opencode | 0.696 | 0.727 | 0.667 | [#241](https://github.com/ai4curation/eval-ont-agent-go/pull/241) | [attempt](attempts/pr241.md) |
| 6 | gpt-5.5 | codex | 0.688 | 1.000 | 0.524 | [#541](https://github.com/ai4curation/eval-ont-agent-go/pull/541) | [attempt](attempts/pr541.md) |
| 7 | kimi-k2.6 | opencode | 0.615 | 0.727 | 0.533 | [#260](https://github.com/ai4curation/eval-ont-agent-go/pull/260) | [attempt](attempts/pr260.md) |
