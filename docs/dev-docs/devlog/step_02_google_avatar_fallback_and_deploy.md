# Step 02 — Gravatar → Google OAuth Avatar Fallback & GitHub Pages Deploy

**Date:** 2026-11-11
**Plan:** [plan_02_google_avatar_fallback_and_deploy.md](../planning/plan_02_google_avatar_fallback_and_deploy.md)

## What changed

- **`index.html`**:
  - Updated `getGravatarUrl(email, size = 64, defaultMode = '404')` to request `d=404` instead of `d=identicon` so emails without a Gravatar cleanly trigger `onerror`.
  - Added `getGoogleAvatarUrl(user)` (reads `user_metadata.avatar_url || user_metadata.picture`) and `handleAvatarError(imgEl, fallbackUrl, fallbackElId)` for single-shot image fallback from Gravatar → Google photo → initials/cloud icon.
  - Updated `renderAvatarHTML()` (with `referrerpolicy="no-referrer"` and `data-fallback`), `updateAuthUIState()`, `renderCommentCard()`, and `renderReplyCard()` to cascade Gravatar → Google avatar → initials/cloud.
  - Updated `submitComment()` to persist `avatar_url: getGoogleAvatarUrl(currentUser) || null` to `public.mcu_comments`.
- **Docs**:
  - Updated `docs/PROJECT.md` (`avatar_url` column in schema + `index.html` line count `2361`), `docs/dev-docs/ROADMAP.md`, and marked `plan_02_google_avatar_fallback_and_deploy.md` as `done`.

## Why

Users logging in via Google OAuth who do not have a Gravatar account previously fell back to a generic `identicon` instead of their actual Google profile photo. Using Gravatar `d=404` preserves existing Gravatar photos while falling back smoothly to Google photos (and persisting `avatar_url` on comments so other users see the Google photo too).

## Files touched

- `index.html`
- `docs/PROJECT.md`
- `docs/dev-docs/ROADMAP.md`
- `docs/dev-docs/planning/plan_02_google_avatar_fallback_and_deploy.md`
- `docs/dev-docs/devlog/step_02_google_avatar_fallback_and_deploy.md`
- `docs/dev-docs/chat-context.md` (gitignored)

## How it was tested

- Extracted both `<script>` blocks from `index.html` and verified `node -c` exit code 0.
- Executed a Node unit check against `getGravatarUrl`, `getGoogleAvatarUrl`, `renderAvatarHTML`, and the 2-step `handleAvatarError` cascade (all assertions passed).
- Verified `http://localhost:8080/` serves the updated markup.
- Committed and pushed to `origin/main` and verified live GitHub Pages deployment (`https://flou-ainan.github.io/mcu-guide/`).
