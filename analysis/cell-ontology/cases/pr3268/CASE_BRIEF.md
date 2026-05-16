---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3267
pr_number: 3268
issue_title: Update claude.md instructions for GitHub Copilot
pr_author: Caroline-99
pr_merged_at: '2025-10-29'
task_type: documentation
difficulty: simple
scoping: mostly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 7
generated_at: '2026-05-15'
scoping_notes: Primary change is CLAUDE.md update, with a minor incidental SPARQL
  file addition.
domain_area: infrastructure
best_f1: 0.897
best_model: gpt-5.4
---

# PR #3268 — Update claude.md instructions for GitHub Copilot

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3267](https://github.com/obophenotype/cell-ontology/issues/3267) | [PR #3268](https://github.com/obophenotype/cell-ontology/pull/3268) | @Caroline-99 | merged 2025-10-29

`documentation` `simple` `mostly_scoped` `approved_first_time`

## Context

The cell ontology repository uses a CLAUDE.md file to provide instructions to AI agents (Claude, GitHub Copilot) working on the codebase. The instructions needed updating to specify how GitHub Copilot should add `dc:creator` attribution when making changes, ensuring proper provenance tracking for AI-generated contributions.

## Changes Made

Modified 3 lines in `CLAUDE.md` to update the agent instructions for dc:creator attribution. Also added 1 line to a SPARQL file for detecting illegal annotation property violations. The documentation change is the primary focus.

## Resolution

Approved on first review. Simple difficulty because this is a documentation-only change, but it is an interesting case study for understanding how ontology repositories configure AI agent behavior and maintain contributor attribution standards.

## Human Diff

```diff
diff --git a/CLAUDE.md b/CLAUDE.md
index 42d6ee51a..f460173e0 100644
--- a/CLAUDE.md
+++ b/CLAUDE.md
@@ -55,13 +55,13 @@ This includes instructions for editing the cl ontology.
 - always commit in a branch, e.g. issue-NNN
 - if there is an existing PR which you started then checkout that branch and continue, rather than starting a new PR (unless you explicitly want to abandon the original PR, e.g. it was on completely the wrong tracks)
 - always make clear detailed commit messages, saying what you did and why
-- always sign your commits `@dragon-ai-agent`
+- always sign your commits `GitHub Copilot`
 - create PRs using `gh pr create ...`
 - File PRs with clear descriptions, and sign your PR
 
 ## Handling GitHub issues and requests
 - Use `gh` to read and write issues/PRs
-- Sign all commits and PRs as `@dragon-ai-agent`
+- Sign all commits and PRs as `GitHub Copilot`
 
 ## TROUBLESHOOTING
 
@@ -99,7 +99,7 @@ terms to "skip" the obsoleted term.
 
 - Link back to the issue you are dealing with using the `term_tracker_item`
 - All terms should have definitions, with at least one definition xref, ideally a PMID
-- You can sign terms as `created_by: dragon-ai-agent`
+- You can sign terms as `dc:creator "GitHub Copilot"` only when creating new terms. You should not add yourself as a creator if you are editing existing terms.
 
 ## Relationships
 
diff --git a/src/sparql/illegal-annotation-property-violation.sparql b/src/sparql/illegal-annotation-property-violation.sparql
index 7cb6cb3c4..defdf044f 100644
--- a/src/sparql/illegal-annotation-property-violation.sparql
+++ b/src/sparql/illegal-annotation-property-violation.sparql
@@ -31,6 +31,7 @@ SELECT DISTINCT ?term ?annotation WHERE {
     <http://purl.org/dc/terms/description>,
     <http://purl.org/dc/terms/source>,
     <http://purl.org/dc/terms/contributor>,
+    <http://purl.org/dc/creator>,
     <http://purl.org/spar/cito/citesAsAuthority>,
     <http://www.geneontology.org/formats/oboInOwl#consider>,
     <http://www.geneontology.org/formats/oboInOwl#creation_date>,

```

## Agent Attempts (7)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | gpt-5.4 | codex | 0.897 | 0.867 | 0.929 | `d4f65ac` | [#81](https://github.com/ai4curation/eval-ont-agent-cl/pull/81) | [attempt](attempts/pr81.md) |
| 2 | gpt-5.5 | opencode | 0.897 | 0.867 | 0.929 | `00eb0c6` | [#71](https://github.com/ai4curation/eval-ont-agent-cl/pull/71) | [attempt](attempts/pr71.md) |
| 3 | gpt-5.5 | opencode | 0.897 | 0.867 | 0.929 | `00eb0c6` | [#53](https://github.com/ai4curation/eval-ont-agent-cl/pull/53) | [attempt](attempts/pr53.md) |
| 4 | claude-haiku-4.5 | claude | 0.467 | 0.933 | 0.311 | `0000000` | [#92](https://github.com/ai4curation/eval-ont-agent-cl/pull/92) | [attempt](attempts/pr92.md) |
| 5 | claude-sonnet-4.5 | claude | 0.387 | 0.800 | 0.255 | `c4a93f6` | [#215](https://github.com/ai4curation/eval-ont-agent-cl/pull/215) | [attempt](attempts/pr215.md) |
| 6 | claude-opus-4.7 | claude | 0.361 | 0.733 | 0.239 | `16fa554` | [#176](https://github.com/ai4curation/eval-ont-agent-cl/pull/176) | [attempt](attempts/pr176.md) |
| 7 | gpt-5.5 | codex | 0.361 | 0.733 | 0.239 | `268ff48` | [#34](https://github.com/ai4curation/eval-ont-agent-cl/pull/34) | [attempt](attempts/pr34.md) |
