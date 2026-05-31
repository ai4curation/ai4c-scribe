---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 218
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes: [missed_requirement, under_editing]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [32023, 32069]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Re-reviewed against issue #32018 + union of human PRs #32021 + #32023 + #32069.
  Gold PR #32021 only covers the taxon-constraint sub-step; metadiff F1=0.0 is not
  meaningful for this case (see cases/pr32021/METADATA.md, case_quality: poor).
  An existing gpt-5 review (pr218-codex-complete.md) reached partial_success; this
  review concurs and adds two findings it missed (GO:0052707 + provenance loss). -->

## Summary

The agent obsoleted `GO:0052704` and `GO:0140479` (replaced by `GO:0052699`) and added both MetaCyc `narrowMatch` xrefs to the parent, but the work is less complete than most attempts on this case: it **missed the `GO:0052707` chained-obsoletion fix** (leaving a `replaced_by` pointing at a now-obsolete term — a `replacedby-obsolete-violation`), **dropped `creation_date`/historical tracker provenance**, and never touched the source `only_in_taxon.tsv`. F1=0.0 is partly a gold-selection artifact, but real defects remain beyond the gold mismatch.

## Strengths

- Correct core obsoletion on both terms (obsolete name/def, comment, `is_obsolete: true`, `replaced_by: GO:0052699`, #32018 tracker).
- Added `MetaCyc:PWY-7255`/`PWY-7550` as `skos:narrowMatch` on `GO:0052699` — matching the issue request and human #32023.
- Rewired the gamma-glutamyl (`GO:0044875`) and hercynylcysteine sulfoxide synthase MF `part_of` links to `GO:0052699`.
- Reasonable PR write-up with rationale and annotation-impact estimate.

## Issues

- **Omission (missed_requirement):** did not update `GO:0052707`, whose `replaced_by` still points at the now-obsolete `GO:0052704`. Human PR #32069 fixed exactly this; leaving it is a `replacedby-obsolete-violation`. The PR comment's claim that it "checked for internal references to obsoleted terms and rewired appropriately" is therefore overstated.
- **Provenance damage (under_editing/regression):** dropped `creation_date` (and the historical #11163 tracker) from `GO:0052704`, and `created_by: pg`/`creation_date` from `GO:0140479`. Obsoletion should preserve this; the human PRs did.
- **Omission (missed_requirement):** did not remove the `only_in_taxon.tsv` rows (gold PR #32021).
- **Style (minor):** stripped the `BROAD` synonym + `Wikipedia:Ergothioneine` xref that human #32069 retained.
