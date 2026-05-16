---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9864
pr_number: 10105
issue_title: Request for new term SYCE1-related gametogenic failure
pr_author: MeeSiing
pr_merged_at: '2026-03-31'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
best_f1: 0.56
best_model: claude-sonnet-4.5
---

# PR #10105 — Request for new term SYCE1-related gametogenic failure

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9864](https://github.com/monarch-initiative/mondo/issues/9864) | [PR #10105](https://github.com/monarch-initiative/mondo/pull/10105) | @MeeSiing | merged 2026-03-31

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #9864 requested a new term for "SYCE1-related gametogenic failure" describing a condition where variants in SYCE1 (synaptonemal complex central element protein 1) cause varying gametogenic phenotypes in both 46,XY and 46,XX individuals, ranging from spermatogenic failure to premature ovarian insufficiency.

## Changes Made

The PR created MONDO:1060214 with 12 additions to mondo-edit.obo: the term ID, label, definition referencing the gametogenic failure phenotype, ClinGen preferred label as exact synonym, logical definition (likely using the gene-related disease pattern linking to SYCE1), parent classification under gametogenic failure, and appropriate cross-references. The curator noted that child terms were not requested and would be handled by the reasoner.

## Resolution

Moderate difficulty because new term creation requires understanding of Mondo's DOSDP patterns, correct parent placement, and logical definition construction. The curator needed to craft a definition that captures the variable expressivity (both male and female presentations) and set up the logical axiom so the reasoner can infer additional classification. An agent would need knowledge of Mondo's term creation SOP and gene-disease patterns.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8013937e49..d7a85ffe7b 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -665193,6 +665193,18 @@ is_a: MONDO:0006949 {source="PMID:29859199", source="https://orcid.org/0000-0001
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9849" xsd:anyURI
 
+[Term]
+id: MONDO:1060214
+name: SYCE1-related gametogenic failure
+def: "An infertility disorder caused by variation in the SYCE1 gene. Affected males may present with non-obstructive azoospermia due to maturation arrest or meiotic failure, while affected females may present with primary ovarian insufficiency." [https://clinicalgenome.org/affiliation/40073/, PMID:32402064, PMID:35718780]
+synonym: "SYCE1-related gametogenic failure" EXACT [https://clinicalgenome.org/affiliation/40073/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0005047 {source="https://clinicalgenome.org/affiliation/40073/"} ! infertility disorder
+intersection_of: MONDO:0005047 ! infertility disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="PMID:32402064", source="PMID:35718780", source="https://clinicalgenome.org/affiliation/40073/"} ! SYCE1
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9864" xsd:anyURI
+
 [Term]
 id: MONDO:7770001
 name: equine juvenile spinocerebellar ataxia, FDXR-related, horse

```

## Agent Attempts (8)

### Attempt 1: claude-sonnet-4.5 / copilot

- **Eval PR**: [#334](https://github.com/ai4curation/eval-ont-agent-mondo/pull/334)
- **F1**: 0.560  **Precision**: 0.636  **Recall**: 0.500  **Jaccard**: 0.389
- **Trace**: [25774281792](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25774281792)
- **Workflow run**: [25774281792](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25774281792)

#### Agent PR Comment

# New Term: SYCE1-related gametogenic failure

#### Agent Issue Comment

Thank you for submitting this new term request! 

I've created the new umbrella term **SYCE1-related gametogenic failure** (MONDO:7770012) as requested. This term is now a parent of both:
- MONDO:0014844 (premature ovarian failure 12) 
- MONDO:0014847 (spermatogenic failure 15)

The term definition captures the varying phenotypes in 46,XY individuals (non-obstructive azoospermia) and 46,XX individuals (primary ovarian insufficiency) as you described.

Changes committed in PR #<NN>.

@GabrielleGCA Please let me know if any adjustments are needed to the term definition or structure.

---
🤖 **Generated by copilot agent**
- Runtime: `copilot`
- Model: `claude-sonnet-4.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25774281792)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8013937e4..26f35ccb5 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -385046,6 +385046,7 @@ xref: OMIM:616947 {source="MONDO:equivalentTo"}
 xref: UMLS:C4310782 {source="MEDGEN:934749", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease
 is_a: MONDO:0019852 {source="DC-OMIM:616947", source="OMIM:616947"} ! inherited primary ovarian failure
+is_a: MONDO:7770012 {source="https://github.com/monarch-initiative/mondo/issues/9864"} ! SYCE1-related gametogenic failure
 intersection_of: MONDO:0019852 ! inherited primary ovarian failure
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="OMIM:616947"} ! SYCE1
@@ -385127,6 +385128,7 @@ xref: MEDGEN:934746 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:616950 {source="MONDO:equivalentTo"}
 xref: UMLS:C4310779 {source="MEDGEN:934746", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0004983 {source="DC-OMIM:616950", source="DOID:0070172", source="MONDO:Redundant", source="OMIM:616950"} ! spermatogenic failure
+is_a: MONDO:7770012 {source="https://github.com/monarch-initiative/mondo/issues/9864"} ! SYCE1-related gametogenic failure
 intersection_of: MONDO:0004983 ! spermatogenic failure
 intersection_of: disease_has_basis_in_dysfunction_of http://identifiers.org/hgnc/28852 ! SYCE1
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
@@ -665300,6 +665302,20 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: SYCE1-related gametogenic failure
+def: "Any infertility disorder in which the cause of the disease is a mutation in the SYCE1 gene. Individuals with variants in SYCE1 may present with varying phenotypes. 46,XY individuals can present with non-obstructive azoospermia due to maturation arrest/meiotic failure. 46,XX individuals can present with primary ovarian insufficiency." [https://www.clinicalgenome.org/affiliation/40073/]
+synonym: "gametogenic failure caused by mutation in SYCE1" EXACT [MONDO:design_pattern]
+synonym: "SYCE1 infertility disorder" EXACT [MONDO:design_pattern, MONDO:patterns/disease_series_by_gene]
+is_a: MONDO:0003847 ! hereditary disease
+is_a: MONDO:0005047 ! infertility disorder
+intersection_of: MONDO:0005047 ! infertility disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9864" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 2: gpt-5.5 / opencode

- **Eval PR**: [#133](https://github.com/ai4curation/eval-ont-agent-mondo/pull/133)
- **F1**: 0.545  **Precision**: 0.545  **Recall**: 0.545  **Jaccard**: 0.375
- **Workflow run**: [25633625526](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25633625526)

#### Agent PR Comment

## Summary

This PR addresses #9864 by adding a new MONDO term for ClinGen Male Infertility GCEP's requested label:

- Added `MONDO:7770012` **SYCE1-related gametogenic failure**
- Defined it as an infertility disorder caused by variation in `SYCE1`, with the 46,XY and 46,XX presentations described in the issue
- Added a ClinGen preferred-label synonym annotation using the Male Infertility GCEP URL
- Added a logical definition and asserted `has_material_basis_in_germline_mutation_in` relationship to `SYCE1` (`http://identifiers.org/hgnc/28852`)
- Linked the existing SYCE1-specific terms as children:
  - `MONDO:0014844` premature ovarian failure 12
  - `MONDO:0014847` spermatogenic failure 15

## Rationale and checks

Checklist completed:

- Reviewed issue #9864 context and the ClinGen Male Infertility GCEP URL supplied in the comments.
- Checked existing SYCE1-related MONDO terms (`MONDO:0014844`, `MONDO:0014847`) for parentage, sources, and the verified HGNC identifier for `SYCE1`.
- Checked the applicable gene-related disease pattern guidance (`disease_series_by_gene.yaml`).
- Used the next available temporary new-term identifier in the `MONDO:777xxxx` range (`MONDO:7770012`).
- Preserved existing parents on the existing terms and only added the more specific new parent.
- Normalized `src/ontology/mondo-edit.obo` with `make NORM` followed by replacing `mondo-edit.obo`.
- Validated OBO syntax with:
  - `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo`
- Ran `git diff --check` for whitespace issues.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25633625526)


#### Agent Issue Comment

Created MONDO:7770012 `SYCE1-related gametogenic failure` and linked the existing SYCE1-specific premature ovarian failure and spermatogenic failure terms as children. Changes committed in PR #<NN>.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25633625526)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8013937e4..d3e546130 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -385046,6 +385046,7 @@ xref: OMIM:616947 {source="MONDO:equivalentTo"}
 xref: UMLS:C4310782 {source="MEDGEN:934749", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease
 is_a: MONDO:0019852 {source="DC-OMIM:616947", source="OMIM:616947"} ! inherited primary ovarian failure
+is_a: MONDO:7770012 {source="OMIM:616947", source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1-related gametogenic failure
 intersection_of: MONDO:0019852 ! inherited primary ovarian failure
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="OMIM:616947"} ! SYCE1
@@ -385127,6 +385128,7 @@ xref: MEDGEN:934746 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:616950 {source="MONDO:equivalentTo"}
 xref: UMLS:C4310779 {source="MEDGEN:934746", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0004983 {source="DC-OMIM:616950", source="DOID:0070172", source="MONDO:Redundant", source="OMIM:616950"} ! spermatogenic failure
+is_a: MONDO:7770012 {source="OMIM:616950", source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1-related gametogenic failure
 intersection_of: MONDO:0004983 ! spermatogenic failure
 intersection_of: disease_has_basis_in_dysfunction_of http://identifiers.org/hgnc/28852 ! SYCE1
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
@@ -665300,6 +665302,17 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: SYCE1-related gametogenic failure
+def: "Any infertility disorder in which the cause of the disease is a variation in the SYCE1 gene. In 46,XY individuals, this condition can present as non-obstructive azoospermia due to maturation arrest or meiotic failure; in 46,XX individuals, it can present as primary ovarian insufficiency." [https://www.clinicalgenome.org/affiliation/40073/, OMIM:616947, OMIM:616950]
+synonym: "SYCE1-related gametogenic failure" EXACT [https://www.clinicalgenome.org/affiliation/40073/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0005047 {source="OMIM:616947", source="OMIM:616950", source="https://www.clinicalgenome.org/affiliation/40073/"} ! infertility disorder
+intersection_of: MONDO:0005047 ! infertility disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="OMIM:616947", source="OMIM:616950", source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9864" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 3: gpt-5.5 / opencode

- **Eval PR**: [#118](https://github.com/ai4curation/eval-ont-agent-mondo/pull/118)
- **F1**: 0.545  **Precision**: 0.545  **Recall**: 0.545  **Jaccard**: 0.375

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8013937e4..d3e546130 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -385046,6 +385046,7 @@ xref: OMIM:616947 {source="MONDO:equivalentTo"}
 xref: UMLS:C4310782 {source="MEDGEN:934749", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease
 is_a: MONDO:0019852 {source="DC-OMIM:616947", source="OMIM:616947"} ! inherited primary ovarian failure
+is_a: MONDO:7770012 {source="OMIM:616947", source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1-related gametogenic failure
 intersection_of: MONDO:0019852 ! inherited primary ovarian failure
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="OMIM:616947"} ! SYCE1
@@ -385127,6 +385128,7 @@ xref: MEDGEN:934746 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:616950 {source="MONDO:equivalentTo"}
 xref: UMLS:C4310779 {source="MEDGEN:934746", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0004983 {source="DC-OMIM:616950", source="DOID:0070172", source="MONDO:Redundant", source="OMIM:616950"} ! spermatogenic failure
+is_a: MONDO:7770012 {source="OMIM:616950", source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1-related gametogenic failure
 intersection_of: MONDO:0004983 ! spermatogenic failure
 intersection_of: disease_has_basis_in_dysfunction_of http://identifiers.org/hgnc/28852 ! SYCE1
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
@@ -665300,6 +665302,17 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: SYCE1-related gametogenic failure
+def: "Any infertility disorder in which the cause of the disease is a variation in the SYCE1 gene. In 46,XY individuals, this condition can present as non-obstructive azoospermia due to maturation arrest or meiotic failure; in 46,XX individuals, it can present as primary ovarian insufficiency." [https://www.clinicalgenome.org/affiliation/40073/, OMIM:616947, OMIM:616950]
+synonym: "SYCE1-related gametogenic failure" EXACT [https://www.clinicalgenome.org/affiliation/40073/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0005047 {source="OMIM:616947", source="OMIM:616950", source="https://www.clinicalgenome.org/affiliation/40073/"} ! infertility disorder
+intersection_of: MONDO:0005047 ! infertility disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="OMIM:616947", source="OMIM:616950", source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9864" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 4: claude-sonnet-4.5 / claude

- **Eval PR**: [#454](https://github.com/ai4curation/eval-ont-agent-mondo/pull/454)
- **F1**: 0.462  **Precision**: 0.545  **Recall**: 0.400  **Jaccard**: 0.300
- **Trace**: [25867754153](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25867754153)
- **Workflow run**: [25867754153](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867754153)

#### Agent PR Comment

## Summary

This PR addresses issue #9864 by creating a new parent term for SYCE1-related gametogenic failures, as requested by ClinGen's Male Infertility GCEP.

#### Agent Issue Comment

Thank you for submitting this term request!

I've successfully created the new term **SYCE1-related gametogenic failure** (MONDO:7770012) as requested by ClinGen's Male Infertility GCEP.

The new term:
- Encompasses both male and female manifestations of SYCE1-related infertility
- Is now the parent term for both MONDO:0014844 (premature ovarian failure 12) and MONDO:0014847 (spermatogenic failure 15)
- Follows the disease_series_by_gene design pattern
- Includes the phenotypic variation information you provided in the definition

Changes have been committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867754153)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8013937e4..e400572a0 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -385046,6 +385046,7 @@ xref: OMIM:616947 {source="MONDO:equivalentTo"}
 xref: UMLS:C4310782 {source="MEDGEN:934749", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease
 is_a: MONDO:0019852 {source="DC-OMIM:616947", source="OMIM:616947"} ! inherited primary ovarian failure
+is_a: MONDO:7770012 {source="https://github.com/monarch-initiative/mondo/issues/9864"} ! SYCE1-related gametogenic failure
 intersection_of: MONDO:0019852 ! inherited primary ovarian failure
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="OMIM:616947"} ! SYCE1
@@ -385127,6 +385128,7 @@ xref: MEDGEN:934746 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:616950 {source="MONDO:equivalentTo"}
 xref: UMLS:C4310779 {source="MEDGEN:934746", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0004983 {source="DC-OMIM:616950", source="DOID:0070172", source="MONDO:Redundant", source="OMIM:616950"} ! spermatogenic failure
+is_a: MONDO:7770012 {source="https://github.com/monarch-initiative/mondo/issues/9864"} ! SYCE1-related gametogenic failure
 intersection_of: MONDO:0004983 ! spermatogenic failure
 intersection_of: disease_has_basis_in_dysfunction_of http://identifiers.org/hgnc/28852 ! SYCE1
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
@@ -665300,6 +665302,21 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: SYCE1-related gametogenic failure
+def: "Any infertility disorder in which the cause of the disease is a mutation in the SYCE1 gene. Individuals with variants in SYCE1 may present with varying phenotypes: 46XY individuals can present with non-obstructive azoospermia due to maturation arrest/meiotic failure, while 46XX individuals can present with primary ovarian insufficiency." [https://www.clinicalgenome.org/affiliation/40073/, MONDO:patterns/disease_series_by_gene]
+synonym: "gametogenic failure caused by mutation in SYCE1" EXACT [MONDO:design_pattern]
+synonym: "SYCE1 infertility disorder" EXACT [MONDO:design_pattern, MONDO:patterns/disease_series_by_gene]
+synonym: "SYCE1-related infertility" EXACT [https://www.clinicalgenome.org/affiliation/40073/]
+is_a: MONDO:0003847 ! hereditary disease
+is_a: MONDO:0005047 ! infertility disorder
+intersection_of: MONDO:0005047 ! infertility disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
+property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9864" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 5: gpt-5.5 / codex

- **Eval PR**: [#98](https://github.com/ai4curation/eval-ont-agent-mondo/pull/98)
- **F1**: 0.455  **Precision**: 0.455  **Recall**: 0.455  **Jaccard**: 0.294
- **Workflow run**: [25633573989](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25633573989)

#### Agent PR Comment

## Summary

Added new term `MONDO:7770012` / `SYCE1-related gametogenic failure` requested by ClinGen's Male Infertility GCEP.

## Rationale

The term is modeled as a `reproductive system disorder` with a `has_material_basis_in_germline_mutation_in` relationship to `SYCE1` (`HGNC:28852`). This follows the local ClinGen gene-related disease pattern used by the adjacent `NR5A1-related sex development disorder` term and avoids asserting the broad term as both a male infertility and female infertility class.

The definition covers the reported sex-specific presentations: non-obstructive azoospermia due to maturation arrest or meiotic failure in 46,XY individuals, and primary ovarian insufficiency in 46,XX individuals. Existing child/sibling context was checked against `MONDO:0014844` and `MONDO:0014847`.

## Completed Checklist

- Checked existing SYCE1-related MONDO terms and parent terms.
- Checked the applicable `disease_series_by_gene` pattern.
- Verified `SYCE1` identifier as `HGNC:28852`.
- Verified supporting literature metadata for PMID:25062452, PMID:25899990, PMID:34718620, and PMID:36177363.
- Added ClinGen preferred-label synonym attribution using the Male Infertility GCEP URL.
- Added issue tracker metadata for issue #9864.
- Ran `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo`; it completed successfully.
- Ran `git diff --check`; it passed.

## Notes

I attempted the requested normalization command, `sh run.sh make NORM && mv NORM mondo-edit.obo`, but it could not run because Docker is not installed in this environment (`docker: not found`). The generated `mondo-edit.TMP.obo` syntax-check file was removed and was not committed.

`aurelian` is also not installed in this environment, so literature checks were performed using accessible web/NCBI metadata instead.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25633573989)


#### Agent Issue Comment

Added `SYCE1-related gametogenic failure` as a new MONDO term. Changes committed in PR #<NN>.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25633573989)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8013937e4..7920413a9 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -665300,6 +665300,18 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: SYCE1-related gametogenic failure
+def: "A reproductive system disorder caused by a variation in the SYCE1 gene, and characterized by gametogenic failure that can present as non-obstructive azoospermia due to maturation arrest or meiotic failure in 46,XY individuals and primary ovarian insufficiency in 46,XX individuals." [https://www.clinicalgenome.org/affiliation/40073/, PMID:25062452, PMID:25899990, PMID:34718620, PMID:36177363]
+comment: Requested by ClinGen's Male Infertility GCEP. 46,XY individuals can present with non-obstructive azoospermia due to maturation arrest or meiotic failure. 46,XX individuals can present with primary ovarian insufficiency.
+synonym: "SYCE1-related gametogenic failure" EXACT [https://www.clinicalgenome.org/affiliation/40073/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0005039 {source="PMID:34718620", source="https://www.clinicalgenome.org/affiliation/40073/"} ! reproductive system disorder
+intersection_of: MONDO:0005039 ! reproductive system disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="PMID:25062452", source="PMID:25899990", source="PMID:34718620", source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9864" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 6: gpt-5.4 / codex

- **Eval PR**: [#172](https://github.com/ai4curation/eval-ont-agent-mondo/pull/172)
- **F1**: 0.417  **Precision**: 0.455  **Recall**: 0.385  **Jaccard**: 0.263
- **Workflow run**: [25640352578](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640352578)

#### Agent PR Comment

This change adds a new MONDO term, `MONDO:7770012` `SYCE1-related gametogenic failure`, in response to issue #9864.

Rationale:
- The issue requested a broader SYCE1 disease term covering both male and female gonadal phenotypes.
- I modeled this as a ClinGen-style umbrella gene term, following the existing pattern used for `MONDO:1060211` (`NR5A1-related sex development disorder`).
- I used `reproductive system disorder` as the direct parent for the new umbrella term, then added the two existing sex-specific SYCE1 terms as subclasses of the new term:
- `MONDO:0014844` `premature ovarian failure 12`
- `MONDO:0014847` `spermatogenic failure 15`
- I did not remove any existing parents from the pre-existing terms.

Evidence reviewed:
- ClinGen Male Infertility GCEP affiliation page: `https://www.clinicalgenome.org/affiliation/40073/`
- PMID:34718620
- PMID:36177363

Definition/modeling notes:
- The new term captures the shared SYCE1 etiology and the reported phenotype split across 46XY and 46XX individuals.
- I added the ClinGen preferred-label style exact synonym annotation to the new term.
- I used the existing verified HGNC identifier already present in MONDO for SYCE1: `http://identifiers.org/hgnc/28852`.

Validation completed:
- Checked the updated OBO structure by running:
  - `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o /tmp/mondo-edit.TMP.obo`
- Normalized the edit file by running:
  - `make -C src/ontology NORM`
  - replaced `src/ontology/mondo-edit.obo` with the normalized `NORM` output

Checklist completed:
- Added a new term with definition, provenance, and logical axiom
- Added subclass links from both existing SYCE1-specific terms
- Preserved existing classifications
- Normalized and syntax-checked the edited ontology file

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640352578)


#### Agent Issue Comment

Addressed in PR #<NN>.

Added `SYCE1-related gametogenic failure` as a new umbrella term and classified the existing sex-specific SYCE1 terms under it.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640352578)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8013937e4..fdc4958e7 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -385046,6 +385046,7 @@ xref: OMIM:616947 {source="MONDO:equivalentTo"}
 xref: UMLS:C4310782 {source="MEDGEN:934749", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease
 is_a: MONDO:0019852 {source="DC-OMIM:616947", source="OMIM:616947"} ! inherited primary ovarian failure
+is_a: MONDO:7770012 {source="PMID:34718620", source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1-related gametogenic failure
 intersection_of: MONDO:0019852 ! inherited primary ovarian failure
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="OMIM:616947"} ! SYCE1
@@ -385127,6 +385128,7 @@ xref: MEDGEN:934746 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: OMIM:616950 {source="MONDO:equivalentTo"}
 xref: UMLS:C4310779 {source="MEDGEN:934746", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0004983 {source="DC-OMIM:616950", source="DOID:0070172", source="MONDO:Redundant", source="OMIM:616950"} ! spermatogenic failure
+is_a: MONDO:7770012 {source="PMID:34718620", source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1-related gametogenic failure
 intersection_of: MONDO:0004983 ! spermatogenic failure
 intersection_of: disease_has_basis_in_dysfunction_of http://identifiers.org/hgnc/28852 ! SYCE1
 intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
@@ -665300,6 +665302,19 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: SYCE1-related gametogenic failure
+def: "A reproductive system disorder caused by a variation in the SYCE1 gene, and characterized by varying phenotypes including spermatogenic failure in 46XY individuals and primary ovarian insufficiency in 46XX individuals." [https://www.clinicalgenome.org/affiliation/40073/, PMID:34718620, PMID:36177363]
+comment: 46XY individuals can present with non-obstructive azoospermia due to maturation arrest or meiotic failure. 46XX individuals can present with primary ovarian insufficiency.
+synonym: "SYCE1-related gametogenic failure" EXACT [https://www.clinicalgenome.org/affiliation/40073/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0005039 {source="PMID:34718620", source="https://www.clinicalgenome.org/affiliation/40073/"} ! reproductive system disorder
+intersection_of: MONDO:0005039 ! reproductive system disorder
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 ! SYCE1
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="PMID:34718620"} ! SYCE1
+property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9864" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 7: claude-opus-4.7 / claude

- **Eval PR**: [#374](https://github.com/ai4curation/eval-ont-agent-mondo/pull/374)
- **F1**: 0.381  **Precision**: 0.364  **Recall**: 0.400  **Jaccard**: 0.235
- **Trace**: [25815891627](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25815891627)
- **Workflow run**: [25815891627](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25815891627)

#### Agent PR Comment

## Summary

Adds a new MONDO term **MONDO:7770012 SYCE1-related gametogenic failure** as requested in monarch-initiative/mondo#9864 by ClinGen's Male Infertility GCEP.

This is an umbrella / spectrum term covering the SYCE1-related disease that manifests as either spermatogenic failure (in 46XY individuals) or primary ovarian insufficiency (in 46XX individuals). The two existing OMIM-derived sex-specific terms remain in place:

- MONDO:0014844 premature ovarian failure 12 (POF12, OMIM:616947)
- MONDO:0014847 spermatogenic failure 15 (SPGF15, OMIM:616950)

#### Agent Issue Comment

Thanks for the request. A new term **MONDO:7770012 SYCE1-related gametogenic failure** has been added in PR #<NN>.

Summary of what was created:
- **Label:** SYCE1-related gametogenic failure
- **Definition:** "Individuals with variants in SYCE1 may present with varying phenotypes. 46XY individuals can present with non-obstructive azoospermia due to maturation arrest/meiotic failure. 46XX individuals can present with primary ovarian insufficiency (POI)."
- **Parents** (union of the parents of MONDO:0014844 and MONDO:0014847, as requested):
  - MONDO:0003847 hereditary disease
  - MONDO:0019852 inherited primary ovarian failure
  - MONDO:0004983 spermatogenic failure
- **Gene relationship:** `has_material_basis_in_germline_mutation_in` HGNC:28852 (SYCE1)
- Source attribution uses the ClinGen Male Infertility GCEP affiliation URL provided in the issue comments.

@ErinRiggs @GabrielleGCA — could you confirm:
1. Are the three is_a parents above what you wanted, or would you prefer only a subset (e.g. drop `hereditary disease` since it is redundant with the others)?
2. Are there any preferred synonyms or abbreviations (e.g. similar to MDCD / SPGF15 / POF12) we should add?
3. Is there a PMID you would like cited in the definition in addition to / instead of the ClinGen affiliation URL?

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25815891627)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8013937e4..4333d77c2 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -665300,6 +665300,17 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: SYCE1-related gametogenic failure
+def: "Individuals with variants in SYCE1 may present with varying phenotypes. 46XY individuals can present with non-obstructive azoospermia due to maturation arrest/meiotic failure. 46XX individuals can present with primary ovarian insufficiency (POI)." [https://www.clinicalgenome.org/affiliation/40073/]
+subset: rare
+is_a: MONDO:0003847 ! hereditary disease
+is_a: MONDO:0004983 ! spermatogenic failure
+is_a: MONDO:0019852 ! inherited primary ovarian failure
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9864" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 8: kimi-k2.6 / opencode

- **Eval PR**: [#279](https://github.com/ai4curation/eval-ont-agent-mondo/pull/279)
- **F1**: 0.348  **Precision**: 0.364  **Recall**: 0.333  **Jaccard**: 0.211
- **Workflow run**: [25755577726](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755577726)

#### Agent PR Comment

## Summary

Added a new MONDO term for **SYCE1-related gametogenic failure** as requested by ClinGen's Male Infertility GCEP (affiliation 40073).

### New Term

- **ID:** MONDO:7770012
- **Name:** SYCE1-related gametogenic failure
- **Definition:** Any hereditary disease in which the cause of the disease is a mutation in the SYCE1 gene. Individuals with pathogenic variants in SYCE1 may present with gametogenic failure; 46,XY individuals can present with non-obstructive azoospermia due to maturation arrest or meiotic failure, and 46,XX individuals can present with primary ovarian insufficiency.
- **Parents:**
  - `MONDO:0003847` (hereditary disease)
  - `MONDO:0005039` (reproductive system disorder)
- **ClinGen label:** Marked with `OMO:0002001="https://w3id.org/information-resource-registry/clingen"`
- **Gene relationship:** `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852` (SYCE1)
- **Issue tracker:** `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9864"`

### Rationale for Parent Terms

The requester asked that the new term have the same parents as both:
- MONDO:0014844 (premature ovarian failure 12 / SYCE1-related)
- MONDO:0014847 (spermatogenic failure 15 / SYCE1-related)

However, adding both `inherited primary ovarian failure` and `spermatogenic failure` as direct parents to a single term is biologically unsound, because a given individual cannot simultaneously be 46,XX and 46,XY. Instead, I selected the common appropriate ancestors that encompass both phenotypes:
- **Hereditary disease** (`MONDO:0003847`) — both conditions are inherited genetic disorders caused by SYCE1 mutations.
- **Reproductive system disorder** (`MONDO:0005039`) — both conditions manifest as failure of gamete production within the reproductive system.

This approach is consistent with other ClinGen-curated broad gene-related disease terms in MONDO (e.g., `SAMD9-related spectrum and myeloid neoplasm risk`, `HDAC4-related haploinsufficiency syndrome`), which use a single broad disease category rather than multiple phenotype-specific parents.

### References Used

- PMID:34718620 — *Variations of C14ORF39 and SYCE1 Identified in Idiopathic Premature Ovarian Insufficiency and Nonobstructive Azoospermia* (directly links SYCE1 to both phenotypes in the same study)
- OMIM:616947 — premature ovarian failure 12
- OMIM:616950 — spermatogenic failure 15
- ClinGen Male Infertility GCEP: https://www.clinicalgenome.org/affiliation/40073/

### Checklist

- [x] Reviewed issue request and ClinGen affiliation
- [x] Researched SYCE1 gene and existing MONDO terms (MONDO:0014844, MONDO:0014847)
- [x] Verified HGNC identifier for SYCE1 (`http://identifiers.org/hgnc/28852`)
- [x] Located supporting literature (PMID:34718620)
- [x] Created new term stanza in `terms/MONDO_7770012.obo`
- [x] Checked in with `obo-checkin.pl`
- [x] Validated OBO syntax with `robot convert` inside ODK docker
- [x] Normalized serialization with `make NORM`
- [x] Verified term appears correctly in normalized `mondo-edit.obo`
- [x] Committed changes


---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755577726)


#### Agent Issue Comment

Hi all,

The requested term **SYCE1-related gametogenic failure** has been added to MONDO as **MONDO:7770012**.

The term has been created with:
- Parent terms: `hereditary disease` and `reproductive system disorder`, which appropriately encompass both the 46,XX and 46,XY phenotypes (primary ovarian insufficiency and non-obstructive azoospermia, respectively).
- Gene relationship to SYCE1 (`http://identifiers.org/hgnc/28852`).
- References: PMID:34718620, OMIM:616947, OMIM:616950, and the ClinGen Male Infertility GCEP affiliation (https://www.clinicalgenome.org/affiliation/40073/).
- The ClinGen label flagged with `OMO:0002001`.

The ClinGen label and definition were taken directly from the issue request. Please let us know if any adjustments are needed.

Changes committed in PR #<NN>.

cc: @ErinRiggs 

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755577726)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8013937e4..017ace4fa 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -665300,6 +665300,19 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: SYCE1-related gametogenic failure
+def: "Any hereditary disease in which the cause of the disease is a mutation in the SYCE1 gene. Individuals with pathogenic variants in SYCE1 may present with gametogenic failure; 46,XY individuals can present with non-obstructive azoospermia due to maturation arrest or meiotic failure, and 46,XX individuals can present with primary ovarian insufficiency." [https://www.clinicalgenome.org/affiliation/40073/, OMIM:616947, OMIM:616950, PMID:34718620]
+synonym: "SYCE1 related gametogenic failure" EXACT [MONDO:design_pattern]
+synonym: "SYCE1-related gametogenic failure" EXACT [] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0003847 {source="https://www.clinicalgenome.org/affiliation/40073/"} ! hereditary disease
+is_a: MONDO:0005039 {source="https://www.clinicalgenome.org/affiliation/40073/"} ! reproductive system disorder
+relationship: disease_has_basis_in_dysfunction_of http://identifiers.org/hgnc/28852 {source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28852 {source="PMID:34718620", source="https://www.clinicalgenome.org/affiliation/40073/"} ! SYCE1
+property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9864" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```
