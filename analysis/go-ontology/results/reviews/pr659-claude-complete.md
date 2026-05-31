---
ontology: go-ontology
issue_number: 31966
pr_number: 32003
eval_repo_pr: 659
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.889
precision: 0.889
recall: 0.889
jaccard: 0.8
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent correctly obsoleted GO:0043713 "(R)-2-hydroxyisocaproate dehydrogenase activity" with `replaced_by: GO:0140175` "(2R)-2-hydroxyacid dehydrogenase (NAD+) activity" (blob `7fce679`, F1 = 0.889). The diff is identical to attempt #611; the only divergence from the gold is a one-sentence obsoletion comment versus the gold's three-sentence EC/RHEA explanation. The 0.889 metadiff **under-represents** quality — the substance is fully correct and this run additionally documented strong methodology.

## Strengths

- All required obsoletion metadata is correct and matches the gold (PR #32003): `obsolete` name prefix, `OBSOLETE.` def prefix retaining `[GOC:jl, PMID:16957230]`, removal of the active `is_a: GO:0016616` axiom, `is_obsolete: true`, `replaced_by: GO:0140175`, and `property_value: term_tracker_item` for issue #31966.
- Correct biochemical replacement: GO:0140175 is right per @sjm41's analysis (EC:1.1.1.345 exactMatch of the "(R)-2-hydroxyisocaproate dehydrogenase" synonym; RHEA:10052 narrowMatch for the substrate-specific reaction) and the curator obsoletion notice.
- Strong, documented methodology (per the PR/issue comments): `runoak -i amigo: associations GO:0043713` returned no direct annotations; `obo-grep.pl -r 'GO:0043713'` confirmed no internal usages; pre/post `robot convert` syntax checks plus `make travis_build` passed; `RESEARCH.md`/`DESIGN_PATTERNS.md` produced; checkout/checkin workflow used; PMID:16957230 reference-validated.
- Tightly scoped: only the GO:0043713 stanza in `src/ontology/go-edit.obo` committed; no scope creep.

## Issues

- Style only: the obsoletion comment is the terse single-sentence form; the gold expands it with the EC:1.1.1.345 synonym chain and RHEA:10052 narrowMatch reasoning. This comment-verbosity convention difference is the sole source of the 0.889 score and is not a substantive defect.
- Minor cosmetic: the agent's issue-comment template left an unfilled `PR #<NN>` placeholder — documentation polish only, no effect on the ontology edit.
- No ontological errors, omissions, or scope problems.
