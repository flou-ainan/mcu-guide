# Plan 02 — Gravatar → Google Avatar Fallback & GitHub Pages Deploy

**Status:** done
**Date:** 2026-11-11

## Goal
Automatically fall back to the user's Google OAuth profile picture whenever they do not have a Gravatar configured, persist Google `avatar_url` on comments, and publish local changes to `origin/main` (GitHub Pages).

## Context
- `public.mcu_comments` now has `avatar_url text` in Supabase (executed by owner).
- Gravatar `?d=404` returns HTTP 404 when an email has no Gravatar, enabling clean client-side fallback without third-party proxy failures.

## Proposed changes
1. **`index.html`**:
   - Update `getGravatarUrl(email, size = 64, defaultMode = '404')`.
   - Add `getGoogleAvatarUrl(user)` and shared `handleAvatarError(imgEl, fallbackUrl, fallbackElId)` helper.
   - Wire Gravatar → Google → initials/cloud fallback in `#auth-btn`, `#auth-view-logged-in`, `renderCommentCard`, and `renderReplyCard`.
   - Persist `avatar_url` in `submitComment()`.
2. **Docs & Deploy**:
   - Update `PROJECT.md`, `ROADMAP.md`, `step_02` devlog, `chat-context.md`.
   - Commit & push to `origin/main` (with `chat-context.md` verified gitignored).
   - Verify live deployment on `https://flou-ainan.github.io/mcu-guide/` and send completion email via SMTP.

## Definition of done / how to test
- `node -c` passes on `index.html`.
- Live HTTP check confirms `https://flou-ainan.github.io/mcu-guide/` serves updated code (Google avatar fallback + episode expander + `privacy.html` + `terms.html`).
- SMTP confirmation email delivered to `gabriel8flow@gmail.com`.
