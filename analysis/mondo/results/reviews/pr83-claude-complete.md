---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 83
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.921
precision: 0.906
recall: 0.935
jaccard: 0.853
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.5 / opencode correctly merged MONDO:0034186 into MONDO:0029144 with a
canonical obsolete stanza and full annotation transfer (blob `5afd59d`). It is
the lowest-F1 variant (0.921) because it stacks two defensible-but-divergent
choices seen individually in higher-scoring attempts: (1) it removed the
redundant `is_a: MONDO:0003847 ! hereditary disease` from the survivor
(entailed via the transferred MONDO:0019222), and (2) it wrote the transferred
characteristic as `has_characteristic HP:0000007 {source="Orphanet:562538"}`
with explicit provenance. Both are reasoned in the PR comment; neither is an
ontological error. Metadiff F1=0.921 **under-represents** quality — the core
merge is correct and the divergences are arguably improvements over the
conservative gold.

## Strengths

- Correct, complete merge; canonical obsoletion metadata (`MONDO:TermsMerged`,
  `replaced_by: MONDO:0029144`, `is_obsolete`, #9842 tracker item including the
  tracker item added to the survivor).
- Full annotation transfer with the transferred synonym correctly re-cited to
  `[Orphanet:562538]`; scheduling artifacts removed.
- Documented validation: `make NORM`, reference-integrity check for
  MONDO:0034186, no-`alt_id` check, and the six merge QC SPARQL queries all
  passing.
- Redundant-parent removal correctly reasoned (MONDO:0019222 sits under inborn
  errors of metabolism, which has hereditary disease as an ancestor).

## Issues

- Scope: removal of `is_a: MONDO:0003847` plus the extra
  `{source="Orphanet:562538"}` on the `has_characteristic` axiom both exceed the
  literal merge request and diverge from gold. Each is independently defensible;
  combined they account for the lowered F1. A reviewer wanting a tight merge-only
  PR would prefer the conservative top-tier form.
- Cosmetic-only: did not reproduce the gold's two-synonym reorder churn (left in
  place). Not an error.
- No substantive errors.
