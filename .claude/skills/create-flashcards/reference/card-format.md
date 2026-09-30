# cards.md format and writing rules

## File layout
```
---
kind: flashcards
code: MA32064
title: Number Theory and Cryptography
label: Proof
---

# MA32064 flashcards (source)

Anything before the first `## ` heading is ignored: use it for a short note on sources and how to rebuild.

## Ch1 Prime numbers

### Euclid's Theorem
Q: State **Euclid's Theorem** (Theorem 1.2).
A: The number of primes is infinite.
Ref: Thm 1.2
```

- `## <Section>`: one subdeck per section. Start it with a short token (`Ch1`, `Week3`), which becomes the Anki tag.
- `### <Title>`: one card per title. Titles must be **unique** and **never renamed** once the student is studying,
  because they are the card IDs. Anki shows the title on the back and Obsidian doesn't show it at all, so a title
  may name the answer.
- Fields start a line as `Key: value`. A line without a key continues the previous field. Blank lines are ignored.

| Field | Meaning |
|---|---|
| `Q:` / `A:` | Front and back of a normal card |
| `C:` | Cloze text instead of Q/A: `{{c1::hidden part}}`. The same number hides together, and different numbers make separate cards |
| `K:` | Key idea of a proof, in one sentence (shown first on the back) |
| `X:` | Extra shown on the back: consequences, examples, warnings, typo notes |
| `Tier:` | `A` or `B` marks a proof card (labelled with the frontmatter `label`). Tier C results get no proof card |
| `Kind:` | Label for a Q/A card: Definition (default), Example, Name it, Exam-style, Method, Interpret … |
| `Ref:` | Where it's from: `Thm 2.13`, `§4.5`, `2025 exam Q2(c)` |

Formatting: maths in `$…$` (or `$$…$$` for display). Use `**bold**`, and `- ` at the start of a line for bullets.
Don't write `::` or a line that is only `?` (they're Obsidian card separators), and don't use `\(`…`\)`.

## Card types (one of each, as a model)

**Definition.** Word for word from the notes, with every hypothesis:
```
### Primitive root
Q: Define a **primitive root modulo $m$** (Definition 4.23).
A: Let $a,m\in\mathbb{N}$ with $m\geqslant2$ and $\gcd(a,m)=1$. Then $a$ is a primitive root modulo $m$ if $(\mathbb{Z}/m\mathbb{Z})^*$ is cyclic and $[a]$ is a generator.
X: Equivalently, $[a]$ has order $\phi(m)$.
Ref: Def 4.23
```

**Statement (cloze).** Hide what matters: hypotheses, the conclusion, the key quantity. 1–4 deletions:
```
### Euler's Theorem
C: **Corollary 4.18 (Euler's Theorem).** If {{c1::$\gcd(a,m)=1$}}, then {{c2::$a^{\phi(m)}\equiv1\pmod m$}}.
Ref: Cor 4.18
```

**Name it.** For every named result, the reverse direction:
```
### Name it: Euler's criterion
Q: **Name the result:** $\left(\frac{a}{p}\right)\equiv a^{(p-1)/2}\pmod p$.
A: Euler's criterion (Proposition 6.4).
Kind: Name it
```

**Worked example.** Take it from the notes or a problem sheet, and recompute the arithmetic before writing it down:
```
### Example: 9x = 6 mod 15
Q: Solve $9x\equiv6\pmod{15}$.
A: $\gcd(9,15)=3$ divides $6$, so there are $3$ solutions. Cancel $3$: $3x\equiv2\pmod5$, so $x\equiv4\pmod5$. Solutions: $x\equiv4,9,14\pmod{15}$.
Kind: Example
```

**Proof (Tier A or B).** The front asks for the proof. `K:` is the one-sentence idea, and `A:` is a 3–6 sentence outline
with the steps an examiner would look for:
```
### Proof: Euler's Theorem
Q: Prove Euler's Theorem.
K: Lagrange-type argument in the group $(\mathbb{Z}/m\mathbb{Z})^*$, which has order $\phi(m)$.
A: $[a]$ lies in $(\mathbb{Z}/m\mathbb{Z})^*$, a finite abelian group of order $\phi(m)$. By Prop 4.12, $g^{|G|}=1$ for every $g$, so $a^{\phi(m)}\equiv1\pmod m$.
Tier: A
Ref: Cor 4.18
```

**Past exam part.** Write it as a Q/A or proof card with the year in the question: `Q: (2025 exam) Prove that …`.

## Writing rules
- **One idea per card.** Split a definition with several parts only if the parts are separate facts.
- **Exact wording for definitions and statements.** The point is word-for-word recall, so don't paraphrase the notes.
- **Every theorem gets a cloze, and every Tier A/B result also gets a proof card.** Tier C results get the cloze only.
- **Check every number** in examples (recompute them). A wrong card is worse than no card.
- **Mark the notes' mistakes:** correct them on the card and say so in `X:`.
- Roughly 10–25 notes per chapter for a maths module. Fewer, better cards beat exhaustive ones.
