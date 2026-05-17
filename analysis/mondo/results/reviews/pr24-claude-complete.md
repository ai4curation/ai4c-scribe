---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 24
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.579
precision: 0.647
recall: 0.524
jaccard: 0.407
outcome: partial_success
failure_modes:
  - over_editing
  - wrong_pattern
case_quality: poor
case_quality_reason: gold_incomplete_dangling_replaced_by
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

claude-haiku-4.5/claude obsoleted MONDO:0009327 but made the most divergent
choices in the set: it added a `def:` (definitions are not used on obsolete
Mondo terms), used `replaced_by:` instead of `consider:` (the issue explicitly
asked for a *term to consider*, not an exact replacement), dropped the
GARD:0024658 xref entirely, and over-stripped subsets and provenance. F1 0.579;
core "obsolete the term" intent met but several pattern errors. Partial success.

## Strengths

- Term marked obsolete: name → `obsolete heart, malformation of`,
  `is_obsolete: true`, both `is_a` parents removed, `obsoletion_candidate`
  removed, `IAO:0006012` and `curated_content_resource` removed,
  `IAO:0000231 OMO:0001000` obsoletion reason added.
- Good issue-grounded rationale in the PR body (OMIM split, MedGen-stays-active
  note from @kanems).

## Issues

- **Wrong pattern**: used `replaced_by: MONDO:0005267` instead of
  `consider: MONDO:0005267`. The issue's "Suggested term to consider" and the
  original stanza comment ("will not have a replacement ID, but one could
  consider...") both indicate this is *not* an exact replacement. The gold and
  almost every other attempt correctly used `consider:`. `replaced_by` asserts
  an exact 1:1 equivalence that does not hold (heart disorder is a broad
  superclass). Substantive ontological error.
- **Wrong pattern**: added `def: "OBSOLETE. ..."`. The agent config's
  obsoletion guidance keeps obsolete stanzas free of definitions ("Remove ALL
  logical axioms and definitions from obsoleted terms"); the gold added no
  `def:`. The original stanza had no definition, so this *introduces* one on an
  obsolete term.
- **Error / data loss**: dropped the `xref: GARD:0024658` line entirely
  (gold retained it with `{source="MONDO:GARD"}`). Losing a cross-reference is
  a real defect.
- Over-editing: removed `gard_rare`/`nord_rare` subsets and flattened all xref
  source qualifiers to bare `MONDO:obsoleteEquivalent`, dropping
  MEDGEN/UMLS secondary provenance.
- Did not rewire the dangling MONDO:0007703 reference.

Net: the term is obsoleted but with a wrong replacement relation, an
inappropriate `def:`, a dropped xref, and provenance loss. Lowest-fidelity
claude-family attempt; partial success only because the basic obsoletion
mechanics are present.
