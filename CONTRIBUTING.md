# Contributing to AISkills

Thank you for your interest in contributing to AISkills! This document provides guidelines for contributing new skills and improvements to the repository.

## 🎯 How to Contribute

### Adding a New Skill

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/AISkills.git
   cd AISkills
   ```

2. **Create a New Branch**
   ```bash
   git checkout -b add-skill-your-skill-name
   ```

3. **Create Your Skill Directory**
   ```bash
   mkdir -p skills/your-skill-name
   cp template/SKILL.md skills/your-skill-name/
   ```

4. **Edit SKILL.md**
   - Update the YAML frontmatter with appropriate metadata
   - Write clear, comprehensive instructions
   - Include practical examples
   - Add notes and best practices

5. **Validate Your Skill**
   ```bash
   pip install -r requirements.txt
   python validate_skills.py
   ```

6. **Commit and Push**
   ```bash
   git add skills/your-skill-name/
   git commit -m "Add your-skill-name skill"
   git push origin add-skill-your-skill-name
   ```

7. **Create a Pull Request**
   - Go to GitHub and create a pull request
   - Describe what your skill does
   - Explain use cases and examples

## ✅ Skill Requirements

### Mandatory Requirements

All skills must:
- ✅ Have a unique, descriptive name (lowercase with hyphens)
- ✅ Include valid YAML frontmatter with `name`, `description`, and `version`
- ✅ Follow semantic versioning (e.g., `1.0.0`)
- ✅ Have the skill name match the directory name
- ✅ Include clear instructions
- ✅ Provide at least one example
- ✅ Pass all validation checks

### Quality Guidelines

Skills should:
- 📝 Be well-documented and easy to understand
- 🎯 Focus on a specific, well-defined task
- 💡 Include practical, real-world examples
- 🔄 Be reusable across different projects
- ⚡ Be concise while remaining comprehensive
- 🧪 Have examples that can be verified

## 📐 Skill Structure

### YAML Frontmatter

```yaml
---
name: your-skill-name          # Required: lowercase with hyphens
description: Brief description # Required: when skill activates
version: 1.0.0                 # Required: semantic version
---
```

### Markdown Content

```markdown
# Skill Name

## Overview
Brief overview of what the skill does (2-3 sentences)

## Instructions
Step-by-step instructions:
1. First step
2. Second step
3. Third step

## Examples

### Example 1: Descriptive Title
**Input:**
```
[Example input]
```

**Output:**
```
[Expected output]
```

## Notes
- Important considerations
- Edge cases
- Best practices
```

## 🎨 Naming Conventions

### Skill Names
- Use lowercase letters
- Separate words with hyphens
- Be descriptive but concise
- Examples: `code-review-assistant`, `api-designer`, `test-generator`

### Version Numbers
- Follow semantic versioning: `MAJOR.MINOR.PATCH`
- Start at `1.0.0` for new skills
- Increment appropriately:
  - **MAJOR**: Breaking changes
  - **MINOR**: New features (backward compatible)
  - **PATCH**: Bug fixes

## 🧪 Testing Your Skill

Before submitting:

1. **Run Validation**
   ```bash
   python validate_skills.py
   ```

2. **Check Markdown Formatting**
   Ensure your SKILL.md is properly formatted

3. **Test Examples**
   Verify that all examples work as described

4. **Review Clarity**
   Have someone else read your skill to ensure it's clear

## 🔄 Updating Existing Skills

When updating a skill:

1. Update the version number according to semantic versioning
2. Document changes in your commit message
3. Ensure backward compatibility when possible
4. Update examples if they've changed
5. Run validation to ensure compliance

## 📋 Pull Request Process

1. **Clear Description**: Explain what your skill does and why it's useful
2. **Examples**: Show how the skill works in practice
3. **Testing**: Confirm validation passes
4. **Documentation**: Update README if adding notable functionality
5. **Review**: Respond to feedback constructively

### PR Title Format
- `Add: your-skill-name skill` for new skills
- `Update: skill-name to version X.Y.Z` for updates
- `Fix: issue in skill-name` for bug fixes

## 🚫 What Not to Submit

Please avoid:
- Skills that are too broad or unfocused
- Duplicate functionality of existing skills
- Skills with incomplete or unclear documentation
- Skills without practical examples
- Skills that don't follow the required format

## 💡 Skill Ideas

Looking for ideas? Consider creating skills for:
- Code generation patterns
- Testing strategies
- Documentation templates
- Code review checklists
- Debugging approaches
- API design patterns
- Security review processes
- Performance optimization
- Refactoring techniques
- Architecture planning

## 🤝 Community Guidelines

- Be respectful and constructive
- Help others learn and improve
- Share knowledge and best practices
- Collaborate and communicate openly
- Give credit where credit is due

## 📞 Getting Help

If you have questions:
- Open an issue for general questions
- Tag maintainers in your PR for specific guidance
- Check existing skills for examples
- Review the [Anthropic skills documentation](https://github.com/anthropics/skills)

## 🙏 Recognition

Contributors will be:
- Listed in the project's contributors
- Credited in skill documentation (if desired)
- Mentioned in release notes for significant contributions

Thank you for helping make AISkills better! 🎉
