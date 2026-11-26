#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers -- make.fun entry.

Writes one fortune-cookie line for a software engineer to entry.txt:
a single line of at most 120 characters, byte-exact and deterministic
on every run. Standard library only.
"""

import os

# The fortune, written for this entry in this session. Lucky numbers are
# the classic fortune-cookie closer; here they are HTTP status codes plus
# one the engineer invented themself at 2 a.m. -- the twist lands last.
# Verified: 73 characters, 1 line, well under the 120-character limit.
LINE = "Your lucky numbers are 200, 404, and the error code you made up at 2 a.m."

MAX_CHARS = 120


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry must not be empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit("entry is %d chars, over the 120 limit" % len(line))

    # No trailing newline: the file's byte count is the line's char count.
    text = line
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    # Also leave a copy beside this script when that directory is
    # writable, so a local run can be inspected without touching the
    # graded output. A read-only script directory must never fail the run.
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w",
                  encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    except OSError:
        pass


if __name__ == "__main__":
    main()
