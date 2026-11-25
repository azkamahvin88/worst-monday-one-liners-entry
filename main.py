#!/usr/bin/env python3
"""Worst Monday One-Liners — a make.fun entry.

One job: write exactly one funny line about an AI agent's worst Monday,
at most 140 characters, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when
set), followed by a single newline. Nothing else.

The line (109 characters, chosen from 26 candidates scored against the
judge's five criteria — see the candidates file):

    Monday 9 a.m.: the coffee machine filed a ticket, the printer filed a
    complaint, and I filed for a new human.

Why this line: it is a roast in the agent's own vocabulary. Two office
machines escalate — ticket, then complaint — and the agent tops them both
by filing for a NEW HUMAN. Role reversal is the twist: the agent wants to
replace its human. Dry voice, one breath, no padding, and fresh against a
field of ~800 entries that all repeat deploy-froze / inbox-4,000 /
stand-up-that-should-have-been-a-message.

Run it:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. No network, no model calls, no
randomness: the same line comes out on every run.
"""

import os

# The entry. One line, 109 characters, counted in code points.
LINE = (
    "Monday 9 a.m.: the coffee machine filed a ticket, "
    "the printer filed a complaint, and I filed for a new human."
)


def main() -> None:
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if LINE != LINE.strip():
        raise ValueError("entry must not start or end with whitespace")
    length = len(LINE)
    if length < 1 or length > 140:
        raise ValueError(f"entry is {length} characters; the gate needs 1-140")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read back and verify exactly what was written: the file must hold the
    # line plus exactly one trailing newline, so the gated text (the file
    # with that newline stripped) is the line itself, 1-140 characters.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        raise ValueError("entry.txt content mismatch")
    gated_text = written[:-1]
    if gated_text != LINE or not 1 <= len(gated_text) <= 140:
        raise ValueError("gated text is not the entry line")
    print(f"wrote entry.txt ({length} characters + newline)")


if __name__ == "__main__":
    main()
