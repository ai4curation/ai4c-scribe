---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 10030
pr_number: 10117
issue_title: Incorrect synonyms for MONDO_0001628
pr_author: matentzn
pr_merged_at: '2026-04-02'
task_type: bulk_edit
difficulty: hard
scoping: loosely_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 8
generated_at: '2026-05-15'
scoping_notes: Bulk removal of synonyms across many terms in the ontology.
domain_area: quality-control
best_f1: 0.003
best_model: claude-sonnet-4.5
---

# PR #10117 — Incorrect synonyms for MONDO_0001628

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #10030](https://github.com/monarch-initiative/mondo/issues/10030) | [PR #10117](https://github.com/monarch-initiative/mondo/pull/10117) | @matentzn | merged 2026-04-02

`bulk_edit` `hard` `loosely_scoped` `approved_first_time`

## Context

An issue was filed reporting incorrect synonyms for MONDO:0001628, which led to a broader investigation revealing that many Mondo terms had synonyms with uncertain or incorrect semantics. These problematic synonyms had been imported from external sources without adequate validation and could mislead downstream consumers of the ontology.

The lead developer (matentzn) performed a systematic review and bulk removal of synonyms that could not be confidently classified as exact, related, broad, or narrow.

## Changes Made

Removed 5,103 lines from `src/ontology/mondo-edit.obo` with zero additions, representing a pure cleanup operation. This is one of the largest single-PR changes in recent Mondo history, affecting synonyms across potentially hundreds of terms. The removal was done programmatically after careful analysis of which synonyms had uncertain provenance or semantics.

## Resolution

Hard difficulty due to the scale and risk involved. Removing over 5,000 synonym lines requires high confidence that none of them are valid. The curator needed to develop criteria for identifying problematic synonyms, validate the removal set, and ensure no valuable synonyms were lost. An agent would struggle with this task as it requires both programmatic analysis and expert judgment about synonym quality.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 5f0045ca84..c06f1160a7 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -128,7 +128,6 @@ synonym: "adrenal cortical insufficiency" EXACT [DOID:10493, NCIT:C26691]
 synonym: "adrenal gland insufficiency" EXACT [icd11.foundation:733056203, NCIT:C26691]
 synonym: "adrenal insufficiency" EXACT [icd11.foundation:733056203, NCIT:C26691]
 synonym: "adrenocortical insufficiency" EXACT [icd11.foundation:733056203, NCIT:C26691]
-synonym: "corticoadrenal insufficiency" EXACT [DOID:10493]
 synonym: "hypoadrenalism" RELATED [GARD:0006722]
 synonym: "hypocortisolemia" EXACT [NCIT:C26691]
 synonym: "hypocortisolism" EXACT [NCIT:C26691]
@@ -385,7 +384,6 @@ subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "ADNFLE" EXACT ABBREVIATION [Orphanet:98784]
 synonym: "autosomal dominant nocturnal frontal lobe epilepsy" EXACT [Orphanet:98784]
-synonym: "ENFL" EXACT ABBREVIATION [DOID:0060681]
 synonym: "epilepsy, nocturnal frontal lobe, familial" EXACT []
 synonym: "familial sleep-related hyperkinetic epilepsy" EXACT [https://www.epilepsydiagnosis.org/syndrome/adnfle-overview.html, PMID:28027860]
 synonym: "familial sleep-related hypermotor epilepsy" EXACT [PMID:27164717, PMID:28027860] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}
@@ -578,9 +576,7 @@ subset: rare
 synonym: "congenital IGHD" EXACT [DOID:0060870, Orphanet:631]
 synonym: "congenital isolated GH deficiency" EXACT [DOID:0060870, Orphanet:631]
 synonym: "congenital isolated growth hormone deficiency" EXACT [DOID:0060870, icd11.foundation:936501166, Orphanet:631]
-synonym: "familial isolated growth hormone deficiency" EXACT [DOID:0060870]
 synonym: "ICGHD" EXACT ABBREVIATION [https://orcid.org/0000-0002-6601-2165]
-synonym: "IGHD" EXACT ABBREVIATION [DOID:0060870]
 synonym: "isolated growth hormone deficiency" EXACT [DOID:0060870, OMIMPS:262400]
 synonym: "non-acquired isolated growth hormone deficiency" RELATED []
 xref: DOID:0060870 {source="MONDO:equivalentTo"}
@@ -1900,7 +1896,6 @@ subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "cerebroocular dysgenesis" RELATED [GARD:0002599]
 synonym: "cerebroocular dysplasia muscular dystrophy syndrome" RELATED [GARD:0002599]
-synonym: "cerebroocular dysplasia-muscular dystrophy syndrome" EXACT [DOID:0050560]
 synonym: "Chemke syndrome" RELATED [GARD:0002599]
 synonym: "hard +/- E syndrome" RELATED [GARD:0002599]
 synonym: "hard syndrome" EXACT [DOID:0050560, Orphanet:899]
@@ -2180,7 +2175,6 @@ subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "11-alpha beta-hydroxysteroid dehydrogenase type I deficiency of" RELATED [GARD:0009882]
 synonym: "11-beta-hydroxysteroid dehydrogenase deficiency type 1" EXACT [Orphanet:168588]
-synonym: "CORTRD" EXACT ABBREVIATION [DOID:0090139]
 synonym: "deficiency of (R)-20-hydroxysteroid dehydrogenase" EXACT [https://orcid.org/0000-0002-6601-2165]
 synonym: "deficiency of cortisone reductase" EXACT [https://orcid.org/0000-0002-6601-2165]
 synonym: "HSD 11B1 deficiency" NARROW [GARD:0009882]
@@ -2563,7 +2557,6 @@ subset: doid_rare {source="DOID:0050026"}
 subset: gard_rare {source="GARD:0000072", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD", source="NORD:1254"}
 subset: rare
-synonym: "ehrlichiosis chafeensis" RELATED [DOID:0050026]
 synonym: "HME" RELATED ABBREVIATION [GARD:0000072]
 synonym: "Human ehrlichial infection, human monocytic type" RELATED [GARD:0000072]
 synonym: "human ehrlichiosis caused by Ehrlichia chaffeensis" RELATED []
@@ -2653,7 +2646,6 @@ def: "An infectious disease caused by infection with rickettsia conorii subsp. i
 subset: doid {source="DOID:0050043"}
 subset: gard_rare {source="GARD:0022730", source="MONDO:GARD"}
 subset: rare
-synonym: "Israeli spotted fever" RELATED [DOID:0050043]
 xref: DOID:0050043 {source="MONDO:equivalentTo"}
 xref: GARD:0022730 {source="MONDO:GARD"}
 is_a: MONDO:0001195 {source="DOID:0050043", source="MONDO:Redundant"} ! spotted fever
@@ -2668,7 +2660,6 @@ name: Far eastern spotted fever
 subset: doid {source="DOID:0050046"}
 subset: gard_rare {source="GARD:0022731", source="MONDO:GARD"}
 subset: rare
-synonym: "Rickettsia heilongjiangensis spotted fever" EXACT [DOID:0050046]
 xref: DOID:0050046 {source="MONDO:equivalentTo"}
 xref: GARD:0022731 {source="MONDO:GARD"}
 xref: MEDGEN:759467 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
@@ -2687,8 +2678,6 @@ def: "A spotted fever that has material basis in Rickettsia honei, which is tran
 subset: doid {source="DOID:0050047"}
 subset: gard_rare {source="GARD:0022732", source="MONDO:GARD"}
 subset: rare
-synonym: "FISF" RELATED ABBREVIATION [DOID:0050047]
-synonym: "Thai tick typhus" EXACT [DOID:0050047]
 xref: DOID:0050047 {source="MONDO:equivalentTo"}
 xref: GARD:0022732 {source="MONDO:GARD"}
 xref: MEDGEN:1375989 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
@@ -2711,7 +2700,6 @@ synonym: "fevers, Japanese spotted" RELATED [MESH:D000073605]
 synonym: "Japanese spotted fever" EXACT [DOID:0050050, MESH:D000073605]
 synonym: "Japanese spotted fevers" RELATED [MESH:D000073605]
 synonym: "oriental spotted fever" RELATED []
-synonym: "Rickettsia japonica spotted fever" EXACT [DOID:0050050]
 synonym: "spotted fever, Japanese" RELATED [MESH:D000073605]
 xref: DOID:0050050 {source="MONDO:equivalentTo"}
 xref: GARD:0022733 {source="MONDO:GARD"}
@@ -2935,7 +2923,6 @@ def: "A dengue disease that involves the most severe form of dengue fever, has m
 subset: doid {source="DOID:0050125"}
 subset: gard_rare {source="GARD:0022736", source="MONDO:GARD"}
 subset: rare
-synonym: "DSS" EXACT ABBREVIATION [DOID:0050125]
 xref: DOID:0050125 {source="MONDO:equivalentTo"}
 xref: GARD:0022736 {source="MONDO:GARD"}
 xref: MEDGEN:83958 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
@@ -2964,7 +2951,6 @@ id: MONDO:0000250
 name: osmotic diarrheal disease
 def: "A diarrhea that results from the presence of osmotically active, poorly absorbed solutes in the bowel lumen that inhibit normal water and electrolyte absorption." [https://www.ncbi.nlm.nih.gov/books/NBK414/]
 subset: doid {source="DOID:0050130"}
-synonym: "osmotic diarrhea" EXACT [DOID:0050130]
 synonym: "osmotic diarrhoea" EXACT OMO:0003005 []
 synonym: "permeability diarrhea" EXACT [https://orcid.org/0000-0002-6601-2165]
 synonym: "permeability diarrhoea" EXACT OMO:0003005 []
@@ -3051,7 +3037,6 @@ id: MONDO:0000255
 name: subcutaneous mycosis
 def: "A mycosis that involves subcutaneous tissue. There are three general types of subcutaneous mycoses: chromoblastomycosis, mycetoma, and sporotrichosis." [https://www.ncbi.nlm.nih.gov/books/NBK7902]
 subset: doid {source="DOID:0050135"}
-synonym: "subcutaneous mycosis" EXACT [DOID:0050135]
 xref: DOID:0050135 {source="MONDO:equivalentTo"}
 xref: ICD10CM:L00-L08 {source="https://github.com/monarch-initiative/mondo/issues/4536", source="https://orcid.org/0000-0001-5208-3432", source="https://orcid.org/0000-0002-4142-7153"}
 xref: MEDGEN:1684692 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
@@ -3339,7 +3324,6 @@ subset: doid {source="DOID:0050174"}
 subset: gard_rare {source="GARD:0022740", source="MONDO:GARD"}
 subset: nord_rare {source="MONDO:NORD"}
 subset: rare
-synonym: "Kunjin encephalitis" EXACT [DOID:0050174]
 xref: DOID:0050174 {source="MONDO:equivalentTo"}
 xref: GARD:0022740 {source="MONDO:GARD"}
 is_a: MONDO:0019376 {source="DOID:0050174"} ! West-Nile encephalitis
@@ -3555,7 +3539,6 @@ subset: rare
 synonym: "Acanthamoeba encephalitis" RELATED []
 synonym: "Acanthamoeba granulomatous encephalitis" RELATED []
 synonym: "granulomatous amebic encephalitis due to Acanthamoeba" RELATED []
-synonym: "granulomatous amoebic encephalitis" EXACT [DOID:0050246]
 xref: DOID:0050246 {source="MONDO:equivalentTo"}
 xref: GARD:0012651 {source="MONDO:GARD"}
 xref: ICD9:323.2 {source="MONDO:relatedTo", source="MONDO:i2s"}
@@ -4075,15 +4058,10 @@ subset: gard_rare {source="GARD:0009520", source="MONDO:GARD"}
 subset: ncit {source="NCIT:C84604"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
-synonym: "Bairnsdale ulcer" EXACT [DOID:0050456]
 synonym: "Buruli ulcer" EXACT [icd11.foundation:1974989140, NCIT:C84604]
-synonym: "Daintree ulcer" EXACT [DOID:0050456]
-synonym: "Mossman ulcer" EXACT [DOID:0050456]
 synonym: "Mycobacterium ulcerans caused disease or disorder" EXACT [MONDO:patterns/specific_infectious_disease_by_agent]
 synonym: "Mycobacterium ulcerans disease or disorder" EXACT []
 synonym: "Mycobacterium ulcerans infectious disease" EXACT []
-synonym: "Searl ulcer" EXACT [DOID:0050456]
-synonym: "Searle's ulcer" EXACT [DOID:0050456]
 xref: DOID:0050456 {source="MONDO:equivalentTo"}
 xref: GARD:0009520 {source="MONDO:GARD"}
 xref: ICD10CM:A31.1 {source="DOID:0050456"}
@@ -4138,17 +4116,10 @@ subset: ordo_disorder {source="Orphanet:83315"}
 subset: orphanet {source="Orphanet:83315"}
 subset: orphanet_rare {source="Orphanet:83315"}
 subset: rare
-synonym: "cat flea rickettsiosis" EXACT [DOID:0050481]
 synonym: "endemic flea-borne typhus" EXACT [NCIT:C84688]
 synonym: "endemic typhus fever" EXACT [icd11.foundation:4659958, NCIT:C84688]
-synonym: "fleaborne typhus" EXACT [DOID:0050481]
 synonym: "murine typhus" EXACT [DOID:0050481, icd11.foundation:4659958, Orphanet:83315, Wikipedia:Murine_typhus]
-synonym: "rat-flea typhus" EXACT [DOID:0050481]
-synonym: "Rickettsia felis spotted fever" EXACT [DOID:0050481]
-synonym: "shop typhus" RELATED [DOID:0050481]
-synonym: "toulon typhus" EXACT [DOID:0050481]
 synonym: "urban typhus" EXACT [DOID:0050481, icd11.foundation:4659958]
-synonym: "urban typhus of Malaya" EXACT [DOID:0050481]
 xref: DOID:0050481 {source="MONDO:equivalentTo"}
 xref: GARD:0019033 {source="MONDO:GARD"}
 xref: ICD10CM:A75.2 {source="Orphanet:83315", source="Orphanet:83315/e"}
@@ -4764,13 +4735,10 @@ def: "A parasitic infection caused by tapeworms of the genus Taenia. Humans are
 subset: doid {source="DOID:0050596"}
 subset: ncit {source="NCIT:C85180"}
 subset: otar {source="MONDO:OTAR"}
-synonym: "beef tapeworm infection" RELATED [DOID:0050596]
 synonym: "infection by taenia saginata" RELATED [https://orcid.org/0000-0002-6601-2165]
-synonym: "infection by Taeniarhynchus saginatus" RELATED [DOID:0050596]
 synonym: "infections, Taenia" RELATED [MONDO:patterns/infectious_disease_by_agent]
 synonym: "Taenia infection" EXACT [MONDO:patterns/infectious_disease_by_agent]
 synonym: "taenia saginata infection" EXACT [https://orcid.org/0000-0002-6601-2165]
-synonym: "Taenia saginata infectious disease" RELATED [DOID:0050596]
 synonym: "unarmed tapeworm infection" RELATED [https://orcid.org/0000-0002-6601-2165]
 xref: DOID:0050596 {source="MONDO:equivalentTo"}
 xref: EFO:1001433 {source="MONDO:equivalentTo", source="MONDO:EFO"}
@@ -5061,7 +5029,6 @@ subset: rare
 synonym: "accessory sinus cancer" EXACT [NCIT:C6014]
 synonym: "accessory sinus carcinoma" EXACT [NCIT:C6014]
 synonym: "adenoid cystic carcinoma of accessory sinus" RELATED []
-synonym: "adenoid cystic carcinoma of paranasal sinus" RELATED [DOID:0050619]
 synonym: "cancer of paranasal sinus" EXACT [MONDO:patterns/cancer]
 synonym: "carcinoma of accessory sinus" EXACT [DOID:0050619, NCIT:C6014]
 synonym: "carcinoma of paranasal sinus" EXACT [DOID:0050619, MONDO:patterns/carcinoma, NCIT:C6014]
@@ -6237,8 +6204,6 @@ name: primary progressive multiple sclerosis
 def: "A multiple sclerosis that is characterized by steady worsening of neurologic functioning, without any distinct relapses or periods of remission. The rate of progression may vary over time, with occasional plateaus or temporary improvements, but the progression is continuous." [DOID:0050784, http://www.mayoclinic.org/multiple-sclerosis/types.html, http://www.nationalmssociety.org/about-multiple-sclerosis/progressive-ms/primary-progressive-ms/index.aspx]
 subset: doid {source="DOID:0050784"}
 subset: otar {source="MONDO:OTAR"}
-synonym: "PPMS" EXACT ABBREVIATION [DOID:0050784]
-synonym: "primary-progressive MS" EXACT [DOID:0050784]
 xref: DOID:0050784 {source="MONDO:equivalentTo"}
 xref: EFO:0008520 {source="MONDO:equivalentTo", source="MONDO:EFO"}
 xref: icd11.foundation:1020720762 {source="MONDO:equivalentTo"}
@@ -6255,8 +6220,6 @@ id: MONDO:0000452
 name: progressive relapsing multiple sclerosis
 def: "A multiple sclerosis that is characterized by steadily worsening symptoms and attacks during periods of remission with disease progression from the onset." [DOID:0050785, http://www.mayoclinic.org/multiple-sclerosis/types.html, http://www.nationalmssociety.org/about-multiple-sclerosis/progressive-ms/progressive-relapsing-ms/index.aspx]
 subset: doid {source="DOID:0050785"}
-synonym: "PRMS" EXACT ABBREVIATION [DOID:0050785]
-synonym: "progressive-relapsing MS" EXACT [DOID:0050785]
 xref: DOID:0050785 {source="MONDO:equivalentTo"}
 xref: MEDGEN:95982 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
... (29844 more lines truncated)
```

## Agent Attempts (8)

### Attempt 1: claude-sonnet-4.5 / claude

- **Eval PR**: [#462](https://github.com/ai4curation/eval-ont-agent-mondo/pull/462)
- **F1**: 0.003  **Precision**: 0.002  **Recall**: 1.000  **Jaccard**: 0.002
- **Trace**: [25867832427](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25867832427)
- **Workflow run**: [25867832427](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867832427)

#### Agent PR Comment

# Fix incorrect synonyms for MONDO:0001628 (tinea unguium)

#### Agent Issue Comment

The incorrect synonyms have been removed from MONDO:0001628 (tinea unguium). Changes committed in PR #<NN>.

All 8 erroneous "cellulitis and abscess" synonyms that were incorrectly associated with this fungal nail infection term have been removed, leaving only the clinically appropriate synonyms related to dermatophytic nail infections.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-sonnet-4-5-20250929`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25867832427)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 5f0045ca8..b9af5d19d 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -30041,14 +30041,6 @@ name: tinea unguium
 def: "A fungal infection of the nail, usually caused by dermatophytes; yeasts; or nondermatophyte molds." [MESH:D014009]
 subset: doid {source="DOID:13074"}
 subset: ncit {source="NCIT:C112214"}
-synonym: "cellulitis and abscess" RELATED [DOID:13074]
-synonym: "cellulitis and abscess of buttock" EXACT [DOID:13074, ICD9CM:682.5]
-synonym: "cellulitis and abscess of face" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger and toe" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of gluteal region" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of trunk" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of upper arm and forearm" EXACT [DOID:13074]
 synonym: "dermatophytic onychia" EXACT [DOID:13074, ICD10CM:B35.1]
 synonym: "dermatophytic onychomycosis" EXACT [DOID:13074]
 synonym: "dermatophytosis of nail" EXACT [DOID:13074, ICD10CM:B35.1, ICD9CM:110.1]

```

### Attempt 2: claude-opus-4.7 / claude

- **Eval PR**: [#386](https://github.com/ai4curation/eval-ont-agent-mondo/pull/386)
- **F1**: 0.003  **Precision**: 0.002  **Recall**: 1.000  **Jaccard**: 0.002
- **Trace**: [25817604142](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25817604142)
- **Workflow run**: [25817604142](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817604142)

#### Agent PR Comment

## Summary

Fixes #10030 by removing incorrect synonyms on MONDO:0001628 (tinea unguium).

Tinea unguium is a fungal infection of the nail (def: "A fungal infection of the nail, usually caused by dermatophytes; yeasts; or nondermatophyte molds."). However, the term had inherited a block of synonyms from DOID:13074 that describe bacterial soft-tissue infections at unrelated body sites. The issue reporter flagged these as obvious errors.

## Synonyms removed

All eight came in with `[DOID:13074]` as their source:

- `"cellulitis and abscess" RELATED`
- `"cellulitis and abscess of buttock" EXACT`
- `"cellulitis and abscess of face" EXACT`
- `"cellulitis and abscess of finger" EXACT`
- `"cellulitis and abscess of finger and toe" EXACT`
- `"cellulitis and abscess of gluteal region" EXACT`
- `"cellulitis and abscess of trunk" EXACT`
- `"cellulitis and abscess of upper arm and forearm" EXACT`

None of these describe a fungal nail infection, so they are not appropriate synonyms (not even RELATED) for this term. The issue explicitly listed the buttock/face/gluteal region/trunk/upper arm variants as incorrect; I also removed the bare "cellulitis and abscess" and the finger/toe variants since they share the same erroneous origin and same conceptual mismatch (cellulitis vs. dermatophytosis).

## What I left alone

- All correct synonyms (`onychomycosis`, `dermatophytic onychia`, `dermatophytosis of nail`, etc.) are preserved.
- Xrefs were not touched. `xref: ICD9:681.9` (cellulitis and abscess of unspecified site, sourced from DOID:13074) looks similarly suspect, but the issue is scoped to synonyms and a follow-up DO-import audit (mentioned by @sabrinatoro in the thread) would be the right place to address xref-level mismatches.
- Logical axioms (`is_a`, `intersection_of`, `disease_has_infectious_agent`) are unchanged — they correctly describe a fungal nail dermatophytosis.

## Checklist

- [x] Identified the source of the bad synonyms (DOID:13074 import)
- [x] Confirmed they conflict with the term definition and logical axioms
- [x] Removed only the synonyms; preserved correct content
- [x] `robot convert` syntax check on the edit file: passes
- [x] `owltools NORM` + `robot convert` normalization run; no spurious diff produced
- [x] Diff inspected — only the eight target lines deleted

## Note on scale

As discussed in the issue thread, this class of bad-import is not unique to MONDO:0001628 — a more systematic sweep of DO-derived synonyms is probably warranted. This PR is intentionally a narrow, term-level fix for the one term the issue identifies.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817604142)


#### Agent Issue Comment

The eight erroneous "cellulitis and abscess..." synonyms on MONDO:0001628 (tinea unguium) have been removed in PR #<NN>.

Note: per @sabrinatoro's comment, a broader DO-import cleanup is still warranted — this PR only addresses the specific term cited in the issue.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-opus-4-7`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25817604142)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 5f0045ca8..b9af5d19d 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -30041,14 +30041,6 @@ name: tinea unguium
 def: "A fungal infection of the nail, usually caused by dermatophytes; yeasts; or nondermatophyte molds." [MESH:D014009]
 subset: doid {source="DOID:13074"}
 subset: ncit {source="NCIT:C112214"}
-synonym: "cellulitis and abscess" RELATED [DOID:13074]
-synonym: "cellulitis and abscess of buttock" EXACT [DOID:13074, ICD9CM:682.5]
-synonym: "cellulitis and abscess of face" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger and toe" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of gluteal region" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of trunk" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of upper arm and forearm" EXACT [DOID:13074]
 synonym: "dermatophytic onychia" EXACT [DOID:13074, ICD10CM:B35.1]
 synonym: "dermatophytic onychomycosis" EXACT [DOID:13074]
 synonym: "dermatophytosis of nail" EXACT [DOID:13074, ICD10CM:B35.1, ICD9CM:110.1]

```

### Attempt 3: kimi-k2.6 / opencode

- **Eval PR**: [#273](https://github.com/ai4curation/eval-ont-agent-mondo/pull/273)
- **F1**: 0.003  **Precision**: 0.002  **Recall**: 0.800  **Jaccard**: 0.002
- **Trace**: [25755662876](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25755662876)
- **Workflow run**: [25755662876](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755662876)

#### Agent PR Comment

## Summary

Removed 8 incorrect synonyms and 1 incorrect xref from MONDO:0001628 (tinea unguium). These synonyms erroneously described bacterial cellulitis and abscess of various body parts, which are unrelated to this fungal nail infection term.

## Background

Issue #10030 reported that MONDO:0001628 "tinea unguium" (a fungal infection of the nails) contained exact synonyms referring to cellulitis and abscess of the buttock, face, gluteal region, trunk, upper arm and forearm, etc. These were incorrectly imported from DOID:13074.

## Changes Made

### Removed Synonyms
The following 8 synonyms were removed from MONDO:0001628:

1. `synonym: "cellulitis and abscess" RELATED [DOID:13074]`
2. `synonym: "cellulitis and abscess of buttock" EXACT [DOID:13074, ICD9CM:682.5]`
3. `synonym: "cellulitis and abscess of face" EXACT [DOID:13074]`
4. `synonym: "cellulitis and abscess of finger" EXACT [DOID:13074]`
5. `synonym: "cellulitis and abscess of finger and toe" EXACT [DOID:13074]`
6. `synonym: "cellulitis and abscess of gluteal region" EXACT [DOID:13074]`
7. `synonym: "cellulitis and abscess of trunk" EXACT [DOID:13074]`
8. `synonym: "cellulitis and abscess of upper arm and forearm" EXACT [DOID:13074]`

### Removed Xref
- `xref: ICD9:681.9 {source="DOID:13074"}` — This ICD-9 code corresponds to "Cellulitis and abscess of unspecified digit," which is not equivalent to tinea unguium.

### Added Term Tracker
- `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10030" xsd:anyURI`

## Checklist

- [x] Read and understood the issue
- [x] Checked out term using `obo-checkout.pl`
- [x] Removed all incorrect cellulitis/abscess-related synonyms
- [x] Removed incorrect ICD9 xref
- [x] Added term tracker item linking to issue #10030
- [x] Checked term back in with `obo-checkin.pl`
- [x] Ran ODK normalization (`make NORM`)
- [x] Validated syntax with `robot convert` — no errors
- [x] Committed changes

## Validation

Syntax validation was performed with:
```
robot convert --catalog catalog-v001.xml -i mondo-edit.obo -f obo -o mondo-edit.TMP.obo
```

No errors were reported.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755662876)


#### Agent Issue Comment

Thank you for reporting this. The incorrect synonyms for MONDO:0001628 (tinea unguium) have been removed in PR #<NN>.

The following erroneous synonyms (all related to cellulitis and abscess of various body parts) were removed:
- cellulitis and abscess (RELATED)
- cellulitis and abscess of buttock (EXACT)
- cellulitis and abscess of face (EXACT)
- cellulitis and abscess of finger (EXACT)
- cellulitis and abscess of finger and toe (EXACT)
- cellulitis and abscess of gluteal region (EXACT)
- cellulitis and abscess of trunk (EXACT)
- cellulitis and abscess of upper arm and forearm (EXACT)

Also removed the incorrectly associated ICD9:681.9 xref.

A term tracker item linking to this issue has been added to the stanza.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `togetherai/moonshotai/Kimi-K2.6`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25755662876)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 5f0045ca8..a8c0e6e98 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -30041,14 +30041,6 @@ name: tinea unguium
 def: "A fungal infection of the nail, usually caused by dermatophytes; yeasts; or nondermatophyte molds." [MESH:D014009]
 subset: doid {source="DOID:13074"}
 subset: ncit {source="NCIT:C112214"}
-synonym: "cellulitis and abscess" RELATED [DOID:13074]
-synonym: "cellulitis and abscess of buttock" EXACT [DOID:13074, ICD9CM:682.5]
-synonym: "cellulitis and abscess of face" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger and toe" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of gluteal region" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of trunk" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of upper arm and forearm" EXACT [DOID:13074]
 synonym: "dermatophytic onychia" EXACT [DOID:13074, ICD10CM:B35.1]
 synonym: "dermatophytic onychomycosis" EXACT [DOID:13074]
 synonym: "dermatophytosis of nail" EXACT [DOID:13074, ICD10CM:B35.1, ICD9CM:110.1]
@@ -30058,7 +30050,6 @@ synonym: "onychomycosis due to dermatophyte" EXACT [DOID:13074]
 synonym: "tinea unguium" EXACT [DOID:13074, ICD10CM:B35.1, NCIT:C112214]
 xref: DOID:13074 {source="MONDO:equivalentTo"}
 xref: ICD10CM:B35.1 {source="MONDO:equivalentTo"}
-xref: ICD9:681.9 {source="DOID:13074"}
 xref: MEDGEN:11825 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:D014009 {source="MONDO:equivalentTo"}
 xref: NCIT:C112214 {source="MONDO:equivalentTo"}
@@ -30070,6 +30061,7 @@ intersection_of: disease_has_location UBERON:0001705 ! nail
 relationship: disease_has_infectious_agent NCBITaxon:4751 ! Fungi
 relationship: disease_has_infectious_agent NCBITaxon:4890 ! Ascomycota
 property_value: curated_content_resource "https://www.malacards.org/card/tinea_unguium" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10030" xsd:anyURI
 
 [Term]
 id: MONDO:0001629

```

### Attempt 4: claude-haiku-4.5 / claude

- **Eval PR**: [#175](https://github.com/ai4curation/eval-ont-agent-mondo/pull/175)
- **F1**: 0.003  **Precision**: 0.002  **Recall**: 1.000  **Jaccard**: 0.002
- **Workflow run**: [25640392448](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640392448)

#### Agent PR Comment

# Removal of Incorrect Synonyms from MONDO:0001628

## Problem Statement
MONDO:0001628 (tinea unguium) is a fungal infection of the nails. However, the term had 8 incorrect synonyms related to "cellulitis and abscess" of various body locations (buttock, face, finger, gluteal region, trunk, upper arm and forearm). These synonyms are completely unrelated to nail fungal infections and appear to have been mistakenly imported from Disease Ontology (DO).

## Changes Made
Removed the following incorrect synonyms from MONDO:0001628:
1. "cellulitis and abscess" RELATED
2. "cellulitis and abscess of buttock" EXACT
3. "cellulitis and abscess of face" EXACT
4. "cellulitis and abscess of finger" EXACT
5. "cellulitis and abscess of finger and toe" EXACT
6. "cellulitis and abscess of gluteal region" EXACT
7. "cellulitis and abscess of trunk" EXACT
8. "cellulitis and abscess of upper arm and forearm" EXACT

## Validation
- Verified the term definition and remaining synonyms are all related to fungal nail infections
- Remaining synonyms include: onychomycosis, dermatophytic onychia, dermatophytic onychomycosis, dermatophytosis of nail, nail dermatophytosis, and onychomycosis due to dermatophyte
- All logical axioms and cross-references remain unchanged and intact
- The term is_a relationships (nail disorder, dermatophytosis) remain valid

## Notes
- These errors appear to stem from DO DOID:13074 (cellulitis and abscess) having been incorrectly used as a source for tinea unguium synonyms
- As noted in the issue comments, this appears to be part of a larger systemic issue that may warrant a more drastic, large-scale approach to address similar problems across the ontology

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640392448)


#### Agent Issue Comment

## Summary

The incorrect synonyms have been removed from MONDO:0001628 (tinea unguium). 

**Changes made:**
- Removed 8 incorrect "cellulitis and abscess" synonyms that were unrelated to tinea unguium (a fungal nail infection)
- Kept all valid nail infection-related synonyms

The changes have been committed to PR <NN>.

---
🤖 **Generated by claude agent**
- Runtime: `claude`
- Model: `claude-haiku-4-5-20251001`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640392448)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 5f0045ca8..b9af5d19d 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -30041,14 +30041,6 @@ name: tinea unguium
 def: "A fungal infection of the nail, usually caused by dermatophytes; yeasts; or nondermatophyte molds." [MESH:D014009]
 subset: doid {source="DOID:13074"}
 subset: ncit {source="NCIT:C112214"}
-synonym: "cellulitis and abscess" RELATED [DOID:13074]
-synonym: "cellulitis and abscess of buttock" EXACT [DOID:13074, ICD9CM:682.5]
-synonym: "cellulitis and abscess of face" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger and toe" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of gluteal region" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of trunk" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of upper arm and forearm" EXACT [DOID:13074]
 synonym: "dermatophytic onychia" EXACT [DOID:13074, ICD10CM:B35.1]
 synonym: "dermatophytic onychomycosis" EXACT [DOID:13074]
 synonym: "dermatophytosis of nail" EXACT [DOID:13074, ICD10CM:B35.1, ICD9CM:110.1]

```

### Attempt 5: gpt-5.4 / codex

- **Eval PR**: [#154](https://github.com/ai4curation/eval-ont-agent-mondo/pull/154)
- **F1**: 0.003  **Precision**: 0.002  **Recall**: 1.000  **Jaccard**: 0.002
- **Workflow run**: [25640342751](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640342751)

#### Agent PR Comment

This change fixes `MONDO:0001628` (`tinea unguium`) by removing eight unrelated DO-derived synonyms:

- `cellulitis and abscess`
- `cellulitis and abscess of buttock`
- `cellulitis and abscess of face`
- `cellulitis and abscess of finger`
- `cellulitis and abscess of finger and toe`
- `cellulitis and abscess of gluteal region`
- `cellulitis and abscess of trunk`
- `cellulitis and abscess of upper arm and forearm`

Rationale:

- The issue reports that these synonyms refer to cellulitis/abscess conditions affecting unrelated body sites, not to fungal nail infection.
- The remaining synonyms on the term continue to describe onychomycosis / dermatophytosis of the nail and were left intact.
- No parentage, definition, xrefs, or logical axioms were changed in this edit.

Completed checklist:

- [x] Read `__issue_context__.json`
- [x] Inspected the `MONDO:0001628` stanza in `src/ontology/mondo-edit.obo`
- [x] Checked out the term to `terms/MONDO_0001628.obo`
- [x] Removed the incorrect synonym axioms only
- [x] Checked the term back into `src/ontology/mondo-edit.obo`
- [x] Ran syntax validation with local `robot convert`
- [x] Committed only the edited ontology file

Validation:

- `robot convert --catalog catalog-v001.xml -i mondo-edit.obo -f obo -o mondo-edit.TMP.obo` completed successfully from `src/ontology`.

Environment limitation:

- I could not run the standard normalization step (`sh run.sh make NORM && mv NORM mondo-edit.obo`) because this runner does not have `docker` available, and `src/ontology/run.sh` depends on Docker.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640342751)

#### Agent Issue Comment

Addressed in PR #<NN>.

Removed the incorrect `cellulitis and abscess...` synonyms from `MONDO:0001628` (`tinea unguium`) while leaving the fungal nail disease synonyms and logical axioms unchanged.

Validation note: local `robot convert` syntax check passed. I could not run the usual ODK normalization step in this environment because `docker` is not available.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.4`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25640342751)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 5f0045ca8..b9af5d19d 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -30041,14 +30041,6 @@ name: tinea unguium
 def: "A fungal infection of the nail, usually caused by dermatophytes; yeasts; or nondermatophyte molds." [MESH:D014009]
 subset: doid {source="DOID:13074"}
 subset: ncit {source="NCIT:C112214"}
-synonym: "cellulitis and abscess" RELATED [DOID:13074]
-synonym: "cellulitis and abscess of buttock" EXACT [DOID:13074, ICD9CM:682.5]
-synonym: "cellulitis and abscess of face" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger and toe" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of gluteal region" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of trunk" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of upper arm and forearm" EXACT [DOID:13074]
 synonym: "dermatophytic onychia" EXACT [DOID:13074, ICD10CM:B35.1]
 synonym: "dermatophytic onychomycosis" EXACT [DOID:13074]
 synonym: "dermatophytosis of nail" EXACT [DOID:13074, ICD10CM:B35.1, ICD9CM:110.1]

```

### Attempt 6: gpt-5.5 / opencode

- **Eval PR**: [#88](https://github.com/ai4curation/eval-ont-agent-mondo/pull/88)
- **F1**: 0.003  **Precision**: 0.002  **Recall**: 0.800  **Jaccard**: 0.002
- **Trace**: [25615982287](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615982287)
- **Workflow run**: [25615982287](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615982287)

#### Agent PR Comment

## Summary

Addressed issue #10030 for `MONDO:0001628` (tinea unguium).

Changes made:
- Removed erroneous cellulitis/abscess synonyms from the tinea unguium term, including the location-specific synonyms for buttock, face, finger, finger/toe, gluteal region, trunk, and upper arm/forearm.
- Removed the broader related synonym `cellulitis and abscess` because it is not applicable to a fungal nail infection.
- Removed the associated incorrect `ICD9:681.9` xref, which refers to cellulitis/abscess rather than tinea unguium.
- Added the issue URL as `IAO:0000233` term tracker metadata.

## Rationale

`tinea unguium` is defined as a fungal infection of the nail. The removed synonyms referred to cellulitis and abscesses at non-nail body locations and were therefore misleading exact synonyms for this term. The remaining synonyms are nail dermatophytosis / onychomycosis-related and consistent with the term meaning.

## Checks performed

- Checked out and edited `MONDO:0001628` via the `terms/` workflow.
- Checked the term back into `src/ontology/mondo-edit.obo`.
- Normalized `mondo-edit.obo` with `make NORM && mv NORM mondo-edit.obo` from `src/ontology`.
- Validated OBO syntax with:
  `robot convert --catalog catalog-v001.xml -i mondo-edit.obo -f obo -o mondo-edit.TMP.obo`

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615982287)


#### Agent Issue Comment

Changes committed in PR #<NN>.

I removed the erroneous cellulitis/abscess synonyms from `MONDO:0001628` (tinea unguium) and also removed the associated incorrect ICD9 xref that referred to cellulitis/abscess rather than nail dermatophytosis.

---
🤖 **Generated by pi agent**
- Runtime: `pi`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615982287)


#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 5f0045ca8..a8c0e6e98 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -30041,14 +30041,6 @@ name: tinea unguium
 def: "A fungal infection of the nail, usually caused by dermatophytes; yeasts; or nondermatophyte molds." [MESH:D014009]
 subset: doid {source="DOID:13074"}
 subset: ncit {source="NCIT:C112214"}
-synonym: "cellulitis and abscess" RELATED [DOID:13074]
-synonym: "cellulitis and abscess of buttock" EXACT [DOID:13074, ICD9CM:682.5]
-synonym: "cellulitis and abscess of face" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger and toe" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of gluteal region" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of trunk" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of upper arm and forearm" EXACT [DOID:13074]
 synonym: "dermatophytic onychia" EXACT [DOID:13074, ICD10CM:B35.1]
 synonym: "dermatophytic onychomycosis" EXACT [DOID:13074]
 synonym: "dermatophytosis of nail" EXACT [DOID:13074, ICD10CM:B35.1, ICD9CM:110.1]
@@ -30058,7 +30050,6 @@ synonym: "onychomycosis due to dermatophyte" EXACT [DOID:13074]
 synonym: "tinea unguium" EXACT [DOID:13074, ICD10CM:B35.1, NCIT:C112214]
 xref: DOID:13074 {source="MONDO:equivalentTo"}
 xref: ICD10CM:B35.1 {source="MONDO:equivalentTo"}
-xref: ICD9:681.9 {source="DOID:13074"}
 xref: MEDGEN:11825 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:D014009 {source="MONDO:equivalentTo"}
 xref: NCIT:C112214 {source="MONDO:equivalentTo"}
@@ -30070,6 +30061,7 @@ intersection_of: disease_has_location UBERON:0001705 ! nail
 relationship: disease_has_infectious_agent NCBITaxon:4751 ! Fungi
 relationship: disease_has_infectious_agent NCBITaxon:4890 ! Ascomycota
 property_value: curated_content_resource "https://www.malacards.org/card/tinea_unguium" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10030" xsd:anyURI
 
 [Term]
 id: MONDO:0001629

```

### Attempt 7: gpt-5.5 / opencode

- **Eval PR**: [#69](https://github.com/ai4curation/eval-ont-agent-mondo/pull/69)
- **F1**: 0.003  **Precision**: 0.002  **Recall**: 0.800  **Jaccard**: 0.002
- **Trace**: [25615940605](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615940605)
- **Workflow run**: [25615940605](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615940605)

#### Agent PR Comment

## Summary

Addressed issue #10030 by removing non-nail cellulitis/abscess synonyms from `MONDO:0001628` (`tinea unguium`). These labels refer to bacterial skin/soft tissue infections at other body locations and are not appropriate synonyms for fungal infection of the nail.

#### Agent Issue Comment

Removed the erroneous cellulitis/abscess synonyms from `MONDO:0001628` (`tinea unguium`). Changes committed in PR #<NN>.

---
🤖 **Generated by opencode agent**
- Runtime: `opencode`
- Model: `openai/gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615940605)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 5f0045ca8..a8c0e6e98 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -30041,14 +30041,6 @@ name: tinea unguium
 def: "A fungal infection of the nail, usually caused by dermatophytes; yeasts; or nondermatophyte molds." [MESH:D014009]
 subset: doid {source="DOID:13074"}
 subset: ncit {source="NCIT:C112214"}
-synonym: "cellulitis and abscess" RELATED [DOID:13074]
-synonym: "cellulitis and abscess of buttock" EXACT [DOID:13074, ICD9CM:682.5]
-synonym: "cellulitis and abscess of face" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger and toe" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of gluteal region" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of trunk" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of upper arm and forearm" EXACT [DOID:13074]
 synonym: "dermatophytic onychia" EXACT [DOID:13074, ICD10CM:B35.1]
 synonym: "dermatophytic onychomycosis" EXACT [DOID:13074]
 synonym: "dermatophytosis of nail" EXACT [DOID:13074, ICD10CM:B35.1, ICD9CM:110.1]
@@ -30058,7 +30050,6 @@ synonym: "onychomycosis due to dermatophyte" EXACT [DOID:13074]
 synonym: "tinea unguium" EXACT [DOID:13074, ICD10CM:B35.1, NCIT:C112214]
 xref: DOID:13074 {source="MONDO:equivalentTo"}
 xref: ICD10CM:B35.1 {source="MONDO:equivalentTo"}
-xref: ICD9:681.9 {source="DOID:13074"}
 xref: MEDGEN:11825 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:D014009 {source="MONDO:equivalentTo"}
 xref: NCIT:C112214 {source="MONDO:equivalentTo"}
@@ -30070,6 +30061,7 @@ intersection_of: disease_has_location UBERON:0001705 ! nail
 relationship: disease_has_infectious_agent NCBITaxon:4751 ! Fungi
 relationship: disease_has_infectious_agent NCBITaxon:4890 ! Ascomycota
 property_value: curated_content_resource "https://www.malacards.org/card/tinea_unguium" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10030" xsd:anyURI
 
 [Term]
 id: MONDO:0001629

```

### Attempt 8: gpt-5.5 / codex

- **Eval PR**: [#49](https://github.com/ai4curation/eval-ont-agent-mondo/pull/49)
- **F1**: 0.003  **Precision**: 0.002  **Recall**: 0.800  **Jaccard**: 0.002
- **Trace**: [25615893658](https://github.com/ai4curation/eval-ont-agent-mondo/tree/master/traces/25615893658)
- **Workflow run**: [25615893658](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615893658)

#### Agent PR Comment

Addressed issue #10030 by cleaning up `MONDO:0001628` (`tinea unguium`).

Changes made:
- Removed the full cellulitis/abscess synonym cluster from `tinea unguium`, including the examples listed in the issue and the same-cluster entries for finger/finger-and-toe.
- Removed `xref: ICD9:681.9 {source="DOID:13074"}` because ICD-9 681.9 is cellulitis and abscess of unspecified digit, which belongs to the same erroneous imported cellulitis/abscess content.
- Added the issue tracker provenance annotation for https://github.com/monarch-initiative/mondo/issues/10030.
- Left the existing nail disorder / dermatophytosis parents and logical definition unchanged; they remain consistent with the term definition and location axiom.

Checklist completed:
- Read `__issue_context__.json`.
- Inspected `MONDO:0001628` with `obo-grep.pl`.
- Checked out and checked in the term with `obo-checkout.pl` / `obo-checkin.pl`.
- Verified the final stanza no longer contains the erroneous cellulitis/abscess synonyms.
- Ran normalization with `make NORM && mv NORM mondo-edit.obo` from `src/ontology` using the local toolchain. The Docker-backed `sh run.sh make NORM` path was attempted first but Docker is not installed in this environment.
- Ran syntax validation: `robot convert --catalog src/ontology/catalog-v001.xml -i src/ontology/mondo-edit.obo -f obo -o mondo-edit.TMP.obo`.
- Ran `git diff --check -- src/ontology/mondo-edit.obo`.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615893658)

#### Agent Issue Comment

Changes committed in PR #<NN>.

I removed the erroneous cellulitis/abscess synonyms from `MONDO:0001628` (`tinea unguium`) and removed the adjacent `ICD9:681.9` xref for cellulitis/abscess of an unspecified digit.

---
🤖 **Generated by codex agent**
- Runtime: `codex`
- Model: `gpt-5.5`
- Agent config: `ai4curation/mondo-agent-config@v3:.`
- Iteration: `1`
- Run: [View workflow run](https://github.com/ai4curation/eval-ont-agent-mondo/actions/runs/25615893658)

#### Agent Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 5f0045ca8..a8c0e6e98 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -30041,14 +30041,6 @@ name: tinea unguium
 def: "A fungal infection of the nail, usually caused by dermatophytes; yeasts; or nondermatophyte molds." [MESH:D014009]
 subset: doid {source="DOID:13074"}
 subset: ncit {source="NCIT:C112214"}
-synonym: "cellulitis and abscess" RELATED [DOID:13074]
-synonym: "cellulitis and abscess of buttock" EXACT [DOID:13074, ICD9CM:682.5]
-synonym: "cellulitis and abscess of face" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of finger and toe" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of gluteal region" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of trunk" EXACT [DOID:13074]
-synonym: "cellulitis and abscess of upper arm and forearm" EXACT [DOID:13074]
 synonym: "dermatophytic onychia" EXACT [DOID:13074, ICD10CM:B35.1]
 synonym: "dermatophytic onychomycosis" EXACT [DOID:13074]
 synonym: "dermatophytosis of nail" EXACT [DOID:13074, ICD10CM:B35.1, ICD9CM:110.1]
@@ -30058,7 +30050,6 @@ synonym: "onychomycosis due to dermatophyte" EXACT [DOID:13074]
 synonym: "tinea unguium" EXACT [DOID:13074, ICD10CM:B35.1, NCIT:C112214]
 xref: DOID:13074 {source="MONDO:equivalentTo"}
 xref: ICD10CM:B35.1 {source="MONDO:equivalentTo"}
-xref: ICD9:681.9 {source="DOID:13074"}
 xref: MEDGEN:11825 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:D014009 {source="MONDO:equivalentTo"}
 xref: NCIT:C112214 {source="MONDO:equivalentTo"}
@@ -30070,6 +30061,7 @@ intersection_of: disease_has_location UBERON:0001705 ! nail
 relationship: disease_has_infectious_agent NCBITaxon:4751 ! Fungi
 relationship: disease_has_infectious_agent NCBITaxon:4890 ! Ascomycota
 property_value: curated_content_resource "https://www.malacards.org/card/tinea_unguium" xsd:anyURI {source="MONDO:MalaCards"}
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10030" xsd:anyURI
 
 [Term]
 id: MONDO:0001629

```
