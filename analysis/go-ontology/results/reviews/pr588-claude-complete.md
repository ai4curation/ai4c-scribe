---
ontology: go-ontology
issue_number: 31985
pr_number: 31986
eval_repo_pr: 588
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/go-ontology-agent-config@v9
case_type: reclassification
difficulty: hard
case_quality: good
f1: 0.909
precision: 0.833
recall: 1.000
jaccard: 0.833
outcome: partial_success
failure_modes:
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent correctly executed all five explicit issue tasks for the EC:1.14.18.11
realignment of GO:0102177 (blob `6ab6948`, F1 0.909, recall 1.000). It is slightly
behind the top gpt-5.4 attempts (#605/#548/#652) because it omitted **two** gold
additions rather than one: both the EXACT synonym preserving the retired label *and*
the `term_tracker_item` for issue #31985. The biochemical core is fully correct;
the metadiff modestly under-represents quality but the term_tracker omission is a
genuine (small) completeness gap.

## Strengths

- All five issue tasks executed exactly: name → `4alpha-monomethylsterol monooxygenase
  activity`; def → full RHEA:58868 cytochrome-b5 reaction; def xref → `[PMID:11707264,
  RHEA:58868]` (correctly dropping `GOC:pz`); RHEA xref `58872`→`58868`; MetaCyc
  `RXN-11930`→`RXN-19724`; `is_a` `GO:0016709`→`GO:0016716` (matching EC:1.14.18.-).
- Correctly identified RHEA:58872 as the partial reaction inappropriate as an
  exact-match xref, consistent with the issue's diagnosis.
- Tightly scoped to a single stanza in `src/ontology/go-edit.obo`; no base
  contamination, no collateral edits.

## Issues

- Under-editing: did not add the human's
  `synonym: "24-methylenelophenol methyl oxidase activity" EXACT []` (defensible — not
  an issue task).
- Under-editing: also did not add
  `property_value: term_tracker_item ".../issues/31985"`. The gold PR added this and it
  is standard practice to link the resolving issue. This is a small but real
  completeness gap that distinguishes it from the higher-scoring #605/#548/#652. The
  biochemical realignment itself is correct and mergeable.
