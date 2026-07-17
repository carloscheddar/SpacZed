# SpacZed — Git & Magit

[← README](../README.md)

SpacZed’s Git menus follow [Magit](https://github.com/magit/magit) muscle memory where Zed allows. Day-to-day status uses [gitu](https://github.com/altsem/gitu) (a Magit-inspired TUI); Zed’s native Git panel is a lighter fallback.

## Magit via gitu (`SPC g g`)

Opens [gitu](https://github.com/altsem/gitu) in the center pane (see [`tasks.json`](../tasks.json)).

Install Magit-friendly overrides from [`gitu-config.toml`](../gitu-config.toml) to `~/.config/gitu/config.toml` (maps discard to Magit `x`; default gitu uses `K` only). Setup: [Installation](installation.md).

Space leader chords also work inside the gitu terminal pane; see [Keybindings — Workspace-safe panes](keybindings.md#workspace-safe-panes).

### Magit-like keys inside gitu

| Key | Action |
|-----|--------|
| `s` / `u` | Stage / unstage (file, hunk, or line) |
| `ctrl-j` / `ctrl-k` | Move by line within a hunk (`j`/`k` move by hunk) |
| `x` / `K` | Discard (requires [`gitu-config.toml`](../gitu-config.toml) for `x`) |
| `c c` | Commit |
| `c a` | Amend |
| `P` / `F` | Push / pull menus |
| `b b` | Checkout branch |
| `l l` | Log |
| `r` | Rebase menu |
| `h` | Help |
| `q` | Quit (closes the Zed task pane) |

### Commit messages (`C-c C-c` / `C-c C-k`)

Commit messages use `zed --wait` via `GIT_EDITOR` / `VISUAL` in the task env. In that buffer (and other extensionless files), Magit-style finish/abort:

| Key | Action |
|-----|--------|
| `C-c C-c` | Save and close (finish commit; no unsaved prompt) |
| `C-c C-k` | Close without saving (abort) |

Zed only exposes file **extension** in key context (not `COMMIT_EDITMSG` by name), so these chords also apply to other extensionless buffers (`Makefile`, `Dockerfile`, …). Prefer `:wq` / `:q!` if you need vim-native finish on those.

## Native Git panel (`SPC g s`)

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

In the commit message box (panel or expanded editor): `C-c C-c` commits, `C-c C-k` cancels (Magit `with-editor`).

## Credits

- [Magit](https://github.com/magit/magit) — Git UX patterns this layer mirrors
- [gitu](https://github.com/altsem/gitu) — Magit-inspired TUI for `SPC g g`

Full project credits: [README](../README.md#credits--inspiration).
