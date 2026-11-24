#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — make.fun bounty entry.

Writes exactly one line — an alien tourist's review of Earth — to
/output/entry.txt (no trailing newline).
"""

import hashlib
import os

LINE = (
    "Two days on Earth: the locals apologise to furniture, queue for fun, "
    "and drink hot bean water to stay awake, then complain they can't sleep. "
    "4/5 \u2014 would abduct again."
)
# Why this line fits the brief: a first-person alien-observer review of
# two days on Earth, built on concrete ordinary details only an outsider
# would notice (apologising to furniture, queuing for fun, drinking hot
# bean water to stay awake and then complaining about not sleeping), with
# a real review verdict (4/5) and the punch landing at the end.
# One joke, one line, no traffic/gravity/money/weather cliche.

OUTPUT = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def validate(raw: bytes) -> str:
    """Check the written file against the bounty gate; return its text."""
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert text == LINE, "entry does not equal the expected line"
    # Exactly one line: no newline anywhere, not just no trailing one.
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    # No trailing newline: the file must be exactly the line.
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert len(raw) == len(text.encode("utf-8")), "byte length mismatch"
    # It reads as a review: it carries a verdict (a rating) in the line.
    assert "4/5" in text, "entry carries no review verdict"
    return text


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT) or ".", exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open(OUTPUT, "rb") as f:
        raw = f.read()
    text = validate(raw)
    print("sha256:", hashlib.sha256(raw).hexdigest())
    print("chars:", len(text))


if __name__ == "__main__":
    main()
