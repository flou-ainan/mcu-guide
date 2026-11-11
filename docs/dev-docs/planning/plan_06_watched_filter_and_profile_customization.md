# Plan 06 — Watched Status Filter & Profile Avatar/Username Customization

**Status:** done
**Date:** 2026-11-11

## Goal
Implement the remaining roadmap features (`Filter by watched status` and `Profile avatar & username customization`), verify live behavior (including Supabase `edited_at`/`edit_history` migration & profile updates), update documentation, push all changes (Steps 03–06) to GitHub Pages, and notify the owner via email.

## Proposed changes

1. **Watched Status Filter (`index.html`):**
   - Add a 3-state segmented filter control (`Todos`, `Não assistidos`, `Assistidos`) next to the search & series visibility controls, keeping responsive wrapping cleanly on mobile (`360px`) and desktop.
   - Track `selectedStatus` (`'all' | 'unwatched' | 'watched'`), add `setWatchedStatusFilter(status)`, filter items in `renderList()`, and ensure toggling checkboxes immediately re-evaluates the filtered view.
2. **Profile Display Name & Avatar Customization (`index.html`):**
   - Add `getDisplayName(user)` (`user_metadata.display_name` -> `user_metadata.full_name` -> email prefix) and `getPreferredAvatarUrl(user)` (`user_metadata.custom_avatar_url` -> Gravatar `404` -> Google `avatar_url`/`picture`).
   - Update navbar pill (`#auth-btn-label` with `truncate`, `#auth-btn-avatar`), `#auth-view-logged-in`, `submitComment`, `renderCommentCard`, and `renderReplyCard` to use these helpers.
   - Add an inline **Personalizar Perfil** form inside `#auth-view-logged-in` (`#profile-display-name`, `#profile-avatar-url`, reset-to-default helper, live preview, Save button).
   - `saveUserProfile(event)` persists `display_name` & `custom_avatar_url` in Supabase Auth (`supabaseClient.auth.updateUser({ data })`) and propagates updated `user_name` / `avatar_url` to the author's existing rows in `public.mcu_comments`, refreshing UI and any open comment drawers immediately.
3. **Verification, Docs & Release (`git push` + email):**
   - Verify syntax (`node -c`), Node `vm` assertions for `selectedStatus` filtering and profile helpers, live Supabase schema check (`edited_at`, `edit_history`), and interactive browser verification at `http://localhost:8080/` (desktop + mobile, 0 console errors).
   - Update `plan_06` (`done`), `step_06` devlog, `ROADMAP.md`, `PROJECT.md`, and `chat-context.md`.
   - Commit clean changes, push to `origin/main` (GitHub Pages), verify live Pages availability/commit status, and send completion email to `gabriel8flow@gmail.com`.

## Definition of done / how to test
- `Todos / Não assistidos / Assistidos` filter switches card list cleanly and syncs with checkbox toggles.
- Navbar, auth modal profile panel, and comment helpers resolve `display_name` and `custom_avatar_url` with safe URL validation and Gravatar/Google fallback.
- Desktop (`1280x800`) and Mobile (`360x800`) render cleanly with 0 console errors.
- Changes pushed to `origin/main` and confirmation email sent.
