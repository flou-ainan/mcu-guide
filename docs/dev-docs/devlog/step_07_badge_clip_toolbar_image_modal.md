# Step 07 — Unclip Card Badges, Collapsible Markdown Toolbar & Rich Insert Image Modal

**Date:** 2026-11-11
**Plan:** [plan_07_badge_clip_toolbar_image_modal.md](../planning/plan_07_badge_clip_toolbar_image_modal.md)
**Scope:** Verified at `http://localhost:8080/` and published (`index.html` + dev docs) to `origin/main` (GitHub Pages).

## What changed

1. **Fixed Floating Card Badge Clipping (`index.html`):**
   - Removed `content-visibility: auto` paint containment on `.mcu-timeline-card` (which clipped `-top-2.5 right-3` badges protruding above the card box), switched `.mcu-timeline-card` to `overflow: visible`, and added `pt-2` to `#timeline-container`.

2. **Comment Composer Toolbar Toggle & `Markdown Permitido` Badge (`index.html`):**
   - Placed a `Markdown Permitido` badge immediately to the right of the `[[ ✏️ Escrever ][ 👁 Preview ]]` tabs in both comment creation and inline edit forms.
   - Hid the formatting toolbar (`renderMarkdownToolbarHTML`) by default behind a discrete `Formatar` toggle button (`renderMarkdownToolbarToggleHTML` + `toggleMarkdownToolbar`).

3. **Rich Insert Image Modal (`index.html`):**
   - Replaced raw placeholder insertion on clicking **Img** with `#insert-image-modal` (`openInsertImageModal`, `closeInsertImageModal`, `previewInsertImageModal`, `confirmInsertImageModal`).
   - Added an `(i)` notice explaining images are not hosted locally and recommending `ImgBB` (`https://pt-br.imgbb.com/`) for free public image hosting.
   - Added inputs for **Descrição da imagem** and **URL da imagem**, live image preview with error state, Escape key handling, and clean Markdown insertion (`![desc](url)`) back into the active comment/edit textarea.

## Files touched

- `index.html` (3591 lines)
- `docs/PROJECT.md`
- `docs/dev-docs/ROADMAP.md`
- `docs/dev-docs/planning/plan_07_badge_clip_toolbar_image_modal.md`
- `docs/dev-docs/devlog/step_07_badge_clip_toolbar_image_modal.md`

## How it was tested

- `node -c` syntax check passed on extracted JS from `index.html`.
- Node `vm` assertions verified removal of `content-visibility: auto`, presence of `Markdown Permitido` pill immediately beside `Escrever / Preview`, hidden-by-default toolbar + `toggleMarkdownToolbar`, and `#insert-image-modal` / `openInsertImageModal` ImgBB link wiring.
- Interactive headless browser test at `http://localhost:8080/` across Desktop (`1280x800`) and Mobile (`360x800`):
  - Verified full unclipped rounded pill borders and text for `Canônico MCU` and `Ignorável` on both desktop and mobile (`final_step_43.png`).
  - Verified `#insert-image-modal` DOM presence (`ImgBB` notice link, `#insert-img-alt`, `#insert-img-url`, `#insert-img-preview`).
  - **0 console/page errors** and **0 HTTP >= 400 failures**.
