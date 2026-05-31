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
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31670
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31676
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/199
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31670 --repo geneontology/go-ontology
    gh pr diff 31676 --repo geneontology/go-ontology
    gh pr diff 199 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made a plausible literal fix for issue #31670 by adding `never_in_taxon NCBITaxon:2` constraints to `GO:0070478` and several other nonsense-mediated decay terms. However, the human PR solved the problem differently and more broadly, using `only_in_taxon NCBITaxon:2759` on parent-level eukaryotic mRNA catabolism terms (`GO:0000956`, `GO:0000958`, `GO:0141065`) plus an incidental TSV cleanup. The F1 score of 0.0 accurately reflects that the agent's diff does not overlap the accepted patch, but it somewhat under-represents that the agent did address the explicitly reported bacterial/NMD annotation problem.


## Strengths

- Directly addressed the term named in the issue: `GO:0070478` nuclear-transcribed mRNA catabolic process, 3'-5' exonucleolytic nonsense-mediated decay, by adding a Bacteria exclusion.
- Covered closely related NMD terms, including parent `GO:0000184`, sibling `GO:0070479`, and regulatory terms `GO:2000622`, `GO:2000623`, and `GO:2000624`.
- The biological rationale is basically sound for the edited terms: canonical nuclear-transcribed mRNA nonsense-mediated decay is a eukaryotic process and should not be annotated to bacteria.
- The edit was syntactically scoped to the taxon constraints table and used valid-looking TSV rows with `NCBITaxon:2` / Bacteria.


## Issues

- Used the wrong accepted pattern for this curation case. The merged PR added `only_in_taxon NCBITaxon:2759` Eukaryota constraints to broader terms, especially `GO:0000956` nuclear-transcribed mRNA catabolic process, so the constraint would be inherited by descendants such as `GO:0070478`.
- Under-edited relative to the human solution by not adding Eukaryota-only constraints for `GO:0000956`, `GO:0000958` mitochondrial mRNA catabolic process, or `GO:0141065` maternal mRNA clearance.
- The agent's `never_in_taxon NCBITaxon:2` rows only block bacteria. They do not rule out annotations to other non-eukaryotes, whereas the accepted `only_in_taxon NCBITaxon:2759` rows express the stronger intended biological scope.
- The direct rows for `GO:0000184`, `GO:0070478`, and `GO:0070479` are narrower and more repetitive than necessary once the parent `GO:0000956` is constrained.
- The PR missed the incidental formatting cleanup for `GO:0140494` migrasome, where the human PR removed an erroneous extra `NCBITaxon:7742` column and normalized the evidence column.
