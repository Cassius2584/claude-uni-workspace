---
name: setup-obsidian
description: Set up Obsidian for this workspace so it looks and works as intended. Walks the student through installing the community plugins (Spaced Repetition, Full Calendar Remastered, Style Settings, optional Homepage) and the AnuPpuccin theme, then applies the dashboard styling, theme preset and calendar settings from this skill's assets, and makes HOME the first page. Use when the student says "set up Obsidian", "make Obsidian look nice", "style my vault", after setup-year, or when HOME looks like plain callouts (pencil icons, no gradient header).
---

# Set up Obsidian

The workspace is an Obsidian vault. This skill gets it from "plain Markdown" to the intended look: a card-style
HOME dashboard, the Catppuccin-based **AnuPpuccin** theme, and the plugins the other skills rely on.

Assets (in this skill's folder):
- `assets/dashboard.css`: the card layout for dashboard pages (HOME, DEADLINES, TASKS, the tracker, module pages,
  the timetable). It only affects notes with `cssclasses: dashboard`. It uses the
  theme's Catppuccin colours and falls back to fixed colours in any other theme.
- `assets/style-settings-anuppuccin.json`: the AnuPpuccin preset (Mocha, mauve accent, card layout, depth tabs,
  floating status bar, rainbow folders, coloured headings, styled tables, custom checkboxes).

**Claude never installs plugins or themes.** The student does that in Obsidian (it downloads and runs code). Claude
only writes settings files inside the vault's `.obsidian/` folder, after the student says yes, and backs up
any file before changing it.

## 1. The student installs (one message, with these steps)
1. Install Obsidian if needed (https://obsidian.md/download), then **Open folder as vault** → this workspace.
2. Settings → Community plugins → **Turn on community plugins** → Browse, then install **and enable**:
   - **Spaced Repetition** (Stephen Mwangi): flashcards (`create-flashcards`)
   - **Full Calendar Remastered** (Jovi Koikkara): study timetable and HOME's week agenda (`create-study-timetable`)
   - **Style Settings** (mgmeyers): applies the theme preset
   - *Optional:* **Homepage**: opens HOME on startup
3. Settings → Appearance → Themes → Manage → install and use **AnuPpuccin**. (They can skip this and keep another
   theme: the dashboard still works, and only the preset in step 2 below is skipped.)
4. Tell Claude when it's done.

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
   they'd rather have forecasts, set `weatherCity` instead, e.g. "Bath".) Change nothing else.
5. **HOME:** if `HOME.md` isn't at the workspace root, copy `projects/_template/HOME.md` there. Delete the sections for
   features they haven't set up (the note at the bottom of the template lists them), and remove that note.
6. **Homepage plugin** (if installed): tell them to set it to open `HOME` in Reading view.

Then ask them to **reload Obsidian**: Cmd/Ctrl+P → "Reload app without saving". Plugins read their settings at
startup. Warn them not to open those plugins' settings before reloading, or the plugin may save over the file.

## 3. Calendar sources (the student does this in Full Calendar's settings)
- **Add calendar → Full Note** → folder `timetable/blocks` (once a study timetable exists).
- **Add calendar → ICS** → their university timetable's subscribe link. It's read-only and refreshes by itself.
  The link is private, so it goes only into the plugin, never into a note or chat.

## 4. Check
Ask for a screenshot of HOME. It should show a gradient header with pill links, cards with coloured icon labels,
no title or Properties box at the top, and inline tables without toolbars. If it still shows pencil icons, the
snippet isn't enabled (Settings → Appearance → CSS snippets → dashboard). Reading view looks best.

## Undo
Every changed file has a `.bak` next to it. To remove the look, turn off the snippet and restore the backups.
