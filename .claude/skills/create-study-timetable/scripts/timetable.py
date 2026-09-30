"""Check a study timetable, write its week summary into TIMETABLE.md, and optionally export an .ics file.

Usage:
  python3 timetable.py <timetable-folder> [--lectures FILE_OR_URL] [--week YYYY-MM-DD] [--ics OUT.ics]

<timetable-folder> holds TIMETABLE.md and blocks/*.md. Each block is a note in the Full Calendar
(Remastered) "Full Note" format, e.g.

  ---
  title: Study - MA32064 - Number theory
  allDay: false
  type: recurring
  daysOfWeek: [M, R]          # U M T W R F S (R = Thursday)
  startTime: "10:00"
  endTime: "11:30"
  startRecur: 2026-09-28
  endRecur: 2026-12-11
  skipDates: [2026-11-02]     # optional (reading week, bank holiday…)
  ---

or a one-off: type: single, date: 2026-11-20 (instead of daysOfWeek/startRecur/endRecur).

--lectures  the university timetable as an .ics file or URL, used only for the clash check. The URL is
            read at run time and never saved anywhere.
--week      the Monday of the week to check and summarise (default: this week, or the first week of term).
--ics       also export all blocks as an .ics file (floating local times, weekly RRULEs) for Apple or
            Google Calendar.
"""

import hashlib
import re
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # Python < 3.9
    ZoneInfo = None

DAY_CODES = ["M", "T", "W", "R", "F", "S", "U"]          # index = date.weekday()
DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
ICS_DAYS = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
START, END = "<!-- week:start -->", "<!-- week:end -->"


# ---------- reading block notes ----------

def parse_frontmatter(text: str) -> dict:
    """Minimal YAML for the keys we use: scalars, [a, b] lists and '- item' block lists."""
    m = re.match(r"^---\n(.*?)\n---", text, flags=re.S)
    if not m:
        return {}
    data, key = {}, None
    for line in m.group(1).splitlines():
        item = re.match(r"^\s+-\s*(.*)$", line)
        if item and key:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(unquote(item.group(1)))
            continue
        kv = re.match(r"^([A-Za-z_]\w*):\s*(.*)$", line)
        if not kv:
            continue
        key, value = kv.group(1), kv.group(2).split(" #")[0].strip()
        if value.startswith("[") and value.endswith("]"):
            data[key] = [unquote(v) for v in value[1:-1].split(",") if v.strip()]
        else:
            data[key] = unquote(value) if value else None
    return data


def unquote(v: str) -> str:
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        return v[1:-1]
    return v


def to_date(v):
    return date.fromisoformat(str(v)[:10]) if v else None


def to_minutes(v) -> int:
    h, m = str(v).split(":")[:2]
    return int(h) * 60 + int(m)


def fmt(minutes: int) -> str:
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def load_blocks(folder: Path):
    blocks, problems = [], []
    files = sorted((folder / "blocks").glob("*.md"))
    if not files:
        sys.exit(f"No block notes in {folder / 'blocks'}")
    for f in files:
        d = parse_frontmatter(f.read_text(encoding="utf-8"))
        name = f.name
        try:
            if not d.get("title"):
                raise ValueError("missing title")
            if str(d.get("allDay", "false")).lower() == "true":
                raise ValueError("allDay blocks aren't supported in a study timetable")
            start, end = to_minutes(d["startTime"]), to_minutes(d["endTime"])
            if end <= start:
                raise ValueError(f"endTime {d['endTime']} is not after startTime {d['startTime']}")
            kind = d.get("type", "single")
            b = {"file": name, "title": d["title"], "start": start, "end": end, "type": kind,
                 "skip": {to_date(x) for x in (d.get("skipDates") or [])}}
            if kind == "recurring":
                days = d.get("daysOfWeek") or []
                bad = [x for x in days if x not in DAY_CODES]
                if not days or bad:
                    raise ValueError(f"daysOfWeek must be a list of U M T W R F S (got {days})")
                b["days"] = [DAY_CODES.index(x) for x in days]
                b["from"], b["until"] = to_date(d.get("startRecur")), to_date(d.get("endRecur"))
            elif kind == "single":
                b["date"] = to_date(d["date"])
            else:
                raise ValueError(f"type must be recurring or single (got {kind})")
            blocks.append(b)
        except (KeyError, ValueError) as e:
            problems.append(f"{name}: {e}")
    if problems:
        sys.exit("Block problems:\n  " + "\n  ".join(problems))
    return blocks


def occurrences(b, monday: date):
    """(date, start, end, title) for block b in the week starting monday."""
    for i in range(7):
        day = monday + timedelta(days=i)
        if b["type"] == "single":
            hit = b["date"] == day
        else:
            hit = (day.weekday() in b["days"] and (not b["from"] or day >= b["from"])
                   and (not b["until"] or day <= b["until"]) and day not in b["skip"])
        if hit:
            yield day, b["start"], b["end"], b["title"]


# ---------- the university timetable (.ics) ----------

def read_ics(source: str) -> str:
    if re.match(r"^(https?|webcal)://", source):
        url = re.sub(r"^webcal://", "https://", source)
        with urllib.request.urlopen(url, timeout=30) as r:
            return r.read().decode("utf-8", errors="replace")
    return Path(source).expanduser().read_text(encoding="utf-8", errors="replace")


def parse_ics_time(prop: str, value: str):
    tzid = re.search(r"TZID=([^;:]+)", prop)
    if re.fullmatch(r"\d{8}", value):
        return None  # all-day event: not a clash
    dt = datetime.strptime(value.rstrip("Z"), "%Y%m%dT%H%M%S")
    if value.endswith("Z"):
        return dt.replace(tzinfo=timezone.utc).astimezone().replace(tzinfo=None)
    if tzid and ZoneInfo:
        try:
            return dt.replace(tzinfo=ZoneInfo(tzid.group(1))).astimezone().replace(tzinfo=None)
        except Exception:
            pass
    return dt  # floating or unknown zone: take as local


def lecture_events(source: str, monday: date):
    text = re.sub(r"\r?\n[ \t]", "", read_ics(source))  # unfold lines
    events, recurring = [], 0
    for block in re.findall(r"BEGIN:VEVENT(.*?)END:VEVENT", text, flags=re.S):
        props = {}
        for line in block.strip().splitlines():
            name, _, value = line.partition(":")
            props.setdefault(name.split(";")[0], (name, value.strip()))
        if "RRULE" in props:
            recurring += 1
        if "DTSTART" not in props or "DTEND" not in props:
            continue
        s, e = parse_ics_time(*props["DTSTART"]), parse_ics_time(*props["DTEND"])
        if not s or not e or not (monday <= s.date() < monday + timedelta(days=7)):
            continue
        title = props.get("SUMMARY", ("", "Timetabled event"))[1].replace("\\,", ",")
        events.append((s.date(), s.hour * 60 + s.minute, e.hour * 60 + e.minute, "Uni - " + title))
    if recurring:
        print(f"Note: {recurring} event(s) in the feed use RRULE; only their listed dates were checked.")
    return events


# ---------- checks and summary ----------

def category(title: str) -> str:
    return title.split(" - ")[0].strip() if " - " in title else "Other"


def module_of(title: str):
    parts = [p.strip() for p in title.split(" - ")]
    return parts[1] if len(parts) >= 3 else None


def clashes(items):
    out = []
    by_day = {}
    for it in items:
        by_day.setdefault(it[0], []).append(it)
    for day, its in sorted(by_day.items()):
        its.sort(key=lambda x: x[1])
        for i, a in enumerate(its):
            for b in its[i + 1:]:
                if b[1] < a[2]:
                    out.append(f"{DAY_NAMES[day.weekday()]} {day:%d %b}: '{a[3]}' {fmt(a[1])}–{fmt(a[2])} "
                               f"overlaps '{b[3]}' {fmt(b[1])}–{fmt(b[2])}")
    return out


def summary(items, monday: date, lectures_checked: bool) -> str:
    cols = {i: [] for i in range(7)}
    for day, s, e, title in sorted(items, key=lambda x: (x[0], x[1])):
        label = title.split(" - ", 1)[1] if " - " in title else title
        cols[day.weekday()].append(f"{fmt(s)}–{fmt(e)} {category(title)}: {label}")
    rows = max((len(v) for v in cols.values()), default=0)
    lines = [f"Week of {monday.day} {monday:%b %Y}" + (" (lectures from the uni timetable included)"
             if lectures_checked else "") + ".", "",
             "| " + " | ".join(DAY_NAMES) + " |", "|" + "---|" * 7]
    for r in range(rows):
        lines.append("| " + " | ".join(cols[i][r] if r < len(cols[i]) else "" for i in range(7)) + " |")

    hours_cat, hours_mod = {}, {}
    for _, s, e, title in items:
        h = (e - s) / 60
        hours_cat[category(title)] = hours_cat.get(category(title), 0) + h
        mod = module_of(title)
        if mod and category(title) != "Uni":
            hours_mod[mod] = hours_mod.get(mod, 0) + h
    lines += ["", "| Category | Hours this week |", "|---|---|"]
    lines += [f"| {c} | {round(h, 2):g} |" for c, h in sorted(hours_cat.items(), key=lambda x: -x[1])]
    if hours_mod:
        lines += ["", "| Module (independent study) | Hours this week |", "|---|---|"]
        lines += [f"| {m} | {round(h, 2):g} |" for m, h in sorted(hours_mod.items(), key=lambda x: -x[1])]
    return "\n".join(lines)


# ---------- .ics export ----------

def ics_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,")


def fold(line: str) -> str:
    out, b = [], line.encode("utf-8")
    while len(b) > 75:
        cut = 75
        while (b[cut] & 0xC0) == 0x80:  # don't split a UTF-8 character
            cut -= 1
        out.append(b[:cut].decode("utf-8"))
        b = b" " + b[cut:]
    out.append(b.decode("utf-8"))
    return "\r\n".join(out)


def export_ics(blocks, path: Path):
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//uni-workspace//create-study-timetable//EN",
             "CALSCALE:GREGORIAN", "X-WR-CALNAME:Study timetable"]
    for b in blocks:
        if b["type"] == "single":
            first = b["date"]
        else:
            first = b["from"] or date.today()
            while first.weekday() not in b["days"]:
                first += timedelta(days=1)
        t = lambda d, m: f"{d:%Y%m%d}T{m // 60:02d}{m % 60:02d}00"  # floating local time
        lines += ["BEGIN:VEVENT", f"UID:{hashlib.sha1(b['file'].encode()).hexdigest()[:16]}@uni-workspace",
                  f"DTSTAMP:{stamp}", f"DTSTART:{t(first, b['start'])}", f"DTEND:{t(first, b['end'])}",
                  f"SUMMARY:{ics_escape(b['title'])}"]
        if b["type"] == "recurring":
            rule = "FREQ=WEEKLY;BYDAY=" + ",".join(ICS_DAYS[d] for d in sorted(b["days"]))
            if b["until"]:
                rule += f";UNTIL={b['until']:%Y%m%d}T235959"
            lines.append("RRULE:" + rule)
            lines += [f"EXDATE:{t(d, b['start'])}" for d in sorted(x for x in b["skip"] if x)]
        lines.append("END:VEVENT")
    lines.append("END:VCALENDAR")
    path.write_text("\r\n".join(fold(l) for l in lines) + "\r\n", encoding="utf-8")
    print(f"Exported {len(blocks)} blocks to {path}")


# ---------- main ----------

def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    folder = Path(args[0]).expanduser()
    opt = lambda name: args[args.index(name) + 1] if name in args else None
    blocks = load_blocks(folder)

    if opt("--week"):
        monday = date.fromisoformat(opt("--week"))
    else:
        starts = [b["from"] for b in blocks if b["type"] == "recurring" and b["from"]]
        base = max(date.today(), min(starts)) if starts else date.today()
        monday = base - timedelta(days=base.weekday())
    if monday.weekday() != 0:
        sys.exit("--week must be a Monday")

    items = [o for b in blocks for o in occurrences(b, monday)]
    lectures = lecture_events(opt("--lectures"), monday) if opt("--lectures") else []
    found = clashes(items + lectures)
    print(f"{len(blocks)} blocks, {len(items)} sessions in the week of {monday:%d %b %Y}"
          + (f", plus {len(lectures)} timetabled events" if opt("--lectures") else "") + ".")
    print("Clashes:\n  " + "\n  ".join(found) if found else "No clashes.")

    text = summary(items + lectures, monday, bool(opt("--lectures")))
    tt = folder / "TIMETABLE.md"
    if tt.exists() and START in tt.read_text(encoding="utf-8"):
        s = tt.read_text(encoding="utf-8")
        s = s[:s.index(START) + len(START)] + "\n" + text + "\n" + s[s.index(END):]
        tt.write_text(s, encoding="utf-8")
        print(f"Updated the week summary in {tt}")
    else:
        print("\n" + text)

    if opt("--ics"):
        export_ics(blocks, Path(opt("--ics")).expanduser())
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
