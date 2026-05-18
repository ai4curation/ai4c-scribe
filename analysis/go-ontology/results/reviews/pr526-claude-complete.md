---
ontology: go-ontology
issue_number: 31984
pr_number: 31987
eval_repo_pr: 526
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: hard
f1: 0.778
precision: 0.7
recall: 0.875
jaccard: 0.636
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31984
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31987
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/526
  Agent config: ai4curation/go-ontology-agent-config@v9
-->

## Summary

The agent correctly executed all four explicit tasks listed in issue #31984: it renamed GO:0008805 to `aerobic carbon monoxide dehydrogenase activity` (matching the gold spelling exactly, no spurious hyphen), corrected its definition to the quinone/quinol reaction, reparented it from GO:0016622 to the quinone-acceptor class GO:0052738, and updated the GO:0043885 anaerobic definition to the `[2Fe-2S]-[ferredoxin]` stoichiometry. The metadiff F1=0.778 slightly under-represents quality on the issue's literal asks (all four done correctly); the deduction is entirely from gold-only provenance/searchability extras the issue never requested.

## Strengths

- GO:0008805 renamed to `aerobic carbon monoxide dehydrogenase activity` — byte-identical to the gold name (no hyphen variant), matching the EC name and the GO:0043885 format requested in the issue.
- GO:0008805 definition corrected to `Catalysis of the reaction: CO + a quinone + H2O = a quinol + CO2.`, the RHEA:48880 / EC:1.2.5.3 reaction.
- GO:0008805 reparented from GO:0016622 (cytochrome acceptor) to GO:0052738 (quinone or similar compound as acceptor) — biochemically correct for the CoxMSL-type aerobic enzyme and exactly the parent the issue specified.
- GO:0043885 definition refined to `CO + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O = 2 reduced [2Fe-2S]-[ferredoxin] + CO2 + 2 H+.` matching RHEA:21040.
- Tightly scoped: only the two target terms touched, no over-editing.

## Issues

- Omission: did not add `synonym: "carbon-monoxide oxygenase activity" BROAD []` to preserve the old label for searchability after the rename. The issue did not request this, but it is standard GO practice on a rename and the gold PR did it.
- Omission: did not add the `term_tracker_item` provenance pointing to issue #31984 on either GO:0008805 or GO:0043885 (gold added it to both). This is the bulk of the recall gap.
- Minor provenance mismatch: the GO:0008805 definition xref list was kept as `[GOC:curators, RHEA:48880]`, whereas the gold trimmed it to `[RHEA:48880]` since the corrected reaction is sourced directly from RHEA. Not a biochemical error.
- Net: a biologically correct, complete resolution of the explicit issue tasks, but an incomplete reproduction of the GO curation pattern (missing synonym + tracker provenance), hence partial_success.
