---
ontology: uberon
issue_number: 3478
pr_number: 3479
eval_repo_pr: 417
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.462
precision: 0.375
recall: 0.600
jaccard: 0.300
outcome: partial_success
failure_modes: [missed_requirement, over_editing]
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
UBERON:0004707 axiom into a Chordata-scoped GCI. The metadiff F1 of 0.462 under-
represents correctness on the issue's two explicit proposals but is also genuinely
depressed by three added `term_tracker_item` provenance lines that the gold PR did
not include. This is a solid, well-scoped resolution of the stated task with a minor
over-edit.

## Strengths

- Both taxon-restriction edits are byte-identical to the gold PR:
  `in_taxon NCBITaxon:6072 ! Eumetazoa` → `in_taxon NCBITaxon:7711 ! Chordata` on
  UBERON:0000110 and UBERON:0004707. This fully satisfies proposal item (1).
- The GCI conversion on UBERON:0007220 is semantically sound: it replaces the
  unconditional `preceded_by UBERON:0004707` with
  `preceded_by UBERON:0004707 {gci_relation="part_of", gci_filler="NCBITaxon:7711"}`.
  The `part_of` differentia is defensible — it mirrors the pre-existing
  `preceded_by RnorDv:0000010 {gci_relation="part_of", gci_filler="NCBITaxon:10116"}`
  GCI already present in the very same UBERON:0007220 stanza, so the agent kept the
  term internally consistent. It is surface-penalized vs the gold's
  `gci_relation="BFO:0000066"` (the IRI form of `occurs in`) but achieves the same
  taxon-constraint-propagation goal the issue targets.
- Strong, grounded methodology: the PR comment cites the same literature as the
  issue (Masak & Davidson 2023, Collazo 2000, Ballard 1964) and explicitly states
  the agent inspected existing taxon-scoped GCIs to match local modeling style. It
  used the `obo-checkout.pl`/`obo-checkin.pl` workflow and honestly reported that
  `robot convert` could not run (not installed in the eval environment) rather than
  silently skipping it.
- Tightly scoped: exactly three term stanzas touched, all issue-relevant; no
  whole-file robot reserialization churn, no unrelated CL label-refresh artifacts.

## Issues

- Over-editing: the agent added `property_value: term_tracker_item
  "https://github.com/obophenotype/uberon/issues/3478" xsd:anyURI` to all three
  edited terms. The gold PR added no such provenance. This is the main extra-edit
  penalty (precision 0.375) and the recall driver alongside the missed defs. It is
  defensible practice (linking edits to the tracking issue) but is not metadiff-
  neutral here and lowers F1 vs an attempt that omitted it.
- Omission: did not reword the textual definitions of `neurula stage` and
  `pharyngula stage` to begin "A chordate developmental stage ...". This is the
  single substantive gap vs the gold and the main recall loss. It is a defensible
  omission since the issue body's proposal items (1) and (2) only request the
  Chordata `in_taxon` restriction and the GCI; the def rewrites appear only in the
  PR author's narrative ("amend their definition accordingly"), not in the issue.
- Net: the issue's explicit asks are fully and correctly resolved; F1=0.462
  reflects the missed optional def polish plus three defensible-but-extra tracker
  lines. Substantively a partial success leaning strong, weaker than pr336/pr279
  only on the added provenance lines.
