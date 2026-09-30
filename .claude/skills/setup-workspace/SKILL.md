---
name: setup-workspace
description: The one entry point for setting up this uni workspace from scratch or finishing a half-done setup. Chains the other skills in order (setup-obsidian, then setup-year, then the optional extras such as tasks and HOME, flashcards, study timetable, weekly review, careers), invoking each one as a skill and skipping whatever is already done. Use when the student says "set up", "set up everything", "get started", "set up the workspace", "finish setting up", or opens a fresh clone where projects/PROFILE.md doesn't exist yet.
---

# Set up the workspace

This is the front door. It doesn't do the work itself: it **invokes the other setup skills in order**, using the
skill tool, so each runs exactly as written. **Never read another skill's SKILL.md and improvise from it.** If a
skill isn't available in this session, stop and ask the student to start a new session in this folder (skills load
when a session starts here), then say "set up" again.

Every step checks whether it's already done, so running "set up" again after a break carries on where it stopped.

## 0. Where are we?
Check, and tell the student in one short list what's done and what's next:
- **This session is in the workspace folder** (it has `CLAUDE.md` and `.claude/skills/`). If not, stop: tell them to
  open a new Code session in the `uni-workspace` folder and say "set up" there.
- **Obsidian:** `.obsidian/` exists (the folder has been opened as a vault) and `.obsidian/snippets/dashboard.css`
  exists (setup-obsidian has run).
- **Year:** `projects/PROFILE.md` exists and at least one module folder (setup-year has run).
- **Extras:** `HOME.md`, `tasks/TASKS.md`, `timetable/`, any `flashcards/`, `careers/BRIEF.md`.

## 1. Open the vault in Obsidian
If `.obsidian/` doesn't exist, ask them to open Obsidian → **Open folder as vault** → this folder, and wait until they
say it's open. (Obsidian creates `.obsidian/` then.) Don't hunt for the app or install it yourself (no Homebrew,
winget or downloads): if they don't have it, give them https://obsidian.md/download and wait. That's the student's
install, like the plugins.

## 2. Obsidian setup
If `dashboard.css` isn't installed yet, **invoke the `setup-obsidian` skill** and let it finish (plugins, theme,
styling, reload). Skip if it's done.

## 3. The year
If `projects/PROFILE.md` doesn't exist, **invoke the `setup-year` skill** and let it finish (profile, Moodle login by
the student, modules, assessments, DEADLINES). Skip if it's done, but if they say modules are missing, invoke
`add-module` for each.

## 4. Extras (one question)
Ask once which of these they want now. Each can also be added later by asking, and none is required:

| Extra | How |
|---|---|
| **Home dashboard + tasks** (recommended) | Copy `projects/_template/HOME.md` to the root and `tasks/_template/TASKS.md` into `tasks/`. Remove HOME cards and header pills (HOME and TASKS) for anything not set up yet, e.g. Timetable, Careers, Review, Moodle before the first sync. Remove the template note |
| **Study timetable** | Invoke `create-study-timetable` (it needs their lecture timetable; an `.ics` export is best) |
| **Flashcards** for exam-heavy modules | Invoke `create-flashcards` once per module they pick |
| **Weekly review** on Sunday evenings | Invoke `weekly-review` and follow its "Schedule it" section |
| **Careers** (grad roles, internships, placements) | Invoke `setup-careers` |

Do them one at a time, in the order they chose. After each, re-add the matching HOME card or pill if HOME exists.

## 5. Finish
- Offer a first **"refresh Moodle"** (invoke `sync-moodle`) so the baseline exists and `projects/updates/MOODLE.md` is created.
- Reply with: what's set up, a table of modules (credits, semester, assessment), the next three deadlines, anything
  `_tbc_`, and what to say next: "what's due?", "refresh Moodle" (weekly), "quiz me on <module>", "weekly review".
- Next time they open the folder (in Claude and Obsidian), there's nothing to set up. They just talk.
