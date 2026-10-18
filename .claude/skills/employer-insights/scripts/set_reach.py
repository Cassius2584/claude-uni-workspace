#!/usr/bin/env python3
"""Set `reach` on role notes and link them to an employer-insights company note.

Run from the vault root (the folder that contains careers/):

    python3 set_reach.py <company-slug> "<Company>" <role-id>=<Reach>:<n> [...]

<Reach> is Realistic, Stretch, "Long shot" or Unclear. <n> is the sample size,
or "public" when the rating came from public sources only.

For each careers/roles/<role-id>.md it:
- sets the `reach` property (added after `tier`, or at the end of the properties),
- adds or replaces the line "**Employer insights:** [<Company>](../companies/<slug>.md) · reach <Reach>"
  after the *What they look for* paragraph (or before ## Prep),
- appends a dated line to the note's Log.
"""
import datetime
import re
import sys
from pathlib import Path

REACH = {"Realistic", "Stretch", "Long shot", "Unclear"}


def update(path: Path, slug: str, label: str, rating: str, n: str, today: str) -> None:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise SystemExit(f"{path}: no properties block")
    head, body = text[4:].split("\n---\n", 1)

    if re.search(r"^reach:", head, re.M):
        head = re.sub(r"^reach:.*$", f"reach: {rating}", head, flags=re.M)
    elif re.search(r"^tier:", head, re.M):
        head = re.sub(r"^(tier:.*)$", rf"\1\nreach: {rating}", head, count=1, flags=re.M)
    else:
        head = head + f"\nreach: {rating}"

    lines = [l for l in body.split("\n") if not l.startswith("**Employer insights:**")]
    idx = next((i for i, l in enumerate(lines) if l.startswith("**What they look for")), None)
    if idx is not None:
        j = idx + 1
        while j < len(lines) and lines[j].strip() and not lines[j].startswith(("**", "#")):
            j += 1
    else:
        j = next((i for i, l in enumerate(lines) if l.startswith("## Prep")), len(lines))
        while j > 0 and not lines[j - 1].strip():
            j -= 1
    lines.insert(j, f"**Employer insights:** [{label}](../companies/{slug}.md) · reach {rating}")

    basis = "public sources" if n == "public" else f"sample n={n}"
    body = "\n".join(lines).rstrip("\n") + f"\n- {today}: Employer insights run: reach {rating} ({basis}).\n"
    path.write_text("---\n" + head + "\n---\n" + body)


def main() -> None:
    if len(sys.argv) < 4:
        raise SystemExit(__doc__)
    slug, label = sys.argv[1], sys.argv[2]
    today = datetime.date.today()
    today = f"{today.day} {today.strftime('%b %Y')}"
    roles = Path("careers/roles")
    if not roles.is_dir():
        raise SystemExit("Run from the vault root (no careers/roles here).")
    for arg in sys.argv[3:]:
        rid, _, rest = arg.partition("=")
        rating, _, n = rest.rpartition(":")
        if rating not in REACH or not n:
            raise SystemExit(f"Bad argument {arg!r}: expected <role-id>=<Reach>:<n>")
        path = roles / f"{rid}.md"
        if not path.exists():
            raise SystemExit(f"No role note {path}")
        update(path, slug, label, rating, n, today)
        print(f"{rid}: reach {rating}")


if __name__ == "__main__":
    main()
