# Installation

This tutorial walks you through installing SCRIBE and its dependencies.

## Prerequisites

Before you begin, ensure you have:

- **Python 3.11+**: Check with `python --version`

## Step 1: Install GitHub CLI

SCRIBE uses the [GitHub CLI](https://cli.github.com/) for API access. This provides automatic authentication and handles rate limiting gracefully.

=== "macOS"

    ```bash
    brew install gh
    ```

=== "Linux (Debian/Ubuntu)"

    ```bash
    # Add GitHub's repository
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
    sudo apt update
    sudo apt install gh
    ```

=== "Windows"

    ```powershell
    winget install --id GitHub.cli
    ```

## Step 2: Authenticate with GitHub

Authenticate the GitHub CLI to access the GitHub API:

```bash
gh auth login
```

Follow the interactive prompts. When asked:

- **What account do you want to log into?** → GitHub.com
- **What is your preferred protocol?** → HTTPS (recommended)
- **Authenticate Git with your GitHub credentials?** → Yes
- **How would you like to authenticate?** → Login with a web browser

Verify authentication:

```bash
gh auth status
```

You should see:

```
github.com
  ✓ Logged in to github.com as YOUR_USERNAME
```

## Step 3: Install SCRIBE

=== "pip"

    ```bash
    pip install ai4c-scribe
    ```

=== "uv (recommended)"

    ```bash
    uv pip install ai4c-scribe
    ```

=== "uvx (no install)"

    ```bash
    # Run directly without installing
    uvx ai4c-scribe --help
    ```

## Step 4: Verify the installation

Test that SCRIBE is working:

```bash
ai4c-scribe --help
```

You should see the help output listing available commands:

```
Usage: ai4c-scribe [OPTIONS] COMMAND [ARGS]...

Commands:
  cache                Manage the local cache
  create-review-cases  Create review cases from extracted PR mining records
  distill              Distill review cases into AI-refined vignettes
  extract              Extract PRs from a repository
  fix-issue            Run an agent to fix a GitHub issue
  metadiff             Compare two diffs and compute metrics
  workflows            Manage evaluation workflows and artifacts
```

## Optional: Install AI dependencies

If you plan to use the `distill` or `fix-issue` commands for AI-powered features, install the optional AI dependencies:

```bash
pip install "ai4c-scribe[ai]"
```

## What's next?

Now that you have SCRIBE installed, choose your path:

- **Training data extraction**: Proceed to [Your first extraction](first-extraction.md)
- **Agent evaluation**: Jump to [Shadow repo evaluation](shadow-repo-eval.md)

## Troubleshooting

### "gh: command not found"

The GitHub CLI is not installed or not in your PATH. Follow the installation instructions for your operating system above.

### "gh auth login" fails

- Make sure you have a GitHub account
- Try authenticating with a personal access token: `gh auth login --with-token`

### Rate limiting

If you hit GitHub's API rate limits, wait a few minutes. The GitHub CLI handles rate limiting automatically, but authenticated requests have much higher limits than unauthenticated ones.
