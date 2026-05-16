---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9937
pr_number: 10112
issue_title: NTR/KY
pr_author: katiermullen
pr_merged_at: '2026-04-02'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
scoping_notes: PR adds exactly one new disease term stanza.
domain_area: rare-disease
best_f1: 0.609
best_model: claude-sonnet-4.5
---

# PR #10112 — NTR/KY

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9937](https://github.com/monarch-initiative/mondo/issues/9937) | [PR #10112](https://github.com/monarch-initiative/mondo/pull/10112) | @katiermullen | merged 2026-04-02

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for KY-related neuromyopathy. The KY gene (kyphoscoliosis peptidase) is involved in muscle development and maintenance, and mutations cause a rare neuromyopathy phenotype. The request came through ClinGen's gene-disease curation workflow.

## Changes Made

Added a new term stanza to `src/ontology/mondo-edit.obo` with 15 lines. The term includes a definition, gene-disease logical axioms linking the disease to KY via germline mutation, classification under the neuromyopathy hierarchy, and appropriate ClinGen provenance annotations.

## Resolution

Medium difficulty as it follows the standard gene-disease new term pattern but requires determining the correct parent class (neuromyopathy vs myopathy vs neuropathy) based on the clinical phenotype. An agent would need to understand that neuromyopathy affects both nerve and muscle and classify accordingly.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb40..9326e393df 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -387232,6 +387232,7 @@ xref: MEDGEN:934678 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:617114 {source="DOID:0080098", source="MONDO:equivalentTo"}
 xref: UMLS:C4310711 {source="MEDGEN:934678", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018943 {source="DOID:0080098", source="MONDO:Redundant", source="OMIM:617114"} ! myofibrillar myopathy
+is_a: MONDO:1010194 {source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
 intersection_of: MONDO:0018943 ! myofibrillar myopathy
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="OMIM:617114"} ! KY
@@ -586707,6 +586708,8 @@ xref: MEDGEN:1798876 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:496686 {source="MONDO:equivalentTo"}
 xref: UMLS:C5567453 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1798876"}
 is_a: MONDO:0018943 {source="Orphanet:496686"} ! myofibrillar myopathy
+is_a: MONDO:1010194 {source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
+relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 property_value: curated_content_resource "https://www.malacards.org/card/kyphosis_lateral_tongue_atrophy_myofibrillar_myopathy_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 
 [Term]
@@ -586727,6 +586730,7 @@ is_a: MONDO:0002254 {source="https://orcid.org/0000-0002-5002-8648"} ! syndromic
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0002-5002-8648"} ! hereditary disease
 is_a: MONDO:0005071 {source="https://orcid.org/0000-0001-9310-0163"} ! nervous system disorder
 is_a: MONDO:0015150 {source="https://orcid.org/0000-0002-4142-7153"} ! complex hereditary spastic paraplegia
+is_a: MONDO:1010194 {source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphoscoliosis_lateral_tongue_atrophy_hereditary_spastic_paraplegia_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6752" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6877" xsd:anyURI
@@ -636114,6 +636118,17 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9878" xsd:anyURI
 
+[Term]
+id: MONDO:1010194
+name: KY-related neuromyopathy
+def: "Any neuromyopathy in which the cause of the disease is mutation in the KY gene." [https://clinicalgenome.org/affiliation/40151/, https://orcid.org/0000-0002-2078-7280, PMID:27484770, PMID:27485408, PMID:28488683, PMID:32818658]
+synonym: "KY-related neuromyopathy" EXACT [https://clinicalgenome.org/affiliation/40151/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0100546 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! hereditary neuromuscular disease
+intersection_of: MONDO:0100546 ! hereditary neuromuscular disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
+
 [Term]
 id: MONDO:1010195
 name: myopathy, non-human animal

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.609 | 0.583 | 0.636 | [#439](https://github.com/ai4curation/eval-ont-agent-mondo/pull/439) | [attempt](attempts/pr439.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.583 | 0.583 | 0.583 | [#532](https://github.com/ai4curation/eval-ont-agent-mondo/pull/532) | [attempt](attempts/pr532.md) |
| 3 | claude-sonnet-4.5 | copilot | 0.583 | 0.583 | 0.583 | [#491](https://github.com/ai4curation/eval-ont-agent-mondo/pull/491) | [attempt](attempts/pr491.md) |
| 4 | claude-opus-4.7 | claude | 0.571 | 0.667 | 0.500 | [#383](https://github.com/ai4curation/eval-ont-agent-mondo/pull/383) | [attempt](attempts/pr383.md) |
| 5 | kimi-k2.6 | opencode | 0.538 | 0.583 | 0.500 | [#268](https://github.com/ai4curation/eval-ont-agent-mondo/pull/268) | [attempt](attempts/pr268.md) |
| 6 | gpt-5.5 | opencode | 0.500 | 0.500 | 0.500 | [#75](https://github.com/ai4curation/eval-ont-agent-mondo/pull/75) | [attempt](attempts/pr75.md) |
| 7 | gpt-5.5 | opencode | 0.500 | 0.500 | 0.500 | [#56](https://github.com/ai4curation/eval-ont-agent-mondo/pull/56) | [attempt](attempts/pr56.md) |
| 8 | gpt-5.5 | codex | 0.500 | 0.500 | 0.500 | [#36](https://github.com/ai4curation/eval-ont-agent-mondo/pull/36) | [attempt](attempts/pr36.md) |
| 9 | gpt-5.4 | codex | 0.500 | 0.583 | 0.438 | [#20](https://github.com/ai4curation/eval-ont-agent-mondo/pull/20) | [attempt](attempts/pr20.md) |
