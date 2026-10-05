---
name: add-module
description: Add one module to the uni workspace from whatever the student has, such as a module code, a unit catalogue link, a VLE page, a handbook PDF or pasted text. Use when the user says "add module X", "set up module X", "I'm also taking X", or shares a module spec.
---

# Add a module

1. **Identify it.** Get the module code and title. If you only have a name, search the unit catalogue in
   `projects/PROFILE.md` for it and confirm the match with the student.
2. **Gather the facts** from, in order of trust: the unit catalogue entry (credits, semester, assessment
   weights, qualifying marks, learning outcomes, content), then the VLE page if it exists yet (staff,
   timetable, dates, GenAI rules, briefs), then anything the student pasted or attached. If a page needs a
   login, the student signs in themselves.
3. **Create the folder** `projects/<CODE>-<short-kebab-name>/` with `lectures/`, `coursework/` (one
   subfolder per assessment, or `problem-sheets/` for exam-only modules) and `resources/`.
4. **Write `MODULE.md`** from `projects/_template/MODULE.md`: properties, the header card, sections, and the
   `base` blocks in the Assessments and Files cards pointed at this module's folder. Add a pill for it to the header of
   `projects/DEADLINES.md`. Mark gaps `_tbc_` with where to find them. Add a dated log line
   naming the sources.
5. **Create assessment notes** in `assessments/` from `projects/_template/assessment.md`, one per dated or
   graded item. Exams with no date yet: blank `due`, `due_note: "<month> exam period"`. They appear in
   `projects/DEADLINES.md` automatically. No table to update. Then run
   `python3 .claude/skills/create-study-timetable/scripts/sync_deadlines.py` so the dated ones show in the calendar.
6. **Check the credit total** for the year against PROFILE.md, and mention it if it's now complete or still
   short.

Reply briefly: what the module is, how it's assessed, anything notable (qualifying mark, group work, GenAI
policy), and what's still `_tbc_`.
