# Step 08 — README showcase & Hulk post-credits fix

**Date:** 2026-11-11  
**Plan:** `plan_08_readme_showcase_and_preview.md`  
**Status:** Done — pushed to `origin/main`

---

## What Changed

### 1. Fix: O Incrível Hulk post-credits data

**Files:** `mcu_data.json`, `data.js`

- Corrected `post_credits.count` from `0` → `1`
- Added scene entry: `"Cena de pré-créditos (Tony Stark / Iniciativa Vingadores)"` at timestamp `~01:47:00`
- Updated `note` to explain that the scene occurs just before the final credits roll (commonly mistaken for no post-credits), and that it is Tony Stark appearing at a bar to recruit General "Thunderbolt" Ross for the Avengers Initiative
- Fix applies to both `mcu_data.json` (primary source) and `data.js` (offline fallback bundle)

**Root cause:** The original note stated the scene was "before the credits", which is technically true (it's a pre-credits stinger), but the `count: 0` incorrectly told users there was no scene at all. The user confirmed via Google AI Overview that the scene exists.

### 2. README overhaul — showcase-grade rewrite

**File:** `README.md`

- Complete rewrite inspired by top-tier GitHub project READMEs
- Added clean live-site screenshot `docs/assets/readme-preview.png` as a clickable link to `https://flou-ainan.github.io/mcu-guide/`, followed by an external clickable text link (`🌐 Acesse o Guia →`) below the image
- Added shields.io badges (MCU, GitHub Pages live, 52 Titles, Offline First/Supabase)
- Full feature table covering all Step 01–07 features
- Content breakdown (52 titles, 37 movies, 15 series, post-credits timestamps)
- Quick Start section (zero-dependency local server)
- Stack table (HTML5, CSS3, Vanilla JS, Tailwind CDN, Supabase, GitHub Pages)
- Privacy & Security section
- Footer with live link, bug report, and feature request links
- Written in Brazilian Portuguese (UI-facing text) / English (technical sections)

### 3. README preview image generation

**File:** `docs/assets/readme-preview.png`

- Captured live site at `https://flou-ainan.github.io/mcu-guide/` via headless Chrome → `/tmp/raw_site.png` (1280×1040px)
- Cropped and resized to a clean 1280×720px screenshot with Pillow (no badge or text overlay inside the image)
- Saved to `docs/assets/readme-preview.png` (~618KB)

---

## Files Touched

| File | Change |
|---|---|
| `mcu_data.json` | Hulk `post_credits`: count 0→1, added scene + corrected note |
| `data.js` | Same as above (offline fallback bundle) |
| `README.md` | Complete overhaul with live preview image |
| `docs/assets/readme-preview.png` | New: clean 1280×720 screenshot (no overlay) |
| `docs/dev-docs/devlog/step_08_readme_showcase_and_hulk_fix.md` | This file |

---

## Testing

- Verified JSON validity: `node -e` confirmed `hulk.post_credits.count === 1` with correct scene data
- Verified preview image renders correctly (read_file + visual inspection confirmed hero banner, CTA pill, and correct layout)
- README renders correctly on GitHub (standard Markdown + centered HTML divs with badges)

---

## Commit

```
git commit -m "docs: overhaul README with live preview and fix Hulk post-credits data"
```
