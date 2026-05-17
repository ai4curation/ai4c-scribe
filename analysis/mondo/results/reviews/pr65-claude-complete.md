---
ontology: mondo
issue_number: 9859
pr_number: 10219
eval_repo_pr: 65
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: reclassification
difficulty: hard
f1: 0.091
precision: 0.049
recall: 0.667
jaccard: 0.048
outcome: partial_success
failure_modes: [under_editing, missed_requirement, wrong_pattern]
case_quality: poor
case_quality_reason: placeholder_id_and_strategy_artifact_deflates_f1
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Byte-identical to attempt #85 (same diff blob `d21c91a`, same
gpt-5.5/opencode/v3 config) — a reproducibility duplicate. The agent
demoted `synonym: "lymphocytic hypophysitis"` on MONDO:0019835 from EXACT to
NARROW (adding NBK562255 and NCIT:C132055 provenance) and added the
`IAO:0000233` issue-tracker annotation, keeping "autoimmune hypophysitis"
EXACT. F1=0.091 (P=0.049, R=0.667). The agent's PR comment describes a more
ambitious "add lymphocytic hypophysitis as a child of primary hypophysitis"
plan, but the actual diff does not create any child term — a notable
narrative/diff mismatch. Sound minimal scope correction, but most of the
issue is unaddressed.

## Strengths

- Correctly demotes the over-broad "lymphocytic hypophysitis" synonym to
  NARROW with the issue-cited NBK562255 reference as provenance — responsive
  to the issue's central point.
- Adds the `IAO:0000233` issue-tracker annotation per Mondo convention.
- Tightly scoped; no erroneous or extraneous edits.

## Issues

- Narrative/diff mismatch: the PR comment claims it "added `lymphocytic
  hypophysitis` as a child of `primary hypophysitis` and removed it as an
  exact synonym", but the actual diff neither creates a child term nor
  removes the synonym (it only changes EXACT→NARROW). The reported summary
  over-states the work done.
- Wrong pattern / missed requirement: no relabel of MONDO:0019835, no new
  lymphocytic hypophysitis term, contrary to the maintainer's plan.
- Under-editing: no reparenting of MONDO:0016534/0019838/0019839, no new
  subtype terms (MONDO:1060217–1060219), no added definitions, no
  MONDO:0021156 cleanup.
- Leaves "autoimmune hypophysitis" EXACT on the grouping.
- Identical to #85 — no independent signal beyond determinism confirmation.
