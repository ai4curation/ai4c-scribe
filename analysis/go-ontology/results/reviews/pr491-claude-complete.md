---
ontology: go-ontology
issue_number: 32005
pr_number: 32026
eval_repo_pr: 491
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.072
precision: 0.857
recall: 0.038
jaccard: 0.037
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
case_quality: poor
case_quality_reason: eval_base_state_contamination
---

## Summary

claude-sonnet-4.5/claude produced a substantively correct GO:0009095 obsoletion: name/def prefixed, all logical axioms + 5 synonyms removed, `is_obsolete: true`, both `consider: GO:0009094` and `consider: GO:0006571` added (with `! label` annotations), and tracker #32005 added while retaining #31091 (same defensible choice as the 0.927 gpt-5.5 runs). One sub-gold detail: the `xref: MetaCyc:PWY-3481` was **retained** on the obsolete stanza, whereas both the human gold and the best agent attempts removed it. The reported F1 of 0.072 is invalid as a quality measure due to **eval base-state contamination** — ~311 lines of unrelated foreign edits in the scored diff, byte-identical across all 9 low-scoring attempts and predating the agent.

## Strengths

- Core obsoletion is correct and well-formed; correct dual `consider` targets with accurate rationale (PWY-3481 = PWY-3462 + PWY-3461 → GO:0009094/GO:0006571).
- Thorough, accurate write-up: confirmed no internal references to GO:0009095, verified both consider terms exist with their narrowMatch MetaCyc xrefs, and correctly deferred the 4 EXP annotations to annotation review.
- Followed the `/term-obsoletion` skill and the checkout/checkin workflow; clear documentation of metadata decisions.

## Issues

- Sub-gold detail: retained `xref: MetaCyc:PWY-3481` on the obsolete term. The human gold and the top gpt-5.5 attempts removed it (since the superpathway is now decomposed onto GO:0009094/GO:0006571). Minor; xref retention on an obsolete term is sometimes done for provenance and the agent's own comment narrates the decomposition, but it diverges from the gold. This is the one genuine in-scope deviation.
- Scored eval PR dominated by foreign, unrelated edits — **base-state contamination**, not an agent error (same block as #291/#224/#223/#487/#525/#450/#404/#324). F1/recall are not a valid measure of this run.
- `failure_modes: [over_editing]` is an artifact of the contaminated scored diff, not behavior attributable to claude-sonnet-4.5. Recommend scoring on the GO:0009095 stanza only, or excluding/down-weighting; see Curation Note in METADATA.md.
