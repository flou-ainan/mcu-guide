# Step 06 — Watched Status Filter, Profile Customization, Responsive Order Toggle & Release Push

**Date:** 2026-11-11
**Plan:** [plan_06_watched_filter_and_profile_customization.md](../planning/plan_06_watched_filter_and_profile_customization.md)
**Scope:** Implemented final Roadmap items (`Filter by watched status`, `Profile avatar & username customization`, `Chronological vs Release order toggle polish`), verified Supabase SQL migration (`edited_at`, `edit_history`), and prepared release commit & push (`Steps 03–06`) to `origin/main` (GitHub Pages).

## What changed

1. **Watched Status Filter (`index.html`):**
   - Added 3-state status toggle bar (`Todos`, `Não assistidos`, `Assistidos`) next to phase chips (`setWatchedStatusFilter`).
   - Updated `renderList()` to filter items against `watchedIds` (`selectedStatus`), keeping immediate live updates when checking/unchecking cards.

2. **Profile Display Name & Avatar Customization (`index.html`):**
   - Added `getDisplayName`, `getCustomAvatarUrl`, `getPreferredAvatarConfig`, `getCommentAvatarProps`, `previewProfileAvatar`, `clearCustomAvatarField`, and `saveUserProfile`.
   - Added inline **Personalizar Perfil** form inside `#auth-view-logged-in` allowing logged-in users to customize their `display_name` and `custom_avatar_url` (stored via `supabaseClient.auth.updateUser({ data })`) or revert cleanly to Gravatar/Google defaults.
   - Propagated customized display names and avatars to `#auth-btn`, auth modal preview, new comments (`submitComment`), and existing authored rows in `public.mcu_comments` (`update({ user_name, avatar_url }).eq('user_id', currentUser.id)`).

3. **Chronological vs Release Order Toggle Responsive Polish (`index.html`):**
   - Updated `#btn-order-release` / `#btn-order-chrono` container to `flex-wrap sm:flex-nowrap` with compact mobile typography and adaptive `Ordem de Lançamento` / `Lançamento` label so mobile (`360x800`) fits with zero horizontal overflow (`document.documentElement.scrollWidth <= window.innerWidth`).

## Files touched

- `index.html` (3383 lines)
- `docs/PROJECT.md`
- `docs/dev-docs/ROADMAP.md`
- `docs/dev-docs/planning/plan_06_watched_filter_and_profile_customization.md`
- `docs/dev-docs/devlog/step_06_watched_filter_profile_customization_deploy.md`

## How it was tested

- Supabase REST verification confirmed `edited_at` and `edit_history` columns live on `public.mcu_comments` (`HTTP/2 200`).
- `node -c` syntax checks passed on `index.html` inline JS and `data.js`.
- Node `vm` unit checks passed for `getDisplayName`, `getCustomAvatarUrl`, `getPreferredAvatarConfig`, `renderAvatarHTML`, and `getCommentAvatarProps` priority ordering.
- Interactive headless browser test at `http://localhost:8080/`:
  - Desktop (`1280x800`): 52 cards loaded, 0 console/page errors, 0 HTTP >= 400 errors; verified `Assistidos` (2), `Não assistidos` (50), and `Todos` (52) filter counts.
  - Mobile (`360x800`): verified `#auth-modal` (`#profile-display-name`, `#profile-avatar-url`), toggled `Cronológica` & `Lançamento`, and confirmed zero horizontal overflow (`body` width `353.57px <= 360px`) with 0 console/page errors and 0 HTTP errors.
