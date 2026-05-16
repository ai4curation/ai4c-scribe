---
ontology: go-ontology
issue_number: 31985
pr_number: 31986
eval_repo_pr: 409
agent: std_claude_haiku45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: ai4curation/go-ontology-agent-config@v9
case_type: reclassification
difficulty: hard
f1: 0.909
precision: 0.833
recall: 1.000
jaccard: 0.833
outcome: success
failure_modes:
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Haiku-4.5 on the claude runtime executed all five explicit issue tasks for GO:0102177
exactly and correctly, producing a diff blob (`6ab6948f4`) identical to the sonnet
claude run #479. The diff is a strict subset of the human resolution, omitting both
the unrequested EXACT synonym and the `term_tracker_item` for #31985. F1 0.909
(recall 1.000) accurately reflects a correct-but-incomplete-vs-human outcome and
slightly under-represents quality given both omissions are housekeeping items not in
the task list. Strong result for the smallest model in the cohort on a hard case.

## Strengths

- All five issue tasks executed exactly: name → `4alpha-monomethylsterol monooxygenase
  activity`; def → full RHEA:58868 cytochrome-b5 reaction; def xref →
  `[PMID:11707264, RHEA:58868]` (drops `GOC:pz`); RHEA xref `58872`→`58868`; MetaCyc
  `RXN-11930`→`RXN-19724`; `is_a` `GO:0016709`→`GO:0016716`.
- MetaCyc xref correctly left unqualified, matching gold and GO convention.
- Clear PR comment with per-field before/after and rationale, correctly identifying
  the cytochrome-b5 (not NAD(P)H) donor as the basis for the GO:0016709→GO:0016716
  reparent.

## Issues

- Omission: did not add `synonym: "24-methylenelophenol methyl oxidase activity"
  EXACT []` preserving the retired label (human added it unprompted).
- Omission: did not add `property_value: term_tracker_item ".../issues/31985"`. The
  checklist claims "Term tracker item reference maintained" but only the pre-existing
  #30193 tracker was kept; the new #31985 tracker (standard GO convention for
  issue-driven edits, present in gold) was not added.
- Both omissions are outside the issue's explicit five-task list; the realignment
  substance is fully correct. Classed as `under_editing`.
