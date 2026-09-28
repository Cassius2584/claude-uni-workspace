# Tracker: spreadsheet

_Copy to `careers/TRACKER.md` to track roles in a spreadsheet instead of ROLES.md / APPLICATIONS.md / SOURCES.md.
When this file exists, the careers skills read and write the sheet described here._

- **Sheet:** <name> · <link>
- **ID:** <spreadsheet id>
- **Tool:** <how Claude reads/writes it, e.g. the google-workspace skill, a Google Drive connector, Excel>

## Tabs and columns (exact order)
| Tab | Columns | Used for |
|---|---|---|
| Roles | Priority · Company · Role · Type · Fit · What they do, what's the role · Location · Start + length · Salary · Deadline · Days left · How to apply · What they look for · Process · Stage · Next step · Next step date · Comments · Link · Source · Found · ID | every role seen (dedupe on ID or Link) + application tracking |
| Pipeline | Stage · Roles | live counts, no writes |
| Watchlist | Company · Interest · What they do · History · Why · Usual opening · Careers page · Lead / intro | target employers |
| Sites | On · Site · URL · Good for · How | sources to check (`On` = Yes) |
| Events | Rating · Event · Date · Company · What they do, location · Comments | careers fairs, talks |
| Filtered out | Found · Company · Role · Reason · Link · ID | failed hard requirements |

## Values
- **Priority:** Now · Next · Later · Applied · Expired or N/A
- **Type:** Grad · Internship · Placement
- **Stage:** Not applied · Applied · Online tests · Video interview · Assessment centre · Offer · Rejected · Withdrawn
- New roles from `find-roles`: Priority from its label (Apply now → Now, Worth a look → Next, Stretch → Later),
  Stage **Not applied**. Leave Deadline blank for rolling roles and say "Rolling" in How to apply.
- **Days left** is a formula: `=IF(J<row>="","",J<row>-TODAY())`.
- Dates as `YYYY-MM-DD`, salary as a number (blank if not stated).

## Commands
Test each once and write down the exact form that worked, e.g. whether data is passed inline or as a path to
a JSON file, and whether adding rows keeps formatting and formulas.
- Read: <command>
- Add rows: <command>
- Update a cell: <command>
