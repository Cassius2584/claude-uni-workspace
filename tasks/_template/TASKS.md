---
cssclasses:
  - dashboard
---

> [!dash-hero] Tasks
> [Home](../HOME.md) [Deadlines](../projects/DEADLINES.md) [Timetable](../timetable/TIMETABLE.md) [New task template](_template/task.md)
> Say "task: …" to add one, and "done with …" to close it.

> [!dash-tasks] Today
> ```base
> filters:
>   and:
>   - kind == "task"
> views:
> - type: table
>   name: Today
>   filters:
>     and:
>     - status != "Done"
>     - or:
>       - status == "Doing"
>       - due <= today() + "1d"
>   order:
>   - title
>   - area
>   - status
>   - priority
>   - due
>   - link
>   sort:
>   - property: due
>     direction: ASC
> ```

> [!dash-due] This week
> ```base
> filters:
>   and:
>   - kind == "task"
> views:
> - type: table
>   name: This week
>   filters:
>     and:
>     - status != "Done"
>     - due <= today() + "7d"
>   order:
>   - due
>   - title
>   - area
>   - status
>   - priority
>   - link
>   sort:
>   - property: due
>     direction: ASC
> ```

> [!dash-inbox] Inbox
> ```base
> filters:
>   and:
>   - kind == "task"
> views:
> - type: table
>   name: Inbox
>   filters:
>     and:
>     - status == "Inbox"
>   order:
>   - title
>   - area
>   - due
>   - created
>   sort:
>   - property: created
>     direction: DESC
> ```

> [!dash-board] Board
> ```base
> filters:
>   and:
>   - kind == "task"
> views:
> - type: cards
>   name: Board
>   filters:
>     and:
>     - status != "Done"
>   groupBy:
>     property: status
>     direction: ASC
>   order:
>   - title
>   - area
>   - due
>   - priority
> ```

> [!dash-list]- By area
> ```base
> filters:
>   and:
>   - kind == "task"
> views:
> - type: table
>   name: By area
>   filters:
>     and:
>     - status != "Done"
>   groupBy:
>     property: area
>     direction: ASC
>   order:
>   - area
>   - title
>   - status
>   - priority
>   - due
>   sort:
>   - property: due
>     direction: ASC
> ```

> [!dash-done]- Done
> ```base
> filters:
>   and:
>   - kind == "task"
> views:
> - type: table
>   name: Done
>   filters:
>     and:
>     - status == "Done"
>   order:
>   - done
>   - title
>   - area
>   sort:
>   - property: done
>     direction: DESC
> ```

> [!dash-info]- How tasks work
> Everything that isn't a university assessment or a job application: uni admin, project work, life, money. Each
> task is one note in this folder, shown in the cards above. Assessments stay in `projects/*/assessments/` and
> roles in `careers/roles/`, and [HOME](../HOME.md) shows all three together.
>
> ### Adding a task
> - **In Claude:** "task: email supervisor about project scope by Fri". Claude creates the note.
> - **In Obsidian:** copy [_template/task.md](_template/task.md), set `kind: task`, and fill in the properties.
> - **File name:** a short slug, e.g. `email-supervisor-scope.md`.
>
> ### Properties (exact names and values)
> | Property | Values |
> |---|---|
> | `kind` | always `task` (the template says `<task>` so it never shows up itself) |
> | `title` | short, starts with a verb: "Email supervisor about scope" |
> | `status` | Inbox · Next · Doing · Waiting · Done |
> | `area` | Uni · Careers · Life · Admin · Money |
> | `priority` | High · Medium · Low |
> | `due` | `YYYY-MM-DD`, or blank if there's no date |
> | `link` | optional link to a module, assessment or role note, e.g. `"[[projects/CM30001-machine-learning/MODULE\|CM30001]]"` |
> | `created`, `done` | `YYYY-MM-DD`; set `done` when status becomes Done |
>
> **Statuses:** *Inbox* means captured but not sorted yet. *Next* means ready to do soon. *Doing* is in progress.
> *Waiting* is blocked on someone else (say who in Notes). *Done* is finished (keep the note, don't delete it).
>
> ### Rules for Claude
> - "task: …" or "add a task" → create a note from the template. Infer `area` and `link` from context. Default
>   `status: Inbox`, or `Next` if it has a due date within 7 days.
> - "Done with X" → set `status: Done` and `done`, and add a Log line.
> - Something with a VLE deadline is an **assessment**, not a task. A task can link to one ("draft lit survey
>   intro" → link to the survey's assessment note).
> - **Planning back from coursework:** when a coursework brief arrives, offer to split it into 3–5 tasks
>   (research, outline, draft, check, submit) with `due` dates counted back from the deadline, each linked to the
>   assessment note. If a study timetable exists, the tasks should fit its blocks for that module.
