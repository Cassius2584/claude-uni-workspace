"""Shared parser and checks for a module's flashcards/cards.md.

cards.md format (full guide: ../reference/card-format.md):

    ---
    kind: flashcards
    code: MA32064
    title: Number Theory and Cryptography
    label: Proof            # what Tier cards are called: Proof, Derivation, Method, Argument …
    ---
    ## Ch1 Prime numbers    ← one subdeck per ## section
    ### Euclid's Theorem    ← one card per ### title (unique; renaming loses review history)
    Q: …  A: …  C: …{{c1::…}}…  K: …  X: …  Tier: A|B  Kind: …  Ref: …

If the frontmatter is missing, code and title come from ../MODULE.md and label is "Proof".
"""

import re
import sys
from pathlib import Path

FIELD_KEYS = {"Q", "A", "C", "K", "X", "Tier", "Kind", "Ref"}


def read_frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not m:
        return {}
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        v = v.split(" #")[0].strip().strip('"').strip("'")
        if k.strip() and v:
            meta[k.strip()] = v
    return meta


def load(module_dir: Path):
    """Return (meta, cards) for a module folder, exiting with a clear message on any problem."""
    src = module_dir / "flashcards" / "cards.md"
    if not src.exists():
        sys.exit(f"No flashcards/cards.md in {module_dir}")
    text = src.read_text(encoding="utf-8")
    meta = read_frontmatter(text)
    module_md = module_dir / "MODULE.md"
    if module_md.exists():
        mod = read_frontmatter(module_md.read_text(encoding="utf-8"))
        meta.setdefault("code", mod.get("code", ""))
        meta.setdefault("title", mod.get("title", ""))
    meta.setdefault("label", "Proof")
    if not meta.get("code") or not meta.get("title"):
        sys.exit("Set code and title in cards.md frontmatter (or MODULE.md properties).")
    cards = parse(text)
    check(cards)
    return meta, cards


def parse(text: str) -> list:
    cards, section, card, last = [], None, None, None
    body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
    for raw in body.splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            section, card, last = line[3:].strip(), None, None
            continue
        if section is None:
            continue  # intro text before the first section
        if line.startswith("### "):
            card = {"Title": line[4:].strip(), "Chapter": section}
            cards.append(card)
            last = None
            continue
        if card is None or not line.strip():
            continue
        m = re.match(r"^(\w+):\s?(.*)$", line)
        if m and m.group(1) in FIELD_KEYS:
            last = m.group(1)
            card[last] = m.group(2)
        elif last:
            card[last] += "\n" + line
        else:
            sys.exit(f"Stray line in card '{card['Title']}': {line}")
    return cards


def math_spans(s: str) -> list:
    return [a or b for a, b in re.findall(r"\$\$(.+?)\$\$|\$(.+?)\$", s, flags=re.S)]


def check(cards: list) -> None:
    """Catch the mistakes that break rendering or scheduling, before anything is built."""
    problems = []
    titles = [c["Title"] for c in cards]
    for t in sorted({t for t in titles if titles.count(t) > 1}):
        problems.append(f"duplicate title '{t}'")
    for c in cards:
        name = c["Title"]
        if "C" in c:
            if not re.search(r"\{\{c\d+::", c["C"]):
                problems.append(f"'{name}': C: has no {{{{c1::…}}}} deletion")
        elif "Q" not in c or "A" not in c:
            problems.append(f"'{name}': needs Q: and A: (or C:)")
        if c.get("Tier", "").strip() not in ("", "A", "B"):
            problems.append(f"'{name}': Tier must be A or B (Tier C results get no proof card)")
        for key in ("Q", "A", "C", "K", "X"):
            s = c.get(key, "")
            if s.replace("\\$", "").count("$") % 2:
                problems.append(f"'{name}' {key}: odd number of $")
            for m in math_spans(s):
                if m.count("{") != m.count("}"):
                    problems.append(f"'{name}' {key}: unbalanced braces in ${m[:40]}$")
                if len(re.findall(r"\\left\b", m)) != len(re.findall(r"\\right\b", m)):
                    problems.append(f"'{name}' {key}: \\left/\\right mismatch in ${m[:40]}$")
    if problems:
        sys.exit("cards.md problems:\n  " + "\n  ".join(problems))


def section_tag(section: str) -> str:
    """'Ch1 Prime numbers' -> 'ch1', 'Week 3 …' -> 'week'."""
    return re.sub(r"\W", "", section.split()[0]).lower()
