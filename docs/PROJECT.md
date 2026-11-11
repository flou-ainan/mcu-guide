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
| `index.html` | 2361 | Main SPA: hero banner, sticky top navbar with Gravatar/Google avatar fallback, filters, timeline views, series episode expander, modal trailer, discrete comments drawer, Supabase auth/sync |
| `privacy.html` | 125 | Privacy Policy page for Google OAuth compliance and user transparency |
| `terms.html` | 113 | Terms of Service page |
| `scraper.py` | 1090 | Python scraper for IMDb covers, YouTube trailers, and Cinemeta series episodes + thumbnails |
| `data.js` | 3008 | Generated JavaScript fallback bundle containing `window.__MCU_FALLBACK_DATA__` |
| `mcu_data.json` | 3007 | Source JSON representation of 52 MCU titles + 152 scraped series episodes |
| `README.md` | 51 | Repository presentation and deployment details |
| `robots.txt` | 5 | Crawler directive allowing TelegramBot and social media link previews |
| `hero-banner.webp` | - | High-res (2048x718) MCU collage banner |
| `og-image-1200x630.jpg` | - | Standard OpenGraph social preview image |
| `AGENTS.md` | 40 | Agent workflows, rules, and documentation standards |
| `.gitignore` | 15 | Local excludes: ignores `docs/dev-docs/chat-context.md`, temp files, pycache |
| `.ai-memory.toml` | 2 | Project binding for ai-memory MCP |
