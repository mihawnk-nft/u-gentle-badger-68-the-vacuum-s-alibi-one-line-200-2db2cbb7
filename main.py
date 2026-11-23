#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes one funny one-line excuse from a robot vacuum for missing a spot
to /output/entry.txt. Pure stdlib, deterministic, no network, no secrets.
"""

import os

ENTRY = (
    "Sensor log, 14:02: unidentified crumb cluster detected. "
    "I have classified it as a pet. His name is Greg. "
    "I do not vacuum Greg."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}: {line}")


if __name__ == "__main__":
    main()
