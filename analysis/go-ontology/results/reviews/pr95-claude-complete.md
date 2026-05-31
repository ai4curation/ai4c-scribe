---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 95
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.857
precision: 0.9
recall: 0.818
jaccard: 0.75
outcome: partial_success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly handled the central reclassification: it *replaced* `is_a: GO:1990351 ! transporter complex` with `is_a: GO:0062137 ! cargo receptor complex`, renamed the primary label, demoted the old transporter labels to BROAD, added the new EXACT spelled-out cargo-receptor synonym, and added the `#31935` `term_tracker_item`. The metadiff (`F1=0.857`, `precision=0.900`, `recall=0.818`) is a fair signal: the ontology is correct but the definition was rewritten more extensively than the curator-specified minimal genus edit, and one extra transporter synonym was retained.

## Strengths

- Correct ontological move: parent *replaced*, not duplicated — `is_a: GO:0062137 ! cargo receptor complex` only, matching the merged gold and biologically correct.
- Primary label change matches the gold and the requester's explicit ask.
- Old primary label correctly demoted to `synonym: "retrograde transporter complex, Golgi to ER" BROAD []`, honoring ValWood's "not restricted to cargo" instruction.
- Added `synonym: "retrograde cargo receptor complex, Golgi to endoplasmic reticulum" EXACT []`, matching the human PR.
- Preserved `capable_of_part_of GO:0006890`; no logical-definition over-specification; explicitly reasoned in the PR comment that no DOSDP pattern applied.
- Documented validation (`make travis_build` pre/post, `linkml-reference-validator` on PMID:16093310).

## Issues

- **Definition over-rewrite**: the issue and the human PR changed only the genus phrase (`Transporter complex that recognises` → `Cargo receptor complex that recognizes`). This agent rewrote the whole first sentence to `A cargo receptor complex that recognizes and binds ... and returns them to the ER` and Americanized the second `recognised` → `recognized`. Substantively valid, but more editing than the curator asked for, and the leading indefinite article ("A cargo receptor complex...") deviates from GO definition style (the human kept the bare genus).
- Retained `synonym: "retrograde transporter complex, Golgi to endoplasmic reticulum" BROAD []`, which the human removed after ValWood's follow-up review. Defensible for a single-iteration run (mirrors the human's first commit) but a real recall delta versus the final gold.
- Net: the ontological substance is fully correct; the partial_success reflects definitional style/scope drift rather than any classification error.
