"""Smoke-test every skill: frontmatter plus referenced script paths. Stdlib only.

Run from the repo root:

    python scripts/smoke-skills.py                 # checks plugins/muse-flow/skills
    python scripts/smoke-skills.py --root <dir>    # check any skills tree
"""

import argparse
import pathlib
import re
import sys

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
SCRIPT_REF_RE = re.compile(r"`(scripts/[A-Za-z0-9_.\-/]+)`")


def check_skill(skill_md: pathlib.Path) -> list[str]:
    errors = []
    text = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return [f"{skill_md}: missing frontmatter block"]
    front = match.group(1)
    if not re.search(r"^name:\s*\S+", front, re.MULTILINE):
        errors.append(f"{skill_md}: frontmatter missing name")
    if not re.search(r"^description:\s*\S+", front, re.MULTILINE):
        errors.append(f"{skill_md}: frontmatter missing description")
    for ref in SCRIPT_REF_RE.findall(text):
        target = skill_md.parent / ref
        if not target.is_file():
            errors.append(f"{skill_md}: referenced script missing: {ref}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-test skill definitions.")
    parser.add_argument("--root", default="plugins/muse-flow/skills")
    args = parser.parse_args()
    root = pathlib.Path(args.root)
    found = sorted(root.glob("*/SKILL.md"))
    if not found:
        print(f"no skills found under {root}")
        return 1
    errors = []
    for skill_md in found:
        skill_errors = check_skill(skill_md)
        errors.extend(skill_errors)
        status = "FAIL" if skill_errors else "ok"
        print(f"{status}: {skill_md.relative_to(root).parent}")
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for line in errors:
            print(f"  {line}")
        return 1
    print(f"\n{len(found)} skills ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
