# Integration Test Instructions

The site is statically generated and has no separate services to start.

1. Run `npm run build`.
2. Confirm `_site/preface/index.html` and `_site/foreword/index.html` exist.
3. Confirm each generated page has its expected title, Urdu text, and RTL styling.
4. Confirm the shared site navigation links to both pages.
