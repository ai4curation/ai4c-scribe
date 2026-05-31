---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 358
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
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

The strongest non-#222 attempt on substance and communication. The agent did a correct, clean full obsoletion of `GO:0052704` and `GO:0140479` (replaced by `GO:0052699`), added both MetaCyc `narrowMatch` xrefs, rewired the two MF `part_of` links, and fixed the `GO:0052707` chained-obsoletion redirect — reproducing the go-edit.obo content of human PRs #32023 + #32069 with a high-quality PR write-up (annotation-migration plan, the exact QC rule it was guarding against, `robot convert`/`reason`/`verify` all 16 checks passing). F1=0.0 is purely a gold-selection artifact. The one substantive gap is the same as most attempts: the source taxon-constraint cleanup.

## Strengths

- Correct, minimal obsoletion edits on both terms; explicitly reasoned about and prevented the `replacedby-obsolete-violation` by fixing `GO:0052707` `replaced_by` → `GO:0052699`.
- `MetaCyc:PWY-7255`/`PWY-7550` `narrowMatch` xrefs on `GO:0052699`; both dependent MF `part_of` links rewired to the parent — matching human #32023/#32069.
- Best-in-case methodology/communication: full `robot` reasoning + 16 SPARQL QC checks reported passing, annotation-migration note (4 EXP / 0 EXP), honest disclosure of the `travis_build` environment limitation.
- The synonym/Wikipedia-xref removal was at least explicitly reasoned ("redundant with the same xref on the parent"), unlike most attempts that stripped it silently.

## Issues

- **Omission (missed_requirement):** did not remove the `only_in_taxon.tsv` rows — the literal gold PR #32021. Notably, the checklist explicitly marked `/taxon-constraint: N/A`, so the agent considered taxon constraints and wrongly dismissed them. This is the precise blind spot for this case: obsoleting a taxon-constrained term without removing its `only_in_taxon` entry leaves a dangling constraint on an obsolete class.
- **Minor:** dropped the historical `term_tracker_item` for #11163 from `GO:0052704`, and did not add a #32018 tracker to the parent `GO:0052699` (human #32023 did). Low impact.
- **Style (minor):** removed the `BROAD` synonym + `Wikipedia:Ergothioneine` xref that human #32069 retained — defensible here given the explicit rationale, but still a deviation from the human approach.
