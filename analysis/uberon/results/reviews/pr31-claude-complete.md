---
ontology: uberon
issue_number: 3495
pr_number: 3542
eval_repo_pr: 31
agent: std_codex_gpt55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: hard
f1: 0.235
precision: 0.222
recall: 0.250
jaccard: 0.133
outcome: partial_success
failure_modes: [scope_creep, wrong_pattern, under_editing]
case_quality: poor
case_quality_reason: placeholder_id_artifact_plus_reserialization_churn
companion_prs: [3541]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

Lowest-scoring attempt (F1=0.235). The agent added 11 terms (4 colon
epithelium + 7 lamina propria). The seven lamina propria terms have correct
genus and correct part_of targets and correctly omit a duplicated
`relationship: part_of`, but the primary labels use the **inverted**
`lamina propria of {segment}` form (with `{segment} lamina propria` demoted
to a single synonym), and the epithelium half duplicates companion PR #3541's
scope. The low precision/recall is driven by this scope creep plus the
inverted naming and the shared placeholder-ID/reserialization artifacts.

## Strengths

- All seven lamina propria terms present with correct genus UBERON:0000030
  and correct part_of targets across all segments.
- Followed @dosumis's instruction: no duplicated `relationship: part_of`
  on the lamina propria terms.
- Correct definition text pattern; one EXACT synonym per term and consistent
  `dc-contributor` / `dcterms-date` / `term_tracker_item` metadata.
- Reserialized with robot, incidentally reproducing the gold's `seeAlso`
  reordering hunk (alignment with gold noise, not a quality signal).
- The (out-of-scope) epithelium terms use the correct genus UBERON:0001277.

## Issues

- **Scope creep**: four epithelium terms (UBERON:9900000-3) duplicate PR
  #3541's deliverable; gold PR #3542 is lamina-propria-only.
- **Wrong label pattern**: primary label `lamina propria of {segment}`
  inverts the canonical convention. Gold and the UBERON:8600034/8600035
  precedent use `{segment} lamina propria` as the primary label; here that
  form is only a synonym.
- **Under-editing on synonyms**: a single inverted-form synonym per term;
  gold provides two synonyms including the adjectival form.
- The epithelium stanzas add both `is_a` and `intersection_of` for the same
  genus (redundant asserted parent), inconsistent with the equivalent-class-
  only modelling requested.
- Definition dbxref is the issue URL; gold uses an ORCID dbxref (a later
  requirement, partially excusable by timing).
- Placeholder ID range UBERON:9900000-10 vs gold 8600134-140 — standard
  artifact, not a defect.
