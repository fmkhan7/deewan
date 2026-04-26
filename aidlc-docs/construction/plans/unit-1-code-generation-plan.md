# Code Generation Plan - Unit 1: Project Setup

**Date**: 2026-04-26
**Unit**: 1 - Project Setup & Infrastructure
**Phase**: CONSTRUCTION - Code Generation

---

## 1. Unit Context

### Purpose
Set up the foundational 11ty project structure for the Urdu poetry collection website.

### Dependencies
- None (first unit)

### Stories Covered
- S1: Project initialization with 11ty
- S2: Build system configuration
- S3: GitHub Pages deployment

---

## 2. Code Generation Steps

### Step 1: Create Package.json
- [ ] Create `package.json` with 11ty dependencies
- [ ] Add npm scripts (build, serve, clean)
- [ ] Include proper metadata

### Step 2: Create 11ty Configuration
- [ ] Create `.eleventy.js` configuration file
- [ ] Configure input/output directories
- [ ] Add passthrough copies for assets
- [ ] Add watch targets

### Step 3: Create Directory Structure
- [ ] Create `src/` directory
- [ ] Create `src/_data/`, `src/_includes/`, `src/assets/`, `src/content/`, `src/pages/`
- [ ] Create subdirectories for assets (css, fonts, js)

### Step 4: Create Base Templates
- [ ] Create `src/_includes/layouts/base.njk` - base HTML template
- [ ] Include Urdu lang attribute
- [ ] Include meta tags, CSS links

### Step 5: Create Site Data
- [ ] Create `src/_data/site.json` - site metadata
- [ ] Include title, description, author

### Step 6: Create Home Page
- [ ] Create `src/pages/index.njk` - home page template
- [ ] Link to base layout

### Step 7: Create GitHub Actions Workflow
- [ ] Create `.github/workflows/deploy.yml`
- [ ] Configure build and deploy steps

### Step 8: Create Git Ignore
- [ ] Create `.gitignore` - ignore _site, node_modules

### Step 9: Test Build
- [ ] Run `npm install`
- [ ] Run `npm run build`
- [ ] Verify `_site/` directory created

---

## 3. File List

| File | Path | Description |
|------|------|-------------|
| package.json | `/package.json` | Node.js dependencies |
| .eleventy.js | `/.eleventy.js` | 11ty configuration |
| base.njk | `/src/_includes/layouts/base.njk` | Base HTML template |
| site.json | `/src/_data/site.json` | Site metadata |
| index.njk | `/src/pages/index.njk` | Home page |
| deploy.yml | `/.github/workflows/deploy.yml` | GitHub Actions |
| .gitignore | `/.gitignore` | Git ignore patterns |

---

## 4. Acceptance Criteria

- [ ] `npm install` completes without errors
- [ ] `npm run build` generates HTML files
- [ ] `_site/` directory contains built site
- [ ] Development server starts with `npm run serve`
- [ ] GitHub Actions workflow is valid YAML