---
ontology: uberon
repo: obophenotype/uberon
issue_number: 2421
pr_number: 3659
issue_title: multicellular organism and organism substance should be disjoint
pr_author: matentzn
pr_merged_at: '2026-02-11'
task_type: axiom_repair
difficulty: medium
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 9
generated_at: '2026-05-17'
domain_area: upper-ontology
best_f1: 0.0
best_model: gpt-5.4
---

# PR #3659 — multicellular organism and organism substance should be disjoint

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #2421](https://github.com/obophenotype/uberon/issues/2421) | [PR #3659](https://github.com/obophenotype/uberon/pull/3659) | @matentzn | merged 2026-02-11

`axiom_repair` `medium` `tightly_scoped` `approved_first_time`

## Context

Issue #2421 reported that UBERON:0000468 (multicellular organism) and UBERON:0000463 (organism substance) should be declared disjoint, as an organism is not a substance and vice versa. This issue had been open since April 2022, nearly four years before resolution, and an earlier PR #3151 had been superseded by this one.

## Changes Made

The PR added a single disjoint_from axiom to uberon-edit.obo, declaring multicellular organism (UBERON:0000468) disjoint from organism substance (UBERON:0000463). Despite being a one-line change, it required careful reasoning about upper-level ontology categories to ensure the disjointness assertion would not create unintended unsatisfiable classes downstream.

## Resolution

Medium difficulty despite the minimal diff. An agent would need to understand BFO-aligned upper-level ontology categories to assess whether the disjointness assertion is logically sound and would not break downstream inferences. The long gap between issue and resolution (nearly four years) reflects that this kind of foundational change requires careful deliberation. Same-day merge once submitted.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16. Do not use the F1=0.0 scores at face value for this case.**

This is an **OWL-serialization / placement artifact** case. The requested change is a single symmetric disjointness axiom between `UBERON:0000468` (multicellular organism) and `UBERON:0000463` (organism substance). Because OBO/OWL `disjoint_from` is symmetric, there are several byte-distinct but logically identical ways to serialize it, and the issue thread itself produced *conflicting* placement guidance:

- **Gold PR #3659** (matentzn, merged 2026-02-11): `disjoint_from: UBERON:0000468 ! multicellular organism` added to the **UBERON:0000463 stanza in `src/ontology/uberon-edit.obo`**.
- **Superseded PR #3151** (ddooley, closed — not rejected on merits, just consolidated by #3659): the equivalent axiom on the **UBERON:0000468 stanza in `src/ontology/components/external-disjoints.obo`**. This placement was *explicitly directed by uberon member anitacaron in the issue* ("the disjoint file is at `src/ontology/components/external-disjoints.obo`").

All three agent attempts produced the **correct logical axiom** and are substantively `success`:

- **#264 (opus-4.7)** — byte-identical to gold's file, stanza, and line position; the *only* deviation is an added `{source="https://github.com/obophenotype/uberon/issues/2421"}` provenance qualifier (arguably an improvement over the bare gold line). F1=0.0 here is almost entirely an exact-line-match artifact caused by the provenance annotation.
- **#299 (sonnet-4.5)** and **#174 (haiku-4.5)** — identical to each other (blob `e2a9fc4`); a clean new `[Term]` stanza in `external-disjoints.obo`, i.e. the placement the uberon team directed in the issue and that PR #3151 used. Logically correct; differs from the final gold only by file/stanza convention.

Whole-file line-based metadiff cannot see symmetric-axiom equivalence or cross-file placement equivalence, so it reports F1=0.0 for all three even though none made a logical error. Downstream scoring/aggregation should treat this case as `case_quality: poor` and judge the attempts against the issue's actual ask (a valid disjointness axiom) rather than the single selected gold serialization. Companion PR: #3151.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 410d961c6..07e5cd192 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -6815,6 +6815,7 @@ xref: VHOG:0001726
 xref: XAO:0004001
 xref: ZFA:0001487
 is_a: UBERON:0000001 ! gross anatomical part
+disjoint_from: UBERON:0000468 ! multicellular organism
 relationship: has_quality PATO:0002198 ! quality of a substance
 relationship: part_of UBERON:0000468 {notes="this relationship may be too strong and may be weakened in future"} ! multicellular organism
 relationship: present_in_taxon NCBITaxon:33090 ! Viridiplantae

```

## Agent Attempts (9)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `f457c1d` | [#680](https://github.com/ai4curation/eval-ont-agent-uberon/pull/680) | [attempt](attempts/pr680.md) |
| 2 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `f457c1d` | [#640](https://github.com/ai4curation/eval-ont-agent-uberon/pull/640) | [attempt](attempts/pr640.md) |
| 3 | gpt-5.4 | opencode | 0.000 | 0.000 | 0.000 | `f457c1d` | [#620](https://github.com/ai4curation/eval-ont-agent-uberon/pull/620) | [attempt](attempts/pr620.md) |
| 4 | gpt-5.5 | opencode | 0.000 | 0.000 | 0.000 | `f457c1d` | [#584](https://github.com/ai4curation/eval-ont-agent-uberon/pull/584) | [attempt](attempts/pr584.md) |
| 5 | kimi-k2.6 | opencode | 0.000 | 0.000 | 0.000 | `e2a9fc4` | [#450](https://github.com/ai4curation/eval-ont-agent-uberon/pull/450) | [attempt](attempts/pr450.md) |
| 6 | gpt-5.4 | codex | 0.000 | 0.000 | 0.000 | `659d1ea` | [#385](https://github.com/ai4curation/eval-ont-agent-uberon/pull/385) | [attempt](attempts/pr385.md) |
| 7 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | `e2a9fc4` | [#299](https://github.com/ai4curation/eval-ont-agent-uberon/pull/299) | [attempt](attempts/pr299.md) |
| 8 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `b2c6f59` | [#264](https://github.com/ai4curation/eval-ont-agent-uberon/pull/264) | [attempt](attempts/pr264.md) |
| 9 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `e2a9fc4` | [#174](https://github.com/ai4curation/eval-ont-agent-uberon/pull/174) | [attempt](attempts/pr174.md) |
