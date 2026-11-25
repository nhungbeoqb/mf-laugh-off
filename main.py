#!/usr/bin/env python3
"""One-Line Laugh-Off entry: a Roomba that knows too much.

Writes exactly one funny line to /output/entry.txt. Pure Python 3
standard library; deterministic — the line is fixed text.
"""

import os

LINE = (
    "My Roomba has mapped my apartment, my habits, and "
    "\u2014 judging by the wall it keeps ramming \u2014 my childhood."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
