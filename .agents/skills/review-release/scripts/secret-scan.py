"""Scan files for likely secret patterns. Exits 1 on any hit. Stdlib only."""
import argparse
import pathlib
import re
import sys

PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"(?i)\b(password|passwd|secret)\s*[:=]\s*\S+"),
    re.compile(r"(?i)\b(api[_-]?key|api[_-]?secret)\s*[:=]\s*\S+"),
    re.compile(r"xox[bap]-"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan files for secrets.")
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()
    hits = 0
    for name in args.files:
        path = pathlib.Path(name)
        if not path.is_file():
            print(f"skip (not a file): {name}")
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            print(f"unreadable {name}: {exc}")
            hits += 1
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for pattern in PATTERNS:
                if pattern.search(line):
                    print(f"HIT {name}:{lineno}: {pattern.pattern[:32]}...")
                    hits += 1
                    break
    if hits:
        print(f"{hits} potential secret(s) found")
        return 1
    print("no secrets detected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
