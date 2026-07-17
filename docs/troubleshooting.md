# SpacZed — Troubleshooting

[← README](../README.md)

## Common issues

**`SPC g g` fails / “gitu: command not found”**  
Install [gitu](https://github.com/altsem/gitu) (`brew install gitu` on macOS) and ensure it is on Zed’s `PATH`. Copy [`tasks.json`](../tasks.json) to `~/.config/zed/tasks.json`. See [Installation](installation.md).

**Opening a file from gitu freezes on `zed --wait …`**  
Show/open must not use `--wait`. SpacZed’s [`tasks.json`](../tasks.json) sets `VISUAL`/`EDITOR`/`GITU_SHOW_EDITOR` to `zed` and only `GIT_EDITOR` to `zed --wait`. Re-copy `tasks.json` and restart the gitu task if an older env still has `--wait` on `VISUAL`.

**Leader chords do nothing**  
Confirm [settings](installation.md#minimal-settings): `vim_mode` is on, `which_key` is enabled, and [`keymap.json`](../keymap.json) is installed. You must be in vim **normal** or **visual** mode — Space inserts text in insert mode (including the Agent thread). Press Escape, then `SPC …`.

**Space opens which-key in the terminal**  
Plain Space is intentionally *not* a leader in Terminal (so shells can type spaces). Use **`alt-space`** for workspace-safe chords there. If which-key still steals Space, reload/reinstall the generated [`keymap.json`](../keymap.json) (older builds bound Space as leader in Terminal).

**Soft wrap / truncate does nothing inside gitu**  
gitu draws its own UI in the terminal; Zed editor soft-wrap toggles cannot change it ([gitu#277](https://github.com/altsem/gitu/issues/277)). Use `SPC t l` / `alt-z` in editor buffers instead.

**which-key shows `Spawn` instead of task names**  
Zed does not support custom which-key labels for `task::Spawn` yet ([zed#46348](https://github.com/zed-industries/zed/issues/46348)). `SPC : :` still opens the task picker.

**Chords clash after merging with your own keymap**  
If you merge SpacZed into an existing `keymap.json`, a personal or default binding can override a Space chord. Prefer SpacZed’s generated file as the base, then add your extras in separate context blocks. When editing SpacZed itself, change the sources and regenerate — see [Contributing](contributing.md).

## Platform limits

These are Zed / ecosystem limits SpacZed works around or maps as closely as possible — not bugs in the shipped keymap:

- No full avy / EasyMotion / Jumpy (jump-to-any-char labels); closest is Helix word jump (`SPC j j`)
- No `SPC m` major-mode / localleader trees (Zed has no Evil major-mode layer)
- Some VSpaceCode / Spacemacs commands have no Zed action yet (skipped rather than faked)
- which-key shows Zed action names, not Spacemacs-style `+File` group labels
- Vim mode ≠ full Evil (text objects / ex ecosystem differ)

## See also

- [Installation](installation.md)
- [Keybindings](keybindings.md)
- [Git & Magit](git-and-magit.md)
- [Contributing](contributing.md)
