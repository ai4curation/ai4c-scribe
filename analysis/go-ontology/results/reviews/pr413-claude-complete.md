---
ontology: go-ontology
issue_number: 31670
pr_number: 31676
eval_repo_pr: 413
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
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

The agent added seven `never_in_taxon: NCBITaxon:2` (Bacteria) rows to `src/taxon_constraints/never_in_taxon.tsv` for the NMD branch (`GO:0000184`, `GO:0070478`, `GO:0070479`, `GO:0170010`, `GO:2000622/623/624`). This is a clean, minimal, biologically sound diff that literally satisfies the reporter's explicit request ("never in taxon: 2"), but the curator (@pgaudet) instead chose a broader `only_in_taxon: Eukaryota` modeling in a different file, so the metadiff F1 is 0.000. The score badly under-represents the quality: this is a defensible alternative resolution, not a failure of understanding.

## Strengths

- Biologically correct: NMD is eukaryote-specific (requires nuclei, splicing, the exon-junction complex, UPF/SMG machinery); excluding Bacteria is right.
- This is literally what the issue reporter asked for ("Can you add the following please? ... never in taxon: 2 ... Any other terms related to non-mediated RNA decay should also have this constraint"). The agent followed the explicit instruction faithfully.
- Clean, minimal, well-targeted diff (7 appended rows, correct 4/5-column TSV format, correct file `never_in_taxon.tsv`).
- Sensible branch coverage: parent `GO:0000184`, both directional variants, the three regulatory terms, and the `GO:0170010` NMD complex — internally coherent.
- Reported full `make travis_build` passing with 0 SPARQL violations and clean ELK reasoning.

## Issues

- Modeling divergence (the reason for F1 0): the curator's accepted resolution used `only_in_taxon: NCBITaxon:2759` (Eukaryota) on the broader parent `GO:0000956` in `only_in_taxon.tsv`, which is stronger (also excludes Archaea/viruses) and more parsimonious (covers no-go/non-stop/deadenylation-dependent decay too). The `/taxon-constraint` skill explicitly advises preferring the more general clade — the agent did not take that step despite the skill being available.
- Did not add `GO:0141065` maternal mRNA clearance or `GO:0000958` mitochondrial mRNA catabolic process (the other gold constraints / @pgaudet's in-thread list).
- Did not address the companion `never_in_taxon` step the human took (PR #31677 added `GO:1990074` polyuridylation-dependent mRNA catabolic process). Ironically, since this attempt used the same file, that row would have been a natural addition.
- Net: a correct-but-non-canonical resolution. Graded `partial_success` because it faithfully and correctly implements the literal request; the F1 of 0 is an artifact of the curator choosing a different (broader) modeling, not an agent error.
