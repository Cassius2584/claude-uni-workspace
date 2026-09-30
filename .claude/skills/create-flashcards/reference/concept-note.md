# Concept note format

One note per idea in `concepts/<Name>.md` at the workspace root, named in plain words with spaces
(`Chinese Remainder Theorem.md`, `Counting two ways.md`), so the graph labels read well. Concepts are shared across
modules: a note exists once and lists every module it appears in.

```markdown
---
kind: concept
modules: [MA32064, MA32054]
---

# Counting two ways

One or two sentences: the statement or idea, in the notes' own notation.

## Where it comes up
- **MA32064** [Ch2 Arithmetic functions](<../projects/MA32064-.../flashcards/obsidian/Ch2 Arithmetic functions.md>): what uses it, with result numbers (Prop 2.7)
- **MA32054** [Week 3 degree sequences](../projects/MA32054-.../lectures/week-03-degree-sequences.md): the handshake lemma

Proof tiers for these results: [proof tiers](../projects/MA32064-.../proof-tiers.md).

## Connected ideas
[Euler's phi function](<Euler's phi function.md>) · [Primitive roots](<Primitive roots.md>)
```

Rules:
- **Links:** relative Markdown links. Wrap paths containing spaces in `<…>`. Link to the most specific note that
  exists: a lecture note (`lectures/week-NN-….md`) first, else the flashcard chapter note, else MODULE.md.
- **What counts as a concept:** a named theorem or definition used in more than one place, a method (an
  algorithm, a test, an estimator), or a proof technique. Aim for 10–20 per module. Skip one-off lemmas: they
  belong on the flashcards.
- **Connected ideas:** 2–5 links to other concept notes, where one builds on, uses or generalises the other.
  Every link must point to a note that exists.
- **Cross-module links are the point.** When a module's concept already has a note (from another module), add a
  `Where it comes up` line and the module code to `modules`. Don't create a second note. Only link modules where
  the notes genuinely use the idea, never by name alone.
- Statements come from the module's notes, like the cards. Never invent a result number.
