---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3163
pr_number: 3545
issue_title: Add CD14 lacks to human dendritic cell terms
pr_author: app/copilot-swe-agent
pr_merged_at: '2026-02-05'
task_type: other
difficulty: simple
scoping: tightly_scoped
scope: multi_term
review_outcome: approved_first_time
num_agent_attempts: 0
generated_at: '2026-05-17'
domain_area: immunology
---

# PR #3545 — Add CD14 lacks to human dendritic cell terms

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3163](https://github.com/obophenotype/cell-ontology/issues/3163) | [PR #3545](https://github.com/obophenotype/cell-ontology/pull/3545) | @app/copilot-swe-agent | merged 2026-02-05

`other` `simple` `tightly_scoped` `approved_first_time`

## Context

Human myeloid and plasmacytoid dendritic cells are characteristically CD14-negative, but this phenotypic information was not captured in CL. Issue #3163 requested adding `lacks_plasma_membrane_part` annotations for CD14 (PR:000001889) to the relevant human dendritic cell terms. Negative marker annotations are important for distinguishing dendritic cells from monocytes, which are CD14-positive.

## Changes Made

Updated `cl-edit.owl` with 4 additions and 4 deletions, adding `lacks_plasma_membrane_part some PR:000001889` (CD14) axioms to the human myeloid dendritic cell and plasmacytoid dendritic cell terms. The deletions reflect replacement of existing axioms with the updated versions that include the negative marker annotation.

## Resolution

Approved on first review in 5 commits. Simple difficulty because the `lacks_plasma_membrane_part` pattern is well-established in CL for representing negative surface marker phenotypes, and the specific CD14-negative status of these dendritic cell types is well-documented immunological knowledge.
