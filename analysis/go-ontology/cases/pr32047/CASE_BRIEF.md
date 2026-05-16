---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 32046
pr_number: 32047
issue_title: 'NTR: [double-stranded RNA immune receptor activity]'
pr_author: dragon-ai-agent
pr_merged_at: '2026-05-07'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 10
generated_at: '2026-05-15'
best_f1: 0.933
best_model: claude-opus-4.7
---

# PR #32047 — NTR: [double-stranded RNA immune receptor activity]

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #32046](https://github.com/geneontology/go-ontology/issues/32046) | [PR #32047](https://github.com/geneontology/go-ontology/pull/32047) | @dragon-ai-agent | merged 2026-05-07

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for molecular function terms covering cytosolic double-stranded RNA immune receptor activity. The existing GO term `GO:0038187 pattern recognition receptor activity` lacked specific children for dsRNA sensors such as NLRP1, NLRP6, IFIH1/MDA5, and ZBP1. The request came from a signaling domain expert who needed these terms for annotation of innate immune signaling pathways.

## Changes Made

Two new terms were added to `go-edit.obo` in a parent-child relationship: GO:7770072 `double-stranded RNA immune receptor activity` as a child of `GO:0038187 pattern recognition receptor activity`, covering broad cytosolic dsRNA sensors, and GO:7770073 `left-handed Z-RNA immune receptor activity` as a more specific child term covering ZBP1-type receptors that specifically recognize the Z-RNA conformation of dsRNA.

## Resolution

The PR was created and merged within the same day by the AI agent. The task required medium difficulty because the two terms needed to correctly reflect the immunological distinction between general dsRNA recognition (by sensors like MDA5) and the specialized Z-RNA conformation recognition (by ZBP1), which is a relatively recent discovery in innate immunity. The hierarchical relationship between the two terms had to be biologically accurate.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index a42b54384..0c887671c 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -617522,6 +617522,31 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-05-07T07:41:13Z
 
+[Term]
+id: GO:7770072
+name: double-stranded RNA immune receptor activity
+namespace: molecular_function
+def: "Combining with a double-stranded RNA and transmitting the signal to initiate an innate immune response." [PMID:23273991, PMID:33243852, PMID:34678144]
+synonym: "dsRNA immune receptor activity" EXACT []
+is_a: GO:0038187 ! pattern recognition receptor activity
+intersection_of: GO:0038023 ! signaling receptor activity
+intersection_of: has_primary_input CHEBI:67208 ! double-stranded RNA
+relationship: has_part GO:0003725 ! double-stranded RNA binding
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/32046" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-07T12:45:27Z
+
+[Term]
+id: GO:7770073
+name: left-handed Z-RNA immune receptor activity
+namespace: molecular_function
+def: "Combining with a left-handed Z-RNA and transmitting the signal to initiate an innate immune response. Z-RNA is a left-handed double-helical conformation of RNA in which the phosphate backbone zigzags." [PMID:32200799]
+synonym: "Z-RNA immune receptor activity" EXACT []
+is_a: GO:7770072 ! double-stranded RNA immune receptor activity
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/32046" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-07T12:45:27Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.933 | 0.933 | 0.933 | `ac55d36` | [#354](https://github.com/ai4curation/eval-ont-agent-go/pull/354) | [attempt](attempts/pr354.md) |
| 2 | kimi-k2.6 | opencode | 0.933 | 0.933 | 0.933 | `5158bbd` | [#289](https://github.com/ai4curation/eval-ont-agent-go/pull/289) | [attempt](attempts/pr289.md) |
| 3 | claude-sonnet-4.5 | claude | 0.867 | 0.867 | 0.867 | `f1f924d` | [#483](https://github.com/ai4curation/eval-ont-agent-go/pull/483) | [attempt](attempts/pr483.md) |
| 4 | gpt-5.4 | codex | 0.867 | 0.867 | 0.867 | `d390a88` | [#209](https://github.com/ai4curation/eval-ont-agent-go/pull/209) | [attempt](attempts/pr209.md) |
| 5 | gpt-5.5 | codex | 0.867 | 0.867 | 0.867 | `e7223fe` | [#71](https://github.com/ai4curation/eval-ont-agent-go/pull/71) | [attempt](attempts/pr71.md) |
| 6 | claude-haiku-4.5 | claude | 0.774 | 0.800 | 0.750 | `04a2016` | [#220](https://github.com/ai4curation/eval-ont-agent-go/pull/220) | [attempt](attempts/pr220.md) |
| 7 | gpt-5.5 | opencode | 0.765 | 0.867 | 0.684 | `a7c1bb2` | [#109](https://github.com/ai4curation/eval-ont-agent-go/pull/109) | [attempt](attempts/pr109.md) |
| 8 | gpt-5.5 | opencode | 0.765 | 0.867 | 0.684 | `a7c1bb2` | [#89](https://github.com/ai4curation/eval-ont-agent-go/pull/89) | [attempt](attempts/pr89.md) |
| 9 | claude-sonnet-4.5 | copilot | 0.692 | 0.600 | 0.818 | `249436b` | [#503](https://github.com/ai4curation/eval-ont-agent-go/pull/503) | [attempt](attempts/pr503.md) |
| 10 | claude-sonnet-4.5 | copilot | 0.692 | 0.600 | 0.818 | `249436b` | [#448](https://github.com/ai4curation/eval-ont-agent-go/pull/448) | [attempt](attempts/pr448.md) |
