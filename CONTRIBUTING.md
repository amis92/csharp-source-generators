# Contributing

This repository uses a data-driven approach to maintain the list of C# Source Generators.

## Structure

- **`data/repositories.yml`** - The single source of truth containing all repository information
- **`scripts/render_readme.py`** - Python script that generates README.md from the YAML data
- **`scripts/validate_data.py`** - Validation script to ensure data quality
- **`scripts/extract_data.py`** - Helper script to extract data from existing README (used during migration)

## Making Changes

### Adding a New Repository

1. Edit `data/repositories.yml`
2. Add your repository under the appropriate category:

```yaml
categories:
  your-category:
    repositories:
    - name: YourGenerator
      url: https://github.com/yourusername/yourgenerator
      description: Brief description of what your generator does
```

3. Run validation: `python scripts/validate_data.py`
4. Render README: `python scripts/render_readme.py`
5. Commit both `data/repositories.yml` and `README.md`

### Adding a New Category

1. Edit `data/repositories.yml`
2. Add your category:

```yaml
categories:
  your-new-category:
    name: Your New Category Name
    repositories:
    - name: FirstRepo
      url: https://github.com/...
      description: ...
```

3. Update the table of contents in the YAML file if needed
4. Follow steps 3-5 from "Adding a New Repository"

## Automation

The repository includes a GitHub Actions workflow (`.github/workflows/render-readme.yml`) that:

- **On Push**: Validates data and auto-generates README.md
- **On Pull Requests**: Validates data and comments if README needs regeneration

## Validation

The validation script checks for:

- Valid GitHub URLs
- Required fields (name, url)
- Duplicate repositories
- Empty descriptions
- Proper YAML structure

Run `python scripts/validate_data.py` before committing to ensure data quality.
