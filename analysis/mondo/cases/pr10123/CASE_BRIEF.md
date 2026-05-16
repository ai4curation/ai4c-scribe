---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9877
pr_number: 10123
issue_title: GPR161-related medulloblastoma predisposition
pr_author: katiermullen
pr_merged_at: '2026-04-06'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-15'
scoping_notes: PR adds exactly one new disease term with no unrelated changes.
domain_area: cancer-predisposition
best_f1: 0.545
best_model: gpt-5.5
---

# PR #10123 — GPR161-related medulloblastoma predisposition

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9877](https://github.com/monarch-initiative/mondo/issues/9877) | [PR #10123](https://github.com/monarch-initiative/mondo/pull/10123) | @katiermullen | merged 2026-04-06

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for GPR161-related medulloblastoma predisposition. GPR161 is a G protein-coupled receptor involved in the Hedgehog signaling pathway, and germline mutations predispose to medulloblastoma, a common pediatric brain tumor. This term captures the genetic predisposition rather than the cancer itself, requiring careful placement in the ontology hierarchy.

## Changes Made

Added a new term stanza to `src/ontology/mondo-edit.obo` with 10 lines. The term includes a definition, gene-disease logical axioms linking to GPR161, and classification under the cancer predisposition hierarchy. The compact size reflects a well-structured new term following established patterns.

## Resolution

Medium difficulty because cancer predisposition terms require dual classification: they must be linked to both the cancer type (medulloblastoma) and the predisposition concept, while also encoding the causal gene relationship. An agent needs to understand the distinction between a cancer and a predisposition to cancer and apply the correct Mondo pattern.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 819fd34156..07692c19ee 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -631093,6 +631093,16 @@ intersection_of: MONDO:0005583 {source="https://orcid.org/0000-0002-5002-8648"}
 intersection_of: MONDO:0700097 MONDO:0019127 {source="https://orcid.org/0000-0002-5002-8648"} ! cross-species analog polymyositis
 relationship: excluded_from_qc_check http://purl.obolibrary.org/obo/mondo/sparql/qc/general/qc-single-child.sparql
 
+[Term]
+id: MONDO:1010204
+name: GPR161-related medulloblastoma predisposition
+def: "A predisposition to medulloblastoma, a tumor that originates in the cerebellum and dorsal brainstem, has a peak incidence in childhood, and makes up a large proportion of embryonal brain tumors due to a variation in the GPR161 gene." [https://clinicalgenome.org/affiliation/40157/]
+synonym: "GPR161-related medulloblastoma predisposition" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0015356 {source="https://clinicalgenome.org/affiliation/40157/"} ! hereditary neoplastic syndrome
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 {source="https://clinicalgenome.org/affiliation/40157/"}
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-5002-8648
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
+
 [Term]
 id: MONDO:1010208
 name: myofibrillar myopathy, non-human animal

```

## Agent Attempts (9)

### Attempt 1: gpt-5.5 / opencode

- **Eval PR**: [#78](https://github.com/ai4curation/eval-ont-agent-mondo/pull/78)
- **F1**: 0.545  **Precision**: 0.667  **Recall**: 0.462  **Jaccard**: 0.375
- **Trace**: [25615976305](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615976305)
- **Workflow run**: [25615976305](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615976305)

#### Agent PR Comment

## Summary

Added a new MONDO term for the ClinGen-priority request:

- `MONDO:7770012` — **GPR161-related medulloblastoma predisposition**

## Rationale and curation notes

- Modeled the term using the MONDO `susceptibility_by_gene` pattern.
- Classified the term under `inherited disease susceptibility` (`MONDO:0020573`).
- Added logical axioms/relationships for:
  - material basis in germline mutation in **GPR161** (`http://identifiers.org/hgnc/23694`)
  - predisposition toward `medulloblastoma` (`MONDO:0007959`)
- Added a ClinGen preferred-label synonym annotation for the requested label.
- Added a pattern-based synonym: `medulloblastoma susceptibility, GPR161 form`.
- Added the issue tracker item annotation pointing to issue #9877.

## Checks performed

- Checked for existing `GPR161` mentions in `mondo-edit.obo`; none were found.
- Verified the target parent terms:
  - `MONDO:0020573` inherited disease susceptibility
  - `MONDO:0007959` medulloblastoma
- Verified the human gene identifier for GPR161 via HGNC REST API: `HGNC:23694`.
- Checked for new-term ID clashes among `MONDO:777` IDs and used the next available ID, `MONDO:7770012`.
- Ran normalization with `make NORM && mv NORM mondo-edit.obo` from `src/ontology`.
- Ran OBO syntax validation with `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo` successfully.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615976305)


#### Agent Issue Comment

Added the new term `GPR161-related medulloblastoma predisposition` as `MONDO:7770012`; changes committed in PR #<NN>.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615976305)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 819fd3415..69a1692ff 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -660295,6 +660295,20 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: GPR161-related medulloblastoma predisposition
+def: "A susceptibility or predisposition to medulloblastoma in which the cause of the disease is a mutation in the GPR161 gene." [https://clinicalgenome.org/affiliation/40157/, MONDO:patterns/susceptibility_by_gene]
+synonym: "GPR161-related medulloblastoma predisposition" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+synonym: "medulloblastoma susceptibility, GPR161 form" EXACT [MONDO:patterns/susceptibility_by_gene]
+is_a: MONDO:0020573 {source="https://clinicalgenome.org/affiliation/40157/"} ! inherited disease susceptibility
+intersection_of: MONDO:0020573 ! inherited disease susceptibility
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694
+intersection_of: predisposes_towards MONDO:0007959 ! medulloblastoma
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 {source="https://clinicalgenome.org/affiliation/40157/"}
+relationship: predisposes_towards MONDO:0007959 {source="https://clinicalgenome.org/affiliation/40157/"} ! medulloblastoma
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 2: gpt-5.5 / opencode

- **Eval PR**: [#59](https://github.com/ai4curation/eval-ont-agent-mondo/pull/59)
- **F1**: 0.545  **Precision**: 0.667  **Recall**: 0.462  **Jaccard**: 0.375
- **Trace**: [25615933855](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615933855)
- **Workflow run**: [25615933855](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615933855)

#### Agent PR Comment

## Summary

Added a new MONDO term for issue #9877:

- `MONDO:7770012` `GPR161-related medulloblastoma predisposition`

#### Agent Issue Comment

Added `GPR161-related medulloblastoma predisposition` as a new MONDO susceptibility term in PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615933855)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 819fd3415..69a1692ff 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -660295,6 +660295,20 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: GPR161-related medulloblastoma predisposition
+def: "A susceptibility or predisposition to medulloblastoma in which the cause of the disease is a mutation in the GPR161 gene." [https://clinicalgenome.org/affiliation/40157/, MONDO:patterns/susceptibility_by_gene]
+synonym: "GPR161-related medulloblastoma predisposition" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+synonym: "medulloblastoma susceptibility, GPR161 form" EXACT [MONDO:patterns/susceptibility_by_gene]
+is_a: MONDO:0020573 {source="https://clinicalgenome.org/affiliation/40157/"} ! inherited disease susceptibility
+intersection_of: MONDO:0020573 ! inherited disease susceptibility
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694
+intersection_of: predisposes_towards MONDO:0007959 ! medulloblastoma
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 {source="https://clinicalgenome.org/affiliation/40157/"}
+relationship: predisposes_towards MONDO:0007959 {source="https://clinicalgenome.org/affiliation/40157/"} ! medulloblastoma
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 3: claude-opus-4.7 / claude

- **Eval PR**: [#389](https://github.com/ai4curation/eval-ont-agent-mondo/pull/389)
- **F1**: 0.526  **Precision**: 0.556  **Recall**: 0.500  **Jaccard**: 0.357
- **Trace**: [25817698085](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25817698085)
- **Workflow run**: [25817698085](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817698085)

#### Agent PR Comment

# GPR161-related medulloblastoma predisposition (MONDO:7770012)

Addresses issue #9877 — a ClinGen priority NTR for a new gene-related cancer
predisposition term.

#### Agent Issue Comment

Thanks for the request. The new term **GPR161-related medulloblastoma predisposition** has been added as `MONDO:7770012` in PR #<NN>.

Logical structure follows the `susceptibility_by_gene` design pattern (parent: `MONDO:0020573 inherited disease susceptibility`, `predisposes_towards MONDO:0007959 medulloblastoma`, `has_material_basis_in_germline_mutation_in HGNC:23694 GPR161`). Citation: ClinGen affiliation 40157 and PMID:31609649 (Begemann et al. 2020, *J Clin Oncol*, "Germline GPR161 Mutations Predispose to Pediatric Medulloblastoma").

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817698085)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 819fd3415..a3cebce6c 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -660295,6 +660295,17 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: GPR161-related medulloblastoma predisposition
+def: "A susceptibility or predisposition to medulloblastoma in which the cause of the disease is a mutation in the GPR161 gene." [https://clinicalgenome.org/affiliation/40157/, MONDO:patterns/susceptibility_by_gene, PMID:31609649]
+synonym: "GPR161-related medulloblastoma predisposition" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0020573 {source="https://clinicalgenome.org/affiliation/40157/"} ! inherited disease susceptibility
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 {source="https://clinicalgenome.org/affiliation/40157/", source="PMID:31609649"} ! GPR161
+relationship: predisposes_towards MONDO:0007959 {source="https://clinicalgenome.org/affiliation/40157/", source="PMID:31609649"} ! medulloblastoma
+property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 4: gpt-5.5 / codex

- **Eval PR**: [#39](https://github.com/ai4curation/eval-ont-agent-mondo/pull/39)
- **F1**: 0.455  **Precision**: 0.556  **Recall**: 0.385  **Jaccard**: 0.294
- **Trace**: [25615869975](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615869975)
- **Workflow run**: [25615869975](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615869975)

#### Agent PR Comment

## Summary

Added a new MONDO term for the ClinGen priority disease name requested in issue #9877:

- `MONDO:7770012` GPR161-related medulloblastoma predisposition

## Rationale

The new term is modeled as a hereditary neoplastic syndrome / inherited disease susceptibility. It uses `predisposes_towards MONDO:0007959` for medulloblastoma rather than making medulloblastoma a parent, consistent with susceptibility-term modeling.

The GPR161 gene identifier was verified against HGNC as `HGNC:23694`, represented as `http://identifiers.org/hgnc/23694`. The definition and relationships are sourced to ClinGen Pediatric Cancer GCEP (`https://clinicalgenome.org/affiliation/40157/`) and Begemann et al. PMID:31609649, which reports germline GPR161 mutations predisposing to pediatric/infant-onset SHH-activated medulloblastoma.

## Completed Checklist

- Checked for existing GPR161-related MONDO content.
- Checked the existing medulloblastoma term and susceptibility/neoplastic syndrome parent terms.
- Checked the `susceptibility_by_gene` design pattern.
- Verified the GPR161 HGNC identifier.
- Reviewed publication metadata/full-text availability for PMID:31609649. `aurelian` was unavailable in this environment, so I used PubMed/NCBI metadata and the open PMC full text.
- Added issue tracker metadata linking to issue #9877.
- Normalized the ontology serialization with the local `make NORM` target and moved `NORM` back to `mondo-edit.obo`. Docker was not installed, so `src/ontology/run.sh` could not be used.
- Validated OBO syntax with `robot convert --catalog catalog-v001.xml -i mondo-edit.obo -f obo -o mondo-edit.TMP.obo`.


---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615869975)


#### Agent Issue Comment

Created MONDO:7770012 for GPR161-related medulloblastoma predisposition. Changes committed in PR #<NN>.


---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615869975)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 819fd3415..ebdd14cc3 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -660295,6 +660295,20 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: GPR161-related medulloblastoma predisposition
+def: "A susceptibility or predisposition to medulloblastoma in which the cause of the disease is a germline mutation in the GPR161 gene. GPR161-related medulloblastoma predisposition has been reported in association with infant-onset SHH-activated medulloblastoma." [https://clinicalgenome.org/affiliation/40157/, PMID:31609649]
+subset: rare
+synonym: "GPR161-related medulloblastoma predisposition" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+is_a: MONDO:0015356 {source="PMID:31609649", source="https://clinicalgenome.org/affiliation/40157/"} ! hereditary neoplastic syndrome
+intersection_of: MONDO:0020573 ! inherited disease susceptibility
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694
+intersection_of: predisposes_towards MONDO:0007959 ! medulloblastoma
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 {source="PMID:31609649", source="https://clinicalgenome.org/affiliation/40157/"}
+relationship: predisposes_towards MONDO:0007959 {source="PMID:31609649", source="https://clinicalgenome.org/affiliation/40157/"} ! medulloblastoma
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 5: claude-sonnet-4.5 / copilot

- **Eval PR**: [#534](https://github.com/ai4curation/eval-ont-agent-mondo/pull/534)
- **F1**: 0.333  **Precision**: 0.444  **Recall**: 0.267  **Jaccard**: 0.200

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 819fd3415..67a476f2c 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -660295,6 +660295,22 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: GPR161-related medulloblastoma predisposition
+def: "A susceptibility or predisposition to medulloblastoma in which the cause of the disease is a mutation in the GPR161 gene." [https://clinicalgenome.org/affiliation/40157/, PMID:36961676]
+subset: predisposition
+synonym: "medulloblastoma susceptibility caused by GPR161" EXACT [MONDO:patterns/susceptibility_by_gene]
+synonym: "medulloblastoma susceptibility, GPR161 form" EXACT [MONDO:patterns/susceptibility_by_gene]
+is_a: MONDO:0020573 ! inherited disease susceptibility
+intersection_of: MONDO:0020573 ! inherited disease susceptibility
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694
+intersection_of: predisposes_towards MONDO:0007959 ! medulloblastoma
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 {source="PMID:36961676", source="https://clinicalgenome.org/affiliation/40157/"}
+relationship: predisposes_towards MONDO:0007959 {source="PMID:36961676", source="https://clinicalgenome.org/affiliation/40157/"} ! medulloblastoma
+property_value: http://purl.org/dc/terms/creator https://clinicalgenome.org/affiliation/40157/
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 6: claude-sonnet-4.5 / copilot

- **Eval PR**: [#492](https://github.com/ai4curation/eval-ont-agent-mondo/pull/492)
- **F1**: 0.333  **Precision**: 0.444  **Recall**: 0.267  **Jaccard**: 0.200

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 819fd3415..67a476f2c 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -660295,6 +660295,22 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: GPR161-related medulloblastoma predisposition
+def: "A susceptibility or predisposition to medulloblastoma in which the cause of the disease is a mutation in the GPR161 gene." [https://clinicalgenome.org/affiliation/40157/, PMID:36961676]
+subset: predisposition
+synonym: "medulloblastoma susceptibility caused by GPR161" EXACT [MONDO:patterns/susceptibility_by_gene]
+synonym: "medulloblastoma susceptibility, GPR161 form" EXACT [MONDO:patterns/susceptibility_by_gene]
+is_a: MONDO:0020573 ! inherited disease susceptibility
+intersection_of: MONDO:0020573 ! inherited disease susceptibility
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694
+intersection_of: predisposes_towards MONDO:0007959 ! medulloblastoma
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 {source="PMID:36961676", source="https://clinicalgenome.org/affiliation/40157/"}
+relationship: predisposes_towards MONDO:0007959 {source="PMID:36961676", source="https://clinicalgenome.org/affiliation/40157/"} ! medulloblastoma
+property_value: http://purl.org/dc/terms/creator https://clinicalgenome.org/affiliation/40157/
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 7: kimi-k2.6 / opencode

- **Eval PR**: [#250](https://github.com/ai4curation/eval-ont-agent-mondo/pull/250)
- **F1**: 0.333  **Precision**: 0.444  **Recall**: 0.267  **Jaccard**: 0.200
- **Trace**: [25755519495](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25755519495)
- **Workflow run**: [25755519495](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755519495)

#### Agent PR Comment

# Add GPR161-related medulloblastoma predisposition (MONDO:7770012)

## Summary
Created a new MONDO term for the ClinGen-priority request to represent germline GPR161-related predisposition to medulloblastoma.

## New Term Details
- **ID:** MONDO:7770012
- **Name:** GPR161-related medulloblastoma predisposition
- **Definition:** A susceptibility or predisposition to medulloblastoma in which the cause of the disease is a mutation in the GPR161 gene. Medulloblastoma is a tumor that originates in the cerebellum and dorsal brainstem, has a peak incidence in childhood, and makes up a large proportion of embryonal brain tumors.
- **Definition sources:** PMID:31609649, https://clinicalgenome.org/affiliation/40157/
- **Parent:** MONDO:0020573 ! inherited disease susceptibility
- **Logical definition:**
  - `intersection_of: MONDO:0020573 ! inherited disease susceptibility`
  - `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694`
  - `intersection_of: predisposes_towards MONDO:0007959 ! medulloblastoma`
- **Subsets:** clingen, predisposition
- **Synonym:** medulloblastoma susceptibility, GPR161 form (EXACT)
- **Term tracker:** https://github.com/monarch-initiative/mondo/issues/9877

## Background Research & Verification
1. **Gene identifier verification:**
   - Queried HGNC REST API for GPR161.
   - Confirmed HGNC ID: **HGNC:23694** (G protein-coupled receptor 161).
   - Constructed URI: `http://identifiers.org/hgnc/23694`.

2. **Literature review:**
   - Identified primary supporting publication: **PMID:31609649** (*Begemann et al., J Clin Oncol. 2020* — "Germline GPR161 Mutations Predispose to Pediatric Medulloblastoma").
   - Verified in PubMed that GPR161 is established as a childhood medulloblastoma predisposition gene (also supported by subsequent literature such as PMID:39184053).

3. **Design pattern compliance:**
   - Reviewed `src/patterns/dosdp-patterns/susceptibility_by_gene.yaml`.
   - Applied the genus–differentia logical definition: *inherited disease susceptibility* that (*has material basis in germline mutation in* GPR161) and (*predisposes towards* medulloblastoma).
   - Named using the modern MONDO gene-related convention requested by ClinGen, while adding the pattern-based exact synonym for completeness.

4. **Parent term consistency:**
   - Checked `MONDO:0020573` (inherited disease susceptibility) and `MONDO:0007959` (medulloblastoma) for correctness.
   - Ensured `predisposes_towards` relationship points to the actual disease term, not to the susceptibility parent.

## Curator Checklist
- [x] Verified gene identifier via HGNC.
- [x] Checked design pattern (`susceptibility_by_gene.yaml`).
- [x] Provided definition with at least one literature xref (PMID:31609649).
- [x] Included ClinGen affiliation URL as source.
- [x] Added logical definition (`intersection_of` axioms).
- [x] Added appropriate source attribution to all logical axioms.
- [x] Linked back to originating GitHub issue (term tracker item).
- [x] Ran `obo-checkout.pl` / `obo-checkin.pl` workflow (terms directory).
- [x] Normalized serialisation via `make NORM` (ODK v1.6).
- [x] Validated OBO syntax via `robot convert` (ODK v1.6) — no errors.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755519495)


#### Agent Issue Comment

Thank you for the GPR161-related medulloblastoma predisposition term request. 

The new term has been created as **MONDO:7770012** and committed in PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755519495)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 819fd3415..07ce38fd9 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -660295,6 +660295,22 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: GPR161-related medulloblastoma predisposition
+def: "A susceptibility or predisposition to medulloblastoma in which the cause of the disease is a mutation in the GPR161 gene. Medulloblastoma is a tumor that originates in the cerebellum and dorsal brainstem, has a peak incidence in childhood, and makes up a large proportion of embryonal brain tumors." [https://clinicalgenome.org/affiliation/40157/, PMID:31609649]
+subset: clingen {source="MONDO:CLINGEN"}
+subset: predisposition
+synonym: "medulloblastoma susceptibility, GPR161 form" EXACT [https://clinicalgenome.org/affiliation/40157/]
+is_a: MONDO:0020573 {source="PMID:31609649", source="https://clinicalgenome.org/affiliation/40157/"} ! inherited disease susceptibility
+intersection_of: MONDO:0020573 ! inherited disease susceptibility
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694
+intersection_of: predisposes_towards MONDO:0007959 ! medulloblastoma
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 {source="PMID:31609649", source="https://clinicalgenome.org/affiliation/40157/"}
+relationship: predisposes_towards MONDO:0007959 {source="PMID:31609649", source="https://clinicalgenome.org/affiliation/40157/"} ! medulloblastoma
+property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 8: claude-sonnet-4.5 / claude

- **Eval PR**: [#440](https://github.com/ai4curation/eval-ont-agent-mondo/pull/440)
- **F1**: 0.320  **Precision**: 0.444  **Recall**: 0.250  **Jaccard**: 0.190
- **Trace**: [25867704846](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25867704846)
- **Workflow run**: [25867704846](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867704846)

#### Agent PR Comment

## Summary

This PR adds a new term for **GPR161-related medulloblastoma predisposition** (MONDO:7770012) in response to a priority ClinGen disease name request (issue #9877).

#### Agent Issue Comment

Thank you for submitting this priority ClinGen disease name request! 

I've successfully created the new term **GPR161-related medulloblastoma predisposition** (MONDO:7770012) with the following details:

- **Label**: GPR161-related medulloblastoma predisposition
- **MONDO ID**: MONDO:7770012
- **Definition**: Based on PMID:31609649 (Germline GPR161 Mutations Predispose to Pediatric Medulloblastoma) and includes details about the sonic hedgehog medulloblastoma (MBSHH) subgroup
- **Parent term**: inherited disease susceptibility (MONDO:0020573)
- **Gene identifier**: HGNC:23694 (GPR161)
- **Relationships**: 
  - has_material_basis_in_germline_mutation_in GPR161
  - predisposes_towards medulloblastoma (MONDO:0007959)
- **Attribution**: ClinGen affiliation 40157

The term follows MONDO's susceptibility_by_gene design pattern and includes appropriate synonyms and metadata.

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867704846)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 819fd3415..54e764363 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -660295,6 +660295,23 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: GPR161-related medulloblastoma predisposition
+def: "A susceptibility or predisposition to medulloblastoma in which the cause of the disease is a germline mutation in the GPR161 gene. GPR161 mutations define a novel brain tumor predisposition syndrome characterized by medulloblastoma in infants, typically with onset in the first years of life. The mutations are exclusively associated with the sonic hedgehog medulloblastoma (MBSHH) subgroup." [https://clinicalgenome.org/affiliation/40157/, PMID:31609649]
+subset: predisposition
+synonym: "GPR161 tumor predisposition syndrome" EXACT [PMID:31609649]
+synonym: "medulloblastoma susceptibility, GPR161 form" EXACT [MONDO:design_pattern]
+synonym: "medulloblastoma susceptibility caused by GPR161" EXACT [MONDO:design_pattern]
+is_a: MONDO:0020573 {source="PMID:31609649"} ! inherited disease susceptibility
+intersection_of: MONDO:0020573 ! inherited disease susceptibility
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 ! GPR161
+intersection_of: predisposes_towards MONDO:0007959 ! medulloblastoma
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 {source="PMID:31609649"} ! GPR161
+relationship: predisposes_towards MONDO:0007959 {source="PMID:31609649"} ! medulloblastoma
+property_value: http://purl.org/dc/terms/creator https://clinicalgenome.org/affiliation/40157/
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```

### Attempt 9: gpt-5.4 / codex

- **Eval PR**: [#174](https://github.com/ai4curation/eval-ont-agent-mondo/pull/174)
- **F1**: 0.320  **Precision**: 0.444  **Recall**: 0.250  **Jaccard**: 0.190
- **Workflow run**: [25640353820](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640353820)

#### Agent PR Comment

Implemented issue #9877 by adding a new MONDO term:

- `MONDO:7770012` `GPR161-related medulloblastoma predisposition`

Rationale:

- The issue requested the ClinGen-preferred gene-related label, so I used `GPR161-related medulloblastoma predisposition` as the primary name rather than an older autogenerated susceptibility-style label.
- I modeled the term as both `hereditary neoplastic syndrome` and `inherited disease susceptibility`.
- I added logical support with:
  - `intersection_of: MONDO:0020573` (`inherited disease susceptibility`)
  - `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694`
  - `intersection_of: predisposes_towards MONDO:0007959` (`medulloblastoma`)
- I added asserted relationships for germline `GPR161` causation and `predisposes_towards medulloblastoma`.

Sources checked:

- ClinGen affiliation supplied in the issue: `https://clinicalgenome.org/affiliation/40157/`
- PMID:31609649, `Germline GPR161 Mutations Predispose to Pediatric Medulloblastoma`
- NCBI Gene for human `GPR161` to verify the gene identifier used in the axiom (`HGNC:23694`; NCBI Gene ID 23432)

Validation completed:

- Checked existing MONDO context for `medulloblastoma`, `GPR161`, and susceptibility/predisposition modeling.
- Allocated the next free NTR identifier in the local `MONDO:777xxxx` range: `MONDO:7770012`.
- Checked the term into `src/ontology/mondo-edit.obo`.
- Ran local normalization with `make NORM` and replaced `src/ontology/mondo-edit.obo` with the normalized output.
- Ran syntax conversion validation with:
  - `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o /tmp/mondo-edit.normalized.TMP.obo`

Completed checklist:

- [x] Read imported issue context from `__issue_context__.json`
- [x] Verified publication support
- [x] Verified gene identifier
- [x] Added new term in MONDO
- [x] Normalized serialization
- [x] Ran syntax validation
- [x] Committed only the ontology edit

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640353820)


#### Agent Issue Comment

Added new term `MONDO:7770012` for `GPR161-related medulloblastoma predisposition` and committed the change in PR #<NN>.

The term is modeled as an inherited cancer predisposition with `predisposes_towards` `medulloblastoma`, with provenance from ClinGen (`https://clinicalgenome.org/affiliation/40157/`) and PMID:31609649.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640353820)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 819fd3415..77e166eb3 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -660295,6 +660295,23 @@ def: "A grouping class for human diseases classified by their underlying molecul
 comment: This term is intended solely for classification purposes and should not be used for direct data annotation.
 is_a: MONDO:0700096 ! human disease
 
+[Term]
+id: MONDO:7770012
+name: GPR161-related medulloblastoma predisposition
+def: "An inherited disease susceptibility in which the cause of the disease is a germline mutation in the GPR161 gene and that predisposes towards medulloblastoma, particularly infant sonic hedgehog medulloblastoma." [https://clinicalgenome.org/affiliation/40157/, PMID:31609649]
+subset: predisposition
+synonym: "medulloblastoma susceptibility caused by GPR161" EXACT [MONDO:design_pattern]
+is_a: MONDO:0015356 {source="PMID:31609649", source="https://clinicalgenome.org/affiliation/40157/"} ! hereditary neoplastic syndrome
+is_a: MONDO:0020573 {source="PMID:31609649", source="https://clinicalgenome.org/affiliation/40157/"} ! inherited disease susceptibility
+intersection_of: MONDO:0020573 ! inherited disease susceptibility
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694
+intersection_of: predisposes_towards MONDO:0007959 ! medulloblastoma
+relationship: has_characteristic MONDO:0021152 {source="PMID:31609649"} ! inherited
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/23694 {source="PMID:31609649"}
+relationship: predisposes_towards MONDO:0007959 {source="PMID:31609649"} ! medulloblastoma
+property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9877" xsd:anyURI
+
 [Term]
 id: MONDO:8000000
 name: infectious discitis

```
