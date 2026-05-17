---
ontology: go-ontology
issue_number: 31969
pr_number: 31988
eval_repo_pr: 82
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.938
precision: 0.914
recall: 0.964
jaccard: 0.883
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31969
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31988
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/82
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31969 --repo geneontology/go-ontology
    gh pr diff 31988 --repo geneontology/go-ontology
    gh pr diff 82 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent addressed the central request in geneontology/go-ontology#31969: it reparented the oxidoreductase activity terms to EC-consistent parents, made the main RHEA/name/definition edits, and added issue tracker provenance. The high metadiff score (F1 0.938, precision 0.914, recall 0.964) is broadly fair for the ontology substance, but it slightly overstates completeness because the agent missed several cleanup details that the human PR included after renaming terms.


## Strengths

- Correctly made the major EC-class parentage fixes, including `GO:0102394` from `GO:0016616` to `GO:0016706`, `GO:0050607` from `GO:0016620` to `GO:0016616`, `GO:0008762` from `GO:0016616` to `GO:0016628`, `GO:0008863` and `GO:0047899` to `GO:0016726`, and `GO:0047111` to `GO:0016725`.
- Covered the grouped oxygenase/dioxygenase repairs rather than only the first examples: `GO:0033759`, `GO:0045431`, `GO:0047594`, and `GO:0050589` were moved to `GO:0050498`, while `GO:0102717` was moved back to `GO:0016706`.
- Correctly handled the EC 1.14 oxygenase branch reclassifications, including `GO:0010277` to `GO:0016709`, `GO:0050588` to `GO:0016702`, `GO:0018570` to `GO:0016708`, `GO:0050616` and `GO:0102915` to `GO:0016717`, and `GO:0004498`, `GO:0036199`, and `GO:0032441` to `GO:0016713`.
- Applied the requested definition updates for key terms, including `GO:0008762` with `RHEA:12248`, `GO:0018525` with `RHEA:29603`, `GO:0044684` with `RHEA:42804`, `GO:0050607` with `RHEA:28502`, `GO:0102717` with `RHEA:32115`, and `GO:0032441` adding `RHEA:48140`.
- Renamed the three terms called out by the issue: `GO:0102394` to "L-isoleucine 4-hydroxylase activity", `GO:0050607` to "S-(hydroxymethyl)mycothiol dehydrogenase activity", and `GO:0047081` to "3-hydroxy-2-methylpyridine-5-carboxylate monooxygenase [NAD(P)H] activity".
- Added `term_tracker_item` metadata for issue `#31969` on the edited term stanzas, matching the human PR's provenance pattern.


## Issues

- The agent did not preserve old primary labels as synonyms after renaming terms. The human PR added the old `GO:0047081` label as a RELATED synonym, the old `GO:0050607` label ("mycothiol-dependent formaldehyde dehydrogenase activity") as an EXACT synonym, and the old `GO:0102394` label as a RELATED synonym. This is an under-editing issue because the renamed terms lose useful legacy search strings.
- `GO:0106145` retains `GOC:lr` as a definition xref in the agent diff. The human PR removed it and kept `PMID:29361149`, `PMID:29581584`, and `RHEA:57848`, which is cleaner after rewriting the definition to the RHEA-style reaction text.
- The `GO:0050616` definition uses a Unicode em dash in `[NADPH-hemoprotein reductase]` where the human PR normalized this to the OBO file's ASCII double-hyphen style (`[NADPH--hemoprotein reductase]`). This likely came from following the issue text literally, but it is less consistent with the surrounding ontology file.
