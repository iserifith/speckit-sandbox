"""Behavioural tests for greet.py (issue #23).

Covers the three required behaviours from specs/001-cli-greeting-tool/spec.md:
default greeting, --name personalisation, and --shout uppercasing, plus the
contracted error handling (invalid args -> stderr usage message, exit code 2).

Runs with the stdlib runner (`python3 -m unittest`) or pytest — no installs.
"""

import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GREET = REPO_ROOT / "greet.py"


def run_greet(*args):
    """Invoke `python3 greet.py <args>` and return the CompletedProcess."""
    return subprocess.run(
        [sys.executable, str(GREET), *args],
        capture_output=True,
        text=True,
    )


class DefaultGreetingTests(unittest.TestCase):
    def test_default_greeting_prints_hello_world(self):
        result = run_greet()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Hello, world!\n")
        self.assertEqual(result.stderr, "")


class NameOptionTests(unittest.TestCase):
    def test_name_personalises_greeting(self):
        result = run_greet("--name", "Ada")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Hello, Ada!\n")

    def test_name_with_spaces_used_verbatim(self):
        result = run_greet("--name", "Ada Lovelace")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Hello, Ada Lovelace!\n")


class ShoutFlagTests(unittest.TestCase):
    def test_shout_uppercases_default_greeting(self):
        result = run_greet("--shout")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "HELLO, WORLD!\n")

    def test_shout_composes_with_name(self):
        result = run_greet("--name", "Ada", "--shout")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "HELLO, ADA!\n")


class InvalidArgumentTests(unittest.TestCase):
    def test_unknown_option_exits_2_with_stderr_usage(self):
        result = run_greet("--bogus")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertNotEqual(result.stderr, "")

    def test_missing_name_value_exits_2_with_stderr_usage(self):
        result = run_greet("--name")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertNotEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
