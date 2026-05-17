---
ontology: mondo
issue_number: 9871
pr_number: 10201
eval_repo_pr: 307
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.069
precision: 0.036
recall: 1.0
jaccard: 0.036
outcome: partial_success
failure_modes: [under_editing]
case_quality: poor
case_quality_reason: gold_scope_expanded_off_issue
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The most minimal attempt: a single one-line edit replacing
`xref: Orphanet:1671 {source="MONDO:equivalentTo", source="OMIM:222500"}` with
`xref: Orphanet:573278 {source="MONDO:equivalentTo"}`. This is the literal core ask of issue
#9871 and it is correct, but the agent did none of the supporting provenance cleanup (subsets,
synonym xref lists, other `source=` qualifiers), so the term is left internally inconsistent
with stale Orphanet:1671 references elsewhere in the stanza. F1=0.069 is extreme but
**recall=1.0** — every line it changed is in the gold; it simply did far too little. The tiny
F1 is mostly the off-issue subtype/obsoletion mass (case flagged poor) compounded by genuine
under-editing.

## Strengths

- The one substantive change is exactly right and matches the gold's equivalent-mapping
  intent: `xref: Orphanet:573278 {source="MONDO:equivalentTo"}` (recall 1.0 — no incorrect or
  extraneous edits at all).
- Clear PR/issue comment correctly explaining the rationale (Orphanet:1671 too narrow;
  573278 the broader appropriate concept; diastematomyelia ≈ split cord malformation).
- Zero risk of collateral damage — no over-editing, no wrong patterns.

## Issues

- Severe under-editing: left `subset: ordo_disorder/ordo_morphological_anomaly/orphanet/`
  `orphanet_rare {source="Orphanet:1671"}`, the `diastematomyelia` EXACT synonym xref list,
  and the ICD10CM/MedDRA/OMIM `source="Orphanet:1671..."` qualifiers all pointing at the now-
  removed Orphanet:1671. The term is internally inconsistent: it claims Orphanet:573278 as
  equivalent while its subsets and synonym provenance still cite 1671.
- Did not add the `property_value: IAO:0000233 ".../issues/9871"` term tracker.
- Did not touch the narrow synonyms "SCM type 1" / "split cord malformation type 1" or upgrade
  "split cord malformation" to EXACT.
- None of the off-issue subtype creation / obsoletion-merge work (the dominant source of the
  near-zero F1; this is the case-quality artifact, not a true agent failure).

Outcome `partial_success`: the single change is correct and the issue's literal headline ask
is satisfied, but the incomplete provenance cleanup leaves the term in a state a curator would
have to finish before merge. Graded as partial (not failure) because the one edit is right and
well-justified; graded above the copilot attempts (#489/#524) which actively introduced a
regression.
