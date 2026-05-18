---
ontology: cell-ontology
issue_number: 3534
pr_number: 3535
eval_repo_pr: 300
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: new_term
difficulty: medium
case_quality: ok
case_quality_reason: sound_gold_but_new_term_scores_sensitive_to_taxon_and_provenance
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes:
  - misattribution
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This is the strongest of the gpt-5.4/gpt-5.5 attempts on this case in modeling
substance: the agent added "hybrid osteochondral skeletal cell" with the verbatim
issue definition (`PMID:30983567` xref), correct periosteum location
`BFO_0000050 some UBERON_0002515` (the *right* relation and the *right* UBERON term,
matching the gold), and the full mouse taxon treatment (`RO_0002162 some
NCBITaxon_10090` + `RO_0002175` annotation). The metadiff F1=0.000 is almost entirely
provenance/ID-convention noise plus one defensible extra parent — not a modeling
failure. The headline defect is a **misattribution**: the agent claimed (via OLS) the
term already exists upstream as `CL:0020028` and minted that ID instead of the
canonical placeholder `CL_9900000` the gold used. Partial success that is
substantively close to gold.

## Strengths

- Correct periosteum modeling: `SubClassOf BFO_0000050 some UBERON_0002515` — the
  same relation (`part_of`) and the same UBERON term as the gold (`UBERON_0002515`,
  periosteum). This is exactly right and better than the opencode gpt-5.4 attempts
  (#582/#520, which used `RO_0002100`) and the gpt-5.5 attempts (#484/#545, which
  used the wrong UBERON ID `UBERON_0001434` = skeletal system).
- Full taxon treatment: `RO_0002162 some NCBITaxon_10090` plus the `RO_0002175`
  "present in taxon" annotation — matches the gold's complete mouse modeling.
- Verbatim issue definition preserved with correct `oboInOwl:hasDbXref
  "PMID:30983567"` on `IAO_0000115`; correct contributor ORCID and
  `terms:creator "GitHub Copilot"`.
- Strong methodology trail: read issue context, checked existing labels/IDs, queried
  OLS for the periosteum UBERON ID, queried PubMed for PMID:30983567 to align the
  definition; honestly reported that `robot` was unavailable.

## Issues

- Misattribution: claimed the term "already exists upstream as `CL:0020028`" and
  minted `CL_0020028` rather than the canonical `CL_9900000` placeholder the gold
  used for this genuinely new term. The OLS-based "already exists" inference is
  incorrect; this ID-convention miss is the dominant cause of F1=0.000 despite
  near-correct modeling.
- Scope: added a second parent `SubClassOf CL_0001035` (bone cell) not in the gold.
  Defensible (the cell co-expresses bone regulators) but the gold deliberately keeps
  a single skeletogenic-cell parent to avoid forcing it into the osteoblast lineage;
  this lowers recall and is an over-edit relative to the tightly-scoped gold.
- Scope: extra `IAO_0000233` term-tracker annotation absent from the gold
  (defensible provenance, minor).
