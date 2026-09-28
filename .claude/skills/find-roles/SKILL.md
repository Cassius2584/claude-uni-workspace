---
name: find-roles
description: Search for graduate roles, internships or placements that match the user's careers brief. Checks their chosen job sites plus a broad web search, reads each job description, filters on hard requirements, scores fit, ranks by fit and urgency, and writes a dated digest with recommendations. Use when the user asks to "find roles", "check for new jobs/internships/placements", "run my job search", or when a scheduled task says to run find-roles.
---

# Find roles

Inputs: `careers/BRIEF.md`, `careers/CV.md`, `careers/SOURCES.md`, `careers/ROLES.md`,
`careers/APPLICATIONS.md`. If BRIEF.md or CV.md is missing, stop and suggest `setup-careers`.

**Tracker:** if `careers/TRACKER.md` exists, follow it for where roles, applications (and, for a spreadsheet,
sources and target employers) live. It describes either an **Obsidian Bases** tracker (one note per role in
`careers/roles/`) or a **spreadsheet**, and replaces ROLES.md / APPLICATIONS.md (and SOURCES.md for a
spreadsheet). "Append to ROLES.md" and "Filtered out table" below then mean the equivalent in that tracker.
Everything else still applies; only the storage changes.

**Scheduled runs:** follow any command rules in the task prompt or TRACKER.md exactly. Use the file tools for
file I/O, one tracker command per call, and no pipes, `&&`, `cd` or variables, so every call matches a
pre-approved permission.

**Scheduled mode** (the prompt says "scheduled", or nobody is there to answer): don't ask questions, skip
`browser` sources, never log in to anything, write the digest, and end with a 3-line summary.

## 1. Collect candidates
Work out today's date and the role types, titles, sectors and region from the brief.
1. **Enabled job boards** in SOURCES.md:
   - `fetch`: read the site's listing or search page for each title/role type (use the site's own search URL
     when you can find it, e.g. filtered by "graduate", "internship", "placement").
   - `search`: web search such as `site:linkedin.com/jobs "graduate software engineer" London 2027`.
   - `browser`: live sessions only, and only if the user is present to log in.
   - If a `fetch` source refuses (403, bot check, empty page), fall back to `search` for that source on this
     run, and suggest switching its **How** to `search` in SOURCES.md.
2. **Target employer pages** in SOURCES.md: read each early-careers page for open roles of the right type.
   - Employers' own applicant tracking systems are usually readable when job boards aren't. Search them
     directly, e.g. `site:job-boards.greenhouse.io`, `site:jobs.lever.co`, `site:jobs.ashbyhq.com`,
     `site:apply.workable.com` plus the title and "new grad" / "graduate" / "2027". Boards and aggregators are
     good for discovery, but always store the **original employer link**, not an aggregator copy.
   - Programmes and fellowships (research programmes, bootcamps, graduate fellowships) run on fixed yearly
     windows. Search for them by name every run, even when not listed as a source.
3. **Broad search:** 3–6 web searches combining titles, role type, year and region (e.g. `"2027 graduate
   scheme" machine learning UK`, `"summer internship 2027" quantitative developer London`), to catch roles
   on sites not listed.

Normalise each hit to *employer, title, type, location, link*. Give it an ID
`<employer>-<short-title>-<year>` in lowercase-hyphenated form. **Drop anything already in ROLES.md or
APPLICATIONS.md** (match on ID or link). Stop collecting at roughly 3× the digest size.

## 2. Read each description
Open every remaining job page and extract:
- Type (grad / internship / placement), **start date and time commitment** (full-time? cohort dates?),
  duration, location and working pattern.
- Salary (or "not stated"), **closing date** (or "rolling"; rolling means apply early).
- Eligibility: degree subject, minimum grade (e.g. 2:1, ABB), graduation year, right to work /
  sponsorship, security clearance.
- Must-have and nice-to-have skills.
- Process: online tests (e.g. HackerRank, SHL, Watson Glaser), video interview, assessment centre. Also note
  anything unusual (cover letter required, portfolio, early-deadline warning).

If a page won't load or is expired, drop the role and note it in the run summary.

## 3. Filter
Check each role against **Hard requirements** in the brief (location, right to work, grade, graduation
date, minimum salary, avoid-lists, employers to skip). Failures go into ROLES.md's **Filtered out** table
with the reason, and don't go into the digest.

**Availability is a flag, not a filter.** If a role's start date or commitment clashes with the brief's
"Available from" or term-time limits, keep it when it's a strong fit or a top tier. Say so plainly in the
gap line ("Jan cohort clashes with Semester 2, so ask about a later cohort"), and make the next step about
resolving the clash. Only filter it out if it's a weak fit anyway.

**Abroad:** keep only where a visa route is plausible for the student (see the brief), and name the route.

## 4. Score and rank
Score fit 0–100 using the weights in the brief (defaults: role/field 30, skills vs CV 25, location 15,
pay 10, employer preference 10, development 10). If the brief has a **priority tier table**, use it for the
role/field component, put "always surface" tiers at the top of the digest regardless of the digest size,
and filter the "filter out" row. Base "skills vs CV" only on what's actually in CV.md. Give
each score one line of reasoning: the main match and the main gap.

Rank by fit, then pull forward anything **closing within 14 days** or **rolling at a target employer**.
Label each role:
- **Apply now**: fit ≥ 75, or a target employer, or closing soon with fit ≥ 60.
- **Worth a look**: fit 60–74.
- **Stretch**: fit < 60 but an interesting employer or role. Include at most 2.

## 5. Write the digest
Create `careers/digests/<yyyy-mm-dd>.md`:

```markdown
# Roles – <Mon 28 Sep 2026>
<n> new roles checked · <k> recommended · <f> filtered out

## Top picks
1. **<Employer> – <Role>** (<type>, <location>) · Fit <82> · Closes <date / rolling>
   Why: <one line>. Gap: <one line>. Process: <tests → AC>. [Link](<url>)

## Worth a look
| Employer | Role | Type | Location | Salary | Closes | Fit | Why | Link |

## Stretch
…

## Heads-up
- <deadlines within 7 days from APPLICATIONS.md, target employers whose schemes usually open this month,
  sources that failed>
```

Then append every new role (recommended or not) to the top of ROLES.md's main table with status `new`.

**Closed programmes:** when a programme or scheme you found has already closed, don't add it as a role.
Put it under Heads-up with when the **next round opens**, and record that month in the target employer's
"Usual opening" (Watchlist / SOURCES.md) so future runs know when to look again.
Keep the digest to the size in the brief. Quality over volume.

## 6. Reply
In a live session, show the top picks and ask which to shortlist. Offer `prep-application` for any of them.
In scheduled mode, reply with three lines: counts, the single best role, and the nearest deadline.

## Rules
- Never apply, submit forms, create accounts on job sites or log in on the user's behalf.
- Never invent details. If the page doesn't say, write "not stated".
- Respect sites: read listing pages at a normal pace. Don't hammer them or get around login walls. Use web
  search for sites that block direct reading.
