# Functional Design Plan - Unit 2: Core Website Structure

**Date**: 2026-04-26
**Unit**: 2 - Core Website Structure
**Phase**: CONSTRUCTION - Functional Design

---

## 1. Unit Context

### Purpose
Create the core website structure with all necessary pages, templates, and components for the Urdu poetry collection.

### Scope
- Ghazals listing and detail pages
- Nazms listing and detail pages
- Navigation components
- Responsive design

### Dependencies
- Unit 1: Project Setup (complete)

---

## 2. Functional Design Steps

### Step 1: Page Design
- [ ] Design ghazals index page
- [ ] Design ghazal detail page template
- [ ] Design nazms index page
- [ ] Design nazm detail page template

### Step 2: Component Design
- [ ] Design header component
- [ ] Design footer component
- [ ] Design navigation component
- [ ] Design poetry display component (couplet/verse)

### Step 3: Data Model Design
- [ ] Define ghazal JSON structure
- [ ] Define nazm JSON structure
- [ ] Design collection aggregation

### Step 4: Generate Functional Design Artifacts
- [ ] Create `aidlc-docs/construction/unit-2-core-structure/functional-design/page-designs.md`
- [ ] Create `aidlc-docs/construction/unit-2-core-structure/functional-design/components.md`
- [ ] Create `aidlc-docs/construction/unit-2-core-structure/functional-design/data-model.md`

---

## 3. Questions for Clarification

[Answer]: 

**Q1**: Should the ghazals/nazms be on separate pages or all on one page with anchor links?

- A) Separate pages - better for SEO and sharing
- B) Single page with anchors - simpler navigation
- C) Hybrid - index on one page, detail on separate pages

---

## 4. Acceptance Criteria

- [ ] Ghazals index page displays list of ghazals
- [ ] Ghazal detail page shows all couplets
- [ ] Nazms index page displays list of nazms
- [ ] Nazm detail page shows all verses
- [ ] Navigation works between all pages
- [ ] Responsive design works on mobile