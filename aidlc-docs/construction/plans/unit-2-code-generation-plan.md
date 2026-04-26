# Code Generation Plan - Unit 2: Core Website Structure

**Date**: 2026-04-26
**Unit**: 2 - Core Website Structure
**Phase**: CONSTRUCTION - Code Generation

---

## 1. Unit Context

### Purpose
Create the core website structure with pages, templates, and components for displaying ghazals and nazms.

### Dependencies
- Unit 1: Project Setup (complete)

### Stories Covered
- S4: Ghazals index page with list
- S5: Ghazal detail page with couplets
- S6: Nazms index page with list
- S7: Nazm detail page with verses
- S8: Navigation between pages

---

## 2. Code Generation Steps

### Step 1: Update 11ty Configuration
- [ ] Add ghazals collection
- [ ] Add nazms collection
- [ ] Configure pagination for detail pages

### Step 2: Create Ghazals Directory and Templates
- [ ] Create `src/ghazals/` directory
- [ ] Create `src/ghazals/index.njk` - ghazals listing
- [ ] Create `src/ghazals/ghazal.njk` - ghazal detail template

### Step 3: Create Nazms Directory and Templates
- [ ] Create `src/nazms/` directory
- [ ] Create `src/nazms/index.njk` - nazms listing
- [ ] Create `src/nazms/nazm.njk` - nazm detail template

### Step 4: Create Reusable Components
- [ ] Create `src/_includes/components/header.njk`
- [ ] Create `src/_includes/components/footer.njk`
- [ ] Create `src/_includes/components/couplet.njk`
- [ ] Create `src/_includes/components/verse.njk`

### Step 5: Create Sample Content
- [ ] Create sample ghazal JSON in `src/content/ghazals/`
- [ ] Create sample nazm JSON in `src/content/nazms/`

### Step 6: Update Base Layout
- [ ] Update `src/_includes/layouts/base.njk` to use components

### Step 7: Add Poetry-Specific CSS
- [ ] Add styles for poetry cards, couplets, verses
- [ ] Add styles for meter badges

### Step 8: Test Build
- [ ] Run `npm run build`
- [ ] Verify all pages generate
- [ ] Verify collections work

---

## 3. File List

| File | Path | Description |
|------|------|-------------|
| .eleventy.js | `/.eleventy.js` | Updated with collections |
| index.njk | `/src/ghazals/index.njk` | Ghazals listing |
| ghazal.njk | `/src/ghazals/ghazal.njk` | Ghazal detail |
| index.njk | `/src/nazms/index.njk` | Nazms listing |
| nazm.njk | `/src/nazms/nazm.njk` | Nazm detail |
| header.njk | `/src/_includes/components/header.njk` | Header component |
| footer.njk | `/src/_includes/components/footer.njk` | Footer component |
| couplet.njk | `/src/_includes/components/couplet.njk` | Couplet component |
| verse.njk | `/src/_includes/components/verse.njk` | Verse component |
| sample.json | `/src/content/ghazals/sample.json` | Sample ghazal |
| sample.json | `/src/content/nazms/sample.json` | Sample nazm |
| style.css | `/src/assets/css/style.css` | Updated with poetry styles |

---

## 4. Acceptance Criteria

- [ ] `/ghazals/` page shows list of ghazals
- [ ] Each ghazal has detail page at `/ghazals/{slug}/`
- [ ] `/nazms/` page shows list of nazms
- [ ] Each nazm has detail page at `/nazms/{slug}/`
- [ ] Navigation works between all pages
- [ ] Sample content displays correctly
- [ ] Build completes without errors