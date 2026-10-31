"""Focused tests for the review-release and record-decide gate scripts.

Run from the repo root:  python -m unittest discover tests
Stdlib only: unittest, subprocess, tempfile.
"""

import pathlib
import subprocess
import sys
import tempfile
import unittest

REVIEW = (
    pathlib.Path(__file__).resolve().parent.parent
    / "plugins"
    / "muse-flow"
    / "skills"
    / "review-release"
    / "scripts"
)
SECRET_SCAN = REVIEW / "secret-scan.py"
CHECK_EVIDENCE = REVIEW / "check-evidence.py"
APPEND_DECISION = (
    pathlib.Path(__file__).resolve().parent.parent
    / "plugins"
    / "muse-flow"
    / "skills"
    / "record-decide"
    / "scripts"
    / "append-decision.py"
)


def run(script: pathlib.Path, *args: str, cwd=None):
    return subprocess.run(
        [sys.executable, str(script), *args],
        capture_output=True,
        text=True,
        cwd=cwd,
    )


class SecretScanTest(unittest.TestCase):
    def test_clean_file_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = pathlib.Path(tmp) / "notes.md"
            target.write_text("# notes\nnothing sensitive here\n", encoding="utf-8")
            proc = run(SECRET_SCAN, str(target))
        self.assertEqual(proc.returncode, 0)
        self.assertIn("no secrets", proc.stdout)

    def test_key_value_secret_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = pathlib.Path(tmp) / "config.txt"
            target.write_text('api_key = "AKIAIOSFODNN7EXAMPLE"\n', encoding="utf-8")
            proc = run(SECRET_SCAN, str(target))
        self.assertEqual(proc.returncode, 1)
        self.assertIn("HIT", proc.stdout)

    def test_missing_path_is_skipped_not_failed(self):
        proc = run(SECRET_SCAN, "does-not-exist.txt")
        self.assertEqual(proc.returncode, 0)
        self.assertIn("skip", proc.stdout)


class CheckEvidenceTest(unittest.TestCase):
    def _logs(self, tmp: str, test_body: str | None, reg_body: str | None):
        base = pathlib.Path(tmp)
        test_log, reg_log = base / "test.log", base / "regression.log"
        if test_body is not None:
            test_log.write_text(test_body, encoding="utf-8")
        if reg_body is not None:
            reg_log.write_text(reg_body, encoding="utf-8")
        return run(
            CHECK_EVIDENCE,
            "--test-log",
            str(test_log),
            "--regression-log",
            str(reg_log),
        )

    def test_missing_log_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = self._logs(tmp, "pass", None)
        self.assertEqual(proc.returncode, 1)
        self.assertIn("missing", proc.stdout)

    def test_empty_log_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = self._logs(tmp, "pass", "")
        self.assertEqual(proc.returncode, 1)
        self.assertIn("empty", proc.stdout)

    def test_two_nonempty_logs_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = self._logs(tmp, "3 passed", "1 regression checked")
        self.assertEqual(proc.returncode, 0)
        self.assertIn("evidence complete", proc.stdout)


class AppendDecisionTest(unittest.TestCase):
    def test_creates_log_with_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = str(pathlib.Path(tmp) / "DECISIONS.md")
            proc = run(
                APPEND_DECISION,
                "--choice",
                "Ship controls in bundle",
                "--options",
                "bundle vs repo-local",
                "--rationale",
                "installers need them",
                "--log",
                log,
            )
            self.assertEqual(proc.returncode, 0)
            text = pathlib.Path(log).read_text(encoding="utf-8")
        self.assertIn("# Decisions", text)
        self.assertIn("Ship controls in bundle", text)
        self.assertIn("Owner: unassigned", text)

    def test_second_run_appends(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = str(pathlib.Path(tmp) / "DECISIONS.md")
            for choice in ("first", "second"):
                proc = run(
                    APPEND_DECISION,
                    "--choice",
                    choice,
                    "--options",
                    "a vs b",
                    "--rationale",
                    "r",
                    "--owner",
                    "cbuntingde",
                    "--log",
                    log,
                )
                self.assertEqual(proc.returncode, 0)
            text = pathlib.Path(log).read_text(encoding="utf-8")
        self.assertIn("first", text)
        self.assertIn("second", text)
        self.assertIn("Owner: cbuntingde", text)


if __name__ == "__main__":
    unittest.main()
