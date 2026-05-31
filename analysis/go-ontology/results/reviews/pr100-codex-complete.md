---
ontology: go-ontology
issue_number: 31969
pr_number: 31988
eval_repo_pr: 100
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/100
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31969 --repo geneontology/go-ontology
    gh pr diff 31988 --repo geneontology/go-ontology
    gh pr diff 100 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent addressed the central request in geneontology/go-ontology#31969: it reparented the 25 oxidoreductase activity terms to parents matching their EC classes, added issue tracker metadata, and made the requested RHEA/name/definition updates. The metadiff score is high (F1 0.938, precision 0.914, recall 0.964) and broadly reflects the quality of the solution, but it slightly overstates completeness because the agent missed several old-label synonym additions that the human PR made after renaming terms.


## Strengths

- Correctly implemented the main parentage corrections, including representative EC-class fixes such as GO:0102394 from GO:0016616 to GO:0016706, GO:0050607 from GO:0016620 to GO:0016616, GO:0008762 from GO:0016616 to GO:0016628, GO:0047111 from GO:0016622 to GO:0016725, and GO:0032441 from GO:0016730 to GO:0016713.
- Covered the broad multi-term cleanup rather than only the first few examples: the agent also handled the grouped reparentings for GO:0033759, GO:0045431, GO:0047594, and GO:0050589 to GO:0050498, plus the reverse GO:0102717 move to GO:0016706.
- Applied the requested RHEA-aligned definition updates for terms such as GO:0008762 using RHEA:12248, GO:0018525 using RHEA:29603, GO:0044684 using RHEA:42804, GO:0050607 using RHEA:28502, GO:0102717 using RHEA:32115, and GO:0032441 adding RHEA:48140.
- Renamed the three terms called out by the issue: GO:0102394 to "L-isoleucine 4-hydroxylase activity", GO:0050607 to "S-(hydroxymethyl)mycothiol dehydrogenase activity", and GO:0047081 to "3-hydroxy-2-methylpyridine-5-carboxylate monooxygenase [NAD(P)H] activity".
- Added `term_tracker_item` metadata for https://github.com/geneontology/go-ontology/issues/31969 on all edited terms, matching the human PR's provenance pattern.


## Issues

- The agent did not preserve old names as synonyms after renaming terms. The human PR added the old GO:0047081 label as a RELATED synonym, the old GO:0050607 label as an EXACT synonym, and the old GO:0102394 label as a RELATED synonym; the agent only changed the labels. This is an under-editing issue because renamed GO terms should retain searchable legacy labels when appropriate.
- GO:0106145 retains `GOC:lr` as a definition xref in the agent diff, while the human PR removes it and keeps PMID:29361149, PMID:29581584, and RHEA:57848. Since the definition was rewritten to the RHEA-style reaction text, retaining the curator xref is a small provenance mismatch.
- The agent used a Unicode em dash in the GO:0050616 definition text (`[NADPH em dash hemoprotein reductase]`) where the human PR normalized this to ASCII double hyphen (`[NADPH--hemoprotein reductase]`). This likely follows the issue text literally, but it is less consistent with the surrounding OBO file style.
