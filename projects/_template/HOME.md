---
cssclasses:
  - dashboard
---

> [!dash-hero] <Semester 1 · 2026/27>
> [Deadlines](projects/DEADLINES.md) [Timetable](timetable/TIMETABLE.md) [Tasks](tasks/TASKS.md) [Careers](careers/TRACKER.md) [Review](reviews/latest.md) [Moodle](projects/updates/MOODLE.md)

> [!dash-priorities] This week's priorities
> ![[reviews/latest#3 priorities]]
> *From the latest [weekly review](reviews/latest.md), refreshed every Sunday*

> [!dash-week] Next 7 days
> ```fc-calendar
> defaultDate: today
> startOffset: 0d
> endOffset: +6d
> height: fit
> weather: false
> layout:
>   orientation: horizontal
>   views:
>     - view: listWeek
>       width: 100%
>       header: true
>       weather: false
> ```

> [!dash-due] Due in the next 14 days
> ```base
> filters:
>   or:
>     - and:
>         - kind == "assessment"
>         - status != "Submitted"
>         - status != "Marked"
>         - due <= today() + "14d"
>         - not:
>             - file.inFolder("projects/EXAMPLE-MA30001-linear-algebra")
>     - and:
>         - kind == "task"
>         - status != "Done"
>         - due <= today() + "14d"
>     - and:
>         - kind == "role"
>         - stage != "Rejected"
>         - stage != "Withdrawn"
>         - stage != "Filtered out"
>         - stage != "Offer"
>         - formula.when <= today() + "14d"
> formulas:
>   when: if(kind == "role", if(deadline, deadline, next_date), due)
>   due_label: formula.when.format("ddd D MMM")
>   what: if(kind == "assessment", item, if(kind == "task", title, company + " – " + role))
>   where: if(kind == "assessment", code, if(kind == "task", area, "Careers"))
> properties:
>   formula.due_label:
>     displayName: Due
>   formula.what:
>     displayName: What
>   formula.where:
>     displayName: Module / area
>   note.status:
>     displayName: Status
> views:
>   - type: table
>     name: Next 14 days
>     order:
>       - formula.due_label
>       - formula.what
>       - formula.where
>       - status
>     sort:
>       - property: formula.when
>         direction: ASC
> ```

> [!dash-graded] Graded work ahead
> ```base
> filters:
>   and:
>     - kind == "assessment"
>     - weight > 0
>     - status != "Submitted"
>     - status != "Marked"
>     - not:
>         - file.inFolder("projects/EXAMPLE-MA30001-linear-algebra")
> formulas:
>   due_label: if(due, due.format("ddd D MMM YYYY"), due_note)
> properties:
>   formula.due_label:
>     displayName: Due
>   note.code:
>     displayName: Module
>   note.item:
>     displayName: Assessment
>   note.weight:
>     displayName: Weight %
>   note.status:
>     displayName: Status
> views:
>   - type: table
>     name: Graded work
>     order:
>       - formula.due_label
>       - code
>       - item
>       - weight
>       - status
>     sort:
>       - property: due
>         direction: ASC
> ```

> [!dash-careers] Apply now
> ```base
> filters:
>   and:
>     - kind == "role"
>     - priority == "Now"
>     - stage == "Not applied"
> properties:
>   note.company:
>     displayName: Company
>   note.role:
>     displayName: Role
>   note.fit:
>     displayName: Fit
>   note.next_step:
>     displayName: Next step
> views:
>   - type: table
>     name: Apply now
>     order:
>       - company
>       - role
>       - fit
>       - next_step
>     sort:
>       - property: fit
>         direction: DESC
> ```
> *[Careers dashboard](careers/TRACKER.md)*

> [!dash-tasks] Tasks
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

> [!dash-revision] Revision
> **Flashcards:** the Flashcards button in the sidebar. Unlock each chapter once it's been lectured.
> **Exam practice:** say "quiz me on <CODE>". Each module's `practice.md` has the log and weak spots.

_Template note (setup removes this): delete any card whose feature isn't set up yet, **and the header pills that
point at it** (Timetable, Careers, Review, Moodle), then add them back when it is.
No timetable → "Next 7 days"; no weekly review → "priorities"; no careers → "Apply now"; no tasks → "Tasks";
no flashcards or practice → "Revision". Styling comes from `setup-obsidian` (the `dashboard` CSS snippet)._
