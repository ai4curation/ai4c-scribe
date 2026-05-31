---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3523
pr_number: 3524
issue_title: Revise textual definition of Retinal Ganglion Cell A into Alpha retinal
  ganglion cell
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-02-17'
task_type: other
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-17'
domain_area: neuroscience
best_f1: 0.667
best_model: claude-opus-4.7
---

# PR #3524 — Revise textual definition of Retinal Ganglion Cell A into Alpha retinal ganglion cell

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3523](https://github.com/obophenotype/cell-ontology/issues/3523) | [PR #3524](https://github.com/obophenotype/cell-ontology/pull/3524) | @app/copilot-swe-agent | merged 2026-02-17

`other` `simple` `tightly_scoped` `approved_first_time`

## Context

CL_0004117 was labeled "Retinal Ganglion Cell A" using an older naming convention. Issue #3523 requested renaming it to "alpha retinal ganglion cell (Mmus)" to align with current RGC nomenclature and to make the mouse-specific taxon scope explicit. This is part of the broader RGC refactoring effort (epic #2844) to modernize retinal ganglion cell terminology in CL.

## Changes Made

Updated `cl-edit.owl` with 4 additions and 3 deletions: the primary label was changed from "Retinal Ganglion Cell A" to "alpha retinal ganglion cell (Mmus)", the textual definition was revised to reference the alpha RGC classification and its large soma size and brisk transient responses, and a species-specific qualifier was added.

## Resolution

Approved on first review despite requiring 14 commits to finalize. Simple difficulty because the change is primarily a label and definition text update following the RGC nomenclature standardization pattern established across the series.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16.**

This is a single-PR resolution (search of issue #3523 / "alpha retinal
ganglion cell" returns only #3524 as the resolving PR — no companion PRs),
so it is **not** a multi-PR partial-gold case. However it is a poor
*evaluation* case because the gold label was renegotiated after the agents'
information cut-off:

- Issue #3523 explicitly states `**Revised cell label** alpha retinal
  ganglion cell` and supplies the exact definition text and references.
- The gold PR #3524 was initially built to exactly that spec (label =
  "alpha retinal ganglion cell"). Then on 2025-12-15 curator RiveraAndrea83
  left a PR comment: *"@copilot please change label to: alpha retinal
  ganglion cell (Mmus)"*, and Copilot amended the label in commit 120a536.
- The `(Mmus)` species qualifier therefore appears in the gold diff but is
  **not present anywhere in the issue** the eval agents were given. No agent
  relying only on the issue could produce it.

Consequence: the metadiff F1 ceiling for this case is ~0.571 (gemma-4-31b)
and the two claude attempts land at 0.429, even though **all three attempts
correctly and faithfully implement every change the issue actually
requested**. The residual gap is the renegotiated label, an en-dash vs hyphen
typographic difference in `non[-/–]direction-selective`, synonym casing
("Retinal ganglion cell A" vs gold's lowercased "retinal ganglion cell A"),
and (sonnet only) one unrequested `terms:date` annotation.

Recommendation for downstream scoring: treat metadiff for this case as a
**lower bound**; the substantive outcome for all three attempts is
`success` against the issue as written. Down-weight or exclude this case from
F1-based aggregation, or re-score against the issue spec rather than the
post-comment gold label.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index 0a225c81e..123d89816 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -21741,17 +21741,18 @@ AnnotationAssertion(rdfs:label obo:CL_0004116 "retinal ganglion cell C")
 SubClassOf(obo:CL_0004116 obo:CL_0000740)
 SubClassOf(obo:CL_0004116 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))
 
-# Class: obo:CL_0004117 (retinal ganglion cell A)
+# Class: obo:CL_0004117 (alpha retinal ganglion cell (Mmus))
 
-AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:12209831") obo:IAO_0000115 obo:CL_0004117 "A monostratified retinal ganglion cell with large soma and large dendritic field.")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:28753612") obo:IAO_0000115 obo:CL_0004117 "A large-bodied retinal projection neuron with wide monostratified dendritic arbors in defined IPL strata, high neurofilament and osteopontin expression, and a thick, fast-conducting axon. It shows short-latency, non-direction-selective responses with large receptive fields and a distinctive rapid action potential waveform. In mammals it forms about five percent of RGCs and includes four conserved ON and OFF sustained and transient subtypes.")
 AnnotationAssertion(terms:contributor obo:CL_0004117 "https://orcid.org/0000-0001-7258-9596")
 AnnotationAssertion(terms:contributor obo:CL_0004117 "https://orcid.org/0000-0002-5260-9315")
 AnnotationAssertion(oboInOwl:hasDbXref obo:CL_0004117 "BAMS:1009")
 AnnotationAssertion(oboInOwl:hasExactSynonym obo:CL_0004117 "alpha cell")
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:12209831") oboInOwl:hasExactSynonym obo:CL_0004117 "retinal ganglion cell A")
 AnnotationAssertion(oboInOwl:hasOBONamespace obo:CL_0004117 "cell")
 AnnotationAssertion(oboInOwl:id obo:CL_0004117 "CL:0004117")
 AnnotationAssertion(rdfs:comment obo:CL_0004117 "This group includes all of the large bodied/large field RGCs in the rat. Group RGA cells have large somata (15 to 39 micrometers in diameter) and large, radially branching dendritic fields (235 to 748 micrometers in diameter), and many exhibit tracer coupling.")
-AnnotationAssertion(rdfs:label obo:CL_0004117 "retinal ganglion cell A")
+AnnotationAssertion(rdfs:label obo:CL_0004117 "alpha retinal ganglion cell (Mmus)")
 SubClassOf(obo:CL_0004117 obo:CL_0000740)
 SubClassOf(obo:CL_0004117 ObjectSomeValuesFrom(obo:RO_0000053 obo:PATO_0070063))
 SubClassOf(obo:CL_0004117 ObjectSomeValuesFrom(obo:RO_0002162 obo:NCBITaxon_10090))

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.667 | 0.571 | 0.800 | `393f9a3` | [#475](https://github.com/ai4curation/eval-ont-agent-cl/pull/475) | [attempt](attempts/pr475.md) |
| 2 | gemma-4-31b | opencode | 0.571 | 0.571 | 0.571 | `ebc9dfc` | [#120](https://github.com/ai4curation/eval-ont-agent-cl/pull/120) | [attempt](attempts/pr120.md) |
| 3 | claude-sonnet-4.5 | claude | 0.429 | 0.429 | 0.429 | `47f4a71` | [#198](https://github.com/ai4curation/eval-ont-agent-cl/pull/198) | [attempt](attempts/pr198.md) |
| 4 | claude-haiku-4.5 | claude | 0.429 | 0.429 | 0.429 | `ba136d0` | [#140](https://github.com/ai4curation/eval-ont-agent-cl/pull/140) | [attempt](attempts/pr140.md) |
| 5 | gpt-5.4 | opencode | 0.375 | 0.429 | 0.333 | `79b0ce9` | [#578](https://github.com/ai4curation/eval-ont-agent-cl/pull/578) | [attempt](attempts/pr578.md) |
| 6 | gpt-5.4 | opencode | 0.375 | 0.429 | 0.333 | `79b0ce9` | [#518](https://github.com/ai4curation/eval-ont-agent-cl/pull/518) | [attempt](attempts/pr518.md) |
| 7 | gpt-5.5 | opencode | 0.353 | 0.429 | 0.300 | `bff85a1` | [#543](https://github.com/ai4curation/eval-ont-agent-cl/pull/543) | [attempt](attempts/pr543.md) |
| 8 | gpt-5.5 | opencode | 0.353 | 0.429 | 0.300 | `bff85a1` | [#481](https://github.com/ai4curation/eval-ont-agent-cl/pull/481) | [attempt](attempts/pr481.md) |
| 9 | gpt-5.4 | codex | 0.353 | 0.429 | 0.300 | `3f3ee54` | [#321](https://github.com/ai4curation/eval-ont-agent-cl/pull/321) | [attempt](attempts/pr321.md) |
