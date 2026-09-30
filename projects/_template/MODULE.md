---
kind: <module>
code: <CODE>
title: "<Module title>"
semester: <Semester 1 | Semester 2 | Full year>
credits: <10>
assessment: "<e.g. Coursework 30% / Exam 70%>"
leader: "<name>"
moodle: <link>
cssclasses:
  - dashboard
---

> [!dash-hero] <CODE> · <Module title>
> [Moodle](<link>) [Catalogue](<link>) [Deadlines](../DEADLINES.md) [Lectures](lectures/) [Coursework](coursework/) [Resources](resources/)
> <Semester> · <credits> ECTS · <assessment> · <leader>

> [!dash-list] At a glance
> | | |
> |---|---|
> | **Term / year** | <e.g. Semester 1 2026/27, Year 3> |
> | **Credits** | <e.g. 10 ECTS (20 CATS) · level · compulsory/optional> |
> | **Module leader** | <name · email · office> |
> | **Timetable** | <e.g. Lecture Mon 10:00 (Room), Lab Thu 14:00 (Room)> |
> | **VLE / Moodle** | <link> |
> | **Unit catalogue** | <link> |

> [!dash-graded] Assessments
> ```base
> filters:
>   and:
>     - kind == "assessment"
>     - file.inFolder("projects/<CODE>-<short-name>")
> views:
>   - type: table
>     name: Assessments
>     order:
>       - item
>       - type
>       - weight
>       - due
>       - due_note
>       - status
>       - mark
>     sort:
>       - property: due
>         direction: ASC
> ```
> _Each assessment is a note in `assessments/`. Update status and marks there. All deadlines: [DEADLINES](../DEADLINES.md)._
>
> Briefs, drafts and feedback: `coursework/` (one subfolder per assessment).
>
> **Rules to remember**
> - <GenAI policy for each assessment, group-work rules, qualifying marks, ethics approval…>

## What it's about
<2–4 sentences in plain English: what the module covers and why it matters.>

## Learning outcomes
_Source: <unit catalogue / VLE>._
1. <…>

## Weekly plan
| Week | Topic | Notes |
|---|---|---|
| 1 | <…> | `lectures/week-01-….md` |

## Key readings
- <Author (Year) *Title*. Publisher.> (essential)

## Log
- <date>: Module set up.
