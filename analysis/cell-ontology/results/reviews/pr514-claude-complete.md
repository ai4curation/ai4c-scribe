---
ontology: cell-ontology
issue_number: 3519
pr_number: 3520
eval_repo_pr: 514
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: simple
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes:
  - over_editing
  - placeholder_id
case_quality: ok
case_quality_reason: sound_gold_but_patterned_new_term_scores_sensitive_to_provenance
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent created the requested oRGC2 retinal ganglion cell orthotype term with a faithful definition, the correct parent (`CL_0000740`, retinal ganglion cell), the requested ORCID contributor, and both issue-specified PMIDs. The diff is byte-identical to attempt #577 (same blob `997deaa`, also gpt-5.4/opencode). The reported F1=0.000 substantially under-represents quality: it is driven by the config-mandated placeholder ID (`CL_9900001` vs gold's curator-assigned `CL_9900000`) compounded by provenance-field and synonym divergences — the established `case_quality: ok` provenance-sensitivity pattern for this case. Substantively a partial success.

## Strengths

- **Correct parent**: `SubClassOf(obo:CL_9900001 obo:CL_0000740)` matches gold and the issue's requested parent `CL_0000740` exactly.
- **Faithful definition with correct references**: Definition captures the conserved orthotype grouping primate ON parasol RGCs with the homologous mouse ON-transient alpha RGC subtype (C41); xref'd to `PMID:37066415` and `PMID:31784286` exactly as the issue specified (gold uses the same two PMIDs).
- **Correct contributor**: `terms:contributor ... <https://orcid.org/0000-0002-5507-2103>` matches the ORCID requested in the issue and used by gold.
- **Tightly scoped to the right file**: Only `src/ontology/cl-edit.owl` touched; one new term added.

## Issues

- **Placeholder ID, not canonical (poor-score driver, not an agent fault)**: Used `CL_9900001` where gold assigned `CL_9900000`. Config-driven and the primary reason F1=0.000; flagged at the case level (`sound_gold_but_patterned_new_term_scores_sensitive_to_provenance`).
- **Unrequested exact synonyms (over-editing)**: Added `hasExactSynonym "C41"` and `hasExactSynonym "ON parasol RGC orthotype"`. Neither was requested in the issue (Synonyms field left blank) nor present in gold; "C41" is a transcriptomic cluster label whose status as an exact synonym of the orthotype is debatable.
- **Extra provenance metadata diverging from gold (over-editing)**: Added `terms:creator "GitHub Copilot"`, `terms:date`, and an `IAO_0000233` issue-link annotation that gold did not include, while omitting the `oboInOwl:id` assertion gold carried. These reduce normalized overlap and are not requested by the issue.
- **Definition wording divergence (style)**: Substitutes "mouse alpha retinal ganglion cell ON-transient subtype, C41" for the issue's "mouse α RGC subtype (ON-transient α RGC, C41)" and drops the "(Hahn et al., 2023; Tran et al., 2019)" attribution that gold retained — substantively equivalent but not verbatim.
- **No build/reasoning validation**: This attempt provides only the diff (no PR-comment notes); consistent with #577, validation appears limited to file inspection without an ontology build/reasoning pass.
