# SpacZed — Contributing

[← README](../README.md)

[`keymap.json`](../keymap.json) is **generated**. Zed has no built-in way to DRY the same chords across editor + panel + terminal contexts, so this repo keeps one source and emits those blocks. Terminal gets a hybrid: base `alt-space` leader, plus Space leader under `vi_mode` and `screen == alt`.

## Edit bindings

1. Edit [`scripts/spacemacs_bindings.json`](../scripts/spacemacs_bindings.json):
   - `workspace` — chords for editor, panels, and Terminal (via `alt-space` and Space-leader contexts)
   - `editor_only` — vim/editor actions only
   - `non_editor_overrides` / `non_editor_extra` — non-editor differences (e.g. close pane on `SPC q q`)
2. Edit [`scripts/static_contexts.json`](../scripts/static_contexts.json) for panel/Magit/`alt-z`/helix extras (including Terminal `ctrl-shift-space` → ToggleViMode).
3. Regenerate:

```bash
python3 scripts/generate_keymap.py
# optional: python3 scripts/generate_keymap.py --check
cp keymap.json ~/.config/zed/keymap.json
```

Do not hand-edit `keymap.json` and commit it without updating the sources.

## Syncing from a live config

Prefer editing [`scripts/spacemacs_bindings.json`](../scripts/spacemacs_bindings.json) and regenerating. If you copied a live keymap for a quick test:

```bash
# Do not commit a hand-edited keymap.json without updating the sources.
python3 scripts/generate_keymap.py
cp keymap.json ~/.config/zed/keymap.json
cp ~/.config/zed/tasks.json ./tasks.json
cp ~/.config/gitu/config.toml ./gitu-config.toml   # if you customize gitu
# Re-check settings.json stays minimal (no personal agent/theme keys)
# Keep docs/ in sync when adding/removing chords
```

## Docs

When you add or rename chords, update:

- [keybindings.md](keybindings.md) for the quick reference / menus
- [git-and-magit.md](git-and-magit.md) for Git-specific chords
- [troubleshooting.md](troubleshooting.md) if you hit a new Zed pitfall worth documenting
