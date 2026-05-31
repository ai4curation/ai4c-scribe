---
ontology: uberon
issue_number: 3478
pr_number: 3479
eval_repo_pr: 649
agent: std_opencode_g54
model: openai/gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.500
precision: 0.375
recall: 0.750
jaccard: 0.333
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern]
case_quality: ok
case_quality_reason: gold_pr_genuine_but_metadiff_under_represents_top_attempts
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent correctly executed both explicit asks in issue #3478: it tightened the
`in_taxon` restriction on `neurula stage` (UBERON:0000110) and `pharyngula stage`
(UBERON:0004707) from Eumetazoa (NCBITaxon:6072) to Chordata (NCBITaxon:7711), and
it converted the unconditional `late embryonic stage` (UBERON:0007220) `preceded_by`
UBERON:0004707 axiom into a taxon-scoped GCI. The metadiff F1 of 0.500 over-states
the GCI quality slightly: the agent encoded the GCI differentia as
`gci_relation="in_taxon"`, which is a genuinely weaker/different model than the
issue's proposed `occurs in` some Chordata. Tightly scoped otherwise, with a
benign EOF whitespace artifact from robot reserialization.

## Strengths

- Both taxon-restriction edits are byte-identical to the gold PR:
  `in_taxon NCBITaxon:6072 ! Eumetazoa` → `in_taxon NCBITaxon:7711 ! Chordata` on
  UBERON:0000110 and UBERON:0004707, fully satisfying proposal item (1).
- The GCI conversion correctly removes the unconditional global
  `preceded_by UBERON:0004707` link and replaces it with a taxon-qualified GCI
  filler `NCBITaxon:7711` (Chordata), preserving the chordate developmental
  ordering without leaking it into the general `late embryo`/`late embryonic stage`
  classes — the precise structural fix the issue requested.
- Tight scope: exactly the three issue-relevant term stanzas plus one trailing-
  newline change; no `term_tracker_item` over-editing (unlike pr417), no unrelated
  CL label-refresh churn.
- Honest, reproducible methodology reported in the PR comment: inspected the
  affected stanzas, checked existing GCI style, used the obo-checkout/checkin
  workflow, and ran `robot convert` reserialization.

## Issues

- Wrong pattern (GCI differentia): the GCI uses
  `{gci_relation="in_taxon", gci_filler="NCBITaxon:7711"}`. The issue explicitly
  proposed `('late embryonic stage' and 'occurs in' some Chordata) SubClassOf
  'preceded by' some 'pharyngula stage'`, and the gold encodes this as
  `gci_relation="BFO:0000066"` (the IRI of `occurs in`). Using `in_taxon` as the
  GCI antecedent differentia is semantically a different (weaker) model than
  `occurs in` — this is a fair penalty, distinct from the merely surface-level
  `occurs_in` vs `BFO:0000066` label/IRI difference seen in the top-tier
  pr336/pr279 attempts. The structural decoupling goal is still achieved, but the
  axiom shape does not match the issue's stated model.
- Omission: did not reword the textual definitions of `neurula stage` and
  `pharyngula stage` to "A chordate developmental stage ...". Defensible (issue
  proposal items 1–2 do not request def rewrites; only the PR author's narrative
  does), but it is the main recall loss vs the gold.
- Minor cosmetic: removed the trailing blank line at EOF (the
  `vessel_supplies_blood_to` stanza, ~line 226040) — a `robot convert` whole-file
  reserialization whitespace artifact, harmless and not contamination (it is
  localized to one EOF line, not a foreign edit block).
- Net: issue's explicit asks resolved structurally; F1=0.500 is roughly accurate
  here — the missed optional defs are offset by the weaker `in_taxon` GCI model, so
  this attempt sits below the `occurs_in`-using pr336/pr279 on substance despite the
  identical headline F1.
