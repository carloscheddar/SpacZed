#!/usr/bin/env python3
"""Generate keymap.json for SpacZed (pronounced "spaced").

Reads scripts/spacemacs_bindings.json + static_contexts.json. Zed has no way to
share one binding table across multiple contexts, so we keep a single source of
truth and emit the duplicated editor / non-editor blocks.

Usage (from repo root):
  python3 scripts/generate_keymap.py
  python3 scripts/generate_keymap.py --check   # exit 1 if keymap.json is stale
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BINDINGS_PATH = Path(__file__).resolve().parent / "spacemacs_bindings.json"
STATIC_PATH = Path(__file__).resolve().parent / "static_contexts.json"
OUT_PATH = ROOT / "keymap.json"

HEADER = """\
// SpacZed (pronounced "spaced") — Spacemacs / VSpaceCode-style keymap for Zed
//
// Inspired by Spacemacs, Doom Emacs, and VSpaceCode menus.
// Space is the leader in vim normal/visual; enable which_key in settings.json.
//
// GENERATED FILE — do not edit by hand.
// Source: scripts/spacemacs_bindings.json + scripts/static_contexts.json
// Regenerate: python3 scripts/generate_keymap.py
//
// Important: single-key prefixes like `space f` are null so they stay pure
// prefixes (otherwise Zed times out ~1s and runs a short binding).
// Editor Spacemacs leader is normal/visual only — not insert (so Space inserts).
// AgentPanel is excluded from the non-editor Space set so thread typing works.
// Non-editor panes (Terminal/gitu, panels, Markdown preview) get workspace-safe
// chords only (soft wrap / vim motions / folds stay editor-only).
"""


def load_json(path: Path):
    return json.loads(path.read_text())


def action_name(value) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return value[0]
    return str(value)


def prefix_nulls(keys: set[str]) -> dict[str, None]:
    """Null every strict prefix of a multi-key Space chord."""
    nulls: dict[str, None] = {"space": None}
    for key in keys:
        parts = key.split()
        if not parts or parts[0] != "space":
            continue
        for n in range(1, len(parts)):
            pref = " ".join(parts[:n])
            if pref not in keys:
                nulls[pref] = None
    return nulls


def sort_bindings(bindings: dict) -> dict:
    """Stable, readable key order: null prefixes first (by depth), then leaves."""

    def sort_key(item):
        k, v = item
        parts = k.split()
        is_null = v is None
        return (0 if is_null else 1, len(parts), k)

    return dict(sorted(bindings.items(), key=sort_key))


def build_editor_bindings(data: dict) -> dict:
    leaves = {}
    leaves.update(data["workspace"])
    leaves.update(data["editor_only"])
    bindings = {}
    bindings.update(prefix_nulls(set(leaves)))
    for k in data.get("editor_extra_prefix_nulls") or []:
        if k not in leaves:
            bindings[k] = None
    # Null unbound close aliases so Zed defaults cannot steal the prefix chord.
    for k in ("space w q",):
        if k not in leaves:
            bindings[k] = None
    bindings.update(leaves)
    bindings.update(data.get("editor_misc") or {})
    return sort_bindings(bindings)


def build_non_editor_bindings(data: dict) -> dict:
    leaves = dict(data["workspace"])
    leaves.update(data.get("non_editor_overrides") or {})
    leaves.update(data.get("non_editor_extra") or {})
    bindings = {}
    bindings.update(prefix_nulls(set(leaves)))
    bindings.update(leaves)
    return sort_bindings(bindings)


def build_keymap(data: dict, static: list) -> list:
    editor_ctx = data["meta"]["editor_context"]
    non_editor_ctx = data["meta"]["non_editor_context"]

    editor_block = {
        "context": editor_ctx,
        "bindings": build_editor_bindings(data),
    }
    non_editor_block = {
        "context": non_editor_ctx,
        "bindings": build_non_editor_bindings(data),
    }

    # Insert generated non-editor block before the Terminal extras / panels.
    out = [editor_block]
    inserted = False
    for block in static:
        ctx = block.get("context")
        if not inserted and ctx in (
            "Terminal",
            "ProjectPanel && not_editing",
            "GitPanel",
        ):
            out.append(non_editor_block)
            inserted = True
        out.append(block)
    if not inserted:
        out.append(non_editor_block)
    return out


def render(keymap: list) -> str:
    body = json.dumps(keymap, indent=2)
    return HEADER + "\n" + body + "\n"


def strip_comments(text: str) -> str:
    out: list[str] = []
    i = 0
    ins = False
    esc = False
    while i < len(text):
        c = text[i]
        if ins:
            out.append(c)
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                ins = False
            i += 1
            continue
        if c == '"':
            ins = True
            out.append(c)
            i += 1
            continue
        if c == "/" and i + 1 < len(text) and text[i + 1] == "/":
            while i < len(text) and text[i] != "\n":
                i += 1
            continue
        out.append(c)
        i += 1
    return "".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check keymap.json matches generation without writing",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=OUT_PATH,
        help="Output path (default: repo keymap.json)",
    )
    args = parser.parse_args()

    data = load_json(BINDINGS_PATH)
    static = load_json(STATIC_PATH)
    keymap = build_keymap(data, static)
    rendered = render(keymap)

    if args.check:
        if not args.output.exists():
            print(f"missing {args.output}", file=sys.stderr)
            return 1
        current = args.output.read_text()
        # Compare parsed JSON so comment/header drift alone does not fail check
        # after intentional header edits — still require exact render for --check
        if current != rendered:
            print(f"{args.output} is stale; run: python3 scripts/generate_keymap.py", file=sys.stderr)
            return 1
        print(f"{args.output} is up to date")
        return 0

    args.output.write_text(rendered)
    # sanity parse
    json.loads(strip_comments(rendered))
    n_ed = sum(1 for k, v in keymap[0]["bindings"].items() if k.startswith("space") and v)
    ne = next(b for b in keymap if "MarkdownPreview" in b.get("context", ""))
    n_ne = sum(1 for k, v in ne["bindings"].items() if k.startswith("space") and v)
    print(f"Wrote {args.output}")
    print(f"  editor Space leaves: {n_ed}")
    print(f"  non-editor Space leaves: {n_ne}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
