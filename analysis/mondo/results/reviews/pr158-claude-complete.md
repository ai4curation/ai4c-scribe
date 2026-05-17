---
ontology: mondo
issue_number: 5726
pr_number: 10155
eval_repo_pr: 158
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: hard
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: failure
failure_modes: [under_editing, missed_requirement, wrong_pattern]
case_quality: poor
case_quality_reason: gold_leakage_base_contamination
companion_prs: [10145, 10231, 10232, 10234, 10235, 10233]
scoring_caveat: "F1=0.0 here is a genuine miss (the agent did not attempt the Template 2 bulk import and instead made an unrelated 1-line axiom change), but the case is still poor: the comparison gold is contaminated by leakage in other attempts and is only Template 2 of a 6-PR resolution. The 0.0 correctly indicates no overlap with gold, but the case cannot be used to compare models fairly against the 1.0 attempts."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This codex/gpt-5.4 run did **not attempt the issue's Template 2 bulk import** at all. Instead it made a single unrelated axiom change to `MONDO:0005755` (equine infectious anemia), replacing `is_a: MONDO:0700170 ! equine neoplasm` with `relationship: excluded_subClassOf MONDO:0700170 ...`. F1/precision/recall = 0.0 because this edit has zero overlap with gold PR #10155 (which adds 724 new NHA cross-species-analog terms and never touches MONDO:0005755). This is a genuine miss of the assigned task, though the case itself remains a poor evaluation reference (gold-leakage contamination across the other attempts; gold is only one tranche of the 6-PR resolution of #5726).

## Strengths

- The specific edit it made is **ontologically defensible in isolation**: equine infectious anemia is a viral infectious disease of horses and asserting `is_a equine neoplasm` is clearly a modeling error; preserving the removed parent as `excluded_subClassOf` with provenance is the Mondo-sanctioned way to record a deliberately dropped subclass axiom.
- Correct repo workflow described (`obo-checkout.pl`/`obo-checkin.pl`, `robot convert`, `make NORM`), single-file scope, transparent commit log.

## Issues

- **Did not address the issue (decisive).** Issue #5726 and gold PR #10155 are about importing ~728 new VeNom-derived NHA disease terms (Template 2). The agent neither added any new terms nor any VeNom xrefs (`under_editing`, `missed_requirement`).
- **Wrong target / off-pattern for this issue.** Fixing one pre-existing parentage bug on an unrelated term (`MONDO:0700170` neoplasm assertion) is out-of-scope for the VeNom import ask; it is not the cross-species-analog `nonhuman_disease` pattern the task required (`wrong_pattern`). The chosen term was not even part of the gold change set.
- **Metadiff (0.0) is accurate here** — there is genuinely no overlap with gold — but the case is still poor for cross-model comparison because the contemporaneous opencode attempts scored a contaminated 1.0; #158 should not be read as "this model is worse at the task" relative to those inflated scores.
- The edit may itself be questionable in repo context (other infectious-disease NHA terms legitimately carry neoplasm-adjacent classifications via curated provenance), and it was made without the issue asking for it — an unrequested change on a non-target term.
