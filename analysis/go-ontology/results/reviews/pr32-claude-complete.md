---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 32
agent: std_codex_g54
model: gpt-5.4
runtime: codex
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

gpt-5.4 / codex (v8, iteration 4) produced a correct core obsoletion of GO:0008785 but, like attempt #33, *rewired* the spurious GO:0070937 comment to GO:0102039 instead of deleting it, propagating a nonsensical cross-reference into an active mRNA-stability term. F1=0.800 *over*-represents quality relative to peers that deleted the bad comment. Blob `ed8baba`.

## Strengths

- Correct core obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items preserved.
- Obsoletion comment accurate: "more specific than the specificity of any known gene product and should be replaced by the broader substrate-appropriate term NADH-dependent peroxiredoxin activity."
- GO:0009321 comment correctly rewired to GO:0102039 (genuinely related complex).
- Substantive RESEARCH.md (PMID:12517450, PMID:11717276, PMID:21674802) and DESIGN_PATTERNS.md; pre/post `make travis_build` passing; honest disclosure of the OAK import failure with documented fallback.

## Issues

- Wrong pattern / data error: GO:0070937 (CRD-mediated mRNA stability complex) — the agent rewired the spurious GO:0008785 comment to GO:0102039 rather than deleting it. The PR text says it updated comments so they "no longer reference the obsolete MF term," but the correct action (taken by the 0.800 majority) was to *remove* the GO:0070937 comment because it is an unrelated copy/paste artifact. The result is an active term carrying a biologically meaningless "See also peroxiredoxin activity" pointer. Despite the strong research methodology, the agent did not flag the GO:0070937 reference as erroneous (cf. its v9 runs #46/#40 which *did* remove it).
- Scope/over-editing (metadiff-only): GO:0009321 hunk not in human PR (defensible); GO:0070937 rewire not defensible.
- Metadiff scores this identically to the correct cluster — the 0.800 masks the regression.
