---
cssclasses:
  - dashboard
---

> [!dash-hero] Moodle updates
> [Home](../../HOME.md) [Deadlines](../DEADLINES.md)
> Say "refresh Moodle" (weekly) to check every module for changes. Each sync writes one digest here.

> [!dash-list] Digests
> ```base
> filters:
>   and:
>     - file.inFolder("projects/updates")
>     - file.name != "MOODLE"
> properties:
>   file.name:
>     displayName: Sync
> views:
>   - type: table
>     name: Digests
>     order:
>       - file.name
>     sort:
>       - property: file.name
>         direction: DESC
> ```
