# Page Designs - Unit 2: Core Website Structure

**Date**: 2026-04-26
**Unit**: 2 - Core Website Structure
**Phase**: CONSTRUCTION - Functional Design

---

## 1. Overview

This document defines the page structure for the Deewan-e-Ekta website using the Hybrid approach (index on one page, detail on separate pages).

---

## 2. Page Structure

### 2.1 Pages to Create

| Page | Path | Purpose |
|------|------|---------|
| Home | `/` | Landing page with collection overview |
| Ghazals Index | `/ghazals/` | List of all ghazals |
| Ghazal Detail | `/ghazals/{slug}/` | Individual ghazal with couplets |
| Nazms Index | `/nazms/` | List of all nazms |
| Nazm Detail | `/nazms/{slug}/` | Individual nazm with verses |

### 2.2 URL Structure

```
/
├── ghazals/
│   ├── index.html      # Ghazals listing
│   └── {slug}/         # Individual ghazal
└── nazms/
    ├── index.html      # Nazms listing
    └── {slug}/         # Individual nazm
```

---

## 3. Page Templates

### 3.1 Ghazals Index Page (`src/ghazals/index.njk`)

```njk
---
layout: layouts/base.njk
title: غزلیں - Ghazals
---

<h1>غزلیں</h1>
<ul class="poetry-list">
{% for ghazal in collections.ghazals %}
  <li>
    <a href="/ghazals/{{ ghazal.slug }}/">
      {{ ghazal.data.title }}
    </a>
    <span class="meter">{{ ghazal.data.meter }}</span>
  </li>
{% endfor %}
</ul>
```

### 3.2 Ghazal Detail Page (`src/ghazals/ghazal.njk`)

```njk
---
layout: layouts/base.njk
---

<article class="ghazal">
  <header>
    <h1>{{ title }}</h1>
    <p class="meter">بحر: {{ meter }}</p>
  </header>
  
  <div class="couplets">
  {% for couplet in couplets %}
    <div class="couplet">
      <p class="line">{{ couplet.line1 }}</p>
      <p class="line">{{ couplet.line2 }}</p>
    </div>
  {% endfor %}
  </div>
</article>
```

### 3.3 Nazms Index Page (`src/nazms/index.njk`)

Similar structure to ghazals index, but for nazms.

### 3.4 Nazm Detail Page (`src/nazms/nazm.njk`)

```njk
---
layout: layouts/base.njk
---

<article class="nazm">
  <header>
    <h1>{{ title }}</h1>
    <p class="meter">بحر: {{ meter }}</p>
  </header>
  
  <div class="verses">
  {% for verse in verses %}
    <p class="verse">{{ verse }}</p>
  {% endfor %}
  </div>
</article>
```

---

## 4. Data Flow

### 4.1 Ghazal Data Flow

```
src/content/ghazals/*.json
    ↓ (11ty collections)
collections.ghazals
    ↓ (template)
src/ghazals/index.njk → /ghazals/index.html
src/ghazals/ghazal.njk → /ghazals/{slug}/index.html
```

### 4.2 Nazm Data Flow

```
src/content/nazms/*.json
    ↓ (11ty collections)
collections.nazms
    ↓ (template)
src/nazms/index.njk → /nazms/index.html
src/nazms/nazm.njk → /nazms/{slug}/index.html
```

---

## 5. Template Organization

```
src/
├── ghazals/
│   ├── index.njk      # Ghazals listing
│   └── ghazal.njk     # Ghazal detail template
├── nazms/
│   ├── index.njk      # Nazms listing
│   └── nazm.njk       # Nazm detail template
```

---

## 6. Acceptance Criteria

- [ ] `/ghazals/` displays list of all ghazals
- [ ] Each ghazal has its own detail page at `/ghazals/{slug}/`
- [ ] `/nazms/` displays list of all nazms
- [ ] Each nazm has its own detail page at `/nazms/{slug}/`
- [ ] Navigation links work correctly
- [ ] 11ty processes all templates without errors