---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3259
pr_number: 3450
issue_title: '[NTR] tPC-IC cell'
pr_author: app/copilot-swe-agent
pr_merged_at: '2025-11-21'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 7
generated_at: '2026-05-15'
domain_area: renal
best_f1: 0.706
best_model: claude-haiku-4.5
---

# PR #3450 — [NTR] tPC-IC cell

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3259](https://github.com/obophenotype/cell-ontology/issues/3259) | [PR #3450](https://github.com/obophenotype/cell-ontology/pull/3450) | @app/copilot-swe-agent | merged 2025-11-21

`new_term` `medium` `tightly_scoped` `changes_requested`

## Context

A new term request was filed for the transitional principal-intercalated cell (tPC-IC), a recently described cell type in the kidney collecting duct that exhibits characteristics of both principal cells and intercalated cells. This cell type represents an intermediate state in the plasticity between these two well-established collecting duct cell populations. The issue had been open since August 2025 as part of ongoing kidney cell type curation.

## Changes Made

Added 14 new lines to `cl-edit.owl` defining the tPC-IC term with a class declaration, rdfs:label, textual definition with literature references, appropriate parentage, and logical axioms linking the cell to UBERON kidney collecting duct structures via part_of relations. One existing line was modified to accommodate the new term in the class hierarchy.

## Resolution

The PR required changes during review before approval and merge, going through 7 commits total. Medium difficulty because modeling a transitional cell state between two existing cell types requires careful consideration of the ontological relationship -- it is not simply a subclass of either parent type but represents a hybrid phenotype that needed appropriate axiomatization.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 51d0f7774..601768459 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3276,6 +3276,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -3638,7 +3639,7 @@ AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
 
 AnnotationAssertion(rdfs:label oboInOwl:hasBroadSynonym "has_broad_synonym")
 
-# Annotation Property: oboInOwl:hasDbXref (has cross-reference)
+# Annotation Property: oboInOwl:hasDbXref (database_cross_reference)
 
 AnnotationAssertion(rdfs:label oboInOwl:hasDbXref "database_cross_reference")
 
@@ -35268,6 +35269,18 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900001 (transitional principal-intercalated cell of kidney collecting duct)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") Annotation(oboInOwl:hasDbXref "PMID:37468583") obo:IAO_0000115 obo:CL_9900001 "A transitional cell located in the renal collecting duct that co-expresses markers of both principal cell (PC) and intercalated cell (IC). This hybrid cell is enriched in Chronic Kidney Disease (CKD).")
+AnnotationAssertion(dc:creator obo:CL_9900001 "GitHub Copilot")
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0000-0002-2999-0103>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") oboInOwl:hasBroadSynonym obo:CL_9900001 "hybrid principal-intercalated cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900001 "tPC-IC cell")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "transitional principal-intercalated cell of kidney collecting duct")
+SubClassOf(obo:CL_9900001 obo:CL_1000454)
+SubClassOf(obo:CL_9900001 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001232))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

## Agent Attempts (7)

### Attempt 1: claude-haiku-4.5 / claude

- **Eval PR**: [#91](https://github.com/ai4curation/eval-ont-agent-cl/pull/91)
- **F1**: 0.706  **Precision**: 0.545  **Recall**: 1.000  **Jaccard**: 0.545
- **Workflow run**: [25640370808](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640370808)

#### Agent PR Comment

# New Cell Type Addition: Transitional Principal-Intercalated Cell of Kidney Collecting Duct

## Summary

Added a new cell type to the Cell Ontology: **transitional principal-intercalated cell of kidney collecting duct** with ID **CL_9900001**. This term represents a hybrid kidney cell type that co-expresses markers of both principal cells (PC) and intercalated cells (IC), enriched in Chronic Kidney Disease (CKD) contexts.

## Changes Made

### New Term: CL_9900001

**Label:** transitional principal-intercalated cell of kidney collecting duct

**Definition:** A transitional cell located in the renal collecting duct that co-expresses markers of both principal cell (PC) and intercalated cell (IC). This hybrid cell is enriched in Chronic Kidney Disease (CKD).

**Parent Term:** CL_1000454 (kidney collecting duct epithelial cell)

**Synonyms:**
- "tPC-IC cell" - Related synonym (abbreviation) - PMID:37468583
- "hybrid principal-intercalated cell" - Broad synonym - PMID:33893305

**Anatomical Location:** UBERON_0001232 (collecting duct of renal tubule) - implicit via parent term

**Contributors:**
- https://orcid.org/0000-0002-2999-0103
- https://orcid.org/0009-0000-8480-9277

**Creation Date:** 2026-05-10

## Rationale

This term was requested to support HuBMap data annotation. The term describes a previously undescribed transitional cell state in the kidney collecting duct that exhibits characteristics of both principal and intercalated cells. This cell type is particularly enriched in Chronic Kidney Disease (CKD) contexts.

The definition and supporting references are based on the supplementary materials of the cited publications, which have been reviewed and confirmed to contain the necessary supporting information.

## Validation Checklist

- ✅ Used CL_99xxxxx format for new term ID as required
- ✅ Included definition with PMID references
- ✅ Established parent-child relationship with appropriate parent term (CL_1000454)
- ✅ Added synonyms with appropriate synonym types and PMID references
- ✅ Added contributor ORCIDs as Dublin Core terms:contributor annotations
- ✅ Added creation date annotation in ISO 8601 format
- ✅ Term label is consistent with cell ontology naming conventions
- ✅ No logical axioms created (following instruction that term should be simple SubClassOf parent)

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640370808)


#### Agent Issue Comment

## Status: New Term Added

The new term **transitional principal-intercalated cell of kidney collecting duct** (CL_9900001) has been successfully created and added to the ontology.

The term was created based on the specifications provided in the issue, with references to PMIDs 37468583 and 33893305 as supporting citations. The term includes both the abbreviated synonym "tPC-IC cell" and the broad synonym "hybrid principal-intercalated cell" with appropriate PMID annotations.

Both contributors listed in the issue have been credited as terms:contributor in the ontology entry.

Changes committed in PR #<NN>

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640370808)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 51d0f7774..2f08c39fa 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -35268,6 +35268,17 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900001 (transitional principal-intercalated cell of kidney collecting duct)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") Annotation(oboInOwl:hasDbXref "PMID:33893305") obo:IAO_0000115 obo:CL_9900001 "A transitional cell located in the renal collecting duct that co-expresses markers of both principal cell (PC) and intercalated cell (IC). This hybrid cell is enriched in Chronic Kidney Disease (CKD).")
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-05-10T00:00:00Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900001 "tPC-IC cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") oboInOwl:hasBroadSynonym obo:CL_9900001 "hybrid principal-intercalated cell")
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0000-0002-2999-0103>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(rdfs:label obo:CL_9900001 "transitional principal-intercalated cell of kidney collecting duct")
+SubClassOf(obo:CL_9900001 obo:CL_1000454)
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

### Attempt 2: gpt-5.5 / opencode

- **Eval PR**: [#65](https://github.com/ai4curation/eval-ont-agent-cl/pull/65)
- **F1**: 0.696  **Precision**: 0.727  **Recall**: 0.667  **Jaccard**: 0.533
- **Trace**: [25615958754](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25615958754)
- **Workflow run**: [25615958754](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615958754)

#### Agent PR Comment

## Summary

Added a new CL term for issue #3259:

- `CL_9900001` transitional principal-intercalated cell of kidney collecting duct

## Changes made

- Added class declaration and term axioms in `src/ontology/cl-edit.owl`.
- Added a textual definition citing PMID:33893305 and PMID:37468583.
- Placed the term under `CL_1000454` kidney collecting duct epithelial cell.
- Added a `part_of` relationship to `UBERON_0001232` collecting duct of renal tubule.
- Added requested synonyms:
  - `tPC-IC cell` as a related abbreviation synonym, PMID:37468583
  - `hybrid principal-intercalated cell` as a broad synonym, PMID:33893305
  - `transitional principal-intercalated cell` as an exact synonym, PMID:37468583
- Added contributor ORCIDs from the issue.
- Added `terms:date`, `dc:creator`, and issue tracker metadata.
- Added a comment noting reported enrichment in chronic kidney disease.

## Rationale and checks

- Confirmed no existing CL term for `transitional principal-intercalated`, `principal-intercalated`, `tPC-IC`, or `hybrid principal-intercalated` was present in `src/ontology/cl-edit.owl`.
- Checked the requested parent `CL_1000454` and related collecting duct principal/intercalated cell terms for consistency.
- Used a new `CL_99xxxxx` identifier per the NTR ID range guidance.
- Validated OWL functional syntax with:
  - `robot convert --input src/ontology/cl-edit.owl --output /tmp/cl-edit-test.owl`

Signed-off-by: GitHub Copilot

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615958754)


#### Agent Issue Comment

Implemented in PR #<NN>.

Added the requested `transitional principal-intercalated cell of kidney collecting duct` term with supplied synonyms, references, collecting duct parentage, contributor ORCIDs, and issue tracker metadata.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615958754)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 51d0f7774..3623b1ab1 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3276,6 +3276,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35268,6 +35269,22 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900001 (transitional principal-intercalated cell of kidney collecting duct)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") Annotation(oboInOwl:hasDbXref "PMID:37468583") obo:IAO_0000115 obo:CL_9900001 "A kidney collecting duct epithelial cell that has a transitional identity and co-expresses markers of renal principal cells and renal intercalated cells.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900001 <https://github.com/obophenotype/cell-ontology/issues/3259>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0000-0002-2999-0103>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(dc:creator obo:CL_9900001 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-05-10T02:06:52Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") oboInOwl:hasBroadSynonym obo:CL_9900001 "hybrid principal-intercalated cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900001 "tPC-IC cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") oboInOwl:hasExactSynonym obo:CL_9900001 "transitional principal-intercalated cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") rdfs:comment obo:CL_9900001 "This hybrid collecting duct cell type is reported to be enriched in chronic kidney disease.")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "transitional principal-intercalated cell of kidney collecting duct")
+SubClassOf(obo:CL_9900001 obo:CL_1000454)
+SubClassOf(obo:CL_9900001 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001232))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

### Attempt 3: gpt-5.5 / opencode

- **Eval PR**: [#46](https://github.com/ai4curation/eval-ont-agent-cl/pull/46)
- **F1**: 0.696  **Precision**: 0.727  **Recall**: 0.667  **Jaccard**: 0.533
- **Trace**: [25615914741](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25615914741)
- **Workflow run**: [25615914741](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615914741)

#### Agent PR Comment

## Summary

Added `CL_9900001` transitional principal-intercalated cell of kidney collecting duct for issue #3259.

## Rationale

The new term represents the requested tPC-IC/hybrid principal-intercalated collecting duct epithelial cell. It is placed under `CL_1000454` kidney collecting duct epithelial cell and asserted as part of `UBERON_0001232` collecting duct of renal tubule, matching the requested parent and anatomical location.

The definition and synonyms cite the requested literature: `PMID:37468583` for tPC-IC/transitioning principal and intercalated cells in injured kidney, and `PMID:33893305` for hybrid principal-intercalated cells identified from single-cell transcriptomics.

## Checklist

- Checked `src/ontology/cl-edit.owl` for existing matching labels/synonyms before adding the term.
- Checked the proposed parent `CL_1000454` and existing collecting duct principal/intercalated cell patterns.
- Added definition, label, related abbreviation synonym, broad synonym, contributors, creator, date, tracker link, parent, and anatomical location.
- Attempted `aurelian fulltext` for both PMIDs; the command was not available in this environment.
- Reviewed PubMed/web content for both PMIDs to confirm support for the term and synonyms.
- Validated syntax with `robot convert -i src/ontology/cl-edit.owl -o /tmp/opencode/cl-edit-check.owl`.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615914741)


#### Agent Issue Comment

Added the requested transitional principal-intercalated cell of kidney collecting duct term. Changes committed in PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615914741)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 51d0f7774..3623b1ab1 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3276,6 +3276,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35268,6 +35269,22 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900001 (transitional principal-intercalated cell of kidney collecting duct)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") Annotation(oboInOwl:hasDbXref "PMID:37468583") obo:IAO_0000115 obo:CL_9900001 "A kidney collecting duct epithelial cell that has a transitional identity and co-expresses markers of renal principal cells and renal intercalated cells.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900001 <https://github.com/obophenotype/cell-ontology/issues/3259>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0000-0002-2999-0103>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(dc:creator obo:CL_9900001 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-05-10T02:06:52Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") oboInOwl:hasBroadSynonym obo:CL_9900001 "hybrid principal-intercalated cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900001 "tPC-IC cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") oboInOwl:hasExactSynonym obo:CL_9900001 "transitional principal-intercalated cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") rdfs:comment obo:CL_9900001 "This hybrid collecting duct cell type is reported to be enriched in chronic kidney disease.")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "transitional principal-intercalated cell of kidney collecting duct")
+SubClassOf(obo:CL_9900001 obo:CL_1000454)
+SubClassOf(obo:CL_9900001 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001232))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

### Attempt 4: gpt-5.5 / codex

- **Eval PR**: [#27](https://github.com/ai4curation/eval-ont-agent-cl/pull/27)
- **F1**: 0.636  **Precision**: 0.636  **Recall**: 0.636  **Jaccard**: 0.467
- **Trace**: [25615862468](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25615862468)
- **Workflow run**: [25615862468](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615862468)

#### Agent PR Comment

## Summary

Added a new CL term for issue #3259:

- `CL_9900001` transitional principal-intercalated cell of kidney collecting duct

The term is asserted as a subclass of `CL_1000454` kidney collecting duct epithelial cell and as part of `UBERON_0001232` collecting duct of renal tubule. It includes a definition with PMID xrefs, the requested related abbreviation synonym `tPC-IC cell`, the requested broad synonym `hybrid principal-intercalated cell`, contributor ORCIDs, date metadata, and a tracker link back to the issue.

#### Agent Issue Comment

Added the requested transitional principal-intercalated cell of kidney collecting duct term in PR #<NN>.

The new term includes the requested PMID-backed definition, synonyms, contributor ORCIDs, collecting duct epithelial parentage, and issue tracker link.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25615862468)

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 51d0f7774..85668d0e2 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3276,6 +3276,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900001))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35268,6 +35269,19 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900001 (transitional principal-intercalated cell of kidney collecting duct)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") Annotation(oboInOwl:hasDbXref "PMID:37468583") obo:IAO_0000115 obo:CL_9900001 "A kidney collecting duct epithelial cell that co-expresses markers of renal principal cells and renal intercalated cells, consistent with a transitional or hybrid identity between renal principal cells and renal intercalated cells.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900001 <https://github.com/obophenotype/cell-ontology/issues/3259>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0000-0002-2999-0103>)
+AnnotationAssertion(terms:contributor obo:CL_9900001 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:date obo:CL_9900001 "2026-05-10T00:50:25Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") oboInOwl:hasBroadSynonym obo:CL_9900001 "hybrid principal-intercalated cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900001 "tPC-IC cell")
+AnnotationAssertion(rdfs:label obo:CL_9900001 "transitional principal-intercalated cell of kidney collecting duct")
+SubClassOf(obo:CL_9900001 obo:CL_1000454)
+SubClassOf(obo:CL_9900001 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001232))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)
@@ -35347,4 +35361,4 @@ SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000945)) obo:CL_0000164)
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001264)) obo:CL_0000164)
 SubClassOf(Annotation(oboInOwl:hasDbXref <https://github.com/obophenotype/cell-ontology/issues/757>) ObjectIntersectionOf(obo:CL_0000540 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_7742)) ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000031))
-)
\ No newline at end of file
+)

```

### Attempt 5: claude-opus-4.7 / claude

- **Eval PR**: [#272](https://github.com/ai4curation/eval-ont-agent-cl/pull/272)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000

#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 51d0f7774..10f66ade5 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3276,6 +3276,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35268,6 +35269,20 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (transitional principal-intercalated cell of kidney collecting duct)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") Annotation(oboInOwl:hasDbXref "PMID:33893305") obo:IAO_0000115 obo:CL_9900000 "A transitional cell located in the renal collecting duct that co-expresses markers of both principal cell (PC) and intercalated cell (IC). This hybrid cell is enriched in Chronic Kidney Disease (CKD).")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900000 "https://github.com/obophenotype/cell-ontology/issues/3259")
+AnnotationAssertion(dc:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0000-0002-2999-0103>)
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-05-15T12:00:00Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") oboInOwl:hasBroadSynonym obo:CL_9900000 "hybrid principal-intercalated cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900000 "tPC-IC cell")
+AnnotationAssertion(rdfs:label obo:CL_9900000 "transitional principal-intercalated cell of kidney collecting duct")
+SubClassOf(obo:CL_9900000 obo:CL_1000454)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001232))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

### Attempt 6: claude-sonnet-4.5 / claude

- **Eval PR**: [#200](https://github.com/ai4curation/eval-ont-agent-cl/pull/200)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Trace**: [25877700574](https://github.com/ai4curation/eval-ont-agent-cl/tree/master/traces/25877700574)
- **Workflow run**: [25877700574](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877700574)

#### Agent PR Comment

## Summary

This PR adds a new cell type term to the Cell Ontology for transitional principal-intercalated cells found in the kidney collecting duct.

## Changes Made

### New Term: CL_9900000
**Label:** transitional principal-intercalated cell of kidney collecting duct

**Definition:** "A transitional cell located in the renal collecting duct that co-expresses markers of both principal cell (PC) and intercalated cell (IC). This hybrid cell is enriched in Chronic Kidney Disease (CKD)."

**Synonyms:**
- "tPC-IC cell" (related synonym, abbreviation) - PMID:37468583
- "hybrid principal-intercalated cell" (broad synonym) - PMID:33893305

**Hierarchy:**
- Parent: CL_1000454 (kidney collecting duct epithelial cell)
- Anatomical location: UBERON_0001232 (collecting duct of renal tubule) via BFO_0000050 (part_of)

**Metadata:**
- References: PMID:37468583, PMID:33893305
- Contributors: 
  - https://orcid.org/0000-0002-2999-0103
  - https://orcid.org/0009-0000-8480-9277
- Creator: GitHub Copilot
- Date: 2026-05-14T00:00:00Z

## Rationale

This term was requested to annotate HuBMAP data. The definition was provided by Dr. Sanjay Jain and is based on published literature characterizing this cell type.

The term represents a transitional/hybrid cell state that co-expresses markers of both principal cells (which regulate sodium and potassium balance) and intercalated cells (which regulate acid/base balance). This cell type is particularly relevant in the context of Chronic Kidney Disease.

## Validation

✓ Parent term CL_1000454 verified to exist
✓ Anatomical location UBERON_0001232 verified in use by related terms
✓ Term ID CL_9900000 assigned from the temporary ID range (9900000-9999999) as specified in cl-idranges.owl
✓ All required metadata included (definition, references, contributors, timestamp)
✓ Synonyms properly formatted with annotation types and references
✓ Logical axioms follow established patterns for similar kidney collecting duct cell types
✓ Both cited publications (PMID:37468583, PMID:33893305) support the definition

## Checklist
- [x] Term added with proper ID from temporary range (CL_99xxxxx)
- [x] Declaration added in correct location
- [x] Class definition with full annotations added
- [x] Definition includes proper references
- [x] Synonyms added with appropriate types and references
- [x] Parent relationship (SubClassOf) to CL_1000454 added
- [x] Location relationship (part_of UBERON_0001232) added
- [x] ORCID contributors credited
- [x] Timestamp added
- [x] Term follows OBO formatting conventions
- [x] Commit message properly formatted and signed

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877700574)


#### Agent Issue Comment

## Status Update

The new term for transitional principal-intercalated cell (tPC-IC) has been successfully added to the Cell Ontology.

**Term Details:**
- **ID:** CL_9900000
- **Label:** transitional principal-intercalated cell of kidney collecting duct
- **Parent:** kidney collecting duct epithelial cell (CL_1000454)
- **Location:** collecting duct of renal tubule (UBERON_0001232)

The term includes the definition and synonyms as requested, with proper citations to PMID:37468583 and PMID:33893305. Both ORCID contributors have been credited.

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25877700574)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 51d0f7774..cd6ae51c9 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3276,6 +3276,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35268,6 +35269,19 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (transitional principal-intercalated cell of kidney collecting duct)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") Annotation(oboInOwl:hasDbXref "PMID:33893305") obo:IAO_0000115 obo:CL_9900000 "A transitional cell located in the renal collecting duct that co-expresses markers of both principal cell (PC) and intercalated cell (IC). This hybrid cell is enriched in Chronic Kidney Disease (CKD).")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0000-0002-2999-0103>)
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(dc:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-05-14T00:00:00Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") oboInOwl:hasBroadSynonym obo:CL_9900000 "hybrid principal-intercalated cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900000 "tPC-IC cell")
+AnnotationAssertion(rdfs:label obo:CL_9900000 "transitional principal-intercalated cell of kidney collecting duct")
+SubClassOf(obo:CL_9900000 obo:CL_1000454)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001232))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

### Attempt 7: gpt-5.4 / codex

- **Eval PR**: [#82](https://github.com/ai4curation/eval-ont-agent-cl/pull/82)
- **F1**: 0.000  **Precision**: 0.000  **Recall**: 0.000  **Jaccard**: 0.000
- **Workflow run**: [25640319682](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640319682)

#### Agent PR Comment

Added a new CL term for the CKD-enriched transitional collecting-duct population described in the issue:

- `CL_9903259` `transitional principal-intercalated cell of kidney collecting duct`

Rationale:
- `PMID:37468583` supports the transitional principal-intercalated collecting-duct population and the abbreviation `tPC-IC cell`.
- `PMID:33893305` supports the broader hybrid wording `hybrid principal-intercalated cell`.
- I used a conservative ontology placement under `CL_1000454` `kidney collecting duct epithelial cell` plus `part_of` `UBERON_0001232` `collecting duct of renal tubule`.
- I did not classify the new term as both a principal cell and an intercalated cell, because the cited sources describe a transitional or hybrid state rather than a canonical fully committed instance of both classes.

Changes made:
- added definition xrefs to `PMID:37468583` and `PMID:33893305`
- added issue tracking annotation back to `https://github.com/obophenotype/cell-ontology/issues/3259`
- added requested contributors:
  - `https://orcid.org/0000-0002-2999-0103`
  - `https://orcid.org/0009-0000-8480-9277`
- added timestamp annotation
- added requested synonyms:
  - related synonym with abbreviation type: `tPC-IC cell`
  - broad synonym: `hybrid principal-intercalated cell`

Checks completed:
- confirmed the preferred label was not already present in `src/ontology/cl-edit.owl`
- confirmed the proposed parent `CL_1000454` exists
- reviewed existing collecting-duct principal and intercalated terms for local modeling consistency
- validated the edited ontology file with `robot convert -i src/ontology/cl-edit.owl -o /tmp/cl-edit.ofn`

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640319682)


#### Agent Issue Comment

Added the requested term locally and committed the ontology update for PR #<NN>.

New term: `CL_9903259` `transitional principal-intercalated cell of kidney collecting duct`

Included:
- definition with `PMID:37468583` and `PMID:33893305`
- requested synonyms and ORCID contributors
- parentage under `kidney collecting duct epithelial cell` with explicit collecting-duct location

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/cl-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-cl/actions/runs/25640319682)


#### Agent Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 51d0f7774..c91bfd7df 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -35268,6 +35268,20 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9903259 (transitional principal-intercalated cell of kidney collecting duct)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") Annotation(oboInOwl:hasDbXref "PMID:37468583") obo:IAO_0000115 obo:CL_9903259 "A kidney collecting duct epithelial cell that co-expresses markers of principal cells and intercalated cells and is enriched in chronic kidney disease.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9903259 <https://github.com/obophenotype/cell-ontology/issues/3259>)
+AnnotationAssertion(dc:creator obo:CL_9903259 "GitHub Copilot")
+AnnotationAssertion(terms:contributor obo:CL_9903259 <https://orcid.org/0000-0002-2999-0103>)
+AnnotationAssertion(terms:contributor obo:CL_9903259 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:date obo:CL_9903259 "2026-05-10T21:34:11Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:33893305") oboInOwl:hasBroadSynonym obo:CL_9903259 "hybrid principal-intercalated cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:37468583") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9903259 "tPC-IC cell")
+AnnotationAssertion(rdfs:label obo:CL_9903259 "transitional principal-intercalated cell of kidney collecting duct")
+SubClassOf(obo:CL_9903259 obo:CL_1000454)
+SubClassOf(obo:CL_9903259 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001232))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)
@@ -35347,4 +35361,4 @@ SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000945)) obo:CL_0000164)
 SubClassOf(ObjectIntersectionOf(obo:CL_0000163 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001264)) obo:CL_0000164)
 SubClassOf(Annotation(oboInOwl:hasDbXref <https://github.com/obophenotype/cell-ontology/issues/757>) ObjectIntersectionOf(obo:CL_0000540 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_7742)) ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000031))
-)
\ No newline at end of file
+)

```
