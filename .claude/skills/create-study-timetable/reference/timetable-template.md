# TIMETABLE.md template

Create `timetable/TIMETABLE.md` from this. Replace `<…>`. Keep the two `week:` markers exactly as they are, and outside any `>` card:
`timetable.py` writes the week grid and hours between them.

```markdown
---
cssclasses:
  - dashboard
---

> [!dash-hero] Study timetable
> [Home](../HOME.md) [Open calendar](obsidian://adv-uri?commandid=full-calendar-remastered%3Afull-calendar-open) [Deadlines](../projects/DEADLINES.md) [Tasks](../tasks/TASKS.md)
> <Semester 1 2026/27> · teaching <28 Sep – 11 Dec 2026> · <reading week w/c 2 Nov>

> [!dash-week] This week
> ````fc-calendar
> defaultDate: today
> height: 900px
> weather: false
> layout:
>   orientation: horizontal
>   views:
>     - view: timeGridWeek
>       width: 100%
>       header: true
>       weather: false
> ````

> [!dash-info]- How the timetable works
> Each block is a note in [blocks/](blocks). The Full Calendar plugin shows them as a week view (calendar
> source: *Full Note*, folder `timetable/blocks`), and lectures come from the university timetable's subscribe
> link added as an *ICS* calendar. To change the plan, drag a block in the calendar, edit its note, or ask Claude
> ("move my Friday blocks to the morning"). Claude reruns the clash check afterwards.

## Preferences
| | |
|---|---|
| Study days | <Mon–Fri, Sat morning> |
| Hours | <09:00–18:00> |
| Best focus | <mornings> |
| Free | <Sunday, and Saturday afternoon> |
| Independent study target | <20 h/week> |
| Regular commitments | <Climbing club Wed 18:00–20:00 (15 min walk each way); job Sat 12:00–17:00> |
| Extras | <daily flashcards 08:45; weekly planning Sun 19:30> |

## This week
<!-- week:start -->
<!-- week:end -->

## How the hours are split
| Module | Credits | Hours/week | Why |
|---|---|---|---|
| <MA32064> | <5 ECTS> | <3> | <exam-only module; steady weekly practice> |

## Log
- <date>: Timetable created from <the uni timetable feed / screenshot> and a short interview.
```
