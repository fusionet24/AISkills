#!/usr/bin/env python3
"""
Skill Validator for AISkills Repository

This script validates SKILL.md files to ensure they follow the Anthropic skills pattern:
- Valid YAML frontmatter with required fields
- Proper semantic versioning
- Unique skill names
- Required sections in markdown
"""

import os
import sys
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class SkillValidator:
    """Validates skill files according to the Anthropic pattern."""
    
    REQUIRED_FIELDS = ['name', 'description', 'version']
    SEMVER_PATTERN = r'^\d+\.\d+\.\d+$'
    
    def __init__(self, skills_dir: str = 'skills'):
        self.skills_dir = Path(skills_dir)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.skill_names: set = set()
    
    def validate_all(self) -> bool:
        """Validate all skills in the skills directory."""
        if not self.skills_dir.exists():
            self.errors.append(f"Skills directory not found: {self.skills_dir}")
            return False
        
        skill_dirs = [d for d in self.skills_dir.iterdir() if d.is_dir()]
        
        if not skill_dirs:
            self.warnings.append("No skills found in skills directory")
            return True
        
        success = True
        for skill_dir in skill_dirs:
            skill_file = skill_dir / 'SKILL.md'
            if not skill_file.exists():
                self.errors.append(f"Missing SKILL.md in {skill_dir.name}")
                success = False
                continue
            
            if not self.validate_skill(skill_file, skill_dir.name):
                success = False
        
        # Check for duplicate names
        if not self._check_unique_names():
            success = False
        
        return success
    
    def validate_skill(self, skill_file: Path, dir_name: str) -> bool:
        """Validate a single skill file."""
        try:
            with open(skill_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"{skill_file}: Failed to read file - {e}")
            return False
        
        # Extract and validate frontmatter
        frontmatter = self._extract_frontmatter(content, skill_file)
        if frontmatter is None:
            return False
        
        # Validate required fields
        if not self._validate_required_fields(frontmatter, skill_file):
            return False
        
        # Validate name format
        if not self._validate_name_format(frontmatter['name'], skill_file):
            return False
        
        # Validate name matches directory
        if frontmatter['name'] != dir_name:
            self.errors.append(
                f"{skill_file}: Skill name '{frontmatter['name']}' "
                f"doesn't match directory name '{dir_name}'"
            )
            return False
        
        # Validate version format
        if not self._validate_version(frontmatter['version'], skill_file):
            return False
        
        # Track skill name for duplicate check
        self.skill_names.add(frontmatter['name'])
        
        # Validate markdown structure
        self._validate_markdown_structure(content, skill_file)
        
        return True
    
    def _extract_frontmatter(self, content: str, skill_file: Path) -> Optional[Dict]:
        """Extract YAML frontmatter from markdown content."""
        # Match YAML frontmatter between --- delimiters
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        
        if not match:
            self.errors.append(f"{skill_file}: Missing or invalid YAML frontmatter")
            return None
        
        try:
            frontmatter = yaml.safe_load(match.group(1))
            if not isinstance(frontmatter, dict):
                self.errors.append(f"{skill_file}: Frontmatter is not a valid YAML object")
                return None
            return frontmatter
        except yaml.YAMLError as e:
            self.errors.append(f"{skill_file}: Invalid YAML in frontmatter - {e}")
            return None
    
    def _validate_required_fields(self, frontmatter: Dict, skill_file: Path) -> bool:
        """Validate that all required fields are present."""
        missing = [f for f in self.REQUIRED_FIELDS if f not in frontmatter]
        if missing:
            self.errors.append(
                f"{skill_file}: Missing required fields: {', '.join(missing)}"
            )
            return False
        
        # Check for empty values
        empty = [f for f in self.REQUIRED_FIELDS if not frontmatter[f]]
        if empty:
            self.errors.append(
                f"{skill_file}: Empty values for: {', '.join(empty)}"
            )
            return False
        
        return True
    
    def _validate_name_format(self, name: str, skill_file: Path) -> bool:
        """Validate skill name format (lowercase with hyphens)."""
        if not re.match(r'^[a-z][a-z0-9-]*$', name):
            self.errors.append(
                f"{skill_file}: Skill name '{name}' must be lowercase "
                "with hyphens (e.g., 'my-skill-name')"
            )
            return False
        return True
    
    def _validate_version(self, version: str, skill_file: Path) -> bool:
        """Validate semantic version format."""
        if not isinstance(version, str):
            version = str(version)
        
        if not re.match(self.SEMVER_PATTERN, version):
            self.errors.append(
                f"{skill_file}: Version '{version}' must follow semantic "
                "versioning (e.g., '1.0.0')"
            )
            return False
        return True
    
    def _validate_markdown_structure(self, content: str, skill_file: Path) -> None:
        """Validate markdown structure and provide recommendations."""
        # Check for main heading
        if not re.search(r'^# .+$', content, re.MULTILINE):
            self.warnings.append(f"{skill_file}: Missing main heading (# Title)")
        
        # Check for common sections
        recommended_sections = ['Overview', 'Instructions', 'Examples']
        for section in recommended_sections:
            if not re.search(rf'^## {section}', content, re.MULTILINE):
                self.warnings.append(
                    f"{skill_file}: Recommended section '## {section}' not found"
                )
    
    def _check_unique_names(self) -> bool:
        """Check for duplicate skill names."""
        # Directory structure enforces uniqueness, but we verify anyway
        # This would only catch errors if someone manually edits skill names
        # without renaming directories
        name_counts = {}
        for name in self.skill_names:
            name_counts[name] = name_counts.get(name, 0) + 1
        
        duplicates = [name for name, count in name_counts.items() if count > 1]
        if duplicates:
            self.errors.append(
                f"Duplicate skill names found: {', '.join(duplicates)}"
            )
            return False
        return True
    
    def print_results(self) -> None:
        """Print validation results."""
        if self.errors:
            print("\n❌ ERRORS:")
            for error in self.errors:
                print(f"  {error}")
        
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  {warning}")
        
        if not self.errors and not self.warnings:
            print("✅ All skills validated successfully!")
        elif not self.errors:
            print("\n✅ Validation passed (with warnings)")
        else:
            print(f"\n❌ Validation failed with {len(self.errors)} error(s)")


def main():
    """Main entry point for the validator."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Validate AI skills following the Anthropic pattern'
    )
    parser.add_argument(
        '--skills-dir',
        default='skills',
        help='Path to skills directory (default: skills)'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Treat warnings as errors'
    )
    
    args = parser.parse_args()
    
    validator = SkillValidator(args.skills_dir)
    success = validator.validate_all()
    validator.print_results()
    
    # Exit with error code if validation failed
    if not success or (args.strict and validator.warnings):
        sys.exit(1)
    
    sys.exit(0)


if __name__ == '__main__':
    main()
