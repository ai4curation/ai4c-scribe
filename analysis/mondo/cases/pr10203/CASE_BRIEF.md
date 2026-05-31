---
ontology: mondo
repo: monarch-initiative/mondo
issue_number: 9882
pr_number: 10203
issue_title: 'Request for new synonyms to: arhinia, choanal atresia, and microphthalmia
  MONDO:0011323'
pr_author: MeeSiing
pr_merged_at: '2026-04-30'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 10
generated_at: '2026-05-17'
best_f1: 1.0
best_model: gpt-5.4
---

# PR #10203 — Request for new synonyms to: arhinia, choanal atresia, and microphthalmia MONDO:0011323

**mondo** | [monarch-initiative/mondo](https://github.com/monarch-initiative/mondo) | [Issue #9882](https://github.com/monarch-initiative/mondo/issues/9882) | [PR #10203](https://github.com/monarch-initiative/mondo/pull/10203) | @MeeSiing | merged 2026-04-30

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

Issue #9882 requested adding new synonyms to MONDO:0011323 (arhinia, choanal atresia, and microphthalmia). The requested synonyms included longer descriptive forms such as "Arhinia, choanal atresia, microphthalmia, and hypogonadotropic hypogonadism" that capture the full phenotypic spectrum of this SMCHD1-related condition.

## Changes Made

The PR added 6 synonym lines to MONDO:0011323 in mondo-edit.obo with no deletions. Each synonym was annotated with appropriate scope (EXACT) and evidence. The additions capture variant clinical descriptions of this complex congenital syndrome that combines craniofacial and endocrine features.

## Resolution

Simple difficulty as a pure additive synonym change. The curator needed to verify each requested synonym was appropriate for EXACT scope and add proper evidence annotations. An agent could handle this by parsing the issue template, extracting requested synonyms, and generating the correct OBO synonym syntax with appropriate xref evidence.

## Curation Note (data quality)

This is **not** a poor evaluation case under the Step 3a/3b criteria: PR #10203
is a single PR that fully resolves issue #9882 (`close #9882`), there are no
companion PRs, no eval base-state contamination, the gold was not
curator-repudiated, and there is no out-of-scope extra edit. `case_quality`
remains `ok`.

However, metadiff F1 is an unusually poor proxy for quality on this case, and
its ranking actively **inverts** true quality, so downstream aggregation should
prefer the narrative reviews over the numeric scores:

- The 7 requested synonyms reduce to 5 genuinely new ones (one is the primary
  label "Arhinia, choanal atresia, and microphthalmia"; one,
  "Hyposmia-nasal and ocular hypoplasia-hypogonadotropic hypogonadism syndrome",
  already exists EXACT).
- Gold (#10203) added exactly those 5, evidencing each with the **requester's
  ORCID** `https://orcid.org/0000-0001-9310-0163` (+ OMIM:603457 where
  applicable) — the Mondo convention for attributing community-submitted
  synonyms — plus a single `property_value: IAO:0000233 ".../issues/9882"`
  term-tracker line.
- Metadiff scores synonym additions partly on evidence-bracket content. No
  agent guessed the submitter-ORCID provenance, so even substantively perfect
  synonym lines fail to match. The only line any agent could match
  byte-for-byte is the IAO term tracker.
- Consequence: the best-scoped attempt, #398 (claude-opus-4.7), added exactly
  the right 5 synonyms with perfect scope discipline but omitted the term
  tracker, scoring F1=0.000 — identical to a no-op. Weaker attempts
  (over-editing, redundant synonyms) score *higher* purely because they
  happened to also add the matching term-tracker line. F1 rank order is
  therefore anti-correlated with curation quality here.

Recommended treatment: judge attempts on synonym substance, scope discipline,
and whether the IAO term tracker was added — not on F1. Substantive ranking of
this set is approximately: #398 ≈ #455 (most complete) > #278 (rigorous but
under-delivered) > #316 > #557 (most over-editing / non-standard evidence).

_Flagged by claude-opus-4.7, 2026-05-15._

## Human Diff

```diff
diff --git a/src/ontology/mondo-edit.obo b/src/ontology/mondo-edit.obo
index 1d63d0424f..ca564db144 100644
--- a/src/ontology/mondo-edit.obo
+++ b/src/ontology/mondo-edit.obo
@@ -275792,15 +275792,20 @@ subset: orphanet_rare {source="Orphanet:2250"}
 subset: otar {source="MONDO:OTAR"}
 subset: rare
 synonym: "arhinia choanal atresia microphthalmia" EXACT [GARD:0008755]
+synonym: "arhinia, choanal atresia, microphthalmia, and hypogonadotropic hypogonadism" EXACT [https://orcid.org/0000-0001-9310-0163, OMIM:603457]
 synonym: "arrhinia-choanal atresia-microphthalmia syndrome" EXACT [MONDO:0015238]
+synonym: "BAM syndrome" EXACT [https://orcid.org/0000-0001-9310-0163, OMIM:603457]
 synonym: "BAMS" EXACT ABBREVIATION [OMIM:603457]
 synonym: "Bosma Arhinia Microphthalmia Syndrome" EXACT [NORD:1909, OMIM:603457]
 synonym: "Bosma arhinia microphthalmia syndrome" EXACT [GARD:0008755, OMIM:603457]
 synonym: "Bosma arhinia-microphthalmia syndrome" EXACT [Orphanet:2250]
 synonym: "Bosma Henkin Christiansen syndrome" EXACT [GARD:0008755]
+synonym: "Bosma syndrome" EXACT [https://orcid.org/0000-0001-9310-0163, OMIM:603457]
 synonym: "Bosma-Henkin-Christiansen syndrome" EXACT [Orphanet:2250]
 synonym: "congenital absence of nose and anterior nasopharynx" RELATED [GARD:0008755]
+synonym: "Gifford-Bosma syndrome" EXACT [https://orcid.org/0000-0001-9310-0163]
 synonym: "hyposmia-nasal and ocular hypoplasia-hypogonadotropic hypogonadism syndrome" EXACT [MONDO:0016393, Orphanet:2250]
+synonym: "Ruprecht Majewski syndrome" EXACT [https://orcid.org/0000-0001-9310-0163, OMIM:603457]
 xref: GARD:0027263 {source="MONDO:GARD"}
 xref: ICD10CM:Q87.0 {source="Orphanet:1135"}
 xref: ICD10CM:Q87.8 {source="Orphanet:2250"}
@@ -275818,6 +275823,7 @@ relationship: curated_content_resource https://search.clinicalgenome.org/kb/cond
 relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/29090 {source="OMIM:603457"} ! SMCHD1
 property_value: curated_content_resource "https://www.malacards.org/card/bosma_arhinia_microphthalmia_syndrome" xsd:anyURI {source="MONDO:MalaCards"}
 property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/7813" xsd:anyURI
+property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9882" xsd:anyURI
 property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/8755/arhinia-choanal-atresia-microphthalmia" xsd:anyURI {source="GARD:0008755"}
 
 [Term]

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 1.000 | 1.000 | 1.000 | `ca564db` | [#754](https://github.com/ai4curation/eval-ont-agent-mondo/pull/754) | [attempt](attempts/pr754.md) |
| 2 | gpt-5.4 | opencode | 1.000 | 1.000 | 1.000 | `ca564db` | [#701](https://github.com/ai4curation/eval-ont-agent-mondo/pull/701) | [attempt](attempts/pr701.md) |
| 3 | kimi-k2.6 | opencode | 0.222 | 0.167 | 0.333 | `137bd53` | [#278](https://github.com/ai4curation/eval-ont-agent-mondo/pull/278) | [attempt](attempts/pr278.md) |
| 4 | gpt-5.5 | opencode | 0.200 | 0.167 | 0.250 | `628479d` | [#720](https://github.com/ai4curation/eval-ont-agent-mondo/pull/720) | [attempt](attempts/pr720.md) |
| 5 | gpt-5.5 | opencode | 0.200 | 0.167 | 0.250 | `628479d` | [#666](https://github.com/ai4curation/eval-ont-agent-mondo/pull/666) | [attempt](attempts/pr666.md) |
| 6 | gpt-5.4 | codex | 0.167 | 0.167 | 0.167 | `2cc7def` | [#573](https://github.com/ai4curation/eval-ont-agent-mondo/pull/573) | [attempt](attempts/pr573.md) |
| 7 | claude-sonnet-4.5 | claude | 0.154 | 0.167 | 0.143 | `7bc233a` | [#455](https://github.com/ai4curation/eval-ont-agent-mondo/pull/455) | [attempt](attempts/pr455.md) |
| 8 | gpt-5.5 | codex | 0.143 | 0.167 | 0.125 | `cdd2df1` | [#557](https://github.com/ai4curation/eval-ont-agent-mondo/pull/557) | [attempt](attempts/pr557.md) |
| 9 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `5287c2d` | [#398](https://github.com/ai4curation/eval-ont-agent-mondo/pull/398) | [attempt](attempts/pr398.md) |
| 10 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `c86ffa9` | [#316](https://github.com/ai4curation/eval-ont-agent-mondo/pull/316) | [attempt](attempts/pr316.md) |
