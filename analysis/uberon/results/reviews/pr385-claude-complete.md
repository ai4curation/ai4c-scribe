---
ontology: uberon
issue_number: 2421
pr_number: 3659
eval_repo_pr: 385
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
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
scoring_caveat: "OBO `disjoint_from` is symmetric; gold #3659 asserts it on the UBERON:0000463 stanza in uberon-edit.obo, while the superseded #3151 (curator-directed placement, per anitacaron in the issue) put the equivalent axiom in external-disjoints.obo. This attempt produces the logically identical symmetric axiom in the curator-directed file as a clean new [Term] stanza (blob 659d1ea, inserted near UBERON:0002470); whole-file line metadiff scores F1=0.0 purely from cross-file placement, not any logical error. F1 grossly under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent (gpt-5.4/codex) added a clean new `[Term]` stanza in `src/ontology/components/external-disjoints.obo` (`id: UBERON:0000468 ! multicellular organism` / `disjoint_from: UBERON:0000463 ! organism substance`; blob `659d1ea`, inserted after the `UBERON:0002470 ! autopod region` stanza). This is the **logically correct symmetric axiom** in the curator-directed file (anitacaron's in-issue guidance; matches superseded PR #3151). F1=0.0 is the established serialization/placement metadiff artifact (gold #3659 used the UBERON:0000463 stanza in `uberon-edit.obo`); it massively under-represents quality. Substantively `success`.

## Strengths

- **Correct logical axiom**: `UBERON:0000468 disjoint_from UBERON:0000463` — symmetric-equivalent to gold's assertion. Correct term IDs and labels.
- **Sound reasoning in the PR comment**: explicitly explained the disjointness makes substance-as-organism reuse patterns unsatisfiable, consistent with the issue's QC goal and cmungall's in-issue ruling that this is "completely reasonable and straightforward" with no problematic entailments.
- **Curator-directed placement**: chose `external-disjoints.obo`, exactly where anitacaron pointed ddooley and where companion PR #3151 placed the equivalent axiom.
- **Tightly scoped**: single 4-line stanza, one file, no serialization churn or out-of-scope edits.
- **Honest about validation limits**: transparently reported that `robot` was not installed in the environment so the `robot convert` syntax check could not be run, rather than silently skipping or fabricating it.

## Issues

- None of substance. The F1=0.0 is purely a metadiff artifact: a symmetric OWL axiom serialized in the curator-directed file rather than the single selected gold serialization. The stanza insertion point differs from the opencode attempts (after `UBERON:0002470` vs after `UBERON:0000476`), but OBO term order is not semantically significant. Line-based whole-file metadiff cannot detect symmetric-axiom or cross-file placement equivalence. The only minor process gap (couldn't run `robot` validation) was due to a missing environment binary, not agent error, and was disclosed. `case_quality: poor` and scoring caveat recorded in METADATA.md (established 2026-05-16); no new poor signal.
