---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31877
pr_number: 31973
issue_title: 'Obsoletion request: GO:0010381 peroxisome-chloroplast membrane tethering
  and NEW TERM peroxisome-chloroplast membrane tether activity'
pr_author: dragon-ai-agent
pr_merged_at: '2026-04-27'
task_type: obsoletion
difficulty: hard
scoping: mostly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-17'
scoping_notes: Primary change was obsoletion of GO:0010381 but the PR also touched
  taxon constraint files due to cascading effects of the obsoletion on constraint
  imports.
domain_area: biological_process
best_f1: 0.553
best_model: gpt-5.5
---

# PR #31973 — Obsoletion request: GO:0010381 peroxisome-chloroplast membrane tethering and NEW TERM peroxisome-chloroplast membrane tether activity

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31877](https://github.com/geneontology/go-ontology/issues/31877) | [PR #31973](https://github.com/geneontology/go-ontology/pull/31973) | @dragon-ai-agent | merged 2026-04-27

`obsoletion` `hard` `mostly_scoped` `approved_first_time`

## Context

Issue #31877 requested both obsoletion of GO:0010381 "peroxisome-chloroplast membrane tethering" (BP) and creation of a replacement MF term. The new term GO:7770065 was added in PR #31929. This PR handles the obsoletion and the resulting cleanup cascade: when a term with taxon constraints is obsoleted, those constraints must be removed from multiple files.

## Changes Made

Four files were modified across 5 commits:
1. `src/ontology/go-edit.obo`: Obsoleted GO:0010381 with standard obsoletion metadata
2. `src/ontology/imports/go_taxon_constraints.owl`: Large OWL file regenerated (-558/+481 lines) reflecting removal of constraints on the obsoleted term
3. `src/taxon_constraints/never_in_taxon.ofn`: Removed 20 lines of OWL axioms for constraints on GO:0010381
4. `src/taxon_constraints/never_in_taxon.tsv`: Removed 4 TSV rows for the term's taxon constraints

## Resolution

The 5 commits show iterative resolution of CI failures: the initial obsoletion passed validation but the taxon constraint files needed manual cleanup to remove references to the now-obsolete term. This case demonstrates that GO obsoletion is not always a single-file operation -- terms with taxon constraints require coordinated changes across the constraint pipeline.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7, 2026-05-15.** This is a poor evaluation
case: the metadiff gold (#31973) is self-contradicting and dominated by
auto-generated artifact noise. Reviewing the issue thread (#31877) and PR
commit history establishes the following.

### The issue's actual asks and curator-blessed solution

1. The issue requested obsoletion of `GO:0010381` (BP) because it represents
   a molecular function, with reannotation to the new MF term `GO:7770065`
   (added separately in companion **PR #31929**, which is *not* in scope for
   this eval — agents were only asked to obsolete).
2. `raymond91125` triggered the obsoletion; `tberardini` (TAIR, the sole
   annotator) approved proceeding and asked the ticket stay open until she
   migrates the one EXP annotation.
3. **`consider:` is correct, `replaced_by:` is wrong.** The author first used
   `consider: GO:7770065` (cross-aspect BP→MF needs manual review, not
   automatic replacement). `pgaudet` confirmed in-thread: *"I dont think we
   want to `replace` terms across ontology aspects."* The merged gold's
   `go-edit.obo` final state uses `consider: GO:7770065`.
4. **TC cleanup is `.tsv`-only.** `raymond91125` explicitly instructed:
   *"please reverse the changes for taxon restrictions on files other than
   src/taxon_constraints/never_in_taxon.tsv. Other files are regenerated based
   on src/taxon_constraints/never_in_taxon.tsv by post-processing."* The only
   hand edit that should be in the PR is removing the 4 `GO:0010381` rows from
   `never_in_taxon.tsv` (Choanoflagellida, Metazoa, Fungi, Amoebozoa).

### Why the gold PR is a poor reference

The 5 commits are: (1) obsolete in go-edit.obo, (2) remove 4 `.tsv` rows,
(3) **`113327b7c` Revert post-processed taxon constraint files** (complying
with raymond91125), (4) merge master, (5) **`e1cd54e5c` Regenerate taxon
constraint OWL files** — which re-introduced exactly the `.ofn` (-20) and
`go_taxon_constraints.owl` (+481/-558) churn that commit 3 had reverted and
the curator had said must not be in the PR. The merged net diff therefore
contradicts the curator's own instruction, and its ~1000-line OWL delta is
overwhelmingly blank-node `genidNNNN` renumbering noise with no semantic
content (a single class removal shifts every downstream blank-node ID).

Consequently the metadiff F1 measures reproduction of generated-file noise,
not curation quality. Attempts that produced the clean, curator-blessed edit
score F1≈0.016 (go-edit.obo only) or F1≈0.553 (go-edit.obo + full TC
regeneration, which the curator explicitly rejected). All ten attempts should
be judged against the issue + curator comments, not the metadiff.

## Human Diff

```diff
diff --git a/src/ontology/go-edit.obo b/src/ontology/go-edit.obo
index 1448889b36..1855cac260 100644
--- a/src/ontology/go-edit.obo
+++ b/src/ontology/go-edit.obo
@@ -103437,11 +103437,13 @@ relationship: regulates GO:0015995 ! chlorophyll biosynthetic process
 
 [Term]
 id: GO:0010381
-name: peroxisome-chloroplast membrane tethering
+name: obsolete peroxisome-chloroplast membrane tethering
 namespace: biological_process
-def: "The attachment of a peroxisome to a chloroplast via molecular tethers that physically bridge their respective membranes and attach them to each other. The tethering may facilitate exchange of metabolites between the organelles." [PMID:17215364]
-synonym: "attachment of peroxisome to chloroplast" EXACT []
-is_a: GO:0140056 ! organelle localization by membrane tethering
+def: "OBSOLETE. The attachment of a peroxisome to a chloroplast via molecular tethers that physically bridge their respective membranes and attach them to each other. The tethering may facilitate exchange of metabolites between the organelles." [PMID:17215364]
+comment: This term was made obsolete because it represents a molecular function rather than a biological process.
+property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31877" xsd:anyURI
+is_obsolete: true
+consider: GO:7770065
 
 [Term]
 id: GO:0010383
diff --git a/src/ontology/imports/go_taxon_constraints.owl b/src/ontology/imports/go_taxon_constraints.owl
index 3f8051b7fd..21690045fb 100644
--- a/src/ontology/imports/go_taxon_constraints.owl
+++ b/src/ontology/imports/go_taxon_constraints.owl
@@ -924,6 +924,25 @@
     
 
 
+    <!-- http://purl.obolibrary.org/obo/GO_0000956 -->
+
+    <owl:Class rdf:about="http://purl.obolibrary.org/obo/GO_0000956">
+        <rdfs:subClassOf>
+            <owl:Restriction>
+                <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0002160"/>
+                <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_2759"/>
+            </owl:Restriction>
+        </rdfs:subClassOf>
+        <rdfs:subClassOf>
+            <owl:Restriction>
+                <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0002162"/>
+                <owl:allValuesFrom rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_2759"/>
+            </owl:Restriction>
+        </rdfs:subClassOf>
+    </owl:Class>
+    
+
+
     <!-- http://purl.obolibrary.org/obo/GO_0000957 -->
 
     <owl:Class rdf:about="http://purl.obolibrary.org/obo/GO_0000957">
@@ -2397,12 +2416,12 @@
     <!-- http://purl.obolibrary.org/obo/GO_0002224 -->
 
     <owl:Class rdf:about="http://purl.obolibrary.org/obo/GO_0002224">
-        <rdfs:subClassOf rdf:nodeID="genid310"/>
-        <rdfs:subClassOf rdf:nodeID="genid313"/>
-        <owl:disjointWith rdf:nodeID="genid316"/>
+        <rdfs:subClassOf rdf:nodeID="genid312"/>
+        <rdfs:subClassOf rdf:nodeID="genid315"/>
+        <owl:disjointWith rdf:nodeID="genid318"/>
         <obo:RO_0002161 rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_7215"/>
     </owl:Class>
-    <owl:Class rdf:nodeID="genid310">
+    <owl:Class rdf:nodeID="genid312">
         <owl:complementOf>
             <owl:Restriction>
                 <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0002162"/>
@@ -2410,7 +2429,7 @@
             </owl:Restriction>
         </owl:complementOf>
     </owl:Class>
-    <owl:Restriction rdf:nodeID="genid313">
+    <owl:Restriction rdf:nodeID="genid315">
         <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0002162"/>
         <owl:someValuesFrom>
             <owl:Class>
@@ -2418,26 +2437,26 @@
             </owl:Class>
         </owl:someValuesFrom>
     </owl:Restriction>
-    <owl:Restriction rdf:nodeID="genid316">
+    <owl:Restriction rdf:nodeID="genid318">
         <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0002162"/>
         <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_7215"/>
     </owl:Restriction>
     <owl:Axiom>
         <owl:annotatedSource rdf:resource="http://purl.obolibrary.org/obo/GO_0002224"/>
         <owl:annotatedProperty rdf:resource="http://www.w3.org/2000/01/rdf-schema#subClassOf"/>
-        <owl:annotatedTarget rdf:nodeID="genid310"/>
+        <owl:annotatedTarget rdf:nodeID="genid312"/>
         <oboInOwl:source>PMID:30034391</oboInOwl:source>
     </owl:Axiom>
     <owl:Axiom>
         <owl:annotatedSource rdf:resource="http://purl.obolibrary.org/obo/GO_0002224"/>
         <owl:annotatedProperty rdf:resource="http://www.w3.org/2000/01/rdf-schema#subClassOf"/>
-        <owl:annotatedTarget rdf:nodeID="genid313"/>
+        <owl:annotatedTarget rdf:nodeID="genid315"/>
         <oboInOwl:source>PMID:30034391</oboInOwl:source>
     </owl:Axiom>
     <owl:Axiom>
         <owl:annotatedSource rdf:resource="http://purl.obolibrary.org/obo/GO_0002224"/>
         <owl:annotatedProperty rdf:resource="http://www.w3.org/2002/07/owl#disjointWith"/>
-        <owl:annotatedTarget rdf:nodeID="genid316"/>
+        <owl:annotatedTarget rdf:nodeID="genid318"/>
         <oboInOwl:source>PMID:30034391</oboInOwl:source>
     </owl:Axiom>
     <owl:Axiom>
@@ -3129,27 +3148,27 @@
     <!-- http://purl.obolibrary.org/obo/GO_0004164 -->
 
     <owl:Class rdf:about="http://purl.obolibrary.org/obo/GO_0004164">
-        <rdfs:subClassOf rdf:nodeID="genid416"/>
         <rdfs:subClassOf rdf:nodeID="genid418"/>
+        <rdfs:subClassOf rdf:nodeID="genid420"/>
     </owl:Class>
-    <owl:Restriction rdf:nodeID="genid416">
+    <owl:Restriction rdf:nodeID="genid418">
         <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0002160"/>
         <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_2157"/>
     </owl:Restriction>
-    <owl:Restriction rdf:nodeID="genid418">
+    <owl:Restriction rdf:nodeID="genid420">
         <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0002162"/>
         <owl:allValuesFrom rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_2157"/>
     </owl:Restriction>
     <owl:Axiom>
         <owl:annotatedSource rdf:resource="http://purl.obolibrary.org/obo/GO_0004164"/>
         <owl:annotatedProperty rdf:resource="http://www.w3.org/2000/01/rdf-schema#subClassOf"/>
-        <owl:annotatedTarget rdf:nodeID="genid416"/>
+        <owl:annotatedTarget rdf:nodeID="genid418"/>
         <oboInOwl:source>PMID:24739148</oboInOwl:source>
     </owl:Axiom>
     <owl:Axiom>
         <owl:annotatedSource rdf:resource="http://purl.obolibrary.org/obo/GO_0004164"/>
         <owl:annotatedProperty rdf:resource="http://www.w3.org/2000/01/rdf-schema#subClassOf"/>
-        <owl:annotatedTarget rdf:nodeID="genid418"/>
+        <owl:annotatedTarget rdf:nodeID="genid420"/>
         <oboInOwl:source>PMID:24739148</oboInOwl:source>
     </owl:Axiom>
     
@@ -3692,27 +3711,27 @@
     <!-- http://purl.obolibrary.org/obo/GO_0005581 -->
 
     <owl:Class rdf:about="http://purl.obolibrary.org/obo/GO_0005581">
-        <rdfs:subClassOf rdf:nodeID="genid494"/>
         <rdfs:subClassOf rdf:nodeID="genid496"/>
+        <rdfs:subClassOf rdf:nodeID="genid498"/>
     </owl:Class>
-    <owl:Restriction rdf:nodeID="genid494">
+    <owl:Restriction rdf:nodeID="genid496">
         <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0002160"/>
         <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_33208"/>
     </owl:Restriction>
-    <owl:Restriction rdf:nodeID="genid496">
+    <owl:Restriction rdf:nodeID="genid498">
         <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0002162"/>
         <owl:allValuesFrom rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_33208"/>
     </owl:Restriction>
     <owl:Axiom>
         <owl:annotatedSource rdf:resource="http://purl.obolibrary.org/obo/GO_0005581"/>
         <owl:annotatedProperty rdf:resource="http://www.w3.org/2000/01/rdf-schema#subClassOf"/>
-        <owl:annotatedTarget rdf:nodeID="genid494"/>
+        <owl:annotatedTarget rdf:nodeID="genid496"/>
         <oboInOwl:source>PMID:12382326</oboInOwl:source>
     </owl:Axiom>
     <owl:Axiom>
         <owl:annotatedSource rdf:resource="http://purl.obolibrary.org/obo/GO_0005581"/>
         <owl:annotatedProperty rdf:resource="http://www.w3.org/2000/01/rdf-schema#subClassOf"/>
-        <owl:annotatedTarget rdf:nodeID="genid496"/>
+        <owl:annotatedTarget rdf:nodeID="genid498"/>
         <oboInOwl:source>PMID:12382326</oboInOwl:source>
     </owl:Axiom>
     
@@ -4763,7 +4782,7 @@
     <!-- http://purl.obolibrary.org/obo/GO_0006097 -->
 
     <owl:Class rdf:about="http://purl.obolibrary.org/obo/GO_0006097">
-        <rdfs:subClassOf rdf:nodeID="genid642"/>
+        <rdfs:subClassOf rdf:nodeID="genid644"/>
         <rdfs:subClassOf>
             <owl:Class>
                 <owl:complementOf>
@@ -4774,8 +4793,8 @@
                 </owl:complementOf>
             </owl:Class>
         </rdfs:subClassOf>
-        <rdfs:subClassOf rdf:nodeID="genid647"/>
-        <rdfs:subClassOf rdf:nodeID="genid650"/>
+        <rdfs:subClassOf rdf:nodeID="genid649"/>
+        <rdfs:subClassOf rdf:nodeID="genid652"/>
         <rdfs:subClassOf>
             <owl:Restriction>
                 <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0002162"/>
@@ -4786,20 +4805,20 @@
                 </owl:someValuesFrom>
             </owl:Restriction>
         </rdfs:subClassOf>
-        <rdfs:subClassOf rdf:nodeID="genid655"/>
... (2824 more lines truncated)
```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | opencode | 0.553 | 0.458 | 0.698 | `d8cfeac` | [#164](https://github.com/ai4curation/eval-ont-agent-go/pull/164) | [attempt](attempts/pr164.md) |
| 2 | gpt-5.5 | opencode | 0.553 | 0.458 | 0.698 | `d8cfeac` | [#146](https://github.com/ai4curation/eval-ont-agent-go/pull/146) | [attempt](attempts/pr146.md) |
| 3 | gpt-5.4 | opencode | 0.552 | 0.457 | 0.697 | `35156a4` | [#651](https://github.com/ai4curation/eval-ont-agent-go/pull/651) | [attempt](attempts/pr651.md) |
| 4 | gpt-5.4 | opencode | 0.552 | 0.457 | 0.697 | `35156a4` | [#602](https://github.com/ai4curation/eval-ont-agent-go/pull/602) | [attempt](attempts/pr602.md) |
| 5 | gpt-5.5 | codex | 0.552 | 0.457 | 0.697 | `d1745c1` | [#130](https://github.com/ai4curation/eval-ont-agent-go/pull/130) | [attempt](attempts/pr130.md) |
| 6 | gpt-5.4 | codex | 0.540 | 0.464 | 0.647 | `59f8ff4` | [#185](https://github.com/ai4curation/eval-ont-agent-go/pull/185) | [attempt](attempts/pr185.md) |
| 7 | claude-sonnet-4.5 | claude | 0.016 | 0.008 | 0.800 | `cf80bf7` | [#454](https://github.com/ai4curation/eval-ont-agent-go/pull/454) | [attempt](attempts/pr454.md) |
| 8 | claude-sonnet-4.5 | copilot | 0.016 | 0.008 | 0.800 | `cf80bf7` | [#377](https://github.com/ai4curation/eval-ont-agent-go/pull/377) | [attempt](attempts/pr377.md) |
| 9 | claude-opus-4.7 | claude | 0.016 | 0.008 | 0.800 | `d1745c1` | [#343](https://github.com/ai4curation/eval-ont-agent-go/pull/343) | [attempt](attempts/pr343.md) |
| 10 | kimi-k2.6 | opencode | 0.016 | 0.008 | 0.800 | `cf80bf7` | [#258](https://github.com/ai4curation/eval-ont-agent-go/pull/258) | [attempt](attempts/pr258.md) |
| 11 | gemma-4-31b | opencode | 0.016 | 0.008 | 0.800 | `cf80bf7` | [#244](https://github.com/ai4curation/eval-ont-agent-go/pull/244) | [attempt](attempts/pr244.md) |
| 12 | claude-haiku-4.5 | claude | 0.016 | 0.008 | 0.800 | `72b55e6` | [#201](https://github.com/ai4curation/eval-ont-agent-go/pull/201) | [attempt](attempts/pr201.md) |
