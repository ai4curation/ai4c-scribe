# PR #10116 — Isolated megalencephaly Orphanet Xref

- **Ontology**: mondo
- **Repo**: monarch-initiative/mondo
- **Issue**: [#9854](https://github.com/monarch-initiative/mondo/issues/9854)
- **PR**: [#10116](https://github.com/monarch-initiative/mondo/pull/10116)
- **Author**: @MeeSiing
- **Merged**: 2026-04-08
- **task_type**: other
- **difficulty**: medium
- **scoping**: tightly_scoped
- **scope**: single_term
- **review_outcome**: changes_requested

## Context

Issue #9854 reported that the Orphanet xref for "Isolated megalencephaly" (ORPHANET:2477) was attached to MONDO:0016608 (megalencephaly) but should instead be on MONDO:0017089 (isolated megalencephaly). The distinction between the broader "megalencephaly" and the more specific "isolated megalencephaly" is clinically relevant for mapping to external databases.

## Changes Made

The PR required 3 commits to complete. The first moved the Orphanet xref to the correct term MONDO:0017089. The second removed a MedDRA xref (MedDRA:10050183) that was also incorrectly placed on isolated megalencephaly. The third commit addressed the source annotation for the MedDRA xref, as the curator was uncertain which source to assign after removing the Orphanet provenance link.

## Resolution

Moderate difficulty because cross-reference corrections require understanding provenance chains. When an xref is moved between terms, associated source annotations may need updating, and other xrefs that depended on the same provenance chain may be affected. The curator's uncertainty about the MedDRA source annotation illustrates a common challenge: maintaining annotation integrity when editing cross-references.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb40..00e98d880b 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -424961,10 +424961,6 @@ name: megalencephaly
 def: "A congenital abnormality in which the occipitofrontal circumference is greater than two standard deviations above the mean for a given age. It is associated with hydrocephalus; subdural effusion; arachnoid cysts; or is part of a genetic condition (e.g., alexander disease; sotos syndrome)." [MESH:D058627]
 subset: gard_rare {source="GARD:0016601", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
-subset: ordo_disorder {source="Orphanet:2477"}
-subset: ordo_malformation_syndrome {source="Orphanet:2477"}
-subset: orphanet {source="Orphanet:2477"}
-subset: orphanet_rare {source="Orphanet:2477"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "macroencephaly" EXACT [icd11.foundation:368780653]
@@ -424972,13 +424968,12 @@ synonym: "megalencephaly" EXACT [ICD10CM:Q04.5, icd11.foundation:368780653, MOND
 synonym: "megalencephaly (disease)" EXACT [https://orcid.org/0000-0002-6601-2165]
 xref: GARD:0016601 {source="MONDO:GARD"}
 xref: HP:0001355 {source="MONDO:otherHierarchy"}
-xref: ICD10CM:Q04.5 {source="https://orcid.org/0009-0001-6494-4831", source="Orphanet:2477", source="MONDO:equivalentTo", source="https://orcid.org/0000-0002-5002-8648", source="Orphanet:2477/e"}
-xref: icd11.foundation:368780653 {source="Orphanet:2477", source="MONDO:equivalentTo"}
+xref: ICD10CM:Q04.5 {source="https://orcid.org/0009-0001-6494-4831", source="MONDO:equivalentTo", source="https://orcid.org/0000-0002-5002-8648"}
+xref: icd11.foundation:368780653 {source="MONDO:equivalentTo"}
 xref: ICD9:742.4 {source="MONDO:relatedTo", source="MONDO:i2s"}
-xref: MedDRA:10050183 {source="Orphanet:2477", source="Orphanet:2477/e"}
+xref: MedDRA:10050183 {source="MONDO:equivalentTo"}
 xref: MEDGEN:65141 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:D058627 {source="MONDO:equivalentTo"}
-xref: Orphanet:2477 {source="MONDO:equivalentTo"}
 xref: SCTID:9740002 {source="MONDO:equivalentTo"}
 xref: UMLS:C0221355 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:65141"}
 is_a: MONDO:0005560 {source="https://orcid.org/0000-0002-4142-7153"} ! brain disorder
@@ -424986,6 +424981,7 @@ is_a: MONDO:0021147 {source="https://orcid.org/0000-0002-4142-7153"} ! disorder
 property_value: curated_content_resource "https://www.malacards.org/card/megalencephaly" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6876" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9854" xsd:anyURI
 property_value: IAO:0000589 "megalencephaly (disease)" xsd:string
 
 [Term]
@@ -435655,13 +435651,19 @@ name: isolated megalencephaly
 def: "A megalencephaly (disease) that is not part of a larger syndrome." [MONDO:patterns/isolated]
 subset: gard_rare {source="GARD:0020977", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
+subset: ordo_disorder {source="Orphanet:2477"}
+subset: ordo_malformation_syndrome {source="Orphanet:2477"}
+subset: orphanet {source="Orphanet:2477"}
+subset: orphanet_rare {source="Orphanet:2477"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "isolated macrencephaly" EXACT []
 synonym: "isolated megalencephaly (disease)" EXACT []
 synonym: "nonsyndromic megalencephaly (disease)" EXACT [MONDO:patterns/isolated]
 xref: GARD:0020977 {source="MONDO:GARD"}
+xref: icd11.foundation:368780653 {source="Orphanet:2477"}
 xref: MEDGEN:439426 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
+xref: Orphanet:2477 {source="MONDO:equivalentTo"}
 xref: Orphanet:268920 {source="MONDO:equivalentObsolete"}
 xref: UMLS:C2720434 {source="MEDGEN:439426", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0016608 {source="MONDO:Redundant", source="Orphanet:268920"} ! megalencephaly
@@ -435669,6 +435671,7 @@ is_a: MONDO:0021147 {source="MONDO:Redundant", source="Orphanet:268920", source=
 intersection_of: MONDO:0016608 ! megalencephaly
 intersection_of: has_characteristic MONDO:0021128 ! has an isolated presentation
 property_value: curated_content_resource "https://www.malacards.org/card/isolated_megalencephaly" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9854" xsd:anyURI
 
 [Term]
 id: MONDO:0017090

```

## Agent Attempts (5)

### Attempt 1: kimi-k2.6 / opencode

- **Eval PR**: [#277](https://github.com/ai4curation/eval-ont-agent-mondo/pull/277)
- **F1**: 0.941  **Precision**: 0.889  **Recall**: 1.000  **Jaccard**: 0.889
- **Trace**: [25755644508](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25755644508)
- **Workflow run**: [25755644508](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755644508)

#### Agent PR Comment

# Fix for Issue #9854 — Move Orphanet:2477 xref to isolated megalencephaly

#### Agent Issue Comment

Thank you for reporting this! The Orphanet:2477 xref has been moved from `megalencephaly` (MONDO:0016608) to `isolated megalencephaly` (MONDO:0017089), along with the associated orphanet subsets and cleanup of Orphanet-derived source annotations on the parent term. Changes committed in PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755644508)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..d4a0c0bc3 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -424961,10 +424961,6 @@ name: megalencephaly
 def: "A congenital abnormality in which the occipitofrontal circumference is greater than two standard deviations above the mean for a given age. It is associated with hydrocephalus; subdural effusion; arachnoid cysts; or is part of a genetic condition (e.g., alexander disease; sotos syndrome)." [MESH:D058627]
 subset: gard_rare {source="GARD:0016601", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
-subset: ordo_disorder {source="Orphanet:2477"}
-subset: ordo_malformation_syndrome {source="Orphanet:2477"}
-subset: orphanet {source="Orphanet:2477"}
-subset: orphanet_rare {source="Orphanet:2477"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "macroencephaly" EXACT [icd11.foundation:368780653]
@@ -424972,13 +424968,11 @@ synonym: "megalencephaly" EXACT [ICD10CM:Q04.5, icd11.foundation:368780653, MOND
 synonym: "megalencephaly (disease)" EXACT [https://orcid.org/0000-0002-6601-2165]
 xref: GARD:0016601 {source="MONDO:GARD"}
 xref: HP:0001355 {source="MONDO:otherHierarchy"}
-xref: ICD10CM:Q04.5 {source="https://orcid.org/0009-0001-6494-4831", source="Orphanet:2477", source="MONDO:equivalentTo", source="https://orcid.org/0000-0002-5002-8648", source="Orphanet:2477/e"}
-xref: icd11.foundation:368780653 {source="Orphanet:2477", source="MONDO:equivalentTo"}
+xref: ICD10CM:Q04.5 {source="https://orcid.org/0009-0001-6494-4831", source="MONDO:equivalentTo", source="https://orcid.org/0000-0002-5002-8648"}
+xref: icd11.foundation:368780653 {source="MONDO:equivalentTo"}
 xref: ICD9:742.4 {source="MONDO:relatedTo", source="MONDO:i2s"}
-xref: MedDRA:10050183 {source="Orphanet:2477", source="Orphanet:2477/e"}
 xref: MEDGEN:65141 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:D058627 {source="MONDO:equivalentTo"}
-xref: Orphanet:2477 {source="MONDO:equivalentTo"}
 xref: SCTID:9740002 {source="MONDO:equivalentTo"}
 xref: UMLS:C0221355 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:65141"}
 is_a: MONDO:0005560 {source="https://orcid.org/0000-0002-4142-7153"} ! brain disorder
@@ -424986,6 +424980,7 @@ is_a: MONDO:0021147 {source="https://orcid.org/0000-0002-4142-7153"} ! disorder
 property_value: curated_content_resource "https://www.malacards.org/card/megalencephaly" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6876" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9854" xsd:anyURI
 property_value: IAO:0000589 "megalencephaly (disease)" xsd:string
 
 [Term]
@@ -435655,6 +435650,10 @@ name: isolated megalencephaly
 def: "A megalencephaly (disease) that is not part of a larger syndrome." [MONDO:patterns/isolated]
 subset: gard_rare {source="GARD:0020977", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
+subset: ordo_disorder {source="Orphanet:2477"}
+subset: ordo_malformation_syndrome {source="Orphanet:2477"}
+subset: orphanet {source="Orphanet:2477"}
+subset: orphanet_rare {source="Orphanet:2477"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "isolated macrencephaly" EXACT []
@@ -435662,6 +435661,7 @@ synonym: "isolated megalencephaly (disease)" EXACT []
 synonym: "nonsyndromic megalencephaly (disease)" EXACT [MONDO:patterns/isolated]
 xref: GARD:0020977 {source="MONDO:GARD"}
 xref: MEDGEN:439426 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
+xref: Orphanet:2477 {source="MONDO:equivalentTo"}
 xref: Orphanet:268920 {source="MONDO:equivalentObsolete"}
 xref: UMLS:C2720434 {source="MEDGEN:439426", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0016608 {source="MONDO:Redundant", source="Orphanet:268920"} ! megalencephaly
@@ -435669,6 +435669,7 @@ is_a: MONDO:0021147 {source="MONDO:Redundant", source="Orphanet:268920", source=
 intersection_of: MONDO:0016608 ! megalencephaly
 intersection_of: has_characteristic MONDO:0021128 ! has an isolated presentation
 property_value: curated_content_resource "https://www.malacards.org/card/isolated_megalencephaly" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9854" xsd:anyURI
 
 [Term]
 id: MONDO:0017090

```

### Attempt 2: claude-sonnet-4.5 / claude

- **Eval PR**: [#457](https://github.com/ai4curation/eval-ont-agent-mondo/pull/457)
- **F1**: 0.895  **Precision**: 0.944  **Recall**: 0.850  **Jaccard**: 0.810
- **Trace**: [25867814044](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25867814044)
- **Workflow run**: [25867814044](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867814044)

#### Agent PR Comment

## Summary

This PR addresses issue #9854 by moving the Orphanet:2477 xref from MONDO:0016608 (megalencephaly) to MONDO:0017089 (isolated megalencephaly), where it is semantically more appropriate.

#### Agent Issue Comment

The Orphanet:2477 (Isolated megalencephaly) xref has been successfully moved from MONDO:0016608 (megalencephaly) to MONDO:0017089 (isolated megalencephaly).

Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867814044)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..da7fd4205 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -424961,10 +424961,6 @@ name: megalencephaly
 def: "A congenital abnormality in which the occipitofrontal circumference is greater than two standard deviations above the mean for a given age. It is associated with hydrocephalus; subdural effusion; arachnoid cysts; or is part of a genetic condition (e.g., alexander disease; sotos syndrome)." [MESH:D058627]
 subset: gard_rare {source="GARD:0016601", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
-subset: ordo_disorder {source="Orphanet:2477"}
-subset: ordo_malformation_syndrome {source="Orphanet:2477"}
-subset: orphanet {source="Orphanet:2477"}
-subset: orphanet_rare {source="Orphanet:2477"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "macroencephaly" EXACT [icd11.foundation:368780653]
@@ -424972,13 +424968,12 @@ synonym: "megalencephaly" EXACT [ICD10CM:Q04.5, icd11.foundation:368780653, MOND
 synonym: "megalencephaly (disease)" EXACT [https://orcid.org/0000-0002-6601-2165]
 xref: GARD:0016601 {source="MONDO:GARD"}
 xref: HP:0001355 {source="MONDO:otherHierarchy"}
-xref: ICD10CM:Q04.5 {source="https://orcid.org/0009-0001-6494-4831", source="Orphanet:2477", source="MONDO:equivalentTo", source="https://orcid.org/0000-0002-5002-8648", source="Orphanet:2477/e"}
-xref: icd11.foundation:368780653 {source="Orphanet:2477", source="MONDO:equivalentTo"}
+xref: ICD10CM:Q04.5 {source="https://orcid.org/0009-0001-6494-4831", source="MONDO:equivalentTo", source="https://orcid.org/0000-0002-5002-8648"}
+xref: icd11.foundation:368780653 {source="MONDO:equivalentTo"}
 xref: ICD9:742.4 {source="MONDO:relatedTo", source="MONDO:i2s"}
-xref: MedDRA:10050183 {source="Orphanet:2477", source="Orphanet:2477/e"}
+xref: MedDRA:10050183 {source="MONDO:equivalentTo"}
 xref: MEDGEN:65141 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:D058627 {source="MONDO:equivalentTo"}
-xref: Orphanet:2477 {source="MONDO:equivalentTo"}
 xref: SCTID:9740002 {source="MONDO:equivalentTo"}
 xref: UMLS:C0221355 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:65141"}
 is_a: MONDO:0005560 {source="https://orcid.org/0000-0002-4142-7153"} ! brain disorder
@@ -424986,6 +424981,7 @@ is_a: MONDO:0021147 {source="https://orcid.org/0000-0002-4142-7153"} ! disorder
 property_value: curated_content_resource "https://www.malacards.org/card/megalencephaly" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6876" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9854" xsd:anyURI
 property_value: IAO:0000589 "megalencephaly (disease)" xsd:string
 
 [Term]
@@ -435655,13 +435651,21 @@ name: isolated megalencephaly
 def: "A megalencephaly (disease) that is not part of a larger syndrome." [MONDO:patterns/isolated]
 subset: gard_rare {source="GARD:0020977", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
+subset: ordo_disorder {source="Orphanet:2477"}
+subset: ordo_malformation_syndrome {source="Orphanet:2477"}
+subset: orphanet {source="Orphanet:2477"}
+subset: orphanet_rare {source="Orphanet:2477"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "isolated macrencephaly" EXACT []
 synonym: "isolated megalencephaly (disease)" EXACT []
 synonym: "nonsyndromic megalencephaly (disease)" EXACT [MONDO:patterns/isolated]
 xref: GARD:0020977 {source="MONDO:GARD"}
+xref: ICD10CM:Q04.5 {source="Orphanet:2477", source="MONDO:equivalentTo", source="Orphanet:2477/e"}
+xref: icd11.foundation:368780653 {source="Orphanet:2477", source="MONDO:equivalentTo"}
+xref: MedDRA:10050183 {source="Orphanet:2477", source="Orphanet:2477/e"}
 xref: MEDGEN:439426 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
+xref: Orphanet:2477 {source="MONDO:equivalentTo"}
 xref: Orphanet:268920 {source="MONDO:equivalentObsolete"}
 xref: UMLS:C2720434 {source="MEDGEN:439426", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0016608 {source="MONDO:Redundant", source="Orphanet:268920"} ! megalencephaly
@@ -435669,6 +435673,7 @@ is_a: MONDO:0021147 {source="MONDO:Redundant", source="Orphanet:268920", source=
 intersection_of: MONDO:0016608 ! megalencephaly
 intersection_of: has_characteristic MONDO:0021128 ! has an isolated presentation
 property_value: curated_content_resource "https://www.malacards.org/card/isolated_megalencephaly" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9854" xsd:anyURI
 
 [Term]
 id: MONDO:0017090

```

### Attempt 3: gemma-4-31b / opencode

- **Eval PR**: [#228](https://github.com/ai4curation/eval-ont-agent-mondo/pull/228)
- **F1**: 0.882  **Precision**: 0.833  **Recall**: 0.938  **Jaccard**: 0.789
- **Trace**: [25704295293](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25704295293)
- **Workflow run**: [25704295293](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25704295293)

#### Agent PR Comment

## Summary
Moved Orphanet xref `Orphanet:2477` and corresponding subsets from `MONDO:0016608` (megalencephaly) to `MONDO:0017089` (isolated megalencephaly).

## Rationale
The issue requested that Isolated megalencephaly (ORPHANET 2477) be moved to the more specific term `MONDO:0017089`.

## Checklist
- [x] Verified current location of `Orphanet:2477` in `MONDO:0016608`.
- [x] Verified target term `MONDO:0017089`.
- [x] Removed `Orphanet:2477` xref and related subsets from `MONDO:0016608`.
- [x] Added `Orphanet:2477` xref and related subsets to `MONDO:0017089`.
- [x] Checked in changes and committed.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25704295293)


#### Agent Issue Comment

The Orphanet xref Orphanet:2477 and its associated subsets have been moved from MONDO:0016608 (megalencephaly) to MONDO:0017089 (isolated megalencephaly), as requested.

Changes committed in PR #<NN>.
---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/google/gemma-4-31B-it`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25704295293)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..0167ac1cd 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -424961,10 +424961,6 @@ name: megalencephaly
 def: "A congenital abnormality in which the occipitofrontal circumference is greater than two standard deviations above the mean for a given age. It is associated with hydrocephalus; subdural effusion; arachnoid cysts; or is part of a genetic condition (e.g., alexander disease; sotos syndrome)." [MESH:D058627]
 subset: gard_rare {source="GARD:0016601", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
-subset: ordo_disorder {source="Orphanet:2477"}
-subset: ordo_malformation_syndrome {source="Orphanet:2477"}
-subset: orphanet {source="Orphanet:2477"}
-subset: orphanet_rare {source="Orphanet:2477"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "macroencephaly" EXACT [icd11.foundation:368780653]
@@ -424972,13 +424968,12 @@ synonym: "megalencephaly" EXACT [ICD10CM:Q04.5, icd11.foundation:368780653, MOND
 synonym: "megalencephaly (disease)" EXACT [https://orcid.org/0000-0002-6601-2165]
 xref: GARD:0016601 {source="MONDO:GARD"}
 xref: HP:0001355 {source="MONDO:otherHierarchy"}
-xref: ICD10CM:Q04.5 {source="https://orcid.org/0009-0001-6494-4831", source="Orphanet:2477", source="MONDO:equivalentTo", source="https://orcid.org/0000-0002-5002-8648", source="Orphanet:2477/e"}
-xref: icd11.foundation:368780653 {source="Orphanet:2477", source="MONDO:equivalentTo"}
+xref: ICD10CM:Q04.5 {source="https://orcid.org/0009-0001-6494-4831", source="MONDO:equivalentTo", source="https://orcid.org/0000-0002-5002-8648"}
+xref: icd11.foundation:368780653 {source="MONDO:equivalentTo"}
 xref: ICD9:742.4 {source="MONDO:relatedTo", source="MONDO:i2s"}
-xref: MedDRA:10050183 {source="Orphanet:2477", source="Orphanet:2477/e"}
+xref: MedDRA:10050183 {}
 xref: MEDGEN:65141 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:D058627 {source="MONDO:equivalentTo"}
-xref: Orphanet:2477 {source="MONDO:equivalentTo"}
 xref: SCTID:9740002 {source="MONDO:equivalentTo"}
 xref: UMLS:C0221355 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:65141"}
 is_a: MONDO:0005560 {source="https://orcid.org/0000-0002-4142-7153"} ! brain disorder
@@ -435655,6 +435650,10 @@ name: isolated megalencephaly
 def: "A megalencephaly (disease) that is not part of a larger syndrome." [MONDO:patterns/isolated]
 subset: gard_rare {source="GARD:0020977", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
+subset: ordo_disorder {source="Orphanet:2477"}
+subset: ordo_malformation_syndrome {source="Orphanet:2477"}
+subset: orphanet {source="Orphanet:2477"}
+subset: orphanet_rare {source="Orphanet:2477"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "isolated macrencephaly" EXACT []
@@ -435663,6 +435662,7 @@ synonym: "nonsyndromic megalencephaly (disease)" EXACT [MONDO:patterns/isolated]
 xref: GARD:0020977 {source="MONDO:GARD"}
 xref: MEDGEN:439426 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:268920 {source="MONDO:equivalentObsolete"}
+xref: Orphanet:2477 {source="MONDO:equivalentTo"}
 xref: UMLS:C2720434 {source="MEDGEN:439426", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0016608 {source="MONDO:Redundant", source="Orphanet:268920"} ! megalencephaly
 is_a: MONDO:0021147 {source="MONDO:Redundant", source="Orphanet:268920", source="Orphanet:268920/inferred"} ! disorder of development or morphogenesis

```

### Attempt 4: claude-opus-4.7 / claude

- **Eval PR**: [#385](https://github.com/ai4curation/eval-ont-agent-mondo/pull/385)
- **F1**: 0.286  **Precision**: 0.167  **Recall**: 1.000  **Jaccard**: 0.167
- **Workflow run**: [25817511094](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817511094)

#### Agent PR Comment

## Summary

Fixes #9854. The `Orphanet:2477` xref (which corresponds to "Isolated megalencephaly" in Orphanet) was misattached to the general term MONDO:0016608 (megalencephaly). This PR moves the xref to the appropriate term MONDO:0017089 (isolated megalencephaly).

## Changes

### MONDO:0016608 (megalencephaly)
- Removed: `xref: Orphanet:2477 {source="MONDO:equivalentTo"}`
- Added `IAO:0000233` link to issue #9854

### MONDO:0017089 (isolated megalencephaly)
- Added: `xref: Orphanet:2477 {source="MONDO:equivalentTo"}`
- Added `IAO:0000233` link to issue #9854

The Orphanet:268920 xref already on MONDO:0017089 is retained as `MONDO:equivalentObsolete` (the older obsolete Orphanet ID), and Orphanet:2477 is now the current `MONDO:equivalentTo` for this term.

## Notes on scope

I took the conservative interpretation of the request: only moving the direct `xref: Orphanet:2477` line. Some other metadata on MONDO:0016608 still references `Orphanet:2477` in source qualifiers (e.g., the `orphanet`/`ordo_disorder` subsets and source attributions on `ICD10CM:Q04.5`, `icd11.foundation:368780653`, `MedDRA:10050183` xrefs). Since the user's request focused specifically on the xref, and reassigning cross-ontology mappings (ICD/MedDRA) requires separate validation that those mappings are truly for isolated megalencephaly rather than general megalencephaly, those were not touched. If a follow-up to also reassign those is desired, a separate issue/PR would be appropriate.

## Validation

- [x] Both terms checked out via `obo-checkout.pl`, edited, and checked back in via `obo-checkin.pl`.
- [x] Syntax validated with `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo` (no errors).
- [x] Verified MONDO:0017089 retains its existing `Orphanet:268920` xref tagged as `MONDO:equivalentObsolete`.

## Test plan

- [ ] Reviewer to confirm the move is consistent with Orphanet's mapping (Orphanet 2477 = isolated megalencephaly).
- [ ] Optional follow-up: decide whether the subsets/source qualifiers sourced to `Orphanet:2477` on MONDO:0016608 should also be migrated.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817511094)


#### Agent Issue Comment

Thanks for reporting. The Orphanet:2477 (Isolated megalencephaly) xref has been moved from MONDO:0016608 (megalencephaly) to MONDO:0017089 (isolated megalencephaly). Changes committed in PR #<NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817511094)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..d488c97fe 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -424978,7 +424978,6 @@ xref: ICD9:742.4 {source="MONDO:relatedTo", source="MONDO:i2s"}
 xref: MedDRA:10050183 {source="Orphanet:2477", source="Orphanet:2477/e"}
 xref: MEDGEN:65141 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:D058627 {source="MONDO:equivalentTo"}
-xref: Orphanet:2477 {source="MONDO:equivalentTo"}
 xref: SCTID:9740002 {source="MONDO:equivalentTo"}
 xref: UMLS:C0221355 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:65141"}
 is_a: MONDO:0005560 {source="https://orcid.org/0000-0002-4142-7153"} ! brain disorder
@@ -424986,6 +424985,7 @@ is_a: MONDO:0021147 {source="https://orcid.org/0000-0002-4142-7153"} ! disorder
 property_value: curated_content_resource "https://www.malacards.org/card/megalencephaly" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6876" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9097" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9854" xsd:anyURI
 property_value: IAO:0000589 "megalencephaly (disease)" xsd:string
 
 [Term]
@@ -435663,12 +435663,14 @@ synonym: "nonsyndromic megalencephaly (disease)" EXACT [MONDO:patterns/isolated]
 xref: GARD:0020977 {source="MONDO:GARD"}
 xref: MEDGEN:439426 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: Orphanet:268920 {source="MONDO:equivalentObsolete"}
+xref: Orphanet:2477 {source="MONDO:equivalentTo"}
 xref: UMLS:C2720434 {source="MEDGEN:439426", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0016608 {source="MONDO:Redundant", source="Orphanet:268920"} ! megalencephaly
 is_a: MONDO:0021147 {source="MONDO:Redundant", source="Orphanet:268920", source="Orphanet:268920/inferred"} ! disorder of development or morphogenesis
 intersection_of: MONDO:0016608 ! megalencephaly
 intersection_of: has_characteristic MONDO:0021128 ! has an isolated presentation
 property_value: curated_content_resource "https://www.malacards.org/card/isolated_megalencephaly" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9854" xsd:anyURI
 
 [Term]
 id: MONDO:0017090

```

### Attempt 5: claude-haiku-4.5 / claude

- **Eval PR**: [#319](https://github.com/ai4curation/eval-ont-agent-mondo/pull/319)
- **F1**: 0.200  **Precision**: 0.111  **Recall**: 1.000  **Jaccard**: 0.111
- **Trace**: [25762279964](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25762279964)
- **Workflow run**: [25762279964](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25762279964)

#### Agent PR Comment

# Orphanet Xref Relocation for Megalencephaly Terms

#### Agent Issue Comment

# Issue #9854 Resolution

The requested xref move has been completed successfully. The Orphanet:2477 cross-reference for "Isolated megalencephaly" has been moved from the parent term MONDO:0016608 (megalencephaly) to the more specific term MONDO:0017089 (isolated megalencephaly).

**Changes committed in PR #<NN>**

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25762279964)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 8fe17dbb4..c7d8a4890 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -424978,7 +424978,6 @@ xref: ICD9:742.4 {source="MONDO:relatedTo", source="MONDO:i2s"}
 xref: MedDRA:10050183 {source="Orphanet:2477", source="Orphanet:2477/e"}
 xref: MEDGEN:65141 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:D058627 {source="MONDO:equivalentTo"}
-xref: Orphanet:2477 {source="MONDO:equivalentTo"}
 xref: SCTID:9740002 {source="MONDO:equivalentTo"}
 xref: UMLS:C0221355 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:65141"}
 is_a: MONDO:0005560 {source="https://orcid.org/0000-0002-4142-7153"} ! brain disorder
@@ -435662,6 +435661,7 @@ synonym: "isolated megalencephaly (disease)" EXACT []
 synonym: "nonsyndromic megalencephaly (disease)" EXACT [MONDO:patterns/isolated]
 xref: GARD:0020977 {source="MONDO:GARD"}
 xref: MEDGEN:439426 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
+xref: Orphanet:2477 {source="MONDO:equivalentTo"}
 xref: Orphanet:268920 {source="MONDO:equivalentObsolete"}
 xref: UMLS:C2720434 {source="MEDGEN:439426", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 is_a: MONDO:0016608 {source="MONDO:Redundant", source="Orphanet:268920"} ! megalencephaly

```
