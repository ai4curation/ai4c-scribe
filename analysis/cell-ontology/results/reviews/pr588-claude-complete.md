---
ontology: cell-ontology
issue_number: 3453
pr_number: 3556
eval_repo_pr: 588
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.125
precision: 0.125
recall: 0.125
jaccard: 0.067
outcome: partial_success
failure_modes:
  - wrong_term
  - missed_requirement
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/obophenotype/cell-ontology/issues/3453
  Human PR (ground truth): https://github.com/obophenotype/cell-ontology/pull/3556
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-cl/pull/588
  Agent config: ai4curation/cl-agent-config
-->

## Summary

This run (gpt-5.4 / opencode) is byte-identical in its ontology diff to eval PR #526 (same blob `b4b7a88`, same `2026-05-17T00:59:23Z` timestamp), and the same assessment applies: correct biological content (labels, definitions, synonyms, PMIDs, ORCIDs, PD-1 marker, lineage parents) but wrong CL IDs (`CL_9900001`/`CL_9900002` vs gold `CL_9900000`/`CL_9900001`) and deliberate omission of the `CL_0011025` exhausted-T-cell parent the curator added in the issue thread. F1=0.125 under-represents conceptual correctness but the off-by-one IDs and the missing exhausted-T-cell link are real defects requiring curator cleanup. Not a poor case — gold #3556 is a clean single-PR reference (METADATA `case_quality: ok`).

## Strengths

- Both requested terms created with correct labels and definitions matching the issue (including @scheuerm's "as a result of" wording and the CD4/CD8 transcription-factor distinctions).
- Correct PD-1 protein `PR_000001919` via `RO_0002104` (`has_plasma_membrane_part`), matching gold's protein choice.
- Correct lineage parents `CL_0000624` / `CL_0000625`.
- Full metadata: `IAO_0000233` to issue #3453 (IRI form), both ORCID contributors, `terms:creator`, `terms:date`, 3 exact synonyms per term.
- Avoided the PMID:35880649 red herring flagged by the curator.
- Includes an articulate PR comment documenting research steps and the (mistaken) rationale for not using `CL_0011025`; methodology is transparent even where the conclusion diverges from the curator.

## Issues

- **Wrong ID allocation (dominant scoring driver):** `CL_9900001`/`CL_9900002` instead of gold `CL_9900000`/`CL_9900001`; the off-by-one propagates into every axiom line, driving F1=0.125.
- **Missed requirement:** no `SubClassOf` to `CL_0011025` (exhausted T cell). The PR comment explicitly argues against this parent ("the issue discussion explicitly called out that these new lineage-defined subsets should not be modeled under it"), but that misreads the thread: the placement note objects only to `CL_0011025` as the *asserted lineage parent*, while curator Caroline-99 explicitly added a `SubClassOf "exhausted T cell"` link and gold retained it. The agent dropped a curator-mandated axiom.
- **Pattern divergence:** two plain asserted `SubClassOf` axioms instead of gold's `EquivalentClasses` defined class + `is_inferred "true"` lineage SubClassOf.
- **Convention drift:** exact synonyms PMID-annotated whereas gold leaves them bare; defensible but adds metadiff distance.
</content>
