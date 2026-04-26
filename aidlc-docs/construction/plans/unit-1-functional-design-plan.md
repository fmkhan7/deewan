# Functional Design Plan - Unit 1: Project Setup & Infrastructure

**Date**: 2026-04-26
**Unit**: 1 - Project Setup & Infrastructure
**Phase**: CONSTRUCTION - Functional Design

---

## 1. Unit Context

### Purpose
Set up the foundational project structure for the Urdu poetry collection website using 11ty (Eleventy) static site generator.

### Scope
- 11ty project initialization
- Package.json configuration
- Folder structure creation
- Build configuration
- GitHub Actions for CI/CD

### Dependencies
- None (this is the first unit)

---

## 2. Functional Design Steps

### Step 1: Analyze Requirements
- [ ] Review requirements from `aidlc-docs/inception/requirements-analysis.md`
- [ ] Identify infrastructure needs for Urdu content
- [ ] Map hosting requirements (GitHub Pages)

### Step 2: Project Structure Design
- [ ] Define 11ty directory structure
- [ ] Design source vs output separation
- [ ] Plan content organization (collections, layouts, includes)
- [ ] Design data folder structure for JSON content

### Step 3: Build System Design
- [ ] Design npm scripts (build, serve, clean)
- [ ] Plan 11ty configuration (passthroughs, filters, plugins)
- [ ] Design asset pipeline (CSS, fonts, images)

### Step 4: Deployment Infrastructure Design
- [ ] Design GitHub Actions workflow
- [ ] Plan GitHub Pages deployment configuration
- [ ] Design custom domain support (future)

### Step 5: Generate Functional Design Artifacts
- [ ] Create `aidlc-docs/construction/unit-1-project-setup/functional-design/project-structure.md`
- [ ] Create `aidlc-docs/construction/unit-1-project-setup/functional-design/build-configuration.md`
- [ ] Create `aidlc-docs/construction/unit-1-project-setup/functional-design/deployment-config.md`

---

## 3. Questions for Clarification

[Answer]: 

**Q1**: Should the 11ty project be in the root of the repo (`/`) or in a subdirectory (e.g., `/website/`)?

- A) Root directory - simpler for GitHub Pages deployment
- B) Subdirectory (`/website/`) - keeps source separate from docs
- C) Other - specify your preference

---

## 4. Acceptance Criteria

- [ ] Package.json with 11ty dependencies
- [ ] 11ty configuration file
- [ ] Proper folder structure created
- [ ] Build script works (`npm run build`)
- [ ] Development server works (`npm run serve`)
- [ ] GitHub Actions workflow created
- [ ] Site builds successfully