# Review Guidelines: Agent Evaluation Runs

You are reviewing the PR that was created in response to GitHub issue
on a biomedical ontology. Your job is to assess the quality of the
agent's work by comparing it to a gold-standard solution. However,
note that in some cases the gold standard may have imperfections, and
the proposed PR may actually improve on it.

## Context

Each review stub (`prNN-{reviewer}-stub.md`) has YAML frontmatter with:

- **issue_number**: The GitHub issue the agent was asked to solve
- **pr_number**: The human PR that solved it (ground truth)
- **eval_repo_pr**: The agent's PR in the evaluation repo
- **agent**: Logical agent handle (e.g., `std_codex_g55`)
- **model / runtime**: The LLM and harness used
- **f1 / precision / recall**: Metadiff scores comparing agent diff to human diff

The HTML comment block contains URLs for the source issue, human PR, and agent PR.

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
