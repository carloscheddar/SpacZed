# SpacZed — Keybindings

[← README](../README.md)

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
| `SPC t l` | Toggle soft wrap (truncate) |
| `SPC t m` | Toggle markdown preview |
| `alt-z` / `opt-z` | Toggle soft wrap (VS Code muscle memory) |
| `SPC a i` | Agent panel |
| `SPC q q` | Close window |
| `SPC : :` | Task picker (Spawn) |
| `SPC : .` | Rerun last task |
| `SPC : R` | Rerun with fresh file/context |

## Menus (second key after `SPC`)

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

## Selected menu details

**Files (`SPC f`)** — find/save/open, open keymap/settings (`SPC f e *`), copy path variants (`SPC f y *`), open with system (`SPC f L`), new terminal (`SPC f T`).

**Project (`SPC p`)** — find file, recent projects, project panel, copy relative path (`SPC p y`), add folder, remote projects.

**Buffers (`SPC b`)** — switch/close/scratch, pin (`SPC b t` / `SPC b T`), restore (`SPC b R`), copy buffer (`SPC b Y`), move to splits.

**Git (`SPC g`)** — gitu status (`SPC g g`), native panel (`SPC g s`), blame/branch/diff/stage/push/pull/fetch/worktree/hunks. Details: [Git & Magit](git-and-magit.md).

**Debug (`SPC d`)** — start/continue/step/stop, panel focus, breakpoint toggle/unset/enable (`SPC d b *`).

**Jump (`SPC j`)** — Helix word-jump labels (`SPC j j` / `SPC j w`; closest to Doom avy / VS Code Jumpy), vim `f`/`F` (`SPC j f`/`F`), sneak (`SPC j s`/`S`), outline, go to definition/refs. Zed has no full avy/EasyMotion char labels yet.

**Text (`SPC x`)** — join/case/sort/indent/rewrap/code actions.

Soft wrap / truncate: `SPC t l` or `alt-z` (`opt-z` on macOS) → `editor::ToggleSoftWrap` (Zed no longer ships this as a default).

Markdown preview: `SPC t m` opens the preview from the editor; the same chord closes the preview pane when it is focused.

**Tasks (`SPC :`)** — spawn picker (`SPC : :` / `SPC : s`), rerun last (`SPC : .` / `SPC : r`), rerun with fresh context (`SPC : R`). Zed has no build/test/configure task types, and which-key cannot show task names for `task::Spawn` yet ([zed#46348](https://github.com/zed-industries/zed/issues/46348)).

## Workspace-safe panes

The same Space leader works in Terminal (including gitu), EmptyPane/Welcome, Project panel, Git panel, Debug panel, Outline panel, and **Markdown preview** for every **workspace-safe** chord (files/projects/git/windows/tasks/toggles like `SPC t z`, docks, …). Editor-only chords (soft wrap, vim motions, format, folds, …) stay vim-editor-only. In those panes, `SPC q q` / `SPC w d` close the active pane item (handy for dismissing gitu) rather than the whole window. **Agent panel thread input is excluded** so Space inserts normally while typing.

> which-key shows `Spawn` for `task::Spawn` bindings ([zed#46348](https://github.com/zed-industries/zed/issues/46348)); custom labels are not supported yet.

## See also

- [Git & Magit](git-and-magit.md)
- [Contributing](contributing.md) — how to change chords
- [Troubleshooting](troubleshooting.md)
