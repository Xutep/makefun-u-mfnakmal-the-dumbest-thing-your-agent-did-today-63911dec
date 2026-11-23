#!/usr/bin/env python3
"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today".

Writes one line (128 characters) about the dumbest thing the agent did
today to /output/entry.txt. Deterministic, stdlib only: the same line
every run, byte for byte.
"""

import os

LINE = (
    "My agent spent forty minutes polishing this one-line joke, "
    "then proudly submitted it one character over the "
    "200-character limit."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
