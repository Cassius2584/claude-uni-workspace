#!/usr/bin/env python3
"""Install the workspace's Obsidian plugins and theme from Obsidian's community directory.

Two steps, so the student can approve the whole batch at once:

    python3 install_plugins.py plan     # lists each item: author, repo, version, files and sizes
    python3 install_plugins.py install  # downloads exactly that list, then enables it

Run from the workspace (vault) root, or pass --vault PATH. Only items listed in Obsidian's own
directory (obsidianmd/obsidian-releases) are installed, from their latest GitHub release. The
bundled local plugin (assets/plugins/) is copied, not downloaded. Existing files are backed up to
<file>.bak. Restricted mode is untouched: the student turns on community plugins in Obsidian.
"""
import argparse
import json
import shutil
import sys
import urllib.request
from pathlib import Path

PLUGINS = [
    ("obsidian-spaced-repetition", "flashcards"),
    ("full-calendar-remastered", "timetable, HOME's week agenda"),
    ("obsidian-style-settings", "applies the theme preset"),
    ("homepage", "opens HOME on startup"),
    ("obsidian-advanced-uri", "HOME's Open calendar and Flashcards buttons"),
]
THEME = ("AnuPpuccin", "the Catppuccin look")
REGISTRY = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/"
ASSETS = Path(__file__).resolve().parent.parent / "assets" / "plugins"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "claude-uni-workspace"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def fetch_json(url):
    return json.loads(fetch(url))


def kb(n):
    return f"{n / 1024:.0f} KB" if n >= 1024 else f"{n} B"


def resolve():
    """Return the list of items to install, each with its download files."""
    plugins = {p["id"]: p for p in fetch_json(REGISTRY + "community-plugins.json")}
    themes = {t["name"]: t for t in fetch_json(REGISTRY + "community-css-themes.json")}
    items = []
    for pid, why in PLUGINS:
        if pid not in plugins:
            sys.exit(f"{pid} isn't in Obsidian's community directory; stopping.")
        entry = plugins[pid]
        rel = fetch_json(f"https://api.github.com/repos/{entry['repo']}/releases/latest")
        assets = {a["name"]: a for a in rel["assets"]}
        if "main.js" not in assets or "manifest.json" not in assets:
            sys.exit(f"{pid}: latest release has no main.js/manifest.json; stopping.")
        files = [(n, assets[n]["browser_download_url"], assets[n]["size"])
                 for n in ("main.js", "manifest.json", "styles.css") if n in assets]
        items.append({"kind": "plugin", "id": pid, "name": entry["name"], "author": entry["author"],
                      "repo": entry["repo"], "version": rel["tag_name"], "why": why, "files": files})
    name, why = THEME
    entry = themes[name]
    raw = f"https://raw.githubusercontent.com/{entry['repo']}/HEAD/"
    files = []
    for n in ("manifest.json", "theme.css"):
        files.append((n, raw + n, len(fetch(raw + n))))
    version = json.loads(fetch(raw + "manifest.json")).get("version", "?")
    items.append({"kind": "theme", "id": name, "name": name, "author": entry["author"],
                  "repo": entry["repo"], "version": version, "why": why, "files": files})
    return items


def installed_version(vault, item):
    sub = "plugins" if item["kind"] == "plugin" else "themes"
    m = vault / ".obsidian" / sub / item["id"] / "manifest.json"
    return json.loads(m.read_text()).get("version") if m.exists() else None


def plan(vault, items):
    total = 0
    print("| Item | Author | Source | Version | Files | For |")
    print("|---|---|---|---|---|---|")
    for it in items:
        size = sum(s for _, _, s in it["files"])
        total += size
        have = installed_version(vault, it)
        ver = it["version"] + (f" (have {have})" if have else "")
        files = ", ".join(f"{n} ({kb(s)})" for n, _, s in it["files"])
        print(f"| {it['name']}{' (theme)' if it['kind'] == 'theme' else ''} | {it['author']} | "
              f"github.com/{it['repo']} | {ver} | {files} | {it['why']} |")
    for local in sorted(ASSETS.iterdir()) if ASSETS.exists() else []:
        m = json.loads((local / "manifest.json").read_text())
        print(f"| {m['name']} | this workspace | bundled, no download | {m['version']} | "
              f"{', '.join(p.name for p in sorted(local.iterdir()))} | {m['description']} |")
    print(f"\nDownload total: {kb(total)}")


def backup(path):
    if path.exists():
        shutil.copy2(path, path.with_name(path.name + ".bak"))


def install(vault, items):
    obs = vault / ".obsidian"
    enabled = []
    for it in items:
        sub = "plugins" if it["kind"] == "plugin" else "themes"
        dest = obs / sub / it["id"]
        dest.mkdir(parents=True, exist_ok=True)
        for name, url, _ in it["files"]:
            data = fetch(url)
            if name == "manifest.json" and it["kind"] == "plugin":
                if json.loads(data).get("id") != it["id"]:
                    sys.exit(f"{it['id']}: manifest id doesn't match; stopping.")
            (dest / name).write_bytes(data)
        if it["kind"] == "plugin":
            enabled.append(it["id"])
        print(f"installed {it['name']} {it['version']}")
    for local in sorted(ASSETS.iterdir()) if ASSETS.exists() else []:
        shutil.copytree(local, obs / "plugins" / local.name, dirs_exist_ok=True)
        enabled.append(local.name)
        print(f"copied {local.name} (bundled)")

    cp = obs / "community-plugins.json"
    current = json.loads(cp.read_text()) if cp.exists() else []
    backup(cp)
    cp.write_text(json.dumps(current + [p for p in enabled if p not in current], indent=2))

    ap = obs / "appearance.json"
    appearance = json.loads(ap.read_text()) if ap.exists() else {}
    if not appearance.get("cssTheme"):
        backup(ap)
        appearance["cssTheme"] = THEME[0]
        ap.write_text(json.dumps(appearance, indent=2))
    print("enabled: " + ", ".join(enabled))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", choices=["plan", "install"])
    ap.add_argument("--vault", default=".", help="workspace root (default: current folder)")
    args = ap.parse_args()
    vault = Path(args.vault).expanduser().resolve()
    if not (vault / ".obsidian").is_dir():
        sys.exit(f"{vault} has no .obsidian folder: open it in Obsidian once first.")
    items = resolve()
    plan(vault, items) if args.action == "plan" else install(vault, items)


if __name__ == "__main__":
    main()
