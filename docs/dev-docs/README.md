# Development documentation conventions

The whole history of the project lives as markdown inside the repository. This is a contingency: even without ai-memory or any agent memory, anyone who clones the project can see what exists, what was done, and what is in progress.

All files here are written in **English**.

## Layout

```
docs/
├── PROJECT.md              # project map, always up to date
└── dev-docs/
    ├── README.md           # this file
    ├── ROADMAP.md          # the one list of what is left (start here to pick work)
    ├── chat-context.md     # lean summary of the owner ↔ agent conversation + last two full replies (gitignored)
    ├── planning/           # plans, written before implementing
    ├── devlog/             # one step per change or executed stage
    ├── decisions/          # ADRs: technical decisions and their reasons
    └── references/         # background material, screenshots, schemas
```

## `chat-context.md`: conversation hand-off

Long agent conversations consume a lot of tokens. `chat-context.md` lets a new session, or another agent, pick up the conversation without the full transcript.

- **Contents:**
  - a lean summary of the whole owner ↔ agent conversation: what was asked and decided, the owner's preferences, open questions, and what is in progress;
  - the **last two complete replies** of the agent, verbatim. They stay in the language they were written in; the rest is in English.
- **Privacy:** it is ignored in `.gitignore` to prevent leaking private conversations or uncommitted notes.
- Replace the file on update. Do not append.

## `docs/PROJECT.md`

A condensed file that helps agents and people find what they need fast, without rereading the code.

**Rule:** every change to the project updates `PROJECT.md` in the same commit. Count lines with `wc -l`.
