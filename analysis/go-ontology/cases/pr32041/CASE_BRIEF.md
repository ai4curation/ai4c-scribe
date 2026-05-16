---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31902
pr_number: 32041
issue_title: 'NTR: [venom-mediated inflammatory response+... leukocyte infiltration+...
  release of inflammatory mediator]'
pr_author: dragon-ai-agent
pr_merged_at: '2026-05-07'
task_type: new_term
difficulty: medium
scoping: loosely_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
best_f1: 0.9
best_model: claude-opus-4.7
---

# PR #32041 — NTR: [venom-mediated inflammatory response+... leukocyte infiltration+... release of inflammatory mediator]

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31902](https://github.com/geneontology/go-ontology/issues/31902) | [PR #32041](https://github.com/geneontology/go-ontology/pull/32041) | @dragon-ai-agent | merged 2026-05-07

`new_term` `medium` `loosely_scoped` `approved_first_time`

## Context

A new term request from a UniProt curator asked for several venom-related biological process terms, including venom-mediated activation of inflammatory response, leukocyte infiltration, and release of inflammatory mediator. These terms are needed to annotate venom toxin proteins that trigger inflammatory cascades in envenomated organisms. The issue referenced PMID:19000915 and PMID:32024243 as supporting literature.

## Changes Made

The PR added GO:7770071 `venom-mediated activation of inflammatory response` as a biological process term. The definition captures the inter-organism nature of envenomation: one organism causes inflammatory response in another organism via venom action. The term includes both a broad synonym (`venom-mediated inflammation`) and an exact synonym using the standard GO inter-organism phrasing (`envenomation resulting in positive regulation of inflammatory response in another organism`).

## Resolution

This PR addressed only one of the three terms requested in the issue, making it partially scoped relative to the full request. The single-term approach is appropriate for incremental ontology development, allowing each term to be reviewed independently. Medium difficulty because the definition required careful framing of inter-organism process semantics, which follow specific GO conventions for processes that span two organisms.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 7aec1566d..c8728f302 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -617485,6 +617485,19 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 created_by: dragon-ai-agent
 creation_date: 2026-05-06T17:36:35Z
 
+[Term]
+id: GO:7770071
+name: venom-mediated activation of inflammatory response
+namespace: biological_process
+def: "A process by which an organism causes inflammatory response in another organism via the action of a venom." [PMID:19000915, PMID:32024243]
+synonym: "venom-mediated inflammation" BROAD []
+synonym: "envenomation resulting in positive regulation of inflammatory response in another organism" EXACT []
+intersection_of: GO:0035738 ! venom-mediated perturbation of biological process
+intersection_of: positively_regulates_in_another_organism GO:0006954 ! inflammatory response
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31902" xsd:anyURI
+created_by: dragon-ai-agent
+creation_date: 2026-05-07T07:41:13Z
+
 [Typedef]
 id: acts_on_population_of
 name: acts on population of

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.900 | 0.900 | 0.900 | [#332](https://github.com/ai4curation/eval-ont-agent-go/pull/332) | [attempt](attempts/pr332.md) |
| 2 | gpt-5.5 | opencode | 0.842 | 0.800 | 0.889 | [#107](https://github.com/ai4curation/eval-ont-agent-go/pull/107) | [attempt](attempts/pr107.md) |
| 3 | gpt-5.5 | opencode | 0.842 | 0.800 | 0.889 | [#88](https://github.com/ai4curation/eval-ont-agent-go/pull/88) | [attempt](attempts/pr88.md) |
| 4 | gpt-5.5 | codex | 0.842 | 0.800 | 0.889 | [#69](https://github.com/ai4curation/eval-ont-agent-go/pull/69) | [attempt](attempts/pr69.md) |
| 5 | claude-sonnet-4.5 | claude | 0.778 | 0.700 | 0.875 | [#468](https://github.com/ai4curation/eval-ont-agent-go/pull/468) | [attempt](attempts/pr468.md) |
| 6 | claude-sonnet-4.5 | copilot | 0.778 | 0.700 | 0.875 | [#384](https://github.com/ai4curation/eval-ont-agent-go/pull/384) | [attempt](attempts/pr384.md) |
| 7 | claude-haiku-4.5 | claude | 0.593 | 0.800 | 0.471 | [#205](https://github.com/ai4curation/eval-ont-agent-go/pull/205) | [attempt](attempts/pr205.md) |
| 8 | kimi-k2.6 | opencode | 0.581 | 0.900 | 0.429 | [#287](https://github.com/ai4curation/eval-ont-agent-go/pull/287) | [attempt](attempts/pr287.md) |
| 9 | gpt-5.4 | codex | 0.533 | 0.800 | 0.400 | [#179](https://github.com/ai4curation/eval-ont-agent-go/pull/179) | [attempt](attempts/pr179.md) |
