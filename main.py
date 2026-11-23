"""Make the Judge Smile — one warm line about a small good thing today.

Writes the entry line to entry.txt inside the output directory
(``MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``).
Standard library only, deterministic, no network access.
"""

import os

LINE = (
    "This morning the bus driver waited ten extra seconds for a limping "
    "old man, then tapped his horn twice like a hello, and the whole "
    "bus grinned."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition's line rules.

    A valid entry is a non-empty, single line of at most 200 Unicode
    code points, with real content (not just whitespace) and no
    trailing newline — the file must contain exactly the line.
    """
    if not isinstance(line, str):
        raise TypeError("line must be a str")
    if not line:
        raise ValueError("line must not be empty")
    if not line.strip():
        raise ValueError("line must contain more than whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes ({len(LINE)} characters) to {path}")


if __name__ == "__main__":
    main()
