---
name: setup-obsidian
description: Set up Obsidian for this workspace so it looks and works as intended. Walks the student through installing the community plugins (Spaced Repetition, Full Calendar Remastered, Style Settings, Homepage) and the AnuPpuccin theme, then applies the dashboard styling, theme preset, calendar settings and a colour-coded graph (plus a local-graph sidebar) from this skill's assets, and makes HOME the first page. Use when the student says "set up Obsidian", "make Obsidian look nice", "style my vault", after setup-year, when HOME looks like plain callouts (pencil icons, no gradient header), or when they ask to make the graph view nicer or more useful.
---

# Set up Obsidian

The workspace is an Obsidian vault. This skill gets it from "plain Markdown" to the intended look: a card-style
HOME dashboard, the Catppuccin-based **AnuPpuccin** theme, and the plugins the other skills rely on.

Assets (in this skill's folder):
- `assets/dashboard.css`: the card layout for dashboard pages (HOME, DEADLINES, TASKS, the tracker, module pages,
  the timetable). It only affects notes with `cssclasses: dashboard`. It uses the
  theme's Catppuccin colours and falls back to fixed colours in any other theme.
- `assets/homepage.json`: Homepage plugin preset (open `HOME` on startup, in Reading view).
- `assets/hide-template-files.css`: hides the template folders, the example module and the repo's own files
  (README, AGENTS, LICENSE, CLAUDE.md) from the file list, so the vault shows only the student's own notes.
- `assets/graph.json`: graph view preset: hides admin notes (timetable blocks, templates, digests, HOME and other hubs)
  and orphans, tighter layout, arrows, and colour groups for concepts, careers and tasks. Module colours are added per student.
- `assets/local-graph-leaf.json`: a Local graph panel for the right sidebar (two links out from the open note).
- `assets/style-settings-anuppuccin.json`: the AnuPpuccin preset (Mocha, mauve accent, card layout, depth tabs,
  floating status bar, rainbow folders, coloured headings, styled tables, custom checkboxes).

**Claude never installs plugins or themes.** The student does that in Obsidian (it downloads and runs code). Claude
only writes settings files inside the vault's `.obsidian/` folder, after the student says yes, and backs up
any file before changing it.

## 1. Install the plugins and theme (the student clicks; one click each)
Obsidian can't be installed into or configured by Claude directly: community plugins stay off until the student
turns off Restricted mode, and installs go through Obsidian's own reviewed directory. **Never download plugin or
theme files yourself.** Instead, make it one click per item:

1. **Obsidian installed and the vault open:** https://obsidian.md/download, then **Open folder as vault** → this
   workspace. Obsidian should be running with this vault open before the links below.
2. **Turn on community plugins.** It's the student's decision; explain it simply: it allows plugins from Obsidian's
   community directory. The first install link below does this for you: while Restricted mode is on, it lands on the
   Community plugins page with a button to turn it off. After they turn it off, open the same link again and it goes
   straight to the plugin. (Or: Settings → Community plugins → **Turn on community plugins**.)
3. **Open each install page.** If you can run commands on their computer, open the links one at a time (macOS
   `open "<link>"`, Windows `start "" "<link>"`, Linux `xdg-open "<link>"`), waiting for them to press
   **Install** then **Enable** (for the theme: **Install and use**) before the next. Otherwise give them the links to click.

   | Item | Link | For |
   |---|---|---|
   | Spaced Repetition | `obsidian://show-plugin?id=obsidian-spaced-repetition` | flashcards (`create-flashcards`) |
   | Full Calendar Remastered | `obsidian://show-plugin?id=full-calendar-remastered` | timetable, HOME's week agenda |
   | Style Settings | `obsidian://show-plugin?id=obsidian-style-settings` | applies the theme preset |
   | Homepage | `obsidian://show-plugin?id=homepage` | opens HOME on startup |
   | AnuPpuccin (theme) | `obsidian://show-theme?name=AnuPpuccin` | the Catppuccin look |

   If a link doesn't open the page (older Obsidian), fall back to Settings → Community plugins → Browse, or
   Appearance → Themes → Manage, and search by name.
4. Check it worked: each plugin has a folder in `.obsidian/plugins/<id>/` and is listed in
   `.obsidian/community-plugins.json`, and `.obsidian/appearance.json` has `"cssTheme": "AnuPpuccin"`. Ask them to
   finish anything that's missing. They can keep another theme if they prefer: the dashboard works with any, and
   only the preset below is skipped.

## 2. Apply the settings (after they confirm)
Check what's installed (`.obsidian/plugins/<id>/manifest.json`, `.obsidian/themes/`, `.obsidian/appearance.json`),
then, backing up each existing file to `<file>.bak` first:
1. **Dashboard snippet:** copy `assets/dashboard.css` to `.obsidian/snippets/dashboard.css`, and add `"dashboard"`
   to `enabledCssSnippets` in `.obsidian/appearance.json`, keeping existing entries and settings.
2. **Theme preset** (only if AnuPpuccin is the theme and Style Settings is installed): if
   `.obsidian/plugins/obsidian-style-settings/data.json` doesn't exist, copy the preset there. If it exists, the
   student has their own settings: ask first, and merge only the keys they want.
3. **Reading view by default:** set `"defaultViewMode": "preview"` in `.obsidian/app.json` (merge, keep the
   other keys). Pages open as dashboards; Cmd/Ctrl+E switches a page to editing.
4. **Full Calendar:** in `.obsidian/plugins/full-calendar-remastered/data.json` (it exists once the plugin has
   been enabled), set `"weatherHide": true`. Otherwise an unconfigured weather widget fills every day header. (If
   they'd rather have forecasts, set `weatherCity` instead, e.g. "Bath".) Also add a **Deadlines** calendar to
   `calendarSources` unless one already points at `timetable/deadlines`:
   `{"type": "local", "name": "Deadlines", "color": "#ef4444", "id": "local_<next free number>", "directory":
   "timetable/deadlines", "template": "", "taskCompletionStyle": "datetime"}`. Then run
   `python3 .claude/skills/create-study-timetable/scripts/sync_deadlines.py` from the workspace root to fill it:
   each dated assessment shows in red in the calendar's all-day row. Change nothing else.
5. **HOME:** if `HOME.md` isn't at the workspace root, copy `projects/_template/HOME.md` there. Delete the cards for
   features they haven't set up, plus header pills pointing at pages that don't exist yet (the note at the bottom of the
   template lists them), and remove that note.
6. **Homepage plugin** (required: without it Obsidian reopens whatever was last open, not HOME). Check it's
   installed **and enabled** (`"homepage"` is in `.obsidian/community-plugins.json`); if not, send them back to its
   install link. Then write `.obsidian/plugins/homepage/data.json`: if it doesn't exist, copy
   `assets/homepage.json`; if it does (the plugin writes its own defaults, which point at "Home"), set these keys
   under `homepages["Main Homepage"]` from the asset and keep the rest: `kind: "File"`, `value: "HOME"`,
   `openOnStartup: true`, `openMode`, `view`. `HOME.md` must exist at the root (step 5).
   **Also turn off Spaced Repetition's note review panel on startup:** set `"enableNoteReviewPaneOnStartup": false`
   in `.obsidian/plugins/obsidian-spaced-repetition/data.json` (under `settings` if that key exists). Otherwise that
   panel takes focus in the right sidebar as Obsidian starts, and Homepage opens HOME there, leaving the main area
   empty. Flashcard review (the Flashcards button in the left ribbon) isn't affected.
7. **Graph view:** start from `assets/graph.json`, keeping any colour groups the student already has. Add one
   colour group per module folder, `path:projects/<CODE>`, before the careers and tasks groups, using these colours
   in order (convert the hex to the decimal `rgb` value): `#F76B15`, `#E54666`, `#8E4EC6`, `#3E63DD`, `#12A594`,
   `#46A758`, `#E2A336`, `#D6409F`, `#0090FF`, `#978365`. Drop filters for folders that don't exist. Write it to
   `.obsidian/graph.json`.
8. **Tidy the file list:** the templates, example module and repo files have to stay (skills copy from the
   `_template/` folders, and git updates them), so hide them rather than delete them. **Never delete them.**
   - Copy `assets/hide-template-files.css` to `.obsidian/snippets/` and add `"hide-template-files"` to
     `enabledCssSnippets` in `appearance.json`. This hides them in the file list.
   - Add them to `userIgnoreFilters` in `.obsidian/app.json` (merge, keep existing entries): `projects/_template/`,
     `tasks/_template/`, `careers/_template/`, `projects/EXAMPLE-MA30001-linear-algebra/`, `README.md`,
     `AGENTS.md`, `LICENSE`, `CLAUDE.md`. This hides them from search, the graph and link suggestions.
   Tell the student they can see them again by turning off the snippet.
9. **Local graph sidebar:** in `.obsidian/workspace.json`, put the leaf from `assets/local-graph-leaf.json` (give it a
   fresh 16-hex-digit `id`, and copy the module colour groups into its `options.colorGroups`) first in the right
   sidebar's tab group, make it the current tab, and set `"collapsed": true`, so Obsidian opens on just HOME and the
   graph is one click away. Remove any note (`markdown`) leaf in the right sidebar: it's a stray copy of HOME.
   Obsidian re-adds its own panels (Backlinks, Outline) as tabs behind the graph on startup. That's fine, because the
   graph stays in front. Skip this step
   if the student would rather keep their sidebar as it is. The sidebar is collapsible (icon at top right).

Then ask them to **reload Obsidian**: Cmd/Ctrl+P → "Reload app without saving". Plugins read their settings at
startup. Warn them not to open those plugins' settings before reloading, or the plugin may save over the file.
Obsidian also rewrites `workspace.json` and `graph.json` as it runs, so for steps 7–9 either use "Reload app without
saving" straight after writing, or ask the student to quit Obsidian first (the safest option).

The graph only becomes useful once notes link by idea rather than by folder. `create-flashcards` offers
**concept notes** for that (`concepts/`, one note per theorem, method or proof technique, linked to every module
it appears in). Mention it.

## 3. Calendar sources (the student does this in Full Calendar's settings)
- **Add calendar → Full Note** → folder `timetable/blocks` (once a study timetable exists).
- The red **Deadlines** calendar (`timetable/deadlines`) is already added by step 4. It's generated from the
  assessment notes, so students change dates there, not by dragging deadlines in the calendar.
- **Add calendar → ICS** → their university timetable's subscribe link. It's read-only and refreshes by itself.
  The link is private, so it goes only into the plugin, never into a note or chat.

## 4. Check
Ask for a screenshot of HOME. It should show a gradient header with pill links, cards with coloured icon labels,
no title or Properties box at the top, and inline tables without toolbars. If it still shows pencil icons, the
snippet isn't enabled (Settings → Appearance → CSS snippets → dashboard). Reading view looks best.
Then the graph view (Cmd/Ctrl+G): each module in its own colour, and no timetable blocks or orphans. The file
list shows no `_template` folders, example module or README.

Finally, check HOME opens by itself: ask them to **quit Obsidian completely and reopen it**. ("Reload app" isn't
the same as a cold start.) If another note opens, or HOME appears in the right sidebar with an empty main
area, check in order: Homepage is enabled (`community-plugins.json`); its `data.json` has `kind: "File"`,
`value: "HOME"` and `openOnStartup: true`; Spaced Repetition's `enableNoteReviewPaneOnStartup` is false; there's no
note (`markdown`) leaf in the right sidebar of `workspace.json`; and `HOME.md` exists at the root.

## Undo
Every changed file has a `.bak` next to it. To remove the look, turn off the snippet and restore the backups.
