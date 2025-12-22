#!/usr/bin/env python3
"""
Extracts repository data from existing README.md into YAML format.
"""

import re
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional


def parse_repository_line(line: str) -> Optional[Dict[str, Any]]:
    """Parse a repository entry line."""
    # Pattern: - [Name](URL) - ![stars](...) ![last commit](...) Description
    # or: - [Name](URL) -![stars](...) ![last commit](...) Description
    # or: - [Name](URL) ![stars](...) ![last commit](...) - Description
    
    match = re.match(r'-\s+\[([^\]]+)\]\(([^)]+)\)\s*(-?)\s*!\[stars\]', line)
    if not match:
        return None
    
    name = match.group(1)
    url = match.group(2)
    
    # Extract description (everything after the badges)
    # Remove badges
    desc_match = re.search(r'!\[last commit\][^)]+\)\s*(-?\s*)?(.*)$', line)
    description = desc_match.group(2).strip() if desc_match and desc_match.group(2) else ""
    
    return {
        'name': name,
        'url': url,
        'description': description
    }


def extract_readme_data() -> Dict[str, Any]:
    """Extract data from README.md."""
    readme_path = Path(__file__).parent.parent / "README.md"
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    data = {
        'header': {
            'title': 'C# Source Generators'
        },
        'table_of_contents': [
            {'name': 'Documentation and samples', 'anchor': 'documentation-and-samples'},
            {'name': 'Source Generators', 'anchor': 'source-generators'},
            {'name': 'Meta - libs and generators for other generators', 'anchor': 'meta---libs-and-generators-for-other-generators'},
            {'name': 'Tips & Tricks', 'anchor': 'tips--tricks'},
            {'name': 'Articles', 'anchor': 'articles'},
            {'name': 'Videos', 'anchor': 'videos'},
            {'name': 'Demo, PoC and excercise projects', 'anchor': 'demo-poc-and-excercise-projects'},
            {'name': 'Projects using custom Source Generators "internally"', 'anchor': 'projects-using-custom-source-generators-internally'}
        ],
        'introduction': [
            "A list of C# Source Generators (not necessarily awesome), because I haven't found a good list yet.",
            "",
            "**C# Source Generators** is a Roslyn compiler feature introduced in C#9/.NET 5. It lets C# developers inspect user code and generate new C# source files that can be added to a compilation.",
            "",
            "Add GitHub topic [`csharp-sourcegenerator`](https://github.com/topics/csharp-sourcegenerator) to your generator repo - let's get it started!"
        ],
        'documentation': [],
        'categories': {},
        'meta': [],
        'articles': [],
        'videos': [],
        'demo_projects': [],
        'projects_using_generators': []
    }
    
    current_section = None
    current_category = None
    current_subcategory = None
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect sections
        if line == "## Documentation and samples":
            current_section = 'documentation'
            current_category = None
            i += 1
            continue
        elif line == "## Source Generators":
            current_section = 'source_generators'
            current_category = None
            i += 1
            continue
        elif line == "## Meta - libs and generators for other generators":
            current_section = 'meta'
            current_category = None
            i += 1
            continue
        elif line == "## Tips & Tricks":
            current_section = 'tips_and_tricks'
            # Capture the entire section
            tips_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('## '):
                tips_lines.append(lines[i])
                i += 1
            data['tips_and_tricks'] = '\n'.join(tips_lines).strip()
            continue
        elif line == "## Articles":
            current_section = 'articles'
            i += 1
            continue
        elif line == "## Videos":
            current_section = 'videos'
            i += 1
            continue
        elif line == "## Demo, PoC and excercise projects":
            current_section = 'demo_projects'
            i += 1
            continue
        elif line == '## Projects using custom Source Generators "internally"':
            current_section = 'projects_using_generators'
            i += 1
            continue
        
        # Handle documentation section
        if current_section == 'documentation' and line.startswith('- '):
            data['documentation'].append(line[2:])  # Remove '- '
        
        # Handle categories
        elif current_section == 'source_generators':
            if line.startswith('### '):
                # Main category
                category_name = line[4:].strip()
                category_id = category_name.lower().replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '').replace('--', '-')
                current_category = category_id
                data['categories'][category_id] = {
                    'name': category_name,
                    'repositories': []
                }
                current_subcategory = None
            elif line.startswith('#### '):
                # Subcategory
                subcategory_name = line[5:].strip()
                subcategory_id = subcategory_name.lower().replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '').replace('--', '-')
                current_subcategory = subcategory_id
                if current_category:
                    if 'subcategories' not in data['categories'][current_category]:
                        data['categories'][current_category]['subcategories'] = {}
                    data['categories'][current_category]['subcategories'][subcategory_id] = {
                        'name': subcategory_name,
                        'repositories': []
                    }
            elif line.startswith('- [') and current_category:
                repo = parse_repository_line(line)
                if repo:
                    if current_subcategory:
                        data['categories'][current_category]['subcategories'][current_subcategory]['repositories'].append(repo)
                    else:
                        data['categories'][current_category]['repositories'].append(repo)
        
        # Handle meta section
        elif current_section == 'meta' and line.startswith('- ['):
            repo = parse_repository_line(line)
            if repo:
                data['meta'].append(repo)
        
        # Handle articles
        elif current_section == 'articles' and line.startswith('- ['):
            data['articles'].append(line[2:])  # Remove '- '
        
        # Handle videos
        elif current_section == 'videos' and line.startswith('- ['):
            data['videos'].append(line[2:])  # Remove '- '
        
        # Handle demo projects
        elif current_section == 'demo_projects' and line.startswith('- ['):
            repo = parse_repository_line(line)
            if repo:
                data['demo_projects'].append(repo)
        
        # Handle projects using generators
        elif current_section == 'projects_using_generators' and line.startswith('- ['):
            repo = parse_repository_line(line)
            if repo:
                data['projects_using_generators'].append(repo)
        
        i += 1
    
    return data


def main():
    """Main entry point."""
    print("Extracting data from README.md...")
    data = extract_readme_data()
    
    output_file = Path(__file__).parent.parent / "data" / "repositories.yml"
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
    
    print(f"✓ Data extracted to {output_file}")
    
    # Print some stats
    total_repos = sum(len(cat.get('repositories', [])) for cat in data['categories'].values())
    total_repos += sum(
        len(subcat.get('repositories', []))
        for cat in data['categories'].values()
        if 'subcategories' in cat
        for subcat in cat['subcategories'].values()
    )
    total_repos += len(data.get('meta', []))
    total_repos += len(data.get('demo_projects', []))
    total_repos += len(data.get('projects_using_generators', []))
    
    print(f"  Categories: {len(data['categories'])}")
    print(f"  Total repositories: {total_repos}")
    print(f"  Articles: {len(data.get('articles', []))}")
    print(f"  Videos: {len(data.get('videos', []))}")


if __name__ == '__main__':
    main()
