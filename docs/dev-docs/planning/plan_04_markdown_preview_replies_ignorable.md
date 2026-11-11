# Plan 04 — Markdown Fixes, Preview Toggle, Replies Label & Ignorável Badge

**Status:** done
**Date:** 2026-11-11

## Goal
Fix comment Markdown rendering (which currently renders flat due to Tailwind CSS Preflight + unloaded `@tailwindcss/typography`), normalize heading sizes and image dimensions following comment Markdown best practices, add an interactive Escrever/Preview toggle in the comment editor, label nested reply threads (`RESPOSTAS`), and rename `Não Canônico` back to `Ignorável`.

## Proposed changes

1. **Dependencies & Scoped Markdown Styles (`index.html`)**:
   - Pin `marked@15/marked.min.js` and load `dompurify@3/dist/purify.min.js`.
   - Add `.comment-markdown` CSS rules in `<style>` for normalized headings (`h4`/`h5`/`h6`), paragraphs, lists, task checkboxes, blockquotes, inline/fenced code, links, tables, horizontal rules, and bounded images (`max-height: 220px`, `max-width: 100%`, `object-fit: contain`, `cursor: zoom-in`).
   - Add delegated click listener on `.comment-markdown img` to open the existing `#image-modal`.
2. **Safe Markdown Parser (`index.html`)**:
   - Configure custom `marked.Renderer` in `getCommentMarkdownRenderer()` / `parseMarkdownSafe()` to cap headings (`h4`–`h6`), escape raw HTML tokens, enforce `https?://` / `mailto:` protocols, force `target="_blank" rel="noopener noreferrer nofollow"` on links, and constrain images (`loading="lazy"`, `referrerpolicy="no-referrer"`).
   - Sanitize rendered HTML through `DOMPurify.sanitize(...)`.
3. **Comment Editor Preview & Replies Label (`index.html`)**:
   - Add **Escrever / Preview** tab selector (`setCommentEditorMode`) in the comment composer (`renderCommentsUI`) with live Markdown preview (`#comment-preview-*`).
   - Add a `RESPOSTAS (${replies.length})` header label above nested replies in `renderCommentCard`.
   - Replace `prose prose-invert prose-xs` with `comment-markdown` in both `renderCommentCard` and `renderReplyCard`.
4. **Badge Rename (`index.html`)**:
   - Change series top-right badge text from `Não Canônico` to `Ignorável`.
5. **Docs & Local Verification**:
   - Update `PROJECT.md`, `ROADMAP.md`, `plan_04` (`done`), `step_04` devlog, `chat-context.md`.
   - Verify locally via `node -c` and live browser (`http://localhost:8080/` desktop + mobile) including Markdown formatting, heading sizes, image sizing, Escrever/Preview toggle, XSS sanitization, `RESPOSTAS` label, and `Ignorável` badge.
   - Send completion email via SMTP to `gabriel8flow@gmail.com`.

## Definition of done / how to test
- `node -c` passes on `index.html`.
- Live browser check at `http://localhost:8080/` confirms Markdown headings, lists, bold, code, blockquotes, links, bounded images, Escrever/Preview switching, XSS payload neutralization, `RESPOSTAS` label, and `Ignorável` badge with 0 console errors.
- Confirmation email sent via SMTP.
