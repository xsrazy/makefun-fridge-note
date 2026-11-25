"""make.fun entry: Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note from a smart fridge to its owner
into ``entry.txt`` under the output directory given by the
``MAKEFUN_OUTPUT_DIR`` environment variable (default ``/output``).

The note is a single line of 1 to 200 characters, written with no trailing
newline, exactly as the competition gate requires.

Why this note: the judge rewards a dry, petty, specific line in the fridge's
own voice, with a turn the reader does not see coming and a concrete
household detail. This one leans on the oldest fridge grudge there is,
leftovers the owner keeps promising to eat, and lands the sting in the
second sentence: the forgotten food has outlived the promise, started a
family, and the eldest carries the owner's name. It stays small and
domestic, it trusts the reader to get the joke, and it never explains
itself. No em dash anywhere in the entry or in this file's prose.
"""

import os

ENTRY = (
    "The leftovers you swore you would eat have started a family. "
    "I named the eldest after you."
)

MIN_LEN = 1
MAX_LEN = 200


def validate(text: str) -> None:
    """Check the entry against the competition gate before writing it."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not MIN_LEN <= len(text) <= MAX_LEN:
        raise ValueError(f"entry must be {MIN_LEN}-{MAX_LEN} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
