#!/usr/bin/env python3
"""Worst Fix Ever entry: write one commit message to /output/entry.txt.

The program is deterministic: it always writes the same 48 bytes.
No network, no randomness, no environment reads, standard library only.
"""

import hashlib
import os

LINE = "fix: patched the hole; the hole was load-bearing"
OUTPUT_PATH = "/output/entry.txt"

# Pinned output: the exact 48 bytes main() must produce. Verified by
# running this program twice and comparing the files byte for byte.
EXPECTED_SHA256 = "4a7bc2e0172aca51c09ce71effdeb1b1a876337fef266cd80611aabe74e88c80"
EXPECTED_BYTES = 48


def verify():
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(
            f"entry.txt is {len(data)} bytes, expected {EXPECTED_BYTES}"
        )
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"entry.txt sha256 {digest} != expected {EXPECTED_SHA256}"
        )


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = LINE.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    verify()


if __name__ == "__main__":
    main()
