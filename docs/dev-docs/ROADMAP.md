# Roadmap

**The one list of what is left.** Keep this list updated as tasks are planned and executed.

**Last updated:** 2026-11-11 (step 07 published to GitHub Pages: unclipped card badges, collapsible Markdown toolbar + `Markdown Permitido` badge, `#insert-image-modal` with preview & ImgBB info).

## Now: external configuration

| Item | Plan | Notes |
|---|---|---|
| **Supabase Auth URL Configuration** | — | Set `Site URL` to `https://flou-ainan.github.io/mcu-guide/` and add both production and `http://localhost:8080/**` to `Redirect URLs` in Supabase Dashboard so production Google OAuth returns to GitHub Pages. |

## Next: ideas & improvements

| Idea | Notes |
|---|---|
| *No open items yet* | Add new feature ideas here as needed. |

## Done (recent)

- High-res hero banner (2048x718, mobile full-width, desktop max-w-6xl).
- OpenGraph & Twitter Card previews (1200x630, TelegramBot-compatible `robots.txt` and Schema.org tags).
- Sticky top navigation bar with Marvel badge and prominent Login button.
- Supabase Auth (Google OAuth & Email/Password modal) + real-time cloud progress sync with conflict resolution.
- Discrete Instagram-style comment drawer per card with Markdown, 2000 chars limit, reactions, and 1-tier replies.
- **Step 01 (2026-11-11, Plan 01, ADR-001):**
  - Optimistic comment reactions (eliminated loading spinner flash).
  - Gravatar avatars across top navbar, auth modal, comments, and replies.
  - Series episode expander with 152 scraped episodes (Stremio Cinemeta + Metahub thumbnails + PT-BR translations), per-episode watched tracking, synopses, and episode-level comments (no trailers/IMDb).
  - Created `privacy.html` & `terms.html` and linked in footer.
- **Step 02 (2026-11-11, Plan 02):**
  - Switched Gravatar lookup to `d=404` with automatic fallback to Google OAuth profile photo (`user_metadata.avatar_url` / `picture`), then initials/cloud icon across navbar, auth modal, comments, and replies.
  - Persisted `avatar_url` on `public.mcu_comments` inserts so other viewers see the commenter's Google photo when Gravatar is absent.
  - Published updates to `origin/main` (GitHub Pages).
- **Step 03 (2026-11-11, Plan 03 — local):**
  - Replaced `MCU Canon` / `Ignorável` with top-right floating badges `Canônico MCU` and `Não Canônico` visible on both mobile and desktop.
  - Scoped watched opacity fade solely to collapsed card/episode summary rows so expanded synopses, episode lists, and comments remain at full contrast (`opacity: 1`).
  - Added collapsed series card progress bar + `%` (visible only when `watchedEps > 0` and collapsed; hides when expanded while keeping progress bar + `%` inside `Episódios` on mobile & desktop).
  - Updated navbar GitHub text to `Conheça o projeto` on wide screens (`hidden md:inline`) and unified series/movie/episode `Comentários` buttons via `renderCommentsTriggerButton`.
- **Step 04 (2026-11-11, Plan 04 — local):**
  - Fixed comment Markdown rendering: replaced dead Tailwind `prose` classes with dedicated `.comment-markdown` CSS rules, pinned `marked@15` + `DOMPurify@3`, normalized heading sizes (`#..###` -> `h4..h6`), constrained comment images (`max-height: 220px`, `object-fit: contain`, delegated zoom modal), and hardened links/XSS.
  - Added **Escrever / Preview** toggle selector (`setCommentEditorMode`) in the comment composer.
  - Added `RESPOSTAS (${replies.length})` label above nested comment replies and renamed `Não Canônico` back to `Ignorável`.
- **Step 05 (2026-11-11, Plan 05):**
  - Normalized scheme-less Markdown link/image domains (`normalizeSafeExternalUrl`), added broken-image fallback link pill, and added quick Markdown toolbar (`B`, `I`, `H`, `Link`, `Img`, `</>`).
  - Added full `DD/MM/YYYY às HH:mm` timestamps, inline author comment/reply editing, and clickable `edited` badge opening `#edit-history-modal`.
  - Applied PageSpeed/UX upgrades: YouTube-style skeleton shimmer cards, immediate `DOMContentLoaded` render from `data.js`, `preconnect`, non-blocking FontAwesome, deferred Markdown/DOMPurify scripts, `content-visibility: auto`, and IMDb resized posters (`_V1_SX40_` blur-up -> `_V1_SX120_` mini-thumbs -> `_V1_SX320_` detail -> full `_V1_.jpg` zoom).
  - Changed collapsed mini-thumbnails to expand the card instead of opening zoom modal.
  - Added `post_credits` counts and start timestamps across all 37 movies with expandable post-credits badge panels.
- **Step 06 (2026-11-11, Plan 06):**
  - Verified live Supabase `edited_at`/`edit_history` migration (`HTTP 200`).
  - Added watched status filter (`Todos`, `Não assistidos`, `Assistidos`) next to phase chips.
  - Added profile customization form inside logged-in Auth Modal (`display_name` & `custom_avatar_url` persisted via `supabase.auth.updateUser` and propagated to navbar & `public.mcu_comments`).
  - Polished Chronological vs Release order toggle responsiveness for `360px` mobile screens (zero horizontal overflow) and published Steps 03–06 to `origin/main` (GitHub Pages).
- **Step 07 (2026-11-11, Plan 07):**
  - Removed `content-visibility: auto` paint containment on `.mcu-timeline-card` so floating `Canônico MCU` / `Ignorável` badges render completely unclipped.
  - Added `Markdown Permitido` badge beside `Escrever / Preview` tabs and hid the formatting toolbar behind a discrete `Formatar` toggle button (`toggleMarkdownToolbar`).
  - Replaced `Img` snippet insertion with `#insert-image-modal` featuring an `(i)` ImgBB hosting recommendation, description input, URL input with live preview, and direct Markdown insertion; published to `origin/main` (GitHub Pages).

## Plans at a glance

| Plan | Status |
|---|---|
| [plan_01_episodes_gravatar_reactions_legal.md](planning/plan_01_episodes_gravatar_reactions_legal.md) | done |
| [plan_02_google_avatar_fallback_and_deploy.md](planning/plan_02_google_avatar_fallback_and_deploy.md) | done |
| [plan_03_card_badges_fade_progress_ux.md](planning/plan_03_card_badges_fade_progress_ux.md) | done |
| [plan_04_markdown_preview_replies_ignorable.md](planning/plan_04_markdown_preview_replies_ignorable.md) | done |
| [plan_05_markdown_links_edit_pagespeed_postcredits.md](planning/plan_05_markdown_links_edit_pagespeed_postcredits.md) | done |
| [plan_06_watched_filter_and_profile_customization.md](planning/plan_06_watched_filter_and_profile_customization.md) | done |
| [plan_07_badge_clip_toolbar_image_modal.md](planning/plan_07_badge_clip_toolbar_image_modal.md) | done |
