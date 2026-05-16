---
ontology: go-ontology
issue_number: 31966
pr_number: 32003
eval_repo_pr: 189
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent obsoleted GO:0043713 "(R)-2-hydroxyisocaproate dehydrogenase activity" with a direct `replaced_by: GO:0140175`, exactly reproducing the human gold PR (#32003) — same blob (`55fadaf` == gold `55fadafbd`), F1 = 1.0. Note the gold PR was itself authored by dragon-ai-agent (claude-opus-4-7), so a perfect line match here means the agent independently arrived at the identical, fully correct solution including the verbose obsoletion comment. The metadiff score accurately represents the quality: this is a textbook category-1 obsoletion.

## Strengths

- Correct ontological action: `is_obsolete: true`, name prefixed `obsolete`, def prefixed `OBSOLETE.`, original provenance `[GOC:jl, PMID:16957230]` retained, `is_a: GO:0016616` logical axiom removed, `replaced_by: GO:0140175` added, `term_tracker_item` pointing to issue #31966 — all conforming to the term-obsoletion skill convention.
- Correct replacement target: GO:0140175 carries `xref: EC:1.1.1.345 {source="skos:exactMatch"}` and `xref: RHEA:10052 {source="skos:narrowMatch"}`; the agent's comment correctly reconstructs the EC-synonym / RHEA-narrowMatch / CHEBI:55534-55535 conjugate-base chain from the issue.
- Obsoletion comment is detailed and biochemically precise, citing EC:1.1.1.345 and RHEA:10052 — matching the gold comment essentially verbatim.
- Sound methodology: ran `make travis_build` before and after edits (both passed), used the checkout/checkin workflow, inspected both GO:0043713 and GO:0140175, reviewed `/term-obsoletion`, `/reaction`, `/chemical-entity` skills, and honestly disclosed that `runoak` annotation checks could not run due to a local oaklib/linkml import error (relied on the issue's stated 0-annotations).
- Tightly scoped: only `src/ontology/go-edit.obo` touched, only the target stanza changed.

## Issues

- None. This is a complete, correct, well-validated obsoletion identical to the merged human resolution. The only environmental limitation (no live OAK annotation re-check) was correctly mitigated by the issue's explicit 0-annotation statement and was disclosed transparently.
