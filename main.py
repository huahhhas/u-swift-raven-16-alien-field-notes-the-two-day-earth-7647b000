#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text — an alien tourist's review of
planet Earth — to /output/entry.txt (and to stdout, for local runs).
"""

LINE = (
    "Five stars: the locals worship glowing rectangles, queue for bitter "
    "bean water, and call it 'being productive'. Would abduct again."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
