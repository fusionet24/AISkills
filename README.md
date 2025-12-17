# AISkills

A centralized repository for AI skills following the Anthropic skills pattern. This repository enables you to develop, test, and maintain reusable AI skills for Claude and GPT-5.2 that can be shared across projects.

## 🎯 Overview

This repository follows the [Anthropic skills pattern](https://github.com/anthropics/skills) to create modular, reusable AI capabilities. Each skill is self-contained with clear documentation, making it easy to:

- **Centralize** AI skills in one place
- **Validate** skills automatically with linting and testing
- **Share** skills across multiple projects
- **Maintain** skills with version control
- **Discover** available skills easily

## 📁 Repository Structure

```
AISkills/
├── skills/                    # All AI skills
│   ├── code-review-assistant/
│   │   └── SKILL.md
│   └── documentation-writer/
│       └── SKILL.md
├── template/                  # Skill template for new skills
│   └── SKILL.md
├── spec/                      # Specifications and guidelines
├── .github/
│   └── workflows/
│       └── validate.yml       # CI/CD validation
├── validate_skills.py         # Skill validation script
├── requirements.txt           # Python dependencies
└── README.md
```

## 🚀 Quick Start

### Using Skills

1. Browse available skills in the `skills/` directory
2. Each skill has a `SKILL.md` file with:
   - Metadata (name, description, version)
   - Instructions for use
   - Examples
   - Notes and best practices

### Creating a New Skill

1. **Copy the template:**
   ```bash
   cp -r template skills/your-skill-name
   ```

2. **Edit the SKILL.md file:**
   ```yaml
   ---
   name: your-skill-name
   description: Clear description of when this skill activates
   version: 1.0.0
   ---
   ```

3. **Add content following the structure:**
   - Overview
   - Instructions
   - Examples
   - Notes

4. **Validate your skill:**
   ```bash
   python validate_skills.py
   ```

## 🔍 Available Skills

### Code Review Assistant
**Version:** 1.0.0  
**Description:** Analyzes code for quality issues, security vulnerabilities, and suggests improvements.

### Documentation Writer
**Version:** 1.0.0  
**Description:** Creates clear, comprehensive technical documentation, READMEs, and API docs.

## ✅ Validation & Testing

This repository includes automated validation to ensure all skills follow the correct pattern:

### Running Validation Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Validate all skills
python validate_skills.py

# Validate with strict mode (warnings as errors)
python validate_skills.py --strict
```

### Validation Checks

The validator ensures:
- ✅ Valid YAML frontmatter
- ✅ Required fields: `name`, `description`, `version`
- ✅ Proper semantic versioning (e.g., `1.0.0`)
- ✅ Lowercase skill names with hyphens
- ✅ Skill name matches directory name
- ✅ No duplicate skill names
- ⚠️  Recommended sections present (Overview, Instructions, Examples)

### CI/CD

GitHub Actions automatically validates:
- All skills on push and pull requests
- Markdown formatting
- YAML frontmatter structure
- Skill naming conventions

## 📝 Skill Format

Each `SKILL.md` file follows this structure:

```markdown
---
name: skill-name
description: A clear description of when this skill should activate
version: 1.0.0
---

# Skill Name

## Overview
Brief overview of the skill's purpose

## Instructions
Step-by-step instructions for using the skill

## Examples
Real-world examples with inputs and outputs

## Notes
Additional considerations and best practices
```

## 🛠️ Development

### Prerequisites

- Python 3.11+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/fusionet24/AISkills.git
cd AISkills

# Install dependencies
pip install -r requirements.txt
```

### Testing Changes

```bash
# Validate all skills
python validate_skills.py

# Run CI checks locally (requires act or GitHub CLI)
gh act pull_request
```

## 📚 Best Practices

1. **Keep skills focused** - Each skill should do one thing well
2. **Use clear names** - Skill names should be descriptive and lowercase with hyphens
3. **Provide examples** - Include real-world examples with expected inputs/outputs
4. **Version appropriately** - Follow semantic versioning
5. **Test thoroughly** - Ensure examples work and instructions are clear
6. **Update regularly** - Keep skills current with best practices

## 🤝 Contributing

We welcome contributions! To add a new skill:

1. Fork the repository
2. Create a new skill using the template
3. Ensure validation passes
4. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📖 Additional Resources

- [Anthropic Skills Pattern](https://github.com/anthropics/skills)
- [Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Claude Documentation](https://claude.ai/docs)

## 📄 License

This repository is available under the MIT License. See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

This repository follows the skills pattern developed by Anthropic for Claude AI. Thanks to the Anthropic team for creating this excellent pattern for organizing AI capabilities.