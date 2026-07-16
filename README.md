# Zed Spacemacs Keymap

Spacemacs / [VSpaceCode](https://github.com/VSpaceCode/VSpaceCode)-style **Space leader** keybindings for [Zed](https://zed.dev), with vim mode and which-key.

Built on ideas from [wangfenjin/zed](https://github.com/wangfenjin/zed), expanded toward VSpaceCode menus, and tuned so leader prefixes like `SPC f` wait for the full chord instead of opening the file finder after a timeout.

> Not full Spacemacs or VSpaceCode. Zed has no Evil layer and no major-mode (`SPC m`) menus. This is a practical Spacemacs-style keymap on top of Zed’s vim mode.

## Features

- ~260 Space-leader chords (buffers, windows, files, project, git, search, debug, …)
- Vim mode + native which-key discovery
- Magit-inspired bindings in the Git panel
- Fixes for Zed pitfalls:
  - `SPC f` (and similar) nulled as **prefixes** so they do not time out into file finder
  - Main context avoids `!menu` so which-key does not hide Spacemacs chords

## Requirements

- Zed with vim mode
- Recent Zed build with `which_key` settings support

## Installation

1. Back up your existing config if you have one:
   - macOS / Linux: `~/.config/zed/`
   - Windows: `%APPDATA%\Zed\`
2. Copy (or merge) the files from this repo:

```bash
# macOS / Linux example
cp keymap.json ~/.config/zed/keymap.json

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
| `SPC p f` | Find file in project |
| `SPC p p` | Recent projects |
| `SPC p t` | Project panel |
| `SPC b b` | Buffer / tab switcher |
| `SPC b d` | Close buffer |
| `SPC w /` | Split right |
| `SPC w h/j/k/l` | Focus pane |
| `SPC g s` | Git panel |
| `SPC g b` | Blame |
| `SPC s s` | Outline (symbols) |
| `SPC e l` | Diagnostics |
| `SPC d d` | Start debugger |
| `SPC a i` | Agent panel |
| `SPC q q` | Close window |

### Menus (second key after `SPC`)

| Key | Menu |
|-----|------|
| `b` | Buffers |
| `w` | Windows |
| `f` | Files |
| `p` | Project |
| `g` | Git |
| `s` | Search / symbol |
| `e` | Errors |
| `c` | Comments / code |
| `d` | Debug |
| `j` | Jump |
| `t` | Toggles |
| `q` | Quit |
| `a` | Agent |
| `x` | Text |
| `z` | Zoom / fold |
| `:` | Tasks |

### Git panel (Magit-ish)

With the git panel focused:

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

## Known gaps vs Spacemacs / VSpaceCode

- No `SPC m` major-mode bindings
- Weak / missing `SPC l` layouts
- Many VS Code–only VSpaceCode commands have no Zed equivalent
- which-key shows action names (not Spacemacs `+File` labels)
- Vim mode ≠ Evil

## Troubleshooting

**`SPC f` opens “Search project files” after ~1s**  
A complete `space f` binding is winning (often Zed’s default). This repo nulls `space f` in the editor context and under `!Editor && !Terminal`. Keep those nulls if you fork the keymap.

**which-key only shows `e` under `SPC f`**  
Avoid `!menu` on the main Spacemacs context. This repo uses `Editor && VimControl && !VimWaiting`.

**Space does nothing in insert mode**  
Expected — leader bindings are for normal/visual (vim) modes.

## Syncing from a live config

If you maintain bindings in `~/.config/zed/keymap.json` and want to refresh this repo:

```bash
cp ~/.config/zed/keymap.json ./keymap.json
# Re-check settings.json stays minimal (no personal agent/theme keys)
```

## Credits

- [wangfenjin/zed](https://github.com/wangfenjin/zed) — Spacemacs-for-Zed starter
- [VSpaceCode](https://github.com/VSpaceCode/VSpaceCode) — menu mnemonics
- [Zed](https://zed.dev) — vim mode + which-key

## License

MIT — see [LICENSE](LICENSE).
