---
ontology: uberon
issue_number: 3478
pr_number: 3479
eval_repo_pr: 38
agent: std_opencode_gpt55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.308
precision: 0.250
recall: 0.400
jaccard: 0.182
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern, scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This attempt is byte-identical to pr57 (same output blob `be1ace0`): the same
opencode / gpt-5.5 configuration produced the same diff. It applied the correct
repair shape (Chordata `in_taxon` on UBERON:0000110 and UBERON:0004707, plus a
GCI conversion on UBERON:0007220) but degraded it with unrequested inline `source=`
axiom annotations and `term_tracker_item` provenance lines, and a divergent GCI
relation. F1=0.308 is driven mainly by self-inflicted scope creep, not wrong core
logic. The PR comment additionally claims `robot reason --reasoner ELK` ran clean,
indicating a validation step beyond the pr57 narrative.

## Strengths

- Correctly identified the three target terms and the correct repair strategy:
  tighten `in_taxon` to Chordata (NCBITaxon:7711) and make the `preceded_by`
  pharyngula axiom on `late embryonic stage` chordate-conditional via a GCI.
- Methodology evidence: read imported issue context, inspected stanzas and GCI
  syntax, used `obo-checkout.pl`/`obo-checkin.pl`, reserialized with `robot convert`,
  and reports running `robot reason --reasoner ELK` without errors — good
  validation discipline for a hard axiom-repair case.

## Issues

- Scope creep (precision killer): added inline
  `{source="https://github.com/obophenotype/uberon/issues/3478"}` annotations onto
  the Chordata `in_taxon` axioms of UBERON:0000110 and UBERON:0004707, plus
  `property_value: term_tracker_item ...` on all three terms. None of these are in
  the gold, and the inline `source=` makes the core taxon edits non-byte-clean.
- Modeling divergence (wrong_pattern): GCI uses
  `{gci_filler="NCBITaxon:7711", gci_relation="in_taxon", source="..."}`; the issue
  proposed `occurs in` (BFO:0000066) and the gold used `gci_relation="BFO:0000066"`.
  Note the PR comment text claims `gci_relation="part_of"` but the actual diff emits
  `in_taxon` — a self-inconsistency between narrative and output.
- Omission: definition-text rewrites of `neurula stage` and `pharyngula stage` not
  made (defensible — not requested in the issue body).
- Duplicate of pr57; identical critique applies.
