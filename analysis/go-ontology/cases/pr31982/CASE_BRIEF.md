---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31964
pr_number: 31982
issue_title: GO:0052597 diamine oxidase activity terms
pr_author: sjm41
pr_merged_at: '2026-04-27'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
best_f1: 1.0
best_model: claude-sonnet-4.5
---

# PR #31982 — GO:0052597 diamine oxidase activity terms

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31964](https://github.com/geneontology/go-ontology/issues/31964) | [PR #31982](https://github.com/geneontology/go-ontology/pull/31982) | @sjm41 | merged 2026-04-27

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

The diamine oxidase activity sub-hierarchy had two issues identified during an enzyme term review: GO:0052598 `histamine oxidase activity` carried a redundant `xref: EC:1.4.3.22 {source="skos:broadMatch"}` that duplicated the broadMatch already present on its parent term GO:0052597, and GO:0004720 `protein-lysine 6-oxidase activity` was incorrectly parented under the diamine oxidase group when it belongs under a different oxidoreductase class.

## Changes Made

Two surgical edits were made in `go-edit.obo`. First, the redundant EC:1.4.3.22 broadMatch was removed from GO:0052598 `histamine oxidase activity`, since EC:1.4.3.22 covers the entire diamine oxidase group and the broadMatch is only appropriate on the parent term (GO:0052597). The RHEA:25625 exactMatch on the child term was retained. Second, GO:0004720 `protein-lysine 6-oxidase activity` was reparented from GO:0052597 to a more appropriate oxidoreductase parent, correcting a misclassification in the hierarchy.

## Resolution

Medium difficulty because the changes required understanding EC enzyme classification scope: EC:1.4.3.22 covers a group of diamine oxidases, so a broadMatch is appropriate on the parent but redundant (and potentially misleading) on a substrate-specific child. The reparenting decision required knowing that lysyl oxidase, despite sharing a copper amine oxidase mechanism, is not a diamine oxidase in the strict sense. The minimal line changes (3 additions, 2 deletions) reflect the surgical precision of the edits.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 23834996e..dd6593ace 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -46595,9 +46595,10 @@ synonym: "protein-L-lysine:oxygen 6-oxidoreductase (deaminating)" RELATED [EC:1.
 xref: EC:1.4.3.13 {source="skos:exactMatch"}
 xref: MetaCyc:PROTEIN-LYSINE-6-OXIDASE-RXN
 xref: RHEA:24544 {source="skos:exactMatch"}
-is_a: GO:0052597 ! diamine oxidase activity
+is_a: GO:0016641 ! oxidoreductase activity, acting on the CH-NH2 group of donors, oxygen as acceptor
 is_a: GO:0140096 ! catalytic activity, acting on a protein
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31964" xsd:anyURI
 
 [Term]
 id: GO:0004721
@@ -345365,13 +345366,13 @@ def: "Catalysis of the reaction: H2O + histamine + O2 = H2O2 + imidazole-4-aceta
 synonym: "1H-Imidazole-4-ethanamine oxidase activity" EXACT [KEGG_REACTION:R02150]
 synonym: "1H-Imidazole-4-ethanamine:oxygen oxidoreductase (deaminating) activity" EXACT [KEGG_REACTION:R02150]
 synonym: "histamine:oxygen oxidoreductase (deaminating) activity" EXACT systematic_synonym [EC:1.4.3.22]
-xref: EC:1.4.3.22 {source="skos:broadMatch"}
 xref: KEGG_REACTION:R02150
 xref: MetaCyc:RXN-9600
 xref: RHEA:25625 {source="skos:exactMatch"}
 is_a: GO:0052597 ! diamine oxidase activity
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28199" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31964" xsd:anyURI
 
 [Term]
 id: GO:0052599

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 1.000 | 1.000 | 1.000 | `dd6593a` | [#469](https://github.com/ai4curation/eval-ont-agent-go/pull/469) | [attempt](attempts/pr469.md) |
| 2 | claude-sonnet-4.5 | copilot | 1.000 | 1.000 | 1.000 | `dd6593a` | [#396](https://github.com/ai4curation/eval-ont-agent-go/pull/396) | [attempt](attempts/pr396.md) |
| 3 | claude-opus-4.7 | claude | 1.000 | 1.000 | 1.000 | `dd6593a` | [#350](https://github.com/ai4curation/eval-ont-agent-go/pull/350) | [attempt](attempts/pr350.md) |
| 4 | gpt-5.4 | codex | 1.000 | 1.000 | 1.000 | `dd6593a` | [#188](https://github.com/ai4curation/eval-ont-agent-go/pull/188) | [attempt](attempts/pr188.md) |
| 5 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `dd6593a` | [#96](https://github.com/ai4curation/eval-ont-agent-go/pull/96) | [attempt](attempts/pr96.md) |
| 6 | gpt-5.5 | opencode | 1.000 | 1.000 | 1.000 | `dd6593a` | [#78](https://github.com/ai4curation/eval-ont-agent-go/pull/78) | [attempt](attempts/pr78.md) |
| 7 | kimi-k2.6 | opencode | 0.889 | 1.000 | 0.800 | `feeefb7` | [#271](https://github.com/ai4curation/eval-ont-agent-go/pull/271) | [attempt](attempts/pr271.md) |
| 8 | claude-haiku-4.5 | claude | 0.857 | 0.750 | 1.000 | `8d9910a` | [#208](https://github.com/ai4curation/eval-ont-agent-go/pull/208) | [attempt](attempts/pr208.md) |
| 9 | gpt-5.5 | codex | 0.857 | 0.750 | 1.000 | `8d9910a` | [#56](https://github.com/ai4curation/eval-ont-agent-go/pull/56) | [attempt](attempts/pr56.md) |
