# Build Configuration Design - Unit 1: Project Setup

**Date**: 2026-04-26
**Unit**: 1 - Project Setup & Infrastructure
**Phase**: CONSTRUCTION - Functional Design

---

## 1. Overview

This document defines the build system configuration for the 11ty project.

---

## 2. Package.json Scripts

```json
{
  "scripts": {
    "start": "eleventy --serve",
    "build": "eleventy",
    "clean": "rm -rf _site",
    "debug": "DEBUG=* eleventy"
  }
}
```

---

## 3. Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `@11ty/eleventy` | ^3.0 | Static site generator |
| `@11ty/eleventy-img` | ^5.0 | Image processing (future) |
| `luxon` | ^3.4 | Date formatting |

---

## 4. 11ty Configuration (.eleventy.js)

### Basic Setup
```javascript
module.exports = function(eleventyConfig) {
  // Passthrough copies
  eleventyConfig.addPassthroughCopy("src/assets");
  
  // Watch for changes
  eleventyConfig.addWatchTarget("src/assets");
  
  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data"
    }
  };
};
```

### Filters to Implement
- `urduDate(date)` - Format date in Urdu numerals
- `htmlminFilter(html)` - Minify HTML output

### Plugins
- RSS plugin (future consideration)
- Navigation plugin (future consideration)

---

## 5. Asset Pipeline

### CSS Processing
- No build step required (plain CSS)
- Use CSS variables for theming
- RTL-specific styles in same file

### Font Handling
- Download Jameel Nori Nastaliq font
- Place in `src/assets/fonts/`
- Configure as passthrough

### JavaScript
- Minimal JS for search functionality
- No build step required for v1

---

## 6. GitHub Actions Build

### Workflow Triggers
- Push to `main` branch
- Pull request to `main` branch

### Build Steps
```yaml
- name: Install Node.js
  uses: actions/setup-node@v4
  
- name: Install dependencies
  run: npm ci
  
- name: Build site
  run: npm run build
  
- name: Deploy to GitHub Pages
  uses: peaceiris/actions-gh-pages@v3
```

---

## 7. Acceptance Criteria

- [ ] `npm run build` generates HTML in `_site/`
- [ ] `npm run serve` starts dev server
- [ ] Assets are copied to `_site/`
- [ ] GitHub Actions builds successfully
- [ ] No build errors or warnings