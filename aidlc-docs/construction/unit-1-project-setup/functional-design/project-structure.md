# Project Structure Design - Unit 1: Project Setup

**Date**: 2026-04-26
**Unit**: 1 - Project Setup & Infrastructure
**Phase**: CONSTRUCTION - Functional Design

---

## 1. Overview

This document defines the 11ty project structure for the Deewan-e-Ekta Urdu poetry website.

---

## 2. Directory Structure

```
/
├── .eleventy.js           # 11ty configuration
├── package.json           # Node.js dependencies
├── package-lock.json     # Locked dependencies
├── .gitignore             # Git ignore patterns
├── README.md              # Project documentation
├── .github/
│   └── workflows/
│       └── deploy.yml    # GitHub Actions workflow
├── src/
│   ├── _data/            # 11ty data files
│   │   └── site.json     # Site metadata
│   ├── _includes/
│   │   ├── layouts/      # Page layouts
│   │   │   └── base.njk  # Base HTML template
│   │   └── components/  # Reusable components
│   ├── assets/
│   │   ├── css/          # Stylesheets
│   │   ├── fonts/        # Urdu fonts
│   │   └── js/           # JavaScript files
│   ├── content/          # Poetry content (JSON)
│   │   ├── ghazals/      # Ghazal collections
│   │   └── nazms/        # Nazm collections
│   └── pages/            # Static pages
│       └── index.njk     # Home page
└── _site/                # Build output (generated)
```

---

## 3. Key Design Decisions

### 3.1 Root Project Location
- **Decision**: Project lives at repository root `/`
- **Rationale**: Simplest for GitHub Pages deployment (`/docs/` or `main` branch)

### 3.2 Source vs Output
- **Source**: `/src/` directory contains all input files
- **Output**: `/_site/` directory contains generated HTML
- **Rationale**: Clean separation, easy to configure 11ty

### 3.3 Content Organization
- **Poetry data**: Stored as JSON files in `/src/content/`
- **Ghazals**: `/src/content/ghazals/` - one JSON file per ghazal
- **Nazms**: `/src/content/nazms/` - one JSON file per nazm
- **Rationale**: Human-editable, version control friendly

### 3.4 Templates
- **Engine**: Nunjucks (.njk) - powerful templating for Urdu content
- **Layouts**: Base layout + specialized page layouts
- **Components**: Reusable header, footer, navigation

---

## 4. File Purposes

| Path | Purpose |
|------|----------|
| `.eleventy.js` | 11ty configuration, passthroughs, filters |
| `package.json` | npm scripts: `build`, `serve`, `clean` |
| `src/_data/site.json` | Site title, description, author |
| `src/_includes/layouts/base.njk` | Base HTML with `<html lang="ur">` |
| `src/assets/css/` | CSS with RTL support, Urdu fonts |
| `src/assets/fonts/` | Jameel Nori Nastaliq font files |
| `src/content/ghazals/*.json` | Ghazal data (title, meter, couplets) |
| `src/content/nazms/*.json` | Nazm data (title, meter, verses) |

---

## 5. 11ty Configuration Requirements

### Passthroughs
```javascript
eleventyConfig.addPassthroughCopy("src/assets");
```

### Collections
- Ghazals collection: `ghazals`
- Nazms collection: `nazms`

### Filters
- `urduDate`: Format dates in Urdu script
- `reverse`: Reverse array for display

---

## 6. Acceptance Criteria

- [ ] Directory structure matches this design
- [ ] All folders created under `/src/`
- [ ] 11ty can process templates from `/src/`
- [ ] Assets (CSS, fonts, JS) are copied to output
- [ ] Content JSON files are loadable as 11ty collections