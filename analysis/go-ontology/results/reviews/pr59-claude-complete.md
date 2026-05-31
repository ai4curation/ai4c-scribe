---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 59
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.800
precision: 0.8
recall: 0.8
jaccard: 0.667
outcome: partial_success
failure_modes: [over_editing, under_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly *replaced* `is_a: GO:1990351 ! transporter complex` with `is_a: GO:0062137 ! cargo receptor complex`, renamed the primary label, demoted both transporter labels to BROAD, and added the `#31935` `term_tracker_item`. However it rewrote the definition substantially and **added an unrequested literature reference (PMID:25583996)** to the definition provenance. The metadiff (`F1=0.800`, `precision=recall=0.800`) is roughly fair; the recall gap is the missing new EXACT synonym and the precision gap is the added reference plus definition rewrite.

## Strengths

- Correct ontological move: parent *replaced*, not duplicated — `is_a: GO:0062137 ! cargo receptor complex` only. Biologically correct and matching the merged gold.
- Primary label change matches the gold and the requester's ask.
- Old primary label demoted to `synonym: "retrograde transporter complex, Golgi to ER" BROAD []`, honoring ValWood's instruction.
- Preserved `capable_of_part_of GO:0006890`; no logical-definition over-specification; added the `#31935` provenance.

## Issues

- **Unrequested reference addition (over_editing)**: changed the definition xref block from `[GOC:bhm, PMID:16093310]` to `[GOC:bhm, PMID:16093310, PMID:25583996]`. The issue asked only for a genus rewording; introducing a new primary reference is a substantive, unrequested content change. Even if PMID:25583996 is relevant to the Erv41-Erv46 complex, adding citations was outside the issue scope and the human PR did not do this. Adding a reference also normally triggers a reference-validation obligation the issue did not request.
- **Definition over-rewrite**: rewrote the whole definition (`A cargo receptor complex that recognizes and binds ... and returns them to the ER. Targets include proteins that lack the HDEL motif used by KDEL receptors for COPI-dependent retrieval.`) rather than the minimal genus swap the issue and human PR used. The added "KDEL receptors" / "COPI-dependent retrieval" gloss is an interpretive expansion, not requested.
- **Omission (under_editing)**: did not add `synonym: "retrograde cargo receptor complex, Golgi to endoplasmic reticulum" EXACT []` for the new label, which the human PR added.
- Reordered the two `term_tracker_item` lines (placed `#31935` before `#24444`); cosmetic, no semantic impact.
- Net: ontology correct, but the gratuitous reference addition is the most concerning scope breach among the gpt-5.5 attempts because it changes evidential provenance, not just wording.
