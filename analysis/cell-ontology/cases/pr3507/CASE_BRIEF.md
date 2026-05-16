---
ontology: cell-ontology
repo: obophenotype/cell-ontology
issue_number: 3506
pr_number: 3507
issue_title: hypertrophic chondrocyte - link to Uberon and improve definition
pr_author: app/copilot-swe-agent
pr_merged_at: '2025-12-12'
task_type: other
difficulty: medium
scoping: mostly_scoped
scope: single_term
review_outcome: approved_first_time
num_agent_attempts: 0
generated_at: '2026-05-15'
domain_area: skeletal
---

# PR #3507 — hypertrophic chondrocyte - link to Uberon and improve definition

**cell-ontology** | [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology) | [Issue #3506](https://github.com/obophenotype/cell-ontology/issues/3506) | [PR #3507](https://github.com/obophenotype/cell-ontology/pull/3507) | @app/copilot-swe-agent | merged 2025-12-12

`other` `medium` `mostly_scoped` `approved_first_time`

## Context

The existing definition of hypertrophic chondrocyte (CL:0000743) described it as "terminally differentiated," which is now known to be inaccurate -- hypertrophic chondrocytes can transdifferentiate into osteoblasts and osteocytes. Issue #3506 requested removing this claim, improving the textual definition, and adding links to relevant UBERON anatomical structures and GO biological processes.

## Changes Made

Updated `cl-edit.owl` with a revised textual definition for CL:0000743 that removes the "terminally differentiated" language, adds part_of links to UBERON growth plate structures, and adds capable_of links to relevant GO processes like chondrocyte hypertrophy. Component files were also updated with version bumps. The change touched 13 files total, though most were minor version updates in component OWL files.

## Resolution

Approved on first review after 10 commits of refinement. Medium difficulty because the change required understanding current research on chondrocyte transdifferentiation and selecting the appropriate UBERON and GO terms to cross-reference, while ensuring the updated definition accurately reflects the cell's biology without overclaiming.
