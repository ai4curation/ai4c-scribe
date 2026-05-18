---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3458
pr_number: 3505
issue_title: NTR Fibrochondrocyte progenitor cell (FCP)
pr_author: app/copilot-swe-agent
pr_merged_at: '2025-12-11'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-17'
domain_area: skeletal
best_f1: 0.696
best_model: claude-sonnet-4.5
---

# PR #3505 — NTR Fibrochondrocyte progenitor cell (FCP)

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3458](https://github.com/obophenotype/cell-ontology/issues/3458) | [PR #3505](https://github.com/obophenotype/cell-ontology/pull/3505) | @app/copilot-swe-agent | merged 2025-12-11

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term request was filed for the fibrochondrocyte progenitor cell (FCP), a precursor cell that gives rise to fibrochondrocytes in fibrocartilaginous tissues such as the meniscus and temporomandibular joint disc. This term is part of a broader effort to populate the chondrocyte and cartilage cell branches of CL, complementing related terms like fibrochondrocyte (CL_4072104) added in PR #3467.

## Changes Made

Added 14 new lines to `cl-edit.owl` defining the FCP term with appropriate class declaration, label, textual definition referencing the progenitor-to-fibrochondrocyte differentiation pathway, parentage linking it to both progenitor cell and the chondrocyte lineage, and logical axioms capturing its developmental potential.

## Resolution

Approved on first review after 8 commits of iterative refinement. Medium difficulty because correctly modeling a progenitor cell requires establishing the develops_into relationship to the mature fibrochondrocyte and positioning the term appropriately within both the progenitor cell hierarchy and the cartilage cell lineage.

## Curation Note (data quality)

`quality_flagged_by: claude-opus-4.7` · `quality_flagged_at: 2026-05-16`

This is **not** a poor evaluation case: gold PR #3505 is the single, complete,
merged human resolution of issue #3458 (confirmed via `gh search prs --repo
obophenotype/cell-ontology 3458` → only #3505; PR metadata shows files_changed =
src/ontology/cl-edit.owl only). No base-state contamination, no gold leakage, no
curator repudiation, no multi-PR partial gold, no metadiff-blind gold field.
Marked `case_quality: ok`.

Two durable scoring caveats nonetheless make the F1 numbers misleading and
should down-weight metadiff-based aggregation for this case:

1. **Placeholder-vs-canonical CL ID artifact.** Gold (Copilot-authored, merged)
   allocated `CL_9900000`. The agent config mandates the CL_99xxxxx range but
   agents cannot know which exact free offset the human picked. Attempts pr100
   (`CL_9900001`) and pr29 (`CL_9900001`) used in-range but offset IDs; pr66/pr48
   (`CL_0020021`) used a different range entirely. All four score F1=precision=
   recall=0.000 by whole-line metadiff purely because the subject IRI differs on
   every line. pr100 (claude-haiku-4.5) is in fact the **closest model to gold**
   of all six attempts (correct conservative parentage, no marker axioms) yet
   scores 0.000 — a stark metadiff under-representation. Only pr230 and pr280
   (both `CL_9900000`) get non-zero F1.

2. **Gold omitted issue-requested marker axioms.** The issue explicitly asked
   for `expresses some` COL1A1, COL3A1, MCAM/CD146, MYLK. Reviewer @dosumis
   raised that the in-vitro colony-forming/multi-lineage text was "too in vitro
   (non-canonical) for a CL def"; gold responded conservatively — split that
   text to an `rdfs:comment` and added **no** `RO_0002292` marker axioms at all.
   Gold also added a reciprocal `SubClassOf(CL_4072104 RO_0002202 some
   CL_9900000)` (fibrochondrocyte develops_from FCP) which no agent reproduced
   (the issue author said they would add it themselves later). Agents that
   formalized the requested markers (all except pr100) therefore lose recall
   against the conservative gold despite doing arguably more complete,
   issue-faithful work.

Net: judge attempts on substance (cell model correctness, parentage, location,
synonym/definition fidelity, modeling pattern) against the issue, not on the
metadiff F1. Reviews in `analysis/cell-ontology/results/reviews/pr{230,280,100,
66,48,29}-claude-complete.md` grade accordingly.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 7bcf184f9..ead4ebcf5 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3285,6 +3285,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -35330,6 +35331,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(ob
 AnnotationAssertion(rdfs:label obo:CL_4072104 "fibrochondrocyte")
 EquivalentClasses(obo:CL_4072104 ObjectIntersectionOf(obo:CL_0000138 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001995)))
 SubClassOf(obo:CL_4072104 obo:CL_0002320)
+SubClassOf(obo:CL_4072104 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_9900000))
 SubClassOf(obo:CL_4072104 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003264))
 SubClassOf(obo:CL_4072104 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003328))
 SubClassOf(obo:CL_4072104 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_000003353))
@@ -35385,6 +35387,18 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (fibrochondrocyte progenitor cell)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasDbXref "PMID:36338137") obo:IAO_0000115 obo:CL_9900000 "A mesenchymal progenitor cell located in fibrocartilaginous tissues, along the fibrochondrocytic differentiation pathway that co-expresses both fibrochondrocyte markers (COL1A1, COL3A1) and mesenchymal stem cell markers (MCAM/CD146, MYLK) in humans. This cell serves as a progenitor for mature fibrochondrocytes and other meniscal cell types, with differentiation regulated by TGF-β signaling, focal adhesion, and extracellular matrix-receptor interaction pathways.")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900000 "FCP")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:31871141") rdfs:comment obo:CL_9900000 "A fibrochondrocyte progenitor cell demonstrates colony-forming capacity and multi-lineage differentiation potential toward osteogenic and adipogenic lineages.")
+AnnotationAssertion(rdfs:label obo:CL_9900000 "fibrochondrocyte progenitor cell")
+SubClassOf(obo:CL_9900000 obo:CL_0008019)
+SubClassOf(obo:CL_9900000 obo:CL_0011026)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001995))
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.696 | 0.727 | 0.667 | `92da4d4` | [#230](https://github.com/ai4curation/eval-ont-agent-cl/pull/230) | [attempt](attempts/pr230.md) |
| 2 | claude-opus-4.7 | claude | 0.615 | 0.727 | 0.533 | `960b14c` | [#280](https://github.com/ai4curation/eval-ont-agent-cl/pull/280) | [attempt](attempts/pr280.md) |
| 3 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `f51e8c8` | [#574](https://github.com/ai4curation/eval-ont-agent-cl/pull/574) | [attempt](attempts/pr574.md) |
| 4 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `f51e8c8` | [#515](https://github.com/ai4curation/eval-ont-agent-cl/pull/515) | [attempt](attempts/pr515.md) |
| 5 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | `b9e2b80` | [#333](https://github.com/ai4curation/eval-ont-agent-cl/pull/333) | [attempt](attempts/pr333.md) |
| 6 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `67c802e` | [#100](https://github.com/ai4curation/eval-ont-agent-cl/pull/100) | [attempt](attempts/pr100.md) |
| 7 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `8e94f3f` | [#66](https://github.com/ai4curation/eval-ont-agent-cl/pull/66) | [attempt](attempts/pr66.md) |
| 8 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `8e94f3f` | [#48](https://github.com/ai4curation/eval-ont-agent-cl/pull/48) | [attempt](attempts/pr48.md) |
| 9 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | `66a3b1b` | [#29](https://github.com/ai4curation/eval-ont-agent-cl/pull/29) | [attempt](attempts/pr29.md) |
