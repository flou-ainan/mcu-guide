# Plan 03 — Card Canon Badges, Watched Fade Scope, Series Progress Bar UX & Labels

**Status:** done
**Date:** 2026-11-11

## Goal
Refine visual hierarchy, mobile readability, and progress feedback across movie and series cards without breaking dark-mode aesthetics or episode tracking.

## Proposed changes

1. **Canon badges (`index.html`)**:
   - Replace `MCU Canon` with `Canônico MCU` and `Ignorável` with `Não Canônico`.
   - Render as a compact badge anchored at the top-right corner of every card (`-top-2.5 right-3`) on both desktop and mobile viewports (with `space-y-4` on `#timeline-container` so cards do not collide).
2. **Scoped watched fade (`index.html`)**:
   - Remove outer `opacity-55` / `opacity-60` / `opacity-65` from card and episode wrappers so expanded panels (`#details-*`, `#ep-details-*`, `#episodes-panel-*`, `#comments-section-*`) remain at full 100% brightness and contrast.
   - Apply subtle fade (`opacity-65 hover:opacity-95 transition-opacity`) only to the collapsed summary header row when watched.
3. **Series progress bar & percentage UX (`index.html`)**:
   - Show a progress bar + percentage (`%`) directly on collapsed series cards whenever `watchedEps > 0`.
   - Hide the card-level progress bar when the series card is expanded (`#details-*` open), keeping the bar + percentage visible inside the `Episódios` button on both mobile and desktop.
   - Sync visibility in `toggleDetails` and `openSeriesEpisodesDirect` via `syncSeriesCardProgressVisibility`.
4. **Navbar GitHub & series comments labels (`index.html`)**:
   - Update navbar GitHub link text to `Conheça o projeto` on wide screens (`hidden md:inline`) while preserving the GitHub icon on all screens.
   - Add `Comentários` label to the series comments button (shared helper `renderCommentsTriggerButton`) matching movies and episodes.
5. **Docs & Local Notification**:
   - Update `PROJECT.md`, `ROADMAP.md`, `plan_03` (`done`), `step_03` devlog, `chat-context.md`.
   - Verify locally on `http://localhost:8080/` (desktop + mobile viewport) and send SMTP confirmation email to `gabriel8flow@gmail.com`.

## Definition of done / how to test
- `node -c` passes on `index.html`.
- Live browser inspection on `http://localhost:8080/` (desktop + 360px mobile) verifies badges, scoped fade on expanded watched items, collapsed vs expanded series progress bar + percentage, GitHub label, and series `Comentários` button with 0 console errors.
- Confirmation email sent via SMTP.
