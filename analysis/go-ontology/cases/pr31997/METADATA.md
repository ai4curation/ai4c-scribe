---
repo: geneontology/go-ontology
issue_number: 27593
pr_number: 31997
issue_title: "NTR ferric iron reductase (for non siderophore)"
issue_created_at: "2024-04-12"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-28"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 16
    deletions: 2
scoping: tightly_scoped
task_type: new_term
difficulty: hard
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Long-standing NTR (2+ years open) with a prior failed PR due to GO ID collision, requiring RHEA reaction alignment and careful parent term selection
case_quality: poor
case_quality_reason: gold_pr_curator_repudiated
companion_prs: []
scoring_caveat: "The gold PR #31997 was merged but its two central modelling decisions were repudiated by GO curators (pgaudet 2026-04-29, ValWood 2026-04-29 and 2026-05-08) within 24h: (a) the GO:0000293 is_a GO:7770068 reparenting is logically inverted (a generic-electron-donor chelate reductase cannot be a subclass of an NADPH-specific reaction; ValWood: GO:0052851 and GO:7770068 'should be siblings'), and (b) GO:7770068 is written in oxidation direction (Fe2+->Fe3+) which contradicts the 'reductase' label (cf. GO:0008823 cupric reductase precedent), with a generic label but NADPH-specific definition. Treat metadiff F1 vs #31997 as fidelity-to-issue-instruction, NOT ontological correctness: high-F1 attempts faithfully reproduced the issue's literal (flawed) ask, while the lowest-F1 attempt (#174, gpt-5.4) is the ontologically best because it refused the inverted is_a — exactly the curators' later objection. Attempt #338 (claude-opus-4.7) independently produced the generic grouping-term design (generic def, GO:0016722 parent, narrowMatch RHEA) that dragon-ai-agent's 2026-05-08 post-merge review proposed as the fix. Judge attempts against the issue + the post-merge curator consensus, not the line-level metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

A new term request for ferric iron reductase activity was filed in April 2024 to support GO-CAM modeling. The existing GO terms for iron reduction were tied to siderophore-mediated processes, but many organisms reduce ferric iron (Fe3+) to ferrous iron (Fe2+) through non-siderophore mechanisms using NADPH as the electron donor. The first attempt at this PR (#31797) was closed due to a GO ID collision where the allocated ID had already been used by a parallel branch.

## Changes Made

The PR added GO:7770068 `ferric iron reductase activity` as a new molecular function term with the reaction `2 Fe2+ + NADP+ + H+ = 2 Fe3+ + NADPH` cross-referenced to RHEA:71767 (skos:exactMatch). The term was placed under GO:0016723 (oxidoreductase activity, acting on metal ions, NAD or NADP as acceptor). The definition referenced PMID:8321236. Additionally, the existing term GO:0000293 was updated to reflect its relationship to the new term.

## Resolution

Hard difficulty due to several factors: the issue was open for over two years, a previous PR attempt failed due to ID collision (requiring careful ID allocation), and the definition needed precise alignment with the RHEA reaction database. The parent term selection required understanding the enzyme classification hierarchy for oxidoreductases acting on metal ion substrates with NAD(P) as acceptor.

## Curation Note (data quality)

**Flagged by:** claude-opus-4.7 on 2026-05-15. **Verdict:** poor evaluation case — the gold PR is curator-repudiated, not a clean reference.

The issue was resolved by a single human PR (#31997); #31797 is the earlier closed attempt (GO ID collision, `GO:7770057`), and #31975/#32033 are unrelated reaction-participant/ChEBI refreshes. There is no multi-PR fragmentation, so `companion_prs` is empty. The problem is different and more subtle: **the merged gold PR #31997 contains modelling errors that GO curators explicitly rejected within 24 hours of merge.**

What ValWood literally asked for (2026-04-01 instruction): (1) add new term with RHEA:71767 + PMID:8321236/34614242/39940646; (2) make GO:0000293 a subclass of the new term; (3) change GO:0000293 def siderophore→chelate. The gold PR (and the high-F1 agent attempts) executed all three literally.

Post-merge curator review repudiated two of these as ontologically wrong:

1. **Inverted subsumption.** pgaudet (2026-04-29): "Are you sure the parent/child relation is correct: 'ferric-chelate reductase activity' [generic donor] ... is not a type of 'ferric iron reductase activity' [NADPH-specific]". ValWood (2026-04-29) confirmed `GO:0052851` and `GO:7770068` "should be siblings". A generic-electron-donor reaction cannot be a subclass of an NADPH-specific reaction.
2. **Reaction direction + label/def mismatch.** ValWood (2026-05-08) flagged "problems with term placement, definitions and reaction direction". The dragon-ai-agent's own 2026-05-08 review (model claude-opus-4.7) confirmed: `GO:7770068` is written in oxidation direction (Fe2+→Fe3+), contradicting the "reductase" name (cf. `GO:0008823` cupric reductase, correctly in reduction direction); and the generic label does not match the NADPH-specific definition. The proposed fix was to repurpose `GO:7770068` as a generic grouping term (def `2 Fe3+ + electron donor = 2 Fe2+ + electron acceptor`, parent `GO:0016722`, drop the RHEA exactMatch) with a separate NADPH-specific child.

**Scoring implication (the inversion):** metadiff F1 vs #31997 measures fidelity to the issue's literal (flawed) instruction, not ontological correctness. The ranking is partly **inverted** relative to true quality:

- Attempt #73 (gpt-5.5/codex, F1 1.000) — perfect reproduction of the gold *including its errors*.
- Attempt #174 (gpt-5.4/codex, F1 0.593, lowest) — **best ontological judgement**: deliberately refused the inverted `GO:0000293 is_a GO:7770068` axiom with reasoning that verbatim anticipates pgaudet/ValWood's objection, and explicitly proposed a separate grouping term.
- Attempt #338 (claude-opus-4.7/claude, F1 0.667) — independently produced the generic grouping-term design (generic def, `GO:0016722` parent, `skos:narrowMatch` RHEA, reduction direction) that the post-merge curator review settled on as the fix.

Downstream aggregation should down-weight or exclude this case from metadiff-based scoring, or rescore against the post-merge curator consensus. The narrative reviews in `analysis/go-ontology/results/reviews/pr{73,269,386,110,91,338,472,195,174}-claude-complete.md` grade on substance and note per-attempt whether F1 over- or under-represents quality.
