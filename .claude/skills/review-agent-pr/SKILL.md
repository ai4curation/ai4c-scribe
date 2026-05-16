---
name: review-agent-pr
description: Review a shadow PR created by an AI agent against the human gold standard
---

# Review Guidelines: Agent Evaluation Runs

You are reviewing the PR that was created in response to GitHub issue
on a biomedical ontology. Your job is to assess the quality of the
agent's work by comparing it to a gold-standard solution. However,
note that in some cases the gold standard may have imperfections, and
the proposed PR may actually improve on it.

## Case briefs

This repo works by making "attempt" PRs in a shadow repo that
are blinded replications of "source" PRs in the original repo.

Let's take GO as an example. You should work from the case brief that is already prepared for you; for example:

* analysis/go-ontology/cases/pr31676/CASE_BRIEF.md

This describes the source PR (31676 in the source repo), an overview, how the human
handled it, and how all the agents handled it.

the front matter might have:

```yaml
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31670
pr_number: 31676
issue_title: 'Taxon constraint: please add for GO:0070478 and similar terms'
pr_author: pgaudet
pr_merged_at: '2026-04-20'
task_type: new_term
difficulty: hard
scoping: mostly_scoped
scope: multi_term
review_outcome: multiple_rounds
num_agent_attempts: 10
generated_at: '2026-05-15'
scoping_notes: Primary goal was adding taxon constraints for specific terms. Also
  fixed a formatting error in the migrasome entry (extra NCBITaxon column) which was
  incidental cleanup.
domain_area: biological_process
best_f1: 0.571
best_model: kimi-k2.6
```

You are encouraged to read the full source issue and the original PR in the source repo, as
well as the summary in the brief.

Note you are also free to suggest changes to some parts of the metadata (task_type, difficuly, scope, ...)

Your job is to evaluate the agent attempts. Each attempt has a metadata section at the start:

E.g. ` grep -A5 '^### Attempt' analysis/go-ontology/cases/pr31676/CASE_BRIEF.md`"


```markdown
### Attempt 1: kimi-k2.6 / opencode

- **Eval PR**: [#263](https://github.com/ai4curation/eval-ont-agent-go/pull/263)
- **F1**: 0.571  **Precision**: 0.400  **Recall**: 1.000  **Jaccard**: 0.400
- **Trace**: [25646686906](https://github.com/ai4curation/eval-ont-agent-go/tree/master/traces/25646686906)
- **Workflow run**: [25646686906](https://github.com/ai4curation/eval-ont-agent-go/actions/runs/25646686906)
```

The review for this attempt would go in `analysis/go-ontology/results/reviews/pr263-{YOU}-complete.md

Where YOU is whatever agent type you are (codex, claude)

## Step 1: Understand the task

Read the source issue to understand what the agent was asked to do:

```bash
gh issue view {issue_number} --repo {source_repo} --json title,body,comments
```

Where `source_repo` comes from the ontology:

| ontology | source_repo |
|----------|-------------|
| go-ontology | geneontology/go-ontology |
| cell-ontology | obophenotype/cell-ontology |
| uberon | obophenotype/uberon |
| mondo | monarch-initiative/mondo |

Read the full issue body and comments. The issue may contain discussion,
clarifications, or constraints that affect what a correct solution looks like.
Some issues are straightforward ("obsolete term X"), others require judgment
("reparent these 49 terms").

## Step 2: Understand the agent's instructions

The agent was given a prompt (see `__agent_prompt__.md` in the eval workflow)
plus agent-specific configuration from a config repo. The config repo contains:

- `CLAUDE.md` / `AGENTS.md` — project-level instructions
- `.agents/skills/` — domain-specific skill files (e.g., term-obsoletion,
  research, design-pattern)

The config repos are:

| ontology | config_repo |
|----------|-------------|
| go-ontology | ai4curation/go-ontology-agent-config |
| cell-ontology | ai4curation/cl-agent-config |
| uberon | ai4curation/uberon-agent-config |
| mondo | ai4curation/mondo-agent-config |

You can browse the config to understand what the agent was told to do:

```bash
gh api repos/{config_repo}/contents/template/CLAUDE.md --jq '.content' | base64 -d
gh api repos/{config_repo}/contents/template/.agents/skills --jq '.[].name'
```

This matters because an agent that ignores its instructions is a different
failure mode from one that follows them but gets the wrong answer.

## Step 3: Read the human PR (ground truth)

```bash
gh pr view {pr_number} --repo {source_repo}
gh pr diff {pr_number} --repo {source_repo}
```

Note what the human changed, how they changed it, and any reviewer feedback.
The human solution is the reference but not necessarily perfect — sometimes
the agent's approach is equally valid or even better.

### Step 3a: Check whether the gold PR is the *whole* human resolution

A single issue is often resolved by the human across **multiple PRs** (e.g.,
a taxon-constraint cleanup in one PR, the actual obsoletion in another). The
case brief and metadiff score compare the agent against **only one** of those
PRs — the one selected as `pr_number`. If that PR is just a sub-step, the
metadiff F1 will be near zero for *every* attempt even when agents fully and
correctly resolve the issue.

Always sanity-check this:

```bash
gh search prs --repo {source_repo} "{issue_number}" --json number,title,state,url --limit 20
gh search prs --repo {source_repo} "{key term from issue title}" --json number,title,url --limit 10
```

If the issue was resolved by several PRs, reconstruct the **union** of the
human changes and judge the agent against that union and against the issue's
explicit asks — not against the single selected gold PR. When this happens,
the case is a **poor evaluation case** and must be flagged (see Step 7a).

## Step 4: Read the agent's PR

```bash
gh pr diff {eval_repo_pr} --repo ai4curation/{eval_repo}
```

Where `eval_repo` maps from the ontology name:

| ontology | eval_repo |
|----------|-----------|
| go-ontology | eval-ont-agent-go |
| cell-ontology | eval-ont-agent-cl |
| uberon | eval-ont-agent-uberon |
| mondo | eval-ont-agent-mondo |

If traces are available, check them for insight into the agent's reasoning:

```bash
gh api repos/ai4curation/{eval_repo}/contents/traces --jq '.[].name' | head -20
```

## 4b: gain further context

To gain further context or to help adjudicate, you should explore both
documentation and existing terms on the source repo. Don't guess about
best practice.

## Step 5: Compare and assess

Consider these dimensions:

### Correctness
Did the agent make the right changes? Are the ontological edits valid?
Compare the substance of the diff, not just the line-by-line match.

### Completeness
Did the agent address all parts of the issue? Missing steps (e.g., forgot to
update cross-references, didn't add a replaced_by) count against completeness.

### Scope discipline
Did the agent stick to what was asked, or did it make additional changes?
Extra changes aren't necessarily wrong — fixing a pre-existing bug while
you're in the neighborhood is often good practice. But gratuitous edits that
don't serve the issue reduce precision and risk introducing errors.

Evaluate whether extra edits were:
- **Justified**: fixing a genuine problem discovered during the work
- **Defensible**: reasonable but not strictly necessary
- **Over-editing**: changes unrelated to the issue

### Methodology
Did the agent follow a reasonable process? Evidence of research, term search,
validation, and design pattern consultation indicates good methodology even if
the final result isn't perfect. Look at PR_COMMENTS.md and ISSUE_COMMENTS.md
if present in the agent's PR.

### Metadiff score interpretation
The F1/precision/recall scores compare the agent's diff to the human's
line-by-line (after normalization). These are useful but imperfect:

- **F1 < 1.0 with high precision**: agent did less than the human (missed some changes)
- **F1 < 1.0 with high recall**: agent did more than the human (extra changes)
- **F1 = 0**: agent either made no changes or completely different changes
- **F1 = 1.0**: agent's diff matches the human's exactly (after normalization)

A score of 0.8 with precision=0.889 and recall=0.727 means the agent made
mostly the same changes as the human but included some extras (lowering recall
from the human's perspective). This can still be a good outcome.

## Step 6: Write the review

Fill in the three sections in the stub file:

### Summary
Two to three sentences: what the agent did, whether it succeeded, and the
headline finding. Mention the metadiff score and whether it over- or
under-represents the actual quality.

### Strengths
Bullet points. What the agent got right. Be specific — cite term IDs,
patterns followed, skills used.

### Issues
Bullet points. What went wrong or could be better. Distinguish between:
- Errors (wrong edits, broken syntax)
- Omissions (missed part of the issue)
- Scope issues (extra edits beyond the issue)
- Style (valid but different from the human's approach)

If there are no issues, say so.

## Step 7: Fill in frontmatter fields

Update these fields in the YAML frontmatter:

- **outcome**: One of `success`, `partial_success`, `failure`, `no_output`
  - `success`: agent addressed the issue correctly with no significant problems
  - `partial_success`: core task done but with notable issues (scope, omissions)
  - `failure`: agent did not solve the issue or made significant errors
  - `no_output`: agent produced no changes (empty diff)
- **failure_modes**: List from: `over_editing`, `under_editing`, `wrong_term`,
  `syntax_error`, `missed_requirement`, `wrong_pattern`, `scope_creep`,
  `no_changes`, `instruction_violation`
- **reviewed_by**: Your model identifier (e.g., `gpt-5.5`, `claude-opus-4.7`)
- **reviewed_at**: Today's date in YYYY-MM-DD format

## Step 7a: Flag poor evaluation cases (curated metadata only)

If you determined in Step 3a that the gold PR is only a sub-step of a
multi-PR human resolution (or the case is otherwise a poor reference — e.g.
the gold PR is wrong, or the issue was substantively renegotiated in
comments), record this in the case's **`METADATA.md`**, NOT the
`CASE_BRIEF.md`.

- `CASE_BRIEF.md` is **auto-generated and derived** — never edit it; any
  change will be overwritten on regeneration.
- `METADATA.md` (same directory) is **hand-curated** and is the correct place
  for durable curator findings.

In `METADATA.md`, add to the frontmatter:

```yaml
case_quality: poor          # poor | ok | good
case_quality_reason: gold_pr_is_partial   # short slug
companion_prs: [32023, 32069]   # other human PRs that resolved the issue
scoring_caveat: "metadiff vs #32021 only covers the taxon-constraint sub-step; judge attempts against the issue and the union of #32021+#32023+#32069"
```

and add a `## Curation Note (data quality)` section to the body explaining
the finding so downstream scoring/aggregation can exclude or down-weight the
case. Then review the attempts **in light of the issue's actual instructions**
rather than the misleading metadiff.

## Step 8: Rename the file

Rename the file from `-stub.md` to `-complete.md` to mark it as reviewed.

## Notes

- Be honest. A high metadiff score with real problems is still a problem.
  A low score with defensible extra work deserves credit.
- Don't fill in rubric scores (instruction_following, correctness, etc.)
  unless specifically asked. The narrative review is more valuable.
- If the issue is ambiguous and the agent made a reasonable interpretation,
  note this. Ambiguous issues are harder and agents deserve credit for
  reasonable judgment calls.
- If you cannot access the issue or PR (404, permissions), note this in the
  review rather than guessing.
- `CASE_BRIEF.md` is derived/auto-generated — **never edit it**. Durable
  curator findings (poor-case flags, metadata corrections) go in the
  hand-curated `METADATA.md` in the same case directory.
- A case where every attempt scores ~0 F1 is a strong signal to apply
  Step 3a before concluding the agents failed — the gold PR may be partial.
