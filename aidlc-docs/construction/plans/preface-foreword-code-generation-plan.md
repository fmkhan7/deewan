# Code Generation Plan: Preface and Foreword Authoring

## Unit Context
- **Unit**: Preface and foreword authoring
- **Stories**: None; requirements are tracked in `aidlc-docs/inception/requirements.md`.
- **Dependencies**: Existing Eleventy base layout and Markdown template engine.
- **Data models or APIs**: None.
- **Scope**: Application templates and the two publishing source files only.

## Steps

- [x] **Step 1: Add a shared content-page layout**
  - Create `src/_includes/layouts/content-page.njk`.
  - Chain to the existing base layout, render the page title once, and wrap rendered Markdown in the existing content and Urdu-text styling classes.

- [x] **Step 2: Simplify the preface and foreword sources**
  - Update `src/pages/preface.md` and `src/pages/foreword.md` to use the shared layout.
  - Keep their titles, permalinks, and Urdu wording unchanged.
  - Replace presentation HTML with Markdown paragraphs.

- [x] **Step 3: Verify the generated pages**
  - Run `npm run build`.
  - Confirm both pages render at their existing URLs with the expected titles, Urdu text, and RTL styling.

## Completion Criteria
- The pages no longer duplicate HTML page scaffolding.
- Their content remains readable and editable as Markdown.
- The site build succeeds and both generated pages preserve existing behavior.
