---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 263
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
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

The agent added clean, correct `only_in_taxon: NCBITaxon:2759` (Eukaryota) rows for `GO:0000956` (nuclear-transcribed mRNA catabolic process) and `GO:0141065` (maternal mRNA clearance) to `src/taxon_constraints/only_in_taxon.tsv`, exactly the broad parent-level strategy curator @pgaudet chose in the gold PR rather than the literal `never_in_taxon: Bacteria` the reporter requested. The metadiff F1 of 0.571 (recall 1.000) is roughly accurate: it reproduces every substantive line the gold PR added, but it omits the migrasome formatting cleanup and never touches the companion `never_in_taxon` change, so it is not a complete reproduction of the human resolution.

## Strengths

- Correctly identified that constraining the parent `GO:0000956` to Eukaryota propagates down to `GO:0070478`, `GO:0000184`, and the rest of the nuclear-transcribed mRNA decay subhierarchy, avoiding per-leaf enumeration. This is precisely the modeling @pgaudet adopted.
- Added `GO:0141065` maternal mRNA clearance, matching one of the three substantive rows in the gold PR and aligning with @pgaudet's in-thread list.
- Minimal, surgical diff (two appended TSV lines, no derived-artifact churn). This is the cleanest of all ten attempts and the easiest to review.
- Edited the correct file (`only_in_taxon.tsv`, not `go-edit.obo`) and ran `make check_all_taxon_constraints_columns`, consistent with the `/taxon-constraint` skill.

## Issues

- Omission: did not reproduce the gold PR's `GO:0140494` migrasome cleanup, which fixed a malformed row (`NCBITaxon:7742` extra column with embedded `Eukaryota  PMID:...` source) into a clean `NCBITaxon:2759` Eukaryota row. This was incidental cleanup the agent had no way to discover from the issue, so it is excusable but still incomplete.
- Omission/inaccuracy: the PR comment claims "`GO:0000958` ... already had an `only_in_taxon Eukaryota` constraint in the file at the time of editing", but `GO:0000958` is one of the three rows the gold PR explicitly *added* — it was not in the base. The agent therefore silently dropped one of the three gold constraints based on an incorrect premise. Final-state impact is limited (GO:0000958 mitochondrial mRNA catabolic process is still uncovered), but the reasoning was wrong.
- Did not address pgaudet's second resolution step (companion PR #31677 added `GO:1990074` polyuridylation-dependent mRNA catabolic process to `never_in_taxon.tsv` as Bacteria-only). The issue text ("Any other terms related to non-mediated RNA decay should also have this constraint") arguably invited this.
- Could not run full `make travis_build` (no `amm`/`robot` in env); validation was limited to the column check.
