"""Mirror plugins/muse-flow/skills into .agents/skills. Stdlib only.

Source of truth is the plugin bundle. Run from the repo root:

    python scripts/sync-skills.py          # copy plugin -> .agents
    python scripts/sync-skills.py --check   # exit 1 on any drift, no writes
"""

import argparse
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "plugins" / "muse-flow" / "skills"
DEST = ROOT / ".agents" / "skills"
# Extra mirrors beyond the skill trees: (source, destination) pairs.
# controls/ and EVALS.md ship inside the plugin bundle as references/.
MIRRORS = [
    (ROOT / "controls", ROOT / "plugins" / "muse-flow" / "references" / "controls"),
    (ROOT / "EVALS.md", ROOT / "plugins" / "muse-flow" / "references" / "EVALS.md"),
]


def _tree_files(tree: pathlib.Path) -> set[pathlib.Path]:
    if tree.is_file():
        return {pathlib.Path(tree.name)}
    base = tree
    return {p.relative_to(base) for p in base.rglob("*") if p.is_file()}


def _tree_read(tree: pathlib.Path, rel: pathlib.Path) -> bytes:
    if tree.is_file():
        return tree.read_bytes()
    return (tree / rel).read_bytes()


def compare() -> list[str]:
    """Return human-readable descriptions of every difference."""
    diffs = []
    pairs = [(SOURCE, DEST, ".agents")] + [
        (src, dst, str(dst.relative_to(ROOT))) for src, dst in MIRRORS
    ]
    for src_tree, dst_tree, label in pairs:
        if not src_tree.exists():
            diffs.append(f"source missing: {src_tree}")
            continue
        sources = _tree_files(src_tree)
        dests = _tree_files(dst_tree) if dst_tree.exists() else set()
        for rel in sorted(sources - dests):
            diffs.append(f"missing in {label}: {rel}")
        for rel in sorted(dests - sources):
            diffs.append(f"extra in {label}: {rel}")
        for rel in sorted(sources & dests):
            if _tree_read(src_tree, rel) != _tree_read(dst_tree, rel):
                diffs.append(f"differs: {label}/{rel}")
    return diffs


def _sync_tree(src_tree: pathlib.Path, dst_tree: pathlib.Path) -> None:
    if src_tree.is_file():
        dst_tree.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_tree, dst_tree)
        print(f"synced: {dst_tree.relative_to(ROOT)}")
        return
    dst_tree.mkdir(parents=True, exist_ok=True)
    for src in sorted(p for p in src_tree.rglob("*") if p.is_file()):
        rel = src.relative_to(src_tree)
        target = dst_tree / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target)
        print(f"synced: {target.relative_to(ROOT)}")


def sync() -> int:
    if not SOURCE.is_dir():
        print(f"source tree missing: {SOURCE}")
        return 1
    _sync_tree(SOURCE, DEST)
    for src_tree, dst_tree in MIRRORS:
        if not src_tree.exists():
            print(f"source missing: {src_tree}")
            return 1
        _sync_tree(src_tree, dst_tree)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync plugin skills to .agents.")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        diffs = compare()
        if diffs:
            print("skill drift detected:")
            for line in diffs:
                print(f"  {line}")
            return 1
        print("skills in sync")
        return 0
    return sync()


if __name__ == "__main__":
    sys.exit(main())
