---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 222
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.148
precision: 1.0
recall: 0.08
jaccard: 0.08
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [32023, 32069]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32018
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32021
  Companion human PRs: https://github.com/geneontology/go-ontology/pull/32023
                       https://github.com/geneontology/go-ontology/pull/32069
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/222
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent (gpt-5.4 / codex) fully and correctly resolved issue #32018 in a
single PR: it obsoleted `GO:0052704` and `GO:0140479` (replaced by
`GO:0052699`), added the two requested MetaCyc pathway xrefs as
`skos:narrowMatch` on `GO:0052699`, rewired the dependent molecular-function
`part_of` links to the parent, fixed the downstream `GO:0052707` redirect, and
removed the two `only_in_taxon.tsv` rows. The metadiff F1 of **0.148 severely
under-represents quality**: this is a *poor evaluation case* — the selected
gold PR #32021 is only the taxon-constraint sub-step, and the agent's diff is
in fact semantically equivalent to the **union of the three human PRs**
(#32021 + #32023 + #32069) that actually closed the issue. Outcome: **success**.

## Strengths

- **Complete, correct obsoletion of both terms.** `GO:0052704` and
  `GO:0140479` each got `name: obsolete ...`, `def: "OBSOLETE. ..."`,
  `is_obsolete: true`, and `replaced_by: GO:0052699` — exactly matching the
  human obsoletions in #32069 and #32023 respectively.
- **MetaCyc mapping semantics correct.** Added `xref: MetaCyc:PWY-7255
  {source="skos:narrowMatch"}` and `MetaCyc:PWY-7550 {source="skos:narrowMatch"}`
  to `GO:0052699`, matching #32023 line-for-line and the issue's explicit
  instruction ("add the two MetaCyc xrefs as narrowMatch to GO:0052699").
- **Reference hygiene around obsoletion.** Rewired both dependent MF terms —
  `GO:0044875` (`part_of GO:0052704` → `GO:0052699`) and `GO:0140483`
  (`part_of GO:0140479` → `GO:0052699`) — and fixed obsolete `GO:0052707`'s
  `replaced_by GO:0052704` → `GO:0052699`. Every one of these matches the
  human PRs (#32069 / #32023); none is gratuitous.
- **Included the literal gold-PR change.** Deleted the `GO:0052704` and
  `GO:0140479` rows from `src/taxon_constraints/only_in_taxon.tsv` — identical
  to gold PR #32021.
- **Demonstrated understanding of the multi-PR dependency.** The PR comment
  explicitly notes the taxon-constraint import had to be rebuilt or
  `make travis_build` reuses a stale `imports/go_taxon_constraints.owl` — i.e.
  the agent independently discovered the exact CI dependency that forced the
  humans to land the taxon-constraint removal (#32021) *before* the obsoletion
  could pass. Strong methodology signal; pre- and post-edit `travis_build`
  both passed.
- Added `term_tracker_item` provenance for #32018 on the affected terms,
  consistent with the human PRs.

## Issues

- **Style / minor scope (only real deviation):** while obsoleting
  `GO:0052704` the agent dropped the existing `synonym: "ergothioneine
  biosynthesis from histidine via N-alpha,N-alpha,N-alpha-trimethyl-L-histidine"
  BROAD []` and the `xref: Wikipedia:Ergothioneine`. Human PR #32069
  deliberately **retained** both — GO convention generally preserves
  synonyms/xrefs on obsoleted terms for historical lookup. Low-impact, but a
  genuine difference from the human approach.
- **Comment wording differs (not an error):** the agent's obsoletion comment
  ("...variant ergothioneine biosynthesis pathways are considered out of scope
  for GO process terms; use the broader parent term and capture lineage-specific
  routes via pathway mappings or GO-CAM as needed.") is more explanatory than
  the humans' terse "The reason for obsoletion is that this term represents a
  GO-CAM model." Arguably better documentation; not a defect.
- **No omissions or correctness errors** relative to the issue or the union of
  the three human PRs. The extra ontology edits beyond gold PR #32021 are
  directly mandated by the issue text, not scope creep.

## Case-level note

This case is flagged `case_quality: poor` (see
`cases/pr32021/METADATA.md`). The metadiff target (#32021) covers only the
taxon-constraint cleanup precondition; the full human resolution is
#32021 + #32023 + #32069. All 11 attempts should be judged against the issue
and that union, not the F1 against #32021 — under which 10/11 attempts score
0.000 despite some doing the substantively correct work.
