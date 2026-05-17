---
ontology: uberon
issue_number: 3475
pr_number: 3477
eval_repo_pr: 11
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3:.
case_type: axiom_repair
difficulty: medium
f1: 0.100
precision: 1.000
recall: 0.053
jaccard: 0.053
outcome: partial_success
failure_modes: [over_editing, scope_creep]
case_quality: poor
case_quality_reason: gold_pr_is_partial
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The issue-relevant edits are correct: the agent removed `is_a: UBERON:0000961` from UBERON:0002835 (ask #1) and renamed UBERON:0000961 → "thoracic paravertebral ganglion" (ask #2), addressing both explicit requests of issue #3475 with clean, tightly-scoped changes to those two stanzas. **However**, like #193, the diff is swamped by a large block of unrelated CL term-label rewrites (`lung ciliated cell` → `lung multiciliated epithelial cell`, `ciliated cell of the bronchus` → `multiciliated epithelial cell of the bronchus`, `glandular epithelial cell` → `glandular secretory epithelial cell`, `lung neuroendocrine cell` → `pulmonary neuroendocrine cell`) plus a synonym-line reorder on UBERON:0003532. The metadiff F1 of 0.100 reflects both the partial gold and this self-inflicted file regeneration. Outcome `partial_success`.

## Strengths

- **Both issue asks satisfied** in the relevant stanzas: spurious is_a on UBERON:0002835 removed; UBERON:0000961 renamed to "thoracic paravertebral ganglion"; old name kept as a `RELATED` synonym.
- **Strongest design-pattern reasoning of the eight attempts:** the PR explicitly notes the rename "restores consistency with the existing regional dorsal root ganglion pattern already used for cervical, lumbar, and sacral dorsal root ganglion classes, where the class is defined by genus-differentia rather than as a subclass of a sympathetic/paravertebral ganglion term." This is exactly the right ontological justification and shows the agent checked sibling patterns.
- The is_a-removal hunk itself is clean and matches gold precisely.

## Issues

- **ODK build-regenerated-file domination (primary):** ~9 hunks of CL label rewrites on lung/bronchus/epithelium terms unrelated to #3475. Verified against eval base branch `eval-base-issue-3475`, which holds the *old* labels — so the agent regenerated/relabelled the file itself (likely `robot convert -o src/ontology/uberon-edit.obo` reserialization picking up newer CL import labels), not base contamination. This dominates the diff and craters recall (0.053); it is a genuine scope failure.
- **Spurious reorder:** the two `synonym: "lower limb skin" EXACT [...]` lines on UBERON:0003532 were transposed (FMA vs ORCID source ordering swapped) — a pure serialization-order artifact with no semantic content, pure diff noise.
- **Over-editing (synonyms):** deleted `ganglion of thorax` and `thorax ganglion` automatic synonyms outright rather than rescoping them (BROAD, as #56/#37 did, would have preserved them).
- The trailing-newline / reserialization churn confirms the whole file was round-tripped through ROBOT, the root cause of the off-topic label block.
- Net: correct core fix with the best pattern rationale, but file-regeneration domination plus synonym deletion make the overall submission low quality independent of the poor-case scoring. See METADATA.md.
