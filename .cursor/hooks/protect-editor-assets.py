#!/usr/bin/env python3
"""Editor-asset guard: blocks agent text edits to editor-owned asset files.

These files hold object relationships and identifiers that blind text edits
break — change them in the engine editor (or through an editor MCP) instead.

Covered engines (edit BLOCKED to port):
  Godot:  *.import, .godot/
  Unreal: *.uasset, *.umap
  Unity:  *.unity, *.prefab, *.meta
"""

import json
import re
import sys

BLOCKED = re.compile(r"(\.(uasset|umap|unity|prefab|meta|import)$)|((^|/)\.godot/)")


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # Fail open: never brick unrelated edits on malformed input.
        print(json.dumps({"permission": "allow"}))
        return

    tool_input = data.get("tool_input") or {}
    path = ""
    for key in ("file_path", "path", "target_file", "target_notebook"):
        value = tool_input.get(key)
        if isinstance(value, str) and value:
            path = value
            break

    if path and BLOCKED.search(path):
        print(
            json.dumps(
                {
                    "permission": "deny",
                    "user_message": (
                        f"Blocked: {path} is an editor-owned asset. "
                        "Make this change in the engine editor or through an editor MCP, not as a text edit."
                    ),
                    "agent_message": (
                        "A project hook blocked this edit: the target is an editor-owned asset file. "
                        "Do not edit it as text. Ask the user to make the change in the engine editor, "
                        "or use an editor MCP integration, and list the exact configuration steps instead."
                    ),
                }
            )
        )
        return

    print(json.dumps({"permission": "allow"}))


if __name__ == "__main__":
    main()
