---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 199
agent: std_claude_hai45
model: claude-haiku-4.5
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
  - wrong_pattern
  - missed_requirement
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [31677]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent added six `never_in_taxon: NCBITaxon:2` (Bacteria) rows to `src/taxon_constraints/never_in_taxon.tsv` for the NMD branch (`GO:0000184`, `GO:0070478`, `GO:0070479`, `GO:2000622/623/624`). Like pr413, this is a clean, minimal, biologically correct diff that literally satisfies the reporter's request but diverges from the curator's chosen `only_in_taxon: Eukaryota` modeling, giving an F1 of 0.000 that under-represents the quality.

## Strengths

- Biologically correct rationale, articulated in detail: nuclear compartmentalization, EJC dependence, eukaryote-specific UPF/SMG machinery — all valid reasons NMD cannot occur in bacteria.
- Faithful to the explicit issue request ("never in taxon: 2" on GO:0070478 and similar NMD terms).
- Clean minimal diff (6 rows), correct file (`never_in_taxon.tsv`), correct TSV column format, no derived-artifact churn.
- Coherent branch coverage including parent `GO:0000184`, both directional variants, and the three regulatory terms; explicitly reasoned about the is_a/regulates relationships.
- Ran `make check_all_taxon_constraints_columns` and verified GO IDs exist in `go-edit.obo`.

## Issues

- Modeling divergence (cause of F1 0): the accepted human resolution used the broader, more parsimonious `only_in_taxon: NCBITaxon:2759` (Eukaryota) on the parent `GO:0000956` in `only_in_taxon.tsv`. The `/taxon-constraint` skill explicitly recommends preferring a more general clade where possible; the agent did not generalize to `only_in_taxon: Eukaryota` despite citing the skill in its checklist.
- Did not add `GO:0141065` maternal mRNA clearance or `GO:0000958` mitochondrial mRNA catabolic process (the curator's other constrained terms / in-thread list).
- Slightly narrower than pr413 (omits the `GO:0170010` NMD-complex CC term), though the NMD-complex constraint is arguably inferable from the cited issue.
- Did not address the companion `never_in_taxon` step the human took (PR #31677, `GO:1990074` polyuridylation-dependent mRNA catabolic process) — would have been a natural same-file addition.
- Consistent with the pre-existing codex self-review, which also graded this `partial_success`. The F1 of 0 reflects a non-canonical-but-valid modeling choice plus a partial gold PR, not an agent comprehension failure.
