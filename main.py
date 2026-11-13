#!/usr/bin/env python3
"""Copy the Sky Leviathan artwork to the competition entry path."""

import os
from pathlib import Path
import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Write the Sky Leviathan artwork for the competition.")
    parser.add_argument("output_dir", nargs="?", help="output directory (overrides MAKEFUN_OUTPUT_DIR)")
    args = parser.parse_args()

    asset = Path(__file__).resolve().parent / "art.jpg"
    if not asset.is_file():
        print(f"Error: required artwork asset is missing: {asset}", file=sys.stderr)
        return 1

    output_dir = Path(args.output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    destination = output_dir / "entry.png"
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        asset_size = asset.stat().st_size
        destination.write_bytes(asset.read_bytes())
        written_size = destination.stat().st_size
    except OSError as exc:
        print(f"Error: could not write artwork to {destination}: {exc}", file=sys.stderr)
        return 1

    if written_size != asset_size:
        raise OSError(
            f"Error: size mismatch after writing {destination}: "
            f"expected {asset_size} bytes, got {written_size} bytes"
        )

    print(f"Wrote {destination} ({written_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
