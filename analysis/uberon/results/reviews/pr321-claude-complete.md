---
ontology: uberon
issue_number: 3478
pr_number: 3479
eval_repo_pr: 321
agent: std_claude_sonnet45
model: claude-sonnet-4-5-20250929
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

The agent correctly tightened the `in_taxon` restriction on `neurula stage`
(UBERON:0000110) and `pharyngula stage` (UBERON:0004707) from Eumetazoa
(NCBITaxon:6072) to Chordata (NCBITaxon:7711), and converted the `late embryonic
stage` (UBERON:0007220) `preceded_by` pharyngula axiom to a Chordata-scoped GCI.
It chose `gci_relation="part_of"` rather than the `occurs in` (BFO:0000066) the issue
proposed and the gold PR used. The F1 of 0.500 under-represents quality on the two
taxon edits (byte-identical to gold) but the GCI relation choice is a genuine
modeling divergence from both the issue and the gold.

## Strengths

- Both taxon-restriction edits (UBERON:0000110, UBERON:0004707) are byte-identical
  to the gold PR.
- Clean scope: exactly three issue-relevant hunks, no provenance noise, no
  robot-reserialization artifacts.
- Good methodology evidence in the PR comment: cites the issue's chordate-specificity
  rationale, references the GCI pattern from issue #2829, and notes the existing
  same-stanza RnorDv `part_of` GCI as the basis for its relation choice.

## Issues

- Modeling divergence: the GCI uses `gci_relation="part_of"` /
  `gci_filler="NCBITaxon:7711"`, whereas the issue explicitly proposed
  `'late embryonic stage' and 'occurs in' some Chordata SubClassOf 'preceded by'
  some 'pharyngula stage'` and the gold PR used `gci_relation="BFO:0000066"`
  (`occurs in`). `part_of` is defensible (it mirrors the pre-existing rat GCI
  `RnorDv:0000010 {gci_relation="part_of", gci_filler="NCBITaxon:10116"}` on the same
  stanza), and for the taxon-constraint-propagation purpose the two are effectively
  equivalent, but it does not match the issue author's stated intent. Weaker than
  pr336/pr279 which used the `occurs_in` form the issue asked for.
- Omission: the definition-text rewrites of `neurula stage` and `pharyngula stage`
  ("A chordate developmental stage ...") were not made — the main recall loss, and a
  defensible miss since the def rewrites were a PR-author addition not in the issue.
- Cosmetic: the PR comment mis-states "'late embryo' (UBERON:0000323)" as having the
  defective axiom; the actual edited term is UBERON:0007220. The diff itself is
  correct; only the prose is loose.
