#!/usr/bin/env python3
"""
Validates the YAML data file for correctness.
"""

import yaml
import re
import sys
from pathlib import Path
from typing import Dict, List, Any, Set
from urllib.parse import urlparse


def validate_url(url: str) -> bool:
    """Validate that a URL is well-formed."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def validate_github_url(url: str) -> bool:
    """Validate that a URL is a GitHub URL."""
    return 'github.com' in url.lower()


def check_duplicates(data: Dict[str, Any]) -> List[str]:
    """Check for duplicate repository URLs."""
    errors = []
    all_urls: Set[str] = set()
    
    def add_repos(repos: List[Dict], section_name: str):
        for repo in repos:
            url = repo.get('url', '')
            if url in all_urls:
                errors.append(f"Duplicate URL found in {section_name}: {url}")
            all_urls.add(url)
    
    # Check categories
    for cat_id, cat_data in data.get('categories', {}).items():
        add_repos(cat_data.get('repositories', []), f"category '{cat_id}'")
        
        # Check subcategories
        for subcat_id, subcat_data in cat_data.get('subcategories', {}).items():
            add_repos(subcat_data.get('repositories', []), f"subcategory '{subcat_id}'")
    
    # Check other sections
    add_repos(data.get('meta', []), 'meta')
    add_repos(data.get('demo_projects', []), 'demo_projects')
    add_repos(data.get('projects_using_generators', []), 'projects_using_generators')
    
    return errors


def validate_repository(repo: Dict[str, Any], location: str) -> List[str]:
    """Validate a single repository entry."""
    errors = []
    
    # Check required fields
    if 'name' not in repo:
        errors.append(f"{location}: Missing 'name' field")
    elif not repo['name'].strip():
        errors.append(f"{location}: 'name' is empty")
    
    if 'url' not in repo:
        errors.append(f"{location}: Missing 'url' field")
    else:
        url = repo['url']
        if not validate_url(url):
            errors.append(f"{location}: Invalid URL format: {url}")
        elif not validate_github_url(url):
            errors.append(f"{location}: URL is not a GitHub URL: {url}")
    
    # Description is optional, but if present should not be empty
    if 'description' in repo and not repo['description'].strip():
        errors.append(f"{location}: 'description' field is present but empty")
    
    return errors


def validate_category(category: Dict[str, Any], cat_id: str, is_subcategory: bool = False) -> List[str]:
    """Validate a category."""
    errors = []
    cat_type = "Subcategory" if is_subcategory else "Category"
    
    # Check for name
    if 'name' not in category:
        errors.append(f"{cat_type} '{cat_id}': Missing 'name' field")
    
    # Validate repositories
    repositories = category.get('repositories', [])
    if not isinstance(repositories, list):
        errors.append(f"{cat_type} '{cat_id}': 'repositories' must be a list")
    else:
        for i, repo in enumerate(repositories):
            if not isinstance(repo, dict):
                errors.append(f"{cat_type} '{cat_id}', repository {i}: Must be a dictionary")
            else:
                repo_errors = validate_repository(repo, f"{cat_type} '{cat_id}', repository '{repo.get('name', f'#{i}')}'")
                errors.extend(repo_errors)
    
    return errors


def validate_data(data: Dict[str, Any]) -> List[str]:
    """Validate the entire data structure."""
    errors = []
    
    # Validate header
    if 'header' not in data:
        errors.append("Missing 'header' section")
    elif 'title' not in data['header']:
        errors.append("Missing 'title' in header")
    
    # Validate categories
    if 'categories' not in data:
        errors.append("Missing 'categories' section")
    else:
        for cat_id, cat_data in data['categories'].items():
            if not isinstance(cat_data, dict):
                errors.append(f"Category '{cat_id}': Must be a dictionary")
                continue
            
            errors.extend(validate_category(cat_data, cat_id))
            
            # Validate subcategories
            if 'subcategories' in cat_data:
                for subcat_id, subcat_data in cat_data['subcategories'].items():
                    if not isinstance(subcat_data, dict):
                        errors.append(f"Subcategory '{cat_id}/{subcat_id}': Must be a dictionary")
                        continue
                    errors.extend(validate_category(subcat_data, f"{cat_id}/{subcat_id}", is_subcategory=True))
    
    # Validate meta
    if 'meta' in data:
        for i, repo in enumerate(data['meta']):
            repo_errors = validate_repository(repo, f"Meta repository '{repo.get('name', f'#{i}')}'")
            errors.extend(repo_errors)
    
    # Validate demo_projects
    if 'demo_projects' in data:
        for i, repo in enumerate(data['demo_projects']):
            repo_errors = validate_repository(repo, f"Demo project '{repo.get('name', f'#{i}')}'")
            errors.extend(repo_errors)
    
    # Validate projects_using_generators
    if 'projects_using_generators' in data:
        for i, repo in enumerate(data['projects_using_generators']):
            repo_errors = validate_repository(repo, f"Project using generators '{repo.get('name', f'#{i}')}'")
            errors.extend(repo_errors)
    
    # Check for duplicates
    duplicate_errors = check_duplicates(data)
    errors.extend(duplicate_errors)
    
    return errors


def main():
    """Main entry point."""
    data_file = Path(__file__).parent.parent / "data" / "repositories.yml"
    
    print(f"Validating {data_file}...")
    
    # Load YAML
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing error: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ File not found: {data_file}")
        sys.exit(1)
    
    # Validate
    errors = validate_data(data)
    
    if errors:
        print(f"\n❌ Validation failed with {len(errors)} error(s):\n")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("✓ Validation passed!")
        
        # Print stats
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


if __name__ == '__main__':
    main()
