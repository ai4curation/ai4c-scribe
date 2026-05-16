# PR #10112 — NTR/KY

- **Ontology**: mondo
- **Repo**: monarch-initiative/mondo
- **Issue**: [#9937](https://github.com/monarch-initiative/mondo/issues/9937)
- **PR**: [#10112](https://github.com/monarch-initiative/mondo/pull/10112)
- **Author**: @katiermullen
- **Merged**: 2026-04-02
- **task_type**: new_term
- **difficulty**: medium
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: approved_first_time
- **scoping_notes**: PR adds exactly one new disease term stanza.

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

### Attempt 1: claude-sonnet-4.5 / claude

- **Eval PR**: [#439](https://github.com/ai4curation/eval-ont-agent-mondo/pull/439)
- **F1**: 0.609  **Precision**: 0.583  **Recall**: 0.636  **Jaccard**: 0.438
- **Trace**: [25867710906](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25867710906)
- **Workflow run**: [25867710906](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867710906)

#### Agent PR Comment

# New Term Request: KY-related neuromyopathy

#### Agent Issue Comment

Changes committed in PR #<NN>.

The new term **MONDO:7770012 (KY-related neuromyopathy)** has been created and is now the parent of the three existing terms as requested:
- MONDO:0014922 "myofibrillar myopathy 7"
- MONDO:0044648 "kyphoscoliosis-lateral tongue atrophy-hereditary spastic paraplegia syndrome"
- MONDO:0044647 "kyphosis-lateral tongue atrophy-myofibrillar myopathy syndrome"

The term will be available in the next MONDO release.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867710906)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..6e134396a 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -387232,6 +387232,7 @@ xref: MEDGEN:934678 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:617114 {source="DOID:0080098", source="MONDO:equivalentTo"}
 xref: UMLS:C4310711 {source="MEDGEN:934678", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018943 {source="DOID:0080098", source="MONDO:Redundant", source="OMIM:617114"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
 intersection_of: MONDO:0018943 ! myofibrillar myopathy
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="OMIM:617114"} ! KY
@@ -586707,6 +586708,7 @@ xref: MEDGEN:1798876 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:496686 {source="MONDO:equivalentTo"}
 xref: UMLS:C5567453 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1798876"}
 is_a: MONDO:0018943 {source="Orphanet:496686"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphosis_lateral_tongue_atrophy_myofibrillar_myopathy_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 
 [Term]
@@ -586727,6 +586729,7 @@ is_a: MONDO:0002254 {source="https://orcid.org/0000-0002-5002-8648"} ! syndromic
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0002-5002-8648"} ! hereditary disease
 is_a: MONDO:0005071 {source="https://orcid.org/0000-0001-9310-0163"} ! nervous system disorder
 is_a: MONDO:0015150 {source="https://orcid.org/0000-0002-4142-7153"} ! complex hereditary spastic paraplegia
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphoscoliosis_lateral_tongue_atrophy_hereditary_spastic_paraplegia_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6752" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6877" xsd:anyURI
@@ -665382,6 +665385,17 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: KY-related neuromyopathy
+def: "Any neuromyopathy in which the cause of the disease is a mutation in the KY gene." [https://clinicalgenome.org/affiliation/40151/, PMID:27484770, PMID:27485408, PMID:28488683, PMID:32818658]
+is_a: MONDO:0100546 {source="https://clinicalgenome.org/affiliation/40151/"} ! hereditary neuromuscular disease
+intersection_of: MONDO:0100546 ! hereditary neuromuscular disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658"} ! KY
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-2078-7280
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 2: claude-sonnet-4.5 / copilot

- **Eval PR**: [#532](https://github.com/ai4curation/eval-ont-agent-mondo/pull/532)
- **F1**: 0.583  **Precision**: 0.583  **Recall**: 0.583  **Jaccard**: 0.412

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..e9d3ddd5f 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -387232,6 +387232,7 @@ xref: MEDGEN:934678 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:617114 {source="DOID:0080098", source="MONDO:equivalentTo"}
 xref: UMLS:C4310711 {source="MEDGEN:934678", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018943 {source="DOID:0080098", source="MONDO:Redundant", source="OMIM:617114"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 intersection_of: MONDO:0018943 ! myofibrillar myopathy
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="OMIM:617114"} ! KY
@@ -586707,6 +586708,7 @@ xref: MEDGEN:1798876 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:496686 {source="MONDO:equivalentTo"}
 xref: UMLS:C5567453 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1798876"}
 is_a: MONDO:0018943 {source="Orphanet:496686"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphosis_lateral_tongue_atrophy_myofibrillar_myopathy_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 
 [Term]
@@ -586727,6 +586729,7 @@ is_a: MONDO:0002254 {source="https://orcid.org/0000-0002-5002-8648"} ! syndromic
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0002-5002-8648"} ! hereditary disease
 is_a: MONDO:0005071 {source="https://orcid.org/0000-0001-9310-0163"} ! nervous system disorder
 is_a: MONDO:0015150 {source="https://orcid.org/0000-0002-4142-7153"} ! complex hereditary spastic paraplegia
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphoscoliosis_lateral_tongue_atrophy_hereditary_spastic_paraplegia_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6752" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6877" xsd:anyURI
@@ -665382,6 +665385,18 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: KY-related neuromyopathy
+def: "Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene." [PMID:27484770, PMID:27485408, PMID:28488683, PMID:32818658]
+subset: rare
+is_a: MONDO:0100546 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! hereditary neuromuscular disease
+intersection_of: MONDO:0100546 ! hereditary neuromuscular disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658"} ! KY
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-2078-7280
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 3: claude-sonnet-4.5 / copilot

- **Eval PR**: [#491](https://github.com/ai4curation/eval-ont-agent-mondo/pull/491)
- **F1**: 0.583  **Precision**: 0.583  **Recall**: 0.583  **Jaccard**: 0.412

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..e9d3ddd5f 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -387232,6 +387232,7 @@ xref: MEDGEN:934678 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:617114 {source="DOID:0080098", source="MONDO:equivalentTo"}
 xref: UMLS:C4310711 {source="MEDGEN:934678", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018943 {source="DOID:0080098", source="MONDO:Redundant", source="OMIM:617114"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 intersection_of: MONDO:0018943 ! myofibrillar myopathy
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="OMIM:617114"} ! KY
@@ -586707,6 +586708,7 @@ xref: MEDGEN:1798876 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:496686 {source="MONDO:equivalentTo"}
 xref: UMLS:C5567453 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1798876"}
 is_a: MONDO:0018943 {source="Orphanet:496686"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphosis_lateral_tongue_atrophy_myofibrillar_myopathy_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 
 [Term]
@@ -586727,6 +586729,7 @@ is_a: MONDO:0002254 {source="https://orcid.org/0000-0002-5002-8648"} ! syndromic
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0002-5002-8648"} ! hereditary disease
 is_a: MONDO:0005071 {source="https://orcid.org/0000-0001-9310-0163"} ! nervous system disorder
 is_a: MONDO:0015150 {source="https://orcid.org/0000-0002-4142-7153"} ! complex hereditary spastic paraplegia
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphoscoliosis_lateral_tongue_atrophy_hereditary_spastic_paraplegia_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6752" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6877" xsd:anyURI
@@ -665382,6 +665385,18 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: KY-related neuromyopathy
+def: "Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene." [PMID:27484770, PMID:27485408, PMID:28488683, PMID:32818658]
+subset: rare
+is_a: MONDO:0100546 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! hereditary neuromuscular disease
+intersection_of: MONDO:0100546 ! hereditary neuromuscular disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658"} ! KY
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-2078-7280
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 4: claude-opus-4.7 / claude

- **Eval PR**: [#383](https://github.com/ai4curation/eval-ont-agent-mondo/pull/383)
- **F1**: 0.571  **Precision**: 0.667  **Recall**: 0.500  **Jaccard**: 0.400
- **Trace**: [25817192792](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25817192792)
- **Workflow run**: [25817192792](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817192792)

#### Agent PR Comment

# NTR: KY-related neuromyopathy (issue #9937)

#### Agent Issue Comment

Thank you for the request. The new term **KY-related neuromyopathy** (`MONDO:7770012`) has been added under `MONDO:0100546` "hereditary neuromuscular disease", and the three existing terms you identified are now classified as children of the new term:

- `MONDO:0014922` "myofibrillar myopathy 7"
- `MONDO:0044648` "kyphoscoliosis-lateral tongue atrophy-hereditary spastic paraplegia syndrome"
- `MONDO:0044647` "kyphosis-lateral tongue atrophy-myofibrillar myopathy syndrome"

Existing parents on the three children were retained per Mondo curation guidelines (a more specific parent is added without removing existing parents unless explicitly requested).

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817192792)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..4d2859643 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -387232,6 +387232,7 @@ xref: MEDGEN:934678 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:617114 {source="DOID:0080098", source="MONDO:equivalentTo"}
 xref: UMLS:C4310711 {source="MEDGEN:934678", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018943 {source="DOID:0080098", source="MONDO:Redundant", source="OMIM:617114"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 intersection_of: MONDO:0018943 ! myofibrillar myopathy
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="OMIM:617114"} ! KY
@@ -586707,6 +586708,7 @@ xref: MEDGEN:1798876 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:496686 {source="MONDO:equivalentTo"}
 xref: UMLS:C5567453 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1798876"}
 is_a: MONDO:0018943 {source="Orphanet:496686"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphosis_lateral_tongue_atrophy_myofibrillar_myopathy_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 
 [Term]
@@ -586727,6 +586729,7 @@ is_a: MONDO:0002254 {source="https://orcid.org/0000-0002-5002-8648"} ! syndromic
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0002-5002-8648"} ! hereditary disease
 is_a: MONDO:0005071 {source="https://orcid.org/0000-0001-9310-0163"} ! nervous system disorder
 is_a: MONDO:0015150 {source="https://orcid.org/0000-0002-4142-7153"} ! complex hereditary spastic paraplegia
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphoscoliosis_lateral_tongue_atrophy_hereditary_spastic_paraplegia_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6752" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6877" xsd:anyURI
@@ -665382,6 +665385,22 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: KY-related neuromyopathy
+def: "Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene." [https://clinicalgenome.org/affiliation/40151/, PMID:27484770, PMID:27485408, PMID:28488683, PMID:32818658]
+subset: clingen {source="MONDO:CLINGEN"}
+subset: disease_grouping
+synonym: "hereditary neuromuscular disease caused by mutation in KY" EXACT [MONDO:patterns/disease_series_by_gene]
+synonym: "KY hereditary neuromuscular disease" EXACT [MONDO:patterns/disease_series_by_gene]
+synonym: "KY-related neuromyopathy" EXACT [https://clinicalgenome.org/affiliation/40151/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0100546 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! hereditary neuromuscular disease
+intersection_of: MONDO:0100546 ! hereditary neuromuscular disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="https://clinicalgenome.org/affiliation/40151/", source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658"} ! KY
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-2078-7280
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 5: kimi-k2.6 / opencode

- **Eval PR**: [#268](https://github.com/ai4curation/eval-ont-agent-mondo/pull/268)
- **F1**: 0.538  **Precision**: 0.583  **Recall**: 0.500  **Jaccard**: 0.368
- **Trace**: [25755525953](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25755525953)
- **Workflow run**: [25755525953](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755525953)

#### Agent PR Comment

## Summary

This PR addresses issue #9937 by adding a new ClinGen-requested gene-related grouping term **KY-related neuromyopathy** (MONDO:7770012) and reclassifying three existing terms as its children.

## Changes Made

1. **New Term: MONDO:7770012 "KY-related neuromyopathy"**
   - Parent: MONDO:0100546 "hereditary neuromuscular disease"
   - Definition: "Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene."
   - Logical definition: `hereditary neuromuscular disease and has_material_basis_in_germline_mutation_in some KY`
   - Sources: PMID:27484770, PMID:27485408, PMID:28488683, PMID:32818658, https://clinicalgenome.org/affiliation/40151/
   - Synonyms: "KY neuromyopathy" EXACT, "neuromyopathy caused by mutation in KY" EXACT
   - Curator attribution: ORCID 0000-0002-2078-7280

2. **Reclassified Children**
   - Added `is_a: MONDO:7770012` to:
     - MONDO:0014922 "myofibrillar myopathy 7"
     - MONDO:0044648 "kyphoscoliosis-lateral tongue atrophy-hereditary spastic paraplegia syndrome"
     - MONDO:0044647 "kyphosis-lateral tongue atrophy-myofibrillar myopathy syndrome"
   - Existing parents were preserved per Mondo curation guidelines.

## Checklist

- [x] Verified existing parent term (MONDO:0100546) is appropriate
- [x] Verified KY gene identifier (HGNC:26576)
- [x] Checked next available temporary MONDO ID (MONDO:7770012)
- [x] Followed `disease_series_by_gene` design pattern
- [x] Added proper definition with multiple PMID sources
- [x] Added ClinGen affiliation URL as source
- [x] Added logical definition with intersection_of axioms
- [x] Added curator ORCID as creator property
- [x] Added term tracker item linking to issue #9937
- [x] Ran ODK normalization (`make NORM`)
- [x] Validated logical consistency with `robot reason` (ELK reasoner)

## Background

The ClinGen Muscular Dystrophy and Myopathy GCEP considers myofibrillar myopathy 7 and the two lateral tongue atrophy syndromes to be part of a spectrum of KY-related neuromyopathy. The literature on KY mutations (PMIDs 27484770, 27485408, 28488683, 32818658) supports a heterogeneous neuromuscular phenotype, so a broad grouping term under hereditary neuromuscular disease was created rather than forcing all phenotypes into a single narrow leaf term.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755525953)


#### Agent Issue Comment

Thank you for the new term request. The changes have been committed in PR #<NN>.

- Added new term **MONDO:7770012** "KY-related neuromyopathy"
- Reclassified the three specified terms as children of MONDO:7770012:
  - MONDO:0014922 "myofibrillar myopathy 7"
  - MONDO:0044648 "kyphoscoliosis-lateral tongue atrophy-hereditary spastic paraplegia syndrome"
  - MONDO:0044647 "kyphosis-lateral tongue atrophy-myofibrillar myopathy syndrome"

Please let us know if these classifications need to be updated in the future.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755525953)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..2920954f0 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -387232,6 +387232,7 @@ xref: MEDGEN:934678 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:617114 {source="DOID:0080098", source="MONDO:equivalentTo"}
 xref: UMLS:C4310711 {source="MEDGEN:934678", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018943 {source="DOID:0080098", source="MONDO:Redundant", source="OMIM:617114"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
 intersection_of: MONDO:0018943 ! myofibrillar myopathy
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="OMIM:617114"} ! KY
@@ -586707,6 +586708,7 @@ xref: MEDGEN:1798876 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:496686 {source="MONDO:equivalentTo"}
 xref: UMLS:C5567453 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1798876"}
 is_a: MONDO:0018943 {source="Orphanet:496686"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphosis_lateral_tongue_atrophy_myofibrillar_myopathy_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 
 [Term]
@@ -586727,6 +586729,7 @@ is_a: MONDO:0002254 {source="https://orcid.org/0000-0002-5002-8648"} ! syndromic
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0002-5002-8648"} ! hereditary disease
 is_a: MONDO:0005071 {source="https://orcid.org/0000-0001-9310-0163"} ! nervous system disorder
 is_a: MONDO:0015150 {source="https://orcid.org/0000-0002-4142-7153"} ! complex hereditary spastic paraplegia
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphoscoliosis_lateral_tongue_atrophy_hereditary_spastic_paraplegia_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6752" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6877" xsd:anyURI
@@ -665382,6 +665385,20 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: KY-related neuromyopathy
+def: "Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene." [https://clinicalgenome.org/affiliation/40151/, PMID:27484770, PMID:27485408, PMID:28488683, PMID:32818658]
+subset: clingen {source="MONDO:CLINGEN"}
+synonym: "KY neuromyopathy" EXACT [MONDO:patterns/disease_series_by_gene]
+synonym: "neuromyopathy caused by mutation in KY" EXACT [MONDO:patterns/disease_series_by_gene]
+is_a: MONDO:0100546 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! hereditary neuromuscular disease
+intersection_of: MONDO:0100546 ! hereditary neuromuscular disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! KY
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-2078-7280
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 6: gpt-5.5 / opencode

- **Eval PR**: [#75](https://github.com/ai4curation/eval-ont-agent-mondo/pull/75)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25615975296](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615975296)
- **Workflow run**: [25615975296](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615975296)

#### Agent PR Comment

## Summary

Addressed issue #9937 by adding a new MONDO term:

- `MONDO:7770012` — `KY-related neuromyopathy`

Updated the requested existing terms to be children of the new term:

- `MONDO:0014922` — `myofibrillar myopathy 7`
- `MONDO:0044647` — `kyphosis-lateral tongue atrophy-myofibrillar myopathy syndrome`
- `MONDO:0044648` — `kyphoscoliosis-lateral tongue atrophy-hereditary spastic paraplegia syndrome`

## Rationale and curation notes

- Used `MONDO:0100546` (`hereditary neuromuscular disease`) as the asserted parent, as requested.
- Added a disease-series-style logical definition using the verified KY HGNC identifier, `http://identifiers.org/hgnc/26576`.
- Cited the ClinGen Muscular Dystrophy and Myopathy GCEP affiliation URL and the four PMIDs provided in the issue (`PMID:27484770`, `PMID:27485408`, `PMID:28488683`, `PMID:32818658`).
- Preserved all existing parents on the three child terms and added the new parent rather than removing existing classification.
- Added the issue tracker reference to the new term.

## Checklist

- [x] Read the issue context and comments.
- [x] Checked existing parent and requested child terms in `src/ontology/mondo-edit.obo`.
- [x] Checked for existing `MONDO:777` new-term ID usage and selected the next available local NTR ID.
- [x] Verified KY as HGNC:26576 using HGNC REST data.
- [x] Retrieved PubMed summary metadata for the cited PMIDs via NCBI E-utilities. Attempted `aurelian fulltext`, but `aurelian` was not available in this environment.
- [x] Checked changes in through the terms workflow and normalized `src/ontology/mondo-edit.obo` with `make NORM`.
- [x] Validated OBO syntax with `robot convert --catalog catalog-v001.xml -i mondo-edit.obo -f obo`.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615975296)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Added `KY-related neuromyopathy` and classified the three requested existing MONDO terms as children.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615975296)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..df272e4b1 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -387232,6 +387232,7 @@ xref: MEDGEN:934678 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:617114 {source="DOID:0080098", source="MONDO:equivalentTo"}
 xref: UMLS:C4310711 {source="MEDGEN:934678", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018943 {source="DOID:0080098", source="MONDO:Redundant", source="OMIM:617114"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 intersection_of: MONDO:0018943 ! myofibrillar myopathy
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="OMIM:617114"} ! KY
@@ -586707,6 +586708,7 @@ xref: MEDGEN:1798876 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:496686 {source="MONDO:equivalentTo"}
 xref: UMLS:C5567453 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1798876"}
 is_a: MONDO:0018943 {source="Orphanet:496686"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphosis_lateral_tongue_atrophy_myofibrillar_myopathy_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 
 [Term]
@@ -586727,6 +586729,7 @@ is_a: MONDO:0002254 {source="https://orcid.org/0000-0002-5002-8648"} ! syndromic
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0002-5002-8648"} ! hereditary disease
 is_a: MONDO:0005071 {source="https://orcid.org/0000-0001-9310-0163"} ! nervous system disorder
 is_a: MONDO:0015150 {source="https://orcid.org/0000-0002-4142-7153"} ! complex hereditary spastic paraplegia
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphoscoliosis_lateral_tongue_atrophy_hereditary_spastic_paraplegia_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6752" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6877" xsd:anyURI
@@ -665382,6 +665385,18 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: KY-related neuromyopathy
+def: "Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene." [https://clinicalgenome.org/affiliation/40151/, PMID:27484770, PMID:27485408, PMID:28488683, PMID:32818658]
+subset: rare
+is_a: MONDO:0100546 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! hereditary neuromuscular disease
+intersection_of: MONDO:0100546 ! hereditary neuromuscular disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! KY
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-2078-7280
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 7: gpt-5.5 / opencode

- **Eval PR**: [#56](https://github.com/ai4curation/eval-ont-agent-mondo/pull/56)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25615932851](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615932851)
- **Workflow run**: [25615932851](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615932851)

#### Agent PR Comment

## Summary

This change addresses issue #9937 by adding a new ClinGen-requested term, `MONDO:7770012` `KY-related neuromyopathy`, as a child of `MONDO:0100546` `hereditary neuromuscular disease`.

The term follows the MONDO gene-related disease series pattern with a text definition, logical definition, `has_material_basis_in_germline_mutation_in` relationship to `KY`, ClinGen source attribution, PubMed references, and issue tracker metadata.

The following existing terms were added as children of the new term, preserving their existing parents:

- `MONDO:0014922` `myofibrillar myopathy 7`
- `MONDO:0044648` `kyphoscoliosis-lateral tongue atrophy-hereditary spastic paraplegia syndrome`
- `MONDO:0044647` `kyphosis-lateral tongue atrophy-myofibrillar myopathy syndrome`

#### Agent Issue Comment

Changes committed in PR #<NN>.

Added `KY-related neuromyopathy` and placed the three requested existing terms underneath it.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615932851)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..df272e4b1 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -387232,6 +387232,7 @@ xref: MEDGEN:934678 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:617114 {source="DOID:0080098", source="MONDO:equivalentTo"}
 xref: UMLS:C4310711 {source="MEDGEN:934678", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018943 {source="DOID:0080098", source="MONDO:Redundant", source="OMIM:617114"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 intersection_of: MONDO:0018943 ! myofibrillar myopathy
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="OMIM:617114"} ! KY
@@ -586707,6 +586708,7 @@ xref: MEDGEN:1798876 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:496686 {source="MONDO:equivalentTo"}
 xref: UMLS:C5567453 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1798876"}
 is_a: MONDO:0018943 {source="Orphanet:496686"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphosis_lateral_tongue_atrophy_myofibrillar_myopathy_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 
 [Term]
@@ -586727,6 +586729,7 @@ is_a: MONDO:0002254 {source="https://orcid.org/0000-0002-5002-8648"} ! syndromic
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0002-5002-8648"} ! hereditary disease
 is_a: MONDO:0005071 {source="https://orcid.org/0000-0001-9310-0163"} ! nervous system disorder
 is_a: MONDO:0015150 {source="https://orcid.org/0000-0002-4142-7153"} ! complex hereditary spastic paraplegia
+is_a: MONDO:7770012 {source="https://clinicalgenome.org/affiliation/40151/", source="https://orcid.org/0000-0002-2078-7280"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphoscoliosis_lateral_tongue_atrophy_hereditary_spastic_paraplegia_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6752" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6877" xsd:anyURI
@@ -665382,6 +665385,18 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: KY-related neuromyopathy
+def: "Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene." [https://clinicalgenome.org/affiliation/40151/, PMID:27484770, PMID:27485408, PMID:28488683, PMID:32818658]
+subset: rare
+is_a: MONDO:0100546 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! hereditary neuromuscular disease
+intersection_of: MONDO:0100546 ! hereditary neuromuscular disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! KY
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-2078-7280
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 8: gpt-5.5 / codex

- **Eval PR**: [#36](https://github.com/ai4curation/eval-ont-agent-mondo/pull/36)
- **F1**: 0.500  **Precision**: 0.500  **Recall**: 0.500  **Jaccard**: 0.333
- **Trace**: [25615869007](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615869007)
- **Workflow run**: [25615869007](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615869007)

#### Agent PR Comment

## Summary

Added a new MONDO term, `MONDO:7770012` `KY-related neuromyopathy`, for issue #9937.

The term is placed under `hereditary neuromuscular disease` (`MONDO:0100546`) and includes a logical definition using `has_material_basis_in_germline_mutation_in` with the verified KY gene identifier `http://identifiers.org/hgnc/26576`.

The following existing terms were classified as children of the new term, preserving their existing parentage:

- `MONDO:0014922` myofibrillar myopathy 7
- `MONDO:0044647` kyphosis-lateral tongue atrophy-myofibrillar myopathy syndrome
- `MONDO:0044648` kyphoscoliosis-lateral tongue atrophy-hereditary spastic paraplegia syndrome

## Rationale

The issue requested a ClinGen-supported gene-related spectrum term for KY-related neuromyopathy, with `hereditary neuromuscular disease` as the parent and three existing terms as children. The new definition follows the requested gene-related disease pattern:

`Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene.`

I used the issue-provided literature sources (`PMID:27484770`, `PMID:27485408`, `PMID:28488683`, `PMID:32818658`) and the ClinGen Muscular Dystrophy and Myopathy GCEP URL as attribution.

## Checks Completed

- Confirmed no existing `KY-related neuromyopathy` term in `src/ontology/mondo-edit.obo`.
- Checked the requested parent term and child terms in `src/ontology/mondo-edit.obo`.
- Checked the `disease_series_by_gene` DOSDP pattern.
- Verified KY as HGNC:26576 using the HGNC REST service.
- Attempted `aurelian fulltext` for all issue-provided PMIDs, but `aurelian` was not installed in this environment; used public literature/database pages as fallback evidence.
- Normalized serialization with local `make NORM` and replaced `src/ontology/mondo-edit.obo` with `NORM`.
- Ran ROBOT syntax conversion:
  - `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo`
- Ran `git diff --check`.


---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615869007)


#### Agent Issue Comment

Created `KY-related neuromyopathy` and classified the three requested existing terms as children. Changes committed in PR #<NN>.


---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615869007)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..52d46aafd 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -387232,6 +387232,7 @@ xref: MEDGEN:934678 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:617114 {source="DOID:0080098", source="MONDO:equivalentTo"}
 xref: UMLS:C4310711 {source="MEDGEN:934678", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018943 {source="DOID:0080098", source="MONDO:Redundant", source="OMIM:617114"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="PMID:27484770", source="PMID:27485408", source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
 intersection_of: MONDO:0018943 ! myofibrillar myopathy
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="OMIM:617114"} ! KY
@@ -586707,6 +586708,7 @@ xref: MEDGEN:1798876 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:496686 {source="MONDO:equivalentTo"}
 xref: UMLS:C5567453 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1798876"}
 is_a: MONDO:0018943 {source="Orphanet:496686"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="PMID:27484770", source="PMID:27485408", source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphosis_lateral_tongue_atrophy_myofibrillar_myopathy_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 
 [Term]
@@ -586727,6 +586729,7 @@ is_a: MONDO:0002254 {source="https://orcid.org/0000-0002-5002-8648"} ! syndromic
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0002-5002-8648"} ! hereditary disease
 is_a: MONDO:0005071 {source="https://orcid.org/0000-0001-9310-0163"} ! nervous system disorder
 is_a: MONDO:0015150 {source="https://orcid.org/0000-0002-4142-7153"} ! complex hereditary spastic paraplegia
+is_a: MONDO:7770012 {source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
 property_value: curated_content_resource "https://www.malacards.org/card/kyphoscoliosis_lateral_tongue_atrophy_hereditary_spastic_paraplegia_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6752" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6877" xsd:anyURI
@@ -665382,6 +665385,18 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: KY-related neuromyopathy
+def: "Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene." [https://clinicalgenome.org/affiliation/40151/, PMID:27484770, PMID:27485408, PMID:28488683, PMID:32818658]
+subset: rare
+is_a: MONDO:0100546 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! hereditary neuromuscular disease
+intersection_of: MONDO:0100546 ! hereditary neuromuscular disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! KY
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-2078-7280
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 9: gpt-5.4 / codex

- **Eval PR**: [#20](https://github.com/ai4curation/eval-ont-agent-mondo/pull/20)
- **F1**: 0.500  **Precision**: 0.583  **Recall**: 0.438  **Jaccard**: 0.333
- **Trace**: [25610264876](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25610264876)
- **Workflow run**: [25610264876](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25610264876)

#### Agent PR Comment

This change addresses issue #9937 by adding a new spectrum term, `MONDO:7770012` `KY-related neuromyopathy`, under `MONDO:0100546` `hereditary neuromuscular disease`.

Rationale:
- The issue requested a ClinGen-style gene-related spectrum term for KY with `hereditary neuromuscular disease` as the parent.
- The cited publications support a KY-associated neuromuscular spectrum spanning the already existing child terms:
- `MONDO:0014922` `myofibrillar myopathy 7`
- `MONDO:0044647` `kyphosis-lateral tongue atrophy-myofibrillar myopathy syndrome`
- `MONDO:0044648` `kyphoscoliosis-lateral tongue atrophy-hereditary spastic paraplegia syndrome`

Ontology changes made:
- Added new term `MONDO:7770012` `KY-related neuromyopathy`
- Added definition: `Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene.`
- Added exact synonyms reflecting the requested ClinGen-preferred label
- Added asserted parentage to `MONDO:0100546`
- Added genus-differentia pattern axioms using `has_material_basis_in_germline_mutation_in` some `KY` (`HGNC:26576`)
- Reclassified the three requested existing terms as children of `KY-related neuromyopathy`
- Added explicit `KY` gene relationships to `MONDO:0044647` and `MONDO:0044648`
- Added issue provenance (`IAO:0000233`) to the new and modified terms

Identifier and evidence checks:
- Verified the human gene identifier as `HGNC:26576` for `KY` using NCBI Gene (`KY kyphoscoliosis peptidase`, primary source HGNC:26576)
- Reviewed the cited literature metadata/titles for:
- `PMID:27484770` `Kyphoscoliosis peptidase (KY) mutation causes a novel congenital myopathy with core targetoid defects`
- `PMID:27485408` `A new early-onset neuromuscular disorder associated with kyphoscoliosis peptidase (KY) deficiency`
- `PMID:28488683` `Progressive hereditary spastic paraplegia caused by a homozygous KY mutation`
- `PMID:32818658` `A novel homozygous KY variant causing a complex neurological disorder`

Validation performed:
- Checked the edited term stanzas back into `src/ontology/mondo-edit.obo`
- Ran `make NORM` from `src/ontology` and replaced `mondo-edit.obo` with the normalized output
- Ran `robot convert --catalog catalog-v001.xml -i mondo-edit.obo -f obo -o mondo-edit.TMP.obo`
- `robot convert` completed successfully, confirming the edited ontology parses after normalization

Completed checklist:
- [x] Read imported issue context from `__issue_context__.json`
- [x] Verified the target parent term in the ontology
- [x] Verified the KY human gene identifier
- [x] Added the new spectrum term in MONDO OBO format
- [x] Reclassified the requested existing children
- [x] Added issue provenance
- [x] Normalized the ontology serialization
- [x] Ran syntax validation

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25610264876)


#### Agent Issue Comment

Implemented in PR #<NN>.

Added `MONDO:7770012` `KY-related neuromyopathy` as a child of `MONDO:0100546` `hereditary neuromuscular disease`, and reclassified these existing terms under it:
- `MONDO:0014922` `myofibrillar myopathy 7`
- `MONDO:0044647` `kyphosis-lateral tongue atrophy-myofibrillar myopathy syndrome`
- `MONDO:0044648` `kyphoscoliosis-lateral tongue atrophy-hereditary spastic paraplegia syndrome`

The new term and reclassification were based on the ClinGen request and the cited KY literature. These changes will be available in the next MONDO release.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25610264876)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..1b5bcc9cc 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -387232,10 +387232,12 @@ xref: MEDGEN:934678 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:617114 {source="DOID:0080098", source="MONDO:equivalentTo"}
 xref: UMLS:C4310711 {source="MEDGEN:934678", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0018943 {source="DOID:0080098", source="MONDO:Redundant", source="OMIM:617114"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="PMID:27484770", source="PMID:27485408", source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
 intersection_of: MONDO:0018943 ! myofibrillar myopathy
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="OMIM:617114"} ! KY
 property_value: curated_content_resource "https://www.malacards.org/card/myopathy_myofibrillar_7" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
 
 [Term]
 id: MONDO:0014923
@@ -586707,7 +586709,10 @@ xref: MEDGEN:1798876 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:496686 {source="MONDO:equivalentTo"}
 xref: UMLS:C5567453 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:1798876"}
 is_a: MONDO:0018943 {source="Orphanet:496686"} ! myofibrillar myopathy
+is_a: MONDO:7770012 {source="PMID:27484770", source="PMID:27485408", source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="PMID:27484770", source="PMID:27485408"} ! KY
 property_value: curated_content_resource "https://www.malacards.org/card/kyphosis_lateral_tongue_atrophy_myofibrillar_myopathy_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
 
 [Term]
 id: MONDO:0044648
@@ -586727,10 +586732,13 @@ is_a: MONDO:0002254 {source="https://orcid.org/0000-0002-5002-8648"} ! syndromic
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0002-5002-8648"} ! hereditary disease
 is_a: MONDO:0005071 {source="https://orcid.org/0000-0001-9310-0163"} ! nervous system disorder
 is_a: MONDO:0015150 {source="https://orcid.org/0000-0002-4142-7153"} ! complex hereditary spastic paraplegia
+is_a: MONDO:7770012 {source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! KY-related neuromyopathy
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="PMID:28488683", source="PMID:32818658"} ! KY
 property_value: curated_content_resource "https://www.malacards.org/card/kyphoscoliosis_lateral_tongue_atrophy_hereditary_spastic_paraplegia_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6752" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6877" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6878" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
 
 [Term]
 id: MONDO:0044649
@@ -665382,6 +665390,21 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: KY-related neuromyopathy
+def: "Any hereditary neuromuscular disease in which the cause of the disease is a mutation in the KY gene." [PMID:27484770, PMID:27485408, PMID:28488683, PMID:32818658]
+subset: clingen {source="MONDO:CLINGEN"}
+subset: rare
+synonym: "KY neuromyopathy" EXACT [https://clinicalgenome.org/affiliation/40151/]
+synonym: "KY-related neuromyopathy" EXACT [https://clinicalgenome.org/affiliation/40151/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0100546 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! hereditary neuromuscular disease
+intersection_of: MONDO:0100546 ! hereditary neuromuscular disease
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 ! KY
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576 {source="PMID:27484770", source="PMID:27485408", source="PMID:28488683", source="PMID:32818658", source="https://clinicalgenome.org/affiliation/40151/"} ! KY
+property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9937" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```
