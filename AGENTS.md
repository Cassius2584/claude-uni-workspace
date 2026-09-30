# AGENTS.md

This workspace was built for Claude Code, but it's plain Markdown, so any coding agent (Codex, Cursor, Gemini CLI,
etc.) can run it. If you're an agent other than Claude Code, start here.

## Setting this up for someone
If the person gave you **only the repo link** (e.g. "help me set up this uni workspace: <link>"), don't try to
carry out these steps from the web page. Instead, explain the project in 3–5 plain sentences (one folder per module
from their Moodle and official specs, one deadline board, a weekly "refresh Moodle", an optional job search), and
suggest they send you this exact message so the request comes from them:

> Clone github.com/Cassius2584/claude-uni-workspace into a new folder called uni-workspace in my home folder, switch to working in that folder, then set up my year by following its CLAUDE.md and setup-year skill (read the files directly if the skill doesn't load).

When they've asked you to clone and set up:
1. **If you can't touch their files** (a plain chat such as claude.ai, ChatGPT or the Gemini app), say so kindly and
   tell them to paste that message into Claude's desktop app (Code tab), Codex or Gemini CLI. Stop there.
2. **Get the files** into the folder they named (default: `uni-workspace` in their home folder; avoid iCloud/OneDrive-synced
   folders such as a synced Documents): `git clone https://github.com/Cassius2584/claude-uni-workspace <folder>`, or
   if git isn't available, download and unzip
   `https://github.com/Cassius2584/claude-uni-workspace/archive/refs/heads/main.zip`. Then delete the `.git`
   folder unless they plan to contribute back, so their own notes can't be pushed anywhere.
3. **Work from that folder.** If your tool can switch its working folder, do it. Either way, **read `CLAUDE.md`
   and `.claude/skills/setup-year/SKILL.md` directly** rather than relying on skills having loaded: sessions only
   load a folder's skills when they start there.
4. **Run setup-year.** They sign in to their university themselves. Never type their password.
5. **Finish** with what they now have, how to reopen it next time (open the `uni-workspace` folder in their AI app, and
   optionally in Obsidian via "Open folder as vault"), and three things to say next: "what's due?", "refresh
   Moodle" (weekly), and "set up careers" (optional).

## 1. Read the rules
**[CLAUDE.md](CLAUDE.md) is the rulebook for every agent.** Read it at the start of every session and follow it.
One Claude Code-specific line needs doing by hand:
- `@projects/PROFILE.md` is a Claude Code import. **Read `projects/PROFILE.md` yourself** (who the student is:
  university, degree, year, VLE). If it doesn't exist, the workspace isn't set up yet, so run `setup-year` below.

## 2. Skills = task playbooks
Each skill is a Markdown file of step-by-step instructions at `.claude/skills/<name>/SKILL.md`. Claude Code
triggers them automatically. In other agents, **open and follow the matching file** when the student asks for
that task:

| When the student says… | Follow |
|---|---|
| "set up my year", "import my modules" | [.claude/skills/setup-year/SKILL.md](.claude/skills/setup-year/SKILL.md) |
| "refresh Moodle", "anything new on Moodle?" | [.claude/skills/sync-moodle/SKILL.md](.claude/skills/sync-moodle/SKILL.md) |
| "add module X", "I'm also taking X" | [.claude/skills/add-module/SKILL.md](.claude/skills/add-module/SKILL.md) |
| "what's due?", "what should I work on?" | [.claude/skills/whats-due/SKILL.md](.claude/skills/whats-due/SKILL.md) |
| "weekly review", "plan my week", "what does next week look like?" | [.claude/skills/weekly-review/SKILL.md](.claude/skills/weekly-review/SKILL.md) |
| "make flashcards for X", "add cards for week N", "which proofs do I need?" | [.claude/skills/create-flashcards/SKILL.md](.claude/skills/create-flashcards/SKILL.md) |
| "make me a study timetable", "when should I study?", "I've joined X on Wednesdays" | [.claude/skills/create-study-timetable/SKILL.md](.claude/skills/create-study-timetable/SKILL.md) |
| "set up careers", "help me find grad jobs" | [.claude/skills/setup-careers/SKILL.md](.claude/skills/setup-careers/SKILL.md) |
| "find roles", "run my job search" | [.claude/skills/find-roles/SKILL.md](.claude/skills/find-roles/SKILL.md) |
| "help me apply to X", "cover letter for X" | [.claude/skills/prep-application/SKILL.md](.claude/skills/prep-application/SKILL.md) |

## 3. What differs outside Claude Code
- **Browser steps** (Moodle and unit catalogue logins in `setup-year`) need a browser tool that the student can
  see and sign in to themselves. Without one, ask the student to paste the pages or export them, and work from that.
  Never type the student's credentials.
- **Web research** (`find-roles`) needs web search and page-fetch tools.
- **Scheduling** (`setup-careers` step 4) describes the Claude desktop app's scheduled tasks and Claude Code
  permission settings. Use your own tool's scheduler (or cron running your CLI non-interactively) and its own
  permission/approval config. Keep the same command rules: file tools for file I/O, no chained shell commands,
  writes only under `careers/`.
- **Obsidian Bases** (`*.base` files, and `base` code blocks in MODULE.md) are Obsidian views over note properties.
  You never edit them. Keep the note properties exact, as listed in the templates and `careers/TRACKER.md`.
