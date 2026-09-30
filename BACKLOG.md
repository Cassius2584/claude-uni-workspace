# Backlog

Ideas for the template, roughly in priority order. Keep the base template small: each new feature should be
something `setup-year` offers as an optional step, not something every student gets by default.

## Next

### `create-study-timetable` skill
Build a weekly study timetable once the student shares their lecture timetable, and keep it in Obsidian.
- **Inputs:** the university timetable (iCal feed URL, a screenshot or an export), the modules in `projects/`
  and their credits, and assessment dates from the assessment notes.
- **Short interview** (5–6 questions, one message): regular commitments (sport, clubs, society, part-time job,
  societies' socials), preferred working hours and days, days off, when they focus best (morning or evening),
  commute or campus days, and how many hours a week they want to study outside lectures.
- **Output:** a weekly plan that fits study blocks into the gaps. Weight blocks by credits and upcoming
  deadlines, and add a short daily flashcards slot. Put a pre-lecture reading block before each lecture and a
  review block after it. Leave buffer time and one full day off.
- **Where it lives (Obsidian first):** one note per recurring block in a `timetable/` folder, written in the
  frontmatter format of the [Full Calendar Remastered](https://community.obsidian.md/plugins/full-calendar-remastered)
  plugin, so it renders as a week view in Obsidian. The same plugin can show the university's iCal feed
  read-only next to it. Check the plugin's current event format when building this.
  A calendar view for Bases is on Obsidian's roadmap. Switch to it when it ships, so no plugin is needed.
- **Optional:** if the student wants it on their phone's calendar, offer to add the blocks to Google Calendar
  through the Google Calendar connector (or ask them to import an `.ics` file into Apple Calendar). Ask before
  creating any events.
- **Upkeep:** "I've joined the climbing club Weds 6–8" or "move my Friday blocks" updates the notes. At the
  start of semester 2, rebuild the plan from the new timetable.

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
- **Recommended Obsidian plugins** in the README: Spaced Repetition, Full Calendar Remastered, and the built-in
  Templates plugin pointed at the `_template` folders.
- **A start-of-session hook** that prints anything due in the next 3 days. Only once the above are in.
