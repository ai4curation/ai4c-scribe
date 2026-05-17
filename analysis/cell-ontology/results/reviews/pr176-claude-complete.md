---
ontology: cell-ontology
issue_number: 3267
pr_number: 3268
eval_repo_pr: 176
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: documentation
difficulty: simple
f1: 0.361
precision: 0.733
recall: 0.239
jaccard: 0.220
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent wrote the strongest, most precise creator/contributor guardrail of any attempt — explicitly forbidding agent-named `terms:contributor`/`dc:contributor` axioms (the exact QC-failing pattern the issue describes) and reserving `terms:contributor` for human-curator ORCIDs on new terms only — and made both correct sign-off swaps. However, it delivered this inside a large unrequested structural rewrite of `CLAUDE.md` (Project Layout, Querying examples, OBO Guidelines, Obsoleting/metadata reorganization), deleting the eval-base `created_by` line wholesale rather than editing it in place. F1=0.361 (P=0.733, R=0.239) reflects that the surgical core change is swamped by out-of-scope edits.

## Strengths

- Both `@dragon-ai-agent` → `GitHub Copilot` sign-off swaps are correct and match the gold.
- Best substantive guidance of all seven attempts: the new bullet pinpoints the issue's root cause exactly — "NEVER add a `terms:contributor` (or `dc:contributor`) axiom whose value is the agent name ... this fails QC" — and correctly scopes `terms:creator` to new-term creation with concrete examples (`obo:CL_0000118`, ORCID). Semantically a clear superset of the gold's terser wording.
- PR/issue comment articulates the QC root cause accurately and concisely.

## Issues

- **Heavy over-editing / scope creep**: rewrote Project Layout ("ONLY EDIT THIS FILE"), the `grep`/`obo-grep.pl` Querying block, the NTR `CL_99xxxxx`/`idrange:81` line, and restructured the Obsoleting/metadata sections — none asked for by issue #3267 (a documentation-only, simple case).
- **Structural divergence from the human's 3-line surgical edit**: the eval-base canonical line `- You can sign terms as 'created_by: dragon-ai-agent'` (the precise line the gold rewrites) was deleted with its block and the replacement guidance relocated into a new "## Other metadata" section. Net content is correct and arguably improved, but the document was reorganized far beyond the issue's ask, which is what drives the low metadiff — a fair reflection, not under-representation.
- Did not add the SPARQL `<http://purl.org/dc/creator>` whitelist line (metadiff recall ceiling; the issue text does not mention SPARQL — minor relative to the scope problems).
- Net assessment: high-quality guidance content undermined by poor scope discipline; would require maintainer trimming before merge despite being substantively the best wording.
