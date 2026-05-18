---
ontology: uberon
issue_number: 2421
pr_number: 3659
eval_repo_pr: 640
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
scoring_caveat: "OBO `disjoint_from` is symmetric; gold #3659 asserts it on the UBERON:0000463 stanza in uberon-edit.obo, while the superseded #3151 (curator-directed placement, per anitacaron in the issue) put the equivalent axiom in external-disjoints.obo. This attempt produces the logically identical symmetric axiom in the curator-directed file as a clean new [Term] stanza (blob f457c1d), plus validation via robot convert and ELK reasoning; whole-file line metadiff scores F1=0.0 purely from cross-file placement, not any logical error. F1 grossly under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent (gpt-5.5/opencode) added a clean new `[Term]` stanza in `src/ontology/components/external-disjoints.obo` (`id: UBERON:0000468 ! multicellular organism` / `disjoint_from: UBERON:0000463 ! organism substance`; blob `f457c1d`, identical to #584/#620/#680) and additionally validated with `robot convert` and ELK reasoning. This is the **logically correct symmetric axiom** in the curator-directed file (anitacaron's in-issue guidance; matches superseded PR #3151). F1=0.0 is the established serialization/placement metadiff artifact (gold #3659 used the UBERON:0000463 stanza in `uberon-edit.obo`); it massively under-represents quality. Substantively `success`.

## Strengths

- **Correct logical axiom**: `UBERON:0000468 disjoint_from UBERON:0000463` — symmetric-equivalent to gold. Correct term IDs/labels.
- **Best-documented methodology of the six**: the PR comment shows the agent confirmed term IDs with `obo-grep.pl`, validated OBO syntax with `robot convert`, and ran ELK reasoning over the edited component — directly addressing the issue's core concern (will the disjointness create unsatisfiable classes?). This matches cmungall's in-issue assessment that no problematic entailments arise.
- **Curator-directed placement**: `external-disjoints.obo`, exactly where anitacaron directed ddooley and where companion PR #3151 placed it.
- **Tightly scoped**: committed only `src/ontology/components/external-disjoints.obo`, a single 4-line stanza, no serialization churn.

## Issues

- None of substance. The F1=0.0 is purely a metadiff artifact: a symmetric OWL axiom serialized in the curator-directed file rather than the single selected gold serialization in `uberon-edit.obo`. Line-based whole-file metadiff cannot see symmetric-axiom or cross-file placement equivalence. `case_quality: poor` and scoring caveat are recorded in METADATA.md (established 2026-05-16). This attempt confirms the established finding; no new poor signal.
