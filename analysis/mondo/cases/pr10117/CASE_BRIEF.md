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
num_agent_attempts: 12
generated_at: '2026-05-17'
scoping_notes: Bulk removal of synonyms across many terms in the ontology.
domain_area: quality-control
best_f1: 0.003
best_model: gpt-5.4
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

## Curation Note (data quality)

**This is a poor evaluation case (`case_quality: poor`, reason `gold_pr_is_out_of_scope_mega_edit`).** Flagged by claude-opus-4.7 on 2026-05-15 during attempt review.

**The issue vs. the gold PR are not scope-matched.** Issue #10030 ("Incorrect synonyms for MONDO_0001628") reports a single, specific defect: the term MONDO:0001628 "tinea unguium" (a fungal nail infection) carries 8 erroneous "cellulitis and abscess..." synonyms (bacterial soft-tissue infections at unrelated body sites) mis-imported from DOID:13074. In the issue thread the curators (matentzn, sabrinatoro) decided against fixing it one-by-one and opted for "a more drastic-large scale approach."

The selected gold PR #10117 ("Remove synonyms with uncertain semantics") *is* that drastic approach: it deletes **5,103 synonym lines with zero additions across hundreds of unrelated terms** ontology-wide (corticoadrenal insufficiency, growth hormone deficiency, spotted fevers, multiple sclerosis, Jaccoud syndrome, etc.). Within it, the 8 tinea-unguium synonyms are removed — but so are thousands of unrelated lines, and even two *valid* tinea-unguium synonyms (`dermatophytic onychomycosis`, `onychomycosis due to dermatophyte`) are swept out as collateral.

**Scoring consequence.** Whole-diff metadiff compares each attempt's correct ~8–10-line single-term fix against this 5,103-line ontology-wide sweep. Every one of the 8 attempts is therefore capped at F1≈0.003 by construction, regardless of quality. This is the Step 3b "gold has an out-of-scope mega-edit" signature: F1 is uniformly near-zero across all attempts, including no-op-equivalent runs.

**Judging the attempts.** Against the *literal ask of issue #10030*, all 8 attempts succeed: each correctly removes exactly the 8 erroneous "cellulitis and abscess..." synonyms from MONDO:0001628 and preserves the valid nail-dermatophytosis synonyms and all logical axioms. The opencode/codex variants (kimi-k2.6, gpt-5.5 ×3) additionally and defensibly remove the parallel mis-imported `xref: ICD9:681.9 {source="DOID:13074"}` and add an `IAO:0000233` issue-tracker provenance annotation per the mondo-agent-config convention. The claude-opus-4.7 run additionally shows the best judgment by explicitly recognizing the curators' large-scale-cleanup intent and consciously scoping its PR narrowly while flagging the broader DO-import audit as follow-up.

No companion PRs exist (`gh search prs --repo monarch-initiative/mondo "10030"` returns only #10117); the issue was resolved by the single ontology-wide PR. Downstream aggregation should down-weight or exclude this case, or re-score attempts against the issue's narrow ask rather than the metadiff vs. #10117.

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

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.003 | 0.002 | 0.889 | `a9a6bf8` | [#744](https://github.com/ai4curation/eval-ont-agent-mondo/pull/744) | [attempt](attempts/pr744.md) |
| 2 | gpt-5.4 | opencode | 0.003 | 0.002 | 0.889 | `a9a6bf8` | [#690](https://github.com/ai4curation/eval-ont-agent-mondo/pull/690) | [attempt](attempts/pr690.md) |
| 3 | gemma-4-31b | opencode | 0.003 | 0.002 | 1.000 | `b9af5d1` | [#596](https://github.com/ai4curation/eval-ont-agent-mondo/pull/596) | [attempt](attempts/pr596.md) |
| 4 | claude-sonnet-4.5 | claude | 0.003 | 0.002 | 1.000 | `b9af5d1` | [#462](https://github.com/ai4curation/eval-ont-agent-mondo/pull/462) | [attempt](attempts/pr462.md) |
| 5 | claude-opus-4.7 | claude | 0.003 | 0.002 | 1.000 | `b9af5d1` | [#386](https://github.com/ai4curation/eval-ont-agent-mondo/pull/386) | [attempt](attempts/pr386.md) |
| 6 | kimi-k2.6 | opencode | 0.003 | 0.002 | 0.800 | `a8c0e6e` | [#273](https://github.com/ai4curation/eval-ont-agent-mondo/pull/273) | [attempt](attempts/pr273.md) |
| 7 | gemma-4-31b | opencode | 0.003 | 0.002 | 1.000 | `b9af5d1` | [#243](https://github.com/ai4curation/eval-ont-agent-mondo/pull/243) | [attempt](attempts/pr243.md) |
| 8 | claude-haiku-4.5 | claude | 0.003 | 0.002 | 1.000 | `b9af5d1` | [#175](https://github.com/ai4curation/eval-ont-agent-mondo/pull/175) | [attempt](attempts/pr175.md) |
| 9 | gpt-5.4 | codex | 0.003 | 0.002 | 1.000 | `b9af5d1` | [#154](https://github.com/ai4curation/eval-ont-agent-mondo/pull/154) | [attempt](attempts/pr154.md) |
| 10 | gpt-5.5 | opencode | 0.003 | 0.002 | 0.800 | `a8c0e6e` | [#88](https://github.com/ai4curation/eval-ont-agent-mondo/pull/88) | [attempt](attempts/pr88.md) |
| 11 | gpt-5.5 | opencode | 0.003 | 0.002 | 0.800 | `a8c0e6e` | [#69](https://github.com/ai4curation/eval-ont-agent-mondo/pull/69) | [attempt](attempts/pr69.md) |
| 12 | gpt-5.5 | codex | 0.003 | 0.002 | 0.800 | `a8c0e6e` | [#49](https://github.com/ai4curation/eval-ont-agent-mondo/pull/49) | [attempt](attempts/pr49.md) |
