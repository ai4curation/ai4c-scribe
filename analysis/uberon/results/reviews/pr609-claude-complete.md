---
ontology: uberon
issue_number: 3602
pr_number: 3603
eval_repo_pr: 609
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: simple
case_quality: good
f1: 0.923
precision: 1.000
recall: 0.857
jaccard: 0.857
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/opencode added `UBERON:8600149` "occlusal surface of tooth" as a
subclass of `UBERON:8600148` "tooth surface structure". The substantive term
content is byte-identical to the gold PR #3603 stanza: same ID, name,
definition with *both* issue cross-references, EXACT synonym `"occlusal
surface"` with the dentaleducationhub reference, correct `is_a`, and
wdduncan's requester ORCID `0000-0001-9625-1899`. Metadiff F1=0.923
(P=1.000, R=0.857) **under-represents** quality: precision is perfect and the
recall gap is entirely (a) the two CLAUDE.md-mandated metadata lines and (b)
one trailing-newline normalization from the required `robot convert`
reserialization. This is the same diff as #668 from the same model/runtime,
and is a clean `success`.

## Strengths

- **Term content matches gold exactly**: id `UBERON:8600149`, name, full def
  text, *both* def xrefs (`dentaleducationhub.com` + HL7
  `CodeSystem-FDI-surface.html`) — matching the two cross-references in issue
  #3602's body and the gold's two-xref def.
- **Correct synonym and parent**: EXACT synonym `"occlusal surface"` with the
  `dentaleducationhub.com/surfaces-of-the-teeth/` reference @aleixpuigb
  specified; `is_a: UBERON:8600148 ! tooth surface structure` as requested.
- **Correct attribution**: `relationship: dc-contributor
  https://orcid.org/0000-0001-9625-1899` — the exact ORCID the gold uses.
- **Followed CLAUDE.md metadata guidance**: added `term_tracker_item`
  pointing at issue #3602 and `created_by: dragon-ai-agent`, both required by
  the agent config though absent from the minimal gold stanza.

## Issues

- **robot-convert trailing-newline churn (artifact, not a defect)**: one
  EOF blank-line removal in the typedef block, a benign side effect of the
  mandated reserialization step; minor recall contributor, no semantic
  impact.
- **No genuine ontological issues.** The metadiff gap is required metadata
  plus serialization normalization; the term is correct and complete.
