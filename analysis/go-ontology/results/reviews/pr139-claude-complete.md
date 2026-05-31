---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 139
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.5
precision: 1.0
recall: 0.333
jaccard: 0.333
outcome: success
failure_modes:
- scope_creep
case_quality: poor
case_quality_reason: base_contamination_GO_0102067
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

A repeat run of the same model/runtime as #169 with an identical resulting
diff (same head blob `59ca8d7`): the agent produced the exact gold
`GO:0140597` definition from human PR #32007 (`"Directly binding to a protein
and delivering it either to an acceptor molecule or to a specific location."`
[PMID:7628437]) plus a full `GO:0140309` holdase rewrite (parent-aligned
wording, "delivers" grammar fix, and the "an holdase" → "a holdase" comment
correction). The metadiff F1 of 0.500 **under-represents** the core edit (the
`GO:0102067` precision hit is base contamination, not an agent error); the
`GO:0140309` expansion is a genuine scope extension beyond gold #32007.

## Strengths

- `GO:0140597` definition byte-identical to gold PR #32007, with
  `PMID:7628437` preserved and synonyms/logical-definition/parentage
  unchanged.
- The `GO:0140309` edits are individually defensible curation: child/parent
  harmonization, a real grammar-bug fix ("it's being delivers"), and a valid
  article correction ("an holdase" → "a holdase").
- Reproducible behavior across the two gpt-5.5/opencode runs (#169, #139) is a
  positive consistency signal.
- No spurious changes to logical axioms, parentage, synonyms, or xrefs.

## Issues

- This attempt file contains only the diff (no PR/issue narrative), so process
  evidence (validation, research) cannot be assessed; judged on the diff,
  which is correct on the core ask.
- Scope: gold PR #32007 changed only `GO:0140597`; the broad `GO:0140309`
  rewrite plus comment edit is beyond the selected gold (round-1 holdase fix
  was already in the eval base via PR #31602). Defensible cleanup but the
  reason recall is below the 0.667 attempts.
- The diff also contains the unrelated `GO:0102067` geranylgeranyl change;
  this is eval base/scaffold contamination from source PR #32006 (identical
  across all 12 attempts), not an agent edit, and should not be charged
  against this run.
