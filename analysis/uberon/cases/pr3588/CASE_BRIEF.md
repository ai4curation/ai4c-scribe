---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3583
pr_number: 3588
issue_title: New terms for tooth surfaces
pr_author: aleixpuigb
pr_merged_at: '2025-08-05'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 2
generated_at: '2026-05-15'
domain_area: dental-anatomy
best_f1: 0.379
best_model: claude-opus-4.7
---

# PR #3588 — New terms for tooth surfaces

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3583](https://github.com/obophenotype/uberon/issues/3583) | [PR #3588](https://github.com/obophenotype/uberon/pull/3588) | @aleixpuigb | merged 2025-08-05

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A request was made to add multiple new terms for tooth surfaces to Uberon. Dental anatomy uses specific terminology for the different surfaces of a tooth (mesial, distal, buccal, lingual, etc.), and these were needed for downstream annotation projects.

## Changes Made

Added approximately 7-8 new tooth surface terms with 75 lines of additions to uberon-edit.obo. Each term followed a consistent pattern with definitions, synonyms, parent class (tooth surface structure), and relationships. The 5 commits suggest iterative refinement of the batch.

## Resolution

Medium difficulty because while each individual term follows a standard pattern, the agent must consistently apply the same modeling approach across multiple terms, ensure no duplication, and get the dental anatomy right for each surface type. The batch nature makes it more complex than a single NTR.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index a84557c7c..0479f338d 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -225288,6 +225288,81 @@ intersection_of: part_of UBERON:0001052 ! rectum
 relationship: dc-contributor https://orcid.org/0000-0002-7073-9172 ! David Osumi-Sutherland
 property_value: dcterms-date "2025-05-27T17:07:22Z" xsd:dateTime
 
+[Term]
+id: UBERON:8600141
+name: distal surface of tooth
+def: "A tooth surface structure that is oriented away from the median plane of the dental arch or oral cavity." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+is_a: UBERON:8600148 ! tooth surface structure
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600142
+name: incisal surface of tooth
+def: "A tooth surface structure that forms the cutting edge of an incisor or canine tooth. It functions to shear or incise food during biting." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+is_a: UBERON:8600148 ! tooth surface structure
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600143
+name: labial surface of tooth
+def: "A tooth surface structure that faces the lips." [https://dentaleducationhub.com/surfaces-of-the-teeth/]
+comment: Tooth surfaces are typically abbreviated using their initial letters. To avoid confusion between 'L' for lingual and labial surfaces, the letter 'F' (for facial surface) is commonly used to refer to the labial surface. {xref="https://orcid.org/0000-0001-9625-1899"}
+synonym: "facial surface of tooth" BROAD []
+is_a: UBERON:8600147 ! facial surface of tooth
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600144
+name: lingual surface of tooth
+def: "A tooth surface structure that faces the tongue or its anatomical equivalent." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+is_a: UBERON:8600148 ! tooth surface structure
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600145
+name: mesial surface of tooth
+def: "A tooth surface structure that is oriented toward the median plane of the dental arch." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+is_a: UBERON:8600148 ! tooth surface structure
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600146
+name: buccal surface of tooth
+def: "A tooth surface structure that is oriented toward the buccal mucosa (i.e., the inner lining of the cheek)." [https://dentaleducationhub.com/surfaces-of-the-teeth/, https://terminology.hl7.org/CodeSystem-FDI-surface.html]
+is_a: UBERON:8600147 ! facial surface of tooth
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600147
+name: facial surface of tooth
+def: "A tooth surface structure that is oriented toward the lips or cheeks." [https://dentaleducationhub.com/surfaces-of-the-teeth/]
+is_a: UBERON:8600148 ! tooth surface structure
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+relationship: dc-contributor https://orcid.org/0000-0001-9625-1899
+property_value: dcterms-date "2025-07-24T08:20:48Z" xsd:dateTime
+
+[Term]
+id: UBERON:8600148
+name: tooth surface structure
+def: "A surface structure that is part of a calcareous tooth." [PMID:32491475]
+synonym: "tooth surface" EXACT [PMID:32071532]
+intersection_of: UBERON:0003102 ! surface structure
+intersection_of: part_of UBERON:0001091 ! calcareous tooth
+relationship: dc-contributor https://orcid.org/0000-0001-6677-8489 ! Aleix Puig-Barbé
+property_value: dcterms-date "2025-08-05T09:28:57Z" xsd:dateTime
+
 [Term]
 id: UBERON:8700000
 name: aorta-gonad-mesonephros

```

## Agent Attempts (2)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.379 | 0.440 | 0.333 | `65caaa1` | [#250](https://github.com/ai4curation/eval-ont-agent-uberon/pull/250) | [attempt](attempts/pr250.md) |
| 2 | claude-sonnet-4.5 | claude | 0.364 | 0.400 | 0.333 | `a806812` | [#318](https://github.com/ai4curation/eval-ont-agent-uberon/pull/318) | [attempt](attempts/pr318.md) |
