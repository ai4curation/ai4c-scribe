# PR #10210 — GINS3 Meier-Gorlin syndrome

- **Ontology**: mondo
- **Repo**: monarch-initiative/mondo
- **Issue**: [#9933](https://github.com/monarch-initiative/mondo/issues/9933)
- **PR**: [#10210](https://github.com/monarch-initiative/mondo/pull/10210)
- **Author**: @MeeSiing
- **Merged**: 2026-05-01
- **task_type**: synonym_update
- **difficulty**: simple
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: approved_first_time

## Context

Issue #9933 raised a question about whether there was sufficient evidence to associate GINS3 with Meier-Gorlin syndrome, noting a 2024 publication confirming pathogenicity of GINS3 variants. The issue referenced functional studies in yeast confirming the disease association for MONDO:0980992.

## Changes Made

The PR added 8 lines of synonym annotations to MONDO:0980992 in mondo-edit.obo. These additions likely include gene-centric synonyms (e.g., "GINS3-related Meier-Gorlin syndrome") and potentially alternate disease names referenced in the literature, each with appropriate synonym scope and evidence annotations.

## Resolution

Simple difficulty as this is a pure additive change with no deletions. The curator identified the relevant term and added multiple synonyms with evidence codes. An agent needs to understand OBO synonym syntax, appropriate scope tags (EXACT, RELATED, etc.), and how to cite PMIDs as evidence for synonym assertions.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424f..1f59ad4a5b 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -617093,13 +617093,21 @@ is_a: MONDO:0016660 {source="OMIM:621507", source="https://orcid.org/0000-0002-4
 [Term]
 id: MONDO:0980992
 name: Meier-Gorlin syndrome 9
+def: "Any Meier-Gorlin syndrome in which the cause of the disease is a mutation in the GINS3 gene." [MONDO:patterns/disease_series_by_gene, OMIM:621512, PMID:38773883]
 subset: doid {source="DOID:0051069"}
 subset: inferred_rare
 subset: omim {source="OMIM:621512"}
 subset: rare
+synonym: "GINS3 Meier-Gorlin syndrome" EXACT [https://orcid.org/0000-0001-6330-7526, PMID:38773883]
+synonym: "Meier-Gorlin syndrome 9" EXACT [DOID:0051069, OMIM:621512]
+synonym: "MGORS9" EXACT ABBREVIATION [OMIM:621512]
 xref: DOID:0051069 {source="MONDO:equivalentTo"}
 xref: OMIM:621512 {source="MONDO:equivalentTo"}
 is_a: MONDO:0016817 {source="OMIM:621512", source="https://orcid.org/0000-0002-4142-7153"} ! Meier-Gorlin syndrome
+intersection_of: MONDO:0016817 ! Meier-Gorlin syndrome
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851 {source="OMIM:621512", source="PMID:38773883"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9933" xsd:anyURI
 
 [Term]
 id: MONDO:0980997

```

## Agent Attempts (5)

### Attempt 1: kimi-k2.6 / opencode

- **Eval PR**: [#274](https://github.com/ai4curation/eval-ont-agent-mondo/pull/274)
- **F1**: 0.526  **Precision**: 0.625  **Recall**: 0.455  **Jaccard**: 0.357
- **Trace**: [25755603999](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25755603999)
- **Workflow run**: [25755603999](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755603999)

#### Agent PR Comment

## Summary

This PR addresses **issue #9933** by completing the missing gene association for **MONDO:0980992 "Meier-Gorlin syndrome 9"**. The term already existed with an OMIM cross-reference (OMIM:621512), but the causal gene relationship and corresponding synonyms had not yet been added.

## Changes made to MONDO:0980992

1. **Added definition** following the `disease_series_by_gene` design pattern:
   > "Any Meier-Gorlin syndrome in which the cause of the disease is a mutation in the GINS3 gene."

2. **Added exact synonyms**:
   - `GINS3 Meier-Gorlin syndrome` (with `MONDO:design_pattern` and `MONDO:patterns/disease_series_by_gene` sources)
   - `Meier-Gorlin syndrome caused by mutation in GINS3`
   - `Meier-Gorlin syndrome 9` (with DOID and OMIM sources)
   - `Meier-Gorlin syndrome type 9`
   - `MGORS9` (exact abbreviation sourced from OMIM:621512)

3. **Added logical definition** (`intersection_of`):
   - `Meier-Gorlin syndrome`
   - `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851` (GINS3)

4. **Added relationships**:
   - `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851 {source="OMIM:621512"}`
   - `has_characteristic HP:0000007 {source="MONDO:HPOA", source="OMIM:621512"}` (Autosomal recessive inheritance)

5. **Added term tracker item** linking back to the originating GitHub issue.

## Rationale

The issue reported that while MONDO had a term for Meier-Gorlin syndrome 9 (OMIM:621512), the gene-to-disease association had not yet been included, which is why it was not visible on Monarch Initiative. The curation team confirmed that adding the **GINS3** gene association and the synonym **"GINS3 Meier-Gorlin syndrome"** would resolve this. The update follows the same design pattern used by other numbered Meier-Gorlin syndrome terms in MONDO (e.g., MONDO:0009143, MONDO:0013428, MONDO:0014894).

## Validation performed

- [x] Checked out MONDO:0980992 for editing
- [x] Verified **HGNC:25851** is the correct identifier for **GINS3** via HGNC REST API
- [x] Confirmed **OMIM:621512** title includes "MEIER-GORLIN SYNDROME 9; MGORS9" via NCBI E-utilities
- [x] Reviewed the `disease_series_by_gene` pattern applied to sibling terms (Meier-Gorlin syndrome 1, 2, 3, 7)
- [x] Edited the term following the established sibling pattern
- [x] Checked the term back into `mondo-edit.obo`
- [x] Ran `make NORM` to normalize serialization
- [x] Ran `robot convert` syntax check — passed with no errors
- [x] Verified the final diff modifies only MONDO:0980992

## Background research

- **PMID:38773883** (cited in the issue) was reviewed via PubMed: *"Functional studies in yeast confirm the pathogenicity of a new GINS3 Meier-Gorlin syndrome variant."* This publication supports the GINS3 gene-disease association.
- The OMIM reference (OMIM:621512) was used as the primary source for the gene relationship, consistent with how other Meier-Gorlin syndrome gene associations are sourced in MONDO.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755603999)


#### Agent Issue Comment

Hi @ValWood and @MeeSiing,

I have added the GINS3 gene association to **MONDO:0980992 Meier-Gorlin syndrome 9** and included **"GINS3 Meier-Gorlin syndrome"** as an exact synonym, as discussed in this thread.

The gene association (`has_material_basis_in_germline_mutation_in HGNC:25851` / GINS3) is sourced from **OMIM:621512**. The term now also includes:
- A definition following the `disease_series_by_gene` pattern
- The logical definition (`intersection_of`) linking it to Meier-Gorlin syndrome and the GINS3 gene
- Autosomal recessive inheritance annotation
- A term tracker item linking back to this issue

This should resolve the missing association you noted at monarchinitiative.org. Please let me know if any further adjustments are needed.

Changes committed in PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755603999)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424..11990af2f 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -617093,13 +617093,24 @@ is_a: MONDO:0016660 {source="OMIM:621507", source="https://orcid.org/0000-0002-4
 [Term]
 id: MONDO:0980992
 name: Meier-Gorlin syndrome 9
+def: "Any Meier-Gorlin syndrome in which the cause of the disease is a mutation in the GINS3 gene." [MONDO:patterns/disease_series_by_gene]
 subset: doid {source="DOID:0051069"}
 subset: inferred_rare
 subset: omim {source="OMIM:621512"}
 subset: rare
+synonym: "GINS3 Meier-Gorlin syndrome" EXACT [MONDO:design_pattern, MONDO:patterns/disease_series_by_gene]
+synonym: "Meier-Gorlin syndrome 9" EXACT [DOID:0051069, OMIM:621512]
+synonym: "Meier-Gorlin syndrome caused by mutation in GINS3" EXACT [MONDO:design_pattern]
+synonym: "Meier-Gorlin syndrome type 9" EXACT []
+synonym: "MGORS9" EXACT ABBREVIATION [OMIM:621512]
 xref: DOID:0051069 {source="MONDO:equivalentTo"}
 xref: OMIM:621512 {source="MONDO:equivalentTo"}
 is_a: MONDO:0016817 {source="OMIM:621512", source="https://orcid.org/0000-0002-4142-7153"} ! Meier-Gorlin syndrome
+intersection_of: MONDO:0016817 ! Meier-Gorlin syndrome
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851
+relationship: has_characteristic HP:0000007 {source="MONDO:HPOA", source="OMIM:621512"} ! Autosomal recessive inheritance
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851 {source="OMIM:621512"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9933" xsd:anyURI
 
 [Term]
 id: MONDO:0980997

```

### Attempt 2: claude-opus-4.7 / claude

- **Eval PR**: [#403](https://github.com/ai4curation/eval-ont-agent-mondo/pull/403)
- **F1**: 0.333  **Precision**: 0.375  **Recall**: 0.300  **Jaccard**: 0.200
- **Trace**: [25818955513](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25818955513)
- **Workflow run**: [25818955513](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25818955513)

#### Agent PR Comment

# GINS3 gene association for Meier-Gorlin syndrome 9 (MONDO:0980992)

Addresses monarch-initiative/mondo#9933.

#### Agent Issue Comment

Thanks @ValWood and @MeeSiing. The GINS3 gene association has been added to MONDO:0980992 'Meier-Gorlin syndrome 9' (HGNC:25851 / GINS3), with the requested "GINS3 Meier-Gorlin syndrome" exact synonym, a definition and logical definition following the `disease_series_by_gene` design pattern, and sources to OMIM:621512, PMID:35603789, and PMID:38773883.

The gene association should be visible from Monarch once the next Mondo release is propagated.

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25818955513)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424..3f8f0d383 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -617093,13 +617093,23 @@ is_a: MONDO:0016660 {source="OMIM:621507", source="https://orcid.org/0000-0002-4
 [Term]
 id: MONDO:0980992
 name: Meier-Gorlin syndrome 9
+def: "Any Meier-Gorlin syndrome in which the cause of the disease is a mutation in the GINS3 gene." [MONDO:patterns/disease_series_by_gene, PMID:35603789, PMID:38773883]
 subset: doid {source="DOID:0051069"}
 subset: inferred_rare
 subset: omim {source="OMIM:621512"}
 subset: rare
+synonym: "GINS3 Meier-Gorlin syndrome" EXACT [MONDO:design_pattern, MONDO:patterns/disease_series_by_gene]
+synonym: "Meier-Gorlin syndrome 9" EXACT [DOID:0051069, OMIM:621512]
+synonym: "Meier-Gorlin syndrome caused by mutation in GINS3" EXACT [MONDO:design_pattern]
+synonym: "Meier-Gorlin syndrome type 9" EXACT []
+synonym: "MGORS9" RELATED ABBREVIATION []
 xref: DOID:0051069 {source="MONDO:equivalentTo"}
 xref: OMIM:621512 {source="MONDO:equivalentTo"}
 is_a: MONDO:0016817 {source="OMIM:621512", source="https://orcid.org/0000-0002-4142-7153"} ! Meier-Gorlin syndrome
+intersection_of: MONDO:0016817 ! Meier-Gorlin syndrome
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851 ! GINS3
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851 {source="OMIM:621512", source="PMID:35603789", source="PMID:38773883"} ! GINS3
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9933" xsd:anyURI
 
 [Term]
 id: MONDO:0980997

```

### Attempt 3: claude-sonnet-4.5 / claude

- **Eval PR**: [#452](https://github.com/ai4curation/eval-ont-agent-mondo/pull/452)
- **F1**: 0.316  **Precision**: 0.375  **Recall**: 0.273  **Jaccard**: 0.188
- **Trace**: [25867777748](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25867777748)
- **Workflow run**: [25867777748](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867777748)

#### Agent PR Comment

## Summary

This PR adds the GINS3 gene association to MONDO:0980992 'Meier-Gorlin syndrome 9', addressing issue #9933 where the gene association was not visible in the Monarch Initiative.

#### Agent Issue Comment

The gene association for GINS3 has been added to MONDO:0980992 'Meier-Gorlin syndrome 9'. The changes include:

1. Added the synonym "GINS3 Meier-Gorlin syndrome" with proper citation (PMID:38773883)
2. Added the gene association relationship `has_material_basis_in_germline_mutation_in` linking to GINS3 (HGNC:25851)
3. Added logical definitions following the disease_series_by_gene pattern
4. Added a proper definition: "Any Meier-Gorlin syndrome in which the cause of the disease is a mutation in the GINS3 gene."

These changes follow the established pattern used by other Meier-Gorlin syndrome subtypes (MGS 1-8) and should make the GINS3 gene association visible in the Monarch Initiative at https://monarchinitiative.org/HGNC:25851.

Changes committed in PR #&lt;NN&gt;.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867777748)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424..aad9643db 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -617093,13 +617093,22 @@ is_a: MONDO:0016660 {source="OMIM:621507", source="https://orcid.org/0000-0002-4
 [Term]
 id: MONDO:0980992
 name: Meier-Gorlin syndrome 9
+def: "Any Meier-Gorlin syndrome in which the cause of the disease is a mutation in the GINS3 gene." [MONDO:patterns/disease_series_by_gene]
 subset: doid {source="DOID:0051069"}
 subset: inferred_rare
 subset: omim {source="OMIM:621512"}
 subset: rare
+synonym: "GINS3 Meier-Gorlin syndrome" EXACT [MONDO:design_pattern, MONDO:patterns/disease_series_by_gene, PMID:38773883]
+synonym: "Meier-Gorlin syndrome 9" EXACT [DOID:0051069, OMIM:621512]
+synonym: "Meier-Gorlin syndrome caused by mutation in GINS3" EXACT [MONDO:design_pattern]
+synonym: "Meier-Gorlin syndrome type 9" EXACT []
+synonym: "MGORS9" RELATED ABBREVIATION []
 xref: DOID:0051069 {source="MONDO:equivalentTo"}
 xref: OMIM:621512 {source="MONDO:equivalentTo"}
-is_a: MONDO:0016817 {source="OMIM:621512", source="https://orcid.org/0000-0002-4142-7153"} ! Meier-Gorlin syndrome
+is_a: MONDO:0016817 {source="MONDO:Redundant", source="OMIM:621512", source="https://orcid.org/0000-0002-4142-7153"} ! Meier-Gorlin syndrome
+intersection_of: MONDO:0016817 ! Meier-Gorlin syndrome
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851 {source="PMID:38773883"}
 
 [Term]
 id: MONDO:0980997

```

### Attempt 4: claude-haiku-4.5 / claude

- **Eval PR**: [#477](https://github.com/ai4curation/eval-ont-agent-mondo/pull/477)
- **F1**: 0.308  **Precision**: 0.250  **Recall**: 0.400  **Jaccard**: 0.182
- **Trace**: [25888766533](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25888766533)
- **Workflow run**: [25888766533](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25888766533)

#### Agent PR Comment

# GINS3 Gene Association for Meier-Gorlin Syndrome 9

#### Agent Issue Comment

# Resolution for GINS3 Meier-Gorlin syndrome #9933

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424..35b057171 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -617093,13 +617093,18 @@ is_a: MONDO:0016660 {source="OMIM:621507", source="https://orcid.org/0000-0002-4
 [Term]
 id: MONDO:0980992
 name: Meier-Gorlin syndrome 9
+def: "Any Meier-Gorlin syndrome in which the cause of the disease is a mutation in the GINS3 gene." [MONDO:patterns/disease_series_by_gene, PMID:38773883]
 subset: doid {source="DOID:0051069"}
 subset: inferred_rare
 subset: omim {source="OMIM:621512"}
 subset: rare
+synonym: "GINS3 Meier-Gorlin syndrome" EXACT [MONDO:design_pattern, MONDO:patterns/disease_series_by_gene]
 xref: DOID:0051069 {source="MONDO:equivalentTo"}
 xref: OMIM:621512 {source="MONDO:equivalentTo"}
 is_a: MONDO:0016817 {source="OMIM:621512", source="https://orcid.org/0000-0002-4142-7153"} ! Meier-Gorlin syndrome
+intersection_of: MONDO:0016817 ! Meier-Gorlin syndrome
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851 {source="PMID:38773883"}
 
 [Term]
 id: MONDO:0980997

```

### Attempt 5: claude-haiku-4.5 / claude

- **Eval PR**: [#419](https://github.com/ai4curation/eval-ont-agent-mondo/pull/419)
- **F1**: 0.308  **Precision**: 0.250  **Recall**: 0.400  **Jaccard**: 0.182
- **Trace**: [25844264116](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25844264116)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424..35b057171 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -617093,13 +617093,18 @@ is_a: MONDO:0016660 {source="OMIM:621507", source="https://orcid.org/0000-0002-4
 [Term]
 id: MONDO:0980992
 name: Meier-Gorlin syndrome 9
+def: "Any Meier-Gorlin syndrome in which the cause of the disease is a mutation in the GINS3 gene." [MONDO:patterns/disease_series_by_gene, PMID:38773883]
 subset: doid {source="DOID:0051069"}
 subset: inferred_rare
 subset: omim {source="OMIM:621512"}
 subset: rare
+synonym: "GINS3 Meier-Gorlin syndrome" EXACT [MONDO:design_pattern, MONDO:patterns/disease_series_by_gene]
 xref: DOID:0051069 {source="MONDO:equivalentTo"}
 xref: OMIM:621512 {source="MONDO:equivalentTo"}
 is_a: MONDO:0016817 {source="OMIM:621512", source="https://orcid.org/0000-0002-4142-7153"} ! Meier-Gorlin syndrome
+intersection_of: MONDO:0016817 ! Meier-Gorlin syndrome
+intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851
+relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851 {source="PMID:38773883"}
 
 [Term]
 id: MONDO:0980997

```
