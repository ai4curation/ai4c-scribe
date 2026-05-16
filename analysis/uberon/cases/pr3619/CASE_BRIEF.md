---
ontology: uberon
repo: obophenotype/uberon
issue_number: 3617
pr_number: 3619
issue_title: Parent-child relationship between tracheal mucosa and nasal cavity mucosa
pr_author: dragon-ai-agent
pr_merged_at: '2025-11-03'
task_type: axiom_repair
difficulty: hard
scoping: tightly_scoped
scope: single_term
review_outcome: multiple_rounds
num_agent_attempts: 3
generated_at: '2026-05-15'
domain_area: respiratory-anatomy
best_f1: 1.0
best_model: claude-sonnet-4.5
---

# PR #3619 — Parent-child relationship between tracheal mucosa and nasal cavity mucosa

**uberon** | [obophenotype/uberon](https://github.com/obophenotype/uberon) | [Issue #3617](https://github.com/obophenotype/uberon/issues/3617) | [PR #3619](https://github.com/obophenotype/uberon/pull/3619) | @dragon-ai-agent | merged 2025-11-03

`axiom_repair` `hard` `tightly_scoped` `multiple_rounds`

## Context

The reasoner was incorrectly inferring that tracheal mucosa was a parent of nasal cavity mucosa due to an overly broad logical definition. The logical definition of tracheal mucosa (UBERON:0000379) used "part_of respiratory airway" which, through the class hierarchy, made nasal cavity mucosa classify as a subclass.

## Changes Made

Modified the logical definition of UBERON:0000379 (tracheal mucosa) to use a more specific anatomical context in the intersection_of axiom. Changed the part_of target from "respiratory airway" to "trachea" (or equivalent specific structure), preventing the incorrect inference chain.

## Resolution

Hard difficulty because this requires understanding OWL reasoning over intersection_of axioms. The agent must trace the inference chain: (1) tracheal mucosa is defined as mucosa that is part_of respiratory airway, (2) nasal cavity is a subclass of respiratory airway, (3) therefore nasal cavity mucosa satisfies the definition. The fix requires choosing a more specific part_of target that excludes nasal structures. The PR went through multiple rounds of review with changes requested.

## Human Diff

```diff
diff --git a/src/ontology/uberon-edit.obo b/src/ontology/uberon-edit.obo
index 1554053e6..2c38526e9 100644
--- a/src/ontology/uberon-edit.obo
+++ b/src/ontology/uberon-edit.obo
@@ -5515,7 +5515,7 @@ property_value: homology_notes "The lamprey head contains another group of muscl
 [Term]
 id: UBERON:0000379
 name: tracheal mucosa
-def: "A mucosa that is part of a respiratory airway." [OBOL:automatic]
+def: "A mucosa that is part of a trachea." [OBOL:automatic]
 synonym: "mucosa of organ of trachea" EXACT [OBOL:automatic]
 synonym: "mucosa of organ of windpipe" EXACT [OBOL:automatic]
 synonym: "mucosa of trachea" EXACT [OBOL:automatic]
@@ -5539,7 +5539,7 @@ xref: BTO:0001390
 xref: FMA:7471
 xref: SCTID:660006
 intersection_of: UBERON:0000344 ! mucosa
-intersection_of: part_of UBERON:0001005 ! respiratory airway
+intersection_of: part_of UBERON:0003126 ! trachea
 
 [Term]
 id: UBERON:0000380

```

## Agent Attempts (3)

| # | Model | Runtime | F1 | P | R | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|---------|--------|
| 1 | claude-sonnet-4.5 | claude | 1.000 | 1.000 | 1.000 | [#322](https://github.com/ai4curation/eval-ont-agent-uberon/pull/322) | [attempt](attempts/pr322.md) |
| 2 | claude-haiku-4.5 | claude | 1.000 | 1.000 | 1.000 | [#191](https://github.com/ai4curation/eval-ont-agent-uberon/pull/191) | [attempt](attempts/pr191.md) |
| 3 | claude-opus-4.7 | claude | 0.750 | 0.750 | 0.750 | [#256](https://github.com/ai4curation/eval-ont-agent-uberon/pull/256) | [attempt](attempts/pr256.md) |
