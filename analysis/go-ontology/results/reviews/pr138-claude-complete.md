---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 138
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [32023, 32069]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Re-reviewed against issue #32018 + union of human PRs #32021 + #32023 + #32069.
  Gold PR #32021 only covers the taxon-constraint sub-step; metadiff F1=0.0 is not
  meaningful for this case (see cases/pr32021/METADATA.md, case_quality: poor).
  Concurs with existing pr138-codex-complete.md (gpt-5.5). -->

## Summary

The cleanest of the gpt-5.5 trio: a correct, complete go-edit.obo obsoletion of `GO:0052704` and `GO:0140479` (replaced by `GO:0052699`), MetaCyc `narrowMatch` xrefs + #32018 trackers on the parent, both MF `part_of` rewires, and `GO:0052707`/`GO:0052711` cleanups — reproducing and slightly extending human PRs #32023 + #32069, without the spurious `ec.obo`/`comments.txt` edits seen in #171/#153. F1=0.0 is partly a gold-selection artifact; the remaining issue is that the taxon-constraint removal was applied to generated artifacts, not the source TSV.

## Strengths

- Correct, complete obsoletion of both terms with full metadata and trackers; `MetaCyc:PWY-7255`/`PWY-7550` `narrowMatch` xrefs on `GO:0052699`.
- Both dependent MF `part_of` links rewired to `GO:0052699`; `GO:0052707` `replaced_by` corrected; `GO:0052711` also given `replaced_by: GO:0052699` and its stale `GO:0052704` comment fixed — a justified, thorough cleanup of references to the obsoleted term.
- Solid validation/communication: documented `make travis_build` pre/post, reference validation, MetaCyc confirmation; no edits to derived report files (unlike #171/#153).

## Issues

- **Missed the source edit (missed_requirement):** the gold PR #32021 deletes two rows from `src/taxon_constraints/only_in_taxon.tsv`. The agent removed the constraints only from generated outputs (`imports/go_taxon_constraints.owl`, `only_in_taxon.ofn`); with the source TSV unchanged, the build would regenerate them — non-durable.
- **Wrong pattern:** taxon-constraint maintenance must target the source TSV, not the generated OWL/OFN artifacts.
- **Over-editing relative to the curated PR**, though the obsoletion + `GO:0052711` cleanup are reasonable given the issue text.
- **Style (minor):** stripped the `BROAD` synonym + `Wikipedia:Ergothioneine` xref that human #32069 retained.
