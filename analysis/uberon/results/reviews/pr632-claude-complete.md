---
ontology: uberon
issue_number: 3602
pr_number: 3603
eval_repo_pr: 632
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: simple
case_quality: good
f1: 0.769
precision: 0.833
recall: 0.714
jaccard: 0.625
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.5/opencode added `UBERON:8600149` "occlusal surface of tooth" as a
subclass of `UBERON:8600148` "tooth surface structure" with the correct ID,
name, *both* definition cross-references (`dentaleducationhub.com` + HL7
`CodeSystem-FDI-surface.html`), EXACT synonym `"occlusal surface"` with the
dentaleducationhub reference, correct `is_a` parent, and wdduncan's requester
ORCID `0000-0001-9625-1899`. The diff is identical to the sibling gpt-5.5
run #571: the only substantive divergence from the gold is the extra word
"tooth" in the definition ("...molar or premolar **tooth**"). Metadiff
F1=0.769 (P=0.833, R=0.714) **under-represents** quality — the gap is the
def-wording variant plus the two CLAUDE.md-mandated metadata lines and a
trailing-newline reserialization artifact. `success`.

## Strengths

- **Correct term skeleton**: id `UBERON:8600149`, name, `is_a:
  UBERON:8600148 ! tooth surface structure` as requested by @wdduncan.
- **Both definition xrefs preserved**: `dentaleducationhub.com` and HL7
  `CodeSystem-FDI-surface.html`, matching the two cross-references in issue
  #3602 and the gold's two-xref def.
- **Correct synonym and ORCID**: EXACT synonym `"occlusal surface"` with the
  dentaleducationhub reference; `relationship: dc-contributor
  https://orcid.org/0000-0001-9625-1899` — the exact ORCID the gold uses.
- **Excellent verification trail**: the PR comment documents the most
  thorough process of all attempts here — parent check, ID-availability
  check, sibling-term review, source-URL reachability checks (and honestly
  reported the dentaleducationhub 401 during automated fetch), `obo-checkin.pl`,
  two `robot convert` runs for syntax validation, and `git diff --check`.
  Side-effect blank-line normalization disclosed.
- **Followed CLAUDE.md metadata guidance**: added `term_tracker_item`
  pointing at issue #3602.

## Issues

- **Definition wording variant (style, not error)**: appends "tooth" to the
  gold/issue-body definition ("...molar or premolar **tooth**"). Defensible
  and arguably clearer, but not the verbatim wording supplied in issue
  #3602; main metadiff-divergent line. Not scored as a failure mode.
- **robot-convert trailing-newline churn (artifact)**: one EOF blank-line
  removal from the mandated reserialization; benign and disclosed.
- **No genuine ontological issues.** Substantively correct and complete.
