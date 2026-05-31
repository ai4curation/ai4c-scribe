---
ontology: uberon
issue_number: 3637
pr_number: 3638
eval_repo_pr: 72
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: new_term
difficulty: medium
f1: 0.588
precision: 0.556
recall: 0.625
jaccard: 0.417
outcome: partial_success
failure_modes:
  - wrong_term
  - instruction_violation
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent added a `'uterine fundus'` term with a correct definition and the
gold's confirmed PMIDs, sound provenance, and an `intersection_of` logical
definition, but assigned the **wrong ID** `UBERON:1200003` instead of the
canonical `UBERON:99xxxxx` NTR range mandated by the agent config (gold uses
`UBERON:9900001`). It also omitted the requested second synonym and an asserted
`is_a`/`part_of`. F1 0.588 (P 0.556 / R 0.625) is roughly fair — the wrong ID
alone guarantees a metadiff penalty on the most identifying line, and there are
real omissions, though the underlying anatomy is modeled correctly.

## Strengths

- Correct definition text and the gold's confirmed reference PMIDs
  `[PMID:40653088, PMID:41204538]`; the agent verified the PMIDs via
  NCBI/PubMed lookups (good methodology, documented in the PR comment).
- Synonym `fundus uteri` EXACT with correct `[PMID:39112955]` xref.
- `intersection_of: UBERON:0000064` / `intersection_of: part_of
  UBERON:0000995` is a coherent genus-differentia logical definition aligned
  with the `anatomyPartOfAnatomy` DOSDP pattern the agent consulted.
- Provenance correct: `dc-contributor` with curator name `! Aleix Puig-Barbé`,
  `dcterms-date`, `term_tracker_item` (typed `property_value ... xsd:anyURI`),
  `created_by`.
- Good documented process: checked for pre-existing terms with `obo-grep.pl`,
  reviewed the DOSDP pattern, ran `robot convert` round-trips and
  `git diff --check`.

## Issues

- **Wrong term ID / instruction violation:** used `UBERON:1200003`. The agent
  config explicitly states "New terms start UBERON:99xxxxx"; gold (and the
  three claude/sonnet/haiku attempts) used `UBERON:9900001`. This is the single
  most impactful divergence and is an instruction violation, not a metadiff
  serialization artifact — the canonical ID was knowable from the config.
- **Under-editing:** no asserted `is_a: UBERON:0000064 ! organ part` and no
  asserted `relationship: part_of UBERON:0000995 ! uterus`. While the reasoner
  can infer `is_a` from the logical definition, gold carries both asserted
  edges; their absence diverges from the approved form and the issue's explicit
  "'part of' some uterus" parentage request is only encoded logically.
- Missing second synonym `fundus of uterus` (EXACT) that the gold includes.
- Term placed at a different file location (near UBERON:3629/scapular blade)
  than gold (near tracheobronchial tree); cosmetic for metadiff but reflects a
  different insertion strategy. Eval PR #72 is CLOSED ([DO NOT MERGE] eval
  shadow), as expected for this workflow.
