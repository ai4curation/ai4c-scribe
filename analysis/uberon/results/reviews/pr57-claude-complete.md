---
ontology: uberon
issue_number: 3478
pr_number: 3479
eval_repo_pr: 57
agent: std_opencode_g55
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

The agent applied the correct overall repair shape — Chordata taxon restriction on
`neurula stage` (UBERON:0000110) and `pharyngula stage` (UBERON:0004707) plus a
GCI conversion on `late embryonic stage` (UBERON:0007220) — but degraded it with
non-requested inline axiom annotations and provenance lines, and a divergent GCI
relation. The low F1 of 0.308 is driven mostly by self-inflicted scope creep
(`{source=...}` annotations and `term_tracker_item`) rather than wrong core logic;
substance is partially correct but noisier than the gold.

## Strengths

- Correctly identified all three target terms and the correct repair strategy:
  tighten `in_taxon` to Chordata (NCBITaxon:7711) and make the `preceded_by`
  pharyngula axiom chordate-conditional via a GCI.
- Documented a sound process: read the imported issue context, inspected terms with
  `obo-grep.pl`, used the checkout/checkin workflow, reserialized and validated OBO
  syntax with `robot convert`.

## Issues

- Scope creep (precision killer): added `{source="https://github.com/obophenotype/uberon/issues/3478"}`
  inline annotations onto the `in_taxon NCBITaxon:7711` axioms of both UBERON:0000110
  and UBERON:0004707, AND added `property_value: term_tracker_item ...` to all three
  terms. The gold made none of these. The inline `source=` on the taxon relationship
  also means the core taxon edits are no longer byte-clean against gold.
- Modeling divergence (wrong_pattern): GCI uses
  `{gci_filler="NCBITaxon:7711", gci_relation="in_taxon", source="..."}`. The issue
  proposed `occurs in` (BFO:0000066); the gold used `gci_relation="BFO:0000066"`.
  `in_taxon` as the GCI differentia is a weaker/different model and additionally
  carries the unrequested `source` annotation.
- Omission: the gold's definition-text rewrites of `neurula stage` and
  `pharyngula stage` were not made (defensible — not in the issue body).
- Identical output to pr38 (blob `be1ace0`); same opencode/gpt-5.5 config produced
  the same diff, so the same critique applies to both.
