---
name: create-study-timetable
description: Build a weekly study timetable around the student's university lecture timetable and regular commitments, kept in Obsidian as calendar notes (Full Calendar plugin), with an optional copy in Google or Apple Calendar. Interviews the student briefly (commitments such as sport, clubs or a job, working hours and days, focus time, weekly study target), fits study blocks into the gaps weighted by credits and deadlines, checks for clashes, and writes a week overview. Use when the student asks for a study timetable, study plan, weekly schedule, "when should I study?", shares their lecture timetable, or wants to change their plan ("I've joined X on Wednesdays", "move my Friday blocks", "new semester timetable").
---

# Create study timetable

A weekly plan of study blocks fitted around lectures and the student's life, kept in the vault:

```
timetable/
├── TIMETABLE.md          ← overview: preferences, this week's grid, hours per module, log
└── blocks/<slug>.md      ← one note per recurring (or one-off) block, in Full Calendar's note format
```

**The block notes are the source of truth.** The Full Calendar plugin shows them as a week view and edits
their frontmatter when the student drags an event. Never regenerate them from somewhere else. Read them, and
edit them.

`scripts/timetable.py` (in this skill's folder, no extra packages) checks the blocks, finds clashes, including with
the university timetable, writes the week grid and hours into `TIMETABLE.md`, and can export an `.ics` file:
```
python3 scripts/timetable.py timetable [--lectures <ics file or URL>] [--week YYYY-MM-DD] [--ics study.ics]
```

## 0. Before you start
- Read `projects/PROFILE.md`, every `projects/*/MODULE.md` for this semester (credits, study hours, timetable,
  semester) and the assessment notes due in the next 6 weeks.
- If `timetable/` exists, you're **updating** (section 7). Read `TIMETABLE.md` and the blocks first.

## 1. Get the university timetable
In order of preference:
1. **The timetable's calendar feed (iCal/ICS link).** Most university timetable systems have a "Subscribe" or
   "Sync to calendar" button. Ask the student to paste the link. **Treat it like a password:** use it only for
   this run (`--lectures <url>`) and never write it into any file. The student pastes it into the plugin's
   settings themselves (section 5).
2. **Already in their Google Calendar**, if a Google Calendar connector is available: read the week's events
   from that calendar (read-only).
3. **A screenshot, PDF or export:** read it, and add lectures as `Uni - …` block notes so they show and are
   clash-checked.

Also find the **teaching dates** (term start and end, reading week, bank holidays) from the university's
calendar or the student. They become `startRecur`, `endRecur` and `skipDates`.

## 2. Interview (one message, short)
Ask only what you don't already know, and offer a default for each:
1. **Regular commitments:** sport, clubs and societies, a part-time job, volunteering, caring, church, regular
   calls. Give the day, time and travel time.
2. **Working pattern:** which days you study, the earliest start and latest finish, and a day (or half-day) that stays free.
3. **Focus:** are you sharper in the morning or the evening? Where do you usually study (library, home)?
4. **Weekly target** for independent study outside lectures. Suggest a number: each module's study hours (from
   MODULE.md, or about 10 hours per UK credit or 25–30 per ECTS credit) minus timetabled hours, spread over the
   teaching and revision weeks. Let them lower it: a plan they'll keep beats an ideal one.
5. Extras: a daily flashcards slot (if they use `create-flashcards`), a weekly planning slot, exercise or meals
   to protect.

Record the answers in `TIMETABLE.md` under `## Preferences` (template: [reference/timetable-template.md](reference/timetable-template.md)).

## 3. Plan the week
- **Blocks of 60–120 minutes**, with at least 15 minutes between them. Put the hardest modules in the student's
  best focus time. At most two blocks of the same module in one day.
- **Split hours by credits**, then shift some towards whatever has deadlines in the next 4 weeks. Give the
  individual project steady blocks every week.
- **After each lecture, a 30–45 minute review** within 24 hours (it can be the start of that module's block).
- **Coursework crunch:** for coursework due in the next 4 weeks, add one-off blocks (`type: single`) in the 2 weeks
  before the deadline, named after the assessment.
- **Daily flashcards**, 15–20 minutes on weekdays (if they use them), and a 15–20 minute **weekly planning** slot.
- **Protect:** commitments and their travel time, the day off, lunch, and evenings after the latest finish.
- **Leave slack:** plan about 80% of the target and don't fill every gap. Weeks always overrun.

## 4. Write the notes
One note per block in `timetable/blocks/`, named `<category>-<code or slug>-<days>.md`
(e.g. `study-ma32064-mon-thu.md`). Use one note with several `daysOfWeek` when the time is the same.
```yaml
---
title: Study - MA32064 - Number theory
allDay: false
type: recurring
daysOfWeek: [M, R]          # U M T W R F S  (R = Thursday, U = Sunday)
startTime: "10:00"          # always quoted HH:mm
endTime: "11:30"
startRecur: 2026-09-28      # first teaching day
endRecur: 2026-12-11        # last teaching day
skipDates: [2026-11-02]     # optional: reading week, bank holidays
---
Optional note: what to work on in this block, links to the module ([[projects/…/MODULE|MA32064]]).
```
One-off blocks use `type: single` and `date: YYYY-MM-DD` instead of the recurrence keys.
**Titles are `Category - Detail`**, which the plugin can colour by category. Use these categories:
`Study - <CODE> - <topic>` (the module code in the middle is what the hours table counts), `Revision - …`,
`Uni - …` (only when lectures aren't coming from a feed), `Life - …`, `Admin - …`.

Create `timetable/TIMETABLE.md` from [reference/timetable-template.md](reference/timetable-template.md).

## 5. Check, then show it
Run `timetable.py` with `--lectures` if you have the feed. It exits with the clashes listed, if there are any.
Fix them and rerun until it says **No clashes**. The script then writes the week grid into `TIMETABLE.md`.

Tell the student how to see it in Obsidian (one-time setup, done by them):
1. Settings → Community plugins → Browse → **Full Calendar Remastered** → Install → Enable.
2. Its settings → **Add calendar** → *Full Note* → folder `timetable/blocks`.
3. Optional: **Add calendar** → *ICS* → paste the university timetable link. It's read-only and refreshes itself.
4. Optional: turn on *Advanced categorization* to colour Study, Life and so on. When it asks how to update
   existing notes, choose **Use Parent Folder (Smart)**, which leaves titles that already have categories alone.
Then open the calendar (ribbon icon or command palette) in week view.

(A calendar view for Obsidian Bases is on Obsidian's roadmap. Once it ships, the same notes can be shown with a
Bases view and no plugin.)

## 6. Optional: on their phone's calendar
Ask if they want it in Google or Apple Calendar as well. **Don't create events without a clear yes.**
- **Import (recommended):** `timetable.py … --ics timetable/study.ics`. In Google Calendar, go to Settings →
  Import & export, and import into a **new calendar called "Study"**, so it's easy to hide or delete. In Apple
  Calendar, use File → Import and choose a new calendar. Imports don't update, so after changes, delete that
  calendar and import again.
- **Google Calendar connector** (if available): list the events you'll create (title, days, times, dates) and
  get a yes, then create each block as a recurring event. Keep a list of what you created in `TIMETABLE.md`'s
  Log, so the events can be changed or removed later.

## 7. Updating
- **"I've joined X on Wednesdays 6–8" / "move my Friday blocks" / "less on Sundays":** edit or add the block
  notes, rerun the check, and add a Log line. Mention if the phone calendar copy needs re-importing.
- **The student dragged things in the calendar:** the notes already changed. Just rerun the check and summary.
- **Coursework or deadlines changed:** adjust the one-off crunch blocks.
- **New semester:** don't delete old blocks. Their `endRecur` already ends them. Get the new timetable, rerun
  the interview briefly (just "anything changed?"), and add new blocks for the new modules.

## Rules
- The student's calendar feed link and any calendar credentials never go into the vault.
- Ask before creating, changing or deleting any event in an external calendar.
- Be realistic. If commitments plus lectures leave less time than the target, say so and suggest what to drop
  or shrink, rather than cramming blocks into every gap.
