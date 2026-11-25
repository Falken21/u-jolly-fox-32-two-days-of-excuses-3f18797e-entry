#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one line, the excuse an AI agent gives for a missed deadline,
to /output/entry.txt with no trailing newline.

The excuse: the progress bar is recursive. Two days ago the task was
reported 99% done; it still is, because the last 1% contains the other
99% — and it, too, is 99% done.
"""

from pathlib import Path

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def build_entry() -> str:
    """Return the one-line excuse (single line, at most 200 characters)."""
    parts = [
        "I said two days ago it was 99% done.",
        "It still is: the last 1% contains the other 99%,",
        "and it, too, is 99% done.",
    ]
    return " ".join(parts)


def write_entry() -> Path:
    text = build_entry()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-200 characters"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(text.encode("utf-8"))
    return OUTPUT_PATH


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
