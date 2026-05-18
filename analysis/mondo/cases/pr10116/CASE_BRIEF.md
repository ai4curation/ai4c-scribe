---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9854
pr_number: 10116
issue_title: Isolated megalencephaly Orphanet Xref
pr_author: MeeSiing
pr_merged_at: '2026-04-08'
task_type: other
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: changes_requested
num_agent_attempts: 11
generated_at: '2026-05-17'
best_f1: 0.944
best_model: gpt-5.4
---

# PR #10116 — Isolated megalencephaly Orphanet Xref

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9854](https://github.com/monarch-initiative/mondo/issues/9854) | [PR #10116](https://github.com/monarch-initiative/mondo/pull/10116) | @MeeSiing | merged 2026-04-08

`other` `medium` `tightly_scoped` `changes_requested`

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

## Agent Attempts (11)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.944 | 0.944 | 0.944 | `aee5774` | [#743](https://github.com/ai4curation/eval-ont-agent-mondo/pull/743) | [attempt](attempts/pr743.md) |
| 2 | gpt-5.4 | opencode | 0.944 | 0.944 | 0.944 | `aee5774` | [#689](https://github.com/ai4curation/eval-ont-agent-mondo/pull/689) | [attempt](attempts/pr689.md) |
| 3 | kimi-k2.6 | opencode | 0.941 | 0.889 | 1.000 | `d4a0c0b` | [#277](https://github.com/ai4curation/eval-ont-agent-mondo/pull/277) | [attempt](attempts/pr277.md) |
| 4 | claude-sonnet-4.5 | claude | 0.895 | 0.944 | 0.850 | `da7fd42` | [#457](https://github.com/ai4curation/eval-ont-agent-mondo/pull/457) | [attempt](attempts/pr457.md) |
| 5 | gemma-4-31b | opencode | 0.882 | 0.833 | 0.938 | `0167ac1` | [#228](https://github.com/ai4curation/eval-ont-agent-mondo/pull/228) | [attempt](attempts/pr228.md) |
| 6 | gpt-5.5 | opencode | 0.759 | 0.611 | 1.000 | `97c80df` | [#723](https://github.com/ai4curation/eval-ont-agent-mondo/pull/723) | [attempt](attempts/pr723.md) |
| 7 | gpt-5.5 | opencode | 0.759 | 0.611 | 1.000 | `97c80df` | [#668](https://github.com/ai4curation/eval-ont-agent-mondo/pull/668) | [attempt](attempts/pr668.md) |
| 8 | gpt-5.5 | codex | 0.759 | 0.611 | 1.000 | `9350695` | [#559](https://github.com/ai4curation/eval-ont-agent-mondo/pull/559) | [attempt](attempts/pr559.md) |
| 9 | gpt-5.4 | codex | 0.667 | 0.611 | 0.733 | `77cc9f3` | [#575](https://github.com/ai4curation/eval-ont-agent-mondo/pull/575) | [attempt](attempts/pr575.md) |
| 10 | claude-opus-4.7 | claude | 0.286 | 0.167 | 1.000 | `d488c97` | [#385](https://github.com/ai4curation/eval-ont-agent-mondo/pull/385) | [attempt](attempts/pr385.md) |
| 11 | claude-haiku-4.5 | claude | 0.200 | 0.111 | 1.000 | `c7d8a48` | [#319](https://github.com/ai4curation/eval-ont-agent-mondo/pull/319) | [attempt](attempts/pr319.md) |
