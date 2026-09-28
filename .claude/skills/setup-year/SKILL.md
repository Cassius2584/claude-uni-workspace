---
name: setup-year
description: Set up this uni workspace for a new academic year. Finds the student's modules on their VLE (Moodle or similar), pulls each module's official spec from the university's unit catalogue, and builds one folder per module plus a combined deadline list. Use when the user says "set up my year", "set up my modules", "import my modules from Moodle", or when projects/PROFILE.md doesn't exist yet.
---

# Set up my year

Goal: go from an empty workspace to one filled-in folder per module and one `projects/DEADLINES.md`,
using the student's VLE and the university's public or SSO-protected unit catalogue. It should take one
sitting.

Work through the steps in order. Tell the student briefly what you're on, and put findings in files, not chat.

## 1. Profile
If `projects/PROFILE.md` is missing, ask in one message:
- University, degree, year of study, academic year.
- VLE address (e.g. `https://moodle.<uni>.ac.uk`). If they don't know it, search for "<uni> Moodle".
- Anything they're taking that might not show on the VLE yet (e.g. semester 2 options).

Find the unit catalogue yourself: search "<uni> unit catalogue <year>" or "<uni> module catalogue". Then copy
`projects/_template/PROFILE.md` to `projects/PROFILE.md` and fill it in.

## 2. Log in (the student does this)
Use a browser tool: the Claude desktop app's built-in browser, or Claude in Chrome. Open the VLE's course
list (Moodle: `/my/courses.php`).
- If you land on a login page, **stop and ask the student to sign in themselves**, and make sure the browser
  is visible to them. Never type credentials, and never do 2FA for them.
- The unit catalogue may sit behind a separate single sign-on. Same rule applies.

## 3. Find the modules
On Moodle, the course list renders with JavaScript, so read it after load, e.g. collect
`a[href*="course/view.php"]` links and their text. Then:
- Keep teaching modules. Drop staff areas, programme "zones", placement pages, maths/study-skills support
  pages and similar.
- Pull the module code from the course name (patterns like `CM32032`, `COMP3001`, `MA30086`).
- Show the student the list and confirm before building anything. Ask about anything missing (semester 2
  modules often aren't on the VLE until later).

## 4. Read each module's VLE page
For each course, gather:
- Welcome/overview text, staff and contacts, timetable (lecture/lab times and rooms), office hours.
- Assessment information: components, weights, due dates, group vs individual, GenAI policy ("open/closed
  lane" or similar), ethics requirements, qualifying marks.
- Assignment pages (Moodle `mod/assign`) for exact **Opens / Due** dates.
- Weekly schedule pages, reading lists, links to the unit catalogue.

Moodle tips: sections can be lazy-loaded, so fetch `/course/view.php?id=<id>&section=<n>` for n = 0…10 and
collect `/mod/` links. Moodle "page" and "assign" activities hold most of the detail. Resources that open in
a frame expose their real file link as a `pluginfile.php` URL inside the page.

## 5. Read the official spec
Open each module's catalogue entry (search the catalogue's unit list for the code). Catalogues are often
behind a **separate** single sign-on from the VLE: the student logs in once more, then you **navigate** to each
page. Background `fetch()` calls from page scripts usually fail on SSO-protected sites because of redirects
and cross-origin rules. Record credits,
level, period/semester, the assessment summary with weights and qualifying marks, requisites, learning
outcomes, content and synopsis. The catalogue is the authority on weights and outcomes. The VLE is the
authority on dates. Flag any disagreement.

Add up the credits. If the total isn't the year's normal load (e.g. 60 ECTS / 120 CATS), tell the student and
ask what's missing.

## 6. Build the folders
For each module:
1. Create `projects/<CODE>-<short-kebab-name>/` with `lectures/`, `coursework/`, `resources/`.
2. Inside `coursework/`, create one subfolder per assessment (e.g. `cw1-business-plan/`,
   `01-proposal/`). Exam-only modules get `coursework/problem-sheets/`.
3. Write `MODULE.md` from `projects/_template/MODULE.md`: fill the properties (`kind: module`, code, title,
   semester, credits, assessment summary, leader, moodle) and every section you have evidence for. Set the
   folder path in the embedded `base` block to this module's folder. Use `_tbc_` plus a note on where to find
   the rest. Add a dated `## Log` line saying where the data came from.
4. Create `assessments/` with **one note per dated or graded item**, from `projects/_template/assessment.md`:
   graded coursework and exams, formative milestones, and admin deadlines (group registration, preference forms).
   Name each `<CODE>-<slug>.md`. Use exact property values; leave `due` blank when there's no date yet and put
   the approximate timing ("Jan 2027 exam period") in `due_note`.

Then copy `projects/_template/Deadlines.base`, `Modules.base` and `DEADLINES.md` into `projects/`, and add a
**Busy spots** line to DEADLINES.md for clusters. In Obsidian, `DEADLINES.md` shows every assessment across
modules (Due next · Graded only · By module · Board · Done) and `Modules.base` shows all modules.

## 7. Files (optional; ask first)
Offer to save the key course files (handbooks, lecture notes, formula books, past papers, templates) into
each module's `resources/` or `lectures/`. If the student agrees:
- Trigger the downloads in the browser. They land in the student's Downloads folder. Browsers block
  rapid-fire downloads, so pace them (a hidden iframe per file with a few seconds between works).
- Move each file into the right module with a clear lowercase-hyphenated name, and log it.
- Never commit these files. They are the university's copyright (the repo's `.gitignore` already excludes
  module folders).

## 8. Wrap up
Say the sync step last: after setup, "refresh Moodle" (`sync-moodle`) keeps it current, ideally weekly. The
first run records a baseline. Offer to run it once now so the baseline exists.

Reply with: a table of modules (credits, semester, assessment), the next three deadlines, anything
`_tbc_`, and anything odd you spotted (broken links, credit shortfall, catalogue/VLE mismatch).
