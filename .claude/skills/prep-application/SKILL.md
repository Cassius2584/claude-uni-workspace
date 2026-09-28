---
name: prep-application
description: Prepare an application for one specific role. Saves the job description, maps its requirements against the user's CV, drafts tailored CV bullets and a cover letter or answers to application questions, lists likely tests and interview questions, and tracks the deadline. Use when the user says "prep/help me apply for <role>", "shortlist <role>", "write a cover letter for <role>", or shares a job link they want to apply to.
---

# Prep an application

Inputs: a role (an ID from `careers/ROLES.md`, a link or pasted text), plus `careers/CV.md` and
`careers/BRIEF.md`. If `careers/TRACKER.md` exists, roles and applications live in that spreadsheet
instead of ROLES.md / APPLICATIONS.md, so read and update the role's row there (see TRACKER.md).

## 1. Folder and job description
Create `careers/roles/<id>/`. Save the full job description as `job.md` (title, employer, link, date
saved, then the text). Pages often disappear after the closing date, so save everything, including the
eligibility and process sections.

## 2. Fit map (`fit.md`)
A table mapping each **requirement** from the description to **evidence in CV.md** (quote it), and a rating:
Strong / Partial / Gap. Under the table:
- **Top 3 selling points** for this role.
- **Gaps and how to handle them:** reframe real experience, mention relevant modules or projects from
  `projects/`, or accept the gap. Never suggest claiming something that isn't true.
- **Employer research:** 3–5 facts worth knowing (what they do, recent news, values they emphasise),
  each with a source link.

## 3. Drafts (`drafts.md`)
- **CV tweaks:** reordered or reworded bullets from CV.md that foreground what this role wants. Rewording only;
  no new claims.
- **Cover letter** (if asked for or useful): under 350 words, specific to this employer and role, in the
  student's voice (UK English). Mark it clearly as a draft for them to rewrite.
- **Application questions:** if the form has them ("Why us?", "Describe a time…"), draft STAR-structured
  answers using only real experience from CV.md. Leave `[add detail]` where only the student can fill in.

## 4. Process prep (`prep.md`)
List the stages from the job description. For each: what it involves, how to practise (e.g. HackerRank
easy/medium problems in their language, numerical reasoning practice, the employer's own practice tests),
and 5–8 likely interview questions (technical and behavioural) for this role.

## 5. Track it
- Set the role's status in ROLES.md to `shortlisted`.
- Add a row to `careers/APPLICATIONS.md`: stage **To apply**, the closing date (or "rolling, aim for
  <date one week from today>"), and the folder.
- With a spreadsheet tracker, do the equivalent on the role's row instead (TRACKER.md says which columns: e.g.
  priority **Now**, stage **Not applied**, next step + date), adding the row first if the role came from a link.
- Say what the student needs to do next, and by when.

## Rules
- The student submits. Never fill in or submit application forms.
- If the brief or module files say GenAI use is restricted for something, respect it. Many employers also ask
  that applications be the candidate's own work, so frame drafts as starting points and remind them once.
