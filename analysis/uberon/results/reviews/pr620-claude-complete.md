---
ontology: uberon
issue_number: 2421
pr_number: 3659
eval_repo_pr: 620
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
scoring_caveat: "OBO `disjoint_from` is symmetric; gold #3659 asserts it on the UBERON:0000463 stanza in uberon-edit.obo, while the superseded #3151 (curator-directed placement, per anitacaron in the issue) put the equivalent axiom in external-disjoints.obo. This attempt produces the logically identical symmetric axiom in the curator-directed file as a clean new [Term] stanza (byte-identical to attempts #584 and #680, blob f457c1d); whole-file line metadiff scores F1=0.0 purely from cross-file placement, not any logical error. F1 grossly under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent (gpt-5.4/opencode) added a clean new `[Term]` stanza in `src/ontology/components/external-disjoints.obo` with `id: UBERON:0000468 ! multicellular organism` / `disjoint_from: UBERON:0000463 ! organism substance`. The diff is byte-identical to attempts #584 and #680 (blob `f457c1d`). This is the **logically correct symmetric axiom** placed in the file anitacaron explicitly directed in the issue, matching superseded PR #3151. The F1=0.0 is the established serialization/placement metadiff artifact (gold #3659 used the UBERON:0000463 stanza in `uberon-edit.obo`); the score massively under-represents quality. Substantively `success`.

## Strengths

- **Correct logical axiom**: `UBERON:0000468 disjoint_from UBERON:0000463`, logically identical to gold's symmetric assertion. Correct term IDs and labels.
- **Curator-directed placement**: `src/ontology/components/external-disjoints.obo` is exactly where anitacaron pointed ddooley in the issue and where companion PR #3151 placed the equivalent axiom — strongly aligned with the in-issue guidance.
- **Tightly scoped**: single 4-line stanza addition, one file, no serialization churn or extraneous edits.
- Inserted at the same neighborhood (after `UBERON:0000476 ! acellular anatomical structure` / `disjoint_from: CL:0000000 ! cell`) as the other opencode attempts — a sensible, well-grouped location among existing UBERON disjoints.

## Issues

- None of substance. The F1=0.0 is purely a metadiff artifact: a symmetric OWL axiom in a different (curator-directed) file than the single selected gold serialization. Line-based whole-file metadiff cannot detect symmetric-axiom or cross-file placement equivalence. `case_quality: poor` and scoring caveat are recorded in METADATA.md (established 2026-05-16). This attempt confirms the established finding; no new poor signal.
