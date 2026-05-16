---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 33
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v8
case_type: obsoletion
difficulty: simple
f1: 0.800
precision: 0.889
recall: 0.727
jaccard: 0.667
outcome: partial_success
failure_modes:
  - over_editing
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

claude-haiku-4.5 / claude (v8) produced a correct obsoletion of GO:0008785, but instead of *removing* the spurious GO:0070937 comment (as every other 0.800 attempt and the gold's intent imply) it *rewired* the GO:0070937 comment to point at GO:0102039 — propagating a biologically nonsensical cross-reference into an active term. F1=0.800 here *over*-represents quality relative to the rest of the 0.800 cluster because of that error. Blob `f5c2608`.

## Strengths

- Correct core obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items preserved.
- Obsoletion comment is accurate and informative ("more specific than the specificity of any known gene product ... replaced by NADH-dependent peroxiredoxin activity (GO:0102039), which includes both this substrate and related hydroperoxides").
- GO:0009321 comment correctly rewired to GO:0102039 (a genuinely related complex).
- Replacement target GO:0102039 correctly identified.

## Issues

- Wrong pattern / data error: GO:0070937 (CRD-mediated mRNA stability complex) had a spurious comment referencing GO:0008785 that is a copy/paste artifact — the term has no relation to peroxide reduction. The agent *kept* the comment and merely swapped the ID to GO:0102039, so an active mRNA-stability term now carries a "See also NADH-dependent peroxiredoxin activity" comment. This is worse than the original artifact: it launders a nonsense reference into a valid-looking one pointing at a live term. All other 0.800-cluster attempts correctly *deleted* this comment. The agent's own PR text even describes both as "Updated ... from GO:0008785 to GO:0102039", confirming it did not recognize the GO:0070937 case as erroneous.
- Scope/over-editing (metadiff-only): GO:0009321 hunk not in human PR. The GO:0009321 rewire is defensible; the GO:0070937 rewire is not.
- The metadiff cannot see this distinction (it scores line overlap), so the identical 0.800 hides a real quality regression vs. peers.
