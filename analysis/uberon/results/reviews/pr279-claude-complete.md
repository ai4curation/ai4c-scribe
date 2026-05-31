---
ontology: uberon
issue_number: 3478
pr_number: 3479
eval_repo_pr: 279
agent: std_claude_hai45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.500
precision: 0.375
recall: 0.750
jaccard: 0.333
outcome: partial_success
failure_modes: [missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This attempt is byte-identical to pr336 (same output blob `0b7dbb4`): the same
claude-haiku-4.5 / claude runtime produced the same three-hunk diff. It correctly
tightens `in_taxon` on `neurula stage` (UBERON:0000110) and `pharyngula stage`
(UBERON:0004707) from Eumetazoa to Chordata (NCBITaxon:7711) and converts the
`late embryonic stage` (UBERON:0007220) `preceded_by` pharyngula axiom to a
Chordata-scoped GCI with `gci_relation="occurs_in"`, matching the issue author's
exact `occurs in some Chordata` proposal. The metadiff F1 of 0.500 under-represents
quality: every change the *issue* explicitly requested is present and correct.

## Strengths

- Both taxon edits are byte-identical to the gold PR (UBERON:0000110 and
  UBERON:0004707, NCBITaxon:6072 → NCBITaxon:7711).
- GCI on UBERON:0007220 uses `gci_relation="occurs_in"` / `gci_filler="NCBITaxon:7711"`
  — the semantically correct relation the issue proposed; the gold used the IRI form
  `BFO:0000066` of the same `occurs in` relation.
- Perfect scope discipline: exactly the three issue-relevant hunks, no provenance
  lines, no robot-reserialization artifacts, no over-editing.
- Demonstrates reproducibility of the haiku/claude configuration on this case
  (identical to pr336).

## Issues

- Omission: the definition-text rewrites of `neurula stage` and `pharyngula stage`
  (gold: "A chordate developmental stage ...") were not made. This is the only
  substantive gap and the cause of recall 0.750. The omission is defensible since
  these def rewrites were a PR-author addition not requested in the issue body.
- Minor surface difference: `occurs_in` (label) vs gold `BFO:0000066` (IRI) for the
  GCI relation — semantically equivalent.
- Note: this attempt has no PR/issue comment recorded in the case file (diff only),
  so methodology cannot be inspected; the diff itself is identical to the
  well-reasoned pr336.
