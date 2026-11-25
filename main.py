#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Deterministic, stdlib-only, offline. Writes exactly one line of text
(no trailing newline) to /output/entry.txt, or to $ENTRY_PATH if set.
"""

import os

JOKE = "I replied-all asking to be removed from the thread, and now I'm cc'd on three more."

OUTPUT_PATH = os.environ.get("ENTRY_PATH", "/output/entry.txt")


def main() -> None:
    path = OUTPUT_PATH
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
