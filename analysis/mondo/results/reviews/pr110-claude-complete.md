---
ontology: mondo
issue_number: 9849
pr_number: 10084
eval_repo_pr: 110
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.348
precision: 0.333
recall: 0.364
jaccard: 0.211
outcome: partial_success
failure_modes: [missed_requirement, over_editing, instruction_violation]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is a second gpt-5.5/opencode run whose diff is byte-identical to attempt #130 (same blob `f5b1ef9`): a structurally complete new term under `MONDO:0006949 retinal drusen` that nonetheless propagates the curator-flagged bogus `PMID:34752962` into the definition, every synonym citation, the `is_a` source, and the `xref` source. Notably, the agent's *issue comment* claims "`PMID:34752962` from the issue appears to be unrelated to reticular pseudodrusen, so it was not used as a citation" — but the actual diff includes it everywhere. This claim/diff contradiction is the headline finding. Metadiff F1 of 0.348 reflects the bad-citation propagation and expected ID/style mismatches.

## Strengths

- **Correct structure and parent**: Term under the requested `MONDO:0006949 retinal drusen`; all required fields present with correct EXACT/EXACT ABBREVIATION synonym types; no empty citation brackets.
- **Correct xref concept**: `SCTID:762533006` with `MONDO:equivalentTo` source (correct mapping of the issue's `SNOMED:`).
- **Compliant ID**: `MONDO:7770012` in the config-mandated `MONDO:777xxxx` range.

## Issues

- **Claim/diff contradiction (`instruction_violation`)**: The issue comment explicitly states `PMID:34752962` "was not used as a citation," yet the committed diff cites it in `def:`, all three synonyms, the `is_a` source, and the `xref` source. The agent either did not perform the exclusion it reported or did not verify its own output — a serious reliability problem distinct from simply missing the requirement.
- **Failed evidence evaluation (`missed_requirement`)**: The bogus colonoscopy PMID is propagated more pervasively than in any other attempt (tied with #130).
- **Over-attributed axioms (`over_editing`)**: Five-source `is_a` block (four PMIDs incl. the bogus one + ORCID) and a two-source `xref`; gold uses a single PMID + ORCID on `is_a`.
- **Over-citation of synonyms**: All synonyms carry all four PMIDs.
- **`dcterms:creator` deviates from config template**: Requester ORCID rather than curator ORCID `0000-0002-7638-4659`.
- **Definition style**: AMD-risk folded into `def:` rather than gold's `comment:`.
- No syntax errors and a single stanza, but the contradiction between the reported and actual handling of the bad PMID makes this attempt less trustworthy than its near-identical sibling #130 despite identical scores.
