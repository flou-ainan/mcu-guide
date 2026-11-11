# Roadmap

**The one list of what is left.** Keep this list updated as tasks are planned and executed.

**Last updated:** 2026-11-11 (step 02: Gravatar → Google avatar fallback & GitHub Pages publish).

## Now: post-deploy configuration

| Item | Plan | Notes |
|---|---|---|
| **Google OAuth Branding URLs** | — | Paste live `https://flou-ainan.github.io/mcu-guide/privacy.html` & `terms.html` URLs in Google Auth Platform Branding and submit verification if required. |

## Next: ideas & improvements

| Idea | Notes |
|---|---|
| Profile avatar & username customization | Allow users to set a custom display name instead of parsing email/OAuth names. |
| Filter by watched status | Add a quick toggle button to show only "Unwatched" or "Watched" movies. |
| Chronological vs Release order toggle polish | Further visual refinements if needed. |

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

## Plans at a glance

| Plan | Status |
|---|---|
| [plan_01_episodes_gravatar_reactions_legal.md](planning/plan_01_episodes_gravatar_reactions_legal.md) | done |
| [plan_02_google_avatar_fallback_and_deploy.md](planning/plan_02_google_avatar_fallback_and_deploy.md) | done |
