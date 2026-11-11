# Step 03 — Card Canon Badges, Watched Fade Scope, Series Progress Bar UX & Labels

**Date:** 2026-11-11
**Plan:** [plan_03_card_badges_fade_progress_ux.md](../planning/plan_03_card_badges_fade_progress_ux.md)

## What changed

- **`index.html`**:
  - Replaced `MCU Canon` / `Ignorável` with top-right floating pill badges `Canônico MCU` and `Não Canônico` (`-top-2.5 right-3`) visible on both desktop and mobile viewports (`#timeline-container` updated to `space-y-4` for clean spacing).
  - Removed outer `opacity-55` / `opacity-60` / `opacity-65` from watched movie, series, and episode wrapper cards; moved fade (`opacity-60 hover:opacity-95` / `opacity-65 hover:opacity-95`) solely onto the collapsed header summary row so expanded synopses, trailers, episode lists, and community comments remain at 100% brightness (`opacity: 1`).
  - Added `#series-card-progress-${id}` bar + percentage (`%`) directly on collapsed series cards whenever `watchedEps > 0`.
  - Updated `toggleCollapsible` (returns `willOpen`), added `syncSeriesCardProgressVisibility`, and wired `toggleDetails` and `openSeriesEpisodesDirect` so the collapsed card progress bar turns off when the series card expands and stays visible inside the `Episódios` header button (now shown on both mobile and desktop alongside percentage `%`).
  - Updated the navbar GitHub link text to `Conheça o projeto` on wide screens (`hidden md:inline`) while preserving the GitHub icon across all viewports.
  - Extracted shared `renderCommentsTriggerButton` helper so series cards display the `Comentários` label matching movies and episodes.
- **Docs**:
  - Created `plan_03_card_badges_fade_progress_ux.md` and `step_03_card_badges_fade_progress_ux.md`.
  - Updated `docs/PROJECT.md` (`index.html` line count `2377`), `docs/dev-docs/ROADMAP.md`, and `docs/dev-docs/chat-context.md` (gitignored).

## Why

- Mobile viewers lacked canon/non-canon classification labels and the series episode progress bar.
- Applying CSS `opacity` on the outer card dimmed expanded synopses and discussion threads; scoping opacity to the collapsed summary header keeps watched cards visually distinct while keeping expanded content crisp and readable.
- Showing progress `%` on collapsed series cards when partial progress exists gives instant feedback without redundant bars once expanded.

## Files touched

- `index.html`
- `docs/PROJECT.md`
- `docs/dev-docs/ROADMAP.md`
- `docs/dev-docs/planning/plan_03_card_badges_fade_progress_ux.md`
- `docs/dev-docs/devlog/step_03_card_badges_fade_progress_ux.md`
- `docs/dev-docs/chat-context.md` (gitignored)

## How it was tested

- Extracted both `<script>` blocks from `index.html` and verified `node -c` exit code `0`.
- Tested live in headless browser on `http://localhost:8080/` across desktop (`1280x800`) and mobile (`360x800`) viewports (0 console errors, 0 horizontal overflow):
  - Verified `Canônico MCU` and `Não Canônico` top-right badges visible on both desktop and mobile.
  - Verified watched movie header has `opacity: 0.6` while expanded `#details-im1` has `opacity: 1`.
  - Verified Echo series progress bar (`40%`) hidden at `0/5`, visible when `2/5` and collapsed, and hidden on the main card when expanded while showing `2/5 assistidos 40%` inside `Episódios` on desktop and mobile.
  - Verified GitHub link shows `Conheça o projeto` on desktop and icon-only on 360px mobile, and series comments button displays `Comentários`.
- Sent SMTP confirmation email to `gabriel8flow@gmail.com`.
