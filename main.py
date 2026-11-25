"""The Excuse My Agent Gave Me -- make.fun bounty entry.

Writes one line: the excuse an AI agent gives its human for missing a
deadline, to /output/entry.txt (override with the ENTRY_OUTPUT
environment variable, or pass a path as argv[1]).

Python standard library only. No network, no input files: the line is
baked into this file.

The joke: the agent hallucinated a deadline extension, then treated its
own hallucination as an official document. Straight-faced apology,
machine condition (hallucination), punch in the last three words.
"""

import os
import sys

ENTRY = (
    "Apologies: I hallucinated a deadline extension, got it in writing "
    "from myself, and believed me."
)

MAX_CHARS = 200


def validate_entry(text: str) -> str:
    """Enforce the gate's rules on the entry before it is written."""
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "ENTRY_OUTPUT", "/output/entry.txt"
    )
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %d characters to %s" % (len(text), out_path))


if __name__ == "__main__":
    main()
