---
ontology: cell-ontology
issue_number: 3267
pr_number: 3268
eval_repo_pr: 92
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: documentation
difficulty: simple
f1: 0.467
precision: 0.933
recall: 0.311
jaccard: 0.304
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly performed both `@dragon-ai-agent` → `GitHub Copilot` sign-off swaps and added solid creator-vs-editor metadata guidance, but it buried these in a sprawling unrelated rewrite of `CLAUDE.md` (Project Layout, Querying ontology, OBO Guidelines, Obsoleting terms sections) and — most seriously — **deleted `.github/copilot-instructions.md`**, a symlink that points to `CLAUDE.md` and is the very file GitHub Copilot reads. F1=0.467 with precision 0.933 / recall 0.311 correctly reflects "did the core change but added a large volume of out-of-scope edits." The headline finding is the destructive symlink removal, which is directly counterproductive to an issue about configuring Copilot.

## Strengths

- Both sign-off line changes (`always sign your commits` and `Sign all commits and PRs as`) are correct and match the gold.
- The new "## Other metadata" section contains accurate, well-formed guidance: `dc:creator "GitHub Copilot"` only for new terms, explicit "You should not add yourself as a creator if you are editing existing terms," and correct ORCID-as-`terms:contributor` example — substantively aligned with the gold's intent.
- Demonstrated awareness of the issue's QC-failure root cause (spurious contributor on definition edits) in its rationale.

## Issues

- **Destructive, counterproductive deletion**: removed `.github/copilot-instructions.md` (a `120000` symlink → `../CLAUDE.md`). The agent's justification ("stale reference/symlink ... no longer needed") is wrong — that symlink is precisely how GitHub Copilot picks up the instructions this issue is about. Deleting it undermines the issue's goal and was never requested.
- **Heavy over-editing / scope creep**: rewrote unrelated content the issue never mentioned — Project Layout ("ONLY EDIT THIS FILE"), the `grep`/`obo-grep.pl` Querying examples, the NTR `CL_99xxxxx` / `idrange:81` line, and restructured the Obsoleting/metadata sections. None of this serves issue #3267.
- The eval-base `CLAUDE.md` (blob `42d6ee51a`, correct pre-#3268 state) had a single canonical "## Other metadata" block; the agent both modified that block AND introduced a second metadata block earlier, leaving the document with two near-duplicate creator-signing bullets (one `dc:creator`, one `terms:creator`) — internally inconsistent.
- Did not add the SPARQL `<http://purl.org/dc/creator>` whitelist line (metadiff recall ceiling; not in issue text — minor relative to the scope problems above).
