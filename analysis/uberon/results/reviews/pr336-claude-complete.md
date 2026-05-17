---
ontology: uberon
issue_number: 3478
pr_number: 3479
eval_repo_pr: 336
agent: std_claude_haiku45
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

The agent correctly executed both of the explicit asks in issue #3478: it tightened the
`in_taxon` restriction on `neurula stage` (UBERON:0000110) and `pharyngula stage`
(UBERON:0004707) from Eumetazoa (NCBITaxon:6072) to Chordata (NCBITaxon:7711), and it
converted the unconditional `late embryonic stage` (UBERON:0007220) `preceded_by`
pharyngula axiom into a Chordata-scoped GCI. The metadiff F1 of 0.500 under-represents
the quality of this attempt: it captured 100% of what the *issue* requested, and the
GCI semantics it chose (`gci_relation="occurs_in"`, `gci_filler="NCBITaxon:7711"`)
match the issue author's exact proposal (`occurs in` some Chordata). The recall loss is
almost entirely the two definition-text rewrites that the gold PR added but that the
issue never explicitly requested.

## Strengths

- Both taxon-restriction edits (UBERON:0000110 and UBERON:0004707) are byte-identical
  to the gold PR: `in_taxon NCBITaxon:6072 ! Eumetazoa` → `in_taxon NCBITaxon:7711 ! Chordata`.
- The GCI conversion on UBERON:0007220 uses `gci_relation="occurs_in"`, which is the
  semantically correct relation the issue explicitly proposed (`'late embryonic stage'
  and 'occurs in' some Chordata SubClassOf 'preceded by' some 'pharyngula stage'`).
  The gold PR used `gci_relation="BFO:0000066"` — the IRI form of the same `occurs in`
  relation — so this is the *intended* semantics, differing only in label-vs-IRI form.
- Tight scope discipline: exactly 3 hunks, all issue-relevant, no over-editing, no
  spurious provenance lines, no robot-reserialization artifacts.
- The PR comment cites the same literature the issue used (Masak & Davidson 2023,
  Collazo 2000, Ballard 1964) showing the agent grounded its reasoning rather than
  guessing.

## Issues

- Omission: did not reword the textual definitions of `neurula stage` and
  `pharyngula stage` to "A chordate developmental stage ..." as the gold PR did. This
  is the sole substantive gap and the main driver of the 0.750 recall. It is a
  defensible omission since the issue body (proposal items 1 and 2) only asked for the
  taxon restriction and the GCI; the def rewrites appear only in the PR author's
  description ("amend their definition accordingly"), not in the issue.
- Minor: GCI relation is `occurs_in` (label form) vs the gold's `BFO:0000066` (IRI
  form). Semantically equivalent for the taxon-constraint-propagation goal; metadiff
  penalises the surface difference but the modeling is correct.
- Overall: this is genuinely the strongest attempt in the case alongside the identical
  pr279; F1=0.500 should be read as "issue fully resolved, PR-author's optional def
  polish missed."
