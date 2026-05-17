---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 182
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.5
precision: 1.0
recall: 0.333
jaccard: 0.333
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31601
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32007
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/182
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31601 --repo geneontology/go-ontology
    gh pr diff 32007 --repo geneontology/go-ontology
    gh pr diff 182 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly made the reference edit to `GO:0140597` protein carrier activity, replacing the older "Binding to and carrying..." definition with the parent-aligned "Directly binding..." wording used in human PR #32007. However, it also changed `GO:0140309` unfolded protein holdase activity and, more seriously, included an unrelated `GO:0102067` geranylgeranyl diphosphate reductase activity definition update from a different issue/PR. The metadiff F1 of 0.5 captures that the accepted line is present but understates the practical scope problem caused by the extra unrelated ontology edit.


## Strengths

- Correctly updated `GO:0140597` to exactly match the human solution: `Directly binding to a protein and delivering it either to an acceptor molecule or to a specific location.`
- Preserved the existing `GO:0140597` definition xref `PMID:7628437` and did not alter that term's synonyms, logical definition, intersections, parentage, or metadata.
- The `GO:0140597` wording is biologically and ontologically coherent with parent `GO:0140104` molecular carrier activity, specializing the parent definition's "specific ion or molecule" to protein.
- The `GO:0140309` edit retained `PMID:39488384` and fixed a real grammar defect in the existing definition, changing "it's being delivers" to "it is being delivered."


## Issues

- The agent over-edited relative to the merged human solution by changing `GO:0140309` unfolded protein holdase activity. The source issue originally mentioned both `GO:0140597` and `GO:0140309`, but human PR #32007 was scoped to `GO:0140597`; its PR text says `GO:0140309` had already been handled previously.
- The agent included a completely unrelated definition and xref-source update for `GO:0102067` geranylgeranyl diphosphate reductase activity, changing the reaction wording and replacing definition xrefs `[EC:1.3.1.83, GOC:pz]` with `[EC:1.3.1.83, PMID:9492312, RHEA:26229]`. That edit belongs to issue #31963 / human PR #32006, not issue #31601, and appears to have entered through an unrelated merge commit.
- The PR description claimed the committed changes were scoped to issue #31601 and only `src/ontology/go-edit.obo`, but it did not mention the extra `GO:0102067` change. That makes the output harder to trust even though the central `GO:0140597` edit is correct.
