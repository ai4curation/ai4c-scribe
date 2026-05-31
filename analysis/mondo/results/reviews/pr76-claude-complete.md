---
ontology: mondo
issue_number: 9861
pr_number: 10113
eval_repo_pr: 76
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

The agent correctly disambiguated the issue — recognizing MONDO:0011236 already
covers the requested GCK hyperinsulinism concept and updating it in place — renamed it
to "GCK-related hyperinsulinism", added the ClinGen-preferred-label synonym with the
correct `OMO:0002001` qualifier, rewrote the definition with the issue PMIDs, added
parent MONDO:0017182, and added the #9861 tracker. F1=0.378 (precision ≈ recall)
under-represents the correct core resolution while fairly penalizing the primary-label
choice, an unrequested logical axiom, and the missed classification restructuring.

## Strengths

- Made the central judgment correctly: updated existing MONDO:0011236 (OMIM:602485
  equivalence) instead of minting a duplicate; PR comment explicitly explains the
  reasoning.
- Added "GCK-related hyperinsulinism" EXACT synonym with the correct ClinGen
  `{OMO:0002001="https://w3id.org/information-resource-registry/clingen"}` qualifier —
  exactly the convention in the agent config CLAUDE.md and matching the gold's synonym
  annotation precisely.
- Renamed primary label to "GCK-related hyperinsulinism" per the explicit `tpollin`
  ClinGen request in the comments.
- Definition rewritten with ClinGen source + the three issue PMIDs; documented
  verification of HGNC:4195 and the PMID abstracts.
- Added issue-requested parent `is_a: MONDO:0017182` without removing existing parents;
  added `IAO:0000233 .../issues/9861` while preserving #4985.

## Issues

- **Primary-label divergence (interpretation).** Made "GCK-related hyperinsulinism"
  primary; the gold kept "hyperinsulinemic hypoglycemia, familial, 3" primary with
  GCK-related as the ClinGen-preferred EXACT synonym. Both readings of the
  internally-contradictory issue are defensible; this is the largest single F1 driver.
- **wrong_pattern / over-editing: added an `intersection_of` equivalence axiom**
  (`intersection_of: MONDO:0017182` + `intersection_of: has_material_basis_in_...GCK`).
  The gold deliberately did not assert an equivalence axiom for this term; introducing
  one is an unrequested ontological commitment that reduces precision and risks
  reasoner/QC side effects.
- **Missed the classification restructuring (missed_requirement).** Gold removed
  `is_a: MONDO:0015624`, added `relationship: excluded_subClassOf MONDO:0015624`, and
  added `is_a: MONDO:0019010 ! congenital isolated hyperinsulinism` after the reviewer's
  CHANGES_REQUESTED. The agent kept MONDO:0015624 and added MONDO:0017182 — a different
  hierarchy. Not predictable from the issue text alone.
- Over-attribution: piled all three PMIDs + ClinGen onto MONDO:0017182 and onto
  multiple synonyms (e.g. "HHF3" EXACT [GARD:0009930, MONDO:Lexical, OMIM:602485]),
  diverging from the gold's lighter, source-specific attributions.
- Under-editing: omitted the Orphanet/DOID-sourced EXACT synonyms the gold added.
