---
ontology: go-ontology
issue_number: 31882
pr_number: 32036
eval_repo_pr: 131
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent produced a diff line-for-line identical to the merged human PR #32036, obsoleting both `GO:1905353` and `GO:0097711` with `replaced_by: GO:1905349`. The metadiff F1 of 1.0 accurately reflects the substantive quality, and the agent additionally documented strong supporting methodology (reference validation of `PMID:27646273`, design-pattern check of the replacement term against `cc_assembly.yaml`).

## Strengths

- Obsoleted both terms from the issue's final decision, correctly extending beyond the single term in the issue title.
- Applied the full standard GO obsoletion structure to both terms: `obsolete` prefix, `OBSOLETE.` definition prefix with preserved text/dbxrefs, `is_obsolete: true`, `term_tracker_item` for issue 31882, and `replaced_by: GO:1905349`.
- Removed all active logical structure: `GO:0097711`'s `is_a: GO:0140056` / `part_of GO:0060271`, and `GO:1905353`'s `intersection_of` axioms (`GO:0022607`, `GO:0097539`) plus the full synonym list.
- Matched the human's provenance cleanup exactly (removed `created_by`/`creation_date` from both stanzas) — the detail that lifts this to F1=1.0.
- Deleted the dangling `starts_with GO:0097711` from `GO:0060271`, matching the human and reasoning explicitly that `has_part GO:1905349` already preserves the relevant connection.
- Obsoletion comments match the human's substance, citing `PMID:27646273` for `GO:0097711` and the no-annotations rationale for `GO:1905353`.
- Strong methodology: validated `PMID:27646273` with `linkml-reference-validator`, confirmed the replacement term `GO:1905349` conforms to the cellular component assembly design pattern, ran `make travis_build` (passed), and honestly reported that the local `runoak` AmiGO annotation check could not run due to an OAK/LinkML startup error (falling back to the curator-documented annotation status in the issue thread).

## Issues

- No substantive ontology issues. The diff is identical to the accepted human solution.
- Reporting-only nit (does not affect the ontology edit): the agent's PR/issue narrative frames the run as a verification of pre-existing branch state ("the local branch already contained the obsoletion changes"). This is an artifact of the eval harness base state rather than an error; the produced diff is correct and complete.
