# Quick Start Guide

This guide will help you quickly get started with the AISkills repository.

## For Users: Using Existing Skills

### Browse Available Skills

Check the `skills/` directory to see all available skills:

```bash
ls skills/
```

Each skill directory contains a `SKILL.md` file with:
- **Metadata**: Name, description, and version
- **Instructions**: How to use the skill
- **Examples**: Real-world usage examples

### Using a Skill with Claude or GPT

1. Navigate to the skill you want to use
2. Read the `SKILL.md` file
3. Copy the relevant instructions or reference the skill in your AI conversation
4. Follow the examples provided

## For Contributors: Creating New Skills

### 1. Set Up Your Environment

```bash
# Clone the repository
git clone https://github.com/fusionet24/AISkills.git
cd AISkills

# Install dependencies
pip install -r requirements.txt
```

### 2. Create a New Skill

```bash
# Copy the template
mkdir -p skills/my-new-skill
cp template/SKILL.md skills/my-new-skill/
```

### 3. Edit Your Skill

Open `skills/my-new-skill/SKILL.md` and update:

```yaml
---
name: my-new-skill
description: What your skill does and when it activates
version: 1.0.0
---
```

Fill in the sections:
- **Overview**: Brief description
- **Instructions**: Step-by-step guide
- **Examples**: Practical examples
- **Notes**: Additional tips

### 4. Validate Your Skill

```bash
# Run validation
python validate_skills.py

# Check for any errors or warnings
```

### 5. Test Your Skill

- Read through your skill documentation
- Try using it with Claude or GPT
- Ensure examples are clear and correct

### 6. Submit Your Skill

```bash
# Create a branch
git checkout -b add-my-new-skill

# Add your skill
git add skills/my-new-skill/

# Commit
git commit -m "Add my-new-skill"

# Push
git push origin add-my-new-skill
```

Then create a pull request on GitHub.

## Common Tasks

### Updating an Existing Skill

1. Edit the skill's `SKILL.md` file
2. Update the version number according to semantic versioning
3. Run validation: `python validate_skills.py`
4. Commit and push your changes

### Running Validation in Strict Mode

```bash
python validate_skills.py --strict
```

This treats warnings as errors.

### Checking a Specific Skills Directory

```bash
python validate_skills.py --skills-dir /path/to/skills
```

## Validation Checklist

Before submitting a skill, ensure:

- ✅ Skill name is lowercase with hyphens
- ✅ Skill name matches directory name
- ✅ Version follows semantic versioning (e.g., `1.0.0`)
- ✅ Description clearly explains when the skill activates
- ✅ Instructions are clear and actionable
- ✅ At least one example is provided
- ✅ Validation passes: `python validate_skills.py`

## Troubleshooting

### Validation Fails

**Issue**: `Skill name 'My-Skill' must be lowercase with hyphens`

**Solution**: Use lowercase letters and hyphens only: `my-skill`

---

**Issue**: `Version '1.0' must follow semantic versioning`

**Solution**: Use three numbers: `1.0.0`

---

**Issue**: `Missing required fields: description`

**Solution**: Add all required fields in YAML frontmatter:
```yaml
---
name: skill-name
description: Clear description
version: 1.0.0
---
```

### Need Help?

- Check the [CONTRIBUTING.md](CONTRIBUTING.md) guide
- Review the [spec/SPECIFICATION.md](spec/SPECIFICATION.md)
- Look at existing skills for examples
- Open an issue on GitHub

## Tips for Writing Great Skills

1. **Be Specific**: Focus on one task or capability
2. **Be Clear**: Use simple, direct language
3. **Provide Examples**: Show real-world usage
4. **Test Thoroughly**: Ensure examples work
5. **Keep Updated**: Maintain relevance with best practices

## Next Steps

- Explore existing skills in `skills/`
- Read the full [README.md](README.md)
- Check out [CONTRIBUTING.md](CONTRIBUTING.md)
- Review the [spec/SPECIFICATION.md](spec/SPECIFICATION.md)

Happy skill building! 🚀
