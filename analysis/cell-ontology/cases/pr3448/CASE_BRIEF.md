---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3447
pr_number: 3448
issue_title: improve definition of Islands of Calleja granule cell
pr_author: app/copilot-swe-agent
pr_merged_at: '2025-11-20'
task_type: other
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 9
generated_at: '2026-05-17'
domain_area: neuroscience
best_f1: 0.522
best_model: claude-sonnet-4.5
---

# PR #3448 — improve definition of Islands of Calleja granule cell

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3447](https://github.com/obophenotype/cell-ontology/issues/3447) | [PR #3448](https://github.com/obophenotype/cell-ontology/pull/3448) | @app/copilot-swe-agent | merged 2025-11-20

`other` `medium` `tightly_scoped` `changes_requested`

## Context

The Islands of Calleja granule cell (CL_4030053) had an incomplete definition and a label that did not follow CL naming conventions. Issue #3447 requested an improved textual definition that better captures the GABAergic nature of this cell type and its anatomical localization, complementing the broader label correction effort tracked in issue #3321.

## Changes Made

Updated `cl-edit.owl` with a corrected label, expanded textual definition referencing the GABAergic classification, and added a subClassOf axiom linking CL_4030053 to the GABAergic neuron hierarchy. Minor adjustments were also made to the HRA subset component file. The net change was 6 additions and 4 deletions in the edit file.

## Resolution

The PR went through one round of changes_requested review before being approved and merged. Medium difficulty because the change required domain knowledge about the neurochemical identity of Islands of Calleja granule cells and correct placement within the GABAergic neuron subhierarchy, beyond a simple text edit.

## Curation Note (data quality)

Flagged `case_quality: poor` (reason `gold_has_out_of_scope_extras_and_provenance`) by claude-opus-4.7 on 2026-05-16.

This issue (#3447) is an unusually well-specified transcription task: it gives the exact target label, the verbatim definition text, the two PMIDs to add, an explicit instruction to retain existing references, and a request for a "GABAergic neuron" axiom. It was resolved by the **single** PR #3448 (no companion PRs; #3321 is only a broad "Basal Ganglion product EPIC" tracking issue, still open). Step 3a does not apply.

However the metadiff F1 (0.429–0.522 across all 6 attempts, precision pinned at 0.375) **systematically under-represents** quality because the gold diff contains material the issue never requested and that an agent editing `cl-edit.owl` cannot/should not reproduce:

1. **Author provenance**: gold adds `AnnotationAssertion(terms:contributor obo:CL_4030053 "https://orcid.org/0000-0002-5507-2103")` — the original copilot PR author's ORCID. Not requested; no agent could produce the correct human ORCID.
2. **Unrelated foreign edit**: gold changes the annotation-property comment at line ~3638 from `# Annotation Property: oboInOwl:hasDbXref (database_cross_reference)` to `(has cross-reference)` — a serialization/comment-regeneration artifact wholly unrelated to CL_4030053.
3. **Auto-generated component churn**: the `hra_subset.owl` hunks (OWL API version string `4.5.29` → `4.5.29.2024-05-13T12:11:03Z`, a stray whitespace line, collapse of the CL_4030053 HRA `owl:Class` block) are pipeline-generated artifacts, not authored edits responsive to the issue.

Net issue-relevant gold content in `cl-edit.owl` is exactly: plural label, verbatim definition, three xrefs (retained DOI + 2 new PMIDs), and `SubClassOf(CL_4030053 CL_0000617)`. **All six attempts reproduced this substantive core.** Substance-based grading:

- **pr72 / pr52** (gpt-5.5/opencode, blob `26c8a14`): cleanest — honored "do not replace existing" by retaining the DOI xref and adding both PMIDs; correct label + GABAergic parent; only defensible extras (IAO_0000233 tracker, CPNE4 comment plural tidy). `success`.
- **pr35** (gpt-5.5/codex), **pr78** (gpt-5.4/codex): correct core + retained DOI; paraphrased definition, IAO_0000233 tracker, EOF newline artifact; pr78 also paraphrased the CPNE4 comment losing the explicit subject. `success`.
- **pr227** (claude-sonnet-4.5): used the issue's verbatim definition text (best fidelity) and was the most tightly scoped, but **dropped the existing DOI xref**, violating the explicit "do not replace the existing ones". `partial_success`.
- **pr98** (claude-haiku-4.5): correct core but **dropped the DOI xref** and additionally **clobbered `terms:date`** (2023-06-14 → 2026-05-10), damaging provenance. `partial_success`.

Downstream scoring/aggregation should down-weight or exclude this case's F1, or re-score against the issue's explicit asks rather than the line-level gold diff.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 88c721ae8..51d0f7774 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3638,7 +3638,7 @@ AnnotationAssertion(rdfs:label oboInOwl:consider "consider")
 
 AnnotationAssertion(rdfs:label oboInOwl:hasBroadSynonym "has_broad_synonym")
 
-# Annotation Property: oboInOwl:hasDbXref (database_cross_reference)
+# Annotation Property: oboInOwl:hasDbXref (has cross-reference)
 
 AnnotationAssertion(rdfs:label oboInOwl:hasDbXref "database_cross_reference")
 
@@ -31938,14 +31938,16 @@ SubClassOf(obo:CL_4030052 obo:CL_1001474)
 SubClassOf(obo:CL_4030052 ObjectSomeValuesFrom(obo:RO_0002100 obo:UBERON_0005403))
 SubClassOf(obo:CL_4030052 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000001177))
 
-# Class: obo:CL_4030053 (Island of Calleja granule cell)
+# Class: obo:CL_4030053 (Islands of Calleja granule cell)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "doi:10.1016/j.cub.2021.10.015") obo:IAO_0000115 obo:CL_4030053 "A DRD1-expressing, medium spiny neuron-like granule cell that is part of an Island of Calleja.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:34795450") Annotation(oboInOwl:hasDbXref "PMID:37898623") Annotation(oboInOwl:hasDbXref "doi:10.1016/j.cub.2021.10.015") obo:IAO_0000115 obo:CL_4030053 "A GABAergic neuron that resides in the islands of calleja and shows the cytoarchitectural and molecular features characteristic of this granule-like cell population. In mice and primates, it expresses D1 and D3 dopamine receptors (Drd1; Drd3), GABAergic markers (GAD1/2) and form densely packed granule cell clusters in the olfactory tubercle within the ventral striatum. Moreover it receives dense dopaminergic input from the VTA, and functionally associated with self-grooming behaviors and depression-like behaviors.")
+AnnotationAssertion(terms:contributor obo:CL_4030053 "https://orcid.org/0000-0002-5507-2103")
 AnnotationAssertion(terms:date obo:CL_4030053 "2023-06-14T13:37:45Z"^^xsd:dateTime)
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "doi:10.1016/j.cub.2021.10.015") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_4030053 "D1-ICj")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "doi:10.1016/j.cub.2021.10.015") rdfs:comment obo:CL_4030053 "In Rhesus macaques, the Island of Calleja granule cell type has been noted to have enriched gene expression of CPNE4.")
-AnnotationAssertion(rdfs:label obo:CL_4030053 "Island of Calleja granule cell")
+AnnotationAssertion(rdfs:label obo:CL_4030053 "Islands of Calleja granule cell")
 SubClassOf(obo:CL_4030053 obo:CL_0000120)
+SubClassOf(obo:CL_4030053 obo:CL_0000617)
 SubClassOf(obo:CL_4030053 ObjectSomeValuesFrom(obo:RO_0002100 ObjectIntersectionOf(obo:UBERON_0001881 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0005403))))
 SubClassOf(obo:CL_4030053 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000001175))
 
diff --git a/src/ontology/components/hra_subset.owl b/src/ontology/components/hra_subset.owl
index 10ac50c7c..8cf47ec60 100644
--- a/src/ontology/components/hra_subset.owl
+++ b/src/ontology/components/hra_subset.owl
@@ -1783,6 +1783,7 @@
         <obo:RO_0002175 rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_9606"/>
         <oboInOwl:inSubset rdf:resource="http://purl.obolibrary.org/obo/uberon/core#human_reference_atlas"/>
     </owl:Class>
+    
 
 
     <!-- http://purl.obolibrary.org/obo/CL_0002042 -->
@@ -4313,10 +4314,7 @@
 
     <!-- http://purl.obolibrary.org/obo/CL_4030053 -->
 
-    <owl:Class rdf:about="http://purl.obolibrary.org/obo/CL_4030053">
-        <obo:RO_0002175 rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_9606"/>
-        <oboInOwl:inSubset rdf:resource="http://purl.obolibrary.org/obo/uberon/core#human_reference_atlas"/>
-    </owl:Class>
+    <owl:Class rdf:about="http://purl.obolibrary.org/obo/CL_4030053"/>
     
 
 
@@ -4699,5 +4697,5 @@
 
 
 
-<!-- Generated by the OWL API (version 4.5.29) https://github.com/owlcs/owlapi -->
+<!-- Generated by the OWL API (version 4.5.29.2024-05-13T12:11:03Z) https://github.com/owlcs/owlapi -->
 

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.522 | 0.375 | 0.857 | `30e40d6` | [#227](https://github.com/ai4curation/eval-ont-agent-cl/pull/227) | [attempt](attempts/pr227.md) |
| 2 | claude-haiku-4.5 | claude | 0.500 | 0.375 | 0.750 | `3159b5d` | [#98](https://github.com/ai4curation/eval-ont-agent-cl/pull/98) | [attempt](attempts/pr98.md) |
| 3 | gpt-5.5 | opencode | 0.462 | 0.375 | 0.600 | `26c8a14` | [#72](https://github.com/ai4curation/eval-ont-agent-cl/pull/72) | [attempt](attempts/pr72.md) |
| 4 | gpt-5.5 | opencode | 0.462 | 0.375 | 0.600 | `26c8a14` | [#52](https://github.com/ai4curation/eval-ont-agent-cl/pull/52) | [attempt](attempts/pr52.md) |
| 5 | gpt-5.5 | codex | 0.462 | 0.375 | 0.600 | `f2beb64` | [#35](https://github.com/ai4curation/eval-ont-agent-cl/pull/35) | [attempt](attempts/pr35.md) |
| 6 | gpt-5.4 | opencode | 0.444 | 0.375 | 0.545 | `aa160ea` | [#572](https://github.com/ai4curation/eval-ont-agent-cl/pull/572) | [attempt](attempts/pr572.md) |
| 7 | claude-opus-4.7 | claude | 0.444 | 0.375 | 0.545 | `d07944b` | [#537](https://github.com/ai4curation/eval-ont-agent-cl/pull/537) | [attempt](attempts/pr537.md) |
| 8 | gpt-5.4 | opencode | 0.444 | 0.375 | 0.545 | `aa160ea` | [#510](https://github.com/ai4curation/eval-ont-agent-cl/pull/510) | [attempt](attempts/pr510.md) |
| 9 | gpt-5.4 | codex | 0.429 | 0.375 | 0.500 | `f33cb1d` | [#78](https://github.com/ai4curation/eval-ont-agent-cl/pull/78) | [attempt](attempts/pr78.md) |
