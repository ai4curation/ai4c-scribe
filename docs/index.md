# SCRIBE

**Social Coding Repository artificial Intelligence Benchmarking and Evaluation**

SCRIBE helps teams evaluate and improve AI coding agents by curating case studies from GitHub repositories and running systematic evaluations at scale.

Part of the [AI4Curation](https://github.com/ai4curation) initiative for integrating AI into knowledge curation workflows.

## Who is SCRIBE for?

SCRIBE is designed for teams that:

- **Maintain GitHub-based repositories** (code, ontologies, knowledge bases, documentation)
- **Want to evaluate AI coding agents** systematically against real-world tasks
- **Need curated case studies** from historical PRs with validated metadata
- **Run projects with established review processes** that contain valuable institutional knowledge

Common use cases include ontology development teams (OBO Foundry projects), open-source maintainers, and research groups using GitHub for collaborative knowledge engineering.

## Two Core Capabilities

### 1. Case Study Curation

Use an agent skill to discover and curate high-quality case studies from your repository's history:

```bash
# Use the /find-training-cases skill in Claude Code to curate cases
# The skill searches for PRs with clean issue-to-PR mappings and writes
# markdown case study files with validated frontmatter

# Validate curated case studies
ai4c-scribe cases validate cases/go-ontology/

# List case studies with summary
ai4c-scribe cases list cases/go-ontology/
```

**What you get:**

- Markdown files with LinkML-validated YAML frontmatter
- Rich metadata: difficulty, scope, task type, domain area, review outcome
- Context and resolution notes written by the curation agent
- Diverse coverage across task types and difficulty levels
- Machine-readable schema for downstream tooling

### 2. Agent Evaluation at Scale

Use "shadow repositories" to evaluate AI agents against known-good human solutions:

```bash
# Run agent evaluation via GitHub Actions workflow
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

**How it works:**

1. **Curate** case studies from your repository's history (using the skill)
2. **Import** the target repository as a "shadow repo" in your organization
3. **Point** workflow config at your case study folder via `input_sets_dir`
4. **Run agents** from the exact commit state before the original PR
5. **Compare** agent solutions against human solutions using metadiff

This approach keeps the original repository clean while enabling systematic, reproducible evaluation.

## Quick Start

### Installation

```bash
# Install from PyPI
pip install ai4c-scribe

# Or with uv (recommended)
uv pip install ai4c-scribe

# Verify installation
ai4c-scribe --help
```

**Requirements:**

- Python 3.11+
- [GitHub CLI (gh)](https://cli.github.com/) authenticated with `gh auth login`

### Curate Your First Case Studies

```bash
# In Claude Code, use the /find-training-cases skill:
# /find-training-cases geneontology/go-ontology --limit 20

# This creates markdown files like cases/go-ontology/31158.md
# with validated YAML frontmatter

# Validate the output
ai4c-scribe cases validate cases/go-ontology/
```

### Configure an Evaluation Run

```yaml
# eval-config.yaml
workflow: eval-agent-on-issue.yml
repo: cmungall/go-ontology-eval-2026
input_sets_dir: cases/go-ontology/
inputs:
  issue_repo: geneontology/go-ontology
  model: [claude-opus-4-5-20251101, claude-sonnet-4-5-20250929]
  agent_config_repo: cmungall/go-ontology-agent-config
  agent_config_tag: v6
```

See the [tutorials](tutorials/index.md) for complete walkthroughs.

## Documentation

<div class="grid cards" markdown>

-   :material-school:{ .lg .middle } **Tutorials**

    ---

    Step-by-step guides from installation to running evaluations

    [:octicons-arrow-right-24: Get started](tutorials/index.md)

-   :material-tools:{ .lg .middle } **How-to guides**

    ---

    Task-focused guides for specific operations

    [:octicons-arrow-right-24: How-to guides](how-to/index.md)

-   :material-book-open-variant:{ .lg .middle } **Explanation**

    ---

    Background concepts, design decisions, and rationale

    [:octicons-arrow-right-24: Concepts](explanation/index.md)

-   :material-file-code:{ .lg .middle } **Reference**

    ---

    CLI commands, GitHub workflows, and case study schema

    [:octicons-arrow-right-24: Reference](reference/index.md)

</div>

## The SCRIBE Pipeline

```mermaid
graph TB
    subgraph "Case Study Curation"
        GH1[GitHub Repository] --> SKILL[/find-training-cases Skill]
        SKILL --> CS[Case Study .md Files]
        CS --> VAL[Validate Schema]
    end

    subgraph "Agent Evaluation Pipeline"
        CS --> CFG[Workflow Config]
        GH2[Original Repository] --> IMP[Import as Shadow Repo]
        CFG --> RUN[Run Agent at Parent SHA]
        IMP --> RUN
        RUN --> CMP[Metadiff vs Human Solution]
        CMP --> MET[Evaluation Metrics]
    end
```

## Background

SCRIBE emerged from the [AI4Curation](https://github.com/ai4curation) project, which explores how AI can assist with knowledge curation in biomedical ontologies and knowledge graphs.

Key insights driving SCRIBE's design:

- **Case studies encode institutional knowledge.** Mature repositories have extensive PR history with reviews, discussions, and iterative refinements. Case studies capture this as structured, reusable evaluation data.

- **Agentic curation beats heuristics.** Rather than deterministic extraction pipelines, an AI agent with judgment can select diverse, high-quality cases and annotate them with rich metadata.

- **Reproducible evaluation requires careful setup.** Agents must start from the same commit state as human developers to enable fair comparison.

- **Shadow repos keep originals clean.** Running evaluations on imported copies avoids polluting production repositories with experiment branches.

- **CLI-first design.** SCRIBE prioritizes command-line workflows that integrate with existing GitHub tooling and automation.

For more on the AI4Curation vision, see:

- [AI4Curation Documentation](https://ai4curation.github.io/aidocs/)
- [Chris Mungall on Knowledge Graphs and AI](https://knowledgegraphinsights.com/chris-mungall/)

## Links

- [GitHub Repository](https://github.com/ai4curation/ai4c-scribe)
- [Issue Tracker](https://github.com/ai4curation/ai4c-scribe/issues)
- [AI4Curation Organization](https://github.com/ai4curation)
