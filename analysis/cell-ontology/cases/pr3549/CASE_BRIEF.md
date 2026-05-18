---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3346
pr_number: 3549
issue_title: Revise intraepithelial lymphocyte and subclasses
pr_author: copilot-swe-agent
pr_merged_at: '2026-02-18'
task_type: axiom_repair
difficulty: hard
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 6
generated_at: '2026-05-17'
domain_area: immunology
best_f1: 0.615
best_model: claude-opus-4.7
---

# PR #3549 — Revise intraepithelial lymphocyte and subclasses

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3346](https://github.com/obophenotype/cell-ontology/issues/3346) | [PR #3549](https://github.com/obophenotype/cell-ontology/pull/3549) | @copilot-swe-agent | merged 2026-02-18

`axiom_repair` `hard` `tightly_scoped` `approved_first_time`

## Context

The intraepithelial lymphocyte (IEL) term (CL:0002496) was incorrectly restricted to intestinal epithelium only. In reality, IELs are found throughout mucosal epithelia including gastrointestinal, respiratory, and reproductive tracts. The definition needed broadening to reflect the true biological scope, and a new intestinal-specific subclass was needed for backward compatibility.

## Changes Made

Modified `cl-edit.owl` with 15 additions and 2 deletions. The changes broaden the IEL definition to encompass all epithelial tissues, remove the intestinal-specific restriction from the parent term, and add a new "intestinal intraepithelial lymphocyte" subclass to preserve the original narrower concept.

## Resolution

Approved on first review. Hard difficulty because this requires: (1) understanding mucosal immunology well enough to know IELs exist outside the gut, (2) correctly broadening a definition without breaking existing annotations, (3) creating a subclass to preserve backward compatibility, and (4) ensuring the logical axioms correctly reflect the broader anatomical scope.

## Curation Note (data quality)

Flagged `case_quality: poor` (quality_flagged_by: claude-opus-4.7, 2026-05-16).
This is a single-PR resolution (gold #3549 fully covers issue #3346; no companion
PRs), so there is no multi-PR fragmentation. The poor flag is for **metadiff
scoring artifacts** that make F1 a misleading quality proxy here:

- **Placeholder-vs-canonical CL ID artifact**: the issue requires minting a new
  `intestinal intraepithelial lymphocyte` term. Gold minted `CL_9900000`. The agent
  cannot predict which placeholder/canonical ID the curators will assign:
  sonnet-4.5 (eval PR #207) used `CL_9900000` and matched by convention; haiku-4.5
  (eval PR #144) used `CL_9900001` and is penalized across the entire subclass block
  for an ID it had no way to know.
- **OWL serialization / xref-placement convention**: both attempts add the
  issue-requested `WIKIPEDIA:Intraepithelial_lymphocyte` (sonnet) as a top-level
  `AnnotationAssertion(oboInOwl:hasDbXref ...)` line, whereas gold embeds it as an
  axiom-annotation inside the IAO_0000115 definition. Same content, different line
  shape — line-oriented metadiff penalizes it.
- **Gold term-tracker misattribution**: gold's `AnnotationAssertion(obo:IAO_0000233
  obo:CL_9900000 "https://github.com/.../issues/3455")` points to issue **#3455**,
  not the actual issue **#3346**. Reproducing gold faithfully on this field is not
  the quality target; sonnet's use of #3346 is arguably more correct.

Net: eval PR #207 (sonnet-4.5) is a substantively correct/complete resolution
scored `success` (F1=0.615 under-represents). Eval PR #144 (haiku-4.5) is
`partial_success` — core axiom repair correct, but it omitted the explicitly
requested WIKIPEDIA xref on both terms, omitted the ORCID contributor on the
broadened parent, and introduced an `is_inferred="true"` modeling error on the new
asserted subclass edge (real defects, not artifacts). Downstream aggregation should
down-weight the line-level F1 for this case and use the substance assessment in the
per-attempt reviews.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index f3b8d2f57..7adcc8e0c 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3299,6 +3299,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -19298,15 +19299,16 @@ SubClassOf(obo:CL_0002495 obo:CL_0000746)
 
 # Class: obo:CL_0002496 (intraepithelial lymphocyte)
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "MP:0008894") obo:IAO_0000115 obo:CL_0002496 "A T cell that is located in the intestinal epithelium and is capable of a mucosal immune response.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GOC:tfm") Annotation(oboInOwl:hasDbXref "MP:0008894") Annotation(oboInOwl:hasDbXref "PMID:29674648") Annotation(oboInOwl:hasDbXref "WIKIPEDIA:Intraepithelial_lymphocyte") obo:IAO_0000115 obo:CL_0002496 "A tissue-resident lymphocyte located within the epithelial layer of mucosal tissues, particularly within the gastrointestinal, respiratory, and reproductive tracts. Characterised by permanent residency, this cell typically expresses CD103 (integrin alpha-E), which binds to E-cadherin on epithelial cells, enabling epithelial retention in both mice and humans. Phenotypically, IEL displays an activated, antigen-experienced state characterised by the constitutive expression of cytotoxic molecules (granzyme B, perforin) and innate-like receptors (such as NKG2D), enabling rapid, localised surveillance and immediate response to epithelial stress.")
 AnnotationAssertion(terms:contributor obo:CL_0002496 <https://orcid.org/0000-0003-1980-3228>)
+AnnotationAssertion(terms:contributor obo:CL_0002496 <https://orcid.org/0009-0000-8480-9277>)
 AnnotationAssertion(oboInOwl:creation_date obo:CL_0002496 "2010-12-07T09:54:50Z"^^xsd:dateTime)
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0002496 "MESH:D000075942")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002496 "IEL")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002496 "intraepithelial T cell")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0002496 "intraepithelial T-cell")
 AnnotationAssertion(rdfs:label obo:CL_0002496 "intraepithelial lymphocyte")
-EquivalentClasses(obo:CL_0002496 ObjectIntersectionOf(obo:CL_0002419 ObjectSomeValuesFrom(obo:RO_0001025 obo:UBERON_0001277) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0002385)))
+EquivalentClasses(obo:CL_0002496 ObjectIntersectionOf(obo:CL_0002419 ObjectSomeValuesFrom(obo:RO_0001025 obo:UBERON_0000483) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0002385)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0002496 obo:CL_0002419)
 
 # Class: obo:CL_0002497 (primary trophoblast giant cell)
@@ -35627,6 +35629,17 @@ SubClassOf(obo:CL_7770006 obo:CL_0002367)
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_9606))
 SubClassOf(obo:CL_7770006 ObjectSomeValuesFrom(obo:RO_0002292 obo:PR_Q9UIK5))
 
+# Class: obo:CL_9900000 (intestinal intraepithelial lymphocyte)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:29674648") Annotation(oboInOwl:hasDbXref "WIKIPEDIA:Intraepithelial_lymphocyte") obo:IAO_0000115 obo:CL_9900000 "A T cell that is located in the intestinal epithelium and is capable of a mucosal immune response.")
+AnnotationAssertion(obo:IAO_0000233 obo:CL_9900000 "https://github.com/obophenotype/cell-ontology/issues/3455")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(terms:creator obo:CL_9900000 "GitHub Copilot")
+AnnotationAssertion(terms:date obo:CL_9900000 "2026-01-05T11:44:26Z"^^xsd:dateTime)
+AnnotationAssertion(rdfs:label obo:CL_9900000 "intestinal intraepithelial lymphocyte")
+EquivalentClasses(obo:CL_9900000 ObjectIntersectionOf(obo:CL_0002419 ObjectSomeValuesFrom(obo:RO_0001025 obo:UBERON_0001277) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0002385)))
+SubClassOf(obo:CL_9900000 obo:CL_0002496)
+
 # Class: obo:CP_0000000 (obsolete CP:0000000)
 
 AnnotationAssertion(obo:IAO_0100001 obo:CP_0000000 obo:CL_0017500)

```

## Agent Attempts (6)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.615 | 0.667 | 0.571 | `2d0a27b` | [#476](https://github.com/ai4curation/eval-ont-agent-cl/pull/476) | [attempt](attempts/pr476.md) |
| 2 | claude-sonnet-4.5 | claude | 0.615 | 0.667 | 0.571 | `ecd7923` | [#207](https://github.com/ai4curation/eval-ont-agent-cl/pull/207) | [attempt](attempts/pr207.md) |
| 3 | gpt-5.5 | opencode | 0.593 | 0.667 | 0.533 | `2484338` | [#547](https://github.com/ai4curation/eval-ont-agent-cl/pull/547) | [attempt](attempts/pr547.md) |
| 4 | gpt-5.5 | opencode | 0.593 | 0.667 | 0.533 | `2484338` | [#487](https://github.com/ai4curation/eval-ont-agent-cl/pull/487) | [attempt](attempts/pr487.md) |
| 5 | claude-haiku-4.5 | claude | 0.261 | 0.250 | 0.273 | `2bd94c2` | [#144](https://github.com/ai4curation/eval-ont-agent-cl/pull/144) | [attempt](attempts/pr144.md) |
| 6 | gpt-5.4 | codex | 0.222 | 0.250 | 0.200 | `aba5ac6` | [#287](https://github.com/ai4curation/eval-ont-agent-cl/pull/287) | [attempt](attempts/pr287.md) |
