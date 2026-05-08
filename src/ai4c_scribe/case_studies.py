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
    """Load all case studies from a directory.

    Supports two layouts:
    - Flat: directory contains .md files directly (e.g., ``cases/31158.md``)
    - Nested: directory contains subdirs with METADATA.md (e.g., ``cases/pr32015/METADATA.md``)

    Args:
        directory: Path to directory containing case study files.

    Returns:
        List of validated CaseStudy instances.

    >>> from pathlib import Path
    >>> cases = load_case_studies_dir(Path("tests/fixtures/cases"))
    >>> len(cases) >= 1
    True
    >>> cases = load_case_studies_dir(Path("examples/cases/go-ontology"))
    >>> len(cases) >= 1
    True
    """
    cases = []

    # Check for nested layout (subdirs with METADATA.md)
    metadata_files = sorted(directory.glob("*/METADATA.md"))
    if metadata_files:
        for md_file in metadata_files:
            cases.append(load_case_study(md_file))
    else:
        # Flat layout (*.md files directly in directory)
        for md_file in sorted(directory.glob("*.md")):
            cases.append(load_case_study(md_file))

    return cases


def filter_case_studies(
    cases: list[CaseStudy],
    filters: dict[str, list[str]],
) -> list[CaseStudy]:
    """Filter case studies by metadata field values.

    Each key in filters is a field name, and the value is a list of
    acceptable values. A case passes if it matches ALL filter keys
    (AND logic across keys, OR logic within a key's values).

    Args:
        cases: List of case studies to filter.
        filters: Dict mapping field names to lists of acceptable values.

    Returns:
        Filtered list of case studies.

    >>> from pathlib import Path
    >>> cases = load_case_studies_dir(Path("tests/fixtures/cases"))
    >>> filtered = filter_case_studies(cases, {"difficulty": ["simple"]})
    >>> all(c.difficulty == "simple" for c in filtered)
    True
    >>> filtered = filter_case_studies(cases, {"task_type": ["obsoletion"]})
    >>> all(c.task_type == "obsoletion" for c in filtered)
    True
    """
    if not filters:
        return cases

    result = []
    for case in cases:
        matches = True
        for field, values in filters.items():
            attr = getattr(case, field, None)
            if attr is None:
                matches = False
                break
            if str(attr) not in values:
                matches = False
                break
        if matches:
            result.append(case)
    return result


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
