# Backlog

Done: `create-flashcards`, `create-study-timetable`.

Ideas for the template, roughly in priority order. Keep the base template small: each new feature should be
something `setup-year` offers as an optional step, not something every student gets by default.

## Next

### Tasks and HOME dashboard
Port `tasks/` (TASKS.md, Tasks.base, template) and HOME.md + Home.base from the personal workspace, generalised.
`whats-due` already has an uncommitted change that reads task notes and the calendar.

### `weekly-review` skill
A Sunday review: last week's done items, next week's events, deadlines and tasks, and 3 suggested priorities.
Calendar and email are optional inputs that it skips if they're not connected. It can also run as a scheduled task.

## Later
- **`exam-practice` skill:** exam-style questions on Tier A/B results. The student sends a photo of a handwritten
  answer, which is marked against the notes and solutions, and weak spots are logged in the tiers page.
- **Planning back from coursework deadlines:** when a brief arrives, split it into 3–5 dated tasks linked to
  the assessment. This is probably a rule in TASKS.md rather than a new skill.
- **Recommended Obsidian plugins** in the README: Spaced Repetition, Full Calendar Remastered (both already
  mentioned by their skills), and the built-in
  Templates plugin pointed at the `_template` folders.
- **A start-of-session hook** that prints anything due in the next 3 days. Only once the above are in.
