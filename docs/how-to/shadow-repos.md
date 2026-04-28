# Set up shadow repos

This guide shows how to create and configure shadow repositories for running agent evaluations at scale.

## Overview

Shadow repositories are copies of the original repository where you run agent evaluations. This keeps experiment branches separate from the production repository.

## Import a repository

### Via GitHub UI

1. Go to [github.com/new/import](https://github.com/new/import)
2. Enter the source repository URL
3. Choose your organization as owner
4. Name it with an `-eval` suffix (e.g., `mondo-eval`)
5. Click "Begin import"

### Via GitHub CLI

```bash
# Note: GitHub CLI doesn't directly support import
# Use the web UI or clone + push approach below
```

### Via clone + push

```bash
# Clone the original
git clone --bare https://github.com/original-org/repo.git

# Create new repo in your org
gh repo create your-org/repo-eval --private

# Push to your new repo
cd repo.git
git push --mirror https://github.com/your-org/repo-eval.git
cd ..
rm -rf repo.git
```

!!! warning "Import vs fork"
    Use **import** rather than fork. Forks maintain a relationship with the upstream
    repository that can cause issues with workflow permissions. Imports create a
    standalone copy.

## Add the evaluation workflow

```bash
# Clone your shadow repo
git clone https://github.com/your-org/repo-eval.git
cd repo-eval

# Create workflows directory
mkdir -p .github/workflows

# Download the workflow
curl -o .github/workflows/eval-agent-on-issue.yml \
  https://raw.githubusercontent.com/ai4curation/ai4c-scribe/main/workflows/eval-agent-on-issue.yml

# Commit and push
git add .github/workflows/
git commit -m "Add SCRIBE evaluation workflow"
git push
```

## Configure secrets

Navigate to Settings → Secrets and variables → Actions in your shadow repo.

### Required secrets

| Secret | Description |
|--------|-------------|
| `ANTHROPIC_API_KEY` | Anthropic API key for Claude |
| `CLAUDE_CODE_OAUTH_TOKEN` | Alternative: OAuth token |

At least one authentication secret is required.

### Optional secrets

| Secret | When needed |
|--------|-------------|
| `GH_PAT` | Accessing private repos across organizations |

### Creating a Personal Access Token (PAT)

If you need `GH_PAT`:

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Create a fine-grained token with:
   - **Contents**: Read and write
   - **Pull requests**: Read and write
   - **Metadata**: Read
3. Select the repositories it needs access to
4. Add to your shadow repo's secrets

## Protect eval-base branches

Evaluation workflows create `eval-base-issue-NNN` branches that serve as baselines. Protect them from accidental modification:

1. Go to Settings → Branches
2. Add rule with pattern: `eval-base-*`
3. Enable:
   - Require pull request before merging
   - Require 1 approval
   - Disable force pushes
   - Disable deletions

## Sync with upstream

If the original repository receives updates you want:

```bash
cd repo-eval

# Add upstream remote (one time)
git remote add upstream https://github.com/original-org/repo.git

# Fetch and merge updates
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

!!! note "Selective syncing"
    For evaluation purposes, you often don't need to sync. The workflow checks out
    at historical commits, so new upstream changes don't affect past evaluations.

## Run evaluations

### Single evaluation

```bash
gh workflow run eval-agent-on-issue \
  --repo your-org/repo-eval \
  --field issue_repo=original-org/repo \
  --field issue_number=123 \
  --field pr_number=456 \
  --field agent_config_repo=your-org/agent-config \
  --field agent_config_tag=v1.0.0 \
  --field model=claude-sonnet-4-5-20250929 \
  --field create_pr=true
```

### Batch evaluations

Script multiple evaluations:

```bash
#!/bin/bash
# eval-batch.sh

ISSUES="7712:8116 7800:8200 7900:8300"  # issue:pr pairs
SHADOW_REPO="your-org/repo-eval"
ISSUE_REPO="original-org/repo"
CONFIG_REPO="your-org/agent-config"
CONFIG_TAG="v1.0.0"
MODEL="claude-sonnet-4-5-20250929"

for pair in $ISSUES; do
  ISSUE=${pair%:*}
  PR=${pair#*:}

  echo "Running evaluation: issue #$ISSUE, PR #$PR"
  gh workflow run eval-agent-on-issue \
    --repo $SHADOW_REPO \
    --field issue_repo=$ISSUE_REPO \
    --field issue_number=$ISSUE \
    --field pr_number=$PR \
    --field agent_config_repo=$CONFIG_REPO \
    --field agent_config_tag=$CONFIG_TAG \
    --field model=$MODEL \
    --field create_pr=true

  # Rate limit: wait between runs
  sleep 5
done
```

## Monitor evaluations

```bash
# List recent runs
gh run list --repo your-org/repo-eval --workflow=eval-agent-on-issue.yml

# Watch a specific run
gh run watch <run-id> --repo your-org/repo-eval

# Download artifacts
gh run download <run-id> --repo your-org/repo-eval
```

## Cleanup

### Delete experiment branches

```bash
# List experiment branches
git branch -r | grep 'scribe-v1'

# Delete a specific branch
git push origin --delete scribe-v1-...-issue-123

# Delete all experiment branches (careful!)
git branch -r | grep 'origin/scribe-v1' | sed 's/origin\///' | xargs -I {} git push origin --delete {}
```

### Close evaluation PRs

```bash
# List open evaluation PRs
gh pr list --repo your-org/repo-eval --state open --search "DO NOT MERGE"

# Close all evaluation PRs
gh pr list --repo your-org/repo-eval --state open --search "DO NOT MERGE" \
  --json number -q '.[].number' | xargs -I {} gh pr close {} --repo your-org/repo-eval
```

## Troubleshooting

### "Branch already exists"

Set `force_new_branch=true` to overwrite:

```bash
--field force_new_branch=true
```

### "Permission denied" on cross-org access

Add `GH_PAT` secret with appropriate permissions.

### Workflow not appearing

Ensure the workflow file is committed to the default branch (`main` or `master`).

## Related

- [Tutorial: Shadow repo evaluation](../tutorials/shadow-repo-eval.md)
- [Explanation: Shadow repos](../explanation/shadow-repos.md)
- [Reference: GitHub workflows](../reference/github-workflows.md)
