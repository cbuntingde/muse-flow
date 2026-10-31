"""Check that test and regression logs exist and are non-empty. Stdlib only."""
import argparse
import pathlib
import sys


def check(path_str: str, label: str) -> None:
    path = pathlib.Path(path_str)
    if not path.is_file():
        print(f"missing {label}: {path}")
        raise SystemExit(1)
    if path.stat().st_size == 0:
        print(f"empty {label}: {path}")
        raise SystemExit(1)
    print(f"ok {label}: {path} ({path.stat().st_size} bytes)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify review evidence logs.")
    parser.add_argument("--test-log", required=True)
    parser.add_argument("--regression-log", required=True)
    args = parser.parse_args()
    check(args.test_log, "test log")
    check(args.regression_log, "regression log")
    print("evidence complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
