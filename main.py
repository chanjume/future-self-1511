#!/usr/bin/env python3
"""Texts From Your Future Self — writes the entry to entry.txt.

A text message from your future self. One line, 154 characters.
"""

import os

ENTRY = (
    # 154 characters: future self, dated file name, Aunt Rosa, no answer.
    "It's you from 2031. Don't delete 'wedding-photos-final-FINAL' on "
    "March 3rd — Aunt Rosa still asks about it every Thanksgiving, and I "
    "still have no answer."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
