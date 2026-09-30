---
cssclasses:
  - dashboard
---

> [!dash-hero] Deadlines · <academic year>
> [Home](../HOME.md) <one pill per module: [CODE](<CODE>-<short-name>/MODULE.md)>

> [!dash-busy] Busy spots
> <weeks where several deadlines cluster, one line each>

> [!dash-due] Due next
> ```base
> filters:
>   and:
>   - kind == "assessment"
>   - not:
>     - file.inFolder("projects/EXAMPLE-MA30001-linear-algebra")
> views:
> - type: table
>   name: Due next
>   filters:
>     and:
>     - status != "Submitted"
>     - status != "Marked"
>   order:
>   - due
>   - due_time
>   - module
>   - item
>   - type
>   - weight
>   - status
>   - due_note
>   sort:
>   - property: due
>     direction: ASC
> ```

> [!dash-graded] Graded only
> ```base
> filters:
>   and:
>   - kind == "assessment"
>   - not:
>     - file.inFolder("projects/EXAMPLE-MA30001-linear-algebra")
> views:
> - type: table
>   name: Graded only
>   filters:
>     and:
>     - weight > 0
>   order:
>   - due
>   - module
>   - item
>   - type
>   - weight
>   - status
>   - mark
>   - due_note
>   sort:
>   - property: due
>     direction: ASC
> ```

> [!dash-board] Board
> ```base
> filters:
>   and:
>   - kind == "assessment"
>   - not:
>     - file.inFolder("projects/EXAMPLE-MA30001-linear-algebra")
> views:
> - type: cards
>   name: Board
>   filters:
>     and:
>     - status != "Marked"
>   order:
>   - item
>   - module
>   - due
>   - weight
>   - status
>   sort:
>   - property: due
>     direction: ASC
> ```

> [!dash-list]- Modules
> ```base
> filters:
>   and:
>   - kind == "module"
>   - not:
>     - file.inFolder("projects/EXAMPLE-MA30001-linear-algebra")
> views:
> - type: table
>   name: All modules
>   order:
>   - file.folder
>   - code
>   - title
>   - semester
>   - credits
>   - assessment
>   - leader
>   - moodle
>   sort:
>   - property: code
>     direction: ASC
> ```

> [!dash-list]- By module
> ```base
> filters:
>   and:
>   - kind == "assessment"
>   - not:
>     - file.inFolder("projects/EXAMPLE-MA30001-linear-algebra")
> views:
> - type: table
>   name: By module
>   order:
>   - module
>   - item
>   - type
>   - weight
>   - due
>   - status
>   - mark
>   sort:
>   - property: code
>     direction: ASC
>   - property: due
>     direction: ASC
> ```

> [!dash-done]- Done
> ```base
> filters:
>   and:
>   - kind == "assessment"
>   - not:
>     - file.inFolder("projects/EXAMPLE-MA30001-linear-algebra")
> views:
> - type: table
>   name: Done
>   filters:
>     or:
>     - status == "Submitted"
>     - status == "Marked"
>   order:
>   - module
>   - item
>   - weight
>   - status
>   - mark
> ```

> [!dash-info]- How deadlines work
> Every assessment is a note in its module's `assessments/` folder. Those notes are the source of truth for dates,
> weights, status and marks. This page shows them in the cards above, each an inline base view. Add a pill to the
> header for each module, and keep Busy spots current.
