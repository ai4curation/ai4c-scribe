---
ontology: uberon
issue_number: 3478
pr_number: 3479
eval_repo_pr: 20
agent: std_codex_gpt55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.462
precision: 0.375
recall: 0.600
jaccard: 0.300
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern, scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly tightened `in_taxon` on `neurula stage` (UBERON:0000110) and
`pharyngula stage` (UBERON:0004707) from Eumetazoa (NCBITaxon:6072) to Chordata
(NCBITaxon:7711) and converted the `late embryonic stage` (UBERON:0007220)
`preceded_by` pharyngula axiom to a GCI. However it chose `gci_relation="in_taxon"`,
which is a weaker/different modeling than the issue's proposed `occurs in`
(BFO:0000066), and it added three `term_tracker_item` provenance lines plus a
trailing-newline deletion artifact. F1=0.462 modestly under-represents the core
taxon edits but the GCI relation choice and extra lines are genuine deviations.

## Strengths

- Both taxon edits (UBERON:0000110, UBERON:0004707) are byte-identical to gold:
  `in_taxon NCBITaxon:6072 ! Eumetazoa` → `in_taxon NCBITaxon:7711 ! Chordata`.
- Converted the unconditional `preceded_by UBERON:0004707` on UBERON:0007220 into a
  taxon-scoped GCI, preserving the chordate ordering while freeing the general
  late-embryonic concept — the correct overall repair shape.
- Good process discipline documented: checked the three stanzas, inspected existing
  GCI encodings, used the `obo-checkout.pl`/`obo-checkin.pl` workflow, reserialized
  and validated with `robot convert`, ran `git diff --check`.

## Issues

- Modeling divergence (wrong_pattern): GCI uses
  `{gci_filler="NCBITaxon:7711", gci_relation="in_taxon"}`. The issue explicitly
  proposed `'occurs in' some Chordata` and the gold used `gci_relation="BFO:0000066"`.
  Using `in_taxon` as the gci_relation expresses a different precondition (the
  late embryonic stage instance being *in* Chordata) than `occurs in`; it is the
  weakest of the relation choices across the attempts and does not match the issue.
- Scope creep: added `property_value: term_tracker_item
  "https://github.com/obophenotype/uberon/issues/3478" xsd:anyURI` to all three
  terms. This is a reasonable provenance convention but not requested by the issue
  and not in the gold; it lowers metadiff precision/recall.
- Serialization artifact: the diff deletes the final trailing blank line of
  uberon-edit.obo (`-` on the last line after `vessel_supplies_blood_to`). This is a
  whitespace/serialization-order artifact from re-serialization, not an intended
  edit, and adds noise to the diff.
- Omission: the gold's definition-text rewrites of `neurula stage` and
  `pharyngula stage` were not made (defensible — not requested in the issue body).
