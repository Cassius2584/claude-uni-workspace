---
name: sync-moodle
description: Refresh the workspace from Moodle after setup. Reads each module's course page, compares with what was seen last time, adds or updates assessment notes for new or changed assignments, lists new files (downloads the ones the student picks), summarises new announcements, fills in weekly topics, and writes a short update digest. Use when the user says "refresh Moodle", "sync Moodle", "check Moodle for updates", "anything new on Moodle?", or at the start of a week.
---

# Sync Moodle

Run on demand, typically once a week. **The student logs in; you never do.** There's deliberately no automated
version: Moodle sits behind the university's single sign-on (usually with 2FA), and its calendar export misses
most of what changes (hidden assignments, dates written in page text, announcements, files).

## 0. Before you start
- Read `projects/PROFILE.md` (VLE address) and every `projects/*/MODULE.md` with a `moodle` property (the course
  link). Modules without one (e.g. next semester's, not live yet) get a quick check on the VLE's course list:
  if the course has appeared, add its link to MODULE.md and treat it as new.
- Each module keeps its sync state in a hidden file, `projects/<module>/.moodle-sync.json`:
  ```json
  {"course_id": 12345, "last_synced": "2026-10-04",
   "seen": {"<activity id>": {"name": "…", "type": "assign|resource|page|forum|quiz|url|folder|…", "dates": "…"}},
   "announcements_seen_until": "2026-10-04T18:00:00Z"}
  ```
  No file means **first sync**: record everything as the baseline, and only report things that aren't already
  in the module's notes.

## 1. Log in (the student does this)
Open the VLE's course list (Moodle: `/my/courses.php`) in a browser tool the student can see. If you land on a
login page, **stop and ask them to sign in**, making sure the browser is visible to them. Never type credentials.
University single sign-on sessions can expire within hours, so expect to ask every time.

## 2. Read each course
Moodle tips (from real use):
- Course pages lazy-load sections: request `/course/view.php?id=<id>&section=<n>` for n = 0…15 (stop after
  two empty sections) and collect `/mod/<type>/view.php?id=<cmid>` links with their names. Same-origin
  `fetch()` from a logged-in Moodle tab works; SSO-protected *other* sites (e.g. the unit catalogue) need real
  navigation instead.
- **Assignments** (`mod/assign`): open each new or previously-dated one and read **Opens / Due / Cut-off**.
- **Dates in one place**: Moodle's upcoming-events page, `/calendar/view.php?view=upcoming` (logged in), lists
  every dated item across courses, including "should be completed by" dates on weekly activities that don't show
  on the assignment page itself. Read it first, then fill gaps from the activity pages.
- **Announcements**: open the course's Announcements forum (`mod/forum`) and read discussions newer than
  `announcements_seen_until` (title, date, author, gist). Forums are often **reused year to year**, so ignore
  posts from before the current academic year: they're last year's.
- **Resources** (`mod/resource`): the real file is a `pluginfile.php` URL inside the page (load the view page in
  a hidden iframe or read its links).
- Section text: look for dates written in prose ("spec released Thu 8 Oct", "register groups by Week 5").

Compare with `seen` and the module's assessment notes:
| Found | Do |
|---|---|
| New assignment or dated activity that's graded, formative-with-deadline or admin | Create an assessment note from `projects/_template/assessment.md` in `assessments/` |
| Due date differs from its assessment note | Update the note's `due`/`due_time`, add a Log line "Moodle moved due date from X to Y", and **flag it** in the digest |
| Weekly ungraded activities (labs, quizzes, "should be completed" exercises) | Don't make assessment notes (they'd flood the Board). Add them to the module's `## Weekly plan` |
| New files | List them in the digest with links. In a live session, offer to download (see step 3) |
| New announcements | Summarise in the digest (one line each); copy any dates or instructions into the relevant note |
| New weekly sections/topics | Fill in the module's `## Weekly plan` |
| Something disappeared or was renamed | Note it; don't delete anything |

## 3. Files (only if the student picks them)
Trigger downloads in the browser: they land in the student's Downloads folder. Browsers block rapid-fire
downloads, so pace them (a hidden iframe per file, a few seconds apart). Move each into the module's
`resources/`, `lectures/` or `coursework/<item>/` with a clear lowercase-hyphenated name, and log it. Course
materials are the university's copyright: never commit or share them.

## 4. Write it down
- Update each module's `.moodle-sync.json` (`seen`, `last_synced`, `announcements_seen_until`).
- Add one Log line to each MODULE.md that changed ("Moodle sync: 2 new files, GA1 brief released, …").
- Write `projects/updates/<yyyy-mm-dd>.md`:
  ```markdown
  # Moodle update – <Sun 4 Oct 2026>
  ## Changed dates        ← first, because these matter most
  ## New deadlines
  ## Announcements
  ## New files            ← with "download?" in live sessions
  ## This week            ← weekly activities and topics, per module
  ```
  Link every item to its note with relative links. Skip empty sections, and if nothing changed, say so in one line.

## 5. Reply
Lead with changed dates and anything due within 7 days, then a one-line count per module. Offer the file
downloads. Keep it short: the digest has the detail.
