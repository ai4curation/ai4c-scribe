# PR #10201 — MONDO:0009106 diastematomyelia

- **Ontology**: mondo
- **Repo**: monarch-initiative/mondo
- **Issue**: [#9871](https://github.com/monarch-initiative/mondo/issues/9871)
- **PR**: [#10201](https://github.com/monarch-initiative/mondo/pull/10201)
- **Author**: @MeeSiing
- **Merged**: 2026-05-04
- **task_type**: other
- **difficulty**: medium
- **scoping**: loosely_scoped
- **scope**: multi_term
- **review_outcome**: changes_requested

## Context

Issue #9871 reported that MONDO:0009106 (diastematomyelia) had an incorrect Orphanet cross-reference (Orphanet:1671 for "Split cord malformation type I" rather than the broader concept). Investigation revealed that Orphanet:573278 correctly maps to the broader concept of diastematomyelia/split cord malformation, and that subtypes (type I with osseous spur, type II with fibrous septum) should be represented.

## Changes Made

The PR evolved from a simple xref correction into a multi-term edit across 5 commits. The initial commit updated the Orphanet xref from 1671 to 573278. A proxy merge was fixed in the second commit. The third commit added 3 new subtypes (MONDO:1060220-1060222) for split cord malformation classification. The fourth and fifth commits resolved merge conflicts with master. The 59 additions and 21 deletions reflect both the xref correction and the creation of new subtype terms with definitions, synonyms, and parent axioms.

## Resolution

Moderate difficulty because the scope expanded significantly from the original request. What began as a cross-reference correction required domain knowledge about split cord malformation types to realize that subtypes were needed. The merge conflicts and multiple commits show iterative development. An agent would need to recognize when an xref discrepancy indicates a deeper modeling issue requiring new terms.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 3616a71b6a..027d104cae 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -210460,35 +210460,37 @@ subset: gard_rare {source="GARD:0001851", source="MONDO:GARD"}
 subset: ncit {source="NCIT:C98913"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: omim {source="OMIM:222500"}
-subset: ordo_disorder {source="Orphanet:1671"}
+subset: ordo_disorder {source="Orphanet:573278"}
 subset: ordo_morphological_anomaly {source="Orphanet:1671"}
-subset: orphanet {source="Orphanet:1671"}
-subset: orphanet_rare {source="Orphanet:1671"}
+subset: orphanet {source="Orphanet:573278"}
+subset: orphanet_rare {source="Orphanet:573278"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:1671]
+synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:573278]
 synonym: "Dimyelia" RELATED [GARD:0001851]
 synonym: "diplomyelia" RELATED [GARD:0001851]
 synonym: "Pseudodiplomyelia" RELATED [GARD:0001851]
-synonym: "SCM type 1" EXACT [Orphanet:1671]
-synonym: "split cord malformation" RELATED [GARD:0001851]
-synonym: "split cord malformation type 1" EXACT [Orphanet:1671]
-synonym: "split spinal cord malformation" RELATED [GARD:0001851]
-synonym: "SSCM" RELATED ABBREVIATION [GARD:0001851]
+synonym: "SCM type 1" NARROW ABBREVIATION [Orphanet:1671]
+synonym: "split cord malformation" EXACT [GARD:0001851, Orphanet:573278]
+synonym: "split cord malformation type 1" NARROW [Orphanet:1671]
+synonym: "split spinal cord malformation" EXACT [GARD:0001851, Orphanet:573278]
+synonym: "SSCM" EXACT ABBREVIATION [GARD:0001851]
 xref: GARD:0001851 {source="MONDO:GARD"}
-xref: ICD10CM:Q06.2 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e", source="Orphanet:1671/specific"}
+xref: ICD10CM:Q06.2 {source="Orphanet:573278", source="MONDO:equivalentTo"}
 xref: icd11.foundation:2070601288 {source="MONDO:equivalentTo"}
 xref: ICD9:742.51 {source="MONDO:equivalentTo", source="MONDO:i2s"}
-xref: MedDRA:10012750 {source="Orphanet:1671", source="Orphanet:1671/e"}
+xref: MedDRA:10012750 {source="Orphanet:573278"}
 xref: MEDGEN:3801 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: NCIT:C98913 {source="MONDO:equivalentTo"}
-xref: OMIM:222500 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e"}
-xref: Orphanet:1671 {source="MONDO:equivalentTo", source="OMIM:222500"}
+xref: OMIM:222500 {source="MONDO:equivalentTo"}
+xref: Orphanet:573278 {source="MONDO:equivalentTo"}
 xref: SCTID:49351009 {source="MONDO:equivalentTo"}
 xref: UMLS:C0011999 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:3801"}
 is_a: MONDO:0002320 {source="NCIT:C98913"} ! congenital nervous system disorder
 is_a: MONDO:0018075 {source="MONDO:0017085-obsoleted", source="https://github.com/monarch-initiative/mondo/pull/2571/"} ! neural tube defect
 property_value: curated_content_resource "https://www.malacards.org/card/diastematomyelia" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: curated_content_resource "https://www.malacards.org/card/split_cord_malformation" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
 
 [Term]
 id: MONDO:0009107
@@ -558641,23 +558643,21 @@ property_value: curated_content_resource "https://www.malacards.org/card/pheochr
 [Term]
 id: MONDO:0035541
 name: obsolete split cord malformation type II
-subset: ordo_disorder {source="Orphanet:573253"}
-xref: Orphanet:573253 {source="MONDO:obsoleteEquivalent"}
-property_value: curated_content_resource "https://www.malacards.org/card/split_cord_malformation_type_ii" xsd:anyURI {source="MONDO:MalaCards"}
-property_value: IAO:0000231 OMO:0001000 {source="MONDO:excludePhenotype"}
+property_value: IAO:0000231 MONDO:TermsMerged
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4776" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/7693" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
 is_obsolete: true
+replaced_by: MONDO:1060221
 
 [Term]
 id: MONDO:0035542
 name: obsolete split cord malformation
-subset: ordo_group_of_disorders {source="Orphanet:573278"}
-xref: Orphanet:573278 {source="MONDO:obsoleteEquivalent"}
-property_value: curated_content_resource "https://www.malacards.org/card/split_cord_malformation" xsd:anyURI {source="MONDO:MalaCards"}
-property_value: IAO:0000231 OMO:0001000 {source="MONDO:excludePhenotype"}
+property_value: IAO:0000231 MONDO:TermsMerged
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4776" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
 is_obsolete: true
+replaced_by: MONDO:0009106
 
 [Term]
 id: MONDO:0035547
@@ -659109,6 +659109,44 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9956" xsd:anyURI
 
+[Term]
+id: MONDO:1060220
+name: split cord malformation type I
+def: "A rare subtype of split cord malformation characterized by each hemicord contained in its own dural sac, typically with an intervening bony or cartilaginous septum." [https://orcid.org/0000-0002-7638-4659, Orphanet:1671]
+synonym: "SCM type 1" EXACT ABBREVIATION [Orphanet:1671]
+synonym: "SCM type I" EXACT ABBREVIATION [Orphanet:1671]
+synonym: "split cord malformation type 1" EXACT [Orphanet:1671]
+xref: Orphanet:1671 {source="MONDO:equivalentTo"}
+is_a: MONDO:0009106 {source="Orphanet:1671"} ! diastematomyelia
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
+
+[Term]
+id: MONDO:1060221
+name: split cord malformation type II
+def: "A rare subtype of split cord malformation characterized by both hemicords included in the same single dural sac. An intradural intervening mesenchymal septum may be present." [https://orcid.org/0000-0002-7638-4659, Orphanet:573253]
+synonym: "diplomyelia" EXACT [Orphanet:573253]
+synonym: "SCM type 2" EXACT ABBREVIATION [Orphanet:573253]
+synonym: "SCM type II" EXACT ABBREVIATION [Orphanet:573253]
+synonym: "split cord malformation type 2" EXACT [Orphanet:573253]
+xref: Orphanet:573253 {source="MONDO:equivalentTo"}
+is_a: MONDO:0009106 {source="Orphanet:573253"} ! diastematomyelia
+property_value: curated_content_resource "https://www.malacards.org/card/split_cord_malformation_type_ii" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
+
+[Term]
+id: MONDO:1060222
+name: split cord malformation, composite type
+def: "A rare intermediate form of split cord malformation characterized by both hemichords encapsulated in a single dural sac with presence of an incomplete ventral or dorsal bony spur." [https://orcid.org/0000-0002-7638-4659, Orphanet:633076, PMID:31557552]
+synonym: "split cord malformation type 1.5" EXACT [Orphanet:633076]
+synonym: "split cord malformation, intermediate type" EXACT [Orphanet:633076]
+synonym: "split cord malformation, mixed type" EXACT [Orphanet:633076]
+xref: Orphanet:633076 {source="MONDO:equivalentTo"}
+is_a: MONDO:0009106 {source="Orphanet:633076"} ! diastematomyelia
+property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-7638-4659
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
+
 [Term]
 id: MONDO:1060223
 name: RNU12-related minor spliceopathy disorder

```

## Agent Attempts (6)

### Attempt 1: kimi-k2.6 / opencode

- **Eval PR**: [#249](https://github.com/ai4curation/eval-ont-agent-mondo/pull/249)
- **F1**: 0.450  **Precision**: 0.321  **Recall**: 0.750  **Jaccard**: 0.290
- **Trace**: [25755499822](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25755499822)
- **Workflow run**: [25755499822](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755499822)

#### Agent PR Comment

## Summary

This PR addresses issue #9871, which reported that the Orphanet xref on **MONDO:0009106 diastematomyelia** was mapped to the overly narrow concept `Orphanet:1671` (Split cord malformation type I) instead of the broader concept `Orphanet:573278` (Split cord malformation). Per the issue reporter, SNOMED CT 445308004 treats "split cord malformation" and "diastematomyelia" as synonyms.

## Changes made

### MONDO:0009106 (diastematomyelia)
- **Replaced Orphanet xref:** `Orphanet:1671` {source="MONDO:equivalentTo"} → `Orphanet:573278` {source="MONDO:equivalentTo"}
- **Updated source attributions** on subsets, synonyms, and cross-references from `Orphanet:1671` to `Orphanet:573278`
- **Removed overly narrow synonyms** sourced from `Orphanet:1671`:
  - "SCM type 1"
  - "split cord malformation type 1"
- **Upgraded synonym status:** "split cord malformation" changed from RELATED to EXACT, with `Orphanet:573278` added as a source
- **Added term tracker:** `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871"`

### MONDO:0035542 (obsolete split cord malformation)
- **Added `replaced_by: MONDO:0009106`** to explicitly link the obsolete term to diastematomyelia
- **Added term tracker** for issue #9871

## Validation performed
- [x] Checked out terms for editing
- [x] Applied edits in isolated term files
- [x] Checked in terms to `src/ontology/mondo-edit.obo`
- [x] Ran `make NORM` to normalize serialization
- [x] Validated OBO syntax with `robot convert` (no errors)
- [x] Verified `Orphanet:1671` no longer appears in `mondo-edit.obo`
- [x] Verified updated stanzas present in normalized file

## Rationale

The previous mapping to `Orphanet:1671` incorrectly equated diastematomyelia with only Split cord malformation type I, when the concept in MONDO represents the broader condition. MONDO already had an obsolete class (MONDO:0035542) for "split cord malformation" that mapped to `Orphanet:573278`. By aligning the active diastematomyelia term with the broader Orphanet concept and formally linking the obsolete term as its replacement, we unify these concepts and correct the overly narrow mapping.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755499822)


#### Agent Issue Comment

Hi @kanems,

Thank you for reporting this mapping discrepancy. The fix has been committed in PR #<NN>.

Changes applied:
- Replaced the too-narrow Orphanet xref on **MONDO:0009106 diastematomyelia** from `Orphanet:1671` (Split cord malformation type I) to `Orphanet:573278` (Split cord malformation).
- Removed the overly specific synonyms "SCM type 1" and "split cord malformation type 1" from diastematomyelia.
- Upgraded "split cord malformation" from a RELATED to an EXACT synonym, in line with the SNOMED CT synonymy you noted.
- Added `replaced_by: MONDO:0009106` to the obsolete **MONDO:0035542 split cord malformation** term so that it now clearly points to diastematomyelia.

Please let us know if anything looks off.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755499822)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 3616a71b6..1de037f1a 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -210460,35 +210460,34 @@ subset: gard_rare {source="GARD:0001851", source="MONDO:GARD"}
 subset: ncit {source="NCIT:C98913"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: omim {source="OMIM:222500"}
-subset: ordo_disorder {source="Orphanet:1671"}
-subset: ordo_morphological_anomaly {source="Orphanet:1671"}
-subset: orphanet {source="Orphanet:1671"}
-subset: orphanet_rare {source="Orphanet:1671"}
+subset: ordo_disorder {source="Orphanet:573278"}
+subset: ordo_morphological_anomaly {source="Orphanet:573278"}
+subset: orphanet {source="Orphanet:573278"}
+subset: orphanet_rare {source="Orphanet:573278"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:1671]
+synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:573278]
 synonym: "Dimyelia" RELATED [GARD:0001851]
 synonym: "diplomyelia" RELATED [GARD:0001851]
 synonym: "Pseudodiplomyelia" RELATED [GARD:0001851]
-synonym: "SCM type 1" EXACT [Orphanet:1671]
-synonym: "split cord malformation" RELATED [GARD:0001851]
-synonym: "split cord malformation type 1" EXACT [Orphanet:1671]
+synonym: "split cord malformation" EXACT [GARD:0001851, Orphanet:573278]
 synonym: "split spinal cord malformation" RELATED [GARD:0001851]
 synonym: "SSCM" RELATED ABBREVIATION [GARD:0001851]
 xref: GARD:0001851 {source="MONDO:GARD"}
-xref: ICD10CM:Q06.2 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e", source="Orphanet:1671/specific"}
+xref: ICD10CM:Q06.2 {source="Orphanet:573278", source="MONDO:equivalentTo", source="Orphanet:573278/specific", source="Orphanet:573278/e"}
 xref: icd11.foundation:2070601288 {source="MONDO:equivalentTo"}
 xref: ICD9:742.51 {source="MONDO:equivalentTo", source="MONDO:i2s"}
-xref: MedDRA:10012750 {source="Orphanet:1671", source="Orphanet:1671/e"}
+xref: MedDRA:10012750 {source="Orphanet:573278", source="Orphanet:573278/e"}
 xref: MEDGEN:3801 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: NCIT:C98913 {source="MONDO:equivalentTo"}
-xref: OMIM:222500 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e"}
-xref: Orphanet:1671 {source="MONDO:equivalentTo", source="OMIM:222500"}
+xref: OMIM:222500 {source="Orphanet:573278", source="MONDO:equivalentTo", source="Orphanet:573278/e"}
+xref: Orphanet:573278 {source="MONDO:equivalentTo", source="OMIM:222500"}
 xref: SCTID:49351009 {source="MONDO:equivalentTo"}
 xref: UMLS:C0011999 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:3801"}
 is_a: MONDO:0002320 {source="NCIT:C98913"} ! congenital nervous system disorder
 is_a: MONDO:0018075 {source="MONDO:0017085-obsoleted", source="https://github.com/monarch-initiative/mondo/pull/2571/"} ! neural tube defect
 property_value: curated_content_resource "https://www.malacards.org/card/diastematomyelia" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
 
 [Term]
 id: MONDO:0009107
@@ -558657,7 +558656,9 @@ xref: Orphanet:573278 {source="MONDO:obsoleteEquivalent"}
 property_value: curated_content_resource "https://www.malacards.org/card/split_cord_malformation" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000231 OMO:0001000 {source="MONDO:excludePhenotype"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4776" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
 is_obsolete: true
+replaced_by: MONDO:0009106
 
 [Term]
 id: MONDO:0035547

```

### Attempt 2: claude-opus-4.7 / claude

- **Eval PR**: [#391](https://github.com/ai4curation/eval-ont-agent-mondo/pull/391)
- **F1**: 0.405  **Precision**: 0.286  **Recall**: 0.696  **Jaccard**: 0.254
- **Trace**: [25818243887](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25818243887)
- **Workflow run**: [25818243887](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25818243887)

#### Agent PR Comment

## Summary

Addresses issue #9871: the Orphanet cross-reference on MONDO:0009106 (diastematomyelia) was pointing to Orphanet:1671 (Split cord malformation type I), which is a narrower concept than diastematomyelia. The issue reporter pointed out that per SNOMED CT 445308004, "split cord malformation" and "diastematomyelia" are synonyms, and that Orphanet:573278 (Split cord malformation) is the appropriate equivalent concept.

## Changes to MONDO:0009106 diastematomyelia

- `xref: Orphanet:1671` → `xref: Orphanet:573278` (the broader, properly equivalent Orphanet term)
- All `source="Orphanet:1671"` qualifiers (on subsets and xrefs) updated to `source="Orphanet:573278"`.
- Synonym xref list for "diastematomyelia" EXACT updated from `Orphanet:1671` to `Orphanet:573278`.
- Removed two synonyms that referred to the narrower SCM type 1 concept and were only present because of the previous incorrect equivalent mapping:
  - `synonym: "SCM type 1" EXACT [Orphanet:1671]`
  - `synonym: "split cord malformation type 1" EXACT [Orphanet:1671]`
- Upgraded `synonym: "split cord malformation"` from RELATED to EXACT, and added `Orphanet:573278` and `SCTID:445308004` to the synonym citation list. SCTID:445308004 is the SNOMED CT concept the reporter referenced as evidence of the synonym relationship.
- Added a `term_tracker_item` (`IAO:0000233`) pointing to issue #9871.

## Rationale

- The reporter correctly identified that Orphanet:1671 (SCM type I) is a narrower concept than diastematomyelia, while Orphanet:573278 (Split cord malformation) is the correctly scoped equivalent — supported by SNOMED CT 445308004, which has "split cord malformation" and "diastematomyelia" as synonyms.
- Source-qualifier updates were applied across the term to keep provenance internally consistent with the new equivalent Orphanet ID.
- The narrower SCM type 1 / type 2 subtypes were not added as separate MONDO terms; the reporter noted these "may or may not be in scope for Mondo," so I left that decision for editor follow-up.
- No `is_a` axioms were modified; logical parents are unaffected.

## Checklist

- [x] Read the issue and inspected MONDO:0009106 stanza
- [x] Verified no other stanzas in `mondo-edit.obo` still reference `Orphanet:1671` after the edit
- [x] Used `obo-checkout.pl` / `obo-checkin.pl` to make edits via the terms/ folder
- [x] Logical axioms (is_a / intersection_of) untouched — only mapping metadata changed
- [ ] `make NORM` skipped: Docker (ODK image) not available in this environment. Maintainers should re-run normalization before final merge.

## Test plan

- [ ] Confirm `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o /tmp/mondo-edit.TMP.obo` succeeds in CI.
- [ ] Confirm reasoner / QC pipeline reports no new unsatisfiable classes or mapping errors on MONDO:0009106.
- [ ] Spot-check downstream consumers (sssom mappings, ROBOT reports) for the Orphanet:1671 → Orphanet:573278 swap.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25818243887)


#### Agent Issue Comment

Thanks for the report. Changes committed in PR #<NN>.

Summary of changes to MONDO:0009106 (diastematomyelia):
- Replaced `xref: Orphanet:1671` (Split cord malformation type I — too narrow) with `xref: Orphanet:573278` (Split cord malformation).
- Updated subset, synonym, and cross-reference source attributions from Orphanet:1671 to Orphanet:573278.
- Removed the narrower synonyms "SCM type 1" and "split cord malformation type 1" (these refer to a narrower subtype that is out of scope here).
- Added "split cord malformation" as an EXACT synonym (per SNOMED CT 445308004), citing Orphanet:573278 and SCTID:445308004.
- Added `term_tracker_item` pointing to this issue.

SCM type 1 and type 2 as narrower subtypes were not added as separate terms; happy to revisit if there is community demand for them.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25818243887)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 3616a71b6..bab69383a 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -210460,35 +210460,34 @@ subset: gard_rare {source="GARD:0001851", source="MONDO:GARD"}
 subset: ncit {source="NCIT:C98913"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: omim {source="OMIM:222500"}
-subset: ordo_disorder {source="Orphanet:1671"}
-subset: ordo_morphological_anomaly {source="Orphanet:1671"}
-subset: orphanet {source="Orphanet:1671"}
-subset: orphanet_rare {source="Orphanet:1671"}
+subset: ordo_disorder {source="Orphanet:573278"}
+subset: ordo_morphological_anomaly {source="Orphanet:573278"}
+subset: orphanet {source="Orphanet:573278"}
+subset: orphanet_rare {source="Orphanet:573278"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:1671]
+synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:573278]
 synonym: "Dimyelia" RELATED [GARD:0001851]
 synonym: "diplomyelia" RELATED [GARD:0001851]
 synonym: "Pseudodiplomyelia" RELATED [GARD:0001851]
-synonym: "SCM type 1" EXACT [Orphanet:1671]
-synonym: "split cord malformation" RELATED [GARD:0001851]
-synonym: "split cord malformation type 1" EXACT [Orphanet:1671]
+synonym: "split cord malformation" EXACT [GARD:0001851, Orphanet:573278, SCTID:445308004]
 synonym: "split spinal cord malformation" RELATED [GARD:0001851]
 synonym: "SSCM" RELATED ABBREVIATION [GARD:0001851]
 xref: GARD:0001851 {source="MONDO:GARD"}
-xref: ICD10CM:Q06.2 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e", source="Orphanet:1671/specific"}
+xref: ICD10CM:Q06.2 {source="Orphanet:573278", source="MONDO:equivalentTo", source="Orphanet:573278/e", source="Orphanet:573278/specific"}
 xref: icd11.foundation:2070601288 {source="MONDO:equivalentTo"}
 xref: ICD9:742.51 {source="MONDO:equivalentTo", source="MONDO:i2s"}
-xref: MedDRA:10012750 {source="Orphanet:1671", source="Orphanet:1671/e"}
+xref: MedDRA:10012750 {source="Orphanet:573278", source="Orphanet:573278/e"}
 xref: MEDGEN:3801 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: NCIT:C98913 {source="MONDO:equivalentTo"}
-xref: OMIM:222500 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e"}
-xref: Orphanet:1671 {source="MONDO:equivalentTo", source="OMIM:222500"}
+xref: OMIM:222500 {source="Orphanet:573278", source="MONDO:equivalentTo", source="Orphanet:573278/e"}
+xref: Orphanet:573278 {source="MONDO:equivalentTo", source="OMIM:222500"}
 xref: SCTID:49351009 {source="MONDO:equivalentTo"}
 xref: UMLS:C0011999 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:3801"}
 is_a: MONDO:0002320 {source="NCIT:C98913"} ! congenital nervous system disorder
 is_a: MONDO:0018075 {source="MONDO:0017085-obsoleted", source="https://github.com/monarch-initiative/mondo/pull/2571/"} ! neural tube defect
 property_value: curated_content_resource "https://www.malacards.org/card/diastematomyelia" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
 
 [Term]
 id: MONDO:0009107

```

### Attempt 3: claude-sonnet-4.5 / claude

- **Eval PR**: [#432](https://github.com/ai4curation/eval-ont-agent-mondo/pull/432)
- **F1**: 0.385  **Precision**: 0.268  **Recall**: 0.682  **Jaccard**: 0.238
- **Trace**: [25867686151](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25867686151)
- **Workflow run**: [25867686151](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867686151)

#### Agent PR Comment

## Summary

Updated the Orphanet cross-reference for MONDO:0009106 (diastematomyelia) from Orphanet:1671 (Split cord malformation type I) to Orphanet:573278 (Split cord malformation).

#### Agent Issue Comment

The Orphanet cross-reference for MONDO:0009106 (diastematomyelia) has been updated from Orphanet:1671 (Split cord malformation type I) to Orphanet:573278 (Split cord malformation) as requested. The broader concept is more appropriate since diastematomyelia and split cord malformation are synonymous per SNOMED CT 445308004.

Changes committed in PR #&lt;NN&gt;

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867686151)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 3616a71b6..648a86e88 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -210460,30 +210460,30 @@ subset: gard_rare {source="GARD:0001851", source="MONDO:GARD"}
 subset: ncit {source="NCIT:C98913"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: omim {source="OMIM:222500"}
-subset: ordo_disorder {source="Orphanet:1671"}
-subset: ordo_morphological_anomaly {source="Orphanet:1671"}
-subset: orphanet {source="Orphanet:1671"}
-subset: orphanet_rare {source="Orphanet:1671"}
+subset: ordo_disorder {source="Orphanet:573278"}
+subset: ordo_morphological_anomaly {source="Orphanet:573278"}
+subset: orphanet {source="Orphanet:573278"}
+subset: orphanet_rare {source="Orphanet:573278"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:1671]
+synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:573278]
 synonym: "Dimyelia" RELATED [GARD:0001851]
 synonym: "diplomyelia" RELATED [GARD:0001851]
 synonym: "Pseudodiplomyelia" RELATED [GARD:0001851]
-synonym: "SCM type 1" EXACT [Orphanet:1671]
+synonym: "SCM type 1" EXACT [Orphanet:573278]
 synonym: "split cord malformation" RELATED [GARD:0001851]
-synonym: "split cord malformation type 1" EXACT [Orphanet:1671]
+synonym: "split cord malformation type 1" EXACT [Orphanet:573278]
 synonym: "split spinal cord malformation" RELATED [GARD:0001851]
 synonym: "SSCM" RELATED ABBREVIATION [GARD:0001851]
 xref: GARD:0001851 {source="MONDO:GARD"}
-xref: ICD10CM:Q06.2 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e", source="Orphanet:1671/specific"}
+xref: ICD10CM:Q06.2 {source="Orphanet:573278", source="MONDO:equivalentTo", source="Orphanet:573278/e", source="Orphanet:573278/specific"}
 xref: icd11.foundation:2070601288 {source="MONDO:equivalentTo"}
 xref: ICD9:742.51 {source="MONDO:equivalentTo", source="MONDO:i2s"}
-xref: MedDRA:10012750 {source="Orphanet:1671", source="Orphanet:1671/e"}
+xref: MedDRA:10012750 {source="Orphanet:573278", source="Orphanet:573278/e"}
 xref: MEDGEN:3801 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: NCIT:C98913 {source="MONDO:equivalentTo"}
-xref: OMIM:222500 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e"}
-xref: Orphanet:1671 {source="MONDO:equivalentTo", source="OMIM:222500"}
+xref: OMIM:222500 {source="Orphanet:573278", source="MONDO:equivalentTo", source="Orphanet:573278/e"}
+xref: Orphanet:573278 {source="MONDO:equivalentTo", source="OMIM:222500"}
 xref: SCTID:49351009 {source="MONDO:equivalentTo"}
 xref: UMLS:C0011999 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:3801"}
 is_a: MONDO:0002320 {source="NCIT:C98913"} ! congenital nervous system disorder

```

### Attempt 4: claude-sonnet-4.5 / copilot

- **Eval PR**: [#524](https://github.com/ai4curation/eval-ont-agent-mondo/pull/524)
- **F1**: 0.239  **Precision**: 0.143  **Recall**: 0.727  **Jaccard**: 0.136

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 3616a71b6..fff200609 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -210460,19 +210460,13 @@ subset: gard_rare {source="GARD:0001851", source="MONDO:GARD"}
 subset: ncit {source="NCIT:C98913"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: omim {source="OMIM:222500"}
-subset: ordo_disorder {source="Orphanet:1671"}
-subset: ordo_morphological_anomaly {source="Orphanet:1671"}
-subset: orphanet {source="Orphanet:1671"}
-subset: orphanet_rare {source="Orphanet:1671"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:1671]
+synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500]
 synonym: "Dimyelia" RELATED [GARD:0001851]
 synonym: "diplomyelia" RELATED [GARD:0001851]
 synonym: "Pseudodiplomyelia" RELATED [GARD:0001851]
-synonym: "SCM type 1" EXACT [Orphanet:1671]
 synonym: "split cord malformation" RELATED [GARD:0001851]
-synonym: "split cord malformation type 1" EXACT [Orphanet:1671]
 synonym: "split spinal cord malformation" RELATED [GARD:0001851]
 synonym: "SSCM" RELATED ABBREVIATION [GARD:0001851]
 xref: GARD:0001851 {source="MONDO:GARD"}
@@ -210483,12 +210477,13 @@ xref: MedDRA:10012750 {source="Orphanet:1671", source="Orphanet:1671/e"}
 xref: MEDGEN:3801 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: NCIT:C98913 {source="MONDO:equivalentTo"}
 xref: OMIM:222500 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e"}
-xref: Orphanet:1671 {source="MONDO:equivalentTo", source="OMIM:222500"}
+xref: Orphanet:1671 {source="MONDO:narrowMatch", source="OMIM:222500"}
 xref: SCTID:49351009 {source="MONDO:equivalentTo"}
 xref: UMLS:C0011999 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:3801"}
 is_a: MONDO:0002320 {source="NCIT:C98913"} ! congenital nervous system disorder
 is_a: MONDO:0018075 {source="MONDO:0017085-obsoleted", source="https://github.com/monarch-initiative/mondo/pull/2571/"} ! neural tube defect
 property_value: curated_content_resource "https://www.malacards.org/card/diastematomyelia" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
 
 [Term]
 id: MONDO:0009107

```

### Attempt 5: claude-sonnet-4.5 / copilot

- **Eval PR**: [#489](https://github.com/ai4curation/eval-ont-agent-mondo/pull/489)
- **F1**: 0.239  **Precision**: 0.143  **Recall**: 0.727  **Jaccard**: 0.136

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 3616a71b6..fff200609 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -210460,19 +210460,13 @@ subset: gard_rare {source="GARD:0001851", source="MONDO:GARD"}
 subset: ncit {source="NCIT:C98913"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: omim {source="OMIM:222500"}
-subset: ordo_disorder {source="Orphanet:1671"}
-subset: ordo_morphological_anomaly {source="Orphanet:1671"}
-subset: orphanet {source="Orphanet:1671"}
-subset: orphanet_rare {source="Orphanet:1671"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:1671]
+synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500]
 synonym: "Dimyelia" RELATED [GARD:0001851]
 synonym: "diplomyelia" RELATED [GARD:0001851]
 synonym: "Pseudodiplomyelia" RELATED [GARD:0001851]
-synonym: "SCM type 1" EXACT [Orphanet:1671]
 synonym: "split cord malformation" RELATED [GARD:0001851]
-synonym: "split cord malformation type 1" EXACT [Orphanet:1671]
 synonym: "split spinal cord malformation" RELATED [GARD:0001851]
 synonym: "SSCM" RELATED ABBREVIATION [GARD:0001851]
 xref: GARD:0001851 {source="MONDO:GARD"}
@@ -210483,12 +210477,13 @@ xref: MedDRA:10012750 {source="Orphanet:1671", source="Orphanet:1671/e"}
 xref: MEDGEN:3801 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: NCIT:C98913 {source="MONDO:equivalentTo"}
 xref: OMIM:222500 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e"}
-xref: Orphanet:1671 {source="MONDO:equivalentTo", source="OMIM:222500"}
+xref: Orphanet:1671 {source="MONDO:narrowMatch", source="OMIM:222500"}
 xref: SCTID:49351009 {source="MONDO:equivalentTo"}
 xref: UMLS:C0011999 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:3801"}
 is_a: MONDO:0002320 {source="NCIT:C98913"} ! congenital nervous system disorder
 is_a: MONDO:0018075 {source="MONDO:0017085-obsoleted", source="https://github.com/monarch-initiative/mondo/pull/2571/"} ! neural tube defect
 property_value: curated_content_resource "https://www.malacards.org/card/diastematomyelia" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9871" xsd:anyURI
 
 [Term]
 id: MONDO:0009107

```

### Attempt 6: claude-haiku-4.5 / claude

- **Eval PR**: [#307](https://github.com/ai4curation/eval-ont-agent-mondo/pull/307)
- **F1**: 0.069  **Precision**: 0.036  **Recall**: 1.000  **Jaccard**: 0.036
- **Trace**: [25762186533](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25762186533)
- **Workflow run**: [25762186533](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25762186533)

#### Agent PR Comment

# PR: Update MONDO:0009106 diastematomyelia xref

#### Agent Issue Comment

# Issue #9871: MONDO:0009106 diastematomyelia

Changes committed in PR #<NN>

The xref for MONDO:0009106 diastematomyelia has been updated from Orphanet:1671 (Split cord malformation type I) to Orphanet:573278 (Split cord malformation) to use the broader, more appropriate mapping. This change aligns with the recommendation in the issue and reflects that diastematomyelia encompasses the full spectrum of split cord malformations, not just type I.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25762186533)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 3616a71b6..ccaea8618 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -210483,7 +210483,7 @@ xref: MedDRA:10012750 {source="Orphanet:1671", source="Orphanet:1671/e"}
 xref: MEDGEN:3801 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: NCIT:C98913 {source="MONDO:equivalentTo"}
 xref: OMIM:222500 {source="Orphanet:1671", source="MONDO:equivalentTo", source="Orphanet:1671/e"}
-xref: Orphanet:1671 {source="MONDO:equivalentTo", source="OMIM:222500"}
+xref: Orphanet:573278 {source="MONDO:equivalentTo"}
 xref: SCTID:49351009 {source="MONDO:equivalentTo"}
 xref: UMLS:C0011999 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:3801"}
 is_a: MONDO:0002320 {source="NCIT:C98913"} ! congenital nervous system disorder

```
