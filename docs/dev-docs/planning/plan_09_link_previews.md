# Plan 09 — OpenGraph & GitHub Social Preview Overhaul

**Status:** done  
**Date:** 2026-11-11

## Goal

1. Replace the published website's OpenGraph link preview (`og-image-1200x630.jpg`) with the chosen **Variation 2** artwork (`1200×630`), fixing the small placeholder comment text in the UI mockup into natural Brazilian Portuguese and refreshing OpenGraph/Twitter meta tags (`?v=2` cache-bust + updated feature description) in `index.html`.
2. Create a distinct **GitHub Repository Social Preview** (`docs/assets/github-social-preview.jpg`, `1280×640`, 2:1 ratio, under 1 MB) visually inspired by Variation 2 but clearly styled as an open-source GitHub repository (`flou-ainan / mcu-guide`, tech stack badges, developer aesthetic) for manual upload in GitHub Repository Settings → Social preview.

## Scope & Files

- `og-image-1200x630.jpg` — Replaced with fixed & resized Variation 2 (`1200×630` JPEG).
- `index.html` — Update `og:image`, `og:image:secure_url`, `twitter:image`, `itemprop="image"`, `meta[name="image"]` to include `?v=2` and update description meta tags to reflect current features.
- `docs/assets/github-social-preview.jpg` — New `1280×640` JPEG (~192 KB) tailored for GitHub Social Preview.
- `docs/PROJECT.md`, `docs/dev-docs/ROADMAP.md`, `docs/dev-docs/devlog/step_09_link_previews.md`, `docs/dev-docs/chat-context.md`.

## Verification

- Inspect both generated/processed images visually via `read_file` and verify exact pixel dimensions (`1200×630` and `1280×640`).
- Verify `index.html` meta tag consistency via `grep`.
- Commit and push to `origin/main` so GitHub Pages serves the updated OpenGraph preview.
