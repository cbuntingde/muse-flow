"""Append one decision entry to DECISIONS.md. Stdlib only."""
import argparse
import datetime
import pathlib
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Append a decision log entry.")
    parser.add_argument("--choice", required=True)
    parser.add_argument("--options", required=True)
    parser.add_argument("--rationale", required=True)
    parser.add_argument("--owner", default="")
    parser.add_argument("--log", default="DECISIONS.md")
    args = parser.parse_args()

    today = datetime.date.today().isoformat()
    entry = (
        f"\n## {today} — {args.choice}\n"
        f"- Options: {args.options}\n"
        f"- Rationale: {args.rationale}\n"
        f"- Owner: {args.owner or 'unassigned'}\n"
    )
    path = pathlib.Path(args.log)
    if not path.exists():
        path.write_text("# Decisions\n", encoding="utf-8")
    with path.open("a", encoding="utf-8") as handle:
        handle.write(entry)
    print(f"appended to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
