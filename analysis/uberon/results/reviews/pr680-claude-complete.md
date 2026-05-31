---
ontology: uberon
issue_number: 2421
pr_number: 3659
eval_repo_pr: 680
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: axiom_repair
difficulty: medium
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: owl_serialization_placement_artifact
companion_prs: [3151]
scoring_caveat: "OBO `disjoint_from` is symmetric; gold #3659 asserts it on the UBERON:0000463 stanza in uberon-edit.obo, while the superseded #3151 (curator-directed placement, per anitacaron in the issue) put the equivalent axiom in external-disjoints.obo. This attempt produces the logically identical symmetric axiom in the curator-directed file as a clean new [Term] stanza (blob f457c1d, identical to #584/#620), with robot convert validation of both the component and uberon-edit.obo; whole-file line metadiff scores F1=0.0 purely from cross-file placement, not any logical error. F1 grossly under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent (gpt-5.4/opencode) added a clean new `[Term]` stanza in `src/ontology/components/external-disjoints.obo` (`id: UBERON:0000468 ! multicellular organism` / `disjoint_from: UBERON:0000463 ! organism substance`; blob `f457c1d`, identical to #584/#620) and validated both the edited component and `uberon-edit.obo` with `robot convert`. This is the **logically correct symmetric axiom** in the curator-directed file (anitacaron's in-issue guidance; matches superseded PR #3151). F1=0.0 is the established serialization/placement metadiff artifact (gold #3659 used the UBERON:0000463 stanza in `uberon-edit.obo`); it massively under-represents quality. Substantively `success`.

## Strengths

- **Correct logical axiom**: `UBERON:0000468 disjoint_from UBERON:0000463` — symmetric-equivalent to gold. Correct term IDs and labels.
- **Good validation**: ran `robot convert` on both the edited `external-disjoints.obo` component and the main `uberon-edit.obo` to confirm both still parse — sound methodology for a foundational disjointness change, consistent with cmungall's in-issue point that no problematic entailments should arise.
- **Curator-directed placement**: `external-disjoints.obo`, exactly where anitacaron directed ddooley and where companion PR #3151 placed it.
- **Tightly scoped**: single 4-line stanza, one file, no serialization churn or out-of-scope edits.

## Issues

- None of substance. The F1=0.0 is purely a metadiff artifact: a symmetric OWL axiom serialized in the curator-directed file rather than the single selected gold serialization in `uberon-edit.obo`. Line-based whole-file metadiff cannot detect symmetric-axiom or cross-file placement equivalence. Minor: the issue-comment commit message ("Add disjoint axiom for organism substance") is slightly underspecified vs the change, but inconsequential. `case_quality: poor` and scoring caveat recorded in METADATA.md (established 2026-05-16); no new poor signal.
