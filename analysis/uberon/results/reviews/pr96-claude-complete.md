---
ontology: uberon
issue_number: 3475
pr_number: 3477
eval_repo_pr: 96
agent: std_claude_haiku45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: axiom_repair
difficulty: medium
f1: 0.667
precision: 1.000
recall: 0.500
jaccard: 0.500
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern]
case_quality: poor
case_quality_reason: gold_pr_is_partial
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent did not remove the spurious `is_a: UBERON:0000961` axiom that issue #3475 explicitly asked to be removed; instead it *rewrote* the line to `is_a: UBERON:0000044 ! dorsal root ganglion`. It also did not perform the second requested change (renaming UBERON:0000961 to "thoracic paravertebral ganglion"). The metadiff F1 of 0.667 (P=1.0, R=0.5) is the highest of the eight attempts only because the single line it touched is the same line the partial gold PR touched — but the *substance* is wrong: this attempt over-represents quality. Note this is a `case_quality: poor` case (gold PR #3477 only resolved one of the issue's two explicit asks).

## Strengths

- Correctly diagnosed the neuroanatomical problem: dorsal root ganglia are sensory, paravertebral/sympathetic ganglia are autonomic; the two should not be in an is_a relationship. The PR narrative is accurate.
- Tightly scoped: only one line changed, no gratuitous edits, no file-regeneration contamination (unlike #11/#193).
- Recognized the existing logical definition (`intersection_of: UBERON:0000044 ! dorsal root ganglion`) correctly types the term.

## Issues

- **Wrong pattern (primary):** The issue asked to *remove* the `is_a: UBERON:0000961` axiom. The agent instead replaced it with `is_a: UBERON:0000044 ! dorsal root ganglion`. This re-asserts an `is_a` parent that is *identical to the genus* of the already-present logical definition (`intersection_of: UBERON:0000044`). In an ontology with a reasoner, asserting the same parent that the equivalence axiom already entails is redundant and is the kind of asserted-vs-inferred duplication Uberon curation avoids — the gold PR deliberately removed the line without replacement precisely because the genus-differentia definition already does the work.
- **Missed requirement:** Did not rename UBERON:0000961 "thoracic ganglion" → "thoracic paravertebral ganglion", the second explicit ask in issue #3475. (The gold PR also omitted this, but the issue text is unambiguous; attempts #319/#232/#19/#56/#37/#11/#193 all did perform the rename.)
- The PR comment claims "All 12 sub-types (T1–T12) inherit the corrected classification" — true of inference, but no sub-type stanzas were actually edited; the language overstates the diff.

## Curation Note

This is a poor evaluation case: gold PR #3477 resolved only the is_a removal, not the rename that issue #3475 also explicitly requested, and no companion PR ever did the rename (current Uberon HEAD still has `name: thoracic ganglion`). Metadiff vs #3477 therefore rewards the minimal/partial answer and penalizes the more complete attempts. See METADATA.md.
