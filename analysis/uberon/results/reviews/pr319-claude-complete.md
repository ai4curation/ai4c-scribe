---
ontology: uberon
issue_number: 3475
pr_number: 3477
eval_repo_pr: 319
agent: std_claude_sonnet45
model: claude-sonnet-4-5-20250929
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: axiom_repair
difficulty: medium
f1: 0.333
precision: 1.000
recall: 0.200
jaccard: 0.200
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_partial
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This is the most faithful response to issue #3475 of all eight attempts. It removed `is_a: UBERON:0000961` from UBERON:0002835 (ask #1) *and* renamed UBERON:0000961 from "thoracic ganglion" to "thoracic paravertebral ganglion" (ask #2), with minimal collateral edits. The metadiff F1 of 0.333 (P=1.0, R=0.2) **severely under-represents quality**: it is low only because the gold PR #3477 did just the one-line is_a deletion and never did the rename the issue explicitly demanded. Judged against the actual issue, this attempt is essentially correct and complete.

## Strengths

- **Both issue asks satisfied.** Removed the incorrect `is_a: UBERON:0000961` axiom (matching gold exactly) and renamed UBERON:0000961 → "thoracic paravertebral ganglion" as issue #3475 explicitly requested ("clarify the name of thoracic ganglion ... to thoracic paravertebral ganglion").
- **Correct synonym handling on rename.** When promoting "thoracic paravertebral ganglion" (previously `EXACT [MA:0001159]`) to the primary label, it correctly demoted the old primary "thoracic ganglion" to an EXACT synonym rather than dropping it — preserving the label as a searchable term and the MA provenance lineage. This is cleaner than #232's RELATED demotion of the old name.
- Left the def, other synonyms (`ganglion of thorax`, `thorax ganglion`), xrefs, and logical definition untouched — tightly scoped, no def rewrite (unlike #19/#56/#37), no tracker-item noise, no file-regeneration contamination (unlike #11/#193).
- Accurate neuroanatomical rationale in the PR narrative.

## Issues

- Minor: dropped the `[MA:0001159]` xref provenance from the synonym record when "thoracic paravertebral ganglion" became the primary name (it was `synonym: "thoracic paravertebral ganglion" EXACT [MA:0001159]`). The MA equivalence is implicitly retained via the new primary label but the explicit MA provenance annotation on that string is lost. Defensible but a curator might have added an `xref: MA:0001159` or kept a synonym with provenance.
- Did not add a `term_tracker_item` linking the change to the issue. Other agents added one; gold did not. This is a convention difference, not an error, and arguably gold's omission is the gap.

No substantive errors. Outcome graded `success` on the merits of the issue despite the low metadiff (poor case — see METADATA.md).
