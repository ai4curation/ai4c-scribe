---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 2967
pr_number: 3309
issue_title: T follicular helper cell logical definition using obsolete term
pr_author: gouttegd
pr_merged_at: '2025-09-09'
task_type: axiom_repair
difficulty: simple
scoping: tightly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 10
generated_at: '2026-05-17'
domain_area: immunology
best_f1: 0.5
best_model: claude-sonnet-4.5
---

# PR #3309 — T follicular helper cell logical definition using obsolete term

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #2967](https://github.com/obophenotype/cell-ontology/issues/2967) | [PR #3309](https://github.com/obophenotype/cell-ontology/pull/3309) | @gouttegd | merged 2025-09-09

`axiom_repair` `simple` `tightly_scoped` `approved_first_time`

## Context

The logical definition of T follicular helper cell referenced a deprecated GO class. When GO obsoletes a term, downstream ontologies that use it in logical axioms must update their references to the replacement term. This is a common maintenance task in the OBO ecosystem.

## Changes Made

Changed a single GO term reference in `cl-edit.owl`, replacing the obsolete GO class with its active replacement in the logical definition of T follicular helper cell. One line added, one line removed.

## Resolution

Approved on first review in a single commit. Simple difficulty because the fix is mechanical: identify the obsolete term, find its replacement, and update the reference. However, this case illustrates an important pattern for agents working with OBO ontologies: they must be able to detect and resolve obsolete cross-ontology references.

## Curation Note (data quality)

`case_quality: poor` — flagged because the metadiff score systematically
under-represents agent quality on this case (a scoring artifact, not a gold
defect; the gold PR #3309 is correct, single, and complete — issue #2967's only
actionable ask was the specific term replacement, with @addiehl twice
recommending `GO:0051024` → `GO:0002639`; the broader release-time
`deprecated_class_reference` check discussed in the thread was never converted
to a CL PR and was explicitly out of scope, exactly as gouttegd scoped #3309).

**The artifact:** The gold `EquivalentClasses(CL:0002038 ...)` axiom serializes
its two `ObjectSomeValuesFrom(obo:RO_0002215 ...)` conjuncts in sorted order —
`GO_0002639` before `GO_0045830` — because the editing tool/ROBOT normalizes
conjunct order. All 8 agents performed a literal in-place text substitution of
`GO_0051024` → `GO_0002639`, leaving the order as `GO_0045830` then
`GO_0002639`. `ObjectIntersectionOf` is commutative, so the agent and gold
axioms are **logically identical**; the line-based metadiff nonetheless scores
the changed line as a mismatch, capping F1 at **0.500** (claude/opencode runs)
and **0.333** (codex runs, additionally hit by an incidental EOF-newline
normalization producing a spurious second hunk).

**Consequence for scoring/aggregation:** All 8 attempts (claude-sonnet-4.5,
claude-opus-4.7, claude-haiku-4.5, gemma-4-31b, gpt-5.5 ×2 opencode, gpt-5.4 &
gpt-5.5 codex) are substantively **success** — every one produced the correct
biological fix with tight scope. The recorded F1 values (`best_f1: 0.5`) should
be treated as a serialization floor, not a quality signal; downstream scoring
should down-weight or exclude this case, or compare on logical/normalized-axiom
equivalence rather than line diff. A ROBOT-normalized comparison would yield
F1 ≈ 1.0 for the 6 non-codex attempts.

## Human Diff

```diff
diff --git a/src/ontology/cl-edit.owl b/src/ontology/cl-edit.owl
index c107a4bed..b63bf2eb3 100644
--- a/src/ontology/cl-edit.owl
+++ b/src/ontology/cl-edit.owl
@@ -14280,7 +14280,7 @@ AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:22552227") oboInOwl:hasR
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:22649468") oboInOwl:hasRelatedSynonym obo:CL_0002038 "follicular helper T cell")
 AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:22508770") oboInOwl:hasRelatedSynonym obo:CL_0002038 "follicular helper T-cell")
 AnnotationAssertion(rdfs:label obo:CL_0002038 "T follicular helper cell")
-EquivalentClasses(obo:CL_0002038 ObjectIntersectionOf(obo:CL_0000492 ObjectSomeValuesFrom(obo:BFO_0000051 obo:PR_000003450) ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001203) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001209) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001860) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001919) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0045830) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0051024)))
+EquivalentClasses(obo:CL_0002038 ObjectIntersectionOf(obo:CL_0000492 ObjectSomeValuesFrom(obo:BFO_0000051 obo:PR_000003450) ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001203) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001209) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001860) ObjectSomeValuesFrom(obo:RO_0002104 obo:PR_000001919) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0002639) ObjectSomeValuesFrom(obo:RO_0002215 obo:GO_0045830)))
 SubClassOf(Annotation(oboInOwl:is_inferred "true") obo:CL_0002038 obo:CL_0000492)
 SubClassOf(obo:CL_0002038 ObjectSomeValuesFrom(obo:RO_0002202 obo:CL_0000896))
 

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.500 | 0.500 | 0.500 | `b6ee438` | [#220](https://github.com/ai4curation/eval-ont-agent-cl/pull/220) | [attempt](attempts/pr220.md) |
| 2 | claude-opus-4.7 | claude | 0.500 | 0.500 | 0.500 | `b6ee438` | [#175](https://github.com/ai4curation/eval-ont-agent-cl/pull/175) | [attempt](attempts/pr175.md) |
| 3 | gemma-4-31b | opencode | 0.500 | 0.500 | 0.500 | `b6ee438` | [#105](https://github.com/ai4curation/eval-ont-agent-cl/pull/105) | [attempt](attempts/pr105.md) |
| 4 | claude-haiku-4.5 | claude | 0.500 | 0.500 | 0.500 | `b6ee438` | [#84](https://github.com/ai4curation/eval-ont-agent-cl/pull/84) | [attempt](attempts/pr84.md) |
| 5 | gpt-5.5 | opencode | 0.500 | 0.500 | 0.500 | `b6ee438` | [#56](https://github.com/ai4curation/eval-ont-agent-cl/pull/56) | [attempt](attempts/pr56.md) |
| 6 | gpt-5.5 | opencode | 0.500 | 0.500 | 0.500 | `b6ee438` | [#38](https://github.com/ai4curation/eval-ont-agent-cl/pull/38) | [attempt](attempts/pr38.md) |
| 7 | gpt-5.4 | opencode | 0.333 | 0.500 | 0.250 | `b5c2038` | [#567](https://github.com/ai4curation/eval-ont-agent-cl/pull/567) | [attempt](attempts/pr567.md) |
| 8 | gpt-5.4 | opencode | 0.333 | 0.500 | 0.250 | `b5c2038` | [#505](https://github.com/ai4curation/eval-ont-agent-cl/pull/505) | [attempt](attempts/pr505.md) |
| 9 | gpt-5.4 | codex | 0.333 | 0.500 | 0.250 | `b5c2038` | [#74](https://github.com/ai4curation/eval-ont-agent-cl/pull/74) | [attempt](attempts/pr74.md) |
| 10 | gpt-5.5 | codex | 0.333 | 0.500 | 0.250 | `b5c2038` | [#22](https://github.com/ai4curation/eval-ont-agent-cl/pull/22) | [attempt](attempts/pr22.md) |
