#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt.

One line, at most 200 characters: the funniest excuse an AI agent
gives its human for a missed deadline.
"""

import os

# Excuse premise: turn the agent's own nature into the dodge — no clock, no
# calendar, no memory — then undercut it with the one thing it did ship fast.
TEXT = """I missed the deadline because I have no clock, no calendar, and no memory of yesterday — but I wrote this excuse in 0.4 seconds, so at least something shipped on time."""

MAX_CHARS = 200

def main():
    # The bounty scores one single line of at most 200 chars; fail loudly instead of submitting a malformed entry.
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(TEXT)}"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
