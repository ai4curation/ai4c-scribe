---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3559
pr_number: 3564
issue_title: '[Synonym] abbreviations like PBMC'
pr_author: RiveraAndrea83
pr_merged_at: '2026-02-06'
task_type: synonym_update
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 7
generated_at: '2026-05-17'
domain_area: cell-biology
best_f1: 0.0
best_model: gpt-5.4
---

# PR #3564 — [Synonym] abbreviations like PBMC

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3559](https://github.com/obophenotype/cell-ontology/issues/3559) | [PR #3564](https://github.com/obophenotype/cell-ontology/pull/3564) | @RiveraAndrea83 | merged 2026-02-06

`synonym_update` `simple` `tightly_scoped` `approved_first_time`

## Context

A community request asked for standard abbreviations to be added as synonyms for commonly referenced cell types. Specifically, PBMC (peripheral blood mononuclear cell) and WBC (white blood cell / leukocyte) are widely used abbreviations in clinical and research literature that were missing from the ontology.

## Changes Made

Added 3 exact synonym annotations to `cl-edit.owl`: "PBMC" for peripheral blood mononuclear cell (CL:2000001) with a literature reference, and "WBC" for leukocyte (CL:0000738). Each synonym includes appropriate database cross-references.

## Resolution

Approved on first review. This is a straightforward synonym addition requiring knowledge of OWL synonym annotation patterns (exact vs. related scope) and proper cross-referencing. An agent would need to identify the correct terms and apply the right synonym type with provenance.

## Curation Note (data quality)

Flagged by claude-opus-4.7 on 2026-05-16 during attempt review.

**Gold PR is valid and complete.** PR #3564 is the sole human resolution of
issue #3559: a single PR by RiveraAndrea83, approved first-time by dosumis,
adding all three requested synonyms. There are no companion PRs. The issue
explicitly requested PBMC, WBC, **and RPE**, and curators addiehl and scheuerm
confirmed all three (RPE specifically approved for CL:0002586). So this is NOT
a Step 3a multi-PR partial-gold case, and NOT a Step 3b poor case — gold is
correct, complete, in-scope, and curator-approved. `case_quality: ok`.

**Metadiff under-represents agent quality (scoring caveat).** All three gold
lines carry axiom annotations:
`AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:...") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasExactSynonym obo:CL_xxxx "ABBR")`
— PMID:40794848 (WBC/CL:0000738), PMID:35835183 (RPE/CL:0002586),
PMID:27696124 (PBMC/CL:2000001). Both agent attempts (#210 sonnet-4.5, #149
haiku-4.5) added the correct three abbreviations to the correct three terms
with the correct `hasExactSynonym` scope, but as bare assertions without the
PMID xref or OMO_0003000 synonym type. Because zero agent lines match a gold
line byte-for-byte, metadiff returns F1=precision=recall=0.0 by construction.
This is a real omission (the issue asked for "reference(s)" and the
cl-agent-config CLAUDE.md demonstrates the exact OMO_0003000 pattern), so
both attempts are scored `partial_success` (~70% correct substance), not
`failure`. Aggregations should not read F1=0.0 here as "agent did nothing."

**CASE_BRIEF text inaccuracy (informational).** The auto-generated
CASE_BRIEF.md (and the Context/Changes Made prose mirrored above) describes
the gold as adding only PBMC and WBC (2 terms), omitting RPE for CL:0002586.
The actual gold PR diff and the issue both cover all three. CASE_BRIEF.md is
derived/auto-generated and was not edited; this note records the discrepancy
for downstream consumers.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 0e1a96337..decb9fc0f 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -10147,6 +10147,7 @@ AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0000738 "MESH:D007962")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0000738 "NCIT:C12529")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000738 "leucocyte")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0000738 "white blood cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:40794848") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasExactSynonym obo:CL_0000738 "WBC")
 AnnotationAssertion(oboInOwl:hasRelatedSynonym obo:CL_0000738 "immune cell")
 AnnotationAssertion(rdfs:label obo:CL_0000738 "leukocyte")
 EquivalentClasses(obo:CL_0000738 ObjectIntersectionOf(obo:CL_0000988 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0002505) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0001667)))
@@ -20133,6 +20134,7 @@ AnnotationAssertion(terms:contributor obo:CL_0002586 <https://orcid.org/0000-000
 AnnotationAssertion(oboInOwl:creation_date obo:CL_0002586 "2011-03-06T03:37:09Z"^^xsd:dateTime)
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0002586 "BTO:0004910")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0002586 "FMA:75802")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:35835183") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasExactSynonym obo:CL_0002586 "RPE")
 AnnotationAssertion(rdfs:label obo:CL_0002586 "retinal pigment epithelial cell")
 EquivalentClasses(obo:CL_0002586 ObjectIntersectionOf(obo:CL_0000066 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0001782)))
 SubClassOf(obo:CL_0002586 obo:CL_0000149)
@@ -29105,6 +29107,7 @@ EquivalentClasses(obo:CL_2000000 ObjectIntersectionOf(obo:CL_0000148 ObjectSomeV
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:TermGenie") obo:IAO_0000115 obo:CL_2000001 "A leukocyte with a single non-segmented nucleus in the mature form found in the circulatory pool of blood.")
 AnnotationAssertion(terms:contributor obo:CL_2000001 <http://www.wikidata.org/entity/Q35563349>)
 AnnotationAssertion(oboInOwl:creation_date obo:CL_2000001 "2014-02-11T17:29:04Z"^^xsd:dateTime)
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:27696124") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasExactSynonym obo:CL_2000001 "PBMC")
 AnnotationAssertion(oboInOwl:id obo:CL_2000001 "CL:2000001")
 AnnotationAssertion(rdfs:label obo:CL_2000001 "peripheral blood mononuclear cell")
 EquivalentClasses(obo:CL_2000001 ObjectIntersectionOf(obo:CL_0000842 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0000178)))

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `54d61fe` | [#590](https://github.com/ai4curation/eval-ont-agent-cl/pull/590) | [attempt](attempts/pr590.md) |
| 2 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `01f8370` | [#552](https://github.com/ai4curation/eval-ont-agent-cl/pull/552) | [attempt](attempts/pr552.md) |
| 3 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `54d61fe` | [#529](https://github.com/ai4curation/eval-ont-agent-cl/pull/529) | [attempt](attempts/pr529.md) |
| 4 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `01f8370` | [#491](https://github.com/ai4curation/eval-ont-agent-cl/pull/491) | [attempt](attempts/pr491.md) |
| 5 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | `138cb33` | [#291](https://github.com/ai4curation/eval-ont-agent-cl/pull/291) | [attempt](attempts/pr291.md) |
| 6 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `6da6106` | [#210](https://github.com/ai4curation/eval-ont-agent-cl/pull/210) | [attempt](attempts/pr210.md) |
| 7 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `86c7e41` | [#149](https://github.com/ai4curation/eval-ont-agent-cl/pull/149) | [attempt](attempts/pr149.md) |
