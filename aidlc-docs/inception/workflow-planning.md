# Workflow Planning - Deewan-e-Ekta

**Date**: 2026-04-26
**Project**: Urdu Poetry Collection Website
**Phase**: INCEPTION - Workflow Planning

---

## 1. Executive Summary

**Project**: Deewan-e-Ekta (دیوان یکتا) - Urdu Poetry Collection Website
**Type**: Static website (Greenfield)
**Complexity**: Low-Medium
**Risk Level**: Low

---

## 2. Scope Analysis

### 2.1 What We're Building
A static website for publishing Urdu poetry with:
- Full Urdu script support (RTL, Nastaliq fonts)
- Browse ghazals and nazms by collection
- Search functionality
- Modern literary aesthetic design
- Support for future multi-poet expansion

### 2.2 What's NOT in Scope
- User accounts/authentication
- Database-driven content
- Admin panel
- Comments/social features
- Dynamic content management

### 2.3 Impact Areas

| Area | Impact | Notes |
|------|--------|-------|
| **User-facing** | High | New UI for poetry display |
| **Structural** | Medium | Static site architecture |
| **Data Model** | Low | JSON-based content |
| **API** | None | No backend APIs |
| **NFR** | Medium | Urdu support, performance |

---

## 3. Execution Plan

### Phase 1: INCEPTION (Complete)
- [x] Workspace Detection
- [x] Requirements Analysis
- [x] Workflow Planning ← **You are here**

### Phase 2: CONSTRUCTION

#### Unit 1: Project Setup & Infrastructure
| Stage | Status | Notes |
|-------|--------|-------|
| Infrastructure Design | Pending | 11ty setup, folder structure |
| Code Generation | Pending | Package.json, config files |
| Build & Test | Pending | Verify build works |

#### Unit 2: Core Website Structure
| Stage | Status | Notes |
|-------|--------|-------|
| Functional Design | Pending | Pages, templates, components |
| Code Generation | Pending | HTML layouts, CSS |
| Build & Test | Pending | Verify all pages render |

#### Unit 3: Urdu Support & Styling
| Stage | Status | Notes |
|-------|--------|-------|
| Functional Design | Pending | Urdu fonts, RTL layout |
| Code Generation | Pending | Font loading, CSS variables |
| Build & Test | Pending | Urdu rendering verification |

#### Unit 4: Content & Data Model
| Stage | Status | Notes |
|-------|--------|-------|
| Functional Design | Pending | JSON schema for poetry |
| Code Generation | Pending | Sample content, converters |
| Build & Test | Pending | Content validation |

#### Unit 5: Search Functionality
| Stage | Status | Notes |
|-------|--------|-------|
| Functional Design | Pending | Search implementation |
| Code Generation | Pending | Search UI and logic |
| Build & Test | Pending | Search verification |

#### Unit 6: Deployment
| Stage | Status | Notes |
|-------|--------|-------|
| Infrastructure Design | Pending | GitHub Pages config |
| Code Generation | Pending | Deploy scripts |
| Build & Test | Pending | Live deployment |

---

## 4. Units of Work

For parallel development, we'll break this into **3 units** that can run somewhat in parallel:

### Unit 1: Foundation (Infrastructure)
- 11ty project setup
- Package.json, config files
- Base folder structure
- GitHub Actions workflow

### Unit 2: Presentation (Templates & Styling)
- Base HTML templates
- CSS with Urdu support
- Navigation components
- Responsive design

### Unit 3: Content & Features
- JSON data model
- Sample poetry content
- Search functionality
- Deployment configuration

---

## 5. Technical Decisions

| Decision | Rationale |
|----------|------------|
| **11ty (Eleventy)** | Static site generator, GitHub Pages native support |
| **JSON for content** | Human-readable, easy to maintain, future-proof |
| **Jameel Nori Nastaliq font** | Free, high-quality Urdu Nastaliq font |
| **CSS Variables** | Easy theming, maintainable styles |
| **Client-side search** | Simple, no server needed |

---

## 6. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-------------|--------|-------------|
| Urdu font rendering issues | Medium | Medium | Test on multiple browsers, provide fallbacks |
| Inpage file conversion | High | High | Design flexible data model, accept JSON directly |
| RTL layout challenges | Low | Medium | Use proven CSS patterns for Arabic script |
| Search performance | Low | Low | Keep dataset small, use simple filtering |

---

## 7. Next Steps

**Upon approval of this plan:**

1. **Start Unit 1**: Project Setup & Infrastructure
   - Create package.json
   - Set up 11ty configuration
   - Create folder structure
   - Set up GitHub Actions

2. **In parallel**: Begin designing templates
3. **After Unit 1**: Proceed to content model and sample data

---

## 8. Approval Required

Please review and approve this execution plan before proceeding to Construction Phase.

**Questions to resolve:**
- [ ] Is the unit breakdown appropriate?
- [ ] Any additional requirements to add?
- [ ] Timeline expectations?