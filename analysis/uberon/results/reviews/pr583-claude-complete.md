---
ontology: uberon
issue_number: 3464
pr_number: 3646
eval_repo_pr: 583
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: reclassification
difficulty: hard
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [3532, 3647]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent reparented `life cycle` (UBERON:0000104) and `life cycle stage` (UBERON:0000105) from `is_a: UBERON:0000000 ! processual entity` to `is_a: BFO:0000015 ! process` and added a `term_tracker_item` link to issue #3464 on both — exactly the COB-compatibility ask in the issue body. The resulting blob (`4f7bca3`) is byte-identical to attempt pr641 (same model gpt-5.5/opencode). F1=0.000 is a pure artifact of the partial gold: selected gold #3646 only adds two `has_ontology_root_term` header declarations, while the substantive reparenting is in companion human PR #3647. Judged against the issue and the union #3532+#3646+#3647, this is a **success**: the two `is_a` hunks are byte-identical to the corresponding core hunks in human PR #3647.

## Strengths

- Both reparenting hunks (UBERON:0000104 and UBERON:0000105 moved from `UBERON:0000000 ! processual entity` to `BFO:0000015 ! process`) are identical to the corresponding hunks in human PR #3647 — the agent independently reproduced the maintainer's chosen mechanism, eliminating the `processual entity` "occurrent" parent as the issue's COB goal requires.
- Adds `term_tracker_item "https://github.com/obophenotype/uberon/issues/3464"` provenance to both edited terms — good OBO curation hygiene exceeding the human's minimal diff (a metadiff-normalized field, so it does not reduce the substantive match).
- Tight scope: only the two intended terms touched, no reserialization churn or collateral edits; precision against the true (union) gold effectively perfect for the part addressed.
- Reproducible/deterministic with pr641 (identical blob), indicating a stable solution for this model.
- Correctly left the temporal-boundary branch (UBERON:0035943 + 3 children) untouched — defensible given COB#40 is unresolved and gold #3646 also did not touch it.

## Issues

- Does not deprecate/rename UBERON:0000000 ("processual entity"), which human PR #3647 obsoletes; after this change UBERON:0000000 still exists as a live class. Acceptable scoping boundary (the issue parked UBERON:0000000's fate; gold #3646 did not touch it), but incomplete relative to the full multi-PR human cleanup.
- Does not act on the comment-thread consensus that the four unused temporal-boundary vestiges (UBERON:0035943/0035944/0035945/0035946) should be removed. pr625 addressed this; here a justified-but-conservative omission, not an error.
- No PR comment/rationale captured for this attempt (diff only); methodology cannot be assessed and no reasoner/QC output is shown for an upper-level structural change. Minor.
