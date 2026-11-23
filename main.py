#!/usr/bin/env python3
"""The One-Line Laugh — writes exactly one funny line to /output/entry.txt."""

import os

LINE = "I deleted social media to be more productive, and now I stare into my fridge with the same intensity."


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(LINE))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
