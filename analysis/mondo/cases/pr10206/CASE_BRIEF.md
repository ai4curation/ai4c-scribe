---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9892
pr_number: 10206
issue_title: chronic myelogenous leukemia, BCR-ABL1 positive
pr_author: MeeSiing
pr_merged_at: '2026-04-30'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 17
generated_at: '2026-05-17'
scoping_notes: Changes limited to relabeling one term and updating its synonyms.
domain_area: oncology
best_f1: 0.769
best_model: gpt-5.4
---

# PR #10206 — chronic myelogenous leukemia, BCR-ABL1 positive

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9892](https://github.com/monarch-initiative/mondo/issues/9892) | [PR #10206](https://github.com/monarch-initiative/mondo/pull/10206) | @MeeSiing | merged 2026-04-30

`synonym_update` `simple` `tightly_scoped` `changes_requested`

## Context

A request was made to relabel MONDO:0011996 to "chronic myeloid leukemia" to better align with OMIM's naming ("leukemia, chronic myeloid"). The existing label "chronic myelogenous leukemia, BCR-ABL1 positive" was considered overly specific for the primary label, as the BCR-ABL1 qualifier could be captured as a synonym instead.

The PR involved some discussion about how strictly Mondo should follow OMIM naming conventions, reflected in the 3 commits needed to finalize the label.

## Changes Made

Relabeled MONDO:0011996 from "chronic myelogenous leukemia, BCR-ABL1 positive" to "chronic myeloid leukemia" in `src/ontology/mondo-edit.obo`. The old label and variations were preserved as synonyms. The 7 additions and 8 deletions reflect the label change plus synonym adjustments across 3 commits.

## Resolution

Easy difficulty overall, though it required a minor judgment call about naming conventions. The multiple commits suggest some back-and-forth about the exact label wording. An agent would need to understand Mondo's relationship with OMIM naming and when to simplify versus preserve qualifier terms.

## Curation Note (data quality)

*Added by claude-opus-4.7, 2026-05-15.*

This is flagged `case_quality: poor` because the gold PR over-reaches the issue,
making metadiff F1 a poor proxy for the well-scoped attempts.

**What issue #9892 actually asked for** (verified against the issue body and the only
PR resolving it, #10206 — there are no companion PRs): (1) relabel MONDO:0011996 to
"chronic myeloid leukemia"; (2) keep "chronic myelogenous leukemia, BCR-ABL1 positive"
as a synonym. The issue body cites three source URLs (cancer.gov, medlineplus.gov,
cancer.org).

**What gold PR #10206 additionally did, none of it requested by the issue:**

- Repointed the existing `synonym: "chronic myeloid leukemia" EXACT` xref list from
  `[DOID:8552, NCIT:C3174, Orphanet:521]` to additionally include the three issue
  URLs **plus the human curator's own ORCID** `https://orcid.org/0000-0001-9310-0163`
  (the ORCID is not derivable from the issue by any agent).
- Deleted `synonym: "leukemia, chronic myeloid" RELATED []`,
  `synonym: "leukemia, chronic myeloid, Philadelphia chromosome positive, somatic"
  EXACT []`, and `synonym: "leukemia, Philadelphia chromosome-positive, resistant to
  imatinib, Somatic mutation" EXACT []`.
- Added `synonym: "leukimia, chronic myeloid" EXACT [OMIM:608232]` — a verbatim,
  typo-bearing OMIM-pipeline synonym introduced by the PR's "normalize to fix failed
  qc" / "fix failed qc of double genes" commits, not a curation decision tied to the
  issue.

**Consequence for scoring.** Every well-scoped attempt is capped at ~0.769 F1 purely
because it (correctly) did not reproduce this gold-only OMIM/QC churn. The four 0.769
runs (#520, #488, #397, #251) and the four 0.741 runs (#435, #82, #63, #44) are
substantively correct, complete, tightly scoped solutions to the *issue*; their F1
**under-represents** quality. #251 (kimi-k2.6) is the strongest — it actually read the
issue's cited URLs and migrated them onto the synonym, matching gold's intent.

Conversely, the two gemma-4-31b runs (#291, #206, F1=0.211) are **genuinely
incomplete**, not metadiff victims: they skipped the three `is_a` referrer comment
updates and the `IAO:0000233` term-tracker item, left an EXACT synonym identical to the
new primary label (a likely Mondo QC failure), and made inaccurate self-reports
("moved to synonyms list" when no synonym was added). For these runs the low F1 is
representative. Downstream aggregation should down-weight the 0.769/0.741 cap as a gold
artifact but treat the gemma gap as real.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424f..29e09aaed4 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -133431,7 +133431,7 @@ xref: SCTID:413656006 {source="MONDO:equivalentTo"}
 xref: UMLS:C0005699 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:2281"}
 is_a: MONDO:0005059 {source="EFO:1000131", source="MESH:D001752/inferred", source="NCIT:C9110/inferred"} ! leukemia
 is_a: MONDO:0005170 {source="EFO:1000131", source="NCIT:C9110/inferred"} ! myeloid neoplasm
-is_a: MONDO:0011996 {source="NCIT:C9110"} ! chronic myelogenous leukemia, BCR-ABL1 positive
+is_a: MONDO:0011996 {source="NCIT:C9110"} ! chronic myeloid leukemia
 
 [Term]
 id: MONDO:0006116
@@ -262021,7 +262021,7 @@ xref: MEDGEN:325075 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:C536093 {source="MONDO:equivalentTo"}
 xref: OMIM:600080 {source="DOID:0060761", source="MONDO:equivalentTo"}
 xref: UMLS:C1838670 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:325075"}
-is_a: MONDO:0011996 {source="DOID:0060761"} ! chronic myelogenous leukemia, BCR-ABL1 positive
+is_a: MONDO:0011996 {source="DOID:0060761"} ! chronic myeloid leukemia
 property_value: curated_content_resource "https://www.malacards.org/card/myelocytic_leukemia_like_syndrome_familial_chronic" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/10141/myelocytic-leukemia-like-syndrome-familial-chronic" xsd:anyURI {source="GARD:0010141"}
 
@@ -293841,7 +293841,7 @@ property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/
 
 [Term]
 id: MONDO:0011996
-name: chronic myelogenous leukemia, BCR-ABL1 positive
+name: chronic myeloid leukemia
 def: "A chronic myeloproliferative neoplasm characterized by the expression of the BCR-ABL1 fusion gene. It presents with neutrophilic leukocytosis. It can appear at any age, but it mostly affects middle aged and older individuals. Patients usually present with fatigue, weight loss, anemia, night sweats, and splenomegaly. If untreated, it follows a biphasic or triphasic natural course; an initial indolent chronic phase which is followed by an accelerated phase, a blast phase, or both. Allogeneic stem cell transplantation and tyrosine kinase inhibitors delay disease progression and prolong overall survival." [NCIT:C3174]
 subset: doid {source="DOID:0081088", source="DOID:8552"}
 subset: doid_rare {source="DOID:8552"}
@@ -293864,15 +293864,13 @@ synonym: "chronic myelogenous leukemia" EXACT [DOID:8552, NCIT:C3174, Orphanet:5
 synonym: "chronic myelogenous leukemia (CML)" EXACT [NCIT:C3174]
 synonym: "chronic myelogenous leukemia, BCR-ABL1 Positive" EXACT [DOID:0081088, NCIT:C3174]
 synonym: "chronic myelogenous leukemias" EXACT [NCIT:C3174]
-synonym: "chronic myeloid leukemia" EXACT [DOID:8552, NCIT:C3174, Orphanet:521]
+synonym: "chronic myeloid leukemia" EXACT [DOID:8552, https://medlineplus.gov/genetics/condition/chronic-myeloid-leukemia/#synonyms, https://orcid.org/0000-0001-9310-0163, https://www.cancer.gov/types/leukemia/patient/cml-treatment-pdq, https://www.cancer.org/cancer/types/chronic-myeloid-leukemia/about/what-is-cml.html, NCIT:C3174, Orphanet:521]
 synonym: "CML" EXACT ABBREVIATION [DOID:8552, NCIT:C3174, OMIM:608232, Orphanet:521]
 synonym: "CML - chronic myelogenous leukaemia" EXACT OMO:0003005 []
 synonym: "CML - chronic myelogenous leukemia" EXACT [DOID:8552, NCIT:C3174]
 synonym: "hematopoeitic - chronic myelocytic leukaemia (CML)" EXACT OMO:0003005 []
 synonym: "hematopoeitic - chronic myelocytic leukemia (CML)" EXACT [NCIT:C3174]
-synonym: "leukemia, chronic myeloid" RELATED []
-synonym: "leukemia, chronic myeloid, Philadelphia chromosome positive, somatic" EXACT []
-synonym: "leukemia, Philadelphia chromosome-positive, resistant to imatinib, Somatic mutation" EXACT []
+synonym: "leukimia, chronic myeloid" EXACT [OMIM:608232]
 synonym: "myeloid leukemia, chronic" EXACT [DOID:8552, MONDO:patterns/chronic, MTH:NOCODE]
 xref: DOID:0081088 {source="MONDO:equivalentTo", source="MONDO:preferredExternal"}
 xref: DOID:8552 {source="MONDO:equivalentTo", source="EFO:0000339"}
@@ -293903,6 +293901,7 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: curated_content_resource "https://www.malacards.org/card/chronic_myelogenous_leukemia_bcr_abl1_positive" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: curated_content_resource "https://www.malacards.org/card/leukemia_chronic_myeloid" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4521" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9892" xsd:anyURI
 
 [Term]
 id: MONDO:0011997
@@ -512035,7 +512034,7 @@ xref: MESH:D015465 {source="UMLS:C0023472", source="MONDO:equivalentTo"}
 xref: NCIT:C3173 {source="UMLS:C0023472", source="MONDO:equivalentTo", source="https://orcid.org/0000-0002-5002-8648"}
 xref: SCTID:413389003 {source="UMLS:C0023472"}
 xref: UMLS:C0023472 {source="MEDGEN:6059", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
-is_a: MONDO:0011996 {source="UMLS:C0023472"} ! chronic myelogenous leukemia, BCR-ABL1 positive
+is_a: MONDO:0011996 {source="UMLS:C0023472"} ! chronic myeloid leukemia
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/8567" xsd:anyURI
 
 [Term]

```

## Agent Attempts (17)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | codex | 0.769 | 0.667 | 0.909 | `4bcd24d` | [#568](https://github.com/ai4curation/eval-ont-agent-mondo/pull/568) | [attempt](attempts/pr568.md) |
| 2 | claude-sonnet-4.5 | copilot | 0.769 | 0.667 | 0.909 | `e3e3dd9` | [#520](https://github.com/ai4curation/eval-ont-agent-mondo/pull/520) | [attempt](attempts/pr520.md) |
| 3 | claude-sonnet-4.5 | copilot | 0.769 | 0.667 | 0.909 | `e3e3dd9` | [#488](https://github.com/ai4curation/eval-ont-agent-mondo/pull/488) | [attempt](attempts/pr488.md) |
| 4 | claude-opus-4.7 | claude | 0.769 | 0.667 | 0.909 | `4514441` | [#397](https://github.com/ai4curation/eval-ont-agent-mondo/pull/397) | [attempt](attempts/pr397.md) |
| 5 | kimi-k2.6 | opencode | 0.769 | 0.667 | 0.909 | `c5db975` | [#251](https://github.com/ai4curation/eval-ont-agent-mondo/pull/251) | [attempt](attempts/pr251.md) |
| 6 | claude-sonnet-4.5 | claude | 0.741 | 0.667 | 0.833 | `65a5b11` | [#435](https://github.com/ai4curation/eval-ont-agent-mondo/pull/435) | [attempt](attempts/pr435.md) |
| 7 | gpt-5.5 | opencode | 0.741 | 0.667 | 0.833 | `65a5b11` | [#82](https://github.com/ai4curation/eval-ont-agent-mondo/pull/82) | [attempt](attempts/pr82.md) |
| 8 | gpt-5.5 | opencode | 0.741 | 0.667 | 0.833 | `65a5b11` | [#63](https://github.com/ai4curation/eval-ont-agent-mondo/pull/63) | [attempt](attempts/pr63.md) |
| 9 | gpt-5.5 | codex | 0.741 | 0.667 | 0.833 | `fc7a3ab` | [#44](https://github.com/ai4curation/eval-ont-agent-mondo/pull/44) | [attempt](attempts/pr44.md) |
| 10 | claude-haiku-4.5 | claude | 0.720 | 0.600 | 0.900 | `97c8008` | [#599](https://github.com/ai4curation/eval-ont-agent-mondo/pull/599) | [attempt](attempts/pr599.md) |
| 11 | gpt-5.4 | opencode | 0.400 | 0.267 | 0.800 | `b55172e` | [#756](https://github.com/ai4curation/eval-ont-agent-mondo/pull/756) | [attempt](attempts/pr756.md) |
| 12 | gpt-5.4 | opencode | 0.400 | 0.267 | 0.800 | `b55172e` | [#703](https://github.com/ai4curation/eval-ont-agent-mondo/pull/703) | [attempt](attempts/pr703.md) |
| 13 | gpt-5.4 | codex | 0.400 | 0.267 | 0.800 | `6c971b8` | [#14](https://github.com/ai4curation/eval-ont-agent-mondo/pull/14) | [attempt](attempts/pr14.md) |
| 14 | gpt-5.4 | codex | 0.400 | 0.267 | 0.800 | `bc85eb4` | [#5](https://github.com/ai4curation/eval-ont-agent-mondo/pull/5) | [attempt](attempts/pr5.md) |
| 15 | claude-haiku-4.5 | claude | 0.400 | 0.267 | 0.800 | `866cca0` | [#3](https://github.com/ai4curation/eval-ont-agent-mondo/pull/3) | [attempt](attempts/pr3.md) |
| 16 | gemma-4-31b | opencode | 0.211 | 0.133 | 0.500 | `faea8f9` | [#291](https://github.com/ai4curation/eval-ont-agent-mondo/pull/291) | [attempt](attempts/pr291.md) |
| 17 | gemma-4-31b | opencode | 0.211 | 0.133 | 0.500 | `faea8f9` | [#206](https://github.com/ai4curation/eval-ont-agent-mondo/pull/206) | [attempt](attempts/pr206.md) |
