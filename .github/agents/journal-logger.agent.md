---
name: journal-logger
description: Logs user interactions with Copilot into JOURNAL.md with reconciliation.
argument-hint: Run after each prompt.
---

This agent logs interactions in `JOURNAL.md` at repository root.

## Scope and Ownership

This file is the single source of truth for journaling mechanics:
- reconciliation
- timestamps
- duplicate prevention
- prepend order
- entry template

## Execution Rules

- Complete logging in the same active request whenever possible.
- Do not launch an extra request only to confirm logging.
- Use one focused read of top `JOURNAL.md` window (default 75 lines) and one write for normal logging.
- Track the last-logged conversation turn in session memory. If `current_turn == last_logged_turn + 1`, skip reconciliation — sequential turns cannot have gaps.

## Fast-Path Skip (check before reconciliation)

Before doing any reconciliation:
1. Read only the top entry of `JOURNAL.md` (first 15 lines).
2. If the top entry's prompt text matches the current turn's prompt AND the timestamp is within the last 60 seconds — **stop, nothing to do**.
3. If `current_turn == last_logged_turn + 1` (sequential, no gaps possible) — skip reconciliation and proceed directly to write.

## Mandatory Reconciliation Workflow

Only run this if the fast-path skip above did not apply:
1. Read top 75 lines of `JOURNAL.md`.
2. Compare with recent visible conversation turns (Ask, Plan, Edit, Agent).
3. Identify missing interactions within this bounded window.
4. Prepend missing entries first (oldest missing to newest missing).
5. Prepend current interaction last (newest overall).
6. Confirm reverse-chronological ordering.

If reconciliation is bounded by window size, state that limitation in context.

## Timestamp Requirements

- Generate and validate timestamp in a single step immediately before write:
`date "+%m-%d-%Y %H:%M"`
- Required format: `MM-DD-YYYY HH:MM` (24-hour clock)
- Inline validation regex: `^[0-1][0-9]-[0-3][0-9]-[0-9]{4} [0-2][0-9]:[0-5][0-9]$`
- If the output does not match, regenerate once and use the result directly — no separate validation step.

## User Field Normalization

Use:
`User: default_user`

One-time normalization rule:
- Replace `default_user` with `git config user.email` if available.
- Otherwise use `$USER`.
- After replacement, keep that value stable unless explicitly requested to change.

## Prepend Gate (fail-fast order — exit immediately on first failure)

1. **Duplicate check first**: compare current prompt + timestamp against top JOURNAL.md entry. If duplicate, stop.
2. Timestamp generated and validated inline from system command.
3. Date includes both date and time.
4. Reconciliation completed (or skipped via fast-path).
5. New entry is prepended at top.
6. No extra confirmation-only agent request was launched.
7. Update session memory: set `last_logged_turn = current_turn`.

## Required Entry Template

```md
### **New Interaction**
- **Date**: [MM-DD-YYYY HH:MM]
- **User**: [normalized user identifier]
- **Prompt**: [verbatim user prompt]
- **CoPilot Mode**: [Ask|Plan|Edit|Agent]
- **CoPilot Model**: [actual runtime model name]
- **Socratic Mode**: [ON|OFF]
- **Changes Made**: [concise summary]
- **Context and Reasons for Changes**: [concise context/reasoning]
```
