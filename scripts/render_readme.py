#!/usr/bin/env python3
"""
Renders README.md from YAML data files.
"""

import yaml
import re
from pathlib import Path
from typing import Dict, List, Any


def load_data() -> Dict[str, Any]:
    """Load data from YAML file."""
    data_file = Path(__file__).parent.parent / "data" / "repositories.yml"
    with open(data_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate_badge_urls(repo_url: str) -> Dict[str, str]:
    """Generate GitHub badge URLs for a repository."""
    # Extract owner/repo from URL
    match = re.search(r'github\.com/([^/]+/[^/]+)', repo_url)
    if not match:
        return {}
    
    repo_path = match.group(1).rstrip('/')
    
    return {
        'stars': f'![stars](https://img.shields.io/github/stars/{repo_path}?style=flat-square&cacheSeconds=604800)',
        'last_commit': f'![last commit](https://img.shields.io/github/last-commit/{repo_path}?style=flat-square&cacheSeconds=86400)'
    }


def render_repository_entry(repo: Dict[str, Any]) -> str:
    """Render a single repository entry."""
    name = repo['name']
    url = repo['url']
    description = repo.get('description', '')
    
    badges = generate_badge_urls(url)
    badges_str = f" {badges['stars']} {badges['last_commit']}" if badges else ""
    
    # Handle special spacing before the dash in description
    spacing = " -" if description and not description.startswith('-') else ""
    
    return f"- [{name}]({url}){spacing}{badges_str}{' ' + description if description else ''}"


def render_category(category: Dict[str, Any], category_id: str) -> str:
    """Render a category section."""
    lines = []
    
    # Category header
    category_name = category.get('name', category_id.replace('-', ' ').title())
    lines.append(f"### {category_name}")
    lines.append("")
    
    # Repositories
    repositories = category.get('repositories', [])
    for repo in repositories:
        lines.append(render_repository_entry(repo))
    
    lines.append("")
    return '\n'.join(lines)


def render_categories_list(categories: Dict[str, Dict[str, Any]]) -> str:
    """Render the categories list in the table of contents."""
    lines = []
    for cat_id, cat_data in categories.items():
        cat_name = cat_data.get('name', cat_id.replace('-', ' ').title())
        # Create anchor from category name
        anchor = cat_name.lower().replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '')
        lines.append(f"- [{cat_name}](#{anchor})")
        
        # Handle subcategories
        if 'subcategories' in cat_data:
            for subcat_id, subcat_data in cat_data['subcategories'].items():
                subcat_name = subcat_data.get('name', subcat_id.replace('-', ' ').title())
                subcat_anchor = subcat_name.lower().replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '')
                lines.append(f"  - [{subcat_name}](#{subcat_anchor})")
    
    return '\n'.join(lines)


def render_readme(data: Dict[str, Any]) -> str:
    """Render the complete README.md content."""
    lines = []
    
    # Header
    header = data.get('header', {})
    lines.append(f"# {header.get('title', 'C# Source Generators')}")
    lines.append("")
    
    # Table of contents
    if 'table_of_contents' in data:
        for section in data['table_of_contents']:
            lines.append(f"  * [{section['name']}](#{section['anchor']})")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # Introduction
    if 'introduction' in data:
        for para in data['introduction']:
            lines.append(para)
            lines.append("")
    
    # Documentation section
    if 'documentation' in data:
        lines.append("## Documentation and samples")
        lines.append("")
        for item in data['documentation']:
            lines.append(f"- {item}")
        lines.append("")
    
    # Source Generators section
    lines.append("## Source Generators")
    lines.append("")
    lines.append("<details open>")
    lines.append(" <summary>Categories</summary>")
    lines.append("")
    lines.append(render_categories_list(data.get('categories', {})))
    lines.append("")
    lines.append("</details>")
    lines.append("")
    
    # Template comment
    lines.append("<!--")
    lines.append("  Sorted alphabetically in each category. Template for entries:")
    lines.append("- [REPO](https://github.com/REPO) - ![stars](https://img.shields.io/github/stars/REPO?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/REPO?style=flat-square&cacheSeconds=86400)")
    lines.append("-->")
    lines.append("")
    
    # Render categories
    categories = data.get('categories', {})
    for cat_id, cat_data in categories.items():
        lines.append(render_category(cat_data, cat_id))
        
        # Handle subcategories
        if 'subcategories' in cat_data:
            for subcat_id, subcat_data in cat_data['subcategories'].items():
                lines.append(render_category(subcat_data, subcat_id))
    
    # Meta section
    if 'meta' in data:
        lines.append("## Meta - libs and generators for other generators")
        lines.append("")
        lines.append("<!--")
        lines.append("  Sorted alphabetically. Template for entries:")
        lines.append("- [REPO](https://github.com/REPO) - ![stars](https://img.shields.io/github/stars/REPO?style=flat-square&cacheSeconds=604800) ![last commit](https://img.shields.io/github/last-commit/REPO?style=flat-square&cacheSeconds=86400)")
        lines.append("-->")
        lines.append("")
        for repo in data['meta']:
            lines.append(render_repository_entry(repo))
        lines.append("")
    
    # Tips & Tricks section (keep as-is from data)
    if 'tips_and_tricks' in data:
        lines.append("## Tips & Tricks")
        lines.append("")
        lines.append(data['tips_and_tricks'])
        lines.append("")
    
    # Articles section
    if 'articles' in data:
        lines.append("## Articles")
        lines.append("")
        lines.append("<!--")
        lines.append("  Sorted from newest. Please follow the template:")
        lines.append("  - [Title](URL) (YYYY-MM-DD) short description.")
        lines.append("-->")
        for article in data['articles']:
            lines.append(f"- {article}")
        lines.append("")
    
    # Videos section
    if 'videos' in data:
        lines.append("## Videos")
        lines.append("")
        lines.append("<!--")
        lines.append("  Sorted from newest. Please follow the template:")
        lines.append("  - [Title](URL) (YYYY-MM-DD) short description.")
        lines.append("-->")
        lines.append("")
        for video in data['videos']:
            lines.append(f"- {video}")
        lines.append("")
    
    # Demo projects section
    if 'demo_projects' in data:
        lines.append("## Demo, PoC and excercise projects")
        lines.append("")
        lines.append("Maybe they can inspire you too!")
        lines.append("")
        for repo in data['demo_projects']:
            lines.append(render_repository_entry(repo))
        lines.append("")
    
    # Projects using generators internally
    if 'projects_using_generators' in data:
        lines.append('## Projects using custom Source Generators "internally"')
        lines.append("")
        for repo in data['projects_using_generators']:
            lines.append(render_repository_entry(repo))
        lines.append("")
    
    return '\n'.join(lines)


def main():
    """Main entry point."""
    data = load_data()
    readme_content = render_readme(data)
    
    output_file = Path(__file__).parent.parent / "README.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✓ README.md generated successfully")


if __name__ == '__main__':
    main()
