---
ontology: go-ontology
issue_number: 31114
pr_number: 32028
eval_repo_pr: 543
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: axiom_repair
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
- under_editing
- wrong_pattern
case_quality: poor
case_quality_reason: gold_pr_partial_and_metadiff_blind_to_created_by
companion_prs:
- 32032
- 32014
scoring_caveat: "Metadiff ignores created_by, so F1=0.0 is mechanical. Gold PR #32028 is an interim wrong fix (GOC:vw); final-correct is bare vw (#32032). Gold PR also bundles GO:0180068 from unrelated issue #31261."
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The agent performed the issue-thread label/synonym swap on GO:0180067 and GO:0180069 and changed `created_by` from `PomBase:vw` to `GOC:vw` on those two terms. The reported F1=0.0 is a scoring artifact: the OBO metadiff explicitly ignores `created_by`, the only field the selected gold PR #32028 actually changed, so no attempt on this case can score above zero. Judged against the issue discussion and the union of human PRs (#32028 + #32032 + #32014), this is a partial success: the metadata edit uses the interim-wrong `GOC:vw` (final-correct is bare `vw`, applied in #32032), and GO:0180068 — bundled into the gold PR but belonging to unrelated issue #31261 — was untouched, which is defensible given the agent only had issue #31114.

## Strengths

- Correctly identified GO:0180067 and GO:0180069 as the terreic-acid terms and performed the label↔synonym swap that ValWood and pgaudet explicitly authorized in the issue thread (`terreate biosynthetic process` → `terreic acid biosynthetic process`; old label demoted to RELATED synonym). This is the originally-requested behavior, not scope creep.
- Updated the GO:0180067 definition text from "formation of terreate" to "formation of terreic acid" to keep the definition consistent with the new primary label.
- Left the logical definition `intersection_of: has_primary_output CHEBI:233617 ! terreate` unchanged, correctly following the GO chemical-entity convention (biologist-friendly label, pH 7.3 CHEBI form retained in the equivalence axiom).
- Addressed the `created_by` cleanup that was the explicit ask in the issue comment chain.

## Issues

- **Wrong convention (`wrong_pattern`)**: used `created_by: GOC:vw`, which matches ValWood's literal (but mistaken) instruction and the interim gold PR #32028, but not the final-correct bare `vw` that pgaudet specified and that companion PR #32032 applied. There is no `GOC:`-prefixed `created_by` anywhere else in go-edit.obo; adjacent terms GO:0180065/GO:0180066 use bare `vw`. A more careful agent (cf. opus #336, which flagged the ambiguity but still chose `GOC:vw`) would have surfaced this conflict.
- **Incomplete vs. gold batch (`under_editing`)**: did not touch GO:0180068 `negative regulation of carbohydrate utilization`. This is only weakly an omission — GO:0180068's `term_tracker_item` points to issue #31261, not #31114, so an agent scoped to #31114 had no signal to find it. The gold PR caught it only because the human ran `grep PomBase:vw` across the whole file.
- The GO:0180069 regulation definition was not updated to match its renamed primary label, and the rendered `! terreate biosynthetic process` comment on the `positively_regulates GO:0180067` axiom was left stale (cosmetic; ROBOT regenerates it).
- F1/precision/recall are all 0.0 but do not represent quality here — they under-represent it. The substantive edits are largely correct and issue-aligned.
