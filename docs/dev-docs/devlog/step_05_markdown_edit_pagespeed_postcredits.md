# Step 05 — Markdown Links/Images, Comment Editing & History Modal, PageSpeed/Skeletons & Post-Credits Timestamps

**Date:** 2026-11-11
**Plan:** [plan_05_markdown_links_edit_pagespeed_postcredits.md](../planning/plan_05_markdown_links_edit_pagespeed_postcredits.md)
**Scope:** Local changes (`index.html`, `mcu_data.json`, `data.js`, `scraper.py`, dev docs) — awaiting owner review and push approval.

## What changed

1. **Markdown Links, Images & Quick Toolbar (`index.html`):**
   - Replaced strict `isSafeExternalUrl` with `normalizeSafeExternalUrl`, automatically prepending `https://` to scheme-less domains (e.g. `www.google.com`, `imgur.com/x.png`) while still blocking unsafe protocols (`javascript:`, `data:`, `vbscript:`, `file:`) and protocol-relative URLs.
   - Styled comment links cleanly (`.comment-markdown a` `#38bdf8` -> `#7dd3fc`).
   - Added a capture-phase `error` listener on `.comment-markdown img` to render a fallback link pill if an external host blocks hotlinking or fails to load.
   - Added `renderMarkdownToolbarHTML` + `insertCommentMarkdown` (`B`, `I`, `H`, `Link`, `Img`, `</>`) to both the main composer and inline edit composer.

2. **Comment Dates, Editing & History Modal (`index.html`):**
   - Updated `formatCommentDate` to always format full date and time (`DD/MM/YYYY às HH:mm`, `pt-BR`).
   - Added inline comment & reply editing for authors (`startEditComment`, `cancelCommentEdit`, `saveCommentEdit`, `setInlineEditMode`, `updateEditCharCount`) with `Escrever / Preview` tabs and Markdown toolbar.
   - Added clickable `edited` badge (`renderEditedBadgeHTML`) opening `#edit-history-modal` (`openEditHistoryModal` / `closeEditHistoryModal`), listing the current revision alongside all prior revisions with timestamps.
   - Persisted `edited_at` and `edit_history` JSONB on `public.mcu_comments` (handling missing-column or missing-`UPDATE`-RLS errors gracefully with guidance).

3. **PageSpeed, Skeletons & Mini-Thumbnail Behavior (`index.html`):**
   - Added `<link rel="preconnect">` / `dns-prefetch` hints for `m.media-amazon.com`, `cdn.jsdelivr.net`, `fonts.googleapis.com`, and Supabase; added hero banner preload (`hero-banner.webp`) with `fetchpriority="high"` and `2048x718` dimensions; deferred `marked` & `dompurify`; switched FontAwesome CSS to non-blocking load; added CSS `content-visibility: auto` (`.mcu-timeline-card`).
   - Replaced `#timeline-container` loading spinner with 6 YouTube-style `.skeleton-shimmer` cards.
   - Added `getSizedPosterUrl` (`_V1_SX40_` progressive blur-up placeholder backgrounds -> `_V1_SX120_` mini-thumbs -> `_V1_SX320_` expanded posters -> full `_V1_.jpg` only in `#image-modal`).
   - Updated startup (`initApp` on `DOMContentLoaded`) to render immediately from `window.__MCU_FALLBACK_DATA__` (`data.js?v=20261111b`) before async `mcu_data.json` sync.
   - Removed `openImageModal` and `cursor-zoom-in` from collapsed mini-thumbnails on both movie and series cards so clicking a mini-thumb only expands the card; fullscreen zoom remains on expanded posters.

4. **Post-Credits Badges & Start Timestamps (`mcu_data.json`, `data.js`, `scraper.py`, `index.html`):**
   - Researched and populated `post_credits` (`count`, `note`, `scenes: [{ type, timestamp }]`) for all 37 MCU movies in `mcu_data.json` and `data.js`, and updated `scraper.py` to preserve `post_credits` across future scrapes.
   - Added `renderPostCreditsSectionHTML` + `togglePostCreditsPanel` inside expanded movie cards (`Sem cena pós-crédito`, `1 cena pós-crédito`, `2 cenas pós-crédito`, or `5 cenas pós-crédito`), revealing scene positions and timestamps on click.

## Files touched

- `index.html` (3169 lines)
- `mcu_data.json` (3471 lines)
- `data.js` (3472 lines)
- `scraper.py` (1092 lines)
- `docs/PROJECT.md`
- `docs/dev-docs/ROADMAP.md`
- `docs/dev-docs/planning/plan_05_markdown_links_edit_pagespeed_postcredits.md`
- `docs/dev-docs/devlog/step_05_markdown_edit_pagespeed_postcredits.md`

## How it was tested

- `node -c data.js` and syntax check (`node -c`) on extracted JS from `index.html`: passed cleanly.
- Data integrity check: verified 52 total entries (37 movies, 15 series) and confirmed all 37 movies contain valid `post_credits` metadata.
- Node `vm` unit assertions verified `normalizeSafeExternalUrl` (`www.google.com` -> `https://www.google.com`, bare domain normalization, `javascript:` & `data:` rejection), `getSizedPosterUrl` (`_V1_SX120_` / `'full'`), `formatCommentDate` (`11/11/2026 às HH:mm`), `renderCommentCard` edit button & clickable `edited` badge, and inline edit box + Markdown toolbar rendering.
- Live browser test via subagent on `http://localhost:8080/` across Desktop (`1280x800`) and Mobile (`360x800`):
  - **0 console errors**, **0 page errors**, **0 HTTP >=400 failures**.
  - Verified `_V1_SX120_` mini-thumbs with `_V1_SX40_` style backgrounds.
  - Verified clicking collapsed mini-thumb expands the card without opening `#image-modal`.
  - Verified expanded poster (`_V1_SX320_`) opens `#image-modal` (`_V1_.jpg`) on click and closes with `Escape`.
  - Verified post-credits badges and timestamp panels on *O Incrível Hulk* (`Sem cena pós-crédito`), *Homem de Ferro* (`1 cena pós-crédito`, `~01:59:40`), and *Os Vingadores* (`2 cenas pós-crédito`, `~02:16:35` & `~02:22:05`).
