"""Write Obsidian Spaced Repetition plugin notes from a module's flashcards/cards.md.

Usage:  python3 build_obsidian.py <module-folder> [--out DIR] [--force]

Writes one note per ## section to <module>/flashcards/obsidian/ (or --out), tagged
#flashcards/<CODE>/<Section>, so the plugin shows one subdeck per chapter.

The plugin keeps review history as <!--SR:...--> comments inside those notes. For a note that
already has history, this only appends cards that aren't in it yet and leaves reviewed cards
alone. Edits to cards that are already there must be made in both files. --force rewrites
everything and throws the history away.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from cards import load  # noqa: E402


def clean(s: str) -> str:
    # The plugin turns **bold** into clozes by default, so drop the bold markers.
    s = s.replace("**", "")
    if "::" in s or re.search(r"^\?\??$", s, flags=re.M):
        sys.exit(f"Text clashes with the plugin's card separators (:: or a lone ?): {s[:60]}")
    return s


def card_block(c: dict, label: str) -> str:
    if "C" in c:
        # Anki cloze {{cN::text}} becomes a highlight cloze ==text==.
        return clean(re.sub(r"\{\{c\d+::(.+?)\}\}", r"==\1==", c["C"]))
    front = clean(c["Q"])
    if c.get("Tier"):
        front += f"\n*({label} · Tier {c['Tier']})*"
    back = []
    if c.get("K"):
        back.append("Key idea: " + clean(c["K"]))
    back.append(clean(c["A"]))
    if c.get("X"):
        back.append("Note: " + clean(c["X"]).replace("\n", " "))
    return "\n".join([front, "?", "\n".join(back)])


def build(module_dir: Path, out_dir: Path, force: bool):
    meta, cards = load(module_dir)
    code, label = meta["code"], meta["label"]
    sections = {}
    for c in cards:
        sections.setdefault(c["Chapter"], []).append(card_block(c, label))

    out_dir.mkdir(parents=True, exist_ok=True)
    for section, blocks in sections.items():
        path = out_dir / (section.replace("/", "-") + ".md")
        tag = f"#flashcards/{code}/" + re.sub(r"[^\w]+", "-", section).strip("-")
        existing = path.read_text(encoding="utf-8") if path.exists() else ""

        if "<!--SR:" in existing and not force:
            # Match on each card's first line, so reviewed cards (and their history) stay untouched.
            new = [b for b in blocks if b.splitlines()[0] not in existing]
            if new:
                path.write_text(existing.rstrip("\n") + "\n\n" + "\n\n".join(new) + "\n", encoding="utf-8")
            print(f"{path.name}: has review history, appended {len(new)} new card(s)")
            continue

        head = [tag, "", f"# {code} · {section}", "",
                "Generated from [cards.md](../cards.md) by the create-flashcards skill. "
                "Review from the Flashcards button in Obsidian's left sidebar."]
        path.write_text("\n\n".join(["\n".join(head)] + blocks) + "\n", encoding="utf-8")
        print(f"Wrote {path.name} ({len(blocks)} cards, {tag})")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    module = Path(args[0]).expanduser().resolve()
    out = Path(args[args.index("--out") + 1]).expanduser() if "--out" in args else module / "flashcards" / "obsidian"
    build(module, out, "--force" in args)
