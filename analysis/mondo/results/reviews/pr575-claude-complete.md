---
ontology: mondo
issue_number: 9854
pr_number: 10116
eval_repo_pr: 575
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: other
difficulty: medium
case_quality: ok
case_quality_reason: sound_gold_but_requires_source_provenance_investigation
f1: 0.667
precision: 0.611
recall: 0.733
jaccard: 0.5
outcome: partial_success
failure_modes:
  - missed_requirement
  - under_editing
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
---

## Summary

Issue #9854 asked to move ORPHANET:2477 ("isolated megalencephaly") from MONDO:0016608
(megalencephaly) to MONDO:0017089 (isolated megalencephaly). This attempt
(gpt-5.4/codex, blob `77cc9f3`) performed the headline move, subset relocation, and
issue-tracker annotation on both terms, but (a) skipped the Orphanet provenance scrub of
the co-located ICD/MedDRA xrefs that gold performed, and (b) introduced an out-of-scope
edit gold did not make: it rewrote the `is_a` axiom provenance on MONDO:0017089 from
`Orphanet:268920` to `Orphanet:2477`. F1=0.667 (precision=0.611, recall=0.733). This is
both an under-edit (missed provenance cleanup) and an over-edit (changed parent-axiom
provenance), so a curator would need to revert one change and add several others.

## Strengths

- Correctly moved `xref: Orphanet:2477 {source="MONDO:equivalentTo"}` from MONDO:0016608
  to MONDO:0017089 — the literal issue request.
- Moved all four ORDO/Orphanet subsets (`{source="Orphanet:2477"}`) to MONDO:0017089,
  matching gold for that block.
- Added `property_value: IAO:0000233 ".../issues/9854"` to **both** MONDO:0016608 and
  MONDO:0017089, matching the gold annotation convention more completely than the
  gpt-5.5 opencode attempts (#668/#723), which annotated only the isolated term.
- Disclosed a documented methodology: issue-context check, `obo-grep.pl` inspection,
  checkout/checkin term workflow, `make NORM`, `robot convert` syntax validation.

## Issues

- Over-editing (the salient problem): rewrote the parent-axiom provenance on
  MONDO:0017089 — `is_a: MONDO:0016608 {source="MONDO:Redundant", source="Orphanet:268920"}`
  → `{source="MONDO:Redundant", source="Orphanet:2477"}` and likewise the
  `is_a: MONDO:0021147 ... Orphanet:268920/inferred` → `Orphanet:2477/inferred`. Gold
  deliberately left these `Orphanet:268920` (the obsolete-equivalent provenance) intact
  and also retained `xref: Orphanet:268920 {source="MONDO:equivalentObsolete"}`. The
  agent's substitution conflates the live mapping (2477) with the obsolete-equivalent
  relationship (268920) and degrades provenance accuracy. This is the only true *error*
  in the attempt.
- Omission: did not strip `source="Orphanet:2477"`/`Orphanet:2477/e` from
  `xref: ICD10CM:Q04.5` and `xref: icd11.foundation:368780653` on MONDO:0016608, nor
  re-source `xref: MedDRA:10050183` (gold → `{source="MONDO:equivalentTo"}`). Stale
  Orphanet provenance remains on the broad term.
- Omission: did not add `xref: icd11.foundation:368780653 {source="Orphanet:2477"}` to
  MONDO:0017089, so moved provenance is incompletely reconstructed.
- Net: closest of the lower-scoring attempts on the annotation convention, but the
  unrequested parent-axiom provenance rewrite plus the missed xref cleanup make this a
  partial_success requiring both a revert and follow-up curation before merge.
