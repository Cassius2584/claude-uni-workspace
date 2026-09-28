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
├── DEADLINES.md                    ← every assessment across the year, in date order
├── CM32032-reinforcement-learning/
│   ├── MODULE.md                   ← credits, outcomes, assessments + weights, dates, staff, timetable, log
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

Prefer a spreadsheet? `setup-careers` can build a Google Sheet tracker instead (Roles, Pipeline, Watchlist, Sites,
Events, with dropdowns and deadline colour coding, reusing last year's tracker if you had one). The skills then
read and write the sheet, via `careers/TRACKER.md`.

**Scheduling tip:** after `setup-careers` creates the scheduled task, click **Run now** on it once and approve the
tools it asks for. Otherwise the first unattended run waits on permission prompts. Scheduled runs happen while the
Claude app is open. A missed run fires the next time you open it.

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

## Viewing it: use Obsidian (recommended)
Everything is plain Markdown, so any editor works, but [Obsidian](https://obsidian.md) (free) is the nicest way
to read and browse it yourself while Claude does the writing:

1. Install Obsidian → **Open folder as vault** → pick this folder.
2. That's it. `MODULE.md` tables, `DEADLINES.md` and the careers digests render cleanly, links between files are
   clickable, and lecture PDFs and past papers open inside Obsidian. Search covers every module at once.

Tips:
- Keep Claude Code and Obsidian open on the same folder. Obsidian picks up Claude's edits live.
- Pin `projects/DEADLINES.md` and the latest digest in the sidebar for a one-glance dashboard.
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
| `.claude/skills/setup-year/` | First-run setup: VLE + unit catalogue → module folders + deadlines |
| `.claude/skills/add-module/` | Add a single module from a code, link, PDF or pasted spec |
| `.claude/skills/whats-due/` | Deadline summary (coursework + applications) with priorities |
| `.claude/skills/setup-careers/` | CV import, search brief interview, job sources, optional schedule |
| `.claude/skills/find-roles/` | Search → read descriptions → filter → score → ranked digest |
| `.claude/skills/prep-application/` | Per-role fit map, tailored drafts, process and interview prep |
| `projects/_template/` | `MODULE.md`, `DEADLINES.md` and `PROFILE.md` templates |
| `careers/_template/` | `BRIEF.md`, `CV.md`, `SOURCES.md`, `ROLES.md`, `APPLICATIONS.md` templates |

Built and tested against Moodle at the University of Bath. The skills are written for any Moodle-based
university, and other VLEs (Canvas, Blackboard) should work with minor guidance. PRs welcome.

## Licence
MIT
