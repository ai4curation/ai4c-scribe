---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 153
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
  Concurs with existing pr153-codex-complete.md (gpt-5.5). -->

## Summary

Effectively the same solution shape as Attempt 9 / PR #171 (same model/runtime): a correct go-edit.obo obsoletion of `GO:0052704` and `GO:0140479` with MetaCyc `narrowMatch` xrefs on the parent, MF `part_of` rewires and the `GO:0052707`/`GO:0052711` cleanups, but the taxon-constraint cleanup was applied to generated artifacts (`go_taxon_constraints.owl`, `only_in_taxon.ofn`) and derived report files (`ec.obo`, `ec_in_xref.txt`, `comments.txt`) rather than the source `only_in_taxon.tsv`. F1=0.0 is partly a gold-selection artifact; the durability/process problems are real.

## Strengths

- Correct, complete go-edit.obo obsoletion of both terms with full metadata and #32018 trackers; MetaCyc `PWY-7255`/`PWY-7550` `narrowMatch` xrefs on `GO:0052699`.
- Both dependent MF `part_of` links rewired to `GO:0052699`; `GO:0052707`/`GO:0052711` references to the obsoleted term cleaned up — matching/extending human #32023/#32069.
- Identified the taxon-constraint removal need that most attempts on this case missed.

## Issues

- **Missed the source edit (missed_requirement):** did not delete the two rows from `src/taxon_constraints/only_in_taxon.tsv` (the gold PR #32021); removed them only from generated outputs, so the build would regenerate them — non-durable.
- **Wrong pattern:** edited generated/report files (`ec.obo`, `ec_in_xref.txt`, `comments.txt`) that are not source-of-truth — ineffective and noisy.
- **Over-editing relative to the curated PR** (the obsoletion scope itself is issue-justified).
- **Communication:** PR comment is truncated/minimal compared with the strongest attempts.
- **Style (minor):** stripped the `BROAD` synonym + `Wikipedia:Ergothioneine` xref that human #32069 retained.
