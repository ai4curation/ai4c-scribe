---
ontology: mondo
issue_number: 9896
pr_number: 10207
eval_repo_pr: 768
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

gpt-5.4/codex correctly resisted the rename: it kept the OMIM-derived primary
label "multiple mitochondrial dysfunctions syndrome 7" and added "GCSH-related
glycine encephalopathy" as an EXACT synonym, explicitly reasoning from MONDO's
OMIM-first naming policy. This is one of only two runs in the 12-attempt set
(with kimi-k2.6/opencode #255) to independently reach the curator's documented
synonym-only decision rather than performing the rename @MeeSiing declined on
scope grounds. The metadiff F1=0.200 substantially under-represents quality
here: this case is flagged `case_quality: poor` because gold #10207 itself
carries out-of-scope `def:`/`is_a: MONDO:0011612` edits the issue never asked
for, so the score punishes the correct synonym-only strategy. The remaining
problem is that the agent then over-edited in the same direction as gold,
adding a fabricated def, a second parent, and ClinGen subset/resource lines
the curator never requested.

## Strengths

- **Did not rename** MONDO:0957382 — the central correct judgment call, aligned
  with the curator's explicit decision (issue comments 2026-04-29/2026-05-01)
  and MONDO OMIM-first label policy, which the agent cites in its PR rationale.
- ClinGen EXACT synonym present with the correct `{OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`
  qualifier and the ClinGen affiliation `https://clinicalgenome.org/affiliation/40011/`
  source — structurally matching gold's synonym axiom shape.
- Added `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9896"`
  matching gold's issue-tracker provenance.
- Preserved the existing `is_a: MONDO:0017338` (fatal multiple mitochondrial
  dysfunctions syndrome) parent — no parent removal, respecting the config rule.
- Sound methodology: reviewed prior curator comment, inspected MONDO:0957382 /
  MONDO:0011612 / MONDO:0017338 stanzas, ran `robot convert` to validate, and
  honestly reported the `make NORM` gap (no docker).

## Issues

- **Scope creep matching gold's own over-reach, not the issue.** The agent
  added an unrequested `def:` (citing PMID:33890291, PMID:36190515), a second
  `is_a: MONDO:0011612 ! glycine encephalopathy` parent, `subset: clingen`,
  and a `relationship: curated_content_resource` ClinGen line. The issue asked
  only for a label change; the curator's resolution was synonym-only. The extra
  parent in particular re-introduces the very scope question the curator was
  deliberating, just via reparenting instead of renaming.
- **Synonym provenance wrong.** Gold cites the requester ORCID
  `https://orcid.org/0000-0002-7437-8060` (from the issue's nano-attribution
  field) alongside the ClinGen affiliation; the agent substituted PMID:33890291
  and PMID:36190515 for that ORCID. The requester attribution is lost.
- **Def text/sources diverge from gold.** Gold's def uses a "Any multiple
  mitochondrial dysfunctions syndrome..." genus sourced to the curator ORCID
  0000-0002-7638-4659 + OMIM:620423; the agent wrote a different "fatal
  multiple mitochondrial dysfunctions syndrome that is also a glycine
  encephalopathy" framing sourced to two PMIDs. Both are unrequested, but the
  agent's also asserts a "glycine encephalopathy" identity in prose that goes
  beyond what the curator was willing to commit to.
- Note #719 is a byte-identical re-run of this same diff (blob `4843176`).
- Net: partial_success — correct headline strategy (no rename, ClinGen EXACT
  synonym, IAO tracker, both parents retained-plus-added) but over-edited with
  def/subset/resource/reparenting changes the curator explicitly declined and
  dropped the requester ORCID. F1=0.200 under-represents the correct
  synonym-only judgment; the failure modes are over-editing/scope, not the
  rename error that sinks most other attempts.
