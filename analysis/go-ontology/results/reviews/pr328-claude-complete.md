---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 328
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: new_term
difficulty: hard
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
  - missed_requirement
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [31677]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent made the single most correct and best-reasoned core edit of all ten attempts — `only_in_taxon: NCBITaxon:2759` (Eukaryota) for `GO:0000956` and `GO:0141065`, *with* a `source` annotation pointing at the tracker issue — exactly the curator's chosen parent-level strategy, with explicit acknowledgement that it adopted @pgaudet's in-thread resolution over the reporter's literal `never_in_taxon: Bacteria` ask. However, it also committed the regenerated `only_in_taxon.ofn` and `go_taxon_constraints.owl`, producing thousands of lines of blank-node (`genid`) renumbering. The metadiff F1 of 0.000 is a pure scoring artifact of that derived-file churn and dramatically under-represents what is arguably the strongest submission on substance.

## Strengths

- Correct, well-justified modeling: parent-level `only_in_taxon: NCBITaxon:2759` on `GO:0000956` propagates to `GO:0070478`, `GO:0000184`, no-go/non-stop/deadenylation-dependent decay, etc. — precisely the curator's resolution. The PR comment explicitly explains why this is stronger (also excludes Archaea/viruses) and more parsimonious than per-leaf `never_in_taxon: Bacteria`.
- Added `GO:0141065` maternal mRNA clearance matching the gold-PR row and @pgaudet's list.
- Best provenance practice of any attempt: populated the `source` column with `https://github.com/geneontology/go-ontology/issues/31670`, producing a properly annotated OWL axiom (the human gold PR left source blank).
- Excellent, accurate self-assessment: the PR comment proactively flags that "the large diff on `go_taxon_constraints.owl` is mostly renumbering of anonymous genid blank-node IDs ... the actual semantic content added is the two new axioms" — correctly diagnosing the exact problem that tanks its own metadiff.
- Strong methodology: `obo-grep.pl` term verification across the NMD subhierarchy, column check, OFN/OWL regeneration via make targets, follow-up note about cleaning up the three offending PANTHER annotations.

## Issues

- Scope creep / over-editing: committing the regenerated `only_in_taxon.ofn` and `go_taxon_constraints.owl` was the wrong call. The human PR (and CI) treat the OWL as a build product; the hundreds of `genidNNN` renumberings make the PR unreviewable and produce F1 0. The agent recognized the noise but committed it anyway rather than reverting the generated files — the correct action would have been to commit only the source TSV (as pr263/pr177 did).
- Omission: did not reproduce the gold PR's `GO:0140494` migrasome malformed-row cleanup (incidental, not derivable from the issue).
- Omission: did not add `GO:0000958` mitochondrial mRNA catabolic process. Unlike the gpt-5.5 attempts it did not even claim it was pre-present; it simply constrained the two terms it judged necessary. Final state leaves GO:0000958 uncovered.
- Did not address the companion `never_in_taxon` step (PR #31677 added `GO:1990074` polyuridylation-dependent mRNA catabolic process as Bacteria-only).
- Net: substantively the best attempt (correct modeling + provenance + honest self-critique) undone by one operational mistake (committing derived artifacts). Graded `partial_success`, not `failure`, because the source-level edit is correct and complete for its chosen scope; the F1 of 0 is entirely a derived-file artifact.
