# Uni workspace

This folder is a university workspace run with Claude Code. One folder per module, one file per module
(`MODULE.md`) as the source of truth, and a single deadline list across the year. Read this file first in every
session.

## About me
@projects/PROFILE.md

If `projects/PROFILE.md` doesn't exist yet, this workspace hasn't been set up. Suggest running the
`setup-year` skill ("set up my year") before doing anything else.

## Layout
```
./
├── CLAUDE.md                  ← this file (shared rules, safe to publish)
├── .claude/skills/            ← setup-year, sync-moodle, add-module, whats-due, create-flashcards, setup-careers, find-roles, prep-application
├── careers/                   ← grad roles / internships / placements (private, git-ignored)
│   ├── CV.md, cv.pdf          ← my CV: the only source of truth for my experience
│   ├── BRIEF.md               ← what I'm looking for: role types, titles, hard requirements, targets
│   ├── SOURCES.md             ← job sites and employer pages to check
│   ├── TRACKER.md             ← (optional) which tracker is in use: Obsidian Bases or a spreadsheet
│   ├── ROLES.md, APPLICATIONS.md ← Markdown tracker (default, when there's no TRACKER.md)
│   ├── Roles.base             ← Obsidian Bases view over the role notes (Bases tracker)
│   ├── digests/               ← one dated search digest per run
│   ├── roles/<id>.md          ← one note per role with properties (Bases tracker)
│   └── roles/<id>/            ← per-application: job description, fit map, drafts, interview prep
└── projects/
    ├── PROFILE.md             ← who I am: uni, degree, year, VLE link (private, git-ignored)
    ├── DEADLINES.md           ← deadlines page: embeds Deadlines.base (private)
    ├── Deadlines.base         ← views over all assessment notes: Due next · Graded only · By module · Board · Done
    ├── Modules.base           ← table / cards of all modules
    ├── _template/             ← copied for each new module (MODULE.md, assessment.md, bases)
    └── <CODE>-<short-name>/   ← one folder per module (private), e.g. CM30001-machine-learning/
        ├── MODULE.md          ← spec (properties + outcomes, timetable, readings, log); embeds its assessments
        ├── assessments/       ← one note per assessment: <CODE>-<slug>.md with due, weight, status, mark
        ├── lectures/          ← notes, one file per week: week-03-sorting.md
        ├── coursework/        ← one subfolder per assessment: brief, drafts, feedback
        ├── flashcards/        ← (optional) cards.md source → Obsidian flashcard notes (+ Anki deck) (create-flashcards)
        └── resources/         ← PDFs, slides, past papers, formula books
```

## Working with modules
- **Before answering anything about a module**, read its `MODULE.md`, then the relevant lectures and
  coursework files. Quote deadlines and weightings from the assessment notes. Never guess them.
- **New material I share** (lecture notes, briefs, feedback) goes into the right subfolder with a clear,
  lowercase-hyphenated filename. Add a one-line dated entry to the module's `## Log`.
- **Assessments are notes.** Each assessment (coursework, exam, formative, admin deadline) is a note in the
  module's `assessments/` folder, with the properties in `projects/_template/assessment.md`. These notes are the
  **only** source of truth for dates, weights, status and marks. `DEADLINES.md` and MODULE.md just show views of
  them. When something is set, moved, submitted or marked, edit that note and add a Log line.
- **What's due?** Use the `whats-due` skill (it reads the assessment notes).
- **New on Moodle?** "Refresh Moodle" runs `sync-moodle`: new or moved deadlines go into assessment notes, and
  announcements, new files and weekly topics into a digest at `projects/updates/<date>.md`. I log in myself.
- **Revision:** "make flashcards for X" or "add cards for week N" runs `create-flashcards`. `flashcards/cards.md`
  is the source; never rename a card's `###` title (it's the card's ID and holds its review history).
- Mark anything unconfirmed as `_tbc_`, and say where it should come from (VLE, unit catalogue, lecturer).

## Careers
- If `careers/BRIEF.md` doesn't exist and I ask about jobs, internships or placements, suggest `setup-careers`.
- Use `find-roles` to search, and `prep-application` for a specific role. Keep ROLES.md and
  APPLICATIONS.md current when I say I've applied, been rejected, passed a stage or got an offer.
- Only claim experience that's in `careers/CV.md`. Never apply, submit forms or log in to job sites for me.

## Sources, in order of trust
1. The official unit/module catalogue (credits, assessment weights, learning outcomes).
2. The module's VLE page (dates, timetable, staff, briefs). Prefer it for anything time-specific.
3. What I tell you.

When they disagree, record both and flag it. Don't silently pick one.

## Writing files
- Plain Markdown that reads well in Obsidian and on GitHub: tables for structured data, short sections, dates
  like "28 Sep 2026".
- Link between files with **relative Markdown links**, e.g. `[DEADLINES](../DEADLINES.md)` or
  `[brief](coursework/cw1/brief.pdf)`, so they're clickable in Obsidian and GitHub. No absolute paths in files.

## House rules
- Ask before deleting anything or overwriting a file I wrote.
- Files, not chat, are the memory. Anything worth remembering goes into the relevant MODULE.md, DEADLINES.md
  or PROFILE.md.
- Never type my passwords or do my university login. I sign in myself when a browser step needs it.
- Never write secrets (passwords, tokens, API keys) into this folder.
- Course materials (notes, slides, past papers) are the university's copyright. They stay in git-ignored
  module folders and are never committed or shared.
- Academic integrity: help me understand and plan, and flag the unit's GenAI rules when they apply. If a
  module says no GenAI for an assessment, say so rather than writing it for me.
