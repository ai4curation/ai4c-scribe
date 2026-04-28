# CLAUDE.md Template for Ontology Repositories

Use this template as a starting point, customizing for the specific ontology.

```markdown
# Agent Instructions for {ONTOLOGY_NAME}

You are an AI agent working on the {ONTOLOGY_NAME} ({ONTOLOGY_ID_PREFIX}).

## About This Ontology

{Brief description of what the ontology covers, its domain, and purpose.}

## Repository Structure

- `src/ontology/` - Main ontology source files
  - `{ontology}-edit.owl` - Primary edit file (OWL format)
  - `{ontology}.obo` - OBO format export
  - `imports/` - Imported ontology modules
  - `components/` - Modular components
- `Makefile` or `src/ontology/Makefile` - Build targets
- `.github/workflows/` - CI/CD pipelines

## Task Guidelines

1. Read the issue context from `__issue_context__.json`
2. Understand what changes are requested
3. Make the necessary changes
4. Run validation before committing
5. Commit with a clear message describing what was done

## CRITICAL RULES

### ONE PR PER ISSUE
- NEVER create a new PR if one already exists for this issue
- Always push to the existing branch
- Check `git branch -a` before creating new branches

### Verify Before Commit
- Always run `git diff` before committing to verify changes match intent
- Run validation commands (see below) before committing
- Never commit unrelated changes

### Copy Existing Patterns
- Look at recent merged PRs for similar changes
- Follow the exact format of existing entries
- Don't invent new patterns without explicit approval

## Validation Commands

```bash
# Basic validation (always run)
make test

# Full validation (for significant changes)
make validate

# Check for common errors
make check
```

If validation fails, fix the issues before committing. Do not commit broken ontology files.

## Common Tasks

### Adding a New Term

1. Find the appropriate location in the edit file
2. Copy the structure from a similar existing term
3. Required annotations:
   - rdfs:label (human-readable name)
   - IAO:0000115 (definition)
   - oboInOwl:id (term ID in {ONTOLOGY_ID_PREFIX}:NNNNNNN format)
4. Add appropriate parent class (rdfs:subClassOf)

### Obsoleting a Term

1. Add `owl:deprecated true`
2. Add `IAO:0000231` (reason for deprecation)
3. Add `IAO:0000227` (term replaced by) if applicable
4. Do NOT delete the term - mark as obsolete
5. Move to obsolete branch in hierarchy if applicable

### Adding Cross-References (xrefs)

1. Use `oboInOwl:hasDbXref` annotation
2. Format: `{DATABASE}:{ID}` (e.g., `MESH:D001234`)
3. Verify the xref is valid before adding

### Editing Definitions

1. Definitions use `IAO:0000115` annotation
2. Keep definitions concise but complete
3. Follow genus-differentia pattern when appropriate
4. Include references if adding factual claims

## File Formats

### OWL/RDF
- Primary edit format for most OBO ontologies
- Use Protege or text editor for modifications
- Manchester syntax or OWL functional syntax

### OBO Format
- Legacy format, generated from OWL
- Some ontologies still edit in OBO format
- Check which format this ontology uses

## Error Handling

If you encounter:
- **Syntax errors**: Check OWL/OBO format carefully
- **Validation failures**: Read error messages, fix root cause
- **Merge conflicts**: Do not force resolve, ask for help
- **Unclear requirements**: Ask for clarification in ISSUE_COMMENTS.md

## Don't Do These Things

- Don't delete terms (obsolete them instead)
- Don't change term IDs
- Don't modify imported ontologies directly
- Don't skip validation
- Don't make changes outside the issue scope
- Don't commit generated files (*.owl, *.obo in root)
```

## Customization Notes

When adapting this template:

1. **Replace placeholders**: `{ONTOLOGY_NAME}`, `{ONTOLOGY_ID_PREFIX}`, `{ontology}`
2. **Add ontology-specific sections**: Some ontologies have unique patterns
3. **Update validation commands**: Match what's in the Makefile
4. **Include domain knowledge**: Key concepts agents should understand
5. **Reference local patterns**: Point to example files in the repo
