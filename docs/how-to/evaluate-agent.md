# Evaluate an Agent

Use ai4c-scribe as a test harness to evaluate AI coding agents against real-world issues with known solutions.

## Overview

The agent evaluation workflow:

1. Find issues in a repository that have associated merged PRs
2. Reset a worktree to the commit state *before* the PR was created
3. Run your agent to attempt the fix
4. Compare the agent's solution against the actual merged PR

This provides reproducible evaluation with ground-truth solutions from real developers.

## Prerequisites

- A git worktree or clone of the repository to evaluate against
- A runner configuration file (`.ai4cscribe/runner.yaml`)
- The `cyberian` AI agent framework (optional, for automated agent execution)

## Basic usage

### 1. Set up the worktree

Clone the target repository:

```bash
git clone https://github.com/owner/repo.git repo-worktree
```

!!! tip "Using git worktrees for large repos"
    If you already have a checkout of a large repository, you can create a lightweight
    [git worktree](https://git-scm.com/docs/git-worktree) instead of a full clone:

    ```bash
    cd existing-repo
    git worktree add ../repo-worktree main
    ```

### 2. Create the runner configuration

Create `.ai4cscribe/runner.yaml` in the worktree:

```yaml
experiment_id: exp001
system_prompt: |
  You are an expert developer. Analyze the issue carefully and
  implement a clean solution following existing code patterns.
agent_timeout: 600
```

### 3. Run the agent on an issue

```bash
ai4c-scribe fix-issue owner/repo 1234 -w /path/to/repo-worktree
```

You'll be prompted to confirm the `git reset --hard` operation. Use `--force` to skip:

```bash
ai4c-scribe fix-issue owner/repo 1234 -w /path/to/repo-worktree --force
```

This will:

1. Fetch the issue context (title, body, all comments)
2. Find the linked PR (if any) to determine ground truth
3. Reset the worktree to the commit *before* the PR was created
4. Create a branch `exp001-issue-1234`
5. Launch an AI agent via [cyberian](https://github.com/ai4curation/cyberian) with the worktree as its working directory
6. The agent receives a task combining your `system_prompt` with the full issue context (title, body, comments, labels)
7. The agent analyzes the issue, makes code changes, and commits them to the branch

### 4. Compare results

After the agent commits its solution, compare it to the actual PR:

```bash
# View the agent's commits
cd repo-worktree
git log --oneline exp001-issue-1234

# Compare to the actual PR's changes
git diff exp001-issue-1234..origin/pr-branch
```

## Dry run mode

Use `--dry-run` to set up the worktree without running the agent (skips confirmation):

```bash
ai4c-scribe fix-issue owner/repo 1234 -w /path/to/worktree --dry-run
```

This is useful for:

- Testing your configuration
- Manually running a different agent
- Debugging worktree setup

## Configuration options

### Runner configuration file

| Field | Description | Default |
|-------|-------------|---------|
| `experiment_id` | Branch name prefix (required) | - |
| `system_prompt` | Inline system prompt text | Generic prompt |
| `system_prompt_file` | Path to system prompt file | - |
| `overlay_dir` | Directory to copy into worktree | - |
| `copier_template` | Copier template URL/path | - |
| `agent_timeout` | Agent task timeout in seconds | 600 |

### CLI options

```bash
ai4c-scribe fix-issue REPO ISSUE -w WORK_DIR [OPTIONS]

Arguments:
  REPO       Repository in owner/name format
  ISSUE      Issue number to fix

Options:
  -w, --work-dir PATH     Path to git worktree (required)
  -c, --config PATH       Path to config file
  -s, --system-prompt     Override system prompt text
  -f, --prompt-file PATH  Override system prompt file
  -o, --overlay PATH      Override overlay directory
  --dry-run               Set up worktree but don't run agent
  --force, -y             Skip confirmation prompt
```

## Finding good test issues

To find issues suitable for evaluation, extract PRs with 1-to-1 issue mapping:

```bash
# Extract PRs that fix exactly one issue
ai4c-scribe extract owner/repo -o prs.jsonl --one-to-one-only -l 100

# These PRs have clear ground-truth mappings
```

Issues that work well:

- Have a single linked PR (1-to-1 mapping)
- Are self-contained (don't require external context)
- Have clear descriptions of what needs to be done
- Were successfully merged (proven solutions)

## Using overlays

Overlays let you inject additional files into the worktree before the agent runs:

```yaml
experiment_id: exp001
overlay_dir: overlays/my-repo
```

Use cases:

- Add a `.claude/CLAUDE.md` with repository-specific instructions
- Include configuration files for the agent
- Add test fixtures or reference data

## Batch evaluation (coming soon)

Future versions will support:

- Running multiple issues in sequence
- Automated comparison against ground-truth PRs
- Aggregate metrics across evaluations
- Integration with evaluation frameworks
