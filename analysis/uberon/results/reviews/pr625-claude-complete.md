---
ontology: uberon
issue_number: 3464
pr_number: 3646
eval_repo_pr: 625
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: reclassification
difficulty: hard
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [3532, 3647]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent fully resolved issue #3464: it reparented `life cycle` (UBERON:0000104) and `life cycle stage` (UBERON:0000105) from `is_a: UBERON:0000000 ! processual entity` to `is_a: BFO:0000015 ! process` (the COB-compatibility ask in the issue body), and additionally obsoleted the four vestigial temporal-boundary terms (UBERON:0035943, UBERON:0035944, UBERON:0035945, UBERON:0035946) — the exact cleanup cmungall and gouttegd called for in the comment thread ("useless vestiges of the heady days of over-formalization", and confirmed unused anywhere in Uberon). F1=0.000 is a pure artifact of the partial gold: selected gold #3646 only adds two `has_ontology_root_term` header lines (an explicit intermediate step), while the substantive work is in companion human PR #3647. Judged against the issue and the union #3532+#3646+#3647, this is the **most complete of the five GPT attempts**: its two reparenting hunks are byte-identical to the corresponding hunks in human PR #3647, and it is the only attempt that also addresses the temporal-boundary branch the thread agreed should go.

## Strengths

- Both core reparenting hunks (`-is_a: UBERON:0000000 ! processual entity` / `+is_a: BFO:0000015 ! process` for UBERON:0000104 and UBERON:0000105) are identical to the corresponding hunks in human PR #3647 — the agent independently arrived at the maintainer's chosen mechanism.
- Uniquely among the GPT attempts, it acts on the issue's *discussion*, not just its title: obsoletes UBERON:0035943/0035944/0035945/0035946 with clean hygiene (`is_obsolete: true`, `name: obsolete ...`, explanatory `comment:` citing #3464, stripped logical axioms/`intersection_of`/relationships). The thread participants (cmungall, gouttegd) explicitly endorsed eliminating these unused 0D-boundary vestiges.
- Removing the `intersection_of`/`relationship` axioms and `present_in_taxon` GCIs on the obsoleted terms is correct obsoletion practice — it prevents dangling logical definitions referencing a dead class.
- PR comment documents a defensible methodology: confirmed stanzas with `obo-grep.pl`, verified the temporal-boundary branch was self-contained, used `obo-checkin.pl`, and reserialized with `robot convert`.
- Scope rationale is explicit and ontologically sound: rather than inventing a new upper-level home for the temporal-boundary terms (COB#40 is still unresolved), it obsoletes the unused branch — a cleaner outcome than the human's #3647, which merely reparented UBERON:0035943 to `BFO:0000001 ! entity`.

## Issues

- Does not deprecate/rename UBERON:0000000 ("processual entity") itself, which human PR #3647 obsoletes. After this change UBERON:0000000 still exists as a live class. The issue framed UBERON:0000000's fate as a COB-parked question and gold #3646 likewise did not touch it, so this is an acceptable scoping boundary rather than an error, but it is incomplete relative to the full human cleanup.
- The agent obsoletes the temporal-boundary terms whereas human #3647 retained UBERON:0035943 (reparented to `BFO:0000001 ! entity`). This is a defensible divergence well-grounded in the issue thread, not an error, but it is a different decision from the maintainer's; ideally it would have been flagged for curator confirmation given the breadth of the structural change.
- No reasoner/consistency-check output shown for an upper-level structural change plus a multi-term obsoletion; methodology is described but QC is not demonstrated. Minor.
