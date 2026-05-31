---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9798
pr_number: 10106
issue_title: '[Obsolete] glass-chapman-hockley syndrome'
pr_author: MeeSiing
pr_merged_at: '2026-04-02'
task_type: obsoletion
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 12
generated_at: '2026-05-17'
best_f1: 0.772
best_model: gpt-5.5
---

# PR #10106 — [Obsolete] glass-chapman-hockley syndrome

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9798](https://github.com/monarch-initiative/mondo/issues/9798) | [PR #10106](https://github.com/monarch-initiative/mondo/pull/10106) | @MeeSiing | merged 2026-04-02

`obsoletion` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #9798 proposed obsoleting MONDO:0023243 (Glass-Chapman-Hockley syndrome) because the matching SNOMED CT concept was retired and Orphanet evidence suggested equivalence with Muenke syndrome (MONDO:0011274). Both conditions involve FGFR3 mutations causing craniosynostosis, and the curator determined they represent the same disease entity.

## Changes Made

The PR merged MONDO:0023243 into MONDO:0011274 (Muenke syndrome) in a single commit. The 15 additions transfer metadata from the obsoleted term (synonyms including "Glass-Chapman-Hockley syndrome", cross-references, replaced_by annotation) to the Muenke syndrome entry. The 20 deletions remove the source term's active axioms and classification. The net reduction reflects that the obsoleted term's stanza shrinks more than the target grows, as some annotations were redundant.

## Resolution

Moderate difficulty because the merge decision required evaluating evidence from multiple sources (SNOMED CT retirement, Orphanet mapping, UMLS data) to confirm equivalence. Once the merge decision is made, the mechanical execution follows standard Mondo merge SOP. An agent would need access to external database lookups to validate such merge proposals.

## Curation Note (data quality)

This case is **ok** (not poor): the gold PR #10106 is the complete, reviewer-approved final resolution. But there is an important durable finding for downstream scoring/aggregation:

- **Two human PRs exist.** PR #10087 ("obsolete glass-chapman-hockley syndrome") was the curator's *first* attempt: a plain obsoletion that kept the obsoleted stanza fat and only added one EXACT synonym to Muenke. Reviewer **@sabrinatoro** rejected this approach and instructed a full **merge**; the curator closed #10087 and opened **PR #10106** (the gold), which follows the canonical Mondo `merge-terms` SOP (obsoleted stanza reduced to id/name/`IAO:0000231 MONDO:TermsMerged`/issue link/`is_obsolete`/`replaced_by`; synonyms + xrefs transferred to MONDO:0011274 with `MONDO:equivalentObsolete`).
- **The issue text is misleading by itself.** Issue #9798 says "[Obsolete]" and "Suggested term to consider", which an agent reasonably reads as a pure obsoletion. The 10 attempts split bimodally: **full-merge** attempts (gpt-5.5/codex #100 F1 0.765, gpt-5.4/codex #165 0.716, opus-4.7 #375 0.706, and the partial gpt-5.5/opencode #135/#116 0.772) vs **obsolete-only** attempts that reproduced the *repudiated* PR #10087 pattern (haiku #424/#293 0.600, copilot/sonnet #335 0.561, claude/sonnet #434 0.500). The metadiff ordering is meaningful and correctly rewards the merge.
- **Metadiff still under-represents the best merge attempts.** #100/#165/#375 made defensible curatorial choices that differ from gold without being wrong: keeping transferred synonyms at `RELATED` (gold promotes to `EXACT`), citing `[Orphanet:1535]` rather than gold's `[PMID:20108486]`, and (for #165/#375) deliberately dropping the retired `xref: SCTID:720814001` which gold instead retains as `MONDO:equivalentObsolete`. Gold additionally makes issue-unrelated incidental edits to Muenke (`MNKES` RELATED→EXACT ABBREVIATION; deleting synonym "Muenke nonsyndromic coronal craniosynostosis"; adding `subset: inferred_rare`) that cap even a well-scoped agent below F1=1.0.
- **Recurring agent error to track:** four lower-tier attempts fabricated the non-existent xref qualifier `MONDO:obsoleteEquivalent` (correct value is `MONDO:equivalentObsolete`), and used the generic obsoletion reason `OMO:0001000` instead of the merge-specific `MONDO:TermsMerged`.

Flagged by claude-opus-4.7, 2026-05-15.

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index e6a3057543..dc8b5b6e0c 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -285337,6 +285337,7 @@ subset: clingen {source="MONDO:CLINGEN"}
 subset: doid {source="DOID:0060703"}
 subset: doid_rare {source="DOID:0060703"}
 subset: gard_rare {source="GARD:0007097", source="MONDO:GARD"}
+subset: inferred_rare
 subset: ncit {source="NCIT:C84904"}
 subset: ncit_rare {source="NCIT:C84904"}
 subset: nord_rare {source="MONDO:NORD"}
@@ -285347,9 +285348,13 @@ subset: orphanet {source="Orphanet:53271"}
 subset: orphanet_rare {source="Orphanet:53271"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
+synonym: "craniosynostosis - dysmorphism - brachydactyly" EXACT [GARD:0002479]
+synonym: "craniosynostosis brachydactyly" EXACT [GARD:0002479]
+synonym: "craniosynostosis with facial dysmorphism and brachydactyly syndrome" EXACT [Orphanet:1535]
+synonym: "craniosynostosis-dysmorphism-brachydactyly syndrome" EXACT [GARD:0002479]
 synonym: "FGFR3-related craniosynostosis" EXACT [DOID:0060703, NCIT:C84904]
-synonym: "MNKES" RELATED ABBREVIATION [MONDO:Lexical]
-synonym: "Muenke nonsyndromic coronal craniosynostosis" RELATED []
+synonym: "glass-chapman-hockley syndrome" EXACT [PMID:20108486]
+synonym: "MNKES" EXACT ABBREVIATION [MONDO:Lexical]
 synonym: "Muenke syndrome" EXACT [DOID:0060703, icd11.foundation:1860572017, MONDO:Lexical, NCIT:C84904, OMIM:602849, Orphanet:53271]
 synonym: "syndrome of coronal craniosynostosis" RELATED [GARD:0007097]
 xref: DOID:0060703 {source="MONDO:equivalentTo"}
@@ -285360,8 +285365,10 @@ xref: MEDGEN:355217 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}
 xref: MESH:C537369 {source="Orphanet:53271/e", source="MONDO:equivalentTo", source="DOID:0060703", source="Orphanet:53271"}
 xref: NCIT:C84904 {source="MONDO:equivalentTo"}
 xref: OMIM:602849 {source="Orphanet:53271/e", source="MONDO:equivalentTo", source="DOID:0060703", source="Orphanet:53271"}
+xref: Orphanet:1535 {source="GARD:0002479", source="MONDO:equivalentObsolete"}
 xref: Orphanet:53271 {source="MONDO:equivalentTo", source="DOID:0060703", source="OMIM:602849"}
 xref: SCTID:440350001 {source="MONDO:equivalentTo"}
+xref: SCTID:720814001 {source="MONDO:equivalentObsolete"}
 xref: UMLS:C1864436 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:355217"}
 is_a: MONDO:0002254 {source="MONDO:Redundant", source="NCIT:C84904", source="https://orcid.org/0000-0002-4142-7153"} ! syndromic disease
 is_a: MONDO:0015338 {source="Orphanet:53271", source="PMID:31633310"} ! syndromic craniosynostosis
@@ -285371,6 +285378,8 @@ relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/
 property_value: curated_content_resource "https://www.malacards.org/card/muenke_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/4948" xsd:anyURI
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/6751" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9798" xsd:anyURI
+property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/2479/glass-chapman-hockley-syndrome" xsd:anyURI {source="GARD:0002479"}
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/7097/muenke-syndrome" xsd:anyURI {source="GARD:0007097"}
 
 [Term]
@@ -540186,25 +540195,11 @@ property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/2471/giganti
 
 [Term]
 id: MONDO:0023243
-name: glass-chapman-hockley syndrome
-def: "The Glass-Chapman-Hockley syndrome is a very rare disease. To date, the syndrome has only been reported in one family with five members affected in three generations. The first patients were two brothers that had an abnormally-shaped head due to coronal craniosynostosis. Their mother, maternal aunt, and maternal grandmother were also found to have the syndrome. The signs and symptoms varied from person to person; however, the signs and symptoms included coronal craniosynostosis, small middle part of the face (midfacial hypoplasia), and short fingers (brachydactyly).The inheritance is thought to be autosomal dominant. No genes have been identified for this syndrome. Treatment included surgery to correct the craniosynostosis. No issues with development and normal intelligence were reported. This is an n-of-1 use case where only one patient or family has been described with this disorder." [GARD:0002479]
-comment: This term is scheduled for obsoletion based on the fact that it is a historical diseaseAfter obsoletion, this term will not have a replacement ID, but one could consider the following term: Muenke syndrome-MONDO:0011274
-subset: inferred_rare
-subset: n_of_one
-subset: obsoletion_candidate
-subset: rare
-synonym: "craniosynostosis - dysmorphism - brachydactyly" RELATED [GARD:0002479]
-synonym: "craniosynostosis brachydactyly" RELATED [GARD:0002479]
-synonym: "craniosynostosis with facial dysmorphism and brachydactyly syndrome" EXACT []
-synonym: "craniosynostosis-dysmorphism-brachydactyly syndrome" RELATED [GARD:0002479]
-synonym: "glass chapman hockley syndrome" RELATED []
-xref: Orphanet:1535 {source="GARD:0002479", source="MONDO:equivalentObsolete"}
-xref: SCTID:720814001 {source="MONDO:equivalentTo"}
-is_a: MONDO:0000426 ! autosomal dominant disease
-is_a: MONDO:0015469 {source="Orphanet:1535/inferred"} ! craniosynostosis
+name: obsolete glass-chapman-hockley syndrome
+property_value: IAO:0000231 MONDO:TermsMerged
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9798" xsd:anyURI
-property_value: IAO:0006012 "2026-02-01" xsd:string
-property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/2479/glass-chapman-hockley-syndrome" xsd:anyURI {source="GARD:0002479"}
+is_obsolete: true
+replaced_by: MONDO:0011274
 
 [Term]
 id: MONDO:0023246

```

## Agent Attempts (12)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.5 | opencode | 0.772 | 0.629 | 1.000 | `9a96c3b` | [#135](https://github.com/ai4curation/eval-ont-agent-mondo/pull/135) | [attempt](attempts/pr135.md) |
| 2 | gpt-5.5 | opencode | 0.772 | 0.629 | 1.000 | `9a96c3b` | [#116](https://github.com/ai4curation/eval-ont-agent-mondo/pull/116) | [attempt](attempts/pr116.md) |
| 3 | gpt-5.5 | codex | 0.765 | 0.743 | 0.788 | `b9c8dbd` | [#100](https://github.com/ai4curation/eval-ont-agent-mondo/pull/100) | [attempt](attempts/pr100.md) |
| 4 | gpt-5.4 | codex | 0.716 | 0.686 | 0.750 | `9e72765` | [#165](https://github.com/ai4curation/eval-ont-agent-mondo/pull/165) | [attempt](attempts/pr165.md) |
| 5 | claude-opus-4.7 | claude | 0.706 | 0.686 | 0.727 | `8ef7f87` | [#375](https://github.com/ai4curation/eval-ont-agent-mondo/pull/375) | [attempt](attempts/pr375.md) |
| 6 | kimi-k2.6 | opencode | 0.621 | 0.514 | 0.783 | `1f596cc` | [#247](https://github.com/ai4curation/eval-ont-agent-mondo/pull/247) | [attempt](attempts/pr247.md) |
| 7 | claude-haiku-4.5 | claude | 0.600 | 0.514 | 0.720 | `dd5bee2` | [#424](https://github.com/ai4curation/eval-ont-agent-mondo/pull/424) | [attempt](attempts/pr424.md) |
| 8 | claude-haiku-4.5 | claude | 0.600 | 0.514 | 0.720 | `dd5bee2` | [#293](https://github.com/ai4curation/eval-ont-agent-mondo/pull/293) | [attempt](attempts/pr293.md) |
| 9 | gpt-5.4 | opencode | 0.593 | 0.457 | 0.842 | `b9c6c2b` | [#735](https://github.com/ai4curation/eval-ont-agent-mondo/pull/735) | [attempt](attempts/pr735.md) |
| 10 | gpt-5.4 | opencode | 0.593 | 0.457 | 0.842 | `b9c6c2b` | [#680](https://github.com/ai4curation/eval-ont-agent-mondo/pull/680) | [attempt](attempts/pr680.md) |
| 11 | claude-sonnet-4.5 | copilot | 0.561 | 0.457 | 0.727 | `8919301` | [#335](https://github.com/ai4curation/eval-ont-agent-mondo/pull/335) | [attempt](attempts/pr335.md) |
| 12 | claude-sonnet-4.5 | claude | 0.500 | 0.400 | 0.667 | `f607b76` | [#434](https://github.com/ai4curation/eval-ont-agent-mondo/pull/434) | [attempt](attempts/pr434.md) |
