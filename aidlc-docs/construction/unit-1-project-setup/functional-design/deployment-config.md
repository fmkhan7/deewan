# Deployment Configuration Design - Unit 1: Project Setup

**Date**: 2026-04-26
**Unit**: 1 - Project Setup & Infrastructure
**Phase**: CONSTRUCTION - Functional Design

---

## 1. Overview

This document defines the deployment configuration for GitHub Pages.

---

## 2. Deployment Target

| Setting | Value |
|---------|-------|
| **Host** | GitHub Pages |
| **Branch** | `gh-pages` |
| **Source** | `/_site/` directory |
| **Domain** | Custom (future) |

---

## 3. GitHub Actions Workflow

### File: `.github/workflows/deploy.yml`

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Build site
        run: npm run build
        
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_site
```

---

## 4. GitHub Pages Configuration

### Option 1: Branch-based (Recommended)
- Push build output to `gh-pages` branch
- GitHub Pages serves from `/` of that branch

### Option 2: Folder-based
- Use `/docs` folder on `main` branch
- Configure in repository settings

---

## 5. Custom Domain (Future)

When ready for custom domain:
1. Add CNAME file to `src/assets/`
2. Configure DNS at domain provider
3. Enable HTTPS (automatic with GitHub Pages)

---

## 6. Acceptance Criteria

- [ ] GitHub Actions workflow file created
- [ ] Workflow triggers on push to main
- [ ] Build step completes successfully
- [ ] Deploy step publishes to GitHub Pages
- [ ] Site accessible at `{user}.github.io/{repo}/`