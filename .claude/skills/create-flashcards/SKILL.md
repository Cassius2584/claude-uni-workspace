---
name: create-flashcards
description: Build and maintain spaced-repetition flashcards for a module from its own notes, as Obsidian Spaced Repetition notes (default) and/or an Anki deck, with one subdeck per chapter, plus a tiers page saying which proofs or derivations to reproduce, reconstruct or just state. Use when the student asks for flashcards, an Anki deck, revision cards, help memorising definitions and theorems word for word, "add cards for week N / chapter N", "which proofs do I need to learn?", to switch a module's cards between Anki and Obsidian, or for concept notes that link ideas across modules ("link concepts for X", "make the graph useful").
---

# Create flashcards

Turns a module's notes into **one source file**, `flashcards/cards.md`, and builds the decks from it with the
scripts in this skill. It pairs the deck with a **tiers page** so the student knows how deeply to learn each proof.

```
projects/<module>/
├── proof-tiers.md             ← A reproduce · B reconstruct · C statement only (named after the label)
└── flashcards/
    ├── cards.md               ← the source of truth: edit this, then rebuild
    ├── obsidian/<Section>.md  ← Obsidian Spaced Repetition notes, one per chapter (default)
    └── <CODE>.apkg            ← Anki deck, only if the student wants it (import with File → Import)
```

Scripts (paths relative to this skill's folder):
- `python3 scripts/build_obsidian.py <module-folder>` needs no extra packages.
- `python3 scripts/build_anki.py <module-folder>` needs `genanki` (`python3 -m pip install --user genanki`).

Both check `cards.md` first (duplicate titles, unbalanced `$` or braces, `\left`/`\right` pairs, clozes without
deletions) and stop with a list of problems. Fix them and rerun.

## 0. Before you start
- Read the module's `MODULE.md`, its assessment notes (is there an exam, and how much is it worth?), the lecture
  notes in `resources/` and `lectures/`, and any past papers and solutions. **Cards come only from these.** Never
  invent content, and never guess a theorem number.
- If the notes come in several versions (PDF and HTML, this year and last year), use the newest, follow its
  numbering, and say which one you used.
- If `flashcards/cards.md` already exists, you're **updating** (see section 5), not starting again.
- **Default to Obsidian:** everything stays in the vault, next to the notes. The student installs the community
  plugin *Spaced Repetition* (by Stephen Mwangi) themselves: Settings → Community plugins → Browse. Mention
  **Anki** once as an option, for students who want a dedicated phone app or Anki's FSRS scheduler, and build
  it only if they say yes. Record the choice in MODULE.md.

## 1. Write `flashcards/cards.md`
Follow [reference/card-format.md](reference/card-format.md) exactly: the format, the card types and the writing
rules. In short:
- Frontmatter: `code`, `title`, and `label`. The label is what proof cards are called: *Proof* for pure maths,
  *Derivation* for statistics or physics, *Method* or *Argument* elsewhere.
- One `## ` section per chapter (or week), in lecture order. Those become the subdecks.
- For each chapter: **definitions** word for word; **fill-in-the-blank (cloze) statements** for every theorem;
  **"Name the result"** cards for named results; **worked examples** from the notes (check the arithmetic); a
  **proof card** (key idea plus outline) for every Tier A or B result; and cards for any past exam question.
- Correct obvious typos in the notes, and say so on the card (`X:`) and to the student.

## 2. Write the tiers page
Use [reference/tiers.md](reference/tiers.md). Name it after the label, e.g. `proof-tiers.md` or
`derivation-tiers.md`, at the top level of the module folder. Calibrate it against past papers: what did they
actually ask the student to prove, and how long were those proofs? Anything the notes mark non-examinable is Tier
C. End with "to confirm with the lecturer". It's a draft, and the student should ask.

## 3. Build and check
Run `build_obsidian.py`, plus `build_anki.py` if the student chose Anki too. If a browser tool is available, it's worth
spot-checking the maths: load MathJax on a page of the rendered fields and look for `mjx-merror` elements.
The script's checks catch structural problems, but not an unknown LaTeX command.

## 4. Record it
Add to MODULE.md (create `## Revision` above `## Google files` or at the end if missing):
```
## Revision
- **Flashcards:** [cards.md](flashcards/cards.md) is the source. Rebuild with the create-flashcards skill.
  Obsidian: [flashcards/obsidian/](flashcards/obsidian), one note per chapter (tag `#flashcards/<CODE>/…`)
  <and, if chosen, Anki: import flashcards/<CODE>.apkg>
- **<Label> tiers:** [<label>-tiers.md](<label>-tiers.md): reproduce (A), reconstruct (B), statement only (C). To confirm with the lecturer.
```
Then add a dated `## Log` line with the number of notes and chapters covered.

## 5. Updating an existing deck
- **"Add cards for week 3 / chapter 4":** read the new material and add cards **only in that section**. Update
  the tiers page for any new proofs, then rebuild.
- **Never rename a `###` title.** Titles become the Anki card IDs, so renaming one creates a duplicate card and
  loses its review history. Edit the text under a title freely.
- **Anki:** the student re-imports the `.apkg`. Existing cards update in place and keep their history.
- **Obsidian:** the plugin stores review history inside the chapter notes. For a note that already has history,
  the builder **only appends new cards**. To change a card that's already been reviewed, edit it in both
  `cards.md` and the chapter note. `--force` rewrites everything and wipes the history, so only use it if the
  student asks.
- **Switching Anki ↔ Obsidian:** build the other format from the same `cards.md`. Ask before deleting the old
  files.

## 6. Concept notes (offer once per module)
Concept notes make Obsidian's graph show how ideas connect within and **across** modules: one note per theorem,
method or proof technique in `concepts/`, linked to where it appears. After building a module's cards, offer them
("want concept notes so the graph links this module's ideas to your other modules?"). If yes, or if the student
asks directly, follow [reference/concept-note.md](reference/concept-note.md):
1. List the module's 10–20 main concepts from the cards and the tiers page.
2. Read the existing `concepts/` notes first. Extend a matching note instead of creating a duplicate.
3. Write or extend each note, with links to the chapter notes (or lecture notes), the tiers page and 2–5 related
   concepts. Check that every link resolves.
4. Add a Log line to MODULE.md. When cards are added later ("add cards for week 5"), add or extend the concepts
   they introduce as well.

Then suggest opening one note with the **local graph** (right sidebar, set up by `setup-obsidian`).

## 7. Tell the student
Keep it short: what was built (notes per chapter, card types), how to open it, and how to study:
- In Obsidian, review from the **Flashcards** button in the left sidebar (or run *Spaced Repetition: Sync* if
  it's new). If they chose Anki: File → Import the `.apkg`, and turn on **FSRS** in the deck options.
- **Only study the chapters that have been lectured** (pick the chapter's subdeck).
- About **10 minutes a day** beats cramming. In Anki, set 10–15 new cards a day.
- **Once a week, write out two or three Tier A proofs on paper** and check them against the notes, because that's the
  exam format. Flipping cards isn't the same as writing.
- Ask the lecturer which proofs are examinable, then update the tiers page.

## Rules
- Course materials are the university's copyright. `cards.md` and the decks stay in the module folder, which is
  git-ignored, and `concepts/` is git-ignored too. Never commit or share them.
- Flashcards made from the student's own lecture notes are fine for academic integrity. If a card comes from a
  past paper, say so in the card (`(2025 exam)`) so the student knows it's exam-style.
