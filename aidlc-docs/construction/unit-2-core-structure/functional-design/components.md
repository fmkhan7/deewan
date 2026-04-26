# Components - Unit 2: Core Website Structure

**Date**: 2026-04-26
**Unit**: 2 - Core Website Structure
**Phase**: CONSTRUCTION - Functional Design

---

## 1. Overview

This document defines reusable components for the poetry website.

---

## 2. Component List

| Component | File | Purpose |
|-----------|------|---------|
| Header | `header.njk` | Site header with title and navigation |
| Footer | `footer.njk` | Site footer with copyright |
| Poetry Card | `poetry-card.njk` | Display ghazal/nazm in lists |
| Couplet | `couplet.njk` | Display a ghazal couplet |
| Verse | `verse.njk` | Display a nazm verse |
| Meter Badge | `meter-badge.njk` | Display poetry meter (بحر) |

---

## 3. Component Designs

### 3.1 Header Component (`src/_includes/components/header.njk`)

```njk
<header class="site-header">
  <div class="container">
    <h1 class="site-title">
      <a href="/">{{ site.title }}</a>
    </h1>
    <nav class="site-nav">
      <a href="/">Home</a>
      <a href="/ghazals/">غزلیں</a>
      <a href="/nazms/">نظمیں</a>
    </nav>
  </div>
</header>
```

### 3.2 Footer Component (`src/_includes/components/footer.njk`)

```njk
<footer class="site-footer">
  <div class="container">
    <p>&copy; {{ site.author }} — {{ site.titleEn }}</p>
  </div>
</footer>
```

### 3.3 Poetry Card Component (`src/_includes/components/poetry-card.njk`)

```njk
<article class="poetry-card">
  <h3>
    <a href="{{ url }}">{{ title }}</a>
  </h3>
  {% if meter %}
  <span class="meter-badge">{{ meter }}</span>
  {% endif %}
</article>
```

### 3.4 Couplet Component (`src/_includes/components/couplet.njk`)

```njk
<div class="couplet">
  <p class="line">{{ line1 }}</p>
  <p class="line">{{ line2 }}</p>
</div>
```

### 3.5 Meter Badge Component (`src/_includes/components/meter-badge.njk`)

```njk
<span class="meter">
  <span class="label">بحر:</span>
  <span class="value">{{ meter }}</span>
</span>
```

---

## 4. CSS Requirements

### Poetry Card Styles

```css
.poetry-card {
  padding: var(--spacing-md);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  transition: transform 0.2s;
}

.poetry-card:hover {
  transform: translateY(-2px);
}
```

### Couplet Styles

```css
.couplet {
  padding: var(--spacing-lg) 0;
  border-bottom: 1px solid var(--color-border);
}

.couplet .line {
  font-family: var(--font-urdu);
  font-size: 1.5rem;
  line-height: 2;
  text-align: center;
}
```

### Meter Badge Styles

```css
.meter-badge {
  display: inline-block;
  background: var(--color-primary);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
}
```

---

## 5. Acceptance Criteria

- [ ] Header component renders with navigation
- [ ] Footer component renders with copyright
- [ ] Poetry card displays title and meter
- [ ] Couplet displays two lines properly
- [ ] All components are reusable
- [ ] CSS styles applied correctly