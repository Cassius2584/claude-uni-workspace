# Tasks

Everything that isn't a university assessment or a job application: uni admin, project work, life, money. Each
task is one note in this folder, viewed through [Tasks.base](Tasks.base) (views: *Today · This week · Inbox ·
By area · Board · Done*). Assessments stay in `projects/*/assessments/` and roles in `careers/roles/`, and
[HOME](../HOME.md) shows all three together.

![[Tasks.base]]

## Adding a task
- **In Claude:** "task: email supervisor about project scope by Fri". Claude creates the note.
- **In Obsidian:** copy [_template/task.md](_template/task.md), set `kind: task`, and fill in the properties.
- **File name:** a short slug, e.g. `email-supervisor-scope.md`.

## Properties (exact names and values)
| Property | Values |
|---|---|
| `kind` | always `task` (the template says `<task>` so it never shows up itself) |
| `title` | short, starts with a verb: "Email supervisor about scope" |
| `status` | Inbox · Next · Doing · Waiting · Done |
| `area` | Uni · Careers · Life · Admin · Money |
| `priority` | High · Medium · Low |
| `due` | `YYYY-MM-DD`, or blank if there's no date |
| `link` | optional link to a module, assessment or role note, e.g. `"[[projects/CM30001-machine-learning/MODULE\|CM30001]]"` |
| `created`, `done` | `YYYY-MM-DD`; set `done` when status becomes Done |

**Statuses:** *Inbox* means captured but not sorted yet. *Next* means ready to do soon. *Doing* is in progress.
*Waiting* is blocked on someone else (say who in Notes). *Done* is finished (keep the note, don't delete it).

## Rules for Claude
- "task: …" or "add a task" → create a note from the template. Infer `area` and `link` from context. Default
  `status: Inbox`, or `Next` if it has a due date within 7 days.
- "Done with X" → set `status: Done` and `done`, and add a Log line.
- Something with a VLE deadline is an **assessment**, not a task. A task can link to one ("draft lit survey
  intro" → link to the survey's assessment note).
- **Planning back from coursework:** when a coursework brief arrives, offer to split it into 3–5 tasks
  (research, outline, draft, check, submit) with `due` dates counted back from the deadline, each linked to the
  assessment note. If a study timetable exists, the tasks should fit its blocks for that module.
