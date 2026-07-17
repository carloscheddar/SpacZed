# SpacZed — Installation

[← README](../README.md)

## Requirements

- [Zed](https://zed.dev) with vim mode
- Recent Zed build with `which_key` settings support
- [gitu](https://github.com/altsem/gitu) on your `PATH` (optional; for Magit-style status via `SPC g g`)

```bash
# macOS
brew install gitu

# other platforms: https://github.com/altsem/gitu/blob/master/docs/installing.md
```

## Install

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

See [Git & Magit](git-and-magit.md) for gitu usage and Magit-inspired chords.

## Minimal settings

Use [`settings.json`](../settings.json) as a starting point, or merge these keys into yours:

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

## Next steps

- [Keybindings](keybindings.md) — chord reference and menus
- [Troubleshooting](troubleshooting.md) — common setup issues
