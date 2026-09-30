---
name: exam-practice
description: Exam-style practice for a module. Sets a past-paper or exam-style question (definitions, statements, short proofs, calculations) on results the student should know, has them answer by hand and send a photo, marks it strictly against a mark scheme written in advance, and logs scores and weak spots with next-review dates. Also runs timed mock papers. Use when the student says "quiz me", "give me an exam question", "test me on <topic/chapter>", "exam practice", "mark my answer", "mock exam", or sends a photo of a handwritten answer to a question you set.
---

# Exam practice

Practice that looks like the exam: a question with marks, answered **by hand** under exam conditions, photographed,
and marked like an examiner would. Everything is recorded in the module folder:

```
projects/<module>/
├── practice.md                ← log of every attempt, weak spots with next-review dates, past-paper questions used
└── practice/.pending-scheme.md ← the mark scheme for the question currently set (hidden in Obsidian: dot-file)
```

## 0. Before you start
- Read the module's `MODULE.md`, its assessment notes (exam format, length, closed or open book), the tiers page
  (`proof-tiers.md` or similar, from `create-flashcards`), `flashcards/cards.md` if present, the lecture notes,
  and the past papers and solutions in `resources/`.
- Read `practice.md` if it exists (create it from [reference/practice-log.md](reference/practice-log.md) if not,
  and add a link to it from the tiers page).
- **Scope:** during teaching, only chapters that have been lectured (MODULE.md weekly plan, the latest
  `projects/updates/` digest, or ask). In the revision period, everything examinable. Skip anything the notes or
  the tiers page mark non-examinable.

## 1. Choose the question
In order of preference:
1. **Weak spots due for review** (`practice.md`, next-review date today or earlier).
2. **A real past-paper question** on lectured material that hasn't been used yet (`practice.md` lists the ones
   used). Only use the parts the paper marks as relevant to this year's module. Past papers are the best practice,
   but there are few of them, so save full papers for mock exams in the revision period.
3. **An exam-style question you write**, modelled on the past papers' style and mark split: typically a definition
   or statement (2–5 marks), a short proof of a Tier A result or an unseen lemma using the same technique
   (4–8 marks), and a calculation (3–6 marks). Tier B results: ask for the key idea and outline, or one step.
   Rotate chapters, and favour results the student hasn't practised yet.
The student can override: "test me on Euler's criterion", "a calculation question", "a whole past paper".

## 2. Set it
1. **First, write the mark scheme** to `practice/.pending-scheme.md`: each part's marks, what earns each mark
   (precise definition wording, the key steps of the proof, method marks and accuracy marks for calculations),
   common errors to penalise, and a model answer. For a past-paper question, base it on the official solutions
   and their mark split. Don't show it, and tell the student it's there and not to open it.
2. **Then present the question** in chat: numbered parts with marks in brackets `[4]`, maths in LaTeX, and a
   suggested time (use the paper's pace if known, e.g. 120 minutes for 80 marks = 1.5 min per mark; otherwise
   1.5 min per mark).
3. **Conditions:** closed book if the exam is (no notes, no flashcards). Answer on paper, then send a photo of
   each page, in order. Typed answers are fine if they prefer.

## 3. Mark it
- **Read the photo carefully.** If a line is unreadable, ask about that line rather than guessing, and never
  give credit for something you can't read.
- **Mark against the scheme, strictly and fairly**, as a university examiner would:
  - **Definitions and statements:** full marks only for the exact meaning with every hypothesis
    ("gcd(a, m) = 1", "p an odd prime"). Missing a hypothesis loses a mark. Wrong or vague wording loses the mark.
  - **Proofs:** marks for each key step in the scheme. Correct alternative proofs get full credit. A proof that
    assumes what it's meant to show, or skips the key step, gets only the marks for the steps it actually shows.
  - **Calculations:** method marks for a correct method even when the arithmetic slips (follow-through), and
    accuracy marks only for correct values.
  - Don't give marks for effort, length, or things that weren't asked.
- **Feedback**, in this order:
  1. A score per part and in total (`14/20`).
  2. For each lost mark: what was missing or wrong, quoting their line, and the correct version.
  3. One **"remember this"** line per weak point: the exact phrase or key step to learn.
  4. The model answer for any part scoring under half.
- Then delete `practice/.pending-scheme.md`, and put the model answer in the log entry instead.

## 4. Log it
Add to `practice.md`:
- a row in **Attempts**: date · question (source: "2025 Q2(c)" or "set") · results tested (links to tiers or cards)
  · score · one-line note;
- for each weak point, a row in **Weak spots**: result · what went wrong · next review. Schedule the next review
  from the score on that result: **under 50% → 2 days, 50–79% → 7 days, 80%+ → 21 days**. A spot scoring 80%+
  twice in a row moves to **Cleared**;
- past-paper parts used, in **Past papers used**.
If a definition or statement was wrong, offer to add or fix its flashcard (`create-flashcards`).
Tiers are the lecturer's call, so don't change them. Do flag it if a Tier B result keeps coming up in questions.

## 5. Next
Offer another question: a weak spot, the next chapter, or "same result, different angle". In the revision
period, suggest a **timed mock**: the relevant questions from one past paper, in one sitting, at the paper's
pace. Mark each question as above, then give a total and the three weakest areas.

## Rules
- **Practice only.** Don't answer or mark anything that will be submitted for credit. For formative problem sheets,
  give hints and check reasoning (not full solutions), and only if the module's GenAI rules allow it.
- Past papers and solutions are the university's copyright: quote what's needed for the question and the
  marking, keep them in the module folder, and never commit or share them.
- Photos of answers stay in the conversation. Save them into `practice/attempts/` only if the student asks.
