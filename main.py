"""Write the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os
from pathlib import Path

from entry import ENTRY


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry must be 1-280 characters, got {len(text)}"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")

    written = out_path.read_bytes()
    if not written:
        raise SystemExit(f"wrote no bytes to {out_path}")
    if not 1 <= len(written) <= 280:
        raise SystemExit(f"wrote {len(written)} characters to {out_path}, expected 1-280")

    print(len(text))


if __name__ == "__main__":
    main()
