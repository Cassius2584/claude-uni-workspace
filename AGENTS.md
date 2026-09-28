# AGENTS.md

This workspace was built for Claude Code, but it's plain Markdown, so any coding agent (Codex, Cursor, Gemini CLI,
etc.) can run it. If you're an agent other than Claude Code, start here.

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
| "add module X", "I'm also taking X" | [.claude/skills/add-module/SKILL.md](.claude/skills/add-module/SKILL.md) |
| "what's due?", "what should I work on?" | [.claude/skills/whats-due/SKILL.md](.claude/skills/whats-due/SKILL.md) |
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
