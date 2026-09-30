"""Build an Anki deck (.apkg) from a module's flashcards/cards.md.

Usage:  python3 build_anki.py <module-folder> [--out DIR]
Needs:  pip install genanki

Writes <module>/flashcards/<CODE>.apkg (or into --out). Import it in Anki with File → Import.
Card GUIDs come from the ### titles, so re-importing updates cards in place and keeps review history.
"""

import hashlib
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from cards import load, section_tag  # noqa: E402

try:
    import genanki
except ImportError:
    sys.exit("genanki isn't installed. Run: python3 -m pip install --user genanki")


def stable_id(name: str) -> int:
    return int(hashlib.sha1(name.encode()).hexdigest()[:8], 16) + (1 << 30)


CSS = """
.card { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 20px;
  line-height: 1.5; text-align: left; color: #1f2328; background: #fbfaf7; padding: 8px 4px; }
.nightMode.card, .night_mode .card { color: #e6e6e6; background: #1e1f22; }
.kind { display: inline-block; font-size: 12px; font-weight: 600; letter-spacing: .06em;
  text-transform: uppercase; color: #6b4fbb; border: 1px solid #cbbef0; border-radius: 999px;
  padding: 1px 10px; margin-bottom: 14px; }
.tierA { color: #b42318; border-color: #f4b4ae; }
.tierB { color: #b25e09; border-color: #f5cf9b; }
.nightMode .kind { color: #b9a6f5; border-color: #54468a; }
.nightMode .tierA { color: #ff9c92; border-color: #7a2e27; }
.nightMode .tierB { color: #ffc27a; border-color: #7a4d14; }
hr#answer { border: none; border-top: 1px solid #d8d4cc; margin: 18px 0; }
.nightMode hr#answer { border-top-color: #3a3b3f; }
.key { background: #f1ecff; border-left: 3px solid #6b4fbb; padding: 8px 12px; margin-bottom: 12px;
  border-radius: 4px; }
.nightMode .key { background: #2a2540; }
.extra { font-size: 16px; color: #57606a; margin-top: 12px; }
.nightMode .extra { color: #a8adb4; }
.ref { font-size: 13px; color: #8c959f; margin-top: 16px; }
.cloze { font-weight: 600; color: #6b4fbb; }
.nightMode .cloze { color: #b9a6f5; }
"""


def models(code: str):
    basic = genanki.Model(
        stable_id(f"{code} basic model v1"), f"{code} Basic",
        fields=[{"name": n} for n in ["Title", "Front", "Back", "Key", "Extra", "Kind", "KindClass", "Ref"]],
        templates=[{
            "name": "Card 1",
            "qfmt": '<div class="kind {{KindClass}}">{{Kind}}</div><div>{{Front}}</div>',
            "afmt": '{{FrontSide}}<hr id="answer">'
                    '{{#Key}}<div class="key"><b>Key idea:</b> {{Key}}</div>{{/Key}}'
                    '<div>{{Back}}</div>'
                    '{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}'
                    '<div class="ref">{{Title}}{{#Ref}} · {{Ref}}{{/Ref}}</div>',
        }],
        css=CSS,
    )
    cloze = genanki.Model(
        stable_id(f"{code} cloze model v1"), f"{code} Cloze", model_type=genanki.Model.CLOZE,
        fields=[{"name": n} for n in ["Text", "Extra", "Title", "Ref"]],
        templates=[{
            "name": "Cloze",
            "qfmt": '<div class="kind">Statement</div><div>{{cloze:Text}}</div>',
            "afmt": '<div class="kind">Statement</div><div>{{cloze:Text}}</div>'
                    '{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}'
                    '<div class="ref">{{Title}}{{#Ref}} · {{Ref}}{{/Ref}}</div>',
        }],
        css=CSS,
    )
    return basic, cloze


def md_to_html(text: str) -> str:
    """Escape HTML, turn $..$ / $$..$$ into MathJax delimiters, **bold** into <b>, "- " lines into bullets."""
    out, pos = [], 0
    for m in re.finditer(r"\$\$(.+?)\$\$|\$(.+?)\$", text, flags=re.S):
        out.append(_text(text[pos:m.start()]))
        if m.group(1) is not None:
            out.append(r"\[" + _math(m.group(1)) + r"\]")
        else:
            out.append(r"\(" + _math(m.group(2)) + r"\)")
        pos = m.end()
    out.append(_text(text[pos:]))
    return "".join(out).replace("\n", "<br>")


def _text(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(^|\n)- ", r"\1• ", s)
    return s


def _math(s: str) -> str:
    # "}}" inside maths would close an Anki cloze early; a space is harmless in LaTeX.
    while "}}" in s:
        s = s.replace("}}", "} }")
    return html.escape(s, quote=False)


def build(module_dir: Path, out_dir: Path):
    meta, cards = load(module_dir)
    code, label = meta["code"], meta["label"]
    root = f"{code} {meta['title']}"
    basic, cloze = models(code)

    decks, counts = {}, {"Q&A": 0, "cloze": 0, label.lower(): 0}
    for c in cards:
        deck_name = f"{root}::{c['Chapter']}"
        deck = decks.setdefault(deck_name, genanki.Deck(stable_id(deck_name), deck_name))
        tags = [code, section_tag(c["Chapter"])]
        guid = genanki.guid_for(code, c["Title"])
        ref = html.escape(c.get("Ref", ""), quote=False)

        if "C" in c:
            note = genanki.Note(model=cloze, guid=guid, tags=tags + ["statement"], fields=[
                md_to_html(c["C"]), md_to_html(c.get("X", "")), html.escape(c["Title"]), ref])
            counts["cloze"] += 1
        else:
            tier = c.get("Tier", "").strip()
            if tier:
                kind, kind_class = f"{label} · Tier {tier}", f"tier{tier}"
                tags += [label.lower().replace(" ", "-"), f"tier-{tier}"]
                counts[label.lower()] += 1
            else:
                kind, kind_class = c.get("Kind", "Definition").strip(), ""
                tags.append(kind.lower().replace(" ", "-"))
                counts["Q&A"] += 1
            note = genanki.Note(model=basic, guid=guid, tags=tags, fields=[
                html.escape(c["Title"]), md_to_html(c["Q"]), md_to_html(c["A"]),
                md_to_html(c.get("K", "")), md_to_html(c.get("X", "")), kind, kind_class, ref])
        deck.add_note(note)

    out = out_dir / f"{code}.apkg"
    genanki.Package(list(decks.values())).write_to_file(out)
    summary = ", ".join(f"{n} {k}" for k, n in counts.items())
    print(f"Wrote {out}: {len(cards)} notes ({summary}) in {len(decks)} subdecks.")
    for name, d in decks.items():
        print(f"  {name.split('::')[1]}: {len(d.notes)}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    module = Path(args[0]).expanduser().resolve()
    out = Path(args[args.index("--out") + 1]).expanduser() if "--out" in args else module / "flashcards"
    out.mkdir(parents=True, exist_ok=True)
    build(module, out)
