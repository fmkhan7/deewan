# Build Instructions

## Prerequisites
- Node.js 18 or newer
- npm

## Build

Install dependencies from the lockfile:

```bash
npm ci
```

Generate the static site:

```bash
npm run build
```

The generated site is written to `_site/`. No environment variables are required.
