# AGENTS.md

This workspace was built for Claude Code, but it's plain Markdown, so any coding agent (Codex, Cursor, Gemini CLI,
etc.) can run it. If you're an agent other than Claude Code, start here.

## Setting this up for someone
If the person gave you **only the repo link** (e.g. "help me set up this uni workspace: <link>"), don't try to
carry out these steps from the web page. Instead, explain the project in 3–5 plain sentences (one folder per module
from their Moodle and official specs, a deadline board and HOME dashboard in Obsidian, a study timetable,
flashcards and exam practice from their own notes, a weekly review, and an optional job search), and
suggest they send you this exact message so the request comes from them:

> Set up github.com/Cassius2584/claude-uni-workspace for me: install git if I don't have it, clone it into a new folder called uni-workspace in my home folder, switch to working in that folder, then set up Obsidian and then my year by following its CLAUDE.md and the setup-obsidian and setup-year skills (read the files directly if the skills don't load).

When they've asked you to clone and set up:
1. **If you can't touch their files** (a plain chat such as claude.ai, ChatGPT or the Gemini app), say so kindly and
   tell them to paste that message into Claude's desktop app (Code tab), Codex or Gemini CLI. Stop there.
2. **Get the files** into the folder they named (default: `uni-workspace` in their home folder; avoid iCloud/OneDrive-synced
   folders such as a synced Documents): `git clone https://github.com/Cassius2584/claude-uni-workspace <folder>`.
   **Check `git --version` first, and set git up if it's missing.** Don't send a beginner to a terminal:
   - macOS: run `xcode-select --install`. Apple's dialog opens; they click **Install** and wait a few minutes.
   - Windows: run `winget install --id Git.Git -e --source winget`, and they approve the installer prompt. (No winget:
     send them to https://git-scm.com/download/win and wait.)
   - Linux: installing needs their password, so give them the one command for their distro (e.g.
     `sudo apt install git`) to run themselves. Never type their password.
   They don't need a GitHub account: the repo is public, and cloning and `git pull` work without one. **Keep the `.git` folder:** it's how they `git pull` new skills and fixes later.
   Their own notes are git-ignored, and they can't push to this repo, so nothing of theirs can leak.
3. **Work from that folder.** If your tool can switch its working folder, do it. Either way, **read `CLAUDE.md`,
   `.claude/skills/setup-obsidian/SKILL.md` and `.claude/skills/setup-year/SKILL.md` directly** rather than relying on skills having loaded: sessions only
   load a folder's skills when they start there.
4. **Run setup-obsidian, then setup-year.** They click
   Install for each plugin and sign in to their university themselves. Never install plugins or type their password.
5. **Finish** with what they now have, how to reopen it next time (open the `uni-workspace` folder in their AI app, and
   in Obsidian via "Open folder as vault", which opens on HOME), and what to say next: "what's due?", "refresh
   Moodle" (weekly), "make me a study timetable", "make flashcards for <module>", and "set up careers" (optional).

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
| "quiz me on X", "exam practice", "mark my answer", "mock exam" | [.claude/skills/exam-practice/SKILL.md](.claude/skills/exam-practice/SKILL.md) |
| "set up Obsidian", "make Obsidian look nice" | [.claude/skills/setup-obsidian/SKILL.md](.claude/skills/setup-obsidian/SKILL.md) |
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
- **Scheduling** (`setup-careers` step 4 and `weekly-review`'s "Schedule it") describes the Claude desktop app's
  scheduled tasks and Claude Code permission settings. Use your own tool's scheduler (or cron running your CLI
  non-interactively) and its own permission/approval config. Keep the same command rules: file tools for file I/O,
  no chained shell commands, and writes only under `careers/` (job search) or `reviews/` (weekly review).
- **Scripts:** `create-flashcards` and `create-study-timetable` run small Python 3 scripts from their `scripts/`
  folders (the Anki builder also needs `pip install genanki`). You need a shell tool for these.
- **Photos:** `exam-practice` marks photos of handwritten answers, so your tool must accept images. If it can't,
  ask the student to type their answer.
- **Obsidian links:** `setup-obsidian` opens `obsidian://` install pages with the OS `open` command. Without a
  shell, give the student the links to click. Never download plugin or theme files yourself.
- **Calendar and email** in `weekly-review` are optional, read-only connectors. Skip those sections if you don't have them.
- **Obsidian views:** the tables are Bases views over note properties. Most are inline ```` ```base ```` blocks in
  dashboard pages (HOME, DEADLINES, TASKS, module pages); the careers views are in `careers/Roles.base`. You never
  need to edit them. Keep note properties exact, as listed in the templates and `careers/TRACKER.md`.
- **Dashboard pages** (`cssclasses: dashboard`) are built from `> [!dash-…]` callout cards. When you edit inside a
  card, keep every line's `> ` prefix. Sections that skills append to (Log, Weekly plan, the timetable's
  `<!-- week:start -->` block) are deliberately outside the cards, so append there as plain Markdown.
- **Study blocks** in `timetable/blocks/` are Full Calendar notes: keep their frontmatter keys and formats exactly
  (see `create-study-timetable`).
