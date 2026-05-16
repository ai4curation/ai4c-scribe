---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 25870
pr_number: 32008
issue_title: GO terms with EC:1.13.11.37 xref
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-28'
task_type: obsoletion
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 7
generated_at: '2026-05-15'
domain_area: molecular_function
best_f1: 0.881
best_model: gpt-5.5
---

# PR #32008 — GO terms with EC:1.13.11.37 xref

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #25870](https://github.com/geneontology/go-ontology/issues/25870) | [PR #32008](https://github.com/geneontology/go-ontology/pull/32008) | @dragon-ai-agent | merged 2026-04-28

`obsoletion` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #25870 (opened July 2023) identified problems with GO terms carrying the EC:1.13.11.37 cross-reference. GO:0018581 "hydroxyquinol 1,2-dioxygenase activity" described only the first step of the reaction, while GO:0047074 described the complete reaction. This PR resolves the duplication by obsoleting GO:0018581 and renaming GO:0047074 to the more recognizable name.

## Changes Made

Two files were modified:
1. In `src/ontology/go-edit.obo`: GO:0018581 was obsoleted with `replaced_by: GO:0047074`, and GO:0047074 was renamed to "hydroxyquinol 1,2-dioxygenase activity" (taking the name from the obsoleted term since it is the more commonly used label)
2. In `src/ontology/imports/go-catalytic-activities-participants.owl`: Removed 31 lines of OWL axioms that referenced the obsoleted term's reaction participants

## Resolution

Merged directly. This addressed part of a long-standing issue (nearly 3 years old) about EC cross-reference alignment. The two-file change demonstrates that obsoletion can require cleanup in both the main edit file and the OWL imports that encode reaction participant relationships.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 8262d5a8a..4c1a6c46f 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -138332,16 +138332,14 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0018581
-name: hydroxyquinol 1,2-dioxygenase activity
+name: obsolete hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
-def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
-xref: EC:1.13.11.37 {source="skos:broadMatch"}
-xref: MetaCyc:RXN-17556
-xref: RHEA:19441 {source="skos:exactMatch"}
-xref: UM-BBD_reactionID:r0232
-is_a: GO:0016702 ! oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of two atoms of oxygen
+def: "OBSOLETE. Catalysis of the reaction: benzene-1,2,4-triol + O2 = 3-hydroxy-cis,cis-muconate + 2 H+." [RHEA:19441]
+comment: The reason for obsoletion is that this term described a sub-reaction of the complete two-step reaction represented by GO:0047074. The second step (non-enzymatic conversion of 3-hydroxy-cis,cis-muconate to maleylacetate) is not catalyzed separately, so this term is equivalent to GO:0047074 hydroxyquinol 1,2-dioxygenase activity.
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/25870" xsd:anyURI
 property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/30193" xsd:anyURI
+is_obsolete: true
+replaced_by: GO:0047074
 
 [Term]
 id: GO:0018582
@@ -291741,9 +291739,10 @@ property_value: term_tracker_item "https://github.com/geneontology/go-ontology/i
 
 [Term]
 id: GO:0047074
-name: 4-hydroxycatechol 1,2-dioxygenase activity
+name: hydroxyquinol 1,2-dioxygenase activity
 namespace: molecular_function
 def: "Catalysis of the reaction: benzene-1,2,4-triol + O2 = maleylacetate + 2 H+." [RHEA:35595]
+synonym: "4-hydroxycatechol 1,2-dioxygenase activity" EXACT []
 xref: EC:1.13.11.37 {source="skos:exactMatch"}
 xref: MetaCyc:RXN-10137
 xref: RHEA:35595 {source="skos:exactMatch"}
diff --git a/src/ontology/imports/go-catalytic-activities-participants.owl b/src/ontology/imports/go-catalytic-activities-participants.owl
index fb8b76d32..f80973982 100644
--- a/src/ontology/imports/go-catalytic-activities-participants.owl
+++ b/src/ontology/imports/go-catalytic-activities-participants.owl
@@ -69756,37 +69756,6 @@
     
 
 
-    <!-- http://purl.obolibrary.org/obo/GO_0018581 -->
-
-    <owl:Class rdf:about="http://purl.obolibrary.org/obo/GO_0018581">
-        <rdfs:subClassOf>
-            <owl:Restriction>
-                <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0000057"/>
-                <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/CHEBI_15378"/>
-            </owl:Restriction>
-        </rdfs:subClassOf>
-        <rdfs:subClassOf>
-            <owl:Restriction>
-                <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0000057"/>
-                <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/CHEBI_15379"/>
-            </owl:Restriction>
-        </rdfs:subClassOf>
-        <rdfs:subClassOf>
-            <owl:Restriction>
-                <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0000057"/>
-                <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/CHEBI_16971"/>
-            </owl:Restriction>
-        </rdfs:subClassOf>
-        <rdfs:subClassOf>
-            <owl:Restriction>
-                <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0000057"/>
-                <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/CHEBI_58139"/>
-            </owl:Restriction>
-        </rdfs:subClassOf>
-    </owl:Class>
-    
-
-
     <!-- http://purl.obolibrary.org/obo/GO_0018582 -->
 
     <owl:Class rdf:about="http://purl.obolibrary.org/obo/GO_0018582">

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.5 | codex | 0.881 | 0.963 | 0.812 | [#545](https://github.com/ai4curation/eval-ont-agent-go/pull/545) | [attempt](attempts/pr545.md) |
| 2 | claude-sonnet-4.5 | claude | 0.667 | 0.519 | 0.933 | [#453](https://github.com/ai4curation/eval-ont-agent-go/pull/453) | [attempt](attempts/pr453.md) |
| 3 | claude-opus-4.7 | claude | 0.667 | 0.519 | 0.933 | [#331](https://github.com/ai4curation/eval-ont-agent-go/pull/331) | [attempt](attempts/pr331.md) |
| 4 | kimi-k2.6 | opencode | 0.667 | 0.519 | 0.933 | [#254](https://github.com/ai4curation/eval-ont-agent-go/pull/254) | [attempt](attempts/pr254.md) |
| 5 | claude-sonnet-4.5 | copilot | 0.651 | 0.519 | 0.875 | [#374](https://github.com/ai4curation/eval-ont-agent-go/pull/374) | [attempt](attempts/pr374.md) |
| 6 | claude-haiku-4.5 | claude | 0.634 | 0.481 | 0.929 | [#406](https://github.com/ai4curation/eval-ont-agent-go/pull/406) | [attempt](attempts/pr406.md) |
| 7 | gemma-4-31b | opencode | 0.634 | 0.481 | 0.929 | [#252](https://github.com/ai4curation/eval-ont-agent-go/pull/252) | [attempt](attempts/pr252.md) |
