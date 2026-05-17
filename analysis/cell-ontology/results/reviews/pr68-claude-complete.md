---
ontology: cell-ontology
issue_number: 3519
pr_number: 3520
eval_repo_pr: 68
agent: std_opencode_gpt55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: simple
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes: [wrong_term, over_editing, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent created an oRGC2 term with the correct definition, both PMID xrefs, correct parent `CL_0000740`, and the requester's ORCID — substantively close to gold — but it minted the term as **`CL_9900001`** instead of the curator-assigned `CL_9900000`. Because `CL_9900001` is a different IRI (and is in fact the canonical ID the curator later assigned to the *sibling* term oRGC4 in PR #3516), every annotation's subject mismatches gold and metadiff scores a hard F1=0. This is a **placeholder-vs-canonical CL ID artifact**: the F1=0 dramatically over-states the failure, but the term content is largely correct. It additionally over-reaches by restructuring two existing terms.

## Strengths

- Definition matches the NTR semantics; both `PMID:37066415` and `PMID:31784286` present as `hasDbXref`.
- Correct requested parent `SubClassOf(... obo:CL_0000740)`.
- Requester ORCID recorded as `terms:contributor`.
- Used a valid temp ID range (`CL_99xxxxx`) per `cl-idranges.owl`; the choice of `CL_9900001` is a defensible-but-unlucky guess (no `CL_99xxxxx` IDs existed in the eval base, so the agent could not have known the curator would assign `CL_9900000`).
- Ran `robot convert` and `robot reason --reasoner ELK` for validation — good methodology.

## Issues

- **Wrong ID (artifact-level, F1=0 by construction):** used `CL_9900001`, not gold's `CL_9900000`. This single choice zeroes the metadiff even though the term is otherwise substantively correct. Note `CL_9900001` was independently assigned to oRGC4 by curators (PR #3516), so this is also a latent ID collision had both been minted naively — a real risk, not just a scoring artifact.
- **Scope / wrong pattern (genuine error):** the agent additionally asserted `SubClassOf(obo:CL_0020027 obo:CL_9900001)` and `SubClassOf(obo:CL_4033052 obo:CL_9900001)`, making the existing mouse ON-transient α RGC and primate ON parasol ganglion cell terms *subclasses* of the new orthotype. The gold does NOT do this, and pr182 explicitly flagged this exact modelling decision as needing curator review rather than asserting it. Making species-specific established terms children of a freshly minted orthotype is an over-reaching ontological change that should not have been made unilaterally.
- **Scope (over-editing):** added `terms:creator`, `terms:date`, `IAO_0000233` not retained in gold.
- Net: even discounting the ID artifact, this attempt is weaker than pr182/pr3 because of the unrequested re-parenting of two existing terms.
