# Plan 07 — Unclip Floating Card Badges, Collapsible Markdown Toolbar & Rich Insert Image Modal

**Status:** done
**Date:** 2026-11-11

## Goal
Fix clipped `Canônico MCU` / `Ignorável` card badges caused by CSS `content-visibility: auto` paint containment, hide the Markdown formatting toolbar behind a discrete toggle button alongside a `Markdown permitido` badge, and replace inline image markdown snippet insertion with a previewable `#insert-image-modal` including an ImgBB hosting notice.

## Proposed changes

1. **Unclip Floating Badges (`index.html`):**
   - Remove `content-visibility: auto` paint containment from `.mcu-timeline-card` (keeping `overflow: visible`) and add slight top spacing (`pt-1`) on `#timeline-container` so `-top-2.5 right-3` badges render intact on all movie and series cards.
2. **Collapsible Markdown Toolbar & `Markdown permitido` Badge (`index.html`):**
   - Add a `Markdown permitido` pill right beside `[[ ✏️ Escrever ][ 👁 Preview ]]` in both the comment composer and inline edit composer.
   - Hide the Markdown toolbar (`renderMarkdownToolbarHTML`) by default and add a discrete toggle button (`toggleMarkdownToolbar(toolbarId, btnEl)`) that expands/collapses it on demand.
3. **Rich Insert Image Modal (`index.html`):**
   - Add `#insert-image-modal` right after `#edit-history-modal`, plus Escape key cleanup.
   - Inside the modal:
     - `(i)` info banner explaining images are not hosted locally, only public URLs can be displayed, and recommending free hosting via `ImgBB` (`https://pt-br.imgbb.com/`).
     - `Descrição da imagem` input (`#insert-img-alt`) and `URL da imagem` input (`#insert-img-url`) with live image preview (`#insert-img-preview`) & error state.
     - `OK, inserir` button pastes `![desc](url)` at the active textarea selection/cursor, closes the modal, restores `write` mode, and updates the char counter.
4. **Docs, Local Verification & Release Check:**
   - Verify via `node -c`, Node `vm` checks, and headless browser at `http://localhost:8080/` (verifying zero badge clipping via bounding rects, hidden-by-default Markdown toolbar + toggle, `Markdown permitido` badge, `#insert-image-modal` flow, and 0 console errors).
   - Keep changes local unless user approves pushing, or update docs cleanly (`plan_07`, `step_07`, `ROADMAP.md`, `PROJECT.md`, `chat-context.md`).

## Definition of done / how to test
- `Canônico MCU` and `Ignorável` badges sit cleanly without top clipping (`badgeRect.top` visible and unclipped inside parent overflow bounds).
- `Markdown permitido` badge appears immediately to the right of `Escrever | Preview`; formatting buttons are hidden until the discrete toolbar toggle is clicked.
- Clicking `Img` opens `#insert-image-modal` with `(i)` ImgBB notice, description input, URL input with live preview, and inserts formatted Markdown on confirm.
- 0 console/page errors on desktop and mobile (`360x800`).
