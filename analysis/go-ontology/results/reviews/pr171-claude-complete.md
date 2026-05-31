---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 171
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern, over_editing]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [32023, 32069]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Re-reviewed against issue #32018 + union of human PRs #32021 + #32023 + #32069.
  Gold PR #32021 only covers the taxon-constraint sub-step; metadiff F1=0.0 is not
  meaningful for this case (see cases/pr32021/METADATA.md, case_quality: poor).
  Concurs with existing pr171-codex-complete.md (gpt-5.5). -->

## Summary

The agent did a correct go-edit.obo obsoletion of `GO:0052704` and `GO:0140479` (replaced by `GO:0052699`, MetaCyc `narrowMatch` xrefs on the parent, MF `part_of` rewires, `GO:0052707`/`GO:0052711` cleanups) — but it tried to do the taxon-constraint cleanup in the **wrong place**: it deleted constraints from generated artifacts (`imports/go_taxon_constraints.owl`, `only_in_taxon.ofn`) and also edited derived/report files (`ec.obo`, `ec_in_xref.txt`, `comments.txt`) while leaving the source `only_in_taxon.tsv` untouched. F1=0.0 is partly a gold-selection artifact, but the durability/process problems are real.

## Strengths

- Correct, complete go-edit.obo obsoletion of both terms with full metadata and #32018 trackers; MetaCyc `PWY-7255`/`PWY-7550` `narrowMatch` xrefs on `GO:0052699`.
- Rewired both dependent MF `part_of` links to `GO:0052699` and updated `GO:0052707`/`GO:0052711` so they no longer point at the now-obsolete `GO:0052704` — matching/extending human #32023/#32069.
- Recognized that the taxon constraints on the obsoleted terms needed to be removed (most attempts missed this entirely) and documented an annotation-impact check.

## Issues

- **Missed the source edit (missed_requirement):** the gold PR #32021 deletes two rows from `src/taxon_constraints/only_in_taxon.tsv`. The agent removed the constraints only from generated outputs (`go_taxon_constraints.owl`, `only_in_taxon.ofn`); since the source TSV is unchanged, the next build regenerates them — the fix is non-durable.
- **Wrong pattern / instruction violation:** edited generated and report artifacts (`ec.obo`, `ec_in_xref.txt`, `comments.txt`) that are not hand-maintained source. These changes are ineffective and noise; the correct source is `go-edit.obo` (+ the taxon-constraint TSV).
- **Over-editing relative to the curated solution**, though the obsoletion scope itself is justified by the issue text.
- **Style (minor):** stripped the `BROAD` synonym + `Wikipedia:Ergothioneine` xref that human #32069 retained.
