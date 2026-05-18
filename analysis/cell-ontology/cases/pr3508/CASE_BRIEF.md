---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3460
pr_number: 3508
issue_title: NTR - Prehypertrophic chondrocyte (preHTCs)
pr_author: app/copilot-swe-agent
pr_merged_at: '2025-12-15'
task_type: new_term
difficulty: medium
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-17'
domain_area: skeletal
best_f1: 0.625
best_model: claude-opus-4.7
---

# PR #3508 — NTR - Prehypertrophic chondrocyte (preHTCs)

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3460](https://github.com/obophenotype/cell-ontology/issues/3460) | [PR #3508](https://github.com/obophenotype/cell-ontology/pull/3508) | @app/copilot-swe-agent | merged 2025-12-15

`new_term` `medium` `tightly_scoped` `approved_first_time`

## Context

A new term was requested for the prehypertrophic chondrocyte (preHTC), a distinct stage in the chondrocyte maturation sequence within the growth plate. Prehypertrophic chondrocytes are located between the proliferative zone and the hypertrophic zone and are characterized by exit from the cell cycle and the onset of Indian hedgehog (Ihh) expression. This term complements the existing hypertrophic chondrocyte (CL:0000743) and the newly added terms for the chondrocyte lineage.

## Changes Made

Added 10 new lines to `cl-edit.owl` defining the prehypertrophic chondrocyte with class declaration, label, textual definition referencing the growth plate zonal organization, subClassOf axiom under chondrocyte, and logical axioms capturing the cell's anatomical location and developmental stage markers.

## Resolution

Approved on first review after 7 commits. Medium difficulty because correctly positioning this cell type requires understanding the spatial and temporal sequence of chondrocyte maturation in endochondral ossification: resting -> proliferative -> prehypertrophic -> hypertrophic.

## Curation Note (data quality)

**Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-16.** This is a single-PR resolution (gold PR #3508, no companion PRs), so it is *not* a partial-gold case. However, the metadiff F1/precision/recall is a poor proxy for agent quality here for three reasons:

1. **Placeholder-vs-canonical CL ID artifact.** The gold PR introduced the term under the temporary ID `CL_9900000` (from `idrange:81`, the NTR range). The ODK release pipeline subsequently renamed it to the canonical `CL:0020022`, which is what OLS and current `cl-edit.owl` carry today (with the exact gold definition, contributor, synonym, and axioms). The choice of temp-ID *number* is curatorially immaterial — it is overwritten at release. Yet agents that selected a different valid temp ID (`CL_9900001`: attempts pr212, pr101) or the eventual canonical ID (`CL_0020022`: attempt pr30) score F1=0.000 across the board, even when the ontology content is otherwise correct. The metadiff is keyed entirely to the gold's arbitrary `CL_9900000`.

2. **Biologically inverted gold relation.** The gold (and the released ontology) asserts `SubClassOf(CL_9900000 ObjectSomeValuesFrom(RO:0002207 CL_0000743))`. `RO:0002207` = "directly develops from", so this reads "prehypertrophic chondrocyte *directly develops from* hypertrophic chondrocyte" — the biological inverse of the issue's explicit request, "develops directly into 'hypertrophic chondrocyte'" (preHTC matures *into* the hypertrophic cell, not from it). Agents that used `RO:0002203` ("develops into": pr181, pr67, pr47, pr212) or `RO:0002210` ("directly develops into": pr30) are biologically *more* faithful to the issue, yet the metadiff penalizes them for not matching the likely-erroneous gold axiom. The curators reviewed and shipped the gold axiom, but it is very probably a curation error.

3. **Config-mandated metadata absent from gold.** The agent `CLAUDE.md` requires `terms:date`, `terms:creator "GitHub Copilot"`, and an `IAO:0000233` term-tracker axiom on new terms. The gold PR includes none of these. Compliant agents are therefore penalized on precision for following their instructions.

**Recommendation for downstream scoring:** down-weight or exclude metadiff for this case. On substance, attempt pr181 (claude-opus-4.7) is a clear success, pr212 (claude-sonnet-4.5) is substantively near-correct (only an arbitrary temp-ID difference), and pr30 (gpt-5.5/codex) is ontologically the most biologically accurate despite an ID-minting instruction violation — all of which the F1 numbers (0.625 / 0.000 / 0.000) badly under-represent.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index e5192d5f3..29248e718 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -3286,6 +3286,7 @@ Declaration(Class(obo:CL_7770003))
 Declaration(Class(obo:CL_7770004))
 Declaration(Class(obo:CL_7770005))
 Declaration(Class(obo:CL_7770006))
+Declaration(Class(obo:CL_9900000))
 Declaration(Class(obo:CP_0000000))
 Declaration(Class(obo:CP_0000025))
 Declaration(Class(obo:CP_0000027))
@@ -10182,6 +10183,15 @@ AnnotationAssertion(rdfs:label obo:CL_0000742 "periarticular chondrocyte")
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0000742 obo:CL_0000138)
 SubClassOf(obo:CL_0000742 ObjectSomeValuesFrom(obo:BFO_0000050 obo:UBERON_0010996))
 
+# Class: obo:CL_9900000 (prehypertrophic chondrocyte)
+
+AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:29985449") Annotation(oboInOwl:hasDbXref "PMID:31871141") Annotation(oboInOwl:hasDbXref "PMID:34137454") obo:IAO_0000115 obo:CL_9900000 "A post-proliferative chondrocyte in the prehypertrophic zone of the cartilage tissue, located between the proliferative and hypertrophic zones. This cell is characterised by increased cell volume and expression of Indian Hedgehog (Ihh), PTH1R, and Runx2/3 in both humans and mice (Hallett et al., 2021). It coordinates the PTHrP-Ihh feedback loop that regulates chondrocyte differentiation and functions as a signalling hub for communication between proliferative chondrocytes, hypertrophic chondrocytes, and periosteal osteoblasts (Hallett et al., 2021).")
+AnnotationAssertion(terms:contributor obo:CL_9900000 <https://orcid.org/0009-0000-8480-9277>)
+AnnotationAssertion(Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasRelatedSynonym obo:CL_9900000 "preHTC")
+AnnotationAssertion(rdfs:label obo:CL_9900000 "prehypertrophic chondrocyte")
+SubClassOf(obo:CL_9900000 obo:CL_0000138)
+SubClassOf(obo:CL_9900000 ObjectSomeValuesFrom(obo:RO_0002207 obo:CL_0000743))
+
 # Class: obo:CL_0000743 (hypertrophic chondrocyte)
 
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "GO_REF:0000034") Annotation(oboInOwl:hasDbXref "PMID:15951842") Annotation(oboInOwl:hasDbXref "PMID:25321476") Annotation(oboInOwl:hasDbXref "PMID:35179487") obo:IAO_0000115 obo:CL_0000743 "A chondrocyte that is part of the hypertrophic cartilage zone. This cell is significantly enlarged and characterised by high expression of type X collagen (COL10A1) in both humans and mice. It actively coordinates endochondral ossification by mineralising the extracellular matrix, attracting blood vessels via angiogenic signalling, and mediating the transition from cartilage to bone - often by transdifferentiating into an osteoblast rather than undergoing apoptosis.")

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-opus-4.7 | claude | 0.625 | 0.714 | 0.556 | `94ee5fb` | [#181](https://github.com/ai4curation/eval-ont-agent-cl/pull/181) | [attempt](attempts/pr181.md) |
| 2 | gpt-5.5 | opencode | 0.500 | 0.571 | 0.444 | `6dfcce1` | [#67](https://github.com/ai4curation/eval-ont-agent-cl/pull/67) | [attempt](attempts/pr67.md) |
| 3 | gpt-5.5 | opencode | 0.500 | 0.571 | 0.444 | `6dfcce1` | [#47](https://github.com/ai4curation/eval-ont-agent-cl/pull/47) | [attempt](attempts/pr47.md) |
| 4 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `48c713c` | [#579](https://github.com/ai4curation/eval-ont-agent-cl/pull/579) | [attempt](attempts/pr579.md) |
| 5 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `48c713c` | [#516](https://github.com/ai4curation/eval-ont-agent-cl/pull/516) | [attempt](attempts/pr516.md) |
| 6 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | `135325f` | [#294](https://github.com/ai4curation/eval-ont-agent-cl/pull/294) | [attempt](attempts/pr294.md) |
| 7 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `f8068ee` | [#212](https://github.com/ai4curation/eval-ont-agent-cl/pull/212) | [attempt](attempts/pr212.md) |
| 8 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `feb2bd6` | [#101](https://github.com/ai4curation/eval-ont-agent-cl/pull/101) | [attempt](attempts/pr101.md) |
| 9 | gpt-5.5 | codex | 0.000 | 0.000 | 0.000 | `4ed552f` | [#30](https://github.com/ai4curation/eval-ont-agent-cl/pull/30) | [attempt](attempts/pr30.md) |
