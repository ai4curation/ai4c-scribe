---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 10149
pr_number: 10156
issue_title: Request for new term [podocytopathy]
pr_author: sabrinatoro
pr_merged_at: '2026-04-15'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 11
generated_at: '2026-05-15'
scoping_notes: PR adds a new parent term and reclassifies three existing children
  under it.
domain_area: kidney-disease
best_f1: 0.476
best_model: gpt-5.5
---

# PR #10156 — Request for new term [podocytopathy]

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #10149](https://github.com/monarch-initiative/mondo/issues/10149) | [PR #10156](https://github.com/monarch-initiative/mondo/pull/10156) | @sabrinatoro | merged 2026-04-15

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A request was made for a new term "podocytopathy" to serve as a grouping class for diseases caused by podocyte dysfunction. Podocytes are specialized cells in the kidney glomerulus, and podocytopathies include conditions like minimal change disease and focal segmental glomerulosclerosis. The term was needed to provide a clinically meaningful grouping in the disease hierarchy.

This was a collaborative effort with a domain expert (cws99) who helped define the scope and children of the new term.

## Changes Made

Added the new term "podocytopathy" to `src/ontology/mondo-edit.obo` with 17 lines of additions. The PR created the parent term with a definition and also reclassified three existing disease terms as children of the new grouping class. No lines were deleted, indicating clean additions to the hierarchy.

## Resolution

Medium difficulty because it requires understanding renal pathology well enough to determine which existing Mondo terms should be classified as podocytopathies. The curator needed to create a proper definition and identify the correct children, which requires domain knowledge about glomerular disease classification.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 3f4dea1042..54f9817370 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -115279,8 +115279,10 @@ xref: SCTID:197710000 {source="DOID:10976"}
 xref: SCTID:77182004 {source="EFO:0004254", source="DOID:10976", source="MONDO:equivalentTo"}
 xref: UMLS:C0017665 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:42231"}
 is_a: MONDO:0002462 {source="DOID:10976", source="MESH:D015433", source="NCIT:C34645"} ! glomerulonephritis
+is_a: MONDO:0700328 {source="PMID:41381622"} ! podocytopathy
 relationship: disease_has_location UBERON:0005777 ! glomerular basement membrane
 property_value: curated_content_resource "https://www.malacards.org/card/membranous_nephropathy" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10149" xsd:anyURI
 
 [Term]
 id: MONDO:0005377
@@ -149461,8 +149463,10 @@ xref: SCTID:197592009 {source="DOID:10966"}
 xref: SCTID:44785005 {source="EFO:1001020", source="DOID:10966", source="MONDO:equivalentTo"}
 xref: UMLS:C0027721 {source="MEDGEN:10307", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0002462 {source="DOID:10966", source="NCIT:C34844"} ! glomerulonephritis
+is_a: MONDO:0700328 {source="PMID:17699461", source="PMID:25684864", source="PMID:38804512", source="PMID:41381622"} ! podocytopathy
 relationship: excluded_subClassOf MONDO:0005377 {source="DOID:10966", source="https://orcid.org/0000-0001-5208-3432"} ! nephrotic syndrome
 property_value: curated_content_resource "https://www.malacards.org/card/lipoid_nephrosis" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10149" xsd:anyURI
 
 [Term]
 id: MONDO:0006836
@@ -583383,8 +583387,10 @@ xref: SCTID:236403004 {source="EFO:0004236", source="MONDO:equivalentTo", source
 xref: SCTID:25821008 {source="DOID:1312"}
 xref: UMLS:C0017668 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:4904"}
 is_a: MONDO:0000490 {source="DOID:1312"} ! glomerulosclerosis
+is_a: MONDO:0700328 {source="PMID:17699461", source="PMID:25684864", source="PMID:38804512", source="PMID:41381622"} ! podocytopathy
 property_value: curated_content_resource "https://www.malacards.org/card/focal_segmental_glomerulosclerosis" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5208-3432
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10149" xsd:anyURI
 
 [Term]
 id: MONDO:0100314
@@ -593048,6 +593054,17 @@ intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.o
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/6119 {source="PMID:29408330"} ! IRF4
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/8090" xsd:anyURI
 
+[Term]
+id: MONDO:0700328
+name: podocytopathy
+def: "A glomerular disorder caused by the structural or functional impairment of podocytes, which leads to proteinuria and often nephrotic syndrome." [https://orcid.org/0009-0009-0876-0331, PMID:17699461, PMID:25684864, PMID:32792490, PMID:38804512, PMID:41381622]
+xref: SCTID:1367669003 {source="MONDO:equivalentTo"}
+is_a: MONDO:0019722 {source="PMID:17699461", source="PMID:25684864", source="PMID:41381622"} ! glomerular disorder
+intersection_of: MONDO:0019722 ! glomerular disorder
+intersection_of: disease_has_location CL:0000653
+relationship: disease_has_location CL:0000653 {source="PMID:17699461", source="PMID:25684864", source="PMID:32792490", source="PMID:41381622"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10149" xsd:anyURI
+
 [Term]
 id: MONDO:0700330
 name: PTEN harmartoma tumor syndrome with immune disorder

```

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | gpt-5.5 | opencode | 0.476 | 0.417 | 0.556 | [#79](https://github.com/ai4curation/eval-ont-agent-mondo/pull/79) | [attempt](attempts/pr79.md) |
| 2 | gpt-5.5 | opencode | 0.476 | 0.417 | 0.556 | [#61](https://github.com/ai4curation/eval-ont-agent-mondo/pull/61) | [attempt](attempts/pr61.md) |
| 3 | gpt-5.4 | codex | 0.455 | 0.417 | 0.500 | [#155](https://github.com/ai4curation/eval-ont-agent-mondo/pull/155) | [attempt](attempts/pr155.md) |
| 4 | claude-sonnet-4.5 | copilot | 0.400 | 0.333 | 0.500 | [#527](https://github.com/ai4curation/eval-ont-agent-mondo/pull/527) | [attempt](attempts/pr527.md) |
| 5 | claude-sonnet-4.5 | copilot | 0.400 | 0.333 | 0.500 | [#498](https://github.com/ai4curation/eval-ont-agent-mondo/pull/498) | [attempt](attempts/pr498.md) |
| 6 | kimi-k2.6 | opencode | 0.400 | 0.333 | 0.500 | [#271](https://github.com/ai4curation/eval-ont-agent-mondo/pull/271) | [attempt](attempts/pr271.md) |
| 7 | claude-sonnet-4.5 | claude | 0.381 | 0.333 | 0.444 | [#451](https://github.com/ai4curation/eval-ont-agent-mondo/pull/451) | [attempt](attempts/pr451.md) |
| 8 | claude-opus-4.7 | claude | 0.381 | 0.333 | 0.444 | [#392](https://github.com/ai4curation/eval-ont-agent-mondo/pull/392) | [attempt](attempts/pr392.md) |
| 9 | claude-haiku-4.5 | claude | 0.364 | 0.333 | 0.400 | [#478](https://github.com/ai4curation/eval-ont-agent-mondo/pull/478) | [attempt](attempts/pr478.md) |
| 10 | claude-haiku-4.5 | claude | 0.364 | 0.333 | 0.400 | [#415](https://github.com/ai4curation/eval-ont-agent-mondo/pull/415) | [attempt](attempts/pr415.md) |
| 11 | gpt-5.5 | codex | 0.364 | 0.333 | 0.400 | [#42](https://github.com/ai4curation/eval-ont-agent-mondo/pull/42) | [attempt](attempts/pr42.md) |
