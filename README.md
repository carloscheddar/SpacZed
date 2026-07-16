# Zed Spacemacs Keymap

Spacemacs / [VSpaceCode](https://github.com/VSpaceCode/VSpaceCode)-style **Space leader** keybindings for [Zed](https://zed.dev), with vim mode and which-key.

Built on ideas from [wangfenjin/zed](https://github.com/wangfenjin/zed), expanded toward VSpaceCode / Doom-style menus, and tuned so leader prefixes like `SPC f` wait for the full chord instead of opening the file finder after a timeout.

> Not full Spacemacs, Doom, or VSpaceCode. Zed has no Evil layer and no major-mode (`SPC m`) menus. This is a practical Spacemacs-style keymap on top of Zed’s vim mode and native actions.

## Features

- **~330 Space-leader chords** across buffers, windows, files, project, git, search, debug, text, tasks, and UI toggles
- Vim mode + native which-key discovery
- **Magit via [gitu](https://github.com/altsem/gitu)** — `SPC g g` opens a Magit-inspired TUI in the center pane
- Magit-inspired bindings in Zed’s native Git panel (`SPC g s`) as a lightweight fallback
- VSpaceCode-style aliases where Zed has a matching action (file copy variants, debug, tasks, layouts, etc.)
- Fixes for Zed pitfalls:
  - `SPC f` (and similar) nulled as **prefixes** so they do not time out into file finder
  - Main context avoids `!menu` so which-key does not hide Spacemacs chords
  - Actions that require input (e.g. `vim::PushFindForward`) are bound with the required `[name, input]` form

## Requirements

- Zed with vim mode
- Recent Zed build with `which_key` settings support
- [gitu](https://github.com/altsem/gitu) on your `PATH` (for Magit status)

```bash
# macOS
brew install gitu

# other platforms: https://github.com/altsem/gitu/blob/master/docs/installing.md
```

## Installation

1. Back up your existing config if you have one:
   - macOS / Linux: `~/.config/zed/`
   - Windows: `%APPDATA%\Zed\`
2. Copy (or merge) the files from this repo:

```bash
# macOS / Linux example
cp keymap.json ~/.config/zed/keymap.json
cp tasks.json ~/.config/zed/tasks.json

# Magit-friendly gitu keys (discard on `x`; see gitu-config.toml)
mkdir -p ~/.config/gitu
cp gitu-config.toml ~/.config/gitu/config.toml

# Merge settings: at minimum enable vim_mode + which_key (see settings.json)
```

3. Restart Zed (or reload the keymap).

### Minimal settings

Use [`settings.json`](settings.json) as a starting point, or merge these keys into yours:

```json
{
  "vim_mode": true,
  "which_key": {
    "enabled": true,
    "delay_ms": 300
  },
  "relative_line_numbers": true,
  "git_panel": {
    "dock": "right"
  }
}
```

Do **not** replace a personalized `settings.json` wholesale unless you intend to.

## Quick reference

| Chord | Action |
|-------|--------|
| `SPC SPC` | Command palette |
| `SPC /` | Project search |
| `SPC '` | Terminal |
| `SPC TAB` | Alternate file |
| `SPC f f` | Find file |
| `SPC f s` | Save |
| `SPC f e d` | Open keymap file |
| `SPC f y Y` | Copy relative path |
| `SPC p f` | Find file in project |
| `SPC p p` | Recent projects |
| `SPC p t` | Project panel |
| `SPC p y` | Copy relative path (project) |
| `SPC b b` | Buffer / tab switcher |
| `SPC b d` | Close buffer |
| `SPC w /` | Split right |
| `SPC w h/j/k/l` | Focus pane |
| `SPC g g` | **gitu** (Magit-like status) |
| `SPC g s` | Native Git panel |
| `SPC g b` | Blame |
| `SPC s s` | Search in file |
| `SPC s j` | Outline (symbols) |
| `SPC e l` | Diagnostics |
| `SPC d d` | Start debugger |
| `SPC j j` | Helix jump-to-word (labels; closest to Doom avy) |
| `SPC j f` | vim `f` — find next char |
| `SPC j s` | vim sneak — find next 2-char sequence |
| `SPC j i` | Outline (symbols) |
| `SPC l d` | Close window / layout |
| `SPC a i` | Agent panel |
| `SPC q q` | Close window |
| `SPC : :` | Task picker (Spawn) |
| `SPC : .` | Rerun last task |
| `SPC : R` | Rerun with fresh file/context |

### Menus (second key after `SPC`)

| Key | Menu |
|-----|------|
| `:` | Tasks |
| `a` | Agent |
| `b` | Buffers |
| `c` | Comments / code |
| `d` | Debug |
| `e` | Errors |
| `f` | Files |
| `g` | Git |
| `h` | Help |
| `i` | Insert |
| `j` | Jump |
| `l` | Layouts |
| `p` | Project |
| `q` | Quit |
| `r` | Resume / recent |
| `s` | Search / symbol |
| `t` | Toggles |
| `w` | Windows |
| `x` | Text |
| `z` | Zoom / fold |
| `D` (`shift-d`) | Diff |
| `F` (`shift-f`) | Frame |
| `S` (`shift-s`) | Show panels |
| `T` (`shift-t`) | UI toggles |

### Selected menu details

**Files (`SPC f`)** — find/save/open, open keymap/settings (`SPC f e *`), copy path variants (`SPC f y *`), open with system (`SPC f L`), new terminal (`SPC f T`).

**Project (`SPC p`)** — find file, recent projects, project panel, copy relative path (`SPC p y`), add folder, remote projects.

**Buffers (`SPC b`)** — switch/close/scratch, pin (`SPC b t` / `SPC b T`), restore (`SPC b R`), copy buffer (`SPC b Y`), move to splits.

**Git (`SPC g`)** — gitu status (`SPC g g`), native panel (`SPC g s`), blame/branch/diff/stage/push/pull/fetch/worktree/hunks.

**Debug (`SPC d`)** — start/continue/step/stop, panel focus, breakpoint toggle/unset/enable (`SPC d b *`).

**Jump (`SPC j`)** — Helix word-jump labels (`SPC j j` / `SPC j w`; closest to Doom avy / VS Code Jumpy), vim `f`/`F` (`SPC j f`/`F`), sneak (`SPC j s`/`S`), outline, go to definition/refs. Zed has no full avy/EasyMotion char labels yet.

**Text (`SPC x`)** — join/case/sort/indent/rewrap/code actions.

**Tasks (`SPC :`)** — spawn picker (`SPC : :` / `SPC : s`), rerun last (`SPC : .` / `SPC : r`), rerun with fresh context (`SPC : R`). Zed has no build/test/configure task types, and which-key cannot show task names for `task::Spawn` yet ([zed#46348](https://github.com/zed-industries/zed/issues/46348)).

### Magit via gitu (`SPC g g`)

Opens [gitu](https://github.com/altsem/gitu) in the center pane (see [`tasks.json`](tasks.json)).

Install Magit-friendly overrides from [`gitu-config.toml`](gitu-config.toml) to `~/.config/gitu/config.toml` (maps discard to Magit `x`; default gitu uses `K` only).

> which-key shows `Spawn` for `task::Spawn` bindings ([zed#46348](https://github.com/zed-industries/zed/issues/46348)); custom labels are not supported yet.

Magit-like keys inside gitu:

| Key | Action |
|-----|--------|
| `s` / `u` | Stage / unstage (file, hunk, or line) |
| `ctrl-j` / `ctrl-k` | Move by line within a hunk (`j`/`k` move by hunk) |
| `x` / `K` | Discard (requires [`gitu-config.toml`](gitu-config.toml) for `x`) |
| `c c` | Commit |
| `c a` | Amend |
| `P` / `F` | Push / pull menus |
| `b b` | Checkout branch |
| `l l` | Log |
| `r` | Rebase menu |
| `h` | Help |
| `q` | Quit (closes the Zed task pane) |

Commit messages use `zed --wait` via `GIT_EDITOR` / `VISUAL` in the task env.

### Native Git panel (`SPC g s`)

Lightweight Magit-ish chords when the built-in panel is focused:

| Key | Action |
|-----|--------|
| `tab` | Diff |
| `c c` | Commit |
| `c a` | Amend |
| `b b` | Branches |
| `s` / `S` | Toggle staged / stage all |
| `P u` / `F u` | Push / pull |
| `f f` | Fetch |
| `q` / `esc` | Close panel |

## Known gaps vs Spacemacs / Doom / VSpaceCode

- No full avy / EasyMotion / Jumpy (labeled jump-to-*any*-char); closest is Helix word jump (`SPC j j`)
- No `SPC m` major-mode / localleader menus (language-specific trees)
- Many VS Code–only VSpaceCode commands have no Zed equivalent (skipped rather than faked)
- Some chords are **aliases** of nearby Zed actions (best-effort parity, not 1:1 Spacemacs behavior)
- which-key shows action names (not Spacemacs `+File` labels); `task::Spawn` always shows as Spawn (so the task menu only lists distinct actions: Spawn / Rerun)
- Vim mode ≠ Evil (no full Evil text objects / ex command ecosystem)

## Troubleshooting

**`SPC f` opens “Search project files” after ~1s**  
A complete `space f` binding is winning (often Zed’s default). This repo nulls `space f` in the editor context and under `!Editor && !Terminal`. Keep those nulls if you fork the keymap.

**which-key only shows `e` under `SPC f`**  
Avoid `!menu` on the main Spacemacs context. This repo uses `Editor && VimControl && !VimWaiting`.

**Keymap errors like “requires input data via [name, input]”**  
Some vim actions (e.g. `vim::PushFindForward`) need an input object. See `SPC j f` in [`keymap.json`](keymap.json) for the correct form.

**Space does nothing in insert mode**  
Expected — leader bindings are for normal/visual (vim) modes.

**`SPC g g` fails / “gitu: command not found”**  
Install gitu (`brew install gitu`) and ensure it is on Zed’s `PATH`. Copy [`tasks.json`](tasks.json) to `~/.config/zed/tasks.json`.

## Syncing from a live config

If you maintain bindings in `~/.config/zed/` and want to refresh this repo:

```bash
cp ~/.config/zed/keymap.json ./keymap.json
cp ~/.config/zed/tasks.json ./tasks.json
cp ~/.config/gitu/config.toml ./gitu-config.toml   # if you customize gitu
# Re-check settings.json stays minimal (no personal agent/theme keys)
# Keep README.md in sync when adding/removing chords
```

## Credits

- [wangfenjin/zed](https://github.com/wangfenjin/zed) — Spacemacs-for-Zed starter
- [VSpaceCode](https://github.com/VSpaceCode/VSpaceCode) — menu mnemonics
- [Doom Emacs](https://github.com/doomemacs/doomemacs) — leader / localleader conventions
- [gitu](https://github.com/altsem/gitu) — Magit-inspired Git TUI
- [Zed](https://zed.dev) — vim mode + which-key + tasks

## License

MIT — see [LICENSE](LICENSE).
