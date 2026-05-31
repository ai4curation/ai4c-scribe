---
ontology: go-ontology
issue_number: 31963
pr_number: 32006
eval_repo_pr: 666
agent: std_opencode_gpt5.4
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: definition_update
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
case_quality: poor
case_quality_reason: gold_pr_is_partial_and_eval_base_already_contains_gold
companion_prs:
  - 32009
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Run on eval base `8a93e3d09` (go-edit.obo blob `8262d5a8a`) where the gold #32006
`GO:0102067` def is already pre-applied, so F1=0.0 vs #32006 is the documented
base-state / partial-gold artifact. The agent's go-edit.obo diff is byte-identical to
attempt #660 (same head blob `7070a10`): it correctly obsoletes `GO:0045550`,
substantively reproducing companion gold PR #32009, but also bundles the same large
off-topic `GO:0018581`/`GO:0047074` obsoletion. Scored `partial_success` for the same
reason as #660 — correct on the real issue task, undermined by unrelated over-editing.

## Strengths

- Correct interpretation of the issue: recognized the def update was already done and
  that the outstanding task per raymond91125's later comment was obsoleting
  `GO:0045550`. The agent's PR comment explicitly frames this as the obsoletion step.
- `GO:0045550` obsoletion matches companion gold #32009 substantively: name → `obsolete
  geranylgeranyl reductase activity`; `OBSOLETE.` def prefix retaining `[PMID:9492312]`;
  `is_a: GO:0016491` removed; `is_obsolete: true`; `replaced_by: GO:0102067`;
  obsoletion comment; `term_tracker_item ".../issues/31963"`. Correct GO obsoletion
  pattern and correct replacement target.
- `GO:0102067` left untouched (already at gold def state in base) — appropriate.
- Reasonable documented methodology (term-search of GO:0045550/GO:0102067, design-pattern
  review, pre/post `make travis_build`).

## Issues

- **Significant off-topic over-editing (scope creep):** identical to #660 — obsoletes
  `GO:0018581` → `replaced_by: GO:0047074` and renames `GO:0047074`, plus removes the
  `GO_0018581` participant block in `go-catalytic-activities-participants.owl`. These
  terms are active in the eval base; the edit is agent-introduced and tied to unrelated
  issues #25870/#30193, not #31963. Substantial unrequested change that would draw
  review objection.
- Obsoletion comment is terser than gold #32009's fuller EC/RHEA/PMID rationale — minor
  style.
- Metadiff F1=0.0 under-represents the correct obsoletion work (vs #32009) and cannot
  isolate the genuine over-edit defect; judge on substance per the case poor-quality
  flag.
