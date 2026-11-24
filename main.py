#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting our own AI agent.

Entry: "My agent spent 3 million tokens writing one sentence about a
cat, then asked if it was OK to press Enter."
"""

import os

LINE = "My agent spent 3 million tokens writing one sentence about a cat, then asked if it was OK to press Enter."


def validate(text):
    """Mirror the bounty gate: 1-200 chars, UTF-8, not only whitespace,
    one single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if text != text.strip():
        raise ValueError("entry has leading or trailing padding")
    if not text:
        raise ValueError("entry is empty")
    if text.isspace():
        raise ValueError("entry is only whitespace")
    if len(text) > 200:
        raise ValueError("entry is over 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be one line")
    text.encode("utf-8").decode("utf-8")  # real UTF-8 round-trip check
    return True


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
