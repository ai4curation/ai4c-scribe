---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3602
pr_number: 3603
issue_title: 'NTR: occlusal surface of tooth'
pr_author: dragon-ai-agent
pr_merged_at: '2025-09-02'
task_type: new_term
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 2
generated_at: '2026-05-15'
domain_area: dental-anatomy
best_f1: 0.632
best_model: claude-opus-4.7
---

# PR #3603 — NTR: occlusal surface of tooth

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3602](https://github.com/obophenotype/uberon/issues/3602) | [PR #3603](https://github.com/obophenotype/uberon/pull/3603) | @dragon-ai-agent | merged 2025-09-02

`new_term` `simple` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for "occlusal surface of tooth," the biting or chewing surface where upper and lower teeth meet. The parent term "tooth surface structure" (UBERON:8600148) already existed, making classification straightforward.

## Changes Made

Added UBERON:8600149 for "occlusal surface of tooth" as a subclass of tooth surface structure. Included an exact synonym ("occlusal surface"), a definition referencing a dental education source, and appropriate relationships.

## Resolution

Simple difficulty because the parent class already existed and the anatomical concept is well-defined. An agent needs to follow the standard NTR pattern: create a new term stanza, place it under the correct parent, add a definition with reference, and include synonyms. Approved on first review.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 989f151e1..138990fd8 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -225363,6 +225363,15 @@ intersection_of: part_of UBERON:0001091 ! calcareous tooth
 relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
 property_value: dcterms-date "2025-08-05T09:28:57Z" xsd:dateTime
 
+[Term]
+id: UBERON:8600149
+name: occlusal surface of tooth
+def: "A tooth surface structure that forms the biting or grinding surface of a molar or premolar." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+synonym: "occlusal surface" EXACT [https://dentaleducationhub.com/surfaces-of-the-teeth/]
+is_a: UBERON:8600148 ! tooth surface structure
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-08-29T11:00:00Z" xsd:dateTime
+
 [Term]
 id: UBERON:8700000
 name: aorta-gonad-mesonephros

```

## Agent Attempts (2)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.632 | 1.000 | 0.462 | `57b2049` | [#252](https://github.com/ai4curation/eval-ont-agent-uberon/pull/252) | [attempt](attempts/pr252.md) |
| 2 | claude-sonnet-4.5 | claude | 0.615 | 0.667 | 0.571 | `88fd2c2` | [#298](https://github.com/ai4curation/eval-ont-agent-uberon/pull/298) | [attempt](attempts/pr298.md) |
