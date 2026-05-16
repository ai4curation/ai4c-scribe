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
num_agent_attempts: 3
generated_at: '2026-05-15'
domain_area: upper-ontology
best_f1: 0.0
best_model: claude-sonnet-4.5
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

## Agent Attempts (3)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 0.000 | 0.000 | 0.000 | [#299](https://github.com/ai4curation/eval-ont-agent-uberon/pull/299) | [attempt](attempts/pr299.md) |
| 2 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | [#264](https://github.com/ai4curation/eval-ont-agent-uberon/pull/264) | [attempt](attempts/pr264.md) |
| 3 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | [#174](https://github.com/ai4curation/eval-ont-agent-uberon/pull/174) | [attempt](attempts/pr174.md) |
