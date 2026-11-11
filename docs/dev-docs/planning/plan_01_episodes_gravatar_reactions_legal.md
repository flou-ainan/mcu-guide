# Plan 01 — Optimistic Reactions, Gravatar Avatars, Series Episode Expander, and Legal Pages

**Status:** done
**Date:** 2026-11-11

## Goal
Improve UX polish, community avatar identity, series episode-level tracking & discussion, and OAuth compliance with Privacy Policy & Terms of Service pages — all tested locally before any git push.

## Context
- Users logging in via Google OAuth or Email/Password need consistent Gravatar avatars in the top navbar, account modal, and comments/replies.
- Comment reactions currently call `loadComments()`, flashing a loading spinner and resetting scroll/draft state.
- Series cards currently only allow marking the entire series, whereas MCU fans want to expand seasons/episodes, inspect thumbnails and synopses, track watched progress per episode, and comment on individual episodes (without trailers or IMDb buttons).
- Google Auth Platform branding requires public Privacy Policy and Terms of Service pages.

## Proposed changes
1. **`scraper.py`, `mcu_data.json`, `data.js`**:
   - Fetch series episode metadata & thumbnails from Stremio Cinemeta (`v3-cinemeta.strem.io`) using existing `imdb_id`.
   - Filter episodes by series chronological split (`aos_s1` ep 1-16, `aos_s1_end` ep 17-22, `daredevil_s1` S1, `loki_s1` S1-2, `whatif` S1-3, etc.).
   - Translate episode titles and synopses to PT-BR with caching in `mcu_data.json`.
2. **`index.html`**:
   - Add pure-JS MD5 helper + `getGravatarUrl(email)` for top navbar `#auth-btn`, `#auth-view-logged-in`, comments, and replies.
   - Replace reaction reload spinner with optimistic cache update + targeted DOM refresh / non-blocking Supabase sync.
   - Add Episode Expander accordion inside series cards (`#episodes-panel-${seriesId}`) showing episode checkboxes, thumbnails, seasons, and clickable sub-cards with synopsis + discrete comments drawer (no trailers / no IMDb).
   - Preserve open accordion/episode/comments states across checkbox re-renders (`openDetailsIds`, `openEpisodesPanels`, `openEpisodeDetailsIds`).
   - Add footer links to `privacy.html` and `terms.html`.
3. **`privacy.html` & `terms.html`**:
   - Create standalone dark-themed pages consistent with `index.html`.
4. **Docs**:
   - Record ADR-001, step_01 devlog, update `PROJECT.md`, `ROADMAP.md`, and `chat-context.md`.

## Definition of done / how to test
- Run `scraper.py` and verify all 15 series entries contain non-empty `episodes` with valid titles, synopses, and thumbnail URLs.
- Extract `<script>` from `index.html` and validate syntax with `node -c`.
- Serve on `http://localhost:8080/` and verify pages load (HTTP 200 for `index.html`, `privacy.html`, `terms.html`, `data.js`, `mcu_data.json`).
- Send completion email via SMTP from `flouainan@gmail.com` to `gabriel8flow@gmail.com`.
