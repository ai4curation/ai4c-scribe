---
repo: geneontology/go-ontology
issue_number: 31984
pr_number: 31987
issue_title: "GO:0008805 (carbon-monoxide oxygenase activity) and GO:0043885 (anaerobic carbon-monoxide dehydrogenase activity)"
issue_created_at: "2026-04-27"
pr_author: sjm41
pr_merged_at: "2026-04-27"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 7
    deletions: 4
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Enzyme term realignment requiring deep understanding of CO dehydrogenase biochemistry and correct EC/RHEA mapping across aerobic and anaerobic variants
case_quality: good
case_quality_reason: hard_but_clean_single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Two carbon monoxide dehydrogenase terms in GO had incorrect names, definitions, and cross-references relative to their EC and RHEA entries. GO:0008805 was named "carbon-monoxide oxygenase activity" but actually corresponded to the aerobic CO dehydrogenase (using quinone as electron acceptor), while GO:0043885 (anaerobic variant) also needed alignment. The enzyme curator sjm41 identified the discrepancies during a systematic review of oxidoreductase terms.

## Changes Made

GO:0008805 was renamed from `carbon-monoxide oxygenase activity` to `aerobic carbon monoxide dehydrogenase activity`. The definition was corrected from a cytochrome-based reaction (`CO + H2O + ferrocytochrome b-561 = CO2 + 2 H+ + 2 ferricytochrome b-561`) to the quinone-based reaction (`CO + a quinone + H2O = a quinol + CO2`) matching RHEA:48880. The parent term was also changed from a cytochrome-dependent oxidoreductase class to the correct quinone-dependent class. Definition cross-references were updated accordingly.

## Resolution

Hard difficulty because the corrections required understanding the distinct biochemistry of aerobic vs. anaerobic CO dehydrogenases. Aerobic CoxMSL-type enzymes use molybdopterin cofactors with quinone electron acceptors, while anaerobic CODH uses nickel-iron centers. Misalignment between GO terms and EC/RHEA entries for these enzymes could lead to incorrect functional annotations. The curator resolved this within a single day, reflecting deep domain expertise.
