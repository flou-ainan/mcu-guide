# Step 04 — Markdown Fixes, Preview Toggle, Replies Label & Ignorável Badge

**Date:** 2026-11-11
**Plan:** [plan_04_markdown_preview_replies_ignorable.md](../planning/plan_04_markdown_preview_replies_ignorable.md)

## What changed

- **`index.html`**:
  - Pinned `marked@15/marked.min.js` and loaded `dompurify@3/dist/purify.min.js`.
  - Added `.comment-markdown` CSS rules in `<style>` so headings (`h4..h6`), paragraphs, bullet/ordered/task lists, blockquotes, inline/fenced code, links, tables, horizontal rules, and images render crisply in dark mode instead of being wiped by Tailwind CSS Preflight.
  - Constrained embedded Markdown images (`max-width: 100%`, `max-height: 220px`, `object-fit: contain`, `loading="lazy"`, `referrerpolicy="no-referrer"`, `cursor: zoom-in`) and wired a delegated click handler on `.comment-markdown img` to open `#image-modal`.
  - Implemented `getCommentMarkdownRenderer()` + `isSafeExternalUrl()` + `DOMPurify.sanitize()` inside `parseMarkdownSafe()` to map `#..###` headings to `h4..h6` (normalized comment typography), neutralize raw HTML/XSS (`javascript:`/`onerror`), and enforce `target="_blank" rel="noopener noreferrer nofollow"` on links.
  - Added **Escrever / Preview** tab selector (`setCommentEditorMode`) and `#comment-preview-*` container in `renderCommentsUI`.
  - Replaced `prose prose-invert prose-xs` with `comment-markdown` in `renderCommentCard` and `renderReplyCard`, and added the `RESPOSTAS (${replies.length})` label above nested replies.
  - Changed the series top-right badge from `Não Canônico` to `Ignorável`.
- **Docs**:
  - Created `plan_04_markdown_preview_replies_ignorable.md` and `step_04_markdown_preview_replies_ignorable.md`.
  - Updated `docs/PROJECT.md` (`index.html` line count `2617`), `docs/dev-docs/ROADMAP.md`, and `docs/dev-docs/chat-context.md` (gitignored).

## Why

Tailwind CDN did not include `@tailwindcss/typography` (`prose` / `prose-xs`), so Tailwind Preflight reset every Markdown tag (`h1..h6`, `ul`, `ol`, `blockquote`, `code`) into plain unstyled text and left comments vulnerable to arbitrary raw HTML or oversized images. Adding scoped `.comment-markdown` CSS, normalized headings, bounded images, `DOMPurify`, an interactive preview toggle, and clear `RESPOSTAS` / `Ignorável` labels resolves both aesthetics and security.

## Files touched

- `index.html`
- `docs/PROJECT.md`
- `docs/dev-docs/ROADMAP.md`
- `docs/dev-docs/planning/plan_04_markdown_preview_replies_ignorable.md`
- `docs/dev-docs/devlog/step_04_markdown_preview_replies_ignorable.md`
- `docs/dev-docs/chat-context.md` (gitignored)

## How it was tested

- Verified JS syntax of both `<script>` blocks via `node -c` (exit code `0`).
- Tested in live browser at `http://localhost:8080/`: confirmed `marked@15` and `dompurify@3` load with HTTP 200, 0 console errors, 15 series cards display `Ignorável` (0 `Não Canônico`), 37 movie cards display `Canônico MCU`, and inspected `.comment-markdown` styles directly.
- Executed Node `vm` checks against real `marked@15.0.12` confirming `#..###` -> `h4..h6`, lists, blockquotes, inline code, links, bounded lazy `img`, and neutralization of `<script>`, `<img onerror>`, and `javascript:` payloads (`ALL_MARKDOWN_V15_CHECKS_PASSED`).
- Sent SMTP confirmation email to `gabriel8flow@gmail.com`.
