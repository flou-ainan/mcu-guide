# Plan 05 — Markdown Link/Image Fixes, Comment Dates & Edit History, PageSpeed/Skeletons, Mini-Thumb Behavior & Post-Credits Data

**Status:** done
**Date:** 2026-11-11

## Goal
Resolve Markdown link/image preview issues, add date+time and comment editing with clickable `edited` history modal, significantly improve PageSpeed/LCP/UX (skeleton cards, low-res blur-up preloading, resized IMDb thumbnails, `content-visibility`, non-blocking CSS/scripts), make collapsed mini-thumbnails expand the card instead of zooming, and add researched post-credits scene counts and start timestamps to all 37 MCU movies.

## Proposed changes

1. **`mcu_data.json` & `data.js` (and `scraper.py` preservation if re-run)**:
   - Add `post_credits` metadata (`count`, `note`, `scenes: [{ type, timestamp }]`) to all 37 movies based on verified MCU release runtimes and credit positions.
   - Ensure `scraper.py` preserves `post_credits` if re-run in the future.
2. **Markdown Links, Images & Timestamps (`index.html`)**:
   - Upgrade `isSafeExternalUrl` -> `normalizeSafeExternalUrl` so domains typed without `https://` (e.g. `www.google.com`, `site.com/img.png`) normalize cleanly to `https://` while still blocking dangerous schemes (`javascript:`, `data:`, `vbscript:`).
   - Add clickable broken-image fallback (`error` capture listener on `.comment-markdown img`) and quick Markdown insert toolbar buttons (`B`, `I`, `H`, `Link`, `Img`, `Code`) in the comment composer so users can verify/insert links and images effortlessly.
   - Update `formatCommentDate(dateStr)` to render both date and time (`DD/MM/YYYY às HH:mm`) on comments, replies, and edit history entries.
3. **Comment Editing & History Modal (`index.html` + Supabase SQL guide)**:
   - Add Edit button (`startEditComment` / `cancelCommentEdit` / `saveCommentEdit`) on own root comments and nested replies with inline Escrever/Preview support.
   - Save `edited_at` and `edit_history` JSON array (`[{ content, edited_at }]`) to `public.mcu_comments`, handling missing column/RLS errors gracefully if the SQL migration has not yet been applied in Supabase.
   - Render clickable `edited` badge next to comment timestamp opening `#edit-history-modal` with all dated revisions.
4. **PageSpeed, Skeletons, Low-Res Preloading & Mini-Thumb Click (`index.html`)**:
   - Add `<link rel="preconnect">` hints, `fetchpriority="high"` + explicit dimensions on hero banner, `defer` on `marked`/`dompurify`, non-blocking FontAwesome CSS load, and `.mcu-timeline-card` `content-visibility: auto`.
   - Replace static spinner in `#timeline-container` with YouTube-style shimmer skeleton cards.
   - Add `getSizedPosterUrl` (`_V1_SX40_` blur-up background preload, `_V1_SX120_` for collapsed mini-thumbs, `_V1_SX320_` for expanded posters, full `_V1_.jpg` only in `#image-modal`).
   - Remove `openImageModal` and `cursor-zoom-in` from collapsed mini-thumbnails so clicking them expands the card; keep fullscreen zoom only on expanded posters (and episode thumbs).
5. **Post-Credits Badges & Timestamps (`index.html`)**:
   - Inside expanded movie cards (`#details-*`), display a post-credits badge (`Sem cena pós-crédito`, `1 cena pós-crédito`, `2 cenas pós-crédito`, or `5 cenas pós-crédito` for *Guardians Vol. 2*).
   - Clicking a badge with 1+ scenes toggles `#post-credits-${item.id}` displaying scene types and start timestamps.
6. **Docs & Local Verification**:
   - Update `PROJECT.md`, `ROADMAP.md`, `plan_05` (`done`), `step_05` devlog, `chat-context.md`.
   - Verify JS syntax, `mcu_data.json` / `data.js` integrity, Markdown link/image/edit-history behavior, live `http://localhost:8080/` rendering (desktop + mobile, 0 console errors), and send SMTP confirmation email (including the exact Supabase SQL snippet for comment editing/history).

## Definition of done / how to test
- `node -c` passes on `index.html` and `data.js`.
- All 37 movies in `mcu_data.json` and `data.js` have validated `post_credits` entries.
- Live browser test at `http://localhost:8080/` confirms skeleton shimmer CSS, `_V1_SX120_` / `_V1_SX40_` poster loading, mini-thumb click expanding the card without opening zoom modal, expanded poster opening zoom modal, post-credits badges + timestamps, Markdown links/images + `edited` modal logic, and 0 console errors.
- Confirmation email sent via SMTP to `gabriel8flow@gmail.com`.
