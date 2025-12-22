# Testing the Refactored Structure

This document demonstrates how to use the new data-driven structure.

## Quick Test

1. **Validate the current data:**
   ```bash
   python scripts/validate_data.py
   ```

2. **Render the README:**
   ```bash
   python scripts/render_readme.py
   ```

3. **Add a new repository** (edit `data/repositories.yml`):
   ```yaml
   categories:
     your-category:
       repositories:
       - name: NewGenerator
         url: https://github.com/user/repo
         description: Description of the generator
   ```

4. **Validate and render:**
   ```bash
   python scripts/validate_data.py && python scripts/render_readme.py
   ```

## Automated Workflow

When you push changes to `data/repositories.yml`:

1. GitHub Actions runs validation
2. If validation passes, README.md is automatically regenerated
3. Changes are committed back to the repository

## Local Development

Install dependencies:
```bash
pip install -r requirements.txt
```

Run validation:
```bash
python scripts/validate_data.py
```

Render README:
```bash
python scripts/render_readme.py
```
