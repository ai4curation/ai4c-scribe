---
repo: monarch-initiative/mondo
issue_number: 9987
pr_number: 10094
issue_title: "Copy-paste error in inborn_metabolic_disrupts.yaml: definition says 'acquired' instead of 'inherited'"
issue_created_at: "2026-02-26"
pr_author: sabrinatoro
pr_merged_at: "2026-03-31"
pr_num_commits: 1
files_changed:
  - path: src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml
    additions: 1
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Trivial copy-paste bug fix in a DOSDP pattern definition template with clear before/after.
---

## Context

Issue #9987 reported a copy-paste error in the DOSDP pattern file `src/patterns/dosdp-patterns/inborn_metabolic_disrupts.yaml`. Line 46 of the definition template read "An acquired metabolic disease that is has its basis in the disruption of %s" when it should say "inherited" instead of "acquired". This error propagated incorrect definitions to all terms instantiated from this pattern.

## Changes Made

The PR made a single-character semantic fix in the DOSDP pattern file, changing "acquired" to "inherited" in the definition template text. This 1 addition and 1 deletion corrects the definition for all terms generated from the `inborn_metabolic_disrupts` pattern, which by definition describes inherited (not acquired) metabolic diseases.

## Resolution

Simple difficulty as a clear-cut word substitution fix. However, this case is notable because errors in DOSDP pattern files have multiplicative impact across all terms instantiated from that pattern. An agent should recognize that pattern file edits have broader implications than single-term edits and could potentially flag such inconsistencies proactively during quality control.
