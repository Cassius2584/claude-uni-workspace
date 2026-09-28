# claude-uni-workspace

A university workspace that [Claude Code](https://claude.com/claude-code) sets up and maintains for you.

Say **"set up my year"**. Claude opens your Moodle, you log in, and it finds your modules, pulls each
module's official spec from your university's unit catalogue, and builds one organised folder per module.
It also produces one deadline list for the whole year. After that, every session starts with context:
ask "what's due?", "help me plan the RL coursework" or "here's the CW1 brief" and Claude knows where
everything is.

It also runs your **job hunt**: a scheduled search for grad roles, internships or placements that match your
CV and brief, ranked by fit, plus per-role application prep. [Jump to careers ↓](#careers-grad-roles-internships-placements)

```
projects/
├── DEADLINES.md                    ← every assessment across the year (a live Obsidian Bases view)
├── Deadlines.base  Modules.base    ← Due next · Graded only · By module · Board · Done; all modules
├── CM32032-reinforcement-learning/
│   ├── MODULE.md                   ← credits, outcomes, staff, timetable, log + this module's assessments
│   ├── assessments/                ← one note per assessment: due, weight, status, mark
│   ├── lectures/                   ← week-01-….md
│   ├── coursework/
│   │   ├── ga1-group-project/      ← brief, drafts, feedback, progress notes
│   │   └── ga2-group-research-project/
│   └── resources/                  ← notes, slides, past papers (never committed)
└── MA32025-medical-statistics/
    └── …
```

See [`projects/EXAMPLE-MA30001-linear-algebra/`](projects/EXAMPLE-MA30001-linear-algebra/MODULE.md) for a
filled-in (fictional) module.

## Careers: grad roles, internships, placements
Say **"set up careers"**. Claude imports your CV and interviews you for a brief: role types, what you
want to do, deal-breakers and dream employers. It then picks the job boards to check. After that:

- **`find-roles`** runs daily or weekly as a scheduled task, or on demand. It checks your chosen boards (Bright
  Network, Prospects, TARGETjobs, Gradcracker, RateMyPlacement, LinkedIn, Indeed…) and your target employers'
  careers pages, plus a broad web search. It then reads every new job description and filters out roles you
  aren't eligible for (grade, right to work, location, salary). It scores the rest for fit against your CV
  and brief, and writes a ranked digest: **Apply now / Worth a look / Stretch**, with the why, the gaps, the
  closing date and the recruitment process.
- **`prep-application`** takes one role, saves the job description (before it disappears), maps each
  requirement to evidence in your CV, drafts tailored CV bullets, a cover letter and STAR answers (real
  experience only), and lists the tests and likely interview questions.
- **`APPLICATIONS.md`** tracks every application from *To apply* to *Offer*. Closing dates show up in
  "what's due?" alongside your coursework.

```
careers/
├── BRIEF.md  CV.md  SOURCES.md
├── ROLES.md             ← everything seen, so digests only show new roles
├── APPLICATIONS.md      ← pipeline + deadlines
├── digests/2026-09-28.md
└── roles/acme-graduate-swe-2027/  job.md · fit.md · drafts.md · prep.md
```

### Pick a tracker
**Use Obsidian Bases.** It's the default, and the one this template is built around. Each role becomes a note, the
views behave like a spreadsheet (sort, filter, board), prep files sit next to each role, it needs no accounts, and
scheduled searches run with no shell permissions at all. The other two are fallbacks:

| Tracker | What you get | Needs |
|---|---|---|
| **Obsidian Bases** (default, recommended) | One note per role; `careers/Roles.base` shows *Open roles · By deadline · Applications · Board · Filtered out* as sortable, filterable tables and cards | Obsidian 1.9+ with the Bases core plugin |
| **Markdown tables** (fallback) | `ROLES.md` + `APPLICATIONS.md`, readable anywhere | Nothing |
| **Spreadsheet** (only if you already live in one) | Google Sheet or Excel with tabs, dropdowns and deadline colour coding, great on a phone | A tool that can **write** to your sheet (e.g. a Google Sheets skill). A read-only Drive connector isn't enough, because the search adds rows every run |

If you kept a tracker last year, `setup-careers` reads it and reuses your columns.

### Scheduled runs without approval prompts
Unattended runs stall on permission prompts, and chained shell commands only offer "Allow once". So
`setup-careers` (with your OK) adds a **narrow** allow-list to `~/.claude/settings.json`: web search/fetch,
reading this workspace, writing only under `careers/`, and (for a spreadsheet) the exact tracker commands, never
a blanket shell rule. It also writes command rules into the task prompt so every step matches. Click **Run now**
once to confirm it runs clean. Scheduled runs happen while the Claude app is open. A missed run fires the next
time you open it.

Claude never applies, fills in forms or logs in to job sites for you.

## Why
Module info is scattered across the VLE, the unit catalogue, handbooks and emails. Chat history forgets. This
puts it all in plain Markdown files that you own, and gives Claude rules for keeping them current, so the
files are the memory.

## Setup (about 10 minutes)
You need **Claude Code**, either the desktop app's Code tab or the terminal, plus a browser Claude can use:
the desktop app's built-in browser or Claude in Chrome.

1. **Get the workspace.** Click **Use this template** on GitHub (or fork/clone), and put it somewhere
   permanent, e.g. `~/uni`.
2. **Open it in Claude Code.** In the desktop app, start a Code session with this folder selected. In the
   terminal, run `claude` inside the folder.
3. **Say "set up my year".** Claude asks for your uni, degree and VLE, opens the VLE, and waits while **you**
   log in. It then shows you the modules it found and builds everything once you confirm.

Then delete the `EXAMPLE-…` folder.

### Using Codex, Cursor or another agent?
It's built for Claude Code, but everything is plain Markdown, so other agents work too. They read
[`AGENTS.md`](AGENTS.md), which points them at the same rules (`CLAUDE.md`) and tells them which skill file to follow
for each request. What's Claude-specific, and what you'll need your own tool's equivalent for:
- a **browser you can log in through** (for Moodle and the unit catalogue)
- **web search** (for the job search)
- **scheduling and approvals** (for the automatic twice-weekly search)

The notes, Obsidian views and templates don't care which AI wrote them.

## Keeping it in sync with Moodle
After setup, say **"refresh Moodle"** once a week (Sunday evening works well). `sync-moodle` checks every course
page against what it saw last time and only reports what's new: changed dates first, then new deadlines,
announcements, new files (downloaded only if you pick them) and the week's topics.

Why it isn't automated:
- **You log in yourself.** Moodle sits behind university single sign-on, usually with 2FA. Storing your password
  for a script is unsafe, usually against IT rules, and wouldn't get past 2FA anyway.
- **The calendar export isn't enough.** It only contains dates already set up as Moodle activities. It misses
  assignments that are still hidden, dates written in page text or handbooks, exams, announcements and files.

## Viewing it: use Obsidian (recommended)
Everything is plain Markdown, so any editor works, but [Obsidian](https://obsidian.md) (free) is the nicest way
to read and browse it yourself while Claude does the writing:

1. Install Obsidian → **Open folder as vault** → pick this folder.
2. That's it. `MODULE.md` tables, `DEADLINES.md` and the careers digests render cleanly, links between files are
   clickable, and lecture PDFs and past papers open inside Obsidian. Search covers every module at once.

Tips:
- Keep Claude Code and Obsidian open on the same folder. Obsidian picks up Claude's edits live.
- Pin `projects/DEADLINES.md` (coursework board) and `careers/Roles.base` (job tracker) in the sidebar for a
  one-glance dashboard. Both are Obsidian Bases: every assessment and every role is a note with properties, so
  you can sort, filter and switch to a card board.
- Want it on your phone? Obsidian Sync or iCloud works, but your CV and course materials sync too, so keep it to
  services you trust.
- Obsidian hides dot-folders, so `.claude/` (the skills) stays out of the way. Your Obsidian settings
  (`.obsidian/`) are git-ignored.

## Day to day
| Say | What happens |
|---|---|
| "What's due?" | Next two weeks of deadlines, with progress and what to do first (`whats-due`) |
| "Add module MA32054" / "I'm also taking Graph Theory" | Pulls the spec and adds the folder (`add-module`) |
| "Here's the CW1 brief" + file | Filed in the right `coursework/` folder and logged |
| "I submitted the business plan" | Status updated in MODULE.md and DEADLINES.md |
| **"Refresh Moodle"** (weekly) | New/moved deadlines → assessment notes; announcements, new files, weekly topics → `projects/updates/<date>.md` (`sync-moodle`) |
| "Update semester 2 modules from Moodle" | Fills in timetables, staff and dates once pages go live |
| "Find me new roles" | Runs the job search now (`find-roles`) |
| "Help me apply to #2 from today's digest" | Fit map, tailored drafts and interview prep (`prep-application`) |
| "I got through to the assessment centre at X" | Application stage updated |

## Privacy and copyright
- `.gitignore` keeps **your** modules, profile, deadlines, CV and applications out of git. Only the template and example are
  tracked, so you can pull updates to this repo without leaking anything.
- PDFs, slides, docs and zips are ignored everywhere. Lecture notes and past papers are your university's
  copyright. Don't publish them.
- Claude never enters your password. Logins are always done by you in the browser.

## What's inside
| Path | Purpose |
|---|---|
| `CLAUDE.md` | Rules Claude follows in every session (read automatically by Claude Code) |
| `AGENTS.md` | Entry point for other agents (Codex, Cursor…): points to `CLAUDE.md` and maps requests to skill files |
| `.claude/skills/setup-year/` | First-run setup: VLE + unit catalogue → module folders + deadlines |
| `.claude/skills/add-module/` | Add a single module from a code, link, PDF or pasted spec |
| `.claude/skills/sync-moodle/` | On-demand Moodle refresh: new/changed deadlines, announcements, files, weekly topics |
| `.claude/skills/whats-due/` | Deadline summary (coursework + applications) with priorities |
| `.claude/skills/setup-careers/` | CV import, search brief interview, job sources, optional schedule |
| `.claude/skills/find-roles/` | Search → read descriptions → filter → score → ranked digest |
| `.claude/skills/prep-application/` | Per-role fit map, tailored drafts, process and interview prep |
| `projects/_template/` | `MODULE.md`, `assessment.md`, `DEADLINES.md`, `PROFILE.md`, and the `Deadlines.base` / `Modules.base` views |
| `careers/_template/` | `BRIEF.md`, `CV.md`, `SOURCES.md`; Markdown tracker (`ROLES.md`, `APPLICATIONS.md`); Obsidian tracker (`role.md`, `Roles.base`, `TRACKER.bases.md`); spreadsheet tracker (`TRACKER.sheet.md`) |

Built and tested against Moodle at the University of Bath. The skills are written for any Moodle-based
university, and other VLEs (Canvas, Blackboard) should work with minor guidance. PRs welcome.

## Licence
MIT
