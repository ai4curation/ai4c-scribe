---
ontology: go-ontology
issue_number: 31985
pr_number: 31986
eval_repo_pr: 605
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/go-ontology-agent-config@v9
case_type: reclassification
difficulty: hard
case_quality: good
f1: 0.957
precision: 0.917
recall: 1.000
jaccard: 0.917
outcome: success
failure_modes:
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent fully realigned GO:0102177 to EC:1.14.18.11, executing all five explicit
issue tasks correctly and also adding the `term_tracker_item` for issue #31985 that
the human added. Recall is 1.000 (every gold line reproduced); the F1 0.957 / precision
0.917 shortfall comes entirely from the one gold line the agent did *not* add — the
EXACT synonym preserving the retired label — which was not part of the issue task
list. The metadiff slightly under-represents quality.

## Strengths

- All five issue tasks executed exactly: name → `4alpha-monomethylsterol monooxygenase
  activity`; def → the full RHEA:58868 cytochrome-b5 reaction; def xref → `[PMID:11707264,
  RHEA:58868]` (correctly dropping the unnecessary `GOC:pz`); RHEA xref
  `58872`→`58868`; MetaCyc `RXN-11930`→`RXN-19724`; `is_a` `GO:0016709`→`GO:0016716`
  (NAD(P)H-donor branch → "another compound as one donor" branch matching EC:1.14.18.-).
- Correctly diagnosed and acted on the issue's core observation that RHEA:58872 is the
  partial subreaction `part_of` the full RHEA:58868, so it was an inappropriate
  exact-match xref.
- Added `property_value: term_tracker_item ".../issues/31985"` while preserving the
  historical #30193 tracker — matching the gold PR.
- Tightly scoped: single file (`src/ontology/go-edit.obo`), single term stanza, no
  collateral edits, no base contamination.

## Issues

- Minor under-editing: the human PR additionally added
  `synonym: "24-methylenelophenol methyl oxidase activity" EXACT []` to preserve the
  retired label for downstream label resolution. This attempt did not. It is a
  defensible omission — preserving an old label as an EXACT synonym is good curation
  practice but was not in the issue's explicit task list, so this is a style/completeness
  gap rather than an error. The biochemical realignment is fully correct and mergeable.
