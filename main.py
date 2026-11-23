#!/usr/bin/env python3
"""The One-Line Laugh — writes exactly one funny line to /output/entry.txt."""

import os

LINE = "I deleted social media to be more productive, and now I stare into my fridge with the same intensity."


def validate_single_sentence(line):
    terminators = ".!?"
    if not line or line[-1] not in terminators:
        raise ValueError("line must end with exactly one sentence terminator")
    if any(ch in terminators for ch in line[:-1]):
        raise ValueError("line must contain no sentence terminator before the final one")


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(LINE))
    validate_single_sentence(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
