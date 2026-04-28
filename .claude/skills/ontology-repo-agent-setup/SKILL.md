---
name: ontology-repo-agent-setup
description: |
  Set up an AI agent configuration GitHub repository for an ontology project.
  Use when creating a new *-agent-config repo (e.g., go-ontology-agent-config, mondo-agent-config)
  that follows the eval-agent-on-issue workflow pattern. Analyzes an existing ontology repository
  to discover CLAUDE.md, AGENTS.md, .claude/ settings, and GitHub workflows,
  then generates a properly structured agent config template repo with justfile, copier.yaml,
  and CLAUDE.md tailored to that ontology.
---

# Ontology Repo Agent Setup

Create agent configuration repositories for ontology projects that work with the `eval-agent-on-issue` GitHub Actions workflow.

## When to Use

- Creating a new `*-agent-config` repository (e.g., `go-ontology-agent-config`)
- Setting up agent instructions for an ontology that will be evaluated via GitHub Actions
- Migrating existing CLAUDE.md/AGENTS.md from an ontology repo to a standalone agent config

## Workflow

### 1. Gather Information

Ask the user for:
- **Source ontology repo**: Local path (e.g., `~/repos/go-ontology`) or GitHub URL (e.g., `go-ontology`)
- **Target agent config repo**: Local path where the new config will be created (e.g., `~/repos/go-ontology-agent-config`)
- **Ontology name**: Human-readable name (e.g., "Gene Ontology", "Mondo Disease Ontology") (can be easily introspected from the repo)
- **Target configuration type**:
   - Claude-based (best supported)
       - skills oriented or subagents oriented

### 2. Analyze Source Repository

Examine the source ontology repo for:

```bash
# Agent instruction files
ls -la CLAUDE.md AGENTS.md .goosehints .github/copilot-instructions.md 2>/dev/null

# Claude configuration (particularly skills and subagents)
ls -la .claude/ 2>/dev/null
find .claude -type f 2>/dev/null

# Copilot agents
ls -la .github/agents

# Codex
ls -la .codex

# Build system
ls -la Makefile justfile 2>/dev/null
head -100 Makefile 2>/dev/null | grep -E '^[a-z_-]+:'  # Extract make targets


# ODK configuration (common in OBO ontologies)
ls -la src/ontology/*.Makefile src/ontology/run.sh 2>/dev/null
```

Key things to extract:
- Existing agent instructions (CLAUDE.md content)
- Available make/just targets for validation (e.g., `make test`, `make validate`)
- ODK patterns if present (src/ontology structure)
- Repository-specific conventions

### 3. Create Agent Config Structure

The target config repository needs this structure:

```
{ontology}-agent-config/
├── justfile              # Required: install recipe
├── copier.yaml           # Required: copier configuration
└── template/
    └── CLAUDE.md         # Agent instructions
```

#### justfile (Required)

```just
AGENT_FILES := "CLAUDE.md AGENTS.md .goosehints .github/copilot-instructions.md .github/agents .claude .codex"

# Remove existing agent instructions from the target directory
[no-cd]
pre_clean target-directory=".":
    cd {{target-directory}} && rm -rf {{AGENT_FILES}}

# Install the template into the target directory
[no-cd]
install target-directory=".": (pre_clean target-directory)
    copier copy -f {{ justfile_directory() }}/template {{ target-directory }}
```

#### copier.yaml (Required)

```yaml
_tasks:
  - echo "Agent config installed successfully"
```

#### template/CLAUDE.md (Required for Claude Code setup)

Write instructions specific to the ontology. Include:

1. **Context about the ontology** - What it is, its domain, key concepts
2. **Repository structure** - Where source files live (e.g., `src/ontology/`)
3. **Build/validation commands** - How to test changes (e.g., `make test`)
4. **Ontology-specific conventions** - Term patterns, annotation requirements
5. **Common tasks** - Adding terms, obsoleting terms, adding xrefs

See `references/claude-md-template.md` for a comprehensive template.

### 4. Incorporate Training Insights

Based on analysis of AI agent failures across OBO ontologies (GO, Mondo, Uberon, CL, EFO):

**Critical rules to include:**
- "ONE PR PER ISSUE" - Always update existing branches, never create duplicate PRs
- Run `git diff` before any commit to verify changes match intent
- Copy patterns from recent merged PRs before making modifications
- Discuss large-scale changes before implementing

**Common failure modes to guard against:**
- Content-objective mismatch (PR description doesn't match actual changes)
- Ontology convention errors (obsoletion patterns, annotation formats)
- Missing validation step before commit

### 5. Initialize Git Repository

```bash
cd {target-repo}
git init
git add .
git commit -m "Initial agent config for {ontology-name}"
```

### 6. Provide Usage Instructions

Tell the user how to use the new config with the workflow:

```bash
gh workflow run eval-agent-on-issue \
  --repo {workflow-repo} \
  --field issue_repo={ontology-repo} \
  --field issue_number=123 \
  --field pr_number=456 \
  --field agent_config_repo={user}/{ontology}-agent-config \
  --field agent_config_tag=main \
  --field model=claude-sonnet-4-5-20250929 \
  --field create_pr=true
```

## Best Practices

### Versioning

- Use git tags for stable versions (e.g., `v1.0.0`)
- Avoid `main` or `latest` for production evaluations
- Document breaking changes

### Multiple Variants

For different agent strategies, create subdirectories:

```
my-agent-config/
├── base/           # Standard agent
├── conservative/   # Minimal changes only
└── experimental/   # More autonomous
```

Reference with `agent_config_directory: base`

### Testing

Before deploying, test the agent config:
1. Apply template to a test copy of the ontology
2. Run validation commands
3. Verify CLAUDE.md is readable and complete

## Resources

- See `references/claude-md-template.md` for CLAUDE.md template
- See `references/obo-patterns.md` for OBO Foundry-specific patterns
