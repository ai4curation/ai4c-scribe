"""Load and validate case study markdown files with YAML frontmatter.

Case studies are markdown files with YAML frontmatter that describe
issue/PR pairs suitable for agent evaluation replay.
"""

from pathlib import Path

import yaml

from ai4c_scribe.schema import CaseStudy


def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from markdown text.

    Parses the YAML block between the first pair of ``---`` delimiters.

    Args:
        text: Full markdown file content.

    Returns:
        Dictionary of parsed YAML frontmatter fields.

    >>> parse_frontmatter("---\\nrepo: foo/bar\\n---\\nBody text.\\n")
    {'repo': 'foo/bar'}
    >>> parse_frontmatter("---\\na: 1\\nb: 2\\n---\\n")
    {'a': 1, 'b': 2}
    """
    parts = text.split("---", 2)
    # parts[0] is empty (before first ---), parts[1] is YAML, parts[2] is body
    yaml_content = parts[1]
    return yaml.safe_load(yaml_content)


def load_case_study(path: Path) -> CaseStudy:
    """Load a single case study from a markdown file with YAML frontmatter.

    Args:
        path: Path to the markdown file.

    Returns:
        Validated CaseStudy instance.

    >>> from pathlib import Path
    >>> p = Path("tests/fixtures/cases/sample-case.md")
    >>> case = load_case_study(p)
    >>> case.repo
    'geneontology/go-ontology'
    >>> case.issue_number
    31158
    """
    text = path.read_text()
    data = parse_frontmatter(text)
    return CaseStudy(**data)


def load_case_studies_dir(directory: Path) -> list[CaseStudy]:
    """Load all case studies from markdown files in a directory.

    Args:
        directory: Path to directory containing .md case study files.

    Returns:
        List of validated CaseStudy instances.

    >>> from pathlib import Path
    >>> cases = load_case_studies_dir(Path("tests/fixtures/cases"))
    >>> len(cases) >= 1
    True
    """
    cases = []
    for md_file in sorted(directory.glob("*.md")):
        cases.append(load_case_study(md_file))
    return cases


def case_study_to_input_set(case: CaseStudy) -> dict[str, str]:
    """Convert a case study to a workflow input_set dictionary.

    Extracts the issue_number and pr_number as strings, suitable for
    passing to workflow runners.

    Args:
        case: A validated CaseStudy instance.

    Returns:
        Dictionary with string values for issue_number and pr_number.

    >>> from pathlib import Path
    >>> case = load_case_study(Path("tests/fixtures/cases/sample-case.md"))
    >>> case_study_to_input_set(case)
    {'issue_number': '31158', 'pr_number': '31262'}
    """
    return {
        "issue_number": str(case.issue_number),
        "pr_number": str(case.pr_number),
    }
