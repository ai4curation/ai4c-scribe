# ============ Hint for for Windows Users ============

# On Windows the "sh" shell that comes with Git for Windows should be used.
# If it is not on path, provide the path to the executable in the following line.
#set windows-shell := ["C:/Program Files/Git/usr/bin/sh", "-cu"]

# ============ Variables used in recipes ============

# Set shebang line for cross-platform Python recipes (assumes presence of launcher on Windows)
shebang := if os() == 'windows' {
  'py'
} else {
  '/usr/bin/env python3'
}


# ============== Project recipes ==============

# List all commands as default command. The prefix "_" hides the command.
_default: _status
    @just --list

# Initialize a new project (use this for projects not yet under version control)
[group('project management')]
setup: _git-init _ai-instructions install _git-add
  git commit -m "Initialise git with minimal project" -a

  
# Install project dependencies
[group('project management')]
install:
  uv sync --group dev


# Run all tests (skips integration tests by default, see pytest.ini)
[group('model development')]
test: pytest mypy format

# Run all tests including integration tests (requires gh CLI auth)
test-full: pytest-all mypy format

# Run pytest (skips integration tests by default)
pytest:
  uv run pytest

# Run all pytest tests including integration (requires gh CLI auth)
pytest-all:
  uv run pytest -m ""

doctest:
  uv run pytest  --doctest-modules src

mypy:
  uv run mypy src tests

format:
	uv run ruff check .

# Fetch eval PR data (agent comments, traces) for the gallery
gallery-fetch:
  uv run ai4c-scribe gallery-fetch analysis/

# Regenerate the gallery HTML from analysis/ directory
gallery:
  uv run ai4c-scribe gallery analysis/ -o analysis/gallery.html
  @echo "Open: open analysis/gallery.html"

# ============== Hidden internal recipes ==============

_status:
  @echo "OK"

# Update project template
_update-template:
  copier update --trust --skip-answered


# Run documentation server
_serve:
  uv run mkdocs serve

# Initialize git repository
_git-init:
  git init

# Add files to git
_git-add:
  git add .

# Commit files to git
_git-commit:
  git commit -m 'chore: just setup was run' -a

# Show git status
_git-status:
  git status

goosehints:
  [ -f .goosehints ] || ln -s CLAUDE.md .goosehints

copilot-instructions:
  [ -f .github/copilot-instructions.md ] || cd .github && ln -s ../CLAUDE.md copilot-instructions.md

_ai-instructions: goosehints copilot-instructions

gh-add-topics:
  gh repo edit --add-topic "ai4c-scribe,monarchinitiative,linkml"

gh-add-secrets:
  gh secret set PAT_FOR_PR --body "$PAT_FOR_PR"
  gh secret set ANTHROPIC_API_KEY --body "$ANTHROPIC_API_KEY"
  gh secret set OPENAI_API_KEY --body "$OPENAI_API_KEY"
  gh secret set CBORG_API_KEY --body "$CBORG_API_KEY"
  gh secret set CLAUDE_CODE_OATH_TOKEN --body "$CLAUDE_CODE_OATH_TOKEN"

gh-invite-the-dragon:
  gh api repos/ai4curation/ai4c-scribe/collaborators/dragon-ai-agent -X PUT -f permission=push

# ============== Distillation test setup ==============

# Create a git worktree for testing distillation with mondo repo
[group('distillation')]
setup-mondo-worktree BRANCH="distill-test":
  #!/usr/bin/env bash
  set -euo pipefail

  # Create test worktree directory if it doesn't exist
  mkdir -p test/worktrees

  # Clone mondo if we don't have it
  if [ ! -d "test/mondo-checkout" ]; then
    echo "Cloning mondo repository..."
    git clone https://github.com/monarch-initiative/mondo.git test/mondo-checkout
  fi

  cd test/mondo-checkout

  # Remove existing worktree if present
  if [ -d "../worktrees/mondo-{{BRANCH}}" ]; then
    echo "Removing existing worktree..."
    git worktree remove ../worktrees/mondo-{{BRANCH}} --force || true
  fi

  # Delete branch if it exists
  git branch -D {{BRANCH}} 2>/dev/null || true

  # Create fresh worktree from master
  echo "Creating worktree at test/worktrees/mondo-{{BRANCH}}..."
  git worktree add ../worktrees/mondo-{{BRANCH}} -b {{BRANCH}} master

  echo "✅ Worktree created at test/worktrees/mondo-{{BRANCH}}"

# Clean up mondo worktree
[group('distillation')]
clean-mondo-worktree BRANCH="distill-test":
  #!/usr/bin/env bash
  set -euo pipefail

  if [ -d "test/mondo-checkout" ]; then
    cd test/mondo-checkout
    git worktree remove ../worktrees/mondo-{{BRANCH}} --force || true
    git branch -D {{BRANCH}} 2>/dev/null || true
  fi

  rm -rf test/worktrees/mondo-{{BRANCH}}
  echo "✅ Cleaned up worktree"

# ============== Include project-specific recipes ==============

import "project.justfile"
