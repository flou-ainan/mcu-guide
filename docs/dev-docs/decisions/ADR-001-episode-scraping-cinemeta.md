# ADR 001 — Episode Metadata via Cinemeta & Unified Episode Progress/Comments

**Status:** accepted
**Date:** 2026-11-11

## Context
Each MCU series in `mcu_data.json` needs episode-level tracking (watched checkboxes), episode thumbnails, synopses in Portuguese, and per-episode discussions, without adding API keys, build steps, or breaking existing Supabase schemas.

## Decision
1. **Episode scraping source:** Use Stremio's public Cinemeta JSON API (`https://v3-cinemeta.strem.io/meta/series/<imdb_id>.json`), paired with `episodes.metahub.space` 780px landscape thumbnails and cached PT-BR translations in `mcu_data.json` / `data.js`.
2. **Chronological series slicing:** Map split series entries (`aos_s1`, `aos_s1_end`, `daredevil_s1`, `loki_s1`, `whatif`, etc.) by explicit season/episode bounds inside `scraper.py`.
3. **Progress & Comments compatibility:** Store episode watched state in the existing `watched_ids` array (e.g., `wandavision-s1e1`) and pass the same episode ID as `movie_id` into `mcu_comments`, avoiding any Supabase schema migration.
4. **Avatars:** Compute email MD5 client-side to render Gravatar URLs (`d=identicon`) consistently across navbar, account modal, comments, and replies.

## Alternatives considered
- **TMDB API:** Requires personal API keys in `scraper.py`.
- **Separate `mcu_episode_comments` table:** Unnecessary schema duplication since `mcu_comments.movie_id` is `text`.

## Consequences
- Zero runtime API calls needed to list episodes or synopses; instant offline-first UX.
- Thumbnails load externally from `episodes.metahub.space` with `<img onerror>` fallback to the series cover poster.
- Checking all episodes of a series automatically marks the parent series watched; unchecking any episode unmarks the parent series while preserving remaining watched episodes.
