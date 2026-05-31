---
ontology: mondo
issue_number: 9861
pr_number: 10113
eval_repo_pr: 496
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.400
precision: 0.316
recall: 0.545
jaccard: 0.250
outcome: partial_success
failure_modes: [missed_requirement, over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This attempt is byte-identical to PR #531 (same agent std_copilot_son45, same blob
`f00c73a`, identical scores) — a replicate run. The agent correctly recognized that
MONDO:0011236 already covers the requested GCK hyperinsulinism concept and updated it
in place rather than creating a duplicate, renamed it to "GCK-related hyperinsulinism",
rewrote the definition with the issue PMIDs, promoted the familial-3 synonyms to EXACT,
added parent MONDO:0017182, and added the #9861 tracker. F1=0.400 under-represents the
correct core resolution while fairly flagging the primary-label and classification
divergences from the gold.

## Strengths

- Correct central disambiguation: updated existing MONDO:0011236 (OMIM:602485
  equivalence) instead of minting a new term.
- Renamed to "GCK-related hyperinsulinism" per the explicit `tpollin` ClinGen comment —
  a defensible reading of an internally contradictory issue.
- Definition rewritten with the ClinGen affiliation source and the exact issue PMIDs
  (15277402, 24890200, 34680961).
- Added issue-requested parent `is_a: MONDO:0017182` without removing existing parents.
- Added the `IAO:0000233 .../issues/9861` tracker while preserving #4985 — matching the
  gold provenance change.
- Scoped: no unrequested `intersection_of` equivalence axiom introduced.

## Issues

- **Primary-label divergence.** Made "GCK-related hyperinsulinism" primary; gold kept
  "hyperinsulinemic hypoglycemia, familial, 3" primary with GCK-related as the
  ClinGen-preferred EXACT synonym. The `OMO:0002001` ClinGen preferred-label qualifier
  documented in the agent config CLAUDE.md was not applied — a missed convention.
- **Missed the classification restructuring (missed_requirement).** Gold removed
  `is_a: MONDO:0015624`, added `relationship: excluded_subClassOf MONDO:0015624`, and
  added `is_a: MONDO:0019010 ! congenital isolated hyperinsulinism`. The agent kept
  MONDO:0015624 and added MONDO:0017182 instead. This emerged from the reviewer's
  CHANGES_REQUESTED dialogue and was not predictable from the issue text.
- **Over-editing**: added the ClinGen URL as an extra source on the "familial, 3"
  synonym (gold used MONDO:Lexical only). Minor/defensible.
- Under-editing on synonym coverage: omitted the Orphanet/DOID-sourced EXACT synonyms
  the gold added.
- **Process note**: this run is a duplicate of #531 and contributes no independent
  signal beyond confirming determinism of the std_copilot_son45 configuration on this
  case.
