# Tutorials

Tutorials are **learning-oriented** guides that walk you through complete workflows step-by-step. They're designed to help you learn SCRIBE by doing real tasks.

## Learning Paths

### Path 1: Training Data Extraction

If you want to mine PRs from GitHub repositories for training or evaluation data:

| Tutorial | Time | Description |
|----------|------|-------------|
| [Installation](installation.md) | 5 min | Install SCRIBE and its dependencies |
| [Your first extraction](first-extraction.md) | 10 min | Extract PRs from a repository |
| [Complete workflow](full-workflow.md) | 15 min | Full pipeline: extract, create review cases, distill |

### Path 2: Agent Evaluation

If you want to evaluate AI coding agents at scale using shadow repositories:

| Tutorial | Time | Description |
|----------|------|-------------|
| [Installation](installation.md) | 5 min | Install SCRIBE and its dependencies |
| [Shadow repo evaluation](shadow-repo-eval.md) | 20 min | Set up and run agent evaluations |

## What you'll learn

**Training Data Path:**

- Install SCRIBE with all dependencies
- Extract PR data from any GitHub repository
- Create review cases capturing the "first revision" state
- Generate AI-refined vignettes with quality ratings
- Manage the local cache for efficient extraction

**Agent Evaluation Path:**

- Create shadow repositories for evaluation
- Configure agent instructions (CLAUDE.md)
- Run evaluations via GitHub Actions workflows
- Compare agent solutions against human ground truth
- Iterate on agent configurations

## Prerequisites

- Python 3.11 or higher
- Basic familiarity with command-line tools
- A GitHub account with `gh` CLI authenticated
- For agent evaluation: Access to create repositories in your GitHub organization
