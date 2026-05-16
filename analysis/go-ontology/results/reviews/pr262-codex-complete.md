---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 262
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
- under_editing
- missed_requirement
- wrong_pattern
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32018
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32021
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/262
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32018 --repo geneontology/go-ontology
    gh pr diff 32021 --repo geneontology/go-ontology
    gh pr diff 262 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent handled the basic obsoletion of GO:0052704 and GO:0140479, but it missed several parts of the full human resolution. The F1=0.0 is still too harsh because the selected PR #32021 is only a taxon-constraint cleanup, yet this attempt is weaker than the other full-obsoletion attempts: it did not add the MetaCyc narrowMatch xrefs to GO:0052699, did not remove the taxon-constraint TSV rows, and dropped creation metadata from the obsolete stanzas.

## Strengths

- Correctly identified GO:0052704 and GO:0140479 as the two pathway-variant terms to obsolete.
- Added obsolete-prefixed labels/definitions, `is_obsolete: true`, and `replaced_by: GO:0052699` for both terms.
- Rewired the active MF `part_of` links from the obsolete pathway variants to GO:0052699.
- Updated GO:0052707's replacement target from GO:0052704 to GO:0052699.

## Issues

- Missed requirement: it did not remove the GO:0052704 and GO:0140479 rows from `src/taxon_constraints/only_in_taxon.tsv`.
- Missed requirement: it did not add `MetaCyc:PWY-7255` and `MetaCyc:PWY-7550` as `skos:narrowMatch` xrefs on GO:0052699, even though that was explicit in the issue and later human PR #32023.
- Metadata regression: it removed existing creation metadata from GO:0052704 and GO:0140479 and dropped the older tracker/xref/synonym information from GO:0052704.
- The obsoletion comments are generic and lose the specific bacterial/fungal pathway mapping rationale.
