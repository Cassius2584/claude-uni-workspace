# Tracker: Obsidian Bases

_Copy to `careers/TRACKER.md` to use this mode. When `careers/TRACKER.md` exists, the careers skills store roles
and applications as described here instead of in ROLES.md / APPLICATIONS.md. Sources and target employers stay in
`SOURCES.md`._

- **Mode:** Obsidian Bases, with one Markdown note per role plus a database view
- **Role notes:** `careers/roles/<id>.md`, created from `careers/_template/role.md`
- **Prep files:** `careers/roles/<id>/` (job.md, fit.md, drafts.md, prep.md), linked from the role note
- **View:** `careers/Roles.base` (copied from `careers/_template/Roles.base`). Open it in Obsidian (1.9 or later,
  with the Bases core plugin on) for the tabs *Open roles · By deadline · Applications · Board · Filtered out*.

## Properties (frontmatter), exact names and values
| Property | Values |
|---|---|
| `kind` | always `role` (the view filters on it) |
| `priority` | Now · Next · Later · Applied · Expired or N/A |
| `company`, `role`, `location`, `start`, `next_step`, `link`, `source` | text |
| `type` | Grad · Internship · Placement |
| `fit` | integer 0–100 |
| `tier` | integer from the brief's tier table (blank if none) |
| `salary` | number, blank if not stated |
| `deadline`, `next_date`, `found` | `YYYY-MM-DD`; `deadline` blank = rolling |
| `stage` | Not applied · Applied · Online tests · Video interview · Assessment centre · Offer · Rejected · Withdrawn · Filtered out |
| `reason` | why it was filtered out (only when `stage: Filtered out`) |

## How the skills use it
- **find-roles:** dedupe by checking for an existing `careers/roles/<id>.md` (or a note with the same `link`).
  For each new role, write a note from the template: recommended roles get stage **Not applied** and priority from
  the label (Apply now → Now, Worth a look → Next, Stretch → Later). Filtered roles get a short note with stage
  **Filtered out** and a `reason`, so they're never re-checked.
- **prep-application:** create `careers/roles/<id>/`, link the prep files under the note's *Prep* heading, and set
  `priority: Now` with the next step and date.
- **whats-due:** read notes whose `deadline` or `next_date` falls in the window and whose stage isn't
  Rejected / Withdrawn / Filtered out.
- **Status updates** ("I applied to X"): edit that note's properties and add a line to its *Log*.

Use the Write/Edit tools on the notes directly. No scripts or shell commands are needed, which keeps scheduled
runs approval-free.
