# Plan 08 — Showcase README Overhaul & Clickable Site Preview Image

**Status:** in progress
**Date:** 2026-11-11

## Goal
Revamp `README.md` into an inviting, modern GitHub showcase highlighting the full MCU Guide experience (all 37 movies, 15 series, 152 scraped episodes, post-credits timestamps, watched filters, cloud sync, profile customization, Markdown comments with image modal & edit history, and zero-build architecture) with a clean, clickable top screenshot banner featuring an integrated **ACESSE O GUIA** call-to-action overlay.

## Proposed changes

1. **Generate Clean Live Screenshot + `ACESSE O GUIA` Banner Image (`docs/assets/readme-preview.png`):**
   - Capture a high-resolution Desktop (`1280x960` or `1280x860`) screenshot of the live site (`https://flou-ainan.github.io/mcu-guide/` or `http://localhost:8080/`) showing the hero header, progress tracker, filters, and unclipped `Canônico MCU` movie cards.
   - Composite a subtle dark bottom vignette + sleek Marvel red rounded CTA pill reading **ACESSE O GUIA** cleanly onto the screenshot (`docs/assets/readme-preview.png`) using Pillow so it renders reliably inside GitHub Markdown.
2. **Rewrite `README.md`:**
   - Keep the heartfelt personal story ("Sobre o Projeto") that explains why the app was created for family & friends.
   - Open right below the centered title/badges with the clickable screenshot wrapped in a link to `https://flou-ainan.github.io/mcu-guide/`.
   - Highlight all major features cleanly in organized sections / tables (Timeline & Filters, 152 Episode Checklists, Post-Credits Timestamps, Cloud Sync & Profile Customization, Community Comments with Safe Markdown + Reactions + Edit History, Performance & Zero-Build Architecture), plus Quick Start (`python3 -m http.server 8080`) and Privacy/Terms links.
3. **Docs, Verification & Release (`git push`):**
   - Inspect `docs/assets/readme-preview.png` via `read_file` to verify crisp typography, zero clipping, and visual polish.
   - Update `plan_08` (`done`), `step_08` devlog, `PROJECT.md`, `ROADMAP.md`, and `chat-context.md`, then commit and push to `origin/main`.

## Definition of done / how to test
- `docs/assets/readme-preview.png` visually reviewed via `read_file`: clean site showcase + readable `ACESSE O GUIA` overlay without covering key UI headers.
- `README.md` links cleanly to `https://flou-ainan.github.io/mcu-guide/`, `docs/assets/readme-preview.png`, `privacy.html`, `terms.html`, and accurately reflects all current features.
- Changes committed and pushed to `origin/main`.
