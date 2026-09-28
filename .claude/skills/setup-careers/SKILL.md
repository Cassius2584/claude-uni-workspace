---
name: setup-careers
description: Set up the careers section of the workspace for finding and applying to graduate roles, internships or placements. Imports the user's CV, interviews them for a search brief, picks job sites to check, and optionally schedules a daily or weekly role search. Use when the user says "set up careers", "help me find grad jobs / internships / placements", "set up job search", or when careers/BRIEF.md doesn't exist yet.
---

# Set up careers

End state: `careers/` contains `CV.md`, `BRIEF.md`, `SOURCES.md`, the chosen tracker (step 3b), empty
`digests/` and `roles/` folders, and (if wanted) an approval-free scheduled search. Copy each file from
`careers/_template/` and fill it in. Never overwrite a filled-in file without asking.

## 1. CV
Ask for their CV (a file path, an attachment or pasted text). Save the original as `careers/cv.<ext>` and
write `careers/CV.md` from it, keeping their wording. Don't embellish, infer skills or fill gaps. If
something's thin (no dates, no grade), note it as a question at the end instead.

Pull education, grade and graduation date from `projects/PROFILE.md` and the module folders if they exist,
and confirm with the student.

## 2. Brief (a short interview, not a form)
Ask in two or three rounds, not one wall of questions. Pre-fill what you can infer from the CV and modules,
then confirm it with them.
1. **Role types:** grad roles, internships, placements (any mix), and start dates.
2. **What they want to do:** in their words. Then propose job titles and sectors to search for, based
   on it plus their CV and modules. Ask what to avoid.
3. **Hard requirements:** locations, right to work / sponsorship, minimum salary, grade and graduation
   date, anything else that's a deal-breaker.
4. **Targets:** employers they'd love to work for and any to skip. Offer 5–10 suggestions that fit their
   brief, each with a one-line reason, and let them pick.
5. **Frequency:** daily or weekly digest, and how many roles per digest.

Write `careers/BRIEF.md`. Read it back as a five-line summary and ask for corrections.

## 3. Sources
Copy `careers/_template/SOURCES.md`. Adjust the defaults to the brief:
- Placements → keep RateMyPlacement on. STEM → Gradcracker on. Public sector → Civil Service Jobs on. Startups →
  Welcome to the Jungle on.
- Non-UK region → replace the UK boards with that region's main graduate boards (search to find them).
- Add a row per target employer, and find their early-careers page URL by searching. Check each URL
  actually loads (careers pages move often). If it 404s and you can't find the new one, leave it blank rather
  than guessing.
- If the student kept a tracker in an earlier year (even for placements), carry the employers worth
  revisiting into the target list, with a note on what happened then.
- Ask whether their university has a careers portal. Add it as `browser` (live sessions only).

## 3b. Choose a tracker
**Default to Obsidian Bases** and recommend it strongly: no accounts, nothing to install beyond Obsidian, sortable
and filterable views, each role's prep notes right next to it, and scheduled runs that never need shell
permissions. Offer Markdown only if they don't want Obsidian, and a spreadsheet only if they already run their
applications from one **and** have a tool that can write to it.

| Option | When | Set up |
|---|---|---|
| **Obsidian Bases** (default, strongly recommended) | Sortable, filterable table and card views; one note per role alongside its prep files; no accounts | Copy `_template/TRACKER.bases.md` → `careers/TRACKER.md` and `_template/Roles.base` → `careers/Roles.base`. Create `careers/roles/`. Keep `SOURCES.md`; skip ROLES/APPLICATIONS.md. Tell them to open `careers/Roles.base` in Obsidian (1.9+, Bases core plugin on). |
| **Markdown tables** (fallback without Obsidian) | Simplest; works in any editor and on GitHub | Copy `ROLES.md` and `APPLICATIONS.md` from the template. No TRACKER.md. |
| **Spreadsheet** (only if already used) | They want it on their phone, shared, or colour-coded, **and** this session has a tool that can write to their sheet (a Google Sheets skill, or Excel via a script). A read-only connector isn't enough: the search adds rows every run. | Build tabs **Roles**, **Pipeline**, **Watchlist**, **Sites**, **Events**, **Filtered out**, with dropdowns for priority, type and stage, and a live "Days left" column. Test each read/add/write command once. Then write `careers/TRACKER.md` from `_template/TRACKER.sheet.md` with the sheet's ID, link, columns and the exact commands that worked. Skip SOURCES/ROLES/APPLICATIONS.md. |

If they kept a tracker in an earlier year, read it first and reuse its columns, wording and status values
whichever option they pick.

## 4. Schedule (optional)
Offer to run `find-roles` automatically at the frequency in the brief. Careers files are git-ignored and
stay on this computer, so the job has to run **locally**:
- **Claude desktop app:** create a scheduled task (use a scheduling tool if one is available in this
  session; otherwise tell them: Code tab → Scheduled → New task) with the working folder set to this
  workspace and the prompt: `Run the find-roles skill in scheduled mode.` It runs while the app is open
  and the computer is awake.
- **Terminal alternative:** a cron/launchd entry running `claude -p "Run the find-roles skill in scheduled mode."`
  in this folder.
- Cloud routines can't see the git-ignored `careers/` files, so don't use them for this.
- Each run starts with no memory, so the task prompt must be **self-contained**: absolute path to this
  workspace, where the brief, CV and tracker are, the priorities, digest location, and "scheduled mode: no
  questions, no logins, never apply".
- Runs only happen while the app is open. A missed run fires on next launch.

### Make scheduled runs approval-free
Unattended runs stall on permission prompts, and some prompts offer only "Allow once". That happens for
compound shell commands (pipes, `&&`, heredocs, `cd`, variables) and for files outside the folder the run
started in. Fix both:

1. **Pre-approve the exact tools** the search needs. Show the student this list and, with their OK, merge it
   into the `permissions.allow` array in their **user** settings (`~/.claude/settings.json`, because scheduled
   runs may not start in this folder). Read the file first and keep existing entries. Use this workspace's
   absolute path:
   ```json
   "WebSearch",
   "WebFetch",
   "Skill(find-roles)",
   "Read(<workspace>/**)",
   "Read(~/.claude/skills/**)",
   "Edit(<workspace>/careers/**)"
   ```
   With a spreadsheet tracker, also add one narrow `Bash(...)` rule per command in TRACKER.md, e.g.
   `"Bash(python3 /abs/path/to/sheets-tool.py sheet add-rows *)"`. Never add a bare `"Bash"` rule.
2. **Put command rules in the task prompt** so every step matches those rules: read and write files only with
   the file tools and only under `<workspace>/careers/`; no Bash for file I/O; write tool input (e.g. JSON rows)
   to `<workspace>/careers/.tmp/` with the Write tool; run each tracker command on its own, with the full path
   and no pipes, `&&`, `cd` or variables. The Obsidian Bases and Markdown trackers need no shell at all.
3. Ask the student to click **Run now** once to confirm there are no prompts. If one appears, add a narrow rule
   for exactly that call.

## 5. First run
Offer to run `find-roles` now so they see a digest straight away.
