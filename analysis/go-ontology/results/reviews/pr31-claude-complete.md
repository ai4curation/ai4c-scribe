---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 31
agent: std_claude_son45
model: claude-sonnet-4.5
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
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

claude-sonnet-4.5 / claude on the v8 config (iteration 4) produced a correct standard obsoletion of GO:0008785 plus the two defensible cross-reference cleanups. F1=0.800 modestly understates quality. Blob `e347ebb`. (A separate `-claudecode-` review and a `-codex-` review already exist for this eval PR under other reviewers; this is the distinct `-claude-` review.)

## Strengths

- Correct, complete obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items (#28261, #28340) explicitly retained for provenance.
- Obsoletion comment accurate: "more specific than the specificity of any known gene product. It has been replaced by the broader term NADH-dependent peroxiredoxin activity."
- GO:0009321 comment rewired to GO:0102039; GO:0070937 erroneous comment removed with a sound copy/paste-artifact justification.
- Detailed obsoletion-skill checklist (name/def prefix, axiom removal, reference sweep, no synonyms on obsolete term) — methodical even at v8.
- Honest disclosure that full `make travis_build` could not complete (missing Ammonite tool) and that the diff was manually reviewed instead — good failure transparency rather than a false validation claim.

## Issues

- Scope/over-editing (metadiff-only): GO:0009321/GO:0070937 hunks not in human PR → recall 0.727. Defensible curation.
- Validation could not be run end-to-end in this environment (Ammonite missing); the agent compensated with manual review but the obsoletion QC checks were not actually executed here. Lowers methodology confidence vs. the codex runs that ran full travis_build.
- Comment omits the explicit EC 1.11.1.26 citation present in the human comment. Stylistic.
