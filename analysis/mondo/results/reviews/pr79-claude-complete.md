---
ontology: mondo
issue_number: 10149
pr_number: 10156
eval_repo_pr: 79
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.476
precision: 0.417
recall: 0.556
jaccard: 0.312
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: placeholder_id_artifact_plus_gold_out_of_scope
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly created `podocytopathy` as a new grouping term under `MONDO:0019722 glomerular disorder` and reclassified the two children explicitly requested in issue #10149 (`MONDO:0006835` minimal change disease / lipoid nephrosis, and `MONDO:0100313` focal segmental glomerulosclerosis). The metadiff F1 of 0.476 substantially **under-represents** quality: it is mechanically capped by (a) the unavoidable placeholder-vs-canonical MONDO ID artifact — the agent uses the eval-base temp ID `MONDO:7770018` while the gold curator assigned canonical `MONDO:0700328`, mismatching every `id:`/`is_a:` line — and (b) the gold PR doing substantially more than the issue asked (a third child, an equivalence axiom, an SCTID xref). Judged against the issue's actual asks, this is essentially a complete, correct solution.

## Strengths

- Correctly created `podocytopathy` with the exact parent requested in the issue (`MONDO:0019722 glomerular disorder`) and a definition closely paraphrasing the issue text, sourced to the three issue-supplied PMIDs (PMID:25684864, PMID:32792490, PMID:38804512).
- Added both issue-requested children (`MONDO:0006835`, `MONDO:0100313`) as additional `is_a: podocytopathy` parents while **preserving their existing parents** (glomerulonephritis / glomerulosclerosis) — exactly the additive reclassification the gold PR also performed.
- Used `subset: disease_grouping`, which is the correct MONDO convention for a grouping class and is consistent with how the curator intended the term to function.
- Recorded the contributor ORCID (`0009-0009-0876-0331`) via `dcterms:creator` and the issue-tracker link via `IAO:0000233` on the new term — matching MONDO metadata conventions and the gold.
- The opencode run log (pr61 sibling, same blob) documents thorough methodology: PMID verification via PubMed, CL:0000653 podocyte verified via OLS, ORCID verified, `robot convert` + `make NORM` + `robot reason` ELK all run.

## Issues

- Did not reproduce the gold's logical (equivalence) definition: `intersection_of: MONDO:0019722` + `intersection_of: disease_has_location CL:0000653` plus the matching `relationship: disease_has_location CL:0000653`. This is a genuine quality gap vs. the gold, but the issue did not request a logical definition and the agent reasonably produced a plain `is_a` grouping term; the curator's genus-differentia modeling is a defensible enrichment beyond the request.
- Did not add the third child the gold added — `MONDO:0005376 membranous glomerulonephritis` (membranous nephropathy). This child was **not listed in the issue** (the issue named only lipoid nephrosis and FSGS), so its omission is a scope-faithful choice, not an error against the request.
- Did not add `xref: SCTID:1367669003 {source="MONDO:equivalentTo"}` or the per-child `property_value: IAO:0000233` tracker lines that the gold added; minor metadata deltas, none requested in the issue.
- Source attributions on the child `is_a` axioms differ in formatting from the gold (agent cites PMIDs + issue URL; gold cites a different PMID set including PMID:41381622 / PMID:17699461 that the curator added from independent literature). This is normal metadiff under-representation, not a substantive error.
