# Tutorials

Tutorials are **learning-oriented** guides that walk you through complete workflows step-by-step. They're designed to help you learn SCRIBE by doing real tasks.

## Learning Paths

### Path 1: Case Study Curation

If you want to curate case studies from GitHub repositories for agent evaluation:

| Tutorial | Time | Description |
|----------|------|-------------|
| [Installation](installation.md) | 5 min | Install SCRIBE and its dependencies |

### Path 2: Agent Evaluation

If you want to evaluate AI coding agents at scale using shadow repositories:

| Tutorial | Time | Description |
|----------|------|-------------|
| [Installation](installation.md) | 5 min | Install SCRIBE and its dependencies |
| [Shadow repo evaluation](shadow-repo-eval.md) | 20 min | Set up and run agent evaluations using case study folders |

## What you'll learn

**Case Study Curation Path:**

- Install SCRIBE with all dependencies
- Use the `/find-training-cases` skill to discover candidate PRs
- Validate case study files against the LinkML schema
- Organize case studies by repository and domain

**Agent Evaluation Path:**

- Create shadow repositories for evaluation
- Configure agent instructions (CLAUDE.md)
- Point workflow config at a case study folder via `input_sets_dir`
- Run evaluations via GitHub Actions workflows
- Compare agent solutions against human ground truth using metadiff
- Iterate on agent configurations

## Prerequisites

- Python 3.11 or higher
- Basic familiarity with command-line tools
- A GitHub account with `gh` CLI authenticated
- For agent evaluation: Access to create repositories in your GitHub organization
