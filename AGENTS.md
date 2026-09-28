# AGENTS.md

This workspace was built for Claude Code, but it's plain Markdown, so any coding agent (Codex, Cursor, Gemini CLI,
etc.) can run it. If you're an agent other than Claude Code, start here.

## Setting this up for someone
Someone has asked you to "set up this uni workspace" (probably by pasting the repo link). Do this, in order:

1. **Explain first, then wait.** In 3–5 plain, non-technical sentences, say what it does: one folder per
   module built from their Moodle and official module specs, a single deadline board, a weekly "refresh Moodle",
   and optionally a job search with application prep. Say what you'll need: their university and degree, about
   10 minutes, and them logging in to Moodle themselves in a browser window. Mention that it works best viewed
   in the free Obsidian app. **Ask if they'd like to go ahead.** Don't download or create anything before a yes.
2. **If you can't touch their files** (a plain chat such as claude.ai, ChatGPT or the Gemini app), say so kindly
   and tell them to paste the same message into Claude's desktop app (Code tab), Codex or Gemini CLI. Stop there.
3. **Ask where to put it**, suggesting a new folder like `~/uni` (or `Documents/uni`). Then get the files:
   `git clone https://github.com/Cassius2584/claude-uni-workspace <folder>`, or if git isn't available, download
   `https://github.com/Cassius2584/claude-uni-workspace/archive/refs/heads/main.zip` and unzip it there. Then
   delete the `.git` folder if they won't be contributing back, so their own notes never get pushed anywhere.
4. **Work from that folder.** If your tool can switch its working folder, switch to it, so `CLAUDE.md` and the
   skills load. Otherwise read `CLAUDE.md` and the skill files there directly.
5. **Run setup-year**: follow `.claude/skills/setup-year/SKILL.md`. They sign in to their university themselves.
   Never type their password.
6. **Finish** with what they now have, how to open it in Obsidian ("Open folder as vault"), and the three
   things they can say next: "what's due?", "refresh Moodle" (weekly), and "set up careers" (optional).

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
