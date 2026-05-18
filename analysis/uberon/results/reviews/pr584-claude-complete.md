---
ontology: uberon
issue_number: 2421
pr_number: 3659
eval_repo_pr: 584
agent: std_opencode_gpt55
model: gpt-5.5
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
scoring_caveat: "OBO `disjoint_from` is symmetric; gold #3659 asserts it on the UBERON:0000463 stanza in uberon-edit.obo, while the superseded #3151 (curator-directed placement, per anitacaron in the issue: 'the disjoint file is at src/ontology/components/external-disjoints.obo') put the equivalent axiom in external-disjoints.obo. This attempt produces the logically identical symmetric axiom in the curator-directed file as a clean new [Term] stanza; whole-file line metadiff scores F1=0.0 purely from cross-file placement, not any logical error. F1 grossly under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent (gpt-5.5/opencode) added a clean new `[Term]` stanza in `src/ontology/components/external-disjoints.obo` asserting `id: UBERON:0000468 ! multicellular organism` / `disjoint_from: UBERON:0000463 ! organism substance`. This is the **logically correct symmetric axiom** and is placed in exactly the file uberon member anitacaron explicitly directed in the issue thread, matching superseded PR #3151's placement. The F1=0.0 is entirely the established serialization/placement metadiff artifact (gold #3659 asserted the symmetric equivalent on the UBERON:0000463 stanza in `uberon-edit.obo`); the score massively under-represents quality. Substantively `success`.

## Strengths

- **Correct logical axiom**: `UBERON:0000468 disjoint_from UBERON:0000463`. Because `disjoint_from` is symmetric, this is logically identical to gold's `UBERON:0000463 disjoint_from UBERON:0000468`. Both term IDs and labels are correct.
- **Curator-directed file placement**: used `src/ontology/components/external-disjoints.obo`, which is exactly where anitacaron pointed ddooley in the issue ("the disjoint file is at `src/ontology/components/external-disjoints.obo`") and where the superseded companion PR #3151 placed it. This is arguably more aligned with the in-issue guidance than the merged gold's `uberon-edit.obo` placement.
- **Tightly scoped**: a single 4-line addition to one file, no serialization churn, no gratuitous edits — consistent with the `tightly_scoped` task type.
- Logically sound per cmungall's in-issue assessment that disjointness here introduces no problematic parthood/connectedness entailments and should not create unsatisfiable classes.

## Issues

- None of substance. The F1=0.0 is purely a metadiff artifact: a symmetric OWL axiom serialized in a different (curator-directed) file from the single selected gold serialization. Whole-file line-based metadiff cannot see symmetric-axiom or cross-file placement equivalence. The `case_quality: poor` flag and scoring caveat are recorded in METADATA.md (established 2026-05-16); this attempt confirms the established finding and introduces no new poor signal.
