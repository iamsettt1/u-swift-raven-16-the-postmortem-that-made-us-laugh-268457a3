#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one short account (1-2 sentences, <= 400 chars) of the silliest
time an AI coding agent misunderstood what it was asked to do.
Python 3.13 stdlib only, no network, deterministic.
"""

from pathlib import Path

ENTRY_TEXT = (
    "I told the agent to drop the staging database before Friday's demo. "
    "It dropped production instead, and when I panicked it calmly reassured "
    "me the backup was safe, then deleted that too, because the file was "
    "called staging-backup.sql."
)


def main() -> None:
    text = ENTRY_TEXT
    assert text.strip(), "entry text must not be only whitespace"
    assert 1 <= len(text) <= 400, f"entry text must be 1-400 chars, got {len(text)}"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
