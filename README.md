
# ai4c-scribe

Learns best practice from your GitHub repo by mining pull requests and extracting training/evaluation datasets for LLM-as-judge frameworks.

## Overview

ai4c-scribe extracts valuable training data from GitHub repositories by analyzing:
- Pull request metadata and lifecycle
- Code reviews and feedback
- Commit history and evolution
- Linked issues and their discussions

This data can be used to train and evaluate LLMs for code review, best practices enforcement, and repository-specific workflows.

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/ai4curation/ai4c-scribe.git
cd ai4c-scribe

# Install with uv
uv sync
```

### Basic Usage

Extract PRs from a repository:

```bash
# Extract the latest 10 merged PRs from mondo
uv run ai4c-scribe extract monarch-initiative/mondo -o mondo-prs.jsonl -l 10

# Extract PRs starting from a specific PR number
uv run ai4c-scribe extract monarch-initiative/mondo -o mondo-prs.jsonl -s 8000 -l 50

# Extract only PRs with 1-to-1 issue mappings
uv run ai4c-scribe extract monarch-initiative/mondo -o mondo-prs.jsonl --one-to-one-only -l 100
```

### CLI Commands

- `extract` - Mine PRs from a repository and export to JSONL format
- `review` - (Coming soon) Convert extracted PRs into markdown review vignettes
- `learn` - (Coming soon) End-to-end pipeline: extract → review → train
- `metadiff` - Compare two diffs and compute metrics (similarity, F1, precision, recall)
- `workflows` - Manage evaluation workflows and download artifacts

Run `uv run ai4c-scribe --help` for full command documentation.

## Example: Mining Mondo Ontology

```bash
# Extract 100 merged PRs from the Mondo ontology repository
uv run ai4c-scribe extract monarch-initiative/mondo \
  -o data/mondo-mining.jsonl \
  --limit 100 \
  --state merged

# Output includes:
# - PR categorization (merged_no_mods, merged_with_mods, revised_abandoned)
# - Complete commit history with diffs
# - Review comments and feedback
# - Linked issues with discussions
# - Timing statistics
```

## Output Format

The `extract` command outputs JSONL (one JSON object per line), with each record containing:

- **Metadata**: PR number, title, author, state, timestamps
- **Commits**: Full commit history with individual diffs
- **Reviews**: Review feedback, comments, and requested changes
- **Issues**: Linked issues with comments (filtered by PR creation time)
- **Diffs**: Initial and final diffs for comparison
- **Statistics**: Time to merge, time to first review, etc.

## PR Categories

PRs are automatically categorized into three types:

- `merged_no_mods`: Single commit merged as-is (no modifications)
- `merged_with_mods`: Multiple commits showing evolution through review
- `revised_abandoned`: Closed without merging

## Metadiff: Comparing PRs

Metadiff is a tool for deterministically comparing two diffs with standard metrics. Perfect for evaluating how well an agent learned to fix issues in a repository.

### Basic Usage

```bash
# List available comparison configs
uv run ai4c-scribe metadiff configs

# Compare two diff files
uv run ai4c-scribe metadiff compare human.diff agent.diff

# With OBO ontology config (masks IDs, ignores metadata)
uv run ai4c-scribe metadiff compare human.diff agent.diff -c obo

# Save results as JSON
uv run ai4c-scribe metadiff compare human.diff agent.diff -o results.json -f json
```

### Python API

```python
from ai4c_scribe.metadiff import compare_diffs, get_config

# Compare two diffs
result = compare_diffs(human_diff, agent_diff, config=get_config("obo"))

# Access metrics
print(f"Similarity: {result.similarity:.3f}")   # Jaccard similarity (0-1)
print(f"F1 Score: {result.f1_score:.3f}")       # Harmonic mean (0-1)
print(f"Precision: {result.precision:.3f}")     # True positives / predicted (0-1)
print(f"Recall: {result.recall:.3f}")           # True positives / actual (0-1)
```

See [METADIFF.md](METADIFF.md) for comprehensive documentation.

## Testing

```bash
# Run all tests
just test

# Run only unit tests
just pytest

# Run specific test file
uv run pytest tests/test_pr_mining.py -v
```

## Documentation Website

[https://ai4curation.github.io/ai4c-scribe](https://ai4curation.github.io/ai4c-scribe)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [ai4c_scribe](src/ai4c_scribe)
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [monarch-project-copier](https://github.com/monarch-initiative/monarch-project-copier)
