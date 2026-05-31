---
ontology: cell-ontology
issue_number: 3519
pr_number: 3520
eval_repo_pr: 49
agent: std_opencode_g55
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

This attempt is byte-identical to pr68 (same diff, same blob `e540d57`): the agent created oRGC2 with the correct definition, both PMID xrefs, correct parent `CL_0000740`, and requester ORCID, but minted it as **`CL_9900001`** instead of gold's `CL_9900000`. The F1=0 is a **placeholder-vs-canonical CL ID artifact** that grossly over-states the failure — the term content is largely correct — but the attempt independently over-reaches by re-parenting two existing terms under the new orthotype, which is a genuine error.

## Strengths

- Definition matches NTR semantics; both `PMID:37066415` and `PMID:31784286` present as `hasDbXref`.
- Correct requested parent `SubClassOf(... obo:CL_0000740)`.
- Requester ORCID recorded as `terms:contributor`.
- Valid temp ID range used; ran `robot convert` for syntax validation.

## Issues

- **Wrong ID (artifact-level, F1=0 by construction):** `CL_9900001` instead of gold's `CL_9900000`. `CL_9900001` is the canonical ID curators later assigned to the sibling term oRGC4 (PR #3516), so this is both a metadiff artifact and a latent ID collision.
- **Scope / wrong pattern (genuine error):** added `SubClassOf(obo:CL_0020027 obo:CL_9900001)` and `SubClassOf(obo:CL_4033052 obo:CL_9900001)`, making the established mouse ON-transient α RGC and primate ON parasol ganglion cell terms subclasses of the new orthotype. Gold does not do this; pr182 correctly deferred this modelling decision to curators. Unilaterally re-parenting existing terms is over-reaching.
- **Scope (over-editing):** added `terms:creator`, `terms:date`, `IAO_0000233` not retained in gold.
- Identical content to pr68; same assessment. The substantive term creation is sound but undermined by the unrequested structural changes.
