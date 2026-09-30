---
kind: module
code: MA30001
title: "Linear Algebra (EXAMPLE)"
semester: Semester 1
credits: 10
assessment: "Coursework 25% / Exam 75%"
leader: "Dr A. Example"
moodle: https://moodle.uni.example/course/view.php?id=12345
cssclasses:
  - dashboard
---

> [!dash-hero] MA30001 · Linear Algebra (EXAMPLE)
> [Moodle](https://moodle.uni.example/course/view.php?id=12345) [Catalogue](https://www.uni.example/catalogues/2026-2027/ma/MA30001.html) [Deadlines](../DEADLINES.md) [Lectures](lectures/) [Coursework](coursework/) [Resources](resources/)
> Semester 1 · 10 ECTS · Coursework 25% / Exam 75% · Dr A. Example

> [!dash-info] This is a made-up example
> It shows what a filled-in module looks like after `setup-year`. The module, staff, rooms and dates are fictional.
> It's kept out of your boards, so leave it as a reference (deleting it would make `git pull` complain later).

> [!dash-list] At a glance
> | | |
> |---|---|
> | **Term / year** | Semester 1 2026/27, Year 2 |
> | **Credits** | 10 ECTS (20 CATS), 200 study hours · FHEQ level 5 · Compulsory |
> | **Module leader** | Dr A. Example · a.example@uni.example · Room 4W 1.01 |
> | **Timetable** | Lectures Mon 10:15 (1W 2.01), Thu 12:15 (3E 1.01) · Problem class Fri 09:15 (8W 2.1) |
> | **VLE / Moodle** | https://moodle.uni.example/course/view.php?id=12345 |
> | **Unit catalogue** | https://www.uni.example/catalogues/2026-2027/ma/MA30001.html |

> [!dash-graded] Assessments
> ```base
> filters:
>   and:
>     - kind == "assessment"
>     - file.inFolder("projects/EXAMPLE-MA30001-linear-algebra")
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
> Briefs, drafts and feedback: `coursework/`.
>
> **Rules to remember**
> - CW1 is **closed lane**: no GenAI use permitted.
> - Formula book is provided in the exam. Copy in `resources/` (not committed).

## What it's about
Vector spaces and the linear maps between them: bases, dimension, eigenvalues and diagonalisation, inner
products and the spectral theorem. It's the language behind most of applied maths, statistics and machine
learning.

## Learning outcomes
_Source: unit catalogue 2026/27._
1. Work with abstract vector spaces, subspaces, bases and dimension.
2. Represent linear maps as matrices and change basis.
3. Compute eigenvalues and eigenvectors and decide when a matrix is diagonalisable.
4. Apply inner products, orthogonality and the spectral theorem.

## Weekly plan
| Week | Topic | Notes |
|---|---|---|
| 1 | Vector spaces and subspaces | `lectures/week-01-vector-spaces.md` |
| 2 | Bases and dimension | |
| 3 | Linear maps and matrices | |
| 4 | Change of basis | |
| 5 | Determinants | |
| 6 | Eigenvalues and eigenvectors | CW1 set |
| 7 | Diagonalisation | |
| 8 | Inner product spaces | |
| 9 | Orthogonality, Gram–Schmidt | CW1 due Fri |
| 10 | Spectral theorem | |
| 11 | Revision | |

## Key readings
- Axler, S. (2024) *Linear Algebra Done Right*. 4th edn. Springer. (essential; free online)

## Log
- 28 Sep 2026: Module set up from unit catalogue and Moodle.
- 5 Oct 2026: Added week 1 lecture notes.
- 16 Oct 2026: CW1 brief saved to `coursework/cw1-problem-set/`; started draft.
