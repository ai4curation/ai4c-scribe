---
ontology: uberon
issue_number: 3409
pr_number: 3466
eval_repo_pr: 194
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: structural_refactor
difficulty: hard
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: failure
failure_modes:
  - wrong_pattern
  - wrong_term
  - missed_requirement
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent edited the legacy `treat-xrefs-as-reverse-genus-differentia` directives in the header of `src/ontology/uberon-edit.obo`, changing `FBdv`, `WBls`, and `ZFS` from `part_of` to `in_taxon` (NCBITaxon:7227/6237/7954). This is the wrong mechanism (the active bridge pipeline is the SSSOM/T ruleset from `src/scripts/taxa.py` + `config/taxa.yaml`, which gold PR #3466 modified) and also an invalid construct — `treat-xrefs-as-reverse-genus-differentia` is an OBO macro expecting a `part_of`-style relation, and the source `bridges.rules` shows `in_taxon` is selected via the `%TAXREL` switch, not via this directive. The agent then ran `robot convert` to reserialize the whole file, which produced a large block of CL-label re-sync noise unrelated to the issue (e.g. `lung ciliated cell`→`lung multiciliated epithelial cell` for `CL:1000271`; `glandular epithelial cell`→`glandular secretory epithelial cell` for `CL:0000150`; `ciliated cell of the bronchus`→`multiciliated epithelial cell of the bronchus` for `CL:0002332`; `lung neuroendocrine cell`→`pulmonary neuroendocrine cell` for `CL:1000223`; `ciliated columnar cell of tracheobronchial tree`→`multiciliated columnar cell of tracheobronchial tree` for `CL:0002145`). F1=0 is accurate: wrong file, wrong pattern, plus reserialization scope creep.

## Strengths

- Identified the correct target relation `RO:0002162`/`in_taxon` and the correct set of life-stage ontologies (FBdv, WBls, ZFS) and their taxa.
- Correctly left the anatomical-ontology (`FBbt`, `WBbt`, `ZFA`, etc.) directives on `part_of`, showing awareness of the continuant/occurrent distinction.
- Documented its process and ran `robot convert` for round-trip validation per the OBO SOP (good instinct, wrong consequence here).

## Issues

- **Wrong mechanism (core error):** edited the legacy `treat-xrefs-as-reverse-genus-differentia` header directives, not the active SSSOM/T pipeline. None of the five gold files were touched.
- **Invalid construct:** `treat-xrefs-as-reverse-genus-differentia: FBdv in_taxon ...` misuses an OBO macro; the established way to get `in_taxon` into bridges is the `%TAXREL` mechanism in `bridges.rules`/`taxa.py`, not this directive. This would not produce the intended axioms.
- **Wrong pattern:** single-relation swap on the life-stage subset only; not the required dual-axiom (`'in taxon'` equivalence + `'part of'/'occurs in'` SubClassOf) form, and continuant bridges remain on `part_of`.
- **Scope creep / serialization artifact:** the `robot convert` reserialization injected ~8 unrelated CL-label changes across `UBERON:0002187`-region terms (multiciliated/secretory/pulmonary cell renames). These are CL import label re-syncs, not curator intent, and are confined to this attempt (not base contamination). They pollute the diff and would risk an unrelated, unreviewed label-churn change in a real PR.
- **Missed requirements:** no dual-axiom generation, no `config/taxa.yaml` `unfold_over` change, no `RO:0002012` import, no documentation updates (`docs/bridges.md`, `docs/combined_multispecies.md`).
