#!/usr/bin/env python3
"""Texts From Your Future Self — make.fun entry.

Writes one funny text message from the writer's future self to
/output/entry.txt. Deterministic: the same line on every run.
Standard library only, no network, no secrets.
"""

import os

ENTRY = (
    "Future you here. Stop watering the plant — it's plastic. "
    "And the password you just changed? You'll forget it by Thursday. "
    "I know. I'm you. I forgot it twice already."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    # A single trailing newline is fine: the gate counts 1-200 characters
    # and the file is 166 characters including it.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
