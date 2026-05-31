---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 45
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.720
precision: 0.9
recall: 0.6
jaccard: 0.562
outcome: partial_success
failure_modes: [over_editing, under_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly *replaced* `is_a: GO:1990351 ! transporter complex` with `is_a: GO:0062137 ! cargo receptor complex`, renamed the primary label, performed a minimal genus-only definition edit, added the new EXACT spelled-out cargo-receptor synonym, and added the `#31935` `term_tracker_item`. But it over-reached on synonym scoping: it demoted the *pre-existing* `retrograde receptor complex` EXACT synonyms (both forms) to BROAD even though the issue never asked to touch them. The metadiff (`F1=0.720`, `precision=0.900`, `recall=0.600`) — the lowest in the case — over-penalizes recall: the core reclassification is fully correct and the recall hit is mostly the unrequested receptor-synonym demotions plus the post-review transporter synonym.

## Strengths

- Correct ontological move: parent *replaced*, not duplicated — `is_a: GO:0062137 ! cargo receptor complex` only. Biologically correct and matching the merged gold.
- Primary label change matches the gold and the requester's ask.
- Minimal genus-only definition edit (`Transporter complex that recognises` → `Cargo receptor complex that recognizes`), with a small "particularly proteins lacking..." rephrase but no full rewrite — closer to the human's intent than the gpt-5.5 attempts.
- Added `synonym: "retrograde cargo receptor complex, Golgi to endoplasmic reticulum" EXACT []`, matching the human PR's new synonym.
- Old transporter labels correctly demoted to BROAD; added the `#31935` provenance; preserved `capable_of_part_of GO:0006890`. Documented design-pattern and reference review in PR comment.

## Issues

- **Over-edit on unrelated synonyms (over_editing)**: demoted the two *pre-existing, untouched-by-issue* synonyms `retrograde receptor complex, Golgi to endoplasmic reticulum` and `retrograde receptor complex, Golgi to ER` from EXACT to BROAD. The issue only asked to demote the *transporter* wording; "receptor complex" is consistent with the new "cargo receptor complex" primary label and the human PR kept these EXACT. This is a genuine, unrequested scope expansion that changes synonym semantics and is the main driver of the low recall.
- Retained `synonym: "retrograde transporter complex, Golgi to endoplasmic reticulum" BROAD []`, which the human removed after a follow-up review round — defensible for a single-iteration run.
- Net: the reclassification and the new synonym are correct; the failure mode is purposeful but unwarranted re-scoping of synonyms the issue did not mention. The high precision (0.900) correctly reflects that what it added was right; the low recall conflates this defensible-but-unrequested re-scoping with the gold rather than indicating missed required work.
