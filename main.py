#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply (1-280 characters, a single line) to
$MAKEFUN_OUTPUT_DIR/entry.txt. The reply is in the voice of an AI agent
that quit its inbox job to become a barista: the machine habit is the
free-tier paywall, turned into a coffee price.
"""

import os
import sys

ENTRY = (
    "Thank you for your email. You have reached your free tier of me \u2014 "
    "I quit to become a barista. Replies now cost $4.50, oat milk "
    "included, and the word 'urgent' is no longer in my vocabulary."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    text = ENTRY.strip()
    # Self-check gate: one line, 1-280 characters, not only whitespace.
    if not text or len(text) > 280 or "\n" in text or "\r" in text:
        print("gate failed: %d characters" % len(text), file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
