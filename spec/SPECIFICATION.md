# AISkills Specification

## Overview

This document defines the specification for skills in the AISkills repository, following the Anthropic skills pattern.

## Skill Structure

### Directory Organization

```
skills/
└── skill-name/
    ├── SKILL.md          # Required: Main skill definition
    └── [resources]/      # Optional: Supporting files
```

### SKILL.md Format

Each skill must have a `SKILL.md` file with the following structure:

#### 1. YAML Frontmatter (Required)

```yaml
---
name: skill-name
description: Description of when and how the skill activates
version: 1.0.0
---
```

**Field Specifications:**

| Field | Type | Required | Format | Description |
|-------|------|----------|--------|-------------|
| `name` | string | Yes | `[a-z][a-z0-9-]*` | Unique skill identifier, lowercase with hyphens |
| `description` | string | Yes | Free text | Clear description of skill purpose and activation |
| `version` | string | Yes | `X.Y.Z` | Semantic version number |

#### 2. Markdown Content (Required)

The markdown body should follow this structure:

```markdown
# Skill Title

## Overview
Brief description of the skill (1-3 paragraphs)

## Instructions
Detailed step-by-step instructions

## Examples
Practical examples with inputs and outputs

## Notes
Additional considerations, edge cases, and best practices
```

**Section Guidelines:**

- **Overview**: Concise explanation of what the skill does
- **Instructions**: Clear, actionable steps for using the skill
- **Examples**: Real-world scenarios with expected inputs/outputs
- **Notes**: Edge cases, limitations, and tips

### Optional Components

Skills may include additional files:
- Supporting scripts
- Configuration files
- Example data
- Templates

## Validation Rules

### Mandatory Rules (Errors)

1. **File Existence**: Each skill directory must contain `SKILL.md`
2. **Frontmatter Format**: Valid YAML between `---` delimiters
3. **Required Fields**: Must include `name`, `description`, `version`
4. **Name Format**: Lowercase letters, numbers, and hyphens only
5. **Name Consistency**: Skill name must match directory name
6. **Version Format**: Must follow semantic versioning (e.g., `1.0.0`)
7. **Non-empty Fields**: No required field can be empty

### Recommended Guidelines (Warnings)

1. **Main Heading**: Should include a top-level heading (`# Title`)
2. **Standard Sections**: Should include Overview, Instructions, Examples
3. **Description Length**: Description should be clear and concise
4. **Example Quality**: Examples should be practical and clear

## Semantic Versioning

Skills use semantic versioning (`MAJOR.MINOR.PATCH`):

- **MAJOR**: Incompatible changes (e.g., changing skill behavior)
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes and small improvements

## Naming Conventions

### Skill Names

- Must be unique within the repository
- Use lowercase letters
- Separate words with hyphens
- Be descriptive but concise
- Match directory name exactly

**Good Examples:**
- `code-review-assistant`
- `api-designer`
- `test-generator`
- `documentation-writer`

**Bad Examples:**
- `CodeReview` (not lowercase)
- `code_review` (underscores not allowed)
- `cr` (too short, not descriptive)
- `code-review-and-testing-and-documentation` (too long)

### Directory Structure

```
skills/skill-name/    # Directory name matches skill name
└── SKILL.md          # Uppercase for consistency
```

## Description Guidelines

A good description:
- Explains when the skill should activate
- Describes what the skill does
- Is written in natural language
- Is concise but complete (1-2 sentences)

**Examples:**

✅ Good:
```yaml
description: Activates when reviewing code to identify quality issues, security vulnerabilities, and suggest improvements
```

❌ Too vague:
```yaml
description: Helps with code
```

❌ Too long:
```yaml
description: This skill is designed to help you review code by analyzing it for various issues including but not limited to security vulnerabilities, code quality problems, performance issues, and suggesting various improvements that could be made to make the code better...
```

## Example Structure

### Minimal Valid Skill

```markdown
---
name: minimal-skill
description: A minimal valid skill example
version: 1.0.0
---

# Minimal Skill

## Overview
This is a minimal valid skill.

## Instructions
1. Do something
2. Check the result

## Examples
Example content here
```

### Comprehensive Skill

```markdown
---
name: comprehensive-skill
description: A comprehensive example skill with all sections
version: 1.2.3
---

# Comprehensive Skill

## Overview
Detailed overview with context and use cases.

## Instructions
1. First step with details
2. Second step with details
3. Third step with details

### Advanced Usage
Additional instructions for advanced scenarios.

## Examples

### Example 1: Basic Use Case
**Input:**
```
[code or text]
```

**Output:**
```
[expected result]
```

### Example 2: Advanced Use Case
**Input:**
```
[code or text]
```

**Output:**
```
[expected result]
```

## Notes
- Important consideration 1
- Important consideration 2
- Edge case handling
- Best practices

## Related Skills
- [other-skill](../other-skill/SKILL.md)
```

## Validation Process

Skills are validated through:

1. **Local Validation**
   ```bash
   python validate_skills.py
   ```

2. **CI/CD Pipeline**
   - Runs on every push and pull request
   - Validates YAML frontmatter
   - Checks naming conventions
   - Verifies semantic versioning
   - Lints markdown formatting

3. **Manual Review**
   - Code review by maintainers
   - Quality assessment
   - Usefulness evaluation

## Best Practices

1. **Focus**: Each skill should do one thing well
2. **Clarity**: Instructions should be clear and unambiguous
3. **Examples**: Include practical, testable examples
4. **Completeness**: Cover common use cases and edge cases
5. **Maintainability**: Keep skills updated and relevant
6. **Modularity**: Skills should be independent when possible
7. **Documentation**: Explain the "why" not just the "what"

## Version History

- **1.0.0** (2025-12-16): Initial specification

## References

- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Semantic Versioning](https://semver.org/)
