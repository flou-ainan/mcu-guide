# Agent instructions

Applies to every agent (Claude Code, Gemini/Antigravity, OpenCode, Copilot, Codex, ...).

## Before you start

1. Read `docs/PROJECT.md`: overview, stack, decisions, and a file map with line counts and functions.
2. Read `docs/dev-docs/ROADMAP.md` (the one list of what is left; pick work from it, not from the latest plan), `docs/dev-docs/chat-context.md` (the conversation so far, condensed), the latest step in `docs/dev-docs/devlog/`, and any open plan in `docs/dev-docs/planning/` to see what is in progress.
3. Only then open the source files related to the task. Do not scan the whole repository when the docs already answer the question.

## Documentation rules (mandatory)

Full conventions: `docs/dev-docs/README.md`. Summary:

- **Every plan becomes a file** in `docs/dev-docs/planning/` before implementation starts.
- **`docs/dev-docs/ROADMAP.md` is the single list of pending work.** Keep it in step with the plans: a new idea goes in a column, a finished item moves to "Done" with its step number, and a plan whose items are all done gets `Status: done`.
- **Every change is logged** as a step in `docs/dev-docs/devlog/`: what changed, why, files touched, how it was tested.
- **Every relevant technical decision** (library, architecture, format) becomes an ADR in `docs/dev-docs/decisions/`.
- **`docs/PROJECT.md` always reflects the current code.** Any change to files, functions, stack, or folder layout updates `PROJECT.md` in the same commit, including line counts.
- **Conversation hand-off:** keep `docs/dev-docs/chat-context.md` up to date: a lean summary of the whole conversation with the owner, plus the last two complete replies verbatim. Always ensure it is in `.gitignore` so no personal tokens/chat leaks occur.

## Language policy

- **English** for developer-facing documentation: dev docs, `PROJECT.md`, plans, devlogs, ADRs, code identifiers, comments, and commit messages.
- **Brazilian Portuguese (`pt-BR`)** for direct interaction with the owner and user-facing UI content.

## Product direction & Guidelines

- **Standalone single-page web app** with zero build-step overhead (Tailwind CDN, vanilla modern JS).
- **Offline first & cloud sync**: LocalStorage works immediately without login; Supabase provides optional cross-device cloud sync and public discussions.
- **Local testing first**: Never push code directly to GitHub without user authorization. Keep changes local for rapid iteration and testing (`python3 -m http.server 8080`).

## Cross-agent memory

This project uses [ai-memory](https://github.com/akitaonrails/ai-memory) to carry context between agents. The source of truth for project state is always `docs/`.

## Recommending the model for the next task

When you finish a task, end your reply to the owner with the model tier and reasoning effort the **next** task needs:
`**Next task:** <what> — tier: standard|top, effort: low|medium|high — <one-line reason>`.
