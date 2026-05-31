---
ontology: go-ontology
issue_number: 31985
pr_number: 31986
eval_repo_pr: 637
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
realignment of GO:0102177, producing a diff byte-identical to attempt #588 (blob
`6ab6948`, F1 0.909, recall 1.000). It omitted the same two gold additions: the EXACT
synonym preserving the retired label and the `term_tracker_item` for #31985. The
biochemical core is fully correct and the PR comment shows strong validation
methodology; the metadiff modestly under-represents quality but the term_tracker
omission is a genuine small completeness gap.

## Strengths

- All five issue tasks executed exactly: name → `4alpha-monomethylsterol monooxygenase
  activity`; def → full RHEA:58868 cytochrome-b5 reaction; def xref → `[PMID:11707264,
  RHEA:58868]` (dropping `GOC:pz`); RHEA xref `58872`→`58868`; MetaCyc
  `RXN-11930`→`RXN-19724`; `is_a` `GO:0016709`→`GO:0016716`.
- Strong, honest methodology in the PR comment: ran `make travis_build` both before
  (baseline) and after edits (both passed), validated `PMID:11707264` with
  `linkml-reference-validator` (resolving it to Darnet, Bard & Rahier 2001), and
  independently checked the external IDs via
  `runoak -i sqlite:obo:rhea info RHEA:58868 RHEA:58872` and
  `runoak -i sqlite:obo:eccode info EC:1.14.18.11 EC:1.14.18.-`.
- Tightly scoped to a single stanza in `src/ontology/go-edit.obo`; no contamination.

## Issues

- Under-editing: did not add the human's
  `synonym: "24-methylenelophenol methyl oxidase activity" EXACT []` (defensible — not
  an issue task).
- Under-editing: also did not add
  `property_value: term_tracker_item ".../issues/31985"`. The gold PR added this; it
  is standard practice to link the resolving issue, and this small completeness gap is
  what places it below the top gpt-5.4 attempts (#605/#548/#652). The realignment
  itself is correct and mergeable.
