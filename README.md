# SpacZed

*(pronounced “spaced”)*

**Spacemacs-style Space leader for [Zed](https://zed.dev).**

Bringing the magic of [Spacemacs](https://github.com/syl20bnr/spacemacs), [Doom Emacs](https://github.com/doomemacs/doomemacs), and [VSpaceCode](https://github.com/VSpaceCode/VSpaceCode) to Zed — Space as your command center, which-key discovery, and Magit-flavored git — on top of Zed’s vim mode and native actions.

## Features

- **~330 Space-leader chords** across buffers, windows, files, project, git, search, debug, text, tasks, and UI toggles
- Vim mode + native which-key discovery
- **Workspace-safe Space chords** in empty panes and project/git/debug/outline/markdown panels; Terminal uses **Space** on alt screen (gitu) / vi-mode, else **`alt-space`**
- **Generated keymap** from a single bindings source
- **Magit via [gitu](https://github.com/altsem/gitu)** — `SPC g g` — plus Magit-inspired chords in Zed’s native Git panel (`SPC g s`)
- VSpaceCode-style menu coverage where Zed has a matching action

## Quick install

1. Back up `~/.config/zed/` (Windows: `%APPDATA%\Zed\`).
2. Copy `keymap.json` and `tasks.json` into that directory; merge [settings.json](settings.json) (at least `vim_mode` + `which_key`).
3. Optional Magit status: install [gitu](https://github.com/altsem/gitu), then copy `gitu-config.toml` → `~/.config/gitu/config.toml`.
4. Restart Zed (or reload the keymap).

Full steps, requirements, and settings details: **[docs/installation.md](docs/installation.md)**.

## Documentation

| Doc | Contents |
|-----|----------|
| [Installation](docs/installation.md) | Requirements, backup, copy/merge, minimal settings |
| [Keybindings](docs/keybindings.md) | Quick reference, menus, selected menu details |
| [Git & Magit](docs/git-and-magit.md) | gitu (`SPC g g`), native Git panel, commit chords |
| [Contributing](docs/contributing.md) | Edit bindings sources, regenerate `keymap.json` |
| [Troubleshooting](docs/troubleshooting.md) | Common setup issues and known gaps vs Spacemacs / Doom / VSpaceCode |

## Credits / Inspiration

SpacZed is not affiliated with or endorsed by these projects. Thanks to:

- [Spacemacs](https://github.com/syl20bnr/spacemacs) — Space leader menus and mnemonics
- [Doom Emacs](https://github.com/doomemacs/doomemacs) — leader conventions; avy-style jump expectations
- [VSpaceCode](https://github.com/VSpaceCode/VSpaceCode) — VS Code menu layout and chord aliases
- [Magit](https://github.com/magit/magit) — Git UX patterns (`SPC g`, `C-c C-c` / `C-c C-k`, discard `x`)
- [gitu](https://github.com/altsem/gitu) — Magit-inspired TUI used for `SPC g g`
- [Helix](https://helix-editor.com/) — word-jump labels behind `SPC j j` / `SPC j w`
- [Zed](https://zed.dev) — vim mode, which-key, tasks, and native Git panel
- [wangfenjin/zed](https://github.com/wangfenjin/zed) — related earlier Spacemacs-for-Zed experiment (incomplete; not a dependency of SpacZed)

## License

MIT — see [LICENSE](LICENSE).
