---
ontology: mondo
issue_number: 9861
pr_number: 10113
eval_repo_pr: 55
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.378
precision: 0.368
recall: 0.389
jaccard: 0.233
outcome: partial_success
failure_modes: [missed_requirement, over_editing, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This attempt is byte-identical to PR #76 (same agent std_opencode_g55, same blob
`3fe151a`, identical scores) — a deterministic replicate. The agent correctly
recognized MONDO:0011236 already covers the requested GCK hyperinsulinism concept and
updated it in place, renamed it to "GCK-related hyperinsulinism", added the ClinGen
preferred-label synonym with the correct `OMO:0002001` qualifier, rewrote the
definition with the issue PMIDs, added parent MONDO:0017182, and added the #9861
tracker. F1=0.378 under-represents the correct core resolution while fairly penalizing
the primary-label choice, an unrequested logical axiom, and the missed classification
restructuring.

## Strengths

- Correct central disambiguation: updated existing MONDO:0011236 (OMIM:602485
  equivalence) rather than minting a duplicate.
- Added "GCK-related hyperinsulinism" EXACT synonym with the correct
  `{OMO:0002001="https://w3id.org/information-resource-registry/clingen"}` ClinGen
  qualifier — matching the gold's synonym annotation exactly and following the agent
  config CLAUDE.md convention.
- Renamed primary label to "GCK-related hyperinsulinism" per the explicit `tpollin`
  ClinGen comment.
- Definition rewritten with ClinGen source + the three issue PMIDs.
- Added issue-requested parent `is_a: MONDO:0017182`; added `IAO:0000233 .../issues/9861`
  while preserving #4985.

## Issues

- **Primary-label divergence (interpretation).** Made "GCK-related hyperinsulinism"
  primary; gold kept "hyperinsulinemic hypoglycemia, familial, 3" primary with
  GCK-related as the ClinGen-preferred EXACT synonym. Largest F1 driver; defensible
  given the contradictory issue.
- **wrong_pattern / over-editing**: added an unrequested `intersection_of` equivalence
  axiom (MONDO:0017182 + has_material_basis_in GCK) that the gold deliberately did not
  assert.
- **Missed the classification restructuring (missed_requirement).** Gold removed
  `is_a: MONDO:0015624`, added `relationship: excluded_subClassOf MONDO:0015624`, and
  added `is_a: MONDO:0019010`. The agent kept MONDO:0015624 and added MONDO:0017182.
- Over-attribution of PMIDs/ClinGen onto MONDO:0017182 and multiple synonyms; omitted
  the Orphanet/DOID-sourced EXACT synonyms the gold added (under-editing).
- **Process note**: duplicate of #76 — confirms determinism of std_opencode_g55 on
  this case, no independent signal.
