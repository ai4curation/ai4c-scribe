---
ontology: uberon
issue_number: 3473
pr_number: 3494
eval_repo_pr: 289
agent: std_claude_son45
model: claude-sonnet-4-5-20250929
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.160
precision: 0.105
recall: 0.333
jaccard: 0.087
outcome: success
failure_modes: [under_editing, over_editing]
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extra_edits
companion_prs: []
scoring_caveat: "metadiff vs #3494 is dominated by ~11 lines of issue-irrelevant churn (CL label-comment refreshes CL:1000271/CL:0002145/CL:0002332/CL:1000223/CL:0000150, synonym reorder in UBERON:0003532) from a master-merge + ROBOT reserialization, plus reasoner-driven endocardium/synovial is_a deletions negotiated only in the PR comment thread. Genuine in-scope content is ~4 has_part→composed_primarily_of swaps; this attempt reproduces 1. F1=0.160 under-represents the correctness of the core fix but the run adds the most non-gold noise of the cohort."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly fixed `squamous epithelium` (UBERON:0006914) — `has_part CL:0000076` → `composed_primarily_of CL:0000076` (matches gold) — and aligned the text definition, but also added the most non-gold metadata of any attempt: a free-text `comment:`, a `dcterms-date`, a `term_tracker_item`, and `created_by: dragon-ai-agent`. It did not propagate the fix to the simple/stratified subclasses. The core axiom change is correct (so F1 0.160 **under-represents** the in-scope correctness), but this run combines under-editing on the substantive axioms with over-editing on provenance/commentary, the weakest precision-against-intent profile in the cohort.

## Strengths

- Core logical-definition repair on UBERON:0006914 is exactly right (`composed_primarily_of`, RO:0002473, CL:0000076), matching gold.
- Text-definition rewrite ("An epithelium that is primarily composed of squamous epithelial cells.") is biologically accurate.
- The issue comment correctly flags the need to test with a reasoner and warns the change could affect other classifications — good awareness of the downstream effect that, in the real PR, became the endocardium/synovial discussion.

## Issues

- Over-editing: adds four non-gold lines to the stanza — a verbose `comment:` restating the changelog inline (ontology comments are not the place for PR-style change rationale; this is what `term_tracker_item` is for), `property_value: dcterms-date "2026-05-14T00:00:00Z" xsd:dateTime`, `property_value: term_tracker_item ".../issues/3473" xsd:anyURI`, and `created_by: dragon-ai-agent`. The agent config prescribes `dcterms-date`/`dc-contributor` provenance for *new* terms; UBERON:0006914 is a pre-existing term being repaired, so stamping `created_by`/`dcterms-date` on it is incorrect provenance (it misattributes term creation to the agent). None of this is in gold.
- Under-editing on the substantive axioms: only UBERON:0006914 fixed; `simple squamous epithelium` (UBERON:0000487) and `stratified squamous epithelium` (UBERON:0006915) — fixed in gold and by the codex attempts — left defective.
- Sparse PR comment (just a title); methodology not evidenced and no reasoner run reported despite the issue's explicit "test results of change" instruction and the agent's own comment recommending it.
- Reasoner-driven endocardium/synovial cleanup not reproduced — unpredictable from the issue, not chargeable.
