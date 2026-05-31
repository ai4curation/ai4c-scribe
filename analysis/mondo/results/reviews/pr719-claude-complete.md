---
ontology: mondo
issue_number: 9896
pr_number: 10207
eval_repo_pr: 719
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.200
precision: 0.25
recall: 0.167
jaccard: 0.111
case_quality: poor
case_quality_reason: gold_has_out_of_scope_edits_and_brief_diff_inaccurate
companion_prs: []
scoring_caveat: "The issue's explicit rename ask was DECLINED by the curator on scope grounds (issue comments 2026-04-29 / 2026-05-01); merged gold #10207 adds the label as an EXACT synonym PLUS an unrequested def and an additional is_a: MONDO:0011612 parent. Metadiff vs #10207 both rewards reproducing unrequested edits and penalizes well-scoped synonym-only agents. Judge against the curator's documented decision (synonym-only, no rename, no parent removal), not the literal gold diff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-15
outcome: partial_success
failure_modes: [over_editing, scope_creep, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Byte-identical re-run of attempt #768 (gpt-5.4/codex, blob `4843176`,
F1=0.200). The agent correctly kept the OMIM-derived primary label and added
"GCSH-related glycine encephalopathy" as an EXACT synonym rather than renaming
MONDO:0957382 — one of only two runs in the 12-attempt set (with #255) to
independently reach the curator's documented synonym-only decision. The
metadiff F1=0.200 under-represents quality: this case is flagged
`case_quality: poor` because gold #10207 itself adds out-of-scope
`def:`/`is_a: MONDO:0011612` edits the issue never requested, penalizing the
correct synonym-only strategy. The agent nonetheless over-edited in gold's
direction with a fabricated def, second parent, and ClinGen subset/resource
lines the curator never asked for.

## Strengths

- **Did not rename** MONDO:0957382 — the central correct call, aligned with
  the curator's explicit decision and MONDO OMIM-first label policy.
- ClinGen EXACT synonym with the correct `{OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`
  qualifier and ClinGen affiliation source — same axiom shape as gold.
- `property_value: IAO:0000233 ".../issues/9896"` matches gold's tracker
  provenance.
- Preserved `is_a: MONDO:0017338` (fatal MMDS) parent — no parent removal.

## Issues

- **Scope creep mirroring gold's own over-reach, not the issue.** Unrequested
  `def:` (PMID:33890291/36190515), second `is_a: MONDO:0011612` parent,
  `subset: clingen`, and a ClinGen `curated_content_resource` relationship.
  The issue asked only for a label change; the curator's resolution was
  synonym-only.
- **Synonym provenance wrong.** Gold cites the requester ORCID
  `0000-0002-7437-8060` (issue nano-attribution) plus the ClinGen affiliation;
  the agent substituted two PMIDs and dropped the requester ORCID.
- **Def genus/sources diverge from gold** (gold: "Any multiple mitochondrial
  dysfunctions syndrome..." sourced to curator ORCID 0000-0002-7638-4659 +
  OMIM:620423); both defs are unrequested and the agent's asserts a glycine-
  encephalopathy identity beyond the curator's committed position.
- This is the identical diff to #768 — no independent signal added by the
  duplicate run.
- Net: partial_success — correct synonym-only strategy but over-edited with
  def/subset/resource/reparenting changes the curator declined and lost the
  requester ORCID. F1=0.200 under-represents the correct judgment; failure
  modes are over-editing/scope, not the rename error of most other attempts.
