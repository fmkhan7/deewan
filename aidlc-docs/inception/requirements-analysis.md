# Requirements Analysis - Deewan-e-Ekta

**Date**: 2026-04-26
**Project**: Urdu Poetry Collection Website (دیوان)
**Phase**: INCEPTION - Requirements Analysis

---

## 1. Project Overview

### Project Name
**Deewan-e-Ekta** (دیوان - یکتا)

### Project Type
Static website for publishing Urdu poetry collections

### Core Purpose
A web platform to publish and browse Urdu poetry (ghazals, nazms) with full Urdu script support (RTL, Nastaliq fonts). Designed to support multiple poets' collections in the future.

---

## 2. Functional Requirements

### FR-1: Poetry Display
- **FR-1.1**: Display ghazals with their couplets (اشعار)
- **FR-1.2**: Display nazms (standalone poems)
- **FR-1.3**: Show poet information and collection metadata
- **FR-1.4**: Proper Urdu text rendering with Nastaliq/Jameel Nori fonts

### FR-2: Navigation & Browsing
- **FR-2.1**: Browse by collection (دیوان)
- **FR-2.2**: Browse by poetry type (غزل, نظم)
- **FR-2.3**: Index view showing all ghazals/nazms in a collection
- **FR-2.4**: Table of contents for quick navigation

### FR-3: Search
- **FR-3.1**: Search poetry by title/meters (بحر)
- **FR-3.2**: Search couplets by keyword/phrase
- **FR-3.3**: Filter by poet (future-proofing)

### FR-4: Content Management
- **FR-4.1**: Accept Inpage .inp files for poetry content
- **FR-4.2**: Convert .inp to structured data (JSON)
- **FR-4.3**: Support manual JSON input as alternative

---

## 3. Non-Functional Requirements

### NFR-1: Urdu Script Support
- **NFR-1.1**: Full right-to-left (RTL) layout support
- **NFR-1.2**: Use Nastaliq-style Urdu fonts (Jameel Nori Nastaliq)
- **NFR-1.3**: Proper character joining (Arabic script rendering)
- **NFR-1.4**: Responsive Urdu text sizing

### NFR-2: Performance
- **NFR-2.1**: Page load time < 2 seconds
- **NFR-2.2**: Static site generation for fast loading
- **NFR-2.3**: Minimal JavaScript for core functionality

### NFR-3: Accessibility
- **NFR-3.1**: Proper lang="ur" attribute on Urdu content
- **NFR-3.2**: Keyboard navigation support
- **NFR-3.3**: Sufficient color contrast

### NFR-4: Maintainability
- **NFR-4.1**: Clean separation of content (JSON) from presentation (HTML/CSS)
- **NFR-4.2**: Modular component structure
- **NFR-4.3**: Documented content schema

### NFR-5: Extensibility
- **NFR-5.1**: Data model supports multiple poets
- **NFR-5.2**: Easy to add new collections
- **NFR-5.3**: Theme customization support

---

## 4. Technical Stack Decision

| Component | Decision | Rationale |
|-----------|----------|------------|
| **Framework** | 11ty (Eleventy) | Static site generator, GitHub Pages compatible |
| **Hosting** | GitHub Pages (default) | Free, supports custom domain |
| **Content Format** | JSON | Human-readable, easy to maintain |
| **Urdu Fonts** | Jameel Nori Nastaliq | Free, high-quality Nastaliq font |
| **Styling** | CSS with CSS Variables | Lightweight, customizable |

---

## 5. Data Model

### Collection (دیوان)
```json
{
  "id": "deewan-e-ekta",
  "title": "دیوان یکتا",
  "titleEn": "Deewan-e-Ekta",
  "poet": {
    "id": "ekta",
    "name": "یکتا",
    "nameEn": "Ekta"
  },
  "description": "Collection description",
  "ghazals": [...],
  "nazms": [...]
}
```

### Ghazal (غزل)
```json
{
  "id": "ghazal-id",
  "title": "غزل کا عنوان",
  "meter": "بحر",
  "couplets": [
    {
      "line1": "پہلی شاعری",
      "line2": "دوسری شاعری",
      "translation": "English translation (optional)"
    }
  ]
}
```

---

## 6. Out of Scope

The following are explicitly NOT in scope for v1:
- User accounts and authentication
- Favorites/bookmarks
- Comments and annotations
- Social sharing
- Admin panel for content management
- Database-driven dynamic content

---

## 7. Acceptance Criteria

1. ✅ Website builds successfully with 11ty
2. ✅ Home page displays collection info
3. ✅ Ghazals list page shows all ghazals in collection
4. ✅ Individual ghazal page displays all couplets
5. ✅ Nazms list page shows all nazms
6. ✅ Individual nazm page displays the poem
7. ✅ Urdu text renders correctly with proper RTL
8. ✅ Nastaliq font loads and displays
9. ✅ Search returns relevant results
10. ✅ Site is responsive on mobile devices
11. ✅ Deploys successfully to GitHub Pages

---

## 8. Questions for Future Phases

- [ ] Confirm Inpage file conversion approach
- [ ] Finalize color scheme for modern literary aesthetic
- [ ] Decide on custom domain requirements
- [ ] Determine SEO requirements for Urdu content