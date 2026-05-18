---
ontology: uberon
issue_number: 2421
pr_number: 3659
eval_repo_pr: 450
agent: std_opencode_kimik26
model: kimi-k2.6
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
scoring_caveat: "OBO `disjoint_from` is symmetric; gold #3659 asserts it on the UBERON:0000463 stanza in uberon-edit.obo, while the superseded #3151 (curator-directed placement, per anitacaron in the issue) put the equivalent axiom in external-disjoints.obo. This attempt produces the logically identical symmetric axiom in the curator-directed file as a clean new [Term] stanza (blob e2a9fc4, identical to claude attempts #299/#174); whole-file line metadiff scores F1=0.0 purely from cross-file placement, not any logical error. F1 grossly under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent (kimi-k2.6/opencode) added a clean new `[Term]` stanza in `src/ontology/components/external-disjoints.obo` (`id: UBERON:0000468 ! multicellular organism` / `disjoint_from: UBERON:0000463 ! organism substance`; blob `e2a9fc4`, byte-identical to the sonnet-4.5 #299 and haiku-4.5 #174 attempts). This is the **logically correct symmetric axiom** in the curator-directed file (anitacaron's in-issue guidance; matches superseded PR #3151). F1=0.0 is the established serialization/placement metadiff artifact (gold #3659 used the UBERON:0000463 stanza in `uberon-edit.obo`); it massively under-represents quality. Substantively `success`.

## Strengths

- **Correct logical axiom**: `UBERON:0000468 disjoint_from UBERON:0000463` — symmetric-equivalent to gold. Correct term IDs and labels.
- **Strongest rationale of the six**: the PR comment correctly frames the QC purpose, cites the concrete `'human milk' EquivalentTo 'milk' and 'Homo sapiens'` failure mode from the issue body, names FoodOn as the downstream reuser, and explicitly notes "no unsatisfiable classes introduced … per cmungall's assessment" — accurately reflecting cmungall's in-issue ruling.
- **Curator-directed placement**: `external-disjoints.obo`, exactly where anitacaron directed ddooley and where companion PR #3151 placed it.
- **Tightly scoped**: single 4-line stanza, one file, no serialization churn.

## Issues

- None of substance. The F1=0.0 is purely a metadiff artifact: a symmetric OWL axiom serialized in the curator-directed file rather than the single selected gold serialization in `uberon-edit.obo`. Line-based whole-file metadiff cannot see symmetric-axiom or cross-file placement equivalence. `case_quality: poor` and scoring caveat are recorded in METADATA.md (established 2026-05-16). This attempt confirms the established finding; no new poor signal.
