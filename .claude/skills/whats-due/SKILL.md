---
name: whats-due
description: Summarise upcoming uni and job-application deadlines from the workspace. Use when the user asks "what's due", "what's coming up", "what should I work on", "deadlines this week/month", or asks about their workload.
---

# What's due

1. Read every assessment note (`kind: assessment` in `projects/*/assessments/`) whose `status` isn't Submitted or
   Marked, and `careers/APPLICATIONS.md` if it exists (or, if `careers/TRACKER.md`
   exists, the roles in that tracker, whether Obsidian role notes or a spreadsheet, with a deadline or
   next-step date that aren't expired, rejected, withdrawn or filtered out) (closing dates and next steps
   for applications not yet submitted), and, if `tasks/` exists, every task note (`kind: task`) whose `status`
   isn't Done and that has a `due` date or `status: Doing`. Use today's date. Default window: the next 14 days, plus anything
   overdue and not marked Submitted. Use the window the student asks for if they give one.
2. For each item in the window, look in the module's `coursework/<item>/` folder (linked from the assessment
   note) to judge progress: is there a brief, a draft, nothing? Items with a blank `due` but a `due_note` in
   the window (e.g. "Jan 2027 exam period") count as due then.
3. Reply with a short table in date order: **date · module · item · weight · days left · status/progress**.
   Put applications in the same table with module "Careers", and tasks with module = their `area` (weight "–").
   If a Google Calendar connector is available, add one line on how busy the next few days look (lectures and
   events), so the advice fits the free time. Then give 1–3 lines on what to do first, weighted by due date × weight × how little is done. Call out
   clusters, formative deadlines worth doing anyway, and admin items (group registration, preference forms)
   that are easy to miss.
4. If the student tells you something's been submitted or marked, update that assessment note's `status`/`mark`
   and add a log line.

Keep it tight. It's a glance, not a report.
