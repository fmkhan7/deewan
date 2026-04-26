# Data Model - Unit 2: Core Website Structure

**Date**: 2026-04-26
**Unit**: 2 - Core Website Structure
**Phase**: CONSTRUCTION - Functional Design

---

## 1. Overview

This document defines the JSON data model for storing poetry content in the 11ty site.

---

## 2. Ghazal Data Model

### 2.1 Single Ghazal JSON (`src/content/ghazals/{slug}.json`)

```json
{
  "title": "غزل کا عنوان",
  "slug": "ghazal-slug",
  "meter": "بحر میزان",
  "couplets": [
    {
      "line1": "پہلی شاعری - مصرعہ اول",
      "line2": "دوسری شاعری - مصرعہ دوم",
      "translation": "English translation (optional)"
    },
    {
      "line1": "تیسری شاعری",
      "line2": "چوتھی شاعری"
    }
  ],
  "description": "Optional description or context",
  "tags": ["love", "nature"]
}
```

### 2.2 Field Definitions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | String | Yes | Ghazal title in Urdu |
| `slug` | String | Yes | URL-friendly identifier |
| `meter` | String | No | Poetic meter (بحر) |
| `couplets` | Array | Yes | Array of couplet objects |
| `couplets[].line1` | String | Yes | First line of couplet |
| `couplets[].line2` | String | Yes | Second line of couplet |
| `couplets[].translation` | String | No | English translation |
| `description` | String | No | Additional context |
| `tags` | Array | No | Categorization tags |

---

## 3. Nazm Data Model

### 3.1 Single Nazm JSON (`src/content/nazms/{slug}.json`)

```json
{
  "title": "نظم کا عنوان",
  "slug": "nazm-slug",
  "meter": "بحر",
  "verses": [
    "پہلی شاعری",
    "دوسری شاعری",
    "تیسری شاعری"
  ],
  "description": "Optional description",
  "tags": ["patriotic", "nature"]
}
```

### 3.2 Field Definitions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | String | Yes | Nazm title in Urdu |
| `slug` | String | Yes | URL-friendly identifier |
| `meter` | String | No | Poetic meter (بحر) |
| `verses` | Array | Yes | Array of verse strings |
| `description` | String | No | Additional context |
| `tags` | Array | No | Categorization tags |

---

## 4. 11ty Collection Configuration

### 4.1 Ghazals Collection (`.eleventy.js`)

```javascript
eleventyConfig.addCollection("ghazals", function(collectionApi) {
  return collectionApi.getFilteredByGlob("src/content/ghazals/*.json");
});
```

### 4.2 Nazms Collection (`.eleventy.js`)

```javascript
eleventyConfig.addCollection("nazms", function(collectionApi) {
  return collectionApi.getFilteredByGlob("src/content/nazms/*.json");
});
```

---

## 5. Sample Data

### 5.1 Sample Ghazal

```json
{
  "title": "پہلی غزل",
  "slug": "pehla-ghazal",
  "meter": "ہزجِ مثمن محذوف",
  "couplets": [
    {
      "line1": "دل پہ جا کے تمہاری یاد آئی",
      "line2": "ہنسیں گے ہم بھی کیا کیا نہ کہائی"
    },
    {
      "line1": "تم ہو تو جہاں کی زینت ہو",
      "line2": "یہ جہاں تمہاری محنت ہو"
    }
  ]
}
```

### 5.2 Sample Nazm

```json
{
  "title": "پہلی نظم",
  "slug": "pehla-nazm",
  "meter": "م自由的",
  "verses": [
    "اے مرے دل کے چراغ",
    "تجھے سلام ہے",
    "تجھے خوب سے خوب سلام ہے"
  ]
}
```

---

## 6. Acceptance Criteria

- [ ] Ghazal JSON schema is valid
- [ ] Nazm JSON schema is valid
- [ ] 11ty collections load ghazals correctly
- [ ] 11ty collections load nazms correctly
- [ ] Sample data can be loaded and displayed
- [ ] Slug generation works correctly