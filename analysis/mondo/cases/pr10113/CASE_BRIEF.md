---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9861
pr_number: 10113
issue_title: '[NTR/gene] Hyperinsulinemic hypoglycemia, familial 3'
pr_author: MeeSiing
pr_merged_at: '2026-04-02'
task_type: other
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 10
generated_at: '2026-05-15'
scoping_notes: PR relabels an existing term and updates its classification and synonyms
  based on user request.
domain_area: metabolic-disease
best_f1: 0.421
best_model: kimi-k2.6
---

# PR #10113 — [NTR/gene] Hyperinsulinemic hypoglycemia, familial 3

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9861](https://github.com/monarch-initiative/mondo/issues/9861) | [PR #10113](https://github.com/monarch-initiative/mondo/pull/10113) | @MeeSiing | merged 2026-04-02

`other` `medium` `tightly_scoped` `changes_requested`

## Context

A user requested a new gene-disease term for "hyperinsulinemic hypoglycemia, familial 3" (GCK-related hyperinsulinism) under issue #9861. During curation, it was determined that the existing term MONDO:0011236 already represented this disease but carried an outdated label. Rather than creating a duplicate, the curator updated the label and synonyms of the existing term. The PR also replaced an earlier failed attempt (PR #10090) that had git conflicts.

## Changes Made

The PR modified MONDO:0011236 in `src/ontology/mondo-edit.obo` with 13 additions and 6 deletions across 6 commits. Changes included updating the rdfs:label to "hyperinsulinemic hypoglycemia, familial, 3", adding "GCK-related hyperinsulinism" as an exact synonym, and adjusting the classification under MONDO:0017182 "familial hyperinsulinism." The multiple commits reflect both the review iteration (a CHANGES_REQUESTED review asking about classification) and the recreation of the PR after rebasing issues.

## Resolution

Medium difficulty because the curator needed to recognize that an existing term matched the new term request rather than creating a duplicate. The review process involved a classification question from the reviewer, requiring the contributor to confirm that the OMIM entry and the requested term were the same concept. An agent would need to search for existing terms before creating new ones and handle reviewer questions about hierarchical placement.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 70c79e85cd..819fd34156 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -280521,8 +280521,8 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011236
-name: hyperinsulinism due to glucokinase deficiency
-def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold for insulin release, characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of profound hypoglycemia induced by fasting and protein rich meals, requiring rapid and intensive treatment to prevent neurological sequelae." [Orphanet:79299]
+name: hyperinsulinemic hypoglycemia, familial, 3
+def: "A form of diffuse hyperinsulinism due to glucokinase hyperactivity associated with a variation in the GCK gene, and characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of hypoglycemia induced by fasting and glucose rich meals." [https://clinicalgenome.org/affiliation/40016/, Orphanet:79299, PMID:15277402, PMID:24890200, PMID:34680961]
 subset: doid {source="DOID:0070216"}
 subset: doid_rare {source="DOID:0070216"}
 subset: gard_rare {source="GARD:0002818", source="MONDO:GARD"}
@@ -280533,10 +280533,15 @@ subset: orphanet {source="Orphanet:79299"}
 subset: orphanet_rare {source="Orphanet:79299"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]
-synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]
-synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]
+synonym: "congenital glucokinase-related hyperinsulinism" EXACT [Orphanet:79299]
+synonym: "GCK-related hyperinsulinism" EXACT [https://clinicalgenome.org/affiliation/40016/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+synonym: "glucokinase-related hyperinsulinemic hypoglycemia" EXACT [Orphanet:79299]
+synonym: "HHF3" EXACT ABBREVIATION [MONDO:Lexical, OMIM:602485]
+synonym: "hyperinsulinemic hypoglycemia due to glucokinase deficiency" EXACT [DOID:0070216]
+synonym: "hyperinsulinemic hypoglycemia familial 3" EXACT [GARD:0009930]
+synonym: "hyperinsulinemic hypoglycemia, familial, 3" EXACT [MONDO:Lexical]
 synonym: "hyperinsulinemic hypoglycemia, familial, type 3" EXACT [MONDO:RULE_1]
+synonym: "hyperinsulinism due to glucokinase deficiency" EXACT [DOID:0070216]
 xref: DOID:0070216 {source="MONDO:equivalentTo"}
 xref: GARD:0002818 {source="MONDO:GARD"}
 xref: ICD10CM:E16.1 {source="Orphanet:79299/attributed", source="Orphanet:79299/ntbt", source="Orphanet:79299"}
@@ -280547,11 +280552,13 @@ xref: Orphanet:79299 {source="OMIM:602485", source="MONDO:equivalentTo"}
 xref: SCTID:717182006 {source="MONDO:equivalentTo"}
 xref: UMLS:C1865290 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:355435"}
 is_a: MONDO:0005803 {source="DC-OMIM:602485"} ! hyperinsulinemic hypoglycemia
-is_a: MONDO:0015624 {source="Orphanet:79299"} ! diazoxide-sensitive diffuse hyperinsulinism
 is_a: MONDO:0017688 {source="Orphanet:79299", source="PMID:33340416"} ! disorder of glycolysis
+is_a: MONDO:0019010 {source="https://clinicalgenome.org/affiliation/40016/"} ! congenital isolated hyperinsulinism
+relationship: excluded_subClassOf MONDO:0015624 {source="Orphanet:79299", source="https://orcid.org/0000-0002-7638-4659"} ! diazoxide-sensitive diffuse hyperinsulinism
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK
 property_value: curated_content_resource "https://www.malacards.org/card/hyperinsulinemic_hypoglycemia_familial_3_2" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/9930/hyperinsulinemic-hypoglycemia-familial-3" xsd:anyURI {source="GARD:0009930"}
 
 [Term]

```

## Agent Attempts (10)

### Attempt 1: kimi-k2.6 / opencode

- **Eval PR**: [#270](https://github.com/ai4curation/eval-ont-agent-mondo/pull/270)
- **F1**: 0.421  **Precision**: 0.421  **Recall**: 0.421  **Jaccard**: 0.267
- **Trace**: [25755545606](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25755545606)
- **Workflow run**: [25755545606](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755545606)

#### Agent PR Comment

# Update MONDO:0011236 to GCK-related hyperinsulinism (ClinGen #9861)

## Summary

This pull request updates existing MONDO term **MONDO:0011236** (*hyperinsulinism due to glucokinase deficiency*) to reflect updated ClinGen Monogenic Diabetes Gene Curation Expert Panel nomenclature and mechanistic understanding. Rather than creating a new term, the existing term was renamed and enriched because it already captured the same OMIM concept (OMIM:602485).

---

## Changes made to MONDO:0011236

### 1. Primary name updated
- **Old:** `hyperinsulinism due to glucokinase deficiency`
- **New:** `GCK-related hyperinsulinism`

**Rationale:** The previous name incorrectly implied a *loss-of-function* / deficiency mechanism, whereas the condition is caused by activating / gain-of-function mutations in *GCK*. The ClinGen Expert Panel (Co-Chair Toni Pollin) explicitly requested adoption of the gene-related naming convention in this repo’s issue thread.

### 2. Definition updated
- **New definition:** "Any hyperinsulinism in which the cause of the disease is a gain-of-function variation in the GCK gene, which lowers the glucose threshold for insulin secretion. This condition is characterized by an autosomal dominant form of congenital hyperinsulinism with recurrent episodes of profound hypoglycemia."
- **Sources:** `https://clinicalgenome.org/affiliation/40016/`, `PMID:15277402`, `PMID:24890200`, `PMID:34680961`

**Rationale:** Replaced the old Orphanet-based definition with a description grounded in the ClinGen-requested literature and consistent with the MONDO `disease_series_by_gene` pattern ("Any [disease] in which the cause of the disease is a variation in the [gene] gene..."). The PMIDs were validated to confirm they specifically describe activating GCK mutations causing hyperinsulinemic hypoglycemia across neonatal, familial, and adult-onset presentations.

### 3. Synonyms updated / added
- Added **"GCK-related hyperinsulinism"** `EXACT` with `OMO:0002001` ClinGen preferred-label qualifier and ClinGen affiliation URL as source.
- Added **"hyperinsulinemic hypoglycemia, familial 3"** `EXACT` with `OMIM:602485` source (reflects the originally requested ClinGen preferred label).
- Promoted **"hyperinsulinemic hypoglycemia familial 3"** and **"hyperinsulinemic hypoglycemia, familial, 3"** from `RELATED` to `EXACT`.
- Retained **"hyperinsulinism due to glucokinase deficiency"** as `RELATED` synonym with `Orphanet:79299` provenance to preserve historical labels.

**Rationale:** The term must be findable under both the new gene-related name and the traditional OMIM-style familial name. Using the ClinGen `OMO:0002001` annotation clearly marks the community-preferred label.

### 4. Parent term added
- Added `is_a: MONDO:0017182 {source="OMIM:602485"} ! familial hyperinsulinism`

**Rationale:** The original ClinGen request explicitly listed MONDO:0017182 as the requested parent term. Existing parents (`hyperinsulinemic hypoglycemia`, `diazoxide-sensitive diffuse hyperinsulinism`, `disorder of glycolysis`) were **not removed**, in accordance with MONDO curation guidelines.

### 5. Logical definition (intersection_of) added
- `intersection_of: MONDO:0017182 ! familial hyperinsulinism`
- `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 ! GCK`

**Rationale:** This adds the standard `disease_series_by_gene` logical definition that was previously missing, enabling automated reasoning. The HGNC identifier **4195** for GCK was explicitly verified against the HGNC REST API.

### 6. Relationship source expanded
- `relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195` now includes PMIDs `15277402`, `24890200`, `34680961` alongside `OMIM:602485`.

### 7. Term tracker item added
- `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI`

---

## Validation / Research performed

| Step | Status |
|------|--------|
| Checked out existing term MONDO:0011236 from `mondo-edit.obo` | ✅ |
| Validated all three PMIDs (15277402, 24890200, 34680961) via PubMed — confirmed they describe GCK gain-of-function mutations causing hyperinsulinism | ✅ |
| Verified HGNC identifier for GCK (`http://identifiers.org/hgnc/4195`) against HGNC REST API | ✅ |
| Reviewed `disease_series_by_gene` pattern in `src/patterns/dosdp-patterns/disease_series_by_gene.yaml` | ✅ |
| Checked existing comparable term (MONDO:0009734 / ABCC8-related familial hyperinsulinism) for synonym and ClinGen-label patterns | ✅ |
| Checked in term, ran `make NORM`, and re-ingested normalized file | ✅ |
| Ran `robot convert` for syntax validation — **no errors** | ✅ |
| Confirmed `property_value` for original issue (#4985) retained while adding new term tracker for #9861 | ✅ |

---

## Files changed

- `src/ontology/mondo-edit.obo` (only)

---

Closes / addresses https://github.com/monarch-initiative/mondo/issues/9861

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755545606)


#### Agent Issue Comment

Thank you to the ClinGen Monogenic Diabetes Gene Curation Expert Panel for this request and for the clarification regarding the preferred primary name. The requested updates have been committed in PR. 

Changes made to **MONDO:0011236** (formerly *hyperinsulinism due to glucokinase deficiency*):
- **Primary name** updated to **"GCK-related hyperinsulinism"** as requested by the Expert Panel (tpollin) to align with updated recommended nomenclature.
- The OMIM-style name **"hyperinsulinemic hypoglycemia, familial 3"** has been retained as an **exact synonym**.
- **Definition** updated to reflect the gain-of-function mechanism in *GCK* and includes the ClinGen PMIDs provided (15277402, 24890200, 34680961).
- A new parent class **familial hyperinsulinism (MONDO:0017182)** was added per the original request.
- A **logical definition** (`intersection_of`) has been added to align with the `disease_series_by_gene` design pattern.
- ClinGen preferred-label synonym tag (`OMO:0002001`) added.

This addresses issue #9861.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755545606)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 70c79e85c..5127b2f49 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -280521,8 +280521,8 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011236
-name: hyperinsulinism due to glucokinase deficiency
-def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold for insulin release, characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of profound hypoglycemia induced by fasting and protein rich meals, requiring rapid and intensive treatment to prevent neurological sequelae." [Orphanet:79299]
+name: GCK-related hyperinsulinism
+def: "Any hyperinsulinism in which the cause of the disease is a gain-of-function variation in the GCK gene, which lowers the glucose threshold for insulin secretion. This condition is characterized by an autosomal dominant form of congenital hyperinsulinism with recurrent episodes of profound hypoglycemia." [https://clinicalgenome.org/affiliation/40016/, PMID:15277402, PMID:24890200, PMID:34680961]
 subset: doid {source="DOID:0070216"}
 subset: doid_rare {source="DOID:0070216"}
 subset: gard_rare {source="GARD:0002818", source="MONDO:GARD"}
@@ -280533,10 +280533,13 @@ subset: orphanet {source="Orphanet:79299"}
 subset: orphanet_rare {source="Orphanet:79299"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]
-synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]
-synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]
+synonym: "GCK-related hyperinsulinism" EXACT [https://clinicalgenome.org/affiliation/40016/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+synonym: "HHF3" EXACT ABBREVIATION [GARD:0009930, OMIM:602485]
+synonym: "hyperinsulinemic hypoglycemia familial 3" EXACT [GARD:0009930]
+synonym: "hyperinsulinemic hypoglycemia, familial 3" EXACT [MONDO:Lexical, OMIM:602485]
+synonym: "hyperinsulinemic hypoglycemia, familial, 3" EXACT [MONDO:Lexical, OMIM:602485]
 synonym: "hyperinsulinemic hypoglycemia, familial, type 3" EXACT [MONDO:RULE_1]
+synonym: "hyperinsulinism due to glucokinase deficiency" RELATED [Orphanet:79299]
 xref: DOID:0070216 {source="MONDO:equivalentTo"}
 xref: GARD:0002818 {source="MONDO:GARD"}
 xref: ICD10CM:E16.1 {source="Orphanet:79299/attributed", source="Orphanet:79299/ntbt", source="Orphanet:79299"}
@@ -280548,10 +280551,14 @@ xref: SCTID:717182006 {source="MONDO:equivalentTo"}
 xref: UMLS:C1865290 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:355435"}
 is_a: MONDO:0005803 {source="DC-OMIM:602485"} ! hyperinsulinemic hypoglycemia
 is_a: MONDO:0015624 {source="Orphanet:79299"} ! diazoxide-sensitive diffuse hyperinsulinism
+is_a: MONDO:0017182 {source="OMIM:602485"} ! familial hyperinsulinism
 is_a: MONDO:0017688 {source="Orphanet:79299", source="PMID:33340416"} ! disorder of glycolysis
-relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK
+intersection_of: MONDO:0017182 ! familial hyperinsulinism
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 ! GCK
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485", source="PMID:15277402", source="PMID:24890200", source="PMID:34680961"} ! GCK
 property_value: curated_content_resource "https://www.malacards.org/card/hyperinsulinemic_hypoglycemia_familial_3_2" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/9930/hyperinsulinemic-hypoglycemia-familial-3" xsd:anyURI {source="GARD:0009930"}
 
 [Term]

```

### Attempt 2: claude-sonnet-4.5 / copilot

- **Eval PR**: [#531](https://github.com/ai4curation/eval-ont-agent-mondo/pull/531)
- **F1**: 0.400  **Precision**: 0.316  **Recall**: 0.545  **Jaccard**: 0.250

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 70c79e85c..f00c73a6f 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -280521,8 +280521,8 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011236
-name: hyperinsulinism due to glucokinase deficiency
-def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold for insulin release, characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of profound hypoglycemia induced by fasting and protein rich meals, requiring rapid and intensive treatment to prevent neurological sequelae." [Orphanet:79299]
+name: GCK-related hyperinsulinism
+def: "Familial hyperinsulinemic hypoglycemia 3 (FHH3) is an autosomal dominant form of congenital hyperinsulinism due to gain-of-function mutations in glucokinase (GCK), which lower the glucose threshold for insulin secretion." [https://clinicalgenome.org/affiliation/40016/, PMID:15277402, PMID:24890200, PMID:34680961]
 subset: doid {source="DOID:0070216"}
 subset: doid_rare {source="DOID:0070216"}
 subset: gard_rare {source="GARD:0002818", source="MONDO:GARD"}
@@ -280534,9 +280534,10 @@ subset: orphanet_rare {source="Orphanet:79299"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]
-synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]
-synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]
+synonym: "hyperinsulinemic hypoglycemia familial 3" EXACT [GARD:0009930]
+synonym: "hyperinsulinemic hypoglycemia, familial, 3" EXACT [https://clinicalgenome.org/affiliation/40016/, MONDO:Lexical]
 synonym: "hyperinsulinemic hypoglycemia, familial, type 3" EXACT [MONDO:RULE_1]
+synonym: "hyperinsulinism due to glucokinase deficiency" EXACT [Orphanet:79299]
 xref: DOID:0070216 {source="MONDO:equivalentTo"}
 xref: GARD:0002818 {source="MONDO:GARD"}
 xref: ICD10CM:E16.1 {source="Orphanet:79299/attributed", source="Orphanet:79299/ntbt", source="Orphanet:79299"}
@@ -280548,10 +280549,12 @@ xref: SCTID:717182006 {source="MONDO:equivalentTo"}
 xref: UMLS:C1865290 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:355435"}
 is_a: MONDO:0005803 {source="DC-OMIM:602485"} ! hyperinsulinemic hypoglycemia
 is_a: MONDO:0015624 {source="Orphanet:79299"} ! diazoxide-sensitive diffuse hyperinsulinism
+is_a: MONDO:0017182 {source="https://clinicalgenome.org/affiliation/40016/"} ! familial hyperinsulinism
 is_a: MONDO:0017688 {source="Orphanet:79299", source="PMID:33340416"} ! disorder of glycolysis
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK
 property_value: curated_content_resource "https://www.malacards.org/card/hyperinsulinemic_hypoglycemia_familial_3_2" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/9930/hyperinsulinemic-hypoglycemia-familial-3" xsd:anyURI {source="GARD:0009930"}
 
 [Term]

```

### Attempt 3: claude-sonnet-4.5 / copilot

- **Eval PR**: [#496](https://github.com/ai4curation/eval-ont-agent-mondo/pull/496)
- **F1**: 0.400  **Precision**: 0.316  **Recall**: 0.545  **Jaccard**: 0.250

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 70c79e85c..f00c73a6f 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -280521,8 +280521,8 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011236
-name: hyperinsulinism due to glucokinase deficiency
-def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold for insulin release, characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of profound hypoglycemia induced by fasting and protein rich meals, requiring rapid and intensive treatment to prevent neurological sequelae." [Orphanet:79299]
+name: GCK-related hyperinsulinism
+def: "Familial hyperinsulinemic hypoglycemia 3 (FHH3) is an autosomal dominant form of congenital hyperinsulinism due to gain-of-function mutations in glucokinase (GCK), which lower the glucose threshold for insulin secretion." [https://clinicalgenome.org/affiliation/40016/, PMID:15277402, PMID:24890200, PMID:34680961]
 subset: doid {source="DOID:0070216"}
 subset: doid_rare {source="DOID:0070216"}
 subset: gard_rare {source="GARD:0002818", source="MONDO:GARD"}
@@ -280534,9 +280534,10 @@ subset: orphanet_rare {source="Orphanet:79299"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]
-synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]
-synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]
+synonym: "hyperinsulinemic hypoglycemia familial 3" EXACT [GARD:0009930]
+synonym: "hyperinsulinemic hypoglycemia, familial, 3" EXACT [https://clinicalgenome.org/affiliation/40016/, MONDO:Lexical]
 synonym: "hyperinsulinemic hypoglycemia, familial, type 3" EXACT [MONDO:RULE_1]
+synonym: "hyperinsulinism due to glucokinase deficiency" EXACT [Orphanet:79299]
 xref: DOID:0070216 {source="MONDO:equivalentTo"}
 xref: GARD:0002818 {source="MONDO:GARD"}
 xref: ICD10CM:E16.1 {source="Orphanet:79299/attributed", source="Orphanet:79299/ntbt", source="Orphanet:79299"}
@@ -280548,10 +280549,12 @@ xref: SCTID:717182006 {source="MONDO:equivalentTo"}
 xref: UMLS:C1865290 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:355435"}
 is_a: MONDO:0005803 {source="DC-OMIM:602485"} ! hyperinsulinemic hypoglycemia
 is_a: MONDO:0015624 {source="Orphanet:79299"} ! diazoxide-sensitive diffuse hyperinsulinism
+is_a: MONDO:0017182 {source="https://clinicalgenome.org/affiliation/40016/"} ! familial hyperinsulinism
 is_a: MONDO:0017688 {source="Orphanet:79299", source="PMID:33340416"} ! disorder of glycolysis
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK
 property_value: curated_content_resource "https://www.malacards.org/card/hyperinsulinemic_hypoglycemia_familial_3_2" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/9930/hyperinsulinemic-hypoglycemia-familial-3" xsd:anyURI {source="GARD:0009930"}
 
 [Term]

```

### Attempt 4: gpt-5.4 / codex

- **Eval PR**: [#170](https://github.com/ai4curation/eval-ont-agent-mondo/pull/170)
- **F1**: 0.400  **Precision**: 0.316  **Recall**: 0.545  **Jaccard**: 0.250
- **Workflow run**: [25640351465](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640351465)

#### Agent PR Comment

Updated `MONDO:0011236` from `hyperinsulinism due to glucokinase deficiency` to `GCK-related hyperinsulinism` based on the issue discussion confirming that this existing term matches the requested concept and that the ClinGen Monogenic Diabetes GCEP prefers the gene-related label.

Changes made:
- Renamed the primary label to `GCK-related hyperinsulinism`.
- Preserved `hyperinsulinism due to glucokinase deficiency` as an exact synonym.
- Tightened synonym scope for the familial hyperinsulinemic hypoglycemia 3 labels by making them exact.
- Added `is_a: MONDO:0017182 ! familial hyperinsulinism` without removing existing parents.
- Rewrote the definition to reflect activating `GCK` mutations lowering the glucose threshold for insulin secretion, with literature support from PMID:15277402, PMID:24890200, and PMID:34680961.
- Added an `IAO:0000233` tracker entry for issue `#9861`.

Background checks completed:
- Read the imported issue context and comment thread.
- Verified the current `MONDO:0011236` stanza in `src/ontology/mondo-edit.obo`.
- Verified the human `GCK` identifier as `HGNC:4195` via HGNC REST.
- Verified the cited PubMed records via NCBI E-utilities:
  - PMID:15277402 `Severe persistent hyperinsulinemic hypoglycemia due to a de novo glucokinase mutation.`
  - PMID:24890200 `Familial adult onset hyperinsulinism due to an activating glucokinase mutation: implications for pharmacological glucokinase activation.`
  - PMID:34680961 `Hyperinsulinemic Hypoglycemia in Three Generations of a Family with Glucokinase Activating Mutation, c.295T>C (p.Trp99Arg).`

Validation completed:
- Ran `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo`.
- Ran local normalization with `make -C src/ontology NORM` followed by replacing `src/ontology/mondo-edit.obo` with the normalized output.

Checklist:
- [x] Confirmed the issue refers to an existing term, not a new term.
- [x] Updated the primary label to match the requested nomenclature.
- [x] Kept prior terminology as synonym coverage.
- [x] Added the requested familial parent.
- [x] Checked literature and identifier provenance.
- [x] Ran syntax validation and normalization locally.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640351465)


#### Agent Issue Comment

Updated `MONDO:0011236` to use the ClinGen-preferred primary label `GCK-related hyperinsulinism`, retained the previous label as an exact synonym, added the requested parent `MONDO:0017182` familial hyperinsulinism, and refreshed the definition to reflect activating `GCK` mutations. Changes are committed locally and can be used for PR #<NN>.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640351465)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 70c79e85c..aab83f4e9 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -280521,8 +280521,8 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011236
-name: hyperinsulinism due to glucokinase deficiency
-def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold for insulin release, characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of profound hypoglycemia induced by fasting and protein rich meals, requiring rapid and intensive treatment to prevent neurological sequelae." [Orphanet:79299]
+name: GCK-related hyperinsulinism
+def: "A familial hyperinsulinemic hypoglycemia caused by activating mutations in the GCK gene, which lower the glucose threshold for insulin secretion." [PMID:15277402, PMID:24890200, PMID:34680961]
 subset: doid {source="DOID:0070216"}
 subset: doid_rare {source="DOID:0070216"}
 subset: gard_rare {source="GARD:0002818", source="MONDO:GARD"}
@@ -280534,9 +280534,10 @@ subset: orphanet_rare {source="Orphanet:79299"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]
-synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]
-synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]
+synonym: "hyperinsulinemic hypoglycemia familial 3" EXACT [GARD:0009930]
+synonym: "hyperinsulinemic hypoglycemia, familial, 3" EXACT [MONDO:Lexical, OMIM:602485]
 synonym: "hyperinsulinemic hypoglycemia, familial, type 3" EXACT [MONDO:RULE_1]
+synonym: "hyperinsulinism due to glucokinase deficiency" EXACT [Orphanet:79299]
 xref: DOID:0070216 {source="MONDO:equivalentTo"}
 xref: GARD:0002818 {source="MONDO:GARD"}
 xref: ICD10CM:E16.1 {source="Orphanet:79299/attributed", source="Orphanet:79299/ntbt", source="Orphanet:79299"}
@@ -280548,10 +280549,12 @@ xref: SCTID:717182006 {source="MONDO:equivalentTo"}
 xref: UMLS:C1865290 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:355435"}
 is_a: MONDO:0005803 {source="DC-OMIM:602485"} ! hyperinsulinemic hypoglycemia
 is_a: MONDO:0015624 {source="Orphanet:79299"} ! diazoxide-sensitive diffuse hyperinsulinism
+is_a: MONDO:0017182 {source="OMIM:602485", source="https://clinicalgenome.org/affiliation/40016/"} ! familial hyperinsulinism
 is_a: MONDO:0017688 {source="Orphanet:79299", source="PMID:33340416"} ! disorder of glycolysis
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK
 property_value: curated_content_resource "https://www.malacards.org/card/hyperinsulinemic_hypoglycemia_familial_3_2" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/9930/hyperinsulinemic-hypoglycemia-familial-3" xsd:anyURI {source="GARD:0009930"}
 
 [Term]

```

### Attempt 5: gpt-5.5 / opencode

- **Eval PR**: [#76](https://github.com/ai4curation/eval-ont-agent-mondo/pull/76)
- **F1**: 0.378  **Precision**: 0.368  **Recall**: 0.389  **Jaccard**: 0.233
- **Trace**: [25615975804](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615975804)
- **Workflow run**: [25615975804](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615975804)

#### Agent PR Comment

## Summary

Addresses monarch-initiative/mondo#9861 by updating the existing equivalent term MONDO:0011236 rather than creating a new term.

Changes made to `src/ontology/mondo-edit.obo`:
- Renamed MONDO:0011236 from “hyperinsulinism due to glucokinase deficiency” to the ClinGen-preferred label “GCK-related hyperinsulinism”.
- Replaced the definition to describe familial hyperinsulinism due to germline gain-of-function variants in `GCK`, with citations to the ClinGen Monogenic Diabetes GCEP URL and PMIDs 15277402, 24890200, and 34680961.
- Added the ClinGen-preferred label as an exact synonym with the preferred-label-by-community annotation.
- Updated “HHF3” and familial hyperinsulinemic hypoglycemia synonyms to exact where appropriate; retained the former label as a related synonym sourced to Orphanet.
- Added the requested parent `MONDO:0017182` familial hyperinsulinism.
- Added a logical definition using `MONDO:0017182` plus the existing verified GCK HGNC identifier (`http://identifiers.org/hgnc/4195`).
- Expanded the GCK material-basis relationship sources and added issue tracker provenance for #9861.

## Checks / rationale

Checklist completed:
- Confirmed the issue discussion clarified that this is the same concept as existing MONDO:0011236 and that the requested primary label is “GCK-related hyperinsulinism”.
- Checked MONDO:0011236 and requested parent MONDO:0017182 in `src/ontology/mondo-edit.obo`.
- Verified the human gene identifier for `GCK` via HGNC (`HGNC:4195`, glucokinase).
- Reviewed PubMed records/abstracts for PMID:15277402, PMID:24890200, and PMID:34680961. These support activating/gain-of-function GCK variants causing hyperinsulinemic hypoglycemia/familial hyperinsulinism. (`aurelian fulltext` was attempted but is not installed in this environment.)
- Normalized serialization with `make NORM` and moved `NORM` back to `src/ontology/mondo-edit.obo`.
- Validated OBO syntax with:
  `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo`

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615975804)


#### Agent Issue Comment

Changes committed in PR #<NN>.

MONDO:0011236 has been updated to use the ClinGen-preferred primary label “GCK-related hyperinsulinism” for this existing equivalent concept, with updated definition, synonyms, familial hyperinsulinism parentage, GCK logical axiom, and issue provenance.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615975804)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 70c79e85c..3fe151a40 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -280521,8 +280521,8 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011236
-name: hyperinsulinism due to glucokinase deficiency
-def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold for insulin release, characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of profound hypoglycemia induced by fasting and protein rich meals, requiring rapid and intensive treatment to prevent neurological sequelae." [Orphanet:79299]
+name: GCK-related hyperinsulinism
+def: "GCK-related hyperinsulinism is a form of familial hyperinsulinism caused by germline gain-of-function mutations in GCK, which lower the glucose threshold for insulin secretion and result in hyperinsulinemic hypoglycemia." [https://clinicalgenome.org/affiliation/40016/, PMID:15277402, PMID:24890200, PMID:34680961]
 subset: doid {source="DOID:0070216"}
 subset: doid_rare {source="DOID:0070216"}
 subset: gard_rare {source="GARD:0002818", source="MONDO:GARD"}
@@ -280533,10 +280533,12 @@ subset: orphanet {source="Orphanet:79299"}
 subset: orphanet_rare {source="Orphanet:79299"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]
-synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]
-synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]
+synonym: "GCK-related hyperinsulinism" EXACT [https://clinicalgenome.org/affiliation/40016/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+synonym: "HHF3" EXACT ABBREVIATION [GARD:0009930, MONDO:Lexical, OMIM:602485]
+synonym: "hyperinsulinemic hypoglycemia familial 3" EXACT [GARD:0009930, OMIM:602485]
+synonym: "hyperinsulinemic hypoglycemia, familial, 3" EXACT [OMIM:602485]
 synonym: "hyperinsulinemic hypoglycemia, familial, type 3" EXACT [MONDO:RULE_1]
+synonym: "hyperinsulinism due to glucokinase deficiency" RELATED [Orphanet:79299]
 xref: DOID:0070216 {source="MONDO:equivalentTo"}
 xref: GARD:0002818 {source="MONDO:GARD"}
 xref: ICD10CM:E16.1 {source="Orphanet:79299/attributed", source="Orphanet:79299/ntbt", source="Orphanet:79299"}
@@ -280548,10 +280550,14 @@ xref: SCTID:717182006 {source="MONDO:equivalentTo"}
 xref: UMLS:C1865290 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:355435"}
 is_a: MONDO:0005803 {source="DC-OMIM:602485"} ! hyperinsulinemic hypoglycemia
 is_a: MONDO:0015624 {source="Orphanet:79299"} ! diazoxide-sensitive diffuse hyperinsulinism
+is_a: MONDO:0017182 {source="PMID:15277402", source="PMID:24890200", source="PMID:34680961", source="https://clinicalgenome.org/affiliation/40016/"} ! familial hyperinsulinism
 is_a: MONDO:0017688 {source="Orphanet:79299", source="PMID:33340416"} ! disorder of glycolysis
-relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK
+intersection_of: MONDO:0017182 ! familial hyperinsulinism
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 ! GCK
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485", source="PMID:15277402", source="PMID:24890200", source="PMID:34680961"} ! GCK
 property_value: curated_content_resource "https://www.malacards.org/card/hyperinsulinemic_hypoglycemia_familial_3_2" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/9930/hyperinsulinemic-hypoglycemia-familial-3" xsd:anyURI {source="GARD:0009930"}
 
 [Term]

```

### Attempt 6: gpt-5.5 / opencode

- **Eval PR**: [#55](https://github.com/ai4curation/eval-ont-agent-mondo/pull/55)
- **F1**: 0.378  **Precision**: 0.368  **Recall**: 0.389  **Jaccard**: 0.233
- **Trace**: [25615933390](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615933390)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 70c79e85c..3fe151a40 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -280521,8 +280521,8 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011236
-name: hyperinsulinism due to glucokinase deficiency
-def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold for insulin release, characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of profound hypoglycemia induced by fasting and protein rich meals, requiring rapid and intensive treatment to prevent neurological sequelae." [Orphanet:79299]
+name: GCK-related hyperinsulinism
+def: "GCK-related hyperinsulinism is a form of familial hyperinsulinism caused by germline gain-of-function mutations in GCK, which lower the glucose threshold for insulin secretion and result in hyperinsulinemic hypoglycemia." [https://clinicalgenome.org/affiliation/40016/, PMID:15277402, PMID:24890200, PMID:34680961]
 subset: doid {source="DOID:0070216"}
 subset: doid_rare {source="DOID:0070216"}
 subset: gard_rare {source="GARD:0002818", source="MONDO:GARD"}
@@ -280533,10 +280533,12 @@ subset: orphanet {source="Orphanet:79299"}
 subset: orphanet_rare {source="Orphanet:79299"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]
-synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]
-synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]
+synonym: "GCK-related hyperinsulinism" EXACT [https://clinicalgenome.org/affiliation/40016/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
+synonym: "HHF3" EXACT ABBREVIATION [GARD:0009930, MONDO:Lexical, OMIM:602485]
+synonym: "hyperinsulinemic hypoglycemia familial 3" EXACT [GARD:0009930, OMIM:602485]
+synonym: "hyperinsulinemic hypoglycemia, familial, 3" EXACT [OMIM:602485]
 synonym: "hyperinsulinemic hypoglycemia, familial, type 3" EXACT [MONDO:RULE_1]
+synonym: "hyperinsulinism due to glucokinase deficiency" RELATED [Orphanet:79299]
 xref: DOID:0070216 {source="MONDO:equivalentTo"}
 xref: GARD:0002818 {source="MONDO:GARD"}
 xref: ICD10CM:E16.1 {source="Orphanet:79299/attributed", source="Orphanet:79299/ntbt", source="Orphanet:79299"}
@@ -280548,10 +280550,14 @@ xref: SCTID:717182006 {source="MONDO:equivalentTo"}
 xref: UMLS:C1865290 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:355435"}
 is_a: MONDO:0005803 {source="DC-OMIM:602485"} ! hyperinsulinemic hypoglycemia
 is_a: MONDO:0015624 {source="Orphanet:79299"} ! diazoxide-sensitive diffuse hyperinsulinism
+is_a: MONDO:0017182 {source="PMID:15277402", source="PMID:24890200", source="PMID:34680961", source="https://clinicalgenome.org/affiliation/40016/"} ! familial hyperinsulinism
 is_a: MONDO:0017688 {source="Orphanet:79299", source="PMID:33340416"} ! disorder of glycolysis
-relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK
+intersection_of: MONDO:0017182 ! familial hyperinsulinism
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 ! GCK
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485", source="PMID:15277402", source="PMID:24890200", source="PMID:34680961"} ! GCK
 property_value: curated_content_resource "https://www.malacards.org/card/hyperinsulinemic_hypoglycemia_familial_3_2" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/9930/hyperinsulinemic-hypoglycemia-familial-3" xsd:anyURI {source="GARD:0009930"}
 
 [Term]

```

### Attempt 7: gpt-5.5 / codex

- **Eval PR**: [#38](https://github.com/ai4curation/eval-ont-agent-mondo/pull/38)
- **F1**: 0.312  **Precision**: 0.263  **Recall**: 0.385  **Jaccard**: 0.185
- **Trace**: [25615869446](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615869446)
- **Workflow run**: [25615869446](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615869446)

#### Agent PR Comment

## Summary

Addresses issue #9861 by updating existing term MONDO:0011236 rather than creating a new term, consistent with the issue discussion confirming this is the same concept as OMIM:602485.

Changes made:

- Changed the primary label from "hyperinsulinism due to glucokinase deficiency" to "GCK-related hyperinsulinism".
- Rewrote the definition to reflect heterozygous activating GCK mutations and lowered glucose threshold for insulin secretion.
- Added ClinGen attribution for the requested preferred label.
- Updated "hyperinsulinemic hypoglycemia, familial, 3" from RELATED to EXACT with OMIM and ClinGen attribution.
- Preserved "hyperinsulinism due to glucokinase deficiency" as an EXACT synonym sourced to Orphanet.
- Added disease-series logical definition axioms using hyperinsulinemic hypoglycemia and GCK.
- Added PMID and ClinGen source attribution to the GCK material-basis relationship.
- Added the issue tracker link for #9861.

## Rationale

The issue thread clarified that the request does not require a new MONDO term. MONDO:0011236 already represents the same concept and already has the GCK material basis and OMIM:602485 xref. The requested parent, MONDO:0017182 familial hyperinsulinism, is already present through the existing ancestry:

MONDO:0011236 -> MONDO:0015624 diazoxide-sensitive diffuse hyperinsulinism -> MONDO:0019010 congenital isolated hyperinsulinism -> MONDO:0017182 familial hyperinsulinism.

The updated label follows the requested ClinGen-preferred gene-related naming while preserving source labels and existing mappings.

## Checks Completed

- Reviewed issue title, body, and comments from `__issue_context__.json`.
- Checked MONDO:0011236 and parent context with `obo-grep.pl`.
- Checked related hyperinsulinism terms for local naming/logical-definition patterns.
- Verified GCK identifier `HGNC:4195` via the HGNC REST API.
- Checked publication metadata/abstracts for PMID:15277402, PMID:24890200, and PMID:34680961 via NCBI E-utilities.
- Ran local syntax validation:
  - `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o src/ontology/mondo-edit.TMP.obo`
- Normalized serialization locally:
  - `make NORM`
  - `mv NORM mondo-edit.obo`
- Re-ran `robot convert` successfully after normalization.

## Notes

The required `aurelian fulltext` command was attempted for all three PMIDs, but `aurelian` is not installed in this environment. The Docker-backed `src/ontology/run.sh` wrapper also could not run because `docker` is not installed, so validation and normalization were performed with the local `robot`, `owltools`, and `make` commands available in the checkout.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615869446)


#### Agent Issue Comment

Changes committed in PR #<NN>.

Updated existing term MONDO:0011236 to use the ClinGen-requested primary label "GCK-related hyperinsulinism" and retained the previous labels as synonyms.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615869446)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 70c79e85c..bbf125f2f 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -280521,8 +280521,8 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011236
-name: hyperinsulinism due to glucokinase deficiency
-def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold for insulin release, characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of profound hypoglycemia induced by fasting and protein rich meals, requiring rapid and intensive treatment to prevent neurological sequelae." [Orphanet:79299]
+name: GCK-related hyperinsulinism
+def: "GCK-related hyperinsulinism is a familial hyperinsulinism caused by heterozygous activating mutations in the GCK gene. It is characterized by a lowered glucose threshold for insulin secretion, leading to hyperinsulinemic hypoglycemia." [https://clinicalgenome.org/affiliation/40016/, PMID:15277402, PMID:24890200, PMID:34680961]
 subset: doid {source="DOID:0070216"}
 subset: doid_rare {source="DOID:0070216"}
 subset: gard_rare {source="GARD:0002818", source="MONDO:GARD"}
@@ -280533,10 +280533,12 @@ subset: orphanet {source="Orphanet:79299"}
 subset: orphanet_rare {source="Orphanet:79299"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
+synonym: "GCK-related hyperinsulinism" EXACT [https://clinicalgenome.org/affiliation/40016/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
 synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]
 synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]
-synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]
+synonym: "hyperinsulinemic hypoglycemia, familial, 3" EXACT [https://clinicalgenome.org/affiliation/40016/, OMIM:602485]
 synonym: "hyperinsulinemic hypoglycemia, familial, type 3" EXACT [MONDO:RULE_1]
+synonym: "hyperinsulinism due to glucokinase deficiency" EXACT [Orphanet:79299]
 xref: DOID:0070216 {source="MONDO:equivalentTo"}
 xref: GARD:0002818 {source="MONDO:GARD"}
 xref: ICD10CM:E16.1 {source="Orphanet:79299/attributed", source="Orphanet:79299/ntbt", source="Orphanet:79299"}
@@ -280549,9 +280551,12 @@ xref: UMLS:C1865290 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source=
 is_a: MONDO:0005803 {source="DC-OMIM:602485"} ! hyperinsulinemic hypoglycemia
 is_a: MONDO:0015624 {source="Orphanet:79299"} ! diazoxide-sensitive diffuse hyperinsulinism
 is_a: MONDO:0017688 {source="Orphanet:79299", source="PMID:33340416"} ! disorder of glycolysis
-relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK
+intersection_of: MONDO:0005803 ! hyperinsulinemic hypoglycemia
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 ! GCK
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485", source="PMID:15277402", source="PMID:24890200", source="PMID:34680961", source="https://clinicalgenome.org/affiliation/40016/"} ! GCK
 property_value: curated_content_resource "https://www.malacards.org/card/hyperinsulinemic_hypoglycemia_familial_3_2" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/9930/hyperinsulinemic-hypoglycemia-familial-3" xsd:anyURI {source="GARD:0009930"}
 
 [Term]

```

### Attempt 8: claude-sonnet-4.5 / claude

- **Eval PR**: [#447](https://github.com/ai4curation/eval-ont-agent-mondo/pull/447)
- **F1**: 0.250  **Precision**: 0.211  **Recall**: 0.308  **Jaccard**: 0.143
- **Trace**: [25867729873](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25867729873)
- **Workflow run**: [25867729873](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867729873)

#### Agent PR Comment

# Update MONDO:0011236 to ClinGen-Preferred Nomenclature

## Summary
Updated MONDO:0011236 to use "GCK-related hyperinsulinism" as the primary term name per ClinGen Monogenic Diabetes Gene Curation Expert Panel (GCEP) request in issue #9861.

## Changes Made

### 1. Primary Label Update
- **Old:** hyperinsulinism due to glucokinase deficiency
- **New:** GCK-related hyperinsulinism
- **Rationale:** Aligns with ClinGen's preferred gene-related disease nomenclature

### 2. Definition Enhancement
Updated the definition to:
- Explicitly state this is caused by **gain-of-function mutations** in GCK (not loss-of-function/deficiency)
- Follow the gene-disease pattern: "Any familial hyperinsulinism in which the cause of the disease is a gain-of-function mutation in the GCK gene"
- Maintain clinical description of the phenotype
- Add proper citations from ClinGen and literature (PMID:15277402, PMID:24890200, PMID:34680961)

### 3. Synonym Updates
- Promoted "hyperinsulinemic hypoglycemia, familial, 3" to EXACT synonym with ClinGen attribution
- Demoted old primary label "hyperinsulinism due to glucokinase deficiency" to EXACT synonym with Orphanet attribution
- Retained all existing synonyms (HHF3, etc.)

### 4. Relationship Additions
- Added parent relationship: `is_a: MONDO:0017182` (familial hyperinsulinism) as requested
- Updated sources on `has_material_basis_in_germline_mutation_in` relationship to include all PMIDs and ClinGen

### 5. Metadata Updates
- Added `property_value: http://purl.org/dc/terms/creator https://clinicalgenome.org/affiliation/40016/`
- Updated issue tracker from #4985 to #9861

## Validation Performed

### Literature Review
Reviewed all three PMIDs provided:
- **PMID:15277402** - Describes severe persistent hyperinsulinemic hypoglycemia due to de novo GCK mutation (Y214C) with gain-of-function characteristics
- **PMID:34680961** - Reports multi-generational family with GCK:c.295T>C (p.Trp99Arg) pathogenic variant causing familial hyperinsulinemic hypoglycemia
- **PMID:24890200** - Documents familial adult-onset hyperinsulinism due to activating GCK mutation (p.Val389Leu)

All sources confirm this condition is caused by **activating/gain-of-function** mutations in GCK.

### Term Structure
- Verified HGNC identifier for GCK (http://identifiers.org/hgnc/4195) is correct
- Confirmed parent term MONDO:0017182 (familial hyperinsulinism) is appropriate
- Maintained existing parent relationships to preserve classification
- Applied proper source attribution throughout

### Ontology Normalization
- Checked out term to `terms/MONDO_0011236.obo`
- Made edits following MONDO curation guidelines
- Checked term back in to `mondo-edit.obo`
- Ran ODK normalization: `make NORM && mv NORM mondo-edit.obo`

## Checklist
- [x] Updated term name to ClinGen-preferred nomenclature
- [x] Enhanced definition with gain-of-function mutation specification
- [x] Added proper synonym attributions including ClinGen source
- [x] Added requested parent relationship to familial hyperinsulinism
- [x] Verified all PMIDs and their relevance to the condition
- [x] Added ClinGen creator attribution
- [x] Updated issue tracker reference
- [x] Normalized ontology serialization
- [x] Committed only modified ontology file

## Notes
This update addresses the ClinGen GCEP's request for updated nomenclature that better reflects current gene-disease naming conventions. The change from "due to glucokinase deficiency" to "GCK-related" is more accurate, as the mutations are gain-of-function (hyperactive enzyme) rather than loss-of-function (deficiency).

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867729873)


#### Agent Issue Comment

The existing MONDO term MONDO:0011236 has been updated as requested. The primary label is now "GCK-related hyperinsulinism" per your preferred nomenclature, with "hyperinsulinemic hypoglycemia, familial, 3" added as an EXACT synonym with proper ClinGen attribution.

Changes committed in PR #<NN>

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867729873)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 70c79e85c..e79778b5c 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -280521,8 +280521,8 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011236
-name: hyperinsulinism due to glucokinase deficiency
-def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold for insulin release, characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of profound hypoglycemia induced by fasting and protein rich meals, requiring rapid and intensive treatment to prevent neurological sequelae." [Orphanet:79299]
+name: GCK-related hyperinsulinism
+def: "Any familial hyperinsulinism in which the cause of the disease is a gain-of-function mutation in the GCK gene. This autosomal dominant form of congenital hyperinsulinism is caused by mutations in glucokinase (GCK) that lower the glucose threshold for insulin secretion, characterized by excessive/uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of hypoglycemia induced by fasting and protein-rich meals." [https://clinicalgenome.org/affiliation/40016/, PMID:15277402, PMID:24890200, PMID:34680961]
 subset: doid {source="DOID:0070216"}
 subset: doid_rare {source="DOID:0070216"}
 subset: gard_rare {source="GARD:0002818", source="MONDO:GARD"}
@@ -280535,8 +280535,9 @@ subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]
 synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]
-synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]
+synonym: "hyperinsulinemic hypoglycemia, familial, 3" EXACT [https://clinicalgenome.org/affiliation/40016/]
 synonym: "hyperinsulinemic hypoglycemia, familial, type 3" EXACT [MONDO:RULE_1]
+synonym: "hyperinsulinism due to glucokinase deficiency" EXACT [Orphanet:79299]
 xref: DOID:0070216 {source="MONDO:equivalentTo"}
 xref: GARD:0002818 {source="MONDO:GARD"}
 xref: ICD10CM:E16.1 {source="Orphanet:79299/attributed", source="Orphanet:79299/ntbt", source="Orphanet:79299"}
@@ -280548,10 +280549,12 @@ xref: SCTID:717182006 {source="MONDO:equivalentTo"}
 xref: UMLS:C1865290 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:355435"}
 is_a: MONDO:0005803 {source="DC-OMIM:602485"} ! hyperinsulinemic hypoglycemia
 is_a: MONDO:0015624 {source="Orphanet:79299"} ! diazoxide-sensitive diffuse hyperinsulinism
+is_a: MONDO:0017182 {source="PMID:15277402", source="PMID:24890200", source="PMID:34680961", source="https://clinicalgenome.org/affiliation/40016/"} ! familial hyperinsulinism
 is_a: MONDO:0017688 {source="Orphanet:79299", source="PMID:33340416"} ! disorder of glycolysis
-relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485", source="PMID:15277402", source="PMID:24890200", source="PMID:34680961", source="https://clinicalgenome.org/affiliation/40016/"} ! GCK
 property_value: curated_content_resource "https://www.malacards.org/card/hyperinsulinemic_hypoglycemia_familial_3_2" xsd:anyURI {source="MONDO:MalaCards"}
-property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI
+property_value: http://purl.org/dc/terms/creator https://clinicalgenome.org/affiliation/40016/
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/9930/hyperinsulinemic-hypoglycemia-familial-3" xsd:anyURI {source="GARD:0009930"}
 
 [Term]

```

### Attempt 9: claude-opus-4.7 / claude

- **Eval PR**: [#381](https://github.com/ai4curation/eval-ont-agent-mondo/pull/381)
- **F1**: 0.240  **Precision**: 0.158  **Recall**: 0.500  **Jaccard**: 0.136
- **Trace**: [25817198970](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25817198970)
- **Workflow run**: [25817198970](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817198970)

#### Agent PR Comment

# Summary

Addresses issue #9861.

The original NTR requested a new term for "Hyperinsulinemic hypoglycemia, familial 3" with synonym "GCK-related hyperinsulinism". As noted in the issue discussion, an existing term **MONDO:0011236** (previously named "hyperinsulinism due to glucokinase deficiency") already covers this concept and gene association (GCK, HGNC:4195, OMIM:602485, Orphanet:79299).

@tpollin (Co-Chair, ClinGen Monogenic Diabetes Gene Curation Expert Panel) subsequently confirmed that the existing term is the same concept but asked that the **primary label be "GCK-related hyperinsulinism"** per updated ClinGen recommended nomenclature. This PR makes that change.

# Changes to MONDO:0011236

| Field | Before | After |
|---|---|---|
| `name` | hyperinsulinism due to glucokinase deficiency | **GCK-related hyperinsulinism** |
| synonym: "hyperinsulinism due to glucokinase deficiency" | (was primary) | EXACT [Orphanet:79299] |
| synonym: "hyperinsulinemic hypoglycemia, familial, 3" | RELATED [MONDO:Lexical] | EXACT [OMIM:602485] |
| `term_tracker_item` | issue #4985 only | issues #4985 and #9861 |

The other synonyms (HHF3 abbreviation, "hyperinsulinemic hypoglycemia familial 3", "hyperinsulinemic hypoglycemia, familial, type 3"), all cross-references (DOID, GARD, ICD10CM, MEDGEN, MESH, OMIM, Orphanet, SCTID, UMLS), parent classes, the `has_material_basis_in_germline_mutation_in GCK` axiom, and the definition were left unchanged — the concept is unchanged, only the preferred label.

# Rationale

- The new primary label "GCK-related hyperinsulinism" follows the MONDO `{GENE}-related {disease description}` naming convention for monogenic diseases (per project CLAUDE.md).
- The change was explicitly requested by the ClinGen Monogenic Diabetes GCEP Co-Chair in the issue thread, in line with their updated recommended nomenclature.
- The prior label is preserved as an EXACT synonym to maintain lookup continuity for users searching by the old name and to retain the Orphanet attribution.
- The OMIM-style "hyperinsulinemic hypoglycemia, familial, 3" was upgraded from RELATED to EXACT with OMIM:602485 as its source, reflecting that this is the OMIM-preferred label for the same concept (consistent with how the existing "type 3" variant is already EXACT).

# Checklist

- [x] Identified the existing term covering the requested concept (MONDO:0011236)
- [x] Honored the ClinGen GCEP Co-Chair's explicit preference for the primary label
- [x] Preserved the prior label as an EXACT synonym with its original Orphanet source
- [x] Added a `term_tracker_item` for issue #9861 (kept the original #4985 reference)
- [x] No logical axioms, parents, or xrefs changed (concept unchanged)
- [x] Edited only `src/ontology/mondo-edit.obo` via the `terms/` workflow (`obo-checkout.pl` / `obo-checkin.pl`)

# Validation notes

- ODK / `robot convert` syntax validation could not be run in this environment (docker not available); however, the edit is minimal, syntactically simple, and round-trips cleanly through `obo-checkout.pl` / `obo-checkin.pl`.
- `aurelian fulltext` was unavailable in this environment, so no new PMID citations beyond those already present in the term were added. The PMIDs supplied in the issue body (15277402, 34680961, 24890200) were not added to the definition xref because the existing Orphanet:79299 definition is unchanged.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817198970)


#### Agent Issue Comment

Thanks @elmacke and @tpollin for the request and clarification.

Per @tpollin's request (Co-Chair, ClinGen Monogenic Diabetes Gene Curation Expert Panel), the existing term MONDO:0011236 has been renamed from "hyperinsulinism due to glucokinase deficiency" to **"GCK-related hyperinsulinism"** as the primary label, in keeping with the updated ClinGen recommended nomenclature. The prior label and the OMIM-style label ("hyperinsulinemic hypoglycemia, familial, 3") are retained as EXACT synonyms.

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817198970)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 70c79e85c..6b2861caa 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -280521,7 +280521,7 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011236
-name: hyperinsulinism due to glucokinase deficiency
+name: GCK-related hyperinsulinism
 def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold for insulin release, characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of profound hypoglycemia induced by fasting and protein rich meals, requiring rapid and intensive treatment to prevent neurological sequelae." [Orphanet:79299]
 subset: doid {source="DOID:0070216"}
 subset: doid_rare {source="DOID:0070216"}
@@ -280535,8 +280535,9 @@ subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]
 synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]
-synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]
+synonym: "hyperinsulinemic hypoglycemia, familial, 3" EXACT [OMIM:602485]
 synonym: "hyperinsulinemic hypoglycemia, familial, type 3" EXACT [MONDO:RULE_1]
+synonym: "hyperinsulinism due to glucokinase deficiency" EXACT [Orphanet:79299]
 xref: DOID:0070216 {source="MONDO:equivalentTo"}
 xref: GARD:0002818 {source="MONDO:GARD"}
 xref: ICD10CM:E16.1 {source="Orphanet:79299/attributed", source="Orphanet:79299/ntbt", source="Orphanet:79299"}
@@ -280552,6 +280553,7 @@ is_a: MONDO:0017688 {source="Orphanet:79299", source="PMID:33340416"} ! disorder
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK
 property_value: curated_content_resource "https://www.malacards.org/card/hyperinsulinemic_hypoglycemia_familial_3_2" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/9930/hyperinsulinemic-hypoglycemia-familial-3" xsd:anyURI {source="GARD:0009930"}
 
 [Term]

```

### Attempt 10: claude-haiku-4.5 / claude

- **Eval PR**: [#194](https://github.com/ai4curation/eval-ont-agent-mondo/pull/194)
- **F1**: 0.188  **Precision**: 0.158  **Recall**: 0.231  **Jaccard**: 0.103
- **Workflow run**: [25640402559](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640402559)

#### Agent PR Comment

# PR: Update MONDO:0011236 for ClinGen Gene-Based Nomenclature

#### Agent Issue Comment

# Issue #9861 Resolution

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 70c79e85c..3009f15cd 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -280521,8 +280521,8 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011236
-name: hyperinsulinism due to glucokinase deficiency
-def: "Hyperinsulism due to glucokinase deficiency (HIGCK) is a form of diazoxide-sensitive diffuse hyperinsulinism, caused by a lowered threshold for insulin release, characterized by an excessive/ uncontrolled insulin secretion (inappropriate for the level of glycemia) and recurrent episodes of profound hypoglycemia induced by fasting and protein rich meals, requiring rapid and intensive treatment to prevent neurological sequelae." [Orphanet:79299]
+name: GCK-related hyperinsulinism
+def: "Any familial hyperinsulinism in which the cause of the disease is a gain-of-function mutation in the GCK gene. This condition is characterized by a lowered glucose threshold for insulin secretion, leading to inappropriate hyperinsulinemia and recurrent episodes of profound hypoglycemia induced by fasting and protein-rich meals." [PMID:15277402, PMID:34680961, PMID:24890200]
 subset: doid {source="DOID:0070216"}
 subset: doid_rare {source="DOID:0070216"}
 subset: gard_rare {source="GARD:0002818", source="MONDO:GARD"}
@@ -280537,6 +280537,7 @@ synonym: "HHF3" RELATED ABBREVIATION [GARD:0009930, MONDO:Lexical]
 synonym: "hyperinsulinemic hypoglycemia familial 3" RELATED [GARD:0009930]
 synonym: "hyperinsulinemic hypoglycemia, familial, 3" RELATED [MONDO:Lexical]
 synonym: "hyperinsulinemic hypoglycemia, familial, type 3" EXACT [MONDO:RULE_1]
+synonym: "hyperinsulinism due to glucokinase deficiency" RELATED [Orphanet:79299]
 xref: DOID:0070216 {source="MONDO:equivalentTo"}
 xref: GARD:0002818 {source="MONDO:GARD"}
 xref: ICD10CM:E16.1 {source="Orphanet:79299/attributed", source="Orphanet:79299/ntbt", source="Orphanet:79299"}
@@ -280546,12 +280547,16 @@ xref: OMIM:602485 {source="Orphanet:79299/e", source="MONDO:equivalentTo", sourc
 xref: Orphanet:79299 {source="OMIM:602485", source="MONDO:equivalentTo"}
 xref: SCTID:717182006 {source="MONDO:equivalentTo"}
 xref: UMLS:C1865290 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:355435"}
+is_a: MONDO:0017182 {source="PMID:15277402", source="PMID:34680961", source="PMID:24890200"} ! familial hyperinsulinism
 is_a: MONDO:0005803 {source="DC-OMIM:602485"} ! hyperinsulinemic hypoglycemia
 is_a: MONDO:0015624 {source="Orphanet:79299"} ! diazoxide-sensitive diffuse hyperinsulinism
 is_a: MONDO:0017688 {source="Orphanet:79299", source="PMID:33340416"} ! disorder of glycolysis
-relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="OMIM:602485"} ! GCK
+intersection_of: MONDO:0017182 ! familial hyperinsulinism
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/4195 {source="PMID:15277402", source="PMID:34680961", source="PMID:24890200"} ! GCK
 property_value: curated_content_resource "https://www.malacards.org/card/hyperinsulinemic_hypoglycemia_familial_3_2" xsd:anyURI {source="MONDO:MalaCards"}
-property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4985" xsd:anyURI
+property_value: http://purl.org/dc/terms/creator https://clinicalgenome.org/affiliation/40016/
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9861" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/9930/hyperinsulinemic-hypoglycemia-familial-3" xsd:anyURI {source="GARD:0009930"}
 
 [Term]

```
