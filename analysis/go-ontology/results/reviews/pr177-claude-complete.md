---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 177
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.571
precision: 0.400
recall: 1.000
jaccard: 0.400
outcome: partial_success
failure_modes:
  - missed_requirement
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [31677]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added `only_in_taxon: NCBITaxon:2759` (Eukaryota) rows for `GO:0000956` (nuclear-transcribed mRNA catabolic process) and `GO:0141065` (maternal mRNA clearance) to `src/taxon_constraints/only_in_taxon.tsv`, inserting them in sorted positions, matching the broad parent-level strategy the curator chose in the gold PR. The metadiff F1 of 0.571 (recall 1.000) accurately reflects that it reproduced every substantive line the gold added while missing the migrasome formatting cleanup and the companion `never_in_taxon` change.

## Strengths

- Correct parent-level modeling: constraining `GO:0000956` to Eukaryota covers `GO:0070478` (the reported term) and the whole nuclear-transcribed mRNA decay branch via inheritance — exactly @pgaudet's chosen resolution, not the literal `never_in_taxon: Bacteria` the reporter requested.
- Added `GO:0141065` maternal mRNA clearance, matching a gold-PR row and @pgaudet's in-thread list.
- Inserted rows in their correct sorted positions in the TSV rather than appending blindly, keeping the file ordering consistent with surrounding entries.
- Reported running `make travis_build` both before and after the edit, used `obo-grep.pl` for term verification, and committed only the single source file (no derived-artifact churn) — the cleanest possible PR shape for this task.
- Correctly avoided duplicating `GO:0000958` after observing it was already present in the eval base (a true observation here, unlike some sibling attempts).

## Issues

- Omission: did not reproduce the gold PR's `GO:0140494` migrasome row cleanup (malformed extra `NCBITaxon:7742` column). This was incidental cleanup not derivable from the issue, so excusable but still an incomplete reproduction.
- Omission: did not add the third gold-PR constraint `GO:0000958` mitochondrial mRNA catabolic process. Because it was already present in the eval base the final state is not biologically wrong, but the agent PR is not fully comparable to the human source edit.
- Did not address the companion resolution step (PR #31677 added `GO:1990074` polyuridylation-dependent mRNA catabolic process to `never_in_taxon.tsv`), which the issue's "any other terms related to ... RNA decay" wording arguably invited.
- The pre-existing codex review graded this `success`; I grade it `partial_success` because two of the three substantive gold constraints and the migrasome fix are not reproduced. The core modeling is nonetheless correct and well-justified.
