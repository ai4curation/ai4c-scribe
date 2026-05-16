---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3409
pr_number: 3466
issue_title: What relation should link a life stage term to its taxon-specific counterpart?
pr_author: gouttegd
pr_merged_at: '2025-01-30'
task_type: other
difficulty: hard
scoping: mostly_scoped
scope: structural_refactor
review_outcome: approved_first_time
num_agent_attempts: 5
generated_at: '2026-05-15'
domain_area: cross-species-bridging
best_f1: 1.0
best_model: claude-opus-4.7
---

# PR #3466 — What relation should link a life stage term to its taxon-specific counterpart?

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3409](https://github.com/obophenotype/uberon/issues/3409) | [PR #3466](https://github.com/obophenotype/uberon/pull/3466) | @gouttegd | merged 2025-01-30

`other` `hard` `mostly_scoped` `approved_first_time`

## Context

Issues #3409 and #3378 discussed the correct axiom pattern for linking taxon-specific anatomy terms (e.g., FBbt terms for Drosophila) to their Uberon counterparts in cross-species bridge ontologies. The existing single-axiom pattern using part_of/occurs_in had been intended as temporary. The original design called for a two-axiom form using in_taxon for the equivalence and a separate SubClassOf for the part_of/occurs_in relationship.

## Changes Made

The PR updated the bridging pipeline in src/scripts/taxa.py and src/ontology/config/taxa.yaml to generate two-axiom bridge patterns instead of single-axiom ones. For continuants, this means generating both an EquivalentTo axiom using in_taxon and a SubClassOf using part_of. For occurrents, the SubClassOf uses occurs_in instead. The Composite Metazoan pipeline was updated to unfold over in_taxon. Documentation in docs/bridges.md and docs/combined_multispecies.md was updated accordingly. The RO import was extended with the in_taxon relation.

## Resolution

Hard difficulty. An agent would need to understand the cross-species bridge ontology architecture, the difference between in_taxon and part_of/occurs_in semantics in OWL, and the Composite Metazoan build pipeline. The changes span five files including Python build scripts, YAML configuration, and documentation. This is infrastructure-level work that affects how all taxon-specific ontologies interoperate with Uberon.

## Human Diff

```diff
diff --git a/docs/bridges.md b/docs/bridges.md
index fe21fc63dd..13f47f3c88 100644
--- a/docs/bridges.md
+++ b/docs/bridges.md
@@ -8,14 +8,14 @@ Uberon term and a term from the foreign ontology.
 For example, the `uberon-bridge-to-zfa` bridge contains axioms such as
 this one:
 
-> ZFA:0001262 EquivalentTo: UBERON:0005564 and (BFO:0000050 some NCBITaxon:7954)
+> ZFA:0001262 EquivalentTo: UBERON:0005564 and (RO:0002162 some NCBITaxon:7954)
 
 which states that ZFA’s [gonad
 primordium](http://purl.obolibrary.org/obo/ZFA_0001262) (ZFA:0001262) is
 equivalent to a Uberon’s [gonad
 primordium](http://purl.obolibrary.org/obo/UBERON_0005564)
-(UBERON:0005564) that is [part
-of](http://purl.obolibrary.org/obo/BFO_0000050) a
+(UBERON:0005564) that is [in
+taxon](http://purl.obolibrary.org/obo/RO_0002162) some
 [Danio](http://purl.obolibrary.org/obo/NCBITaxon_7954) (NCBITaxon:7954).
 
 Such a bridge may be used by anyone who wants to merge Uberon and ZFA to
diff --git a/docs/combined_multispecies.md b/docs/combined_multispecies.md
index b7efe76a12..415758d241 100644
--- a/docs/combined_multispecies.md
+++ b/docs/combined_multispecies.md
@@ -113,7 +113,7 @@ that `collected-drosophila` contains the following axiom (provided by the
 bridge between Uberon and FBbt):
 
 ```
-FBbt:00004865 EquivalentTo: UBERON:0000992 and (part_of some NCBITaxon:7227)
+FBbt:00004865 EquivalentTo: UBERON:0000992 and (in_taxon some NCBITaxon:7227)
 ```
 
 (`NCBITaxon:7227` being the identifier for the _Drosophila melanogaster_
@@ -132,7 +132,7 @@ FBbt:00004911 SubClassOf: continuous_with some FBbt:00004865
 gets rewritten as
 
 ```
-FBbt:00004911 SubClassOf: continous_with some (UBERON:00009992 and (part_of some NCBITaxon:7227))
+FBbt:00004911 SubClassOf: continous_with some (UBERON:00009992 and (in_taxon some NCBITaxon:7227))
 ```
 
 The figure below illustrates the resulting differences between a
diff --git a/src/ontology/config/taxa.yaml b/src/ontology/config/taxa.yaml
index b628b1e756..a2256ae221 100644
--- a/src/ontology/config/taxa.yaml
+++ b/src/ontology/config/taxa.yaml
@@ -1,8 +1,7 @@
 defaults:
   compositing:
     unfold_over:
-      - BFO:0000050
-      - BFO:0000066
+      - RO:0002162
 species:
   - taxon_id: NCBITaxon:9606
     label: human
diff --git a/src/ontology/imports/ro_terms.txt b/src/ontology/imports/ro_terms.txt
index 4854fe8d45..3b30ff6b9a 100644
--- a/src/ontology/imports/ro_terms.txt
+++ b/src/ontology/imports/ro_terms.txt
@@ -1,4 +1,5 @@
 BFO:0000050
+RO:0002012
 RO:0002202
 RO:0002158
 RO:0002476
diff --git a/src/scripts/taxa.py b/src/scripts/taxa.py
index d56b657c3b..9a9b9ba1d2 100644
--- a/src/scripts/taxa.py
+++ b/src/scripts/taxa.py
@@ -65,11 +65,17 @@ def generate_bridging_rules(f, taxa):
             f.write(f"""
 [{name}-uberon] subject=={prefix}:* object==UBERON:* {{
     predicate==* -> annotate(%{{subject_id}}, IAO:0000589, "%{{object_label}} ({label})");
-    predicate==semapv:crossSpeciesExactMatch -> create_axiom("%subject_id EquivalentTo: %object_id and (%TAXREL some {taxon_id})");
+    predicate==semapv:crossSpeciesExactMatch -> {{
+        create_axiom("%subject_id EquivalentTo: %object_id and (RO:0002162 some {taxon_id})");
+        create_axiom("%subject_id SubClassOf: %TAXREL some {taxon_id}");
+    }}
 }}
 [{name}-cl] subject=={prefix}:* object==CL:* {{
     predicate==* -> annotate(%{{subject_id}}, IAO:0000589, "%{{object_label}} ({label})");
-    predicate==semapv:crossSpeciesExactMatch -> create_axiom("%subject_id EquivalentTo: %object_id and (%TAXREL some {taxon_id})");
+    predicate==semapv:crossSpeciesExactMatch -> {{
+        create_axiom("%subject_id EquivalentTo: %object_id and (RO:0002162 some {taxon_id})");
+        create_axiom("%subject_id SubClassOf: %TAXREL some {taxon_id}");
+    }}
 }}
 """)
 

```

## Agent Attempts (5)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 1.000 | 1.000 | 1.000 | `13f47f3` | [#235](https://github.com/ai4curation/eval-ont-agent-uberon/pull/235) | [attempt](attempts/pr235.md) |
| 2 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `995a97d` | [#290](https://github.com/ai4curation/eval-ont-agent-uberon/pull/290) | [attempt](attempts/pr290.md) |
| 3 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `2fc7700` | [#280](https://github.com/ai4curation/eval-ont-agent-uberon/pull/280) | [attempt](attempts/pr280.md) |
| 4 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `d953654` | [#194](https://github.com/ai4curation/eval-ont-agent-uberon/pull/194) | [attempt](attempts/pr194.md) |
| 5 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `2fc7700` | [#161](https://github.com/ai4curation/eval-ont-agent-uberon/pull/161) | [attempt](attempts/pr161.md) |
