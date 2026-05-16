---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 286
agent: std_opencode_k26
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes: [missed_requirement]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [32023, 32069]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Re-reviewed against issue #32018 + union of human PRs #32021 + #32023 + #32069.
  Gold PR #32021 only covers the taxon-constraint sub-step; metadiff F1=0.0 is not
  meaningful for this case (see cases/pr32021/METADATA.md, case_quality: poor). -->

## Summary

A correct, complete go-edit.obo obsoletion of `GO:0052704` and `GO:0140479` (replaced by `GO:0052699`), with both MetaCyc `narrowMatch` xrefs + trackers on the parent, both MF `part_of` rewires, the `GO:0052707` redirect fix, and an additional `GO:0052711` comment cleanup — reproducing and slightly extending the go-edit.obo content of human PRs #32023 + #32069. F1=0.0 is a gold-selection artifact. The gap is the untouched source `only_in_taxon.tsv`.

## Strengths

- Full, correct obsoletion metadata on both terms; preserved the historical #11163 tracker on `GO:0052704` (better than several other attempts that dropped it).
- `MetaCyc:PWY-7255`/`PWY-7550` `narrowMatch` xrefs + #32018 tracker on `GO:0052699`; both MF `part_of` links rewired; `GO:0052707` `replaced_by` corrected — matching human #32023/#32069.
- **Justified extra edit:** also updated the `GO:0052711` obsoletion comment that still pointed at `GO:0052704`, removing another stale reference to a now-obsolete term. Defensible cleanup directly caused by this obsoletion.
- Reported `robot convert`/`reason` and enumerated SPARQL QC checks (`obsolete-reference-violation`, `replacedby-obsolete-violation`, etc.) passing.

## Issues

- **Omission (missed_requirement):** did not remove the `GO:0052704`/`GO:0140479` rows from `src/taxon_constraints/only_in_taxon.tsv` — the literal gold PR #32021 and a required CI precondition for obsoleting these taxon-constrained terms.
- **Style (minor):** stripped the `BROAD` synonym and `Wikipedia:Ergothioneine` xref from `GO:0052704`; human PR #32069 retained both. Recurring pattern across this case.
