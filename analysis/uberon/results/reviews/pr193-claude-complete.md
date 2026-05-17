---
ontology: uberon
issue_number: 3475
pr_number: 3477
eval_repo_pr: 193
agent: std_copilot_sonnet45
model: claude-sonnet-4.5
runtime: copilot
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

The issue-relevant work is correct: the agent removed `is_a: UBERON:0000961` from UBERON:0002835 (ask #1) and renamed UBERON:0000961 → "thoracic paravertebral ganglion" (ask #2), satisfying both explicit asks of issue #3475. **However**, the diff is dominated by a large block of CL term-label rewrites across unrelated lung/epithelium terms (`lung ciliated cell` → `lung multiciliated epithelial cell`, `ciliated cell of the bronchus` → `multiciliated epithelial cell of the bronchus`, `glandular epithelial cell` → `glandular secretory epithelial cell`, `lung neuroendocrine cell` → `pulmonary neuroendocrine cell`) that have nothing to do with #3475. The metadiff F1 of 0.100 reflects both the poor partial gold and this self-inflicted file-regeneration contamination. Outcome `partial_success`.

## Strengths

- **Both issue asks satisfied** within the two relevant stanzas: spurious is_a on UBERON:0002835 removed; UBERON:0000961 renamed to "thoracic paravertebral ganglion"; the three ambiguous synonyms demoted to RELATED.
- Accurate neuroanatomical rationale in the (terse) PR/issue comments.

## Issues

- **ODK build-regenerated-file domination (primary):** The diff contains ~9 hunks of CL label updates on lung/bronchus/epithelium terms entirely unrelated to issue #3475. Verified against the eval base branch `eval-base-issue-3475`, which carries the *old* labels (`lung ciliated cell`, `glandular epithelial cell`) — so this is **not** base contamination; the agent itself regenerated/relabelled the file (a label-sync or `robot`/ODK reserialization pulling newer CL labels) and committed the churn. This is the dominant cause of the 0.053 recall and is a real failure mode, not a metadiff artifact.
- **Scope creep / wrong provenance form:** Added `relationship: dc-contributor https://github.com/obophenotype/uberon/issues/3475` and `property_value: dcterms-date "2026-05-13T..." xsd:dateTime` to both terms. Using `dc-contributor` to point at a GitHub *issue URL* is semantically wrong — dc-contributor is for agents/people (ORCIDs), not issue links; the correct annotation is `term_tracker_item` (as #19/#232/#56 used). The hard-coded `dcterms-date` timestamp is also undesirable churn.
- The PR/issue comments are unusually thin (one sentence each) and do not disclose the large off-topic CL relabel block — a transparency gap.
- Net: the core ontological fix is correct, but the regenerated-file domination plus malformed provenance make this a low-quality submission independent of the poor-case scoring. See METADATA.md.
