# Project: MCU Guide (Guia Cronológico do MCU)

Interactive chronological and release guide for Marvel Cinematic Universe movies and TV series with episode-level tracking, trailer embeds, cloud sync, and discrete discussions.

- **Repository:** `flou-ainan/mcu-guide`
- **Live Demo / Deployment:** GitHub Pages (`https://flou-ainan.github.io/mcu-guide/`)
- **Backend / BaaS:** Supabase (`https://fcwseeibamfdtmmvjjyh.supabase.co`)

---

## Architecture & Stack

1. **Frontend:**
   - Single-file SPA (`index.html`), zero-build toolchain, plus static legal pages (`privacy.html`, `terms.html`).
   - Tailwind CSS via CDN + FontAwesome 6 icons.
   - Marked.js for markdown rendering in user comments.
   - Client-side RFC 1321 `md5()` for Gravatar profile avatars.
   - LocalStorage for instant offline progress tracking (`mcu_watched_items`).
2. **Backend & Cloud Sync (Supabase):**
   - `@supabase/supabase-js` v2 CDN.
   - Email/Password and Google OAuth authentication.
   - Real-time progress synchronization with conflict merge strategies (supports movies, series, and individual episode IDs).
   - Public discrete comment drawer with optimistic reactions (Like, Dislike, Hulk punch, Laugh) and single-tier replies for both titles and individual episodes.
3. **Data Scraper:**
   - Python 3 (`scraper.py`) collecting IMDb covers, YouTube trailers, and Stremio Cinemeta episode metadata + `episodes.metahub.space` thumbnails with PT-BR translation (`translate.googleapis.com`).
   - Output structured into `mcu_data.json` and bundled as `data.js` (`window.__MCU_FALLBACK_DATA__`).

---

## Technical Decisions

| ADR | Summary |
|---|---|
| [ADR-001](dev-docs/decisions/ADR-001-episode-scraping-cinemeta.md) | Episode metadata via Stremio Cinemeta, unified `watched_ids` & `mcu_comments` (`movie_id`), client-side Gravatar MD5 |

---

## Database Schema (Supabase)

- **`public.mcu_progress`**:
  - `user_id` (uuid, primary key, references auth.users)
  - `watched_ids` (text[]) — stores movie, series, and episode IDs (`<series_id>-s<S>e<E>`)
  - `updated_at` (timestamptz)
- **`public.mcu_comments`**:
  - `id` (uuid, primary key)
  - `movie_id` (text, not null) — accepts title IDs or episode IDs
  - `user_id` (uuid, references auth.users)
  - `user_name` (text), `user_email` (text), `avatar_url` (text, nullable Google OAuth fallback photo)
  - `parent_id` (uuid, nullable for 1-level nested replies)
  - `reply_to_name` (text, nullable)
  - `content` (text, max 2000 chars)
  - `created_at` (timestamptz)
  - `edited_at` (timestamptz, nullable)
  - `edit_history` (jsonb, default `'[]'::jsonb` — array of `{ content, original_at, replaced_at }`)
  - *Trigger:* enforced max 200 comments per user.
- **`public.mcu_comment_reactions`**:
  - `comment_id` (uuid, references public.mcu_comments)
  - `user_id` (uuid, references auth.users)
  - `reaction` (text: 'like', 'dislike', 'hulk', 'laugh')
  - `created_at` (timestamptz)

---

## File Map

| File | Lines | Description |
|---|---|---|
| `index.html` | 3591 | Main SPA: hero banner (`fetchpriority="high"`), sticky top navbar (`Conheça o projeto`, custom/Gravatar/Google avatar & display name), responsive order switcher, watched status filter (`Todos / Não assistidos / Assistidos`), phase filters, shimmer skeletons, timeline views (`overflow: visible`, sized IMDb thumbnails, unclipped canon/ignorable badges, scoped watched fade), expandable post-credits timestamps, series episode expander & collapsed progress bar, modal trailer, safe Markdown comments drawer (`marked@15` + `DOMPurify@3`, collapsible formatting toolbar, `Markdown Permitido` pill, preview, `#insert-image-modal` with ImgBB info & live preview, inline editing & `#edit-history-modal`), Supabase auth/sync + inline profile customization |
| `privacy.html` | 125 | Privacy Policy page for Google OAuth compliance and user transparency |
| `terms.html` | 113 | Terms of Service page |
| `scraper.py` | 1092 | Python scraper for IMDb covers, YouTube trailers, Cinemeta series episodes + thumbnails, preserving researched `post_credits` data |
| `data.js` | 3477 | Generated JavaScript fallback bundle containing `window.__MCU_FALLBACK_DATA__` (including movie `post_credits`) |
| `mcu_data.json` | 3476 | Source JSON representation of 52 MCU titles (all 37 movies with `post_credits`) + 152 scraped series episodes |
| `README.md` | 166 | Showcase repository presentation with clickable clean live preview and external link |
| `docs/assets/readme-preview.png` | - | Clean 1280x720 desktop screenshot of live site for `README.md` |
| `robots.txt` | 5 | Crawler directive allowing TelegramBot and social media link previews |
| `hero-banner.webp` | - | High-res (2048x718) MCU collage banner |
| `og-image-1200x630.jpg` | - | OpenGraph/Telegram/WhatsApp social preview (`1200x630`) showcasing MCU triad + app UI mockup (canon badge, post-credits timestamps, progress bar, comments) |
| `docs/assets/github-social-preview.jpg` | - | Open-source GitHub Repository Social Preview (`1280x640`, ~192 KB) for manual upload in GitHub Repository Settings |
| `AGENTS.md` | 40 | Agent workflows, rules, and documentation standards |
| `.gitignore` | 15 | Local excludes: ignores `docs/dev-docs/chat-context.md`, temp files, pycache |
| `.ai-memory.toml` | 2 | Project binding for ai-memory MCP |
