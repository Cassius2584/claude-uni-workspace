---
name: setup-careers
description: Set up the careers section of the workspace for finding and applying to graduate roles, internships or placements. Imports the user's CV, interviews them for a search brief, picks job sites to check, and optionally schedules a daily or weekly role search. Use when the user says "set up careers", "help me find grad jobs / internships / placements", "set up job search", or when careers/BRIEF.md doesn't exist yet.
---

# Set up careers

End state: `careers/` contains `CV.md`, `BRIEF.md`, `SOURCES.md`, `ROLES.md`, `APPLICATIONS.md`, empty
`digests/` and `roles/` folders, and (if wanted) a scheduled search. Copy each file from
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

## 3b. Spreadsheet tracker (optional)
Markdown tables work, but a spreadsheet is nicer for sorting and filtering, colour coding and viewing on a phone.
If the student wants one and a spreadsheet tool is available (a Google Sheets skill or connector, or Excel),
create a sheet with tabs **Roles**, **Pipeline**, **Watchlist** (target employers), **Sites**, **Events**
and **Filtered out**. Add dropdowns for priority, type and stage, and a live "Days left" column. If they already
kept a tracker in an earlier year, read it first and reuse its columns and wording. Then write
`careers/TRACKER.md` from `careers/_template/TRACKER.md` with the sheet's ID, link, tab names, column order and
the exact commands for reading and adding rows, and don't create SOURCES/ROLES/APPLICATIONS.md.

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
- Tell the student to click **Run now** on the task once and approve the tools it asks for (web search, the
  spreadsheet tool, file writes). Otherwise the first unattended run stalls on approval prompts. Runs only
  happen while the app is open. A missed run fires on next launch.

## 5. First run
Offer to run `find-roles` now so they see a digest straight away.
