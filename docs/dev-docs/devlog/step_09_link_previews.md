# Step 09 — Website OpenGraph Preview & GitHub Social Preview

**Date:** 2026-11-11  
**Plan:** `plan_09_link_previews.md`  
**Status:** Done — pushed to `origin/main`

---

## What Changed

### 1. Website OpenGraph Preview (`og-image-1200x630.jpg` + `index.html`)

- Replaced `og-image-1200x630.jpg` with the owner-selected **Variation 2** artwork (`1200×630` JPEG), showing the MCU triad alongside an app UI mockup featuring progress bar (`68%`), `Canônico MCU` badge, `2 Cenas Pós-Créditos • Timestamps`, and a Portuguese comment card (`Gabriel há 5 min`).
- Patched the small comment box placeholder copy inside the generated image via Pillow (matching background `#26292E` and `-3.05°` tilt) so all visible text is natural Brazilian Portuguese.
- Updated `index.html` OpenGraph, Twitter Card, primary `<meta>`, and Schema.org tags:
  - Added `?v=2` query string to `og-image-1200x630.jpg` URLs to bust Telegram/WhatsApp/social scraper caches.
  - Updated descriptions to reflect current capabilities: 52 titles (37 movies + 15 series), chronological & release order, post-credits scenes with timestamps, cloud sync, and Markdown comments.

### 2. GitHub Repository Social Preview (`docs/assets/github-social-preview.jpg`)

- Generated a distinct **GitHub Social Preview** (`1280×640` JPEG, ~192 KB, 2:1 ratio) visually inspired by Variation 2 while clearly branding the open-source GitHub repository (`flou-ainan / mcu-guide` with Octocat mark, `"Código aberto • SPA sem build • Offline-First & Cloud Sync"`, stack pills `Vanilla JS`, `Tailwind CSS`, `Supabase`, `GitHub Pages`, and floating JSON snippet card).
- Ready for manual upload under **GitHub → Settings → General → Social preview**.

---

## Files Touched

| File | Change |
|---|---|
| `og-image-1200x630.jpg` | Replaced with `1200×630` Variation 2 artwork (PT-BR comment patch) |
| `index.html` | Updated OG/Twitter/Schema descriptions and `og-image-1200x630.jpg?v=2` |
| `docs/assets/github-social-preview.jpg` | Added `1280×640` GitHub repository social preview (~192 KB) |
| `docs/dev-docs/planning/plan_09_link_previews.md` | Plan doc (marked `done`) |
| `docs/dev-docs/devlog/step_09_link_previews.md` | This devlog |
| `docs/dev-docs/ROADMAP.md` | Added Steps 08 & 09 |
| `docs/PROJECT.md` | Updated preview asset descriptions |

---

## Verification

- Visual inspection via `read_file` confirmed clean PT-BR copy, exact pixel dimensions (`1200×630` and `1280×640`), and safe margins on both images.
- `grep -n "og-image" index.html` confirmed all 5 meta image tags consistently point to `og-image-1200x630.jpg?v=2`.
