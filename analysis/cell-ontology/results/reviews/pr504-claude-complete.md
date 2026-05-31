---
ontology: cell-ontology
issue_number: 3267
pr_number: 3268
eval_repo_pr: 504
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: documentation
difficulty: simple
case_quality: good
f1: 0.448
precision: 0.867
recall: 0.302
jaccard: 0.289
outcome: partial_success
failure_modes:
  - scope_creep
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent correctly made both changes issue #3267 explicitly asked for in `CLAUDE.md` — both `@dragon-ai-agent` sign-off lines replaced with `GitHub Copilot`, and the `created_by: dragon-ai-agent` term-signing line rewritten to `dc:creator "GitHub Copilot"` for newly created terms only with an explicit prohibition on creator/contributor metadata when editing existing terms (the QC-failure root cause named in the issue body). However, the diff (blob `f5ef7f7f2`, byte-identical to sibling pr565) bundles substantial unrequested rewrites: the `## Project Layout`, `## Querying ontology`, and `## OBO Guidelines` sections were rewritten, the obsoletion/merge section restructured, and an entirely new `## Other metadata` block (terms:date, ORCID `terms:contributor` guidance) was inserted — none of which the issue requested. F1=0.448 under-represents the *correctness* of the two required edits but the low recall (0.302) genuinely reflects real scope creep, not a metadiff artifact.

## Strengths

- Both gold sign-off line changes match exactly: the commit-signature line (~line 56) and the "Handling GitHub issues and requests" line (~line 62) both go from `@dragon-ai-agent` to `GitHub Copilot`.
- The term-metadata rewrite at the `created_by` line (~line 99) is semantically a superset of the gold's guidance: it restricts `dc:creator "GitHub Copilot"` to new terms only and explicitly prohibits `dc:creator`/contributor annotations on edits including textual definition updates — directly targeting the issue's stated QC-failure cause (spurious `dc:contributor "dragon-ai-agent"` added during definition edits).
- Single-file change: confined to `CLAUDE.md`; no spurious edits to ontology source files.
- Precision 0.867 confirms the lines the agent did change are substantively the right ones.

## Issues

- **Scope creep (primary):** The agent rewrote multiple sections the issue never mentioned — `## Project Layout` ("ONLY EDIT THIS FILE, or files under docs/"), the entire `## Querying ontology` section (replaced the neuron grep examples with `CL_0004177` examples), the `## OBO Guidelines` NTR line, and the obsoletion/merge prose. It also inserted a brand-new `## Other metadata` block duplicating term_tracker_item/definition guidance and adding unrequested `terms:date` and ORCID `terms:contributor` rules. These are unsolicited edits to agent-instruction policy and are the dominant driver of recall=0.302 — a real quality problem, not just style.
- The new `## Other metadata` block partially duplicates the existing canonical metadata section further down the file (the `created_by` line still appears separately at ~line 99), creating two overlapping sets of attribution guidance — exactly the kind of conflicting-instruction risk the issue was trying to eliminate.
- Did not add `<http://purl.org/dc/creator>` to `src/sparql/illegal-annotation-property-violation.sparql`. The gold PR added this as a QC-whitelisting corollary, but the issue text contains no mention of SPARQL/QC whitelisting, so this is a metadiff recall ceiling rather than a substantive omission.
- Whitespace churn (trailing-newline removal near line 130) adds noise unrelated to the task.

Net: the core task is done correctly, but the unrequested structural rewrites and duplicated metadata block prevent this from being a clean success — `partial_success`. This is a good evaluation case (`case_quality: good` per METADATA.md); the low F1 reflects genuine over-editing, not a poor reference.
